"""
diagnose_channel_usage.py
==========================
Stage 2 follow-up: after fixing the lr instability and the TE estimator's
finite-sample bias, the honest result was "no detected learned coupling at
any bandwidth" (see TODO.md). That's a more basic question than saturation:
is the channel dead on the *sending* side (speaker never encodes its goal
into the message), the *receiving* side (listener ignores the message it's
given), or both?

Three diagnostics, per bandwidth, on a single trained policy pair:

1. Per-bit message variance across the eval set -- do any/all bits collapse
   to a near-constant value (std ~ 0)?
2. Encoding fidelity: contemporaneous ridge-regression R^2 predicting the
   emitted message from the speaker's own input observation (its private
   goal). This is NOT the coupling-capacity question (which asks whether
   B's *history* predicts A's future) -- it's simpler: is the message even
   a function of the goal at all?
3. Dead-channel ablation: rerun frozen evaluation with the listener always
   receiving an all-zero message instead of the real one (rollout(...,
   zero_message=True)) and compare eval task return to the real-message
   condition. If performance is statistically indistinguishable, the
   listener isn't using the message regardless of what it encodes.

Usage:
    python3 diagnose_channel_usage.py --bits 1 2 8 32 128 --episodes 2000 --seed 42
"""

from __future__ import annotations
import argparse
import json
import os
from datetime import datetime

import numpy as np
import torch

from run_bandwidth_sweep import train_policies, rollout

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LOG_DIR = os.path.join(ROOT, "experiments", "results", "logs")
os.makedirs(LOG_DIR, exist_ok=True)


def _ridge_r2(Y, X, ridge=1e-6):
    """Contemporaneous R^2 of least-squares Y ~ X (with intercept), in-sample.
    Used here only as a descriptive encoding-fidelity number, not as a
    coupling-capacity estimate -- no bias correction needed for this
    diagnostic since we're not claiming a bits/step figure, just "does the
    message vary with the goal at all."
    """
    n = X.shape[0]
    Xa = np.hstack([X, np.ones((n, 1))])
    gram = Xa.T @ Xa + ridge * np.eye(Xa.shape[1])
    beta = np.linalg.solve(gram, Xa.T @ Y)
    resid = Y - Xa @ beta
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((Y - Y.mean(axis=0)) ** 2)
    return float(1.0 - ss_res / (ss_tot + 1e-12))


def diagnose_one_bandwidth(n_bits, episodes, seed, lr=5e-4, n_eval_episodes=150, episodes_per_update=1,
                            entropy_coef=0.02):
    env, speaker, listener, channel, baseline, ep_returns = train_policies(
        n_bits, episodes, seed, lr=lr, log_every=episodes,
        episodes_per_update=episodes_per_update, entropy_coef=entropy_coef)  # log only at the end

    def eval_batch(zero_message, n_eps, seed_offset):
        returns, all_messages, all_speaker_obs, all_listener_states = [], [], [], []
        for k in range(n_eps):
            _, _, _, rewards, rec = rollout(
                env, speaker, listener, channel, n_bits,
                seed=999_000 + seed * 100 + seed_offset + k,
                greedy=False, record=True, zero_message=zero_message)
            returns.append(sum(rewards))
            all_messages.append(rec["messages"])
            all_speaker_obs.append(rec["speaker_obs"])
            all_listener_states.append(rec["listener_states"])
        return (np.array(returns),
                np.concatenate(all_messages, axis=0) if n_bits > 0 else None,
                np.concatenate(all_speaker_obs, axis=0),
                np.concatenate(all_listener_states, axis=0))

    real_returns, messages, speaker_obs, listener_states = eval_batch(
        zero_message=False, n_eps=n_eval_episodes, seed_offset=0)
    zero_returns, _, _, _ = eval_batch(zero_message=True, n_eps=n_eval_episodes, seed_offset=500_000)

    if n_bits > 0:
        per_bit_std = messages.std(axis=0)
        encoding_r2 = _ridge_r2(messages, speaker_obs)
        # Receiver-side complement to the encoding-R^2 check: does the
        # listener's output distribution depend on message *content* at all,
        # holding its own observation fixed? Pair each listener state with a
        # randomly shuffled (still real, still in-distribution) message from
        # elsewhere in the eval set and measure KL(real-message dist ||
        # shuffled-message dist). Near-zero KL means the listener has learned
        # to ignore the channel regardless of what it carries.
        with torch.no_grad():
            l_obs_t = torch.tensor(listener_states, dtype=torch.float32)
            msg_t = torch.tensor(messages, dtype=torch.float32)
            rng = np.random.default_rng(seed)
            shuffle_idx = rng.permutation(len(msg_t))
            dist_real = listener(l_obs_t, msg_t)
            dist_shuf_msg = listener(l_obs_t, msg_t[shuffle_idx])
            listener_message_sensitivity_kl = float(
                torch.distributions.kl_divergence(dist_real, dist_shuf_msg).mean().item())
            # Same-run reference scale: how much does the listener's output
            # change when its OWN state varies (message held fixed)? This
            # contextualizes whether the message-sensitivity KL above is
            # "near zero" or just this policy's normal low end of sensitivity.
            shuffle_idx_state = rng.permutation(len(l_obs_t))
            dist_shuf_state = listener(l_obs_t[shuffle_idx_state], msg_t)
            listener_state_sensitivity_kl = float(
                torch.distributions.kl_divergence(dist_real, dist_shuf_state).mean().item())
    else:
        per_bit_std = np.array([])
        encoding_r2 = 0.0
        listener_message_sensitivity_kl = 0.0
        listener_state_sensitivity_kl = 0.0

    env.close()

    real_mean, real_std = float(real_returns.mean()), float(real_returns.std())
    zero_mean, zero_std = float(zero_returns.mean()), float(zero_returns.std())
    # Welch's t-test style effect size (no scipy dependency): standardized
    # mean difference using pooled eval-episode standard errors.
    se = np.sqrt(real_std ** 2 / n_eval_episodes + zero_std ** 2 / n_eval_episodes) + 1e-9
    z_stat = (real_mean - zero_mean) / se

    return {
        "n_bits": n_bits,
        "train_final_return_mean_last50": float(np.mean(ep_returns[-50:])),
        "eval_return_real_message_mean": real_mean,
        "eval_return_real_message_std": real_std,
        "eval_return_zero_message_mean": zero_mean,
        "eval_return_zero_message_std": zero_std,
        "real_vs_zero_z_stat": float(z_stat),
        "per_bit_message_std": per_bit_std.tolist(),
        "n_dead_bits_std_below_0.01": int(np.sum(per_bit_std < 0.01)) if n_bits > 0 else 0,
        "speaker_goal_to_message_encoding_r2": encoding_r2,
        "listener_message_sensitivity_kl": listener_message_sensitivity_kl,
        "listener_state_sensitivity_kl": listener_state_sensitivity_kl,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, nargs="+", default=[1, 2, 8, 32, 128])
    ap.add_argument("--episodes", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--lr", type=float, default=5e-4)
    ap.add_argument("--eval_episodes", type=int, default=150)
    ap.add_argument("--episodes_per_update", type=int, default=1)
    ap.add_argument("--entropy_coef", type=float, default=0.02)
    args = ap.parse_args()

    print("=" * 70)
    print("Stage 2 diagnostic -- is the learned channel dead on send, receive, or both?")
    print(f"bandwidths={args.bits}  episodes/bandwidth={args.episodes}  seed={args.seed}  lr={args.lr}"
          f"  episodes_per_update={args.episodes_per_update}  entropy_coef={args.entropy_coef}")
    print("=" * 70)

    results = []
    for b in args.bits:
        print(f"\n[Diagnostic] B={b} bits/step ...")
        r = diagnose_one_bandwidth(b, args.episodes, args.seed, lr=args.lr,
                                    n_eval_episodes=args.eval_episodes,
                                    episodes_per_update=args.episodes_per_update,
                                    entropy_coef=args.entropy_coef)
        print(f"   train (last 50 ep) return   = {r['train_final_return_mean_last50']:+.2f}")
        print(f"   eval return, real message   = {r['eval_return_real_message_mean']:+.2f} +/- {r['eval_return_real_message_std']:.2f}")
        print(f"   eval return, zeroed message = {r['eval_return_zero_message_mean']:+.2f} +/- {r['eval_return_zero_message_std']:.2f}"
              f"   (z = {r['real_vs_zero_z_stat']:+.2f})")
        print(f"   dead bits (std<0.01): {r['n_dead_bits_std_below_0.01']}/{b}   "
              f"speaker-goal -> message encoding R^2 = {r['speaker_goal_to_message_encoding_r2']:.3f}")
        print(f"   listener sensitivity: message-shuffle KL = {r['listener_message_sensitivity_kl']:.4f} nats"
              f"   vs. state-shuffle (reference) KL = {r['listener_state_sensitivity_kl']:.4f} nats")
        results.append(r)

    payload = {
        "timestamp": datetime.now().isoformat(),
        "author": "Ashok Pasala (VIT-AP University)",
        "experiment": "P1_stage2_channel_usage_diagnostic",
        "seed": args.seed,
        "episodes_per_bandwidth": args.episodes,
        "lr": args.lr,
        "eval_episodes": args.eval_episodes,
        "results": results,
    }
    out_path = os.path.join(LOG_DIR, f"P1_stage2_channel_diagnostic_seed{args.seed}.json")
    with open(out_path, "w") as f:
        json.dump(payload, f, indent=2, default=float)
    print(f"\nLog written -> {out_path}")


if __name__ == "__main__":
    main()

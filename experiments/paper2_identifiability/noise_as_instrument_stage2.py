"""
noise_as_instrument_stage2.py
==============================
Applies the noise-as-instrument method (validated on a linear-Gaussian toy in
noise_as_instrument.py) to a *real* system this project did not design to
make it work: the trained Stage 2 PettingZoo speaker/listener from
train_with_receiver_aux.py (the "best config" -- dual auxiliary loss,
entropy_coef=0.02, B=8 -- that produced the paper's headline ablation z=+0.50
and randomisation z=+1.82 numbers).

Method. The Gumbel-Sigmoid channel (gumbel_channel.py) injects fresh
logistic noise into the message logits on every call:
    gumbel_noise = log(u) - log(1-u),   u ~ Uniform(0,1)
independent of everything else by construction -- exactly the "exogenous
channel noise" Remark 2 of paper_main/main.tex argues qualifies as an
instrument. This script fixes the environment seed per episode (so the
goal/landmark configuration -- the analogue of the shared-convention latent
C -- is held fixed) and re-runs the *entire* episode `k_resamples` times with
independently redrawn channel noise each time (supplied externally, bypassing
torch's global RNG so it cannot leak into the listener's decoding). The
listener acts greedily, so the only source of variation across resamples of
the same episode is the channel noise itself.

This gives, per episode, several (mean message, mean injected noise, episode
return) triples sharing the same underlying goal -- pooled across episodes,
the naive regression of return on message is confounded by the goal exactly
as Theorem 1 describes, while the instrumental estimate using the noise
should recover the *causal* effect of the message on behaviour.

Ground truth to check against: this project already knows the answer for
this system, established independently via direct intervention (ablation
and randomisation, in evaluate() from train_with_receiver_aux.py) -- a
small, non-zero effect capturing at most ~12% of the value of the goal
information. This script does not look for a new number; it checks whether
a completely different estimation route (instrumental variables on organic
channel noise) agrees with what direct intervention already established.

Usage:
    python3 noise_as_instrument_stage2.py --episodes 20000 --iv_episodes 150 --k_resamples 20
"""

from __future__ import annotations
import argparse
import json
import os
import sys
from datetime import datetime

import numpy as np
import torch

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PAPER1_RL_DIR = os.path.join(ROOT, "experiments", "paper1_rl")
sys.path.insert(0, PAPER1_RL_DIR)
from train_with_receiver_aux import train_policies_dual_aux, evaluate  # noqa: E402

LOG_DIR = os.path.join(ROOT, "experiments", "results", "logs")
PLOT_DIR = os.path.join(ROOT, "experiments", "results", "plots")
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(PLOT_DIR, exist_ok=True)


def gumbel_channel_forward_with_noise(logits, tau, noise_u):
    """Reimplements GumbelBinaryChannel's forward math but takes the uniform
    noise draw as an explicit external argument instead of sampling from
    torch's global RNG -- so the instrument (the noise) is fully under our
    control and provably independent of the goal, the listener's action
    sampling, and everything else. gumbel_channel.py itself is untouched."""
    u = noise_u.clamp(1e-6, 1 - 1e-6)
    gumbel_noise = torch.log(u) - torch.log1p(-u)
    y_soft = torch.sigmoid((logits + gumbel_noise) / tau)
    y_hard = (y_soft > 0.5).float()
    message = y_hard + (y_soft - y_soft.detach())
    return message, gumbel_noise


def rollout_with_injected_noise(env, speaker, listener, n_bits, tau, env_seed, noise_rng):
    """One full episode. The environment seed fixes the goal/landmark layout
    (the shared-convention analogue C); the channel noise is drawn from an
    independent, externally supplied RNG on every step; the listener acts
    greedily so the only source of trajectory variation across resamples of
    the same env_seed is the injected channel noise."""
    obs, _ = env.reset(seed=env_seed)
    speaker_id = [a for a in env.agents if a.startswith("speaker")][0]
    listener_id = [a for a in env.agents if a.startswith("listener")][0]

    rewards = []
    msg_sum = torch.zeros(n_bits)
    noise_sum = torch.zeros(n_bits)
    steps = 0
    speaker_noop = None

    with torch.no_grad():
        while env.agents:
            s_obs = torch.tensor(obs[speaker_id], dtype=torch.float32)
            l_obs = torch.tensor(obs[listener_id], dtype=torch.float32)

            msg_logits = speaker(s_obs)
            noise_u = torch.tensor(noise_rng.uniform(size=n_bits), dtype=torch.float32)
            message, gumbel_noise = gumbel_channel_forward_with_noise(msg_logits, tau, noise_u)

            dist = listener(l_obs, message)
            action = dist.probs.argmax()  # greedy: removes action-sampling stochasticity as a confound

            if speaker_noop is None:
                speaker_noop = env.action_space(speaker_id).sample() * 0
            actions = {speaker_id: int(speaker_noop), listener_id: int(action.item())}
            next_obs, reward, terminations, truncations, _ = env.step(actions)

            rewards.append(float(reward[listener_id]))
            msg_sum += message.detach()
            noise_sum += gumbel_noise.detach()
            steps += 1

            obs = next_obs
            if all(terminations.values()) or all(truncations.values()):
                break

    U = sum(rewards)
    M = (msg_sum / max(steps, 1)).numpy()
    N = (noise_sum / max(steps, 1)).numpy()
    return U, M, N


def collect_iv_dataset(env, speaker, listener, n_bits, tau, n_episodes, k_resamples, base_seed):
    rows = []
    for ep in range(n_episodes):
        env_seed = 7_000_000 + base_seed * 10_000 + ep  # fixes the goal (C) for this episode
        for k in range(k_resamples):
            noise_rng = np.random.default_rng(base_seed * 1_000_000 + ep * 1000 + k)
            U, M, N = rollout_with_injected_noise(env, speaker, listener, n_bits, tau, env_seed, noise_rng)
            rows.append({"episode": ep, "resample": k, "U": U,
                         "M_mean": float(np.mean(M)), "N_mean": float(np.mean(N))})
    return rows


def cov(x, y):
    return float(np.cov(x, y, ddof=1)[0, 1])


def var(x):
    return float(np.var(x, ddof=1))


def naive_ols(M, U):
    return cov(M, U) / var(M)


def iv_estimate(M, U, N):
    return cov(U, N) / cov(M, N)


def first_stage_f_stat(M, N):
    n = len(N)
    beta = cov(M, N) / var(N)
    alpha = np.mean(M) - beta * np.mean(N)
    resid = M - (alpha + beta * N)
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((M - np.mean(M)) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    dof = n - 2
    return float((r2 / (1 - r2)) * dof) if r2 < 1 else float("inf")


def bootstrap_ci(M, U, N, estimator, n_boot=1000, seed=0):
    rng = np.random.default_rng(seed)
    n = len(M)
    vals = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        vals.append(estimator(M[idx], U[idx], N[idx]) if estimator is iv_estimate
                     else estimator(M[idx], U[idx]))
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, default=8)
    ap.add_argument("--episodes", type=int, default=20000, help="training episodes for the base policy")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--entropy_coef", type=float, default=0.02)
    ap.add_argument("--iv_episodes", type=int, default=150, help="distinct goals/env-seeds for the IV dataset")
    ap.add_argument("--k_resamples", type=int, default=20, help="channel-noise resamples per goal")
    args = ap.parse_args()

    print("=" * 70)
    print("Stage 2, real system: noise-as-instrument vs. direct intervention")
    print(f"bits={args.bits}  train_episodes={args.episodes}  entropy_coef={args.entropy_coef}")
    print("=" * 70)

    print("\n[1/3] Training the dual-aux policy (paper's best config)...")
    env, speaker, listener, channel, baseline, ep_returns = train_policies_dual_aux(
        args.bits, args.episodes, args.seed, entropy_coef=args.entropy_coef,
        episodes_per_update=16, speaker_aux_coef=200.0, listener_aux_coef=200.0,
        log_every=max(args.episodes // 4, 1))

    print("\n[2/3] Direct-intervention ground truth (ablation + randomisation) on this trained instance...")
    direct = evaluate(env, speaker, listener, channel, args.bits, args.seed, n_eval_episodes=150)
    print(f"  real={direct['eval_return_real_message_mean']:+.2f}  "
          f"ablated={direct['eval_return_zero_message_mean']:+.2f} (z={direct['real_vs_zero_z_stat']:+.2f})  "
          f"randomised={direct['eval_return_shuffled_message_mean']:+.2f} (z={direct['real_vs_shuffled_z_stat']:+.2f})")

    print(f"\n[3/3] Noise-as-instrument: {args.iv_episodes} goals x {args.k_resamples} channel-noise resamples "
          f"= {args.iv_episodes * args.k_resamples} full-episode rollouts...")
    rows = collect_iv_dataset(env, speaker, listener, args.bits, channel.tau,
                              args.iv_episodes, args.k_resamples, args.seed)
    env.close()

    M = np.array([r["M_mean"] for r in rows])
    U = np.array([r["U"] for r in rows])
    N = np.array([r["N_mean"] for r in rows])

    naive = naive_ols(M, U)
    iv = iv_estimate(M, U, N)
    f_stat = first_stage_f_stat(M, N)
    naive_ci = bootstrap_ci(M, U, N, naive_ols)
    iv_ci = bootstrap_ci(M, U, N, iv_estimate)

    print(f"\n  naive OLS  (return on mean message):     {naive:+.3f}   95% CI [{naive_ci[0]:+.3f}, {naive_ci[1]:+.3f}]")
    print(f"  IV estimate (noise-as-instrument):        {iv:+.3f}   95% CI [{iv_ci[0]:+.3f}, {iv_ci[1]:+.3f}]")
    print(f"  first-stage F-statistic:                  {f_stat:.1f}  ({'OK' if f_stat >= 10 else 'WEAK -- do not trust the IV point estimate'})")

    value_of_info = 8.10  # expert (-8.78) minus goal-blind (-16.88), from Table 2 of paper_main/main.tex
    direct_effect_ablation = direct['eval_return_real_message_mean'] - direct['eval_return_zero_message_mean']
    direct_effect_randomisation = direct['eval_return_real_message_mean'] - direct['eval_return_shuffled_message_mean']
    print(f"\n  For scale: direct-intervention effect sizes on this same policy were "
          f"{direct_effect_ablation:+.2f} (ablation) and {direct_effect_randomisation:+.2f} (randomisation) "
          f"reward units, against a value of information of {value_of_info:.2f}.")

    summary = {
        "config": vars(args),
        "training_final_return_mean_last100": float(np.mean(ep_returns[-100:])),
        "direct_intervention": direct,
        "value_of_information": value_of_info,
        "iv_dataset_n": len(rows),
        "naive_ols": naive, "naive_ols_ci95": naive_ci,
        "iv_estimate": iv, "iv_estimate_ci95": iv_ci,
        "first_stage_f_stat": f_stat,
        "rows": rows,
    }
    out_path = os.path.join(LOG_DIR, f"paper2_noise_as_instrument_stage2_seed{args.seed}.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, default=float)
    print(f"\nWrote {out_path}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

        ax = axes[0]
        ax.scatter(M, U, s=10, alpha=0.4, color="#4a7fb5")
        ax.set_xlabel("Mean message value (per episode)")
        ax.set_ylabel("Episode return")
        ax.set_title(f"Raw data: {len(rows)} rollouts, {args.iv_episodes} goals x {args.k_resamples} noise draws")

        ax = axes[1]
        labels = ["Naive OLS", "IV\n(noise instrument)", "Ablation\n(direct)", "Randomisation\n(direct)"]
        vals = [naive, iv, direct_effect_ablation / value_of_info, direct_effect_randomisation / value_of_info]
        errs_lo = [naive - naive_ci[0], iv - iv_ci[0], 0, 0]
        errs_hi = [naive_ci[1] - naive, iv_ci[1] - iv, 0, 0]
        colors = ["#d95f5f", "#4a7fb5", "#3c8c5a", "#3c8c5a"]
        ax.bar(labels, vals, color=colors, yerr=[errs_lo, errs_hi], capsize=4)
        ax.axhline(0, color="black", linewidth=0.8)
        ax.set_yscale("symlog", linthresh=1.0)
        ax.set_ylabel("Effect estimate, symlog scale (IV/naive: reward per unit\nmessage; direct: fraction of value of information)")
        ax.set_title(f"IV 95% CI spans [{iv_ci[0]:.0f}, {iv_ci[1]:.0f}] (F={f_stat:.1f}): do not trust it", fontsize=10.5)
        plt.setp(ax.get_xticklabels(), fontsize=8)

        fig.tight_layout()
        plot_path = os.path.join(PLOT_DIR, "paper2_noise_as_instrument_stage2.png")
        fig.savefig(plot_path, dpi=150)
        print(f"Wrote {plot_path}")
    except ImportError:
        print("matplotlib not available -- skipped plot, JSON summary still written.")


if __name__ == "__main__":
    main()

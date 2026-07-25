"""
run_bandwidth_sweep.py
=======================
Stage 2 of Paper 1: does the Capacity-Bandwidth Saturation Law (Prediction 1)
survive when the interface is *learned* end-to-end by gradient descent,
rather than imposed by hand as in the `coupling_lab.py` analytical sandbox?

Environment: PettingZoo MPE `simple_speaker_listener_v4`. The speaker sees a
private goal (which landmark the listener should reach) and must convey it;
the listener sees its own state plus the message and must navigate to the
correct landmark. We bypass the environment's own fixed-vocabulary
communication channel (see `gumbel_channel.py` for why) and route messages
through a `GumbelBinaryChannel` whose width `n_bits` is the swept bandwidth
B in {1, 2, 4, 8, 16, 32}.

Training: both policies are optimized jointly with REINFORCE (advantage =
return - value baseline). Gradients also flow through the Gumbel-Sigmoid
channel from the listener's loss back into the speaker's message logits, so
the message code is shaped by both the score-function term (via the
speaker's own action distribution -- degenerate here, see below) and direct
backprop through the channel (the DIAL-style path). Since the speaker has no
physical action in this scenario, its only trainable signal *is* the
backprop-through-channel path -- which is exactly the "learned interface"
this stage is testing.

After training at each bandwidth, we log:
  * episodic task return (navigation success),
  * measured coupling capacity via the paper's own predictive-gain
    estimator (`coupling_lab.predictive_gain_te`), applied to the recorded
    message-bit trajectory (source) and listener-state trajectory (target)
    over a frozen evaluation rollout.

Usage:
    python3 run_bandwidth_sweep.py --seed 42
    python3 run_bandwidth_sweep.py --bits 1 2 4 8 16 32 --episodes 800
"""

from __future__ import annotations
import argparse
import json
import os
from datetime import datetime

import numpy as np
import torch
import torch.optim as optim

from gumbel_channel import GumbelBinaryChannel
from policies import SpeakerPolicy, ListenerPolicy, ValueBaseline
import coupling_lab as cl

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LOG_DIR = os.path.join(ROOT, "experiments", "results", "logs")
os.makedirs(LOG_DIR, exist_ok=True)


def make_env(max_cycles: int = 25):
    # PettingZoo split its Multi-Agent Particle Environments out into the
    # standalone `mpe2` package; `pettingzoo.mpe` no longer exists.
    from mpe2 import simple_speaker_listener_v4
    return simple_speaker_listener_v4.parallel_env(
        max_cycles=max_cycles, continuous_actions=False
    )


def rollout(env, speaker, listener, channel, n_bits, seed, baseline=None,
            greedy=False, record=False, zero_message=False):
    """Run one episode. Returns (log_probs, values, entropies, rewards, records).

    zero_message: ablation switch. If True, the listener always receives an
    all-zero message regardless of what the speaker emits -- the speaker's
    forward pass still runs (so gradients/logging are unaffected when this
    is used only at eval time), but the *information* never reaches the
    listener. Used to test whether the listener's task performance actually
    depends on the message at all (dead-channel diagnostic).
    """
    obs, _ = env.reset(seed=seed)
    speaker_id = [a for a in env.agents if a.startswith("speaker")][0]
    listener_id = [a for a in env.agents if a.startswith("listener")][0]

    log_probs, values, entropies, rewards = [], [], [], []
    messages, listener_states, speaker_obs_hist = [], [], []

    speaker_noop = None  # resolved from action space on first use

    done = False
    while env.agents:
        s_obs = torch.tensor(obs[speaker_id], dtype=torch.float32)
        l_obs = torch.tensor(obs[listener_id], dtype=torch.float32)

        msg_logits = speaker(s_obs)
        message = channel(msg_logits, hard=True)  # (n_bits,) in {0,1}, straight-through
        message_to_listener = torch.zeros_like(message) if zero_message else message

        dist = listener(l_obs, message_to_listener)
        value = baseline(l_obs) if baseline is not None else torch.zeros(())
        if not greedy:
            action = dist.sample()
        else:
            action = dist.probs.argmax()
        log_prob = dist.log_prob(action)

        if speaker_noop is None:
            speaker_noop = env.action_space(speaker_id).sample() * 0

        actions = {speaker_id: int(speaker_noop), listener_id: int(action.item())}
        next_obs, reward, terminations, truncations, infos = env.step(actions)

        rewards.append(float(reward[listener_id]))
        log_probs.append(log_prob)
        values.append(value)
        entropies.append(dist.entropy())

        if record:
            messages.append(message.detach().numpy().copy())
            listener_states.append(np.asarray(obs[listener_id], dtype=float))
            speaker_obs_hist.append(s_obs.detach().numpy().copy())

        obs = next_obs
        done = all(terminations.values()) or all(truncations.values())
        if done:
            break

    records = None
    if record:
        records = {
            "messages": np.array(messages),
            "listener_states": np.array(listener_states),
            "speaker_obs": np.array(speaker_obs_hist),
        }
    return log_probs, values, entropies, rewards, records


def discount_returns(rewards, gamma=0.95):
    G, out = 0.0, []
    for r in reversed(rewards):
        G = r + gamma * G
        out.append(G)
    out.reverse()
    return torch.tensor(out, dtype=torch.float32)


def train_policies(n_bits, episodes, seed, lr=3e-3, entropy_coef=0.02, log_every=50,
                    episodes_per_update=1):
    """Train speaker/listener/baseline for one bandwidth and return them, still
    live (env open), so callers can run custom evaluation/ablation rollouts
    without re-training. Used by both train_one_bandwidth and
    diagnose_channel_usage.py.

    episodes_per_update: how many episodes' trajectories to accumulate before
    each Adam step (default 1 = original single-episode REINFORCE update).
    Motivation: diagnose_channel_usage.py found the speaker's gradient is
    real and stable (~0.3 norm, never vanishing) but ~40x smaller than the
    listener's and computed from a single noisy episode -- a supervised
    probe with the same channel and batch_size=64 converged to R^2>0.99 in
    a few hundred steps, so batching more episodes per update is the
    leading hypothesis for reducing REINFORCE variance enough for the
    speaker's weak, indirect signal to actually accumulate in a consistent
    direction. `episodes` still counts total episodes of experience, so runs
    stay comparable across different episodes_per_update settings.
    """
    torch.manual_seed(seed)
    np.random.seed(seed)

    env = make_env()
    env.reset(seed=seed)
    speaker_id = [a for a in env.agents if a.startswith("speaker")][0]
    listener_id = [a for a in env.agents if a.startswith("listener")][0]
    obs_dim_s = env.observation_space(speaker_id).shape[0]
    obs_dim_l = env.observation_space(listener_id).shape[0]
    n_actions = env.action_space(listener_id).n

    channel = GumbelBinaryChannel(n_bits=n_bits, tau=1.0)
    speaker = SpeakerPolicy(obs_dim_s, n_bits)
    listener = ListenerPolicy(obs_dim_l, n_bits, n_actions)
    baseline = ValueBaseline(obs_dim_l)

    params = list(speaker.parameters()) + list(listener.parameters()) + list(baseline.parameters())
    opt = optim.Adam(params, lr=lr)

    n_updates = episodes // episodes_per_update
    ep_returns = []
    ep_counter = 0
    for update in range(n_updates):
        batch_log_probs, batch_values, batch_entropies, batch_returns = [], [], [], []
        for _ in range(episodes_per_update):
            log_probs, values, entropies, rewards, _ = rollout(
                env, speaker, listener, channel, n_bits,
                seed=seed * 10_000 + ep_counter, baseline=baseline)
            returns = discount_returns(rewards)
            batch_log_probs.extend(log_probs)
            batch_values.extend(values)
            batch_entropies.extend(entropies)
            batch_returns.append(returns)
            ep_returns.append(sum(rewards))
            ep_counter += 1

        returns = torch.cat(batch_returns)
        values = torch.stack(batch_values)
        advantage = returns - values.detach()
        adv_norm = (advantage - advantage.mean()) / (advantage.std() + 1e-6)

        policy_loss = -torch.stack([lp * a for lp, a in zip(batch_log_probs, adv_norm)]).sum()
        value_loss = torch.nn.functional.mse_loss(values, returns, reduction="sum")
        entropy_bonus = torch.stack(batch_entropies).sum()
        loss = policy_loss + 0.5 * value_loss - entropy_coef * entropy_bonus

        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(params, max_norm=5.0)
        opt.step()

        if ep_counter % log_every < episodes_per_update:
            recent = np.mean(ep_returns[-log_every:])
            print(f"      [B={n_bits:>2d} bits] episode {ep_counter:>4d}/{episodes}  "
                  f"mean return (last {min(log_every, len(ep_returns))}) = {recent:+.3f}")

    return env, speaker, listener, channel, baseline, ep_returns


def train_one_bandwidth(n_bits, episodes, seed, lr=3e-3, entropy_coef=0.02, log_every=50,
                         n_eval_episodes=150, episodes_per_update=1):
    env, speaker, listener, channel, baseline, ep_returns = train_policies(
        n_bits, episodes, seed, lr=lr, entropy_coef=entropy_coef, log_every=log_every,
        episodes_per_update=episodes_per_update)

    # Frozen evaluation rollouts: measure task success + coupling capacity.
    eval_returns = []
    all_messages, all_states = [], []
    for k in range(n_eval_episodes):
        _, _, _, rewards, rec = rollout(env, speaker, listener, channel, n_bits,
                                        seed=999_000 + seed * 100 + k,
                                        greedy=False, record=True)
        eval_returns.append(sum(rewards))
        all_messages.append(rec["messages"])
        all_states.append(rec["listener_states"])

    messages = np.concatenate(all_messages, axis=0)
    states = np.concatenate(all_states, axis=0)
    # The listener's observation includes the env's own built-in comm slots
    # (constant here, since our speaker always emits a no-op in favor of the
    # side-channel above): zero variance there makes the residual covariance
    # in predictive_gain_te singular (logdet -> -inf on both models -> NaN).
    # Drop any dead dimensions before estimating TE.
    live = states.std(axis=0) > 1e-8
    states = states[:, live]
    # predictive_gain_te is an in-sample linear-regression estimator: as
    # n_bits approaches the eval sample count, its in-sample R^2 is
    # mechanically inflated even for pure noise (verified: 128-bit random
    # noise vs. random state reports ~0.7 "bits" of fake coupling at 500
    # samples). cl.effective_te subtracts a block-shuffled surrogate
    # baseline to remove this finite-sample/dimensionality bias -- the same
    # correction already used for the KSG cross-check in run_experiments.py.
    if n_bits > 0 and messages.shape[0] > 20 and states.shape[1] > 0:
        te_bits, te_raw, te_surrogate = cl.effective_te(
            cl.predictive_gain_te, messages, states, direction="A->B", n_surrogate=8, seed=seed)
    else:
        te_bits, te_raw, te_surrogate = 0.0, 0.0, 0.0

    env.close()
    return {
        "n_bits": n_bits,
        "train_returns": ep_returns,
        "eval_return_mean": float(np.mean(eval_returns)),
        "eval_return_std": float(np.std(eval_returns)),
        "measured_te_bits": float(te_bits),
        "measured_te_raw_bits": float(te_raw),
        "measured_te_surrogate_bits": float(te_surrogate),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, nargs="+", default=[1, 2, 4, 8, 16, 32])
    ap.add_argument("--episodes", type=int, default=600)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--lr", type=float, default=3e-3)
    ap.add_argument("--eval_episodes", type=int, default=150)
    args = ap.parse_args()

    print("=" * 70)
    print("Stage 2 -- Learned Gumbel-Softmax Channel (PettingZoo)")
    print(f"bandwidths={args.bits}  episodes/bandwidth={args.episodes}  seed={args.seed}  lr={args.lr}"
          f"  eval_episodes={args.eval_episodes}")
    print("=" * 70)

    results = []
    for b in args.bits:
        print(f"\n[Bandwidth sweep] training at B={b} bits/step ...")
        r = train_one_bandwidth(b, episodes=args.episodes, seed=args.seed, lr=args.lr,
                                 n_eval_episodes=args.eval_episodes)
        print(f"   -> eval return {r['eval_return_mean']:+.3f} +/- {r['eval_return_std']:.3f}   "
              f"measured TE = {r['measured_te_bits']:.3f} bits "
              f"(raw={r['measured_te_raw_bits']:.3f}, surrogate={r['measured_te_surrogate_bits']:.3f})")
        results.append(r)

    payload = {
        "timestamp": datetime.now().isoformat(),
        "author": "Ashok Pasala (VIT-AP University)",
        "experiment": "P1_stage2_learned_gumbel_channel",
        "environment": "simple_speaker_listener_v4",
        "seed": args.seed,
        "episodes_per_bandwidth": args.episodes,
        "lr": args.lr,
        "eval_episodes": args.eval_episodes,
        "bandwidth_bits": [r["n_bits"] for r in results],
        "eval_return_mean": [r["eval_return_mean"] for r in results],
        "eval_return_std": [r["eval_return_std"] for r in results],
        "measured_te_bits": [r["measured_te_bits"] for r in results],
        "measured_te_raw_bits": [r["measured_te_raw_bits"] for r in results],
        "measured_te_surrogate_bits": [r["measured_te_surrogate_bits"] for r in results],
    }
    out_path = os.path.join(LOG_DIR, f"P1_stage2_gumbel_seed{args.seed}.json")
    with open(out_path, "w") as f:
        json.dump(payload, f, indent=2, default=float)
    print(f"\nLog written -> {out_path}")


if __name__ == "__main__":
    main()

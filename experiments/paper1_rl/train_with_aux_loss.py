"""
train_with_aux_loss.py
========================
Stage 2, next attempt after isolating the chicken-and-egg failure: plain
REINFORCE never gets the speaker to encode anything (encoding R^2 ~0.001
regardless of batch size or entropy_coef) and the listener has learned to
almost entirely ignore the channel (message-sensitivity KL ~18x smaller than
its sensitivity to its own state) -- see TODO.md. Neither side has a reason
to move first.

This script adds a small auxiliary reconstruction loss directly into the
joint RL objective: a decoder must reconstruct the speaker's own goal
observation from the transmitted message, trained via direct backprop
through the same straight-through Gumbel channel (exactly the loss that
converged in a few hundred steps in probe_supervised_encoding.py, now
co-trained alongside the RL objective instead of replacing it). The goal is
to give the speaker a real, low-variance gradient toward encoding
*something* from the start, so the listener has something non-trivial to
learn to attend to.

This does NOT touch run_bandwidth_sweep.py's train_policies() -- that
function is shared by multiple existing scripts and its rollout() contract
returns detached numpy for recording, which isn't differentiable. Kept
self-contained here instead to avoid risk to that shared path.

Usage:
    python3 train_with_aux_loss.py --bits 8 --episodes 2000 --aux_coef 1.0
"""

from __future__ import annotations
import argparse
import json
import os
from datetime import datetime

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from gumbel_channel import GumbelBinaryChannel
from policies import SpeakerPolicy, ListenerPolicy, ValueBaseline
from probe_supervised_encoding import Decoder
from run_bandwidth_sweep import make_env, rollout, discount_returns
from diagnose_channel_usage import _ridge_r2

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LOG_DIR = os.path.join(ROOT, "experiments", "results", "logs")
os.makedirs(LOG_DIR, exist_ok=True)


def rollout_with_aux(env, speaker, listener, channel, baseline, seed):
    """Same control flow as run_bandwidth_sweep.rollout(), but also returns
    the raw (non-detached) per-step (message, speaker_obs) tensor pairs so
    an auxiliary reconstruction loss can backprop through them."""
    obs, _ = env.reset(seed=seed)
    speaker_id = [a for a in env.agents if a.startswith("speaker")][0]
    listener_id = [a for a in env.agents if a.startswith("listener")][0]

    log_probs, values, entropies, rewards = [], [], [], []
    aux_messages, aux_speaker_obs = [], []
    speaker_noop = None

    while env.agents:
        s_obs = torch.tensor(obs[speaker_id], dtype=torch.float32)
        l_obs = torch.tensor(obs[listener_id], dtype=torch.float32)

        msg_logits = speaker(s_obs)
        message = channel(msg_logits, hard=True)

        dist = listener(l_obs, message)
        value = baseline(l_obs)
        action = dist.sample()
        log_prob = dist.log_prob(action)

        if speaker_noop is None:
            speaker_noop = env.action_space(speaker_id).sample() * 0
        actions = {speaker_id: int(speaker_noop), listener_id: int(action.item())}
        next_obs, reward, terminations, truncations, infos = env.step(actions)

        rewards.append(float(reward[listener_id]))
        log_probs.append(log_prob)
        values.append(value)
        entropies.append(dist.entropy())
        aux_messages.append(message)      # still attached to the graph
        aux_speaker_obs.append(s_obs)

        obs = next_obs
        if all(terminations.values()) or all(truncations.values()):
            break

    return log_probs, values, entropies, rewards, aux_messages, aux_speaker_obs


def train_policies_aux(n_bits, episodes, seed, lr=5e-4, entropy_coef=0.0,
                        episodes_per_update=16, aux_coef=1.0, log_every=None):
    torch.manual_seed(seed)
    np.random.seed(seed)
    log_every = log_every or episodes

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
    decoder = Decoder(n_bits, obs_dim_s)

    params = (list(speaker.parameters()) + list(listener.parameters())
              + list(baseline.parameters()) + list(decoder.parameters()))
    opt = optim.Adam(params, lr=lr)

    n_updates = episodes // episodes_per_update
    ep_returns, ep_counter = [], 0
    for update in range(n_updates):
        batch_log_probs, batch_values, batch_entropies, batch_returns = [], [], [], []
        batch_messages, batch_speaker_obs = [], []
        for _ in range(episodes_per_update):
            log_probs, values, entropies, rewards, aux_messages, aux_speaker_obs = rollout_with_aux(
                env, speaker, listener, channel, baseline, seed=seed * 10_000 + ep_counter)
            returns = discount_returns(rewards)
            batch_log_probs.extend(log_probs)
            batch_values.extend(values)
            batch_entropies.extend(entropies)
            batch_returns.append(returns)
            batch_messages.extend(aux_messages)
            batch_speaker_obs.extend(aux_speaker_obs)
            ep_returns.append(sum(rewards))
            ep_counter += 1

        returns = torch.cat(batch_returns)
        values = torch.stack(batch_values)
        advantage = returns - values.detach()
        adv_norm = (advantage - advantage.mean()) / (advantage.std() + 1e-6)

        policy_loss = -torch.stack([lp * a for lp, a in zip(batch_log_probs, adv_norm)]).sum()
        value_loss = nn.functional.mse_loss(values, returns, reduction="sum")
        entropy_bonus = torch.stack(batch_entropies).sum()

        messages_t = torch.stack(batch_messages)
        speaker_obs_t = torch.stack(batch_speaker_obs)
        recon = decoder(messages_t)
        aux_loss = nn.functional.mse_loss(recon, speaker_obs_t, reduction="mean")

        loss = policy_loss + 0.5 * value_loss - entropy_coef * entropy_bonus + aux_coef * aux_loss

        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(params, max_norm=5.0)
        opt.step()

        if ep_counter % log_every < episodes_per_update:
            recent = np.mean(ep_returns[-log_every:])
            print(f"      [B={n_bits:>2d}] episode {ep_counter:>4d}/{episodes}  "
                  f"return(last {min(log_every, len(ep_returns))})={recent:+.2f}  aux_loss={aux_loss.item():.4f}")

    return env, speaker, listener, channel, baseline, decoder, ep_returns


def evaluate(env, speaker, listener, channel, n_bits, seed, n_eval_episodes=150):
    """Reuses run_bandwidth_sweep.rollout (frozen, detached) for eval so this
    matches the same diagnostics used elsewhere (encoding R^2, real-vs-zero
    return, listener message-sensitivity KL)."""
    def eval_batch(zero_message, seed_offset):
        returns, all_messages, all_speaker_obs, all_listener_states = [], [], [], []
        for k in range(n_eval_episodes):
            _, _, _, rewards, rec = rollout(
                env, speaker, listener, channel, n_bits,
                seed=999_000 + seed * 100 + seed_offset + k,
                greedy=False, record=True, zero_message=zero_message)
            returns.append(sum(rewards))
            all_messages.append(rec["messages"])
            all_speaker_obs.append(rec["speaker_obs"])
            all_listener_states.append(rec["listener_states"])
        return (np.array(returns), np.concatenate(all_messages, axis=0),
                np.concatenate(all_speaker_obs, axis=0), np.concatenate(all_listener_states, axis=0))

    real_returns, messages, speaker_obs, listener_states = eval_batch(False, 0)
    zero_returns, _, _, _ = eval_batch(True, 500_000)

    encoding_r2 = _ridge_r2(messages, speaker_obs)

    with torch.no_grad():
        l_obs_t = torch.tensor(listener_states, dtype=torch.float32)
        msg_t = torch.tensor(messages, dtype=torch.float32)
        rng = np.random.default_rng(seed)
        dist_real = listener(l_obs_t, msg_t)
        dist_shuf_msg = listener(l_obs_t, msg_t[rng.permutation(len(msg_t))])
        dist_shuf_state = listener(l_obs_t[rng.permutation(len(l_obs_t))], msg_t)
        msg_kl = float(torch.distributions.kl_divergence(dist_real, dist_shuf_msg).mean().item())
        state_kl = float(torch.distributions.kl_divergence(dist_real, dist_shuf_state).mean().item())

    real_mean, real_std = float(real_returns.mean()), float(real_returns.std())
    zero_mean, zero_std = float(zero_returns.mean()), float(zero_returns.std())
    se = np.sqrt(real_std ** 2 / n_eval_episodes + zero_std ** 2 / n_eval_episodes) + 1e-9
    z_stat = (real_mean - zero_mean) / se

    return {
        "eval_return_real_message_mean": real_mean,
        "eval_return_zero_message_mean": zero_mean,
        "real_vs_zero_z_stat": float(z_stat),
        "speaker_goal_to_message_encoding_r2": encoding_r2,
        "listener_message_sensitivity_kl": msg_kl,
        "listener_state_sensitivity_kl": state_kl,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, nargs="+", default=[8])
    ap.add_argument("--episodes", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--lr", type=float, default=5e-4)
    ap.add_argument("--entropy_coef", type=float, default=0.0)
    ap.add_argument("--episodes_per_update", type=int, default=16)
    ap.add_argument("--aux_coef", type=float, default=1.0)
    ap.add_argument("--eval_episodes", type=int, default=150)
    args = ap.parse_args()

    print("=" * 70)
    print("Stage 2 -- REINFORCE + auxiliary reconstruction loss (bootstrap attempt)")
    print(f"bandwidths={args.bits}  episodes={args.episodes}  epu={args.episodes_per_update}  "
          f"entropy_coef={args.entropy_coef}  aux_coef={args.aux_coef}")
    print("=" * 70)

    results = []
    for b in args.bits:
        env, speaker, listener, channel, baseline, decoder, ep_returns = train_policies_aux(
            b, args.episodes, args.seed, lr=args.lr, entropy_coef=args.entropy_coef,
            episodes_per_update=args.episodes_per_update, aux_coef=args.aux_coef)
        r = evaluate(env, speaker, listener, channel, b, args.seed, n_eval_episodes=args.eval_episodes)
        env.close()
        r["n_bits"] = b
        r["aux_coef"] = args.aux_coef
        print(f"[B={b}] eval return real={r['eval_return_real_message_mean']:+.2f} "
              f"zero={r['eval_return_zero_message_mean']:+.2f} (z={r['real_vs_zero_z_stat']:+.2f})")
        print(f"        encoding R^2={r['speaker_goal_to_message_encoding_r2']:.4f}   "
              f"msg-sensitivity KL={r['listener_message_sensitivity_kl']:.4f}   "
              f"state-sensitivity KL={r['listener_state_sensitivity_kl']:.4f}")
        results.append(r)

    out_path = os.path.join(LOG_DIR, f"P1_stage2_aux_loss_seed{args.seed}.json")
    with open(out_path, "w") as f:
        json.dump({"timestamp": datetime.now().isoformat(), "results": results,
                    "episodes": args.episodes, "episodes_per_update": args.episodes_per_update,
                    "entropy_coef": args.entropy_coef}, f, indent=2, default=float)
    print(f"\nLog written -> {out_path}")


if __name__ == "__main__":
    main()

"""
probe_oracle_listener.py
==========================
Stage 2 sanity check, queued after three independent receiver-side fixes
(entropy_coef, episodes_per_update batching, message-aware value baseline)
all failed to get the listener to exploit a channel that demonstrably
carries the goal (see TODO.md). Before chasing a fourth credit-assignment
fix, check a more basic possibility: does knowing the goal even help the
listener get meaningfully more reward in this environment, in absolute
terms?

Trains a listener with direct oracle access to the speaker's true
observation (concatenated onto its own obs, no channel, no speaker, no
information bottleneck at all -- the best any listener could possibly do
with the goal) and compares its achievable return against the current
best message-based results (~-16 to -19 eval return, per TODO.md).

If the oracle's return isn't dramatically better than the message-blind
listener's, the environment's reward shaping doesn't reward correct
goal-conditioning much in absolute terms, and the "listener won't exploit
an informative channel" finding is explained by low task sensitivity to
the goal, not (or not only) by an RL credit-assignment failure.

If the oracle achieves a much better return, that confirms there IS real
reward headroom on the table, and the receiver-side mystery remains a real,
worthwhile open question.

Usage:
    python3 probe_oracle_listener.py --episodes 6000
"""

from __future__ import annotations
import argparse

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

from policies import ValueBaseline
from run_bandwidth_sweep import make_env, discount_returns


class OracleListenerPolicy(nn.Module):
    """Listener conditioned directly on the speaker's true observation --
    no channel, no bottleneck, no speaker network at all. Upper bound on
    what any listener could achieve if it perfectly knew the goal."""

    def __init__(self, obs_dim_l, obs_dim_s, n_actions, hidden=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim_l + obs_dim_s, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
            nn.Linear(hidden, n_actions),
        )

    def forward(self, l_obs, s_obs):
        return Categorical(logits=self.net(torch.cat([l_obs, s_obs], dim=-1)))


def rollout_oracle(env, listener, baseline, seed, greedy=False):
    obs, _ = env.reset(seed=seed)
    speaker_id = [a for a in env.agents if a.startswith("speaker")][0]
    listener_id = [a for a in env.agents if a.startswith("listener")][0]

    log_probs, values, entropies, rewards = [], [], [], []
    speaker_noop = None

    while env.agents:
        s_obs = torch.tensor(obs[speaker_id], dtype=torch.float32)
        l_obs = torch.tensor(obs[listener_id], dtype=torch.float32)

        dist = listener(l_obs, s_obs)
        value = baseline(l_obs)
        action = dist.probs.argmax() if greedy else dist.sample()
        log_prob = dist.log_prob(action)

        if speaker_noop is None:
            speaker_noop = env.action_space(speaker_id).sample() * 0
        actions = {speaker_id: int(speaker_noop), listener_id: int(action.item())}
        next_obs, reward, terminations, truncations, infos = env.step(actions)

        rewards.append(float(reward[listener_id]))
        log_probs.append(log_prob)
        values.append(value)
        entropies.append(dist.entropy())

        obs = next_obs
        if all(terminations.values()) or all(truncations.values()):
            break

    return log_probs, values, entropies, rewards


def train_oracle(episodes, seed, lr=5e-4, entropy_coef=0.02, episodes_per_update=16, log_every=None):
    log_every = log_every or episodes
    torch.manual_seed(seed)
    np.random.seed(seed)

    env = make_env()
    env.reset(seed=seed)
    speaker_id = [a for a in env.agents if a.startswith("speaker")][0]
    listener_id = [a for a in env.agents if a.startswith("listener")][0]
    obs_dim_s = env.observation_space(speaker_id).shape[0]
    obs_dim_l = env.observation_space(listener_id).shape[0]
    n_actions = env.action_space(listener_id).n

    listener = OracleListenerPolicy(obs_dim_l, obs_dim_s, n_actions)
    baseline = ValueBaseline(obs_dim_l)
    params = list(listener.parameters()) + list(baseline.parameters())
    opt = optim.Adam(params, lr=lr)

    n_updates = episodes // episodes_per_update
    ep_returns, ep_counter = [], 0
    for update in range(n_updates):
        batch_log_probs, batch_values, batch_entropies, batch_returns = [], [], [], []
        for _ in range(episodes_per_update):
            log_probs, values, entropies, rewards = rollout_oracle(
                env, listener, baseline, seed=seed * 10_000 + ep_counter)
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
        value_loss = nn.functional.mse_loss(values, returns, reduction="sum")
        entropy_bonus = torch.stack(batch_entropies).sum()
        loss = policy_loss + 0.5 * value_loss - entropy_coef * entropy_bonus

        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(params, max_norm=5.0)
        opt.step()

        if ep_counter % log_every < episodes_per_update:
            recent = np.mean(ep_returns[-log_every:])
            print(f"      [oracle] episode {ep_counter:>5d}/{episodes}  return(last {min(log_every, len(ep_returns))})={recent:+.2f}")

    # Frozen eval.
    eval_returns = []
    for k in range(150):
        _, _, _, rewards = rollout_oracle(env, listener, baseline, seed=999_000 + seed * 100 + k, greedy=False)
        eval_returns.append(sum(rewards))
    env.close()
    return float(np.mean(eval_returns)), float(np.std(eval_returns))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", type=int, default=6000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--episodes_per_update", type=int, default=16)
    args = ap.parse_args()

    print("=" * 70)
    print("Oracle listener (direct access to speaker's true goal obs, no channel)")
    print(f"episodes={args.episodes}  episodes_per_update={args.episodes_per_update}  seed={args.seed}")
    print("=" * 70)

    mean_r, std_r = train_oracle(args.episodes, args.seed, episodes_per_update=args.episodes_per_update)
    print(f"\nOracle eval return: {mean_r:+.2f} +/- {std_r:.2f}")
    print("Compare against: message-based listener best runs so far, eval return ~ -16 to -19 (see TODO.md).")


if __name__ == "__main__":
    main()

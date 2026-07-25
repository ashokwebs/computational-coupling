"""
train_with_receiver_aux.py
============================
Stage 2, next step after train_with_aux_loss.py's finding: an auxiliary
reconstruction loss on the *speaker* (aux_coef=200) got the speaker's
encoding R^2 from 0.001 to 0.76 -- a real fix. But even with a fully
converged, highly informative channel at 20000 episodes, the listener's
task performance was statistically identical with the real message vs. a
zeroed one (z=0.00). The bottleneck moved cleanly to the receiver side:
plain REINFORCE isn't teaching the listener to condition its action on the
now-meaningful message dimensions.

This script gives the *listener* the same kind of bootstrapping aid the
speaker got, but done properly as an auxiliary task sharing the listener's
own hidden representation (not a separate probe network) -- so the gradient
actually shapes the same features that feed the action head, which is the
only way an auxiliary loss can influence actual behavior. `ListenerPolicyWithAux`
adds a second head (goal-reconstruction) off the same trunk used for action
logits; forward() defaults to returning just the Categorical (so eval code
elsewhere -- run_bandwidth_sweep.rollout(), diagnose_channel_usage.py's
diagnostics -- keeps working unmodified), and training code opts in via
return_aux=True to also get the reconstruction head's prediction.

Both speaker and listener get their own auxiliary coefficient here, since
Stage 2 so far has needed both a sender-side and (now) a receiver-side
bootstrapping aid -- solving one alone was demonstrably insufficient.

Usage:
    python3 train_with_receiver_aux.py --bits 8 --episodes 20000 \
        --speaker_aux_coef 200 --listener_aux_coef 200
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
from torch.distributions import Categorical

from gumbel_channel import GumbelBinaryChannel
from policies import SpeakerPolicy
from probe_supervised_encoding import Decoder
from run_bandwidth_sweep import make_env, rollout, discount_returns
from diagnose_channel_usage import _ridge_r2

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LOG_DIR = os.path.join(ROOT, "experiments", "results", "logs")
os.makedirs(LOG_DIR, exist_ok=True)


class ValueBaselineWithMessage(nn.Module):
    """policies.ValueBaseline only ever sees the listener's own observation,
    never the message -- so the advantage estimate can't explain away any
    return variance the message *should* account for once it's informative.
    That leaves more noise for the action head's REINFORCE gradient to fight
    through than necessary. This variant conditions the baseline on the
    message too, exactly like the listener's own policy does."""

    def __init__(self, obs_dim, n_bits, hidden=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim + n_bits, hidden), nn.Tanh(),
            nn.Linear(hidden, 1),
        )

    def forward(self, obs, message):
        x = torch.cat([obs, message], dim=-1) if message.shape[-1] > 0 else obs
        return self.net(x).squeeze(-1)


class ListenerPolicyWithAux(nn.Module):
    """Same trunk as policies.ListenerPolicy, plus a goal-reconstruction head
    off the SAME hidden features that feed the action head -- so an
    auxiliary loss on that head actually shapes what the action head sees,
    unlike a separate probe network trained on frozen/detached features."""

    def __init__(self, obs_dim, n_bits, n_actions, speaker_obs_dim, hidden=64):
        super().__init__()
        self.trunk = nn.Sequential(
            nn.Linear(obs_dim + n_bits, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
        )
        self.action_head = nn.Linear(hidden, n_actions)
        self.aux_head = nn.Linear(hidden, speaker_obs_dim)

    def forward(self, obs, message, return_aux=False):
        x = torch.cat([obs, message], dim=-1) if message.shape[-1] > 0 else obs
        h = self.trunk(x)
        dist = Categorical(logits=self.action_head(h))
        if return_aux:
            return dist, self.aux_head(h)
        return dist


def rollout_with_aux(env, speaker, listener, channel, baseline, seed):
    obs, _ = env.reset(seed=seed)
    speaker_id = [a for a in env.agents if a.startswith("speaker")][0]
    listener_id = [a for a in env.agents if a.startswith("listener")][0]

    log_probs, values, entropies, rewards = [], [], [], []
    speaker_aux_messages, speaker_aux_obs = [], []
    listener_aux_preds, listener_aux_targets = [], []
    speaker_noop = None

    while env.agents:
        s_obs = torch.tensor(obs[speaker_id], dtype=torch.float32)
        l_obs = torch.tensor(obs[listener_id], dtype=torch.float32)

        msg_logits = speaker(s_obs)
        message = channel(msg_logits, hard=True)

        dist, listener_aux_pred = listener(l_obs, message, return_aux=True)
        # Detach message here: the baseline should still see message content
        # (to reduce advantage variance for the listener's policy gradient),
        # but its value_loss is reduction="sum" over the whole batch -- an
        # undetached message would open a large, uncontrolled sum-scaled
        # gradient path back to the speaker, on top of the already-tuned
        # aux_coef=200 pathway (verified: this collapsed encoding R^2 from
        # 0.90 to 0.0003 when tried without detaching).
        value = baseline(l_obs, message.detach())
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
        speaker_aux_messages.append(message)
        speaker_aux_obs.append(s_obs)
        listener_aux_preds.append(listener_aux_pred)
        listener_aux_targets.append(s_obs)  # listener's aux head also predicts the speaker's goal

        obs = next_obs
        if all(terminations.values()) or all(truncations.values()):
            break

    return (log_probs, values, entropies, rewards,
            speaker_aux_messages, speaker_aux_obs,
            listener_aux_preds, listener_aux_targets)


def train_policies_dual_aux(n_bits, episodes, seed, lr=5e-4, entropy_coef=0.0,
                             episodes_per_update=16, speaker_aux_coef=200.0,
                             listener_aux_coef=200.0, log_every=None):
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
    listener = ListenerPolicyWithAux(obs_dim_l, n_bits, n_actions, obs_dim_s)
    baseline = ValueBaselineWithMessage(obs_dim_l, n_bits)
    speaker_decoder = Decoder(n_bits, obs_dim_s)

    params = (list(speaker.parameters()) + list(listener.parameters())
              + list(baseline.parameters()) + list(speaker_decoder.parameters()))
    opt = optim.Adam(params, lr=lr)

    n_updates = episodes // episodes_per_update
    ep_returns, ep_counter = [], 0
    for update in range(n_updates):
        batch_log_probs, batch_values, batch_entropies, batch_returns = [], [], [], []
        batch_messages, batch_speaker_obs = [], []
        batch_listener_preds, batch_listener_targets = [], []
        for _ in range(episodes_per_update):
            (log_probs, values, entropies, rewards, s_msgs, s_obs_list,
             l_preds, l_targets) = rollout_with_aux(
                env, speaker, listener, channel, baseline, seed=seed * 10_000 + ep_counter)
            returns = discount_returns(rewards)
            batch_log_probs.extend(log_probs)
            batch_values.extend(values)
            batch_entropies.extend(entropies)
            batch_returns.append(returns)
            batch_messages.extend(s_msgs)
            batch_speaker_obs.extend(s_obs_list)
            batch_listener_preds.extend(l_preds)
            batch_listener_targets.extend(l_targets)
            ep_returns.append(sum(rewards))
            ep_counter += 1

        returns = torch.cat(batch_returns)
        values = torch.stack(batch_values)
        advantage = returns - values.detach()
        adv_norm = (advantage - advantage.mean()) / (advantage.std() + 1e-6)

        policy_loss = -torch.stack([lp * a for lp, a in zip(batch_log_probs, adv_norm)]).sum()
        value_loss = nn.functional.mse_loss(values, returns, reduction="sum")
        entropy_bonus = torch.stack(batch_entropies).sum()

        speaker_recon = speaker_decoder(torch.stack(batch_messages))
        speaker_aux_loss = nn.functional.mse_loss(
            speaker_recon, torch.stack(batch_speaker_obs), reduction="mean")

        listener_recon = torch.stack(batch_listener_preds)
        listener_aux_loss = nn.functional.mse_loss(
            listener_recon, torch.stack(batch_listener_targets), reduction="mean")

        loss = (policy_loss + 0.5 * value_loss - entropy_coef * entropy_bonus
                + speaker_aux_coef * speaker_aux_loss + listener_aux_coef * listener_aux_loss)

        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(params, max_norm=5.0)
        opt.step()

        if ep_counter % log_every < episodes_per_update:
            recent = np.mean(ep_returns[-log_every:])
            print(f"      [B={n_bits:>2d}] episode {ep_counter:>5d}/{episodes}  "
                  f"return(last {min(log_every, len(ep_returns))})={recent:+.2f}  "
                  f"speaker_aux={speaker_aux_loss.item():.4f}  listener_aux={listener_aux_loss.item():.4f}")

    return env, speaker, listener, channel, baseline, ep_returns


def evaluate(env, speaker, listener, channel, n_bits, seed, n_eval_episodes=150):
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
    ap.add_argument("--episodes", type=int, default=6000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--lr", type=float, default=5e-4)
    ap.add_argument("--entropy_coef", type=float, default=0.0)
    ap.add_argument("--episodes_per_update", type=int, default=16)
    ap.add_argument("--speaker_aux_coef", type=float, default=200.0)
    ap.add_argument("--listener_aux_coef", type=float, default=200.0)
    ap.add_argument("--eval_episodes", type=int, default=150)
    args = ap.parse_args()

    print("=" * 70)
    print("Stage 2 -- dual (sender + receiver) auxiliary bootstrapping loss")
    print(f"bandwidths={args.bits}  episodes={args.episodes}  epu={args.episodes_per_update}  "
          f"speaker_aux_coef={args.speaker_aux_coef}  listener_aux_coef={args.listener_aux_coef}")
    print("=" * 70)

    results = []
    for b in args.bits:
        env, speaker, listener, channel, baseline, ep_returns = train_policies_dual_aux(
            b, args.episodes, args.seed, lr=args.lr, entropy_coef=args.entropy_coef,
            episodes_per_update=args.episodes_per_update,
            speaker_aux_coef=args.speaker_aux_coef, listener_aux_coef=args.listener_aux_coef)
        r = evaluate(env, speaker, listener, channel, b, args.seed, n_eval_episodes=args.eval_episodes)
        env.close()
        r["n_bits"] = b
        print(f"[B={b}] eval return real={r['eval_return_real_message_mean']:+.2f} "
              f"zero={r['eval_return_zero_message_mean']:+.2f} (z={r['real_vs_zero_z_stat']:+.2f})")
        print(f"        encoding R^2={r['speaker_goal_to_message_encoding_r2']:.4f}   "
              f"msg-sensitivity KL={r['listener_message_sensitivity_kl']:.4f}   "
              f"state-sensitivity KL={r['listener_state_sensitivity_kl']:.4f}")
        results.append(r)

    out_path = os.path.join(LOG_DIR, f"P1_stage2_dual_aux_seed{args.seed}.json")
    with open(out_path, "w") as f:
        json.dump({"timestamp": datetime.now().isoformat(), "results": results,
                    "episodes": args.episodes, "episodes_per_update": args.episodes_per_update,
                    "speaker_aux_coef": args.speaker_aux_coef,
                    "listener_aux_coef": args.listener_aux_coef}, f, indent=2, default=float)
    print(f"\nLog written -> {out_path}")


if __name__ == "__main__":
    main()

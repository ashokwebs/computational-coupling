"""
probe_supervised_encoding.py
=============================
Stage 2 root-cause isolation. diagnose_channel_usage.py showed the speaker
never learns to encode its goal into the message under REINFORCE, at any
bandwidth (encoding R^2 ~ 0.001-0.05 everywhere). Two very different things
could explain that:

  (a) The architecture itself (SpeakerPolicy -> GumbelBinaryChannel
      straight-through) can't carry a learnable signal at all -- e.g. the
      straight-through Gumbel-Sigmoid gradient is too biased/noisy for this
      small MLP to use.
  (b) The architecture is fine, but REINFORCE + backprop-through-channel
      credit assignment (the speaker has no reward of its own -- its only
      learning signal is the listener's advantage-weighted log-prob,
      propagated back through a discrete channel) never actually reaches
      or shapes the speaker's weights in this environment/training budget.

This probe isolates (a) from (b) by removing RL entirely: train speaker +
channel + a small decoder with a *direct supervised* loss requiring the
transmitted message to reconstruct the speaker's own observation (its
private goal). If this converges fast, the architecture is fine and the
bug is in the RL credit-assignment path. If it can't converge even here,
the problem is upstream of RL.

Usage:
    python3 probe_supervised_encoding.py --bits 8 --steps 2000
"""

from __future__ import annotations
import argparse
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from gumbel_channel import GumbelBinaryChannel
from policies import SpeakerPolicy


class Decoder(nn.Module):
    def __init__(self, n_bits, obs_dim, hidden=64):
        super().__init__()
        in_dim = max(n_bits, 1)
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
            nn.Linear(hidden, obs_dim),
        )

    def forward(self, message):
        return self.net(message)


def make_env():
    from mpe2 import simple_speaker_listener_v4
    return simple_speaker_listener_v4.parallel_env(max_cycles=25, continuous_actions=False)


def collect_speaker_obs(env, n_samples, seed):
    """Sample speaker observations across many independent episode resets
    (the goal is set at reset and is what we're testing whether the
    channel can transmit)."""
    speaker_id = [a for a in env.agents if a.startswith("speaker")][0]
    obs_list = []
    for i in range(n_samples):
        obs, _ = env.reset(seed=seed * 100_000 + i)
        obs_list.append(np.asarray(obs[speaker_id], dtype=np.float32))
    return np.stack(obs_list)


def probe(n_bits, steps, seed, lr=1e-3, batch_size=64, tau=1.0):
    torch.manual_seed(seed)
    np.random.seed(seed)

    env = make_env()
    env.reset(seed=seed)
    obs_dim_s = env.observation_space([a for a in env.agents if a.startswith("speaker")][0]).shape[0]

    # Pre-sample a large pool of (goal) observations once -- cheap, and
    # keeps this probe about the channel/speaker, not env sampling noise.
    pool = collect_speaker_obs(env, n_samples=4000, seed=seed)
    env.close()
    pool_t = torch.tensor(pool, dtype=torch.float32)

    channel = GumbelBinaryChannel(n_bits=n_bits, tau=tau)
    speaker = SpeakerPolicy(obs_dim_s, n_bits)
    decoder = Decoder(n_bits, obs_dim_s)
    params = list(speaker.parameters()) + list(decoder.parameters())
    opt = optim.Adam(params, lr=lr)

    n = pool_t.shape[0]
    losses = []
    for step in range(steps):
        idx = np.random.randint(0, n, size=batch_size)
        batch = pool_t[idx]
        msg_logits = speaker(batch)
        message = channel(msg_logits, hard=True)
        pred = decoder(message)
        loss = nn.functional.mse_loss(pred, batch)

        opt.zero_grad()
        loss.backward()
        opt.step()
        losses.append(loss.item())

        if (step + 1) % max(1, steps // 10) == 0:
            print(f"      [B={n_bits:>3d}] step {step + 1:>5d}/{steps}  "
                  f"recon MSE (last {max(1, steps // 10)}) = {np.mean(losses[-(steps // 10):]):.4f}")

    # Final held-out-style R^2 (same pool, but large N and post-training --
    # this probe isn't about generalization, it's about whether the
    # architecture is even capable of carrying the signal).
    with torch.no_grad():
        msg_logits = speaker(pool_t)
        message = channel(msg_logits, hard=True)
        pred = decoder(message)
        ss_res = ((pred - pool_t) ** 2).sum().item()
        ss_tot = ((pool_t - pool_t.mean(dim=0)) ** 2).sum().item()
        r2 = 1.0 - ss_res / (ss_tot + 1e-12)

    return {"n_bits": n_bits, "final_recon_r2": r2, "final_loss": float(np.mean(losses[-20:]))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bits", type=int, nargs="+", default=[1, 2, 8, 32, 128])
    ap.add_argument("--steps", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--lr", type=float, default=1e-3)
    args = ap.parse_args()

    print("=" * 70)
    print("Supervised encoding probe -- can speaker+channel learn to transmit the")
    print("goal at all, with RL removed entirely?")
    print("=" * 70)

    for b in args.bits:
        r = probe(b, args.steps, args.seed, lr=args.lr)
        print(f"[B={b:>3d}] final reconstruction R^2 = {r['final_recon_r2']:.4f}   "
              f"final MSE = {r['final_loss']:.4f}\n")


if __name__ == "__main__":
    main()

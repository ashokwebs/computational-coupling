"""
policies.py
===========
Small MLP speaker/listener policies for the Stage 2 PettingZoo
`simple_speaker_listener` testbed. Kept intentionally small: this is a
controlled bandwidth sweep, not a benchmark-scale MARL result, so we favor
fast CPU training over model capacity.
"""

from __future__ import annotations
import torch
import torch.nn as nn
from torch.distributions import Categorical


class SpeakerPolicy(nn.Module):
    """Maps the speaker's goal observation to `n_bits` channel logits."""

    def __init__(self, obs_dim: int, n_bits: int, hidden: int = 64):
        super().__init__()
        self.n_bits = n_bits
        out_dim = max(n_bits, 1)
        self.net = nn.Sequential(
            nn.Linear(obs_dim, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
            nn.Linear(hidden, out_dim),
        )

    def forward(self, obs: torch.Tensor) -> torch.Tensor:
        logits = self.net(obs)
        return logits[..., : self.n_bits] if self.n_bits > 0 else logits[..., :0]


class ListenerPolicy(nn.Module):
    """Maps [listener obs ; received message bits] to a movement-action distribution."""

    def __init__(self, obs_dim: int, n_bits: int, n_actions: int, hidden: int = 64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim + n_bits, hidden), nn.Tanh(),
            nn.Linear(hidden, hidden), nn.Tanh(),
            nn.Linear(hidden, n_actions),
        )

    def forward(self, obs: torch.Tensor, message: torch.Tensor) -> Categorical:
        x = torch.cat([obs, message], dim=-1) if message.shape[-1] > 0 else obs
        return Categorical(logits=self.net(x))


class ValueBaseline(nn.Module):
    """Scalar state-value baseline (variance reduction for REINFORCE)."""

    def __init__(self, obs_dim: int, hidden: int = 64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim, hidden), nn.Tanh(),
            nn.Linear(hidden, 1),
        )

    def forward(self, obs: torch.Tensor) -> torch.Tensor:
        return self.net(obs).squeeze(-1)

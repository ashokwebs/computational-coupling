"""
gumbel_channel.py
==================
Learned, differentiable bandwidth-limited channel for Stage 2 (PettingZoo).

PettingZoo's `simple_speaker_listener` bakes its own fixed-vocabulary
communication channel (`dim_c=3`, tied to the landmark count) directly into
the scenario, so it isn't exposed as a tunable "bits/step" knob. We bypass
it: the speaker's native env action is a fixed no-op (it never moves, and
the built-in channel is left uninformative), and a *learned* message is
routed through this module as a side-channel appended to the listener's
observation instead. That keeps bandwidth an explicit, sweepable
hyperparameter -- mirroring the `total_bits` knob in `coupling_lab.py`'s
analytical sandbox, but now optimized end-to-end rather than imposed.

The channel discretizes each of `n_bits` message lines independently with a
Gumbel-Sigmoid (binary Concrete) relaxation: each line becomes an
(approximately) 1-bit symbol, so total channel capacity is `n_bits` per
step. A straight-through estimator keeps the forward pass discrete while
gradients flow as if it were the soft relaxation, so the speaker's message
policy is learnable via backprop through the channel (a la DIAL), not only
through policy-gradient credit assignment.
"""

from __future__ import annotations
import torch
import torch.nn as nn


class GumbelBinaryChannel(nn.Module):
    """A bandwidth-`n_bits`-per-step discrete communication channel.

    Forward pass maps real-valued logits -> `n_bits` independent {0, 1}
    symbols via a straight-through Gumbel-Sigmoid relaxation, so the
    channel is discrete on the forward pass but differentiable on the
    backward pass.
    """

    def __init__(self, n_bits: int, tau: float = 1.0):
        super().__init__()
        if n_bits < 0:
            raise ValueError("n_bits must be >= 0")
        self.n_bits = n_bits
        self.tau = tau

    def forward(self, logits: torch.Tensor, hard: bool = True) -> torch.Tensor:
        """logits: (..., n_bits) real-valued -> (..., n_bits) in {0, 1}."""
        if self.n_bits == 0:
            return logits.new_zeros(logits.shape[:-1] + (0,))
        u = torch.rand_like(logits).clamp(1e-6, 1 - 1e-6)
        gumbel_noise = torch.log(u) - torch.log1p(-u)  # logistic noise
        y_soft = torch.sigmoid((logits + gumbel_noise) / self.tau)
        if not hard:
            return y_soft
        y_hard = (y_soft > 0.5).float()
        return y_hard + (y_soft - y_soft.detach())  # straight-through

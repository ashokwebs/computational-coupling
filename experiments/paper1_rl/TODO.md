# 🤖 Paper 1 MARL Experiment TODOs

- [x] Define experiment configuration template in `experiment_template.md`.
- [ ] Implement PettingZoo `simple_speaker_listener_v4` environment wrapper with PyTorch.
- [ ] Implement Gumbel-Softmax discrete channel bottleneck module sweeping $B \in [1, 2, 4, 8, 16, 32]$ bits.
- [ ] Implement Neural Predictive Gain Transfer Entropy estimator ($L_{\text{self}} - L_{\text{joint}}$).
- [ ] Run sweep across 5 random seeds (42, 43, 44, 45, 46).
- [ ] Generate publication plot: $C_{\text{couple}}$ vs Channel Bandwidth $B$ with PCA saturation dimension line.

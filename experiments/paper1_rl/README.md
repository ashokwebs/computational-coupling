# 🧪 Paper 1 — Coupling-Capacity Testbed

**Paper Title:** *Validating Capacity–Bandwidth Saturation Laws in Coupled Systems*
**Target Venues:** NeurIPS / ICML

---

## 🎯 Goal

Validate the three falsifiable predictions of the Theory of Computational Coupling in a
setting where we have **100% ground-truth access** to internal states and can set the
receiver's effective dimensionality, coupling gain, and channel bit-budget by hand.

## 📦 What's here (implemented & runnable — pure NumPy)

| File | Role |
| :--- | :--- |
| `coupling_lab.py` | Simulator (coupled VAR systems + bandwidth-limited channel), three transfer-entropy estimators (Gaussian/predictive-gain, model-free KSG, effective-TE surrogates), and effective-dimensionality tools. |
| `run_experiments.py` | Runs all three predictions + the estimator cross-check across 5 seeds; writes figures and JSON logs. |

```bash
python3 run_experiments.py
```

Outputs → `../../figures/`, `../../paper/figures/`, and `../results/logs/`.

## 📊 Results (5 seeds, seeds 42–46)

- **P1 — Saturation law:** capacity saturates at `0.39 × min(d_eff)` bits/step, flat in bandwidth.
- **P2 — Efficiency:** `C/B` rises 3.5× with joint self-predictive accuracy (`r = 0.94`).
- **P3 — Asymmetry:** asymmetry index tracks role from −0.89 to +0.88 (`r = 1.00`).
- **Cross-check:** predictive-gain and KSG estimators agree within 2% (`r > 0.99`).

## 🚧 Stage 2: learned interfaces (the deep-RL version, in progress)

| File | Role |
| :--- | :--- |
| `gumbel_channel.py` | `GumbelBinaryChannel` — straight-through Gumbel-Sigmoid discrete channel; width `n_bits` is the swept bandwidth. |
| `policies.py` | Small MLP `SpeakerPolicy` / `ListenerPolicy` / `ValueBaseline`. |
| `run_bandwidth_sweep.py` | Trains speaker+listener via REINFORCE in PettingZoo's `simple_speaker_listener_v4`, bypassing the env's own fixed-vocabulary comm channel in favor of the learned one, sweeping `B ∈ {1,2,4,8,16,32}` bits/step. Logs task return and measured coupling capacity (via `coupling_lab.predictive_gain_te` on the message/listener-state trajectories) to `experiments/results/logs/`. |

```bash
pip install torch pettingzoo mpe2 gymnasium   # not needed for Stage 1 (PettingZoo split MPE into mpe2)
python3 run_bandwidth_sweep.py --seed 42
```

Swaps the hand-set interface for a **learned** one and checks whether the same saturation
law emerges when the channel is optimized end-to-end rather than imposed by hand. The
Stage 1 NumPy sandbox above is the analytical control for this study. Mechanically
smoke-tested (runs clean, no NaNs) but not yet run long enough to be a real result (see
`TODO.md`) — REINFORCE over a tiny MLP converges slowly on CPU, so the publication-grade
multi-seed sweep will likely need real compute.

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

## 🔜 Next: learned interfaces (the deep-RL version)

Swap the hand-set interface for a **learned** Gumbel-Softmax channel in a `PettingZoo`
cooperative game (`simple_speaker_listener`) and confirm the same laws emerge when the
interface is optimized rather than imposed. The present NumPy sandbox is the analytical
control for that study.

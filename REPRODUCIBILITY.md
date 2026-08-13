---
tags: ["#meta/reproducibility"]
alias: "Reproducibility Protocol"
---

# 🔬 Reproducibility Checklist & Standards

Bro, to make sure our research survives Reviewer #2 and meets top venue standards (**NeurIPS**, **ICML**, **ICLR**, **Nature Machine Intelligence**, **Nature Neuroscience**), every single experiment in this repo gotta follow this checklist.

---

## 📋 Empirical Reproducibility Checklist

### 1. Code & Environment Integrity
- [x] **Minimal dependencies:** The proof-of-concept (`experiments/paper1_rl/`) needs only NumPy + Matplotlib — no GPU, no heavyweight frameworks — so it reproduces on any machine.
- [x] **Fixed Random Seeds:** Every stochastic operation is seeded (`np.random.default_rng`); the sandbox sweeps use seeds `42–46` and reproduce exactly.
- [x] **Deterministic re-run:** `python3 run_experiments.py` regenerates all figures + JSON logs from scratch.

### 2. Information-Theoretic Estimation Standards
- [x] **Transfer Entropy Estimator:** Two independent estimators reported — predictive-gain (Gaussian/Geweke form) and KSG *k*-NN ($k=6$, lag $\Delta=1$, channel-coordinate projection). They agree within 2%.
- [x] **Surrogate Baseline (Effective Transfer Entropy):** Block-shuffled surrogates subtracted for the KSG cross-check ($\mathrm{ETE} = \mathrm{TE} - \mathrm{TE}_{\text{surr}}$).
- [x] **Confidence Intervals:** All sandbox plots show std error bands across 5 seeds.

### 3. Open Dataset Access
- [ ] **Standardized BIDS Access:** For biological recordings (Paper 2), use publicly available OpenNeuro datasets (`ds007764` DUET, `ds007471` Joint Agency EEG) and specify exact commit hashes or BIDS release tags.
- [ ] **Pre-processing Pipelines:** Script all artifact rejection, bandpass filtering, and spatial alignment (FUGW) deterministically.

---

## 🧪 Logging Format Template

When logging an experiment run, create a JSON entry in `experiments/results/logs/`:

```json
{
  "experiment_id": "paper1_rl_sweep_seed42_20260723",
  "timestamp": "2026-07-23T20:00:00",
  "paper": "Paper 1",
  "environment": "simple_speaker_listener_v4",
  "seed": 42,
  "bandwidth_bits": [1, 2, 4, 8, 16, 32],
  "te_estimator": "predictive_gain_loss",
  "results": {
    "capacity_bits": [0.42, 0.81, 1.45, 1.98, 2.01, 2.02],
    "sat_dimension": 2
  },
  "hardware": "NVIDIA RTX 4090 / AMD EPYC",
  "status": "COMPLETED"
}
```

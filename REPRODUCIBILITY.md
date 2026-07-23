---
tags: [#meta/reproducibility]
alias: "Reproducibility Protocol"
---

# 🔬 Reproducibility Checklist & Standards

Bro, to make sure our research survives Reviewer #2 and meets top venue standards (**NeurIPS**, **ICML**, **ICLR**, **Nature Machine Intelligence**, **Nature Neuroscience**), every single experiment in this repo gotta follow this checklist.

---

## 📋 Empirical Reproducibility Checklist

### 1. Code & Environment Integrity
- [ ] **Dependency Pinning:** All python package dependencies are explicitly locked.
- [ ] **Fixed Random Seeds:** All stochastic operations (PyTorch, NumPy, Python `random`, PettingZoo environments) take an explicit `--seed` parameter.
- [ ] **Hardware Logging:** Experiment logs record CPU/GPU hardware, PyTorch version, and OS platform.

### 2. Information-Theoretic Estimation Standards
- [ ] **Transfer Entropy Estimator:** Report exact hyperparams used for Kraskov (KSG) k-NN estimator ($k$, delay $\tau$, embedding dimension $d$) or neural predictive-gain loss architecture.
- [ ] **Surrogate Baseline (Effective Transfer Entropy):** Always perform surrogate shuffling (Fourier or block-shuffling) to compute baseline noise floor and subtract finite-sample bias ($\mathrm{ETE} = \mathrm{TE} - \mathrm{TE}_{\text{surr}}$).
- [ ] **Confidence Intervals:** All plots include error bands (standard deviation or 95% bootstrap confidence intervals) across at least 5 independent random seeds.

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

---
tags: ["#meta/reproducibility"]
alias: "Reproducibility Protocol"
---

# 🔬 Reproducibility Checklist & Standards

Bro, to make sure our research survives Reviewer #2 and meets top venue standards (**NeurIPS**, **ICML**, **ICLR**, **Nature Machine Intelligence**, **Nature Neuroscience**), every single experiment in this repo gotta follow this checklist.

---

## 📋 Empirical Reproducibility Checklist

> [!important] **A reproducible number is not a supported claim.**
> Everything below reproduces exactly, and for a while we mistook that for evidence. It is not.
> A simulation that satisfies a theory's assumptions by construction will reproduce a confirming
> number every time you run it — see `paper_main/` §2.3, where we retract our own headline
> validation for exactly this reason. Seed discipline is necessary and nowhere near sufficient;
> item 4 below is the one that actually protects you.

### 1. Code & Environment Integrity
- [x] **Minimal dependencies:** The sandbox (`experiments/paper1_rl/`) needs only NumPy + Matplotlib — no GPU, no heavyweight frameworks — so it reproduces on any machine.
- [x] **Fixed Random Seeds:** Every stochastic operation is seeded (`np.random.default_rng`); the sandbox sweeps use seeds `42–46` and reproduce exactly.
- [x] **Deterministic re-run:** `python3 run_experiments.py` regenerates all figures + JSON logs from scratch.

### 2. Information-Theoretic Estimation Standards
- [x] **Transfer Entropy Estimator:** Two independent estimators reported — predictive-gain (Gaussian/Geweke form) and KSG *k*-NN ($k=6$, lag $\Delta=1$, channel-coordinate projection). They agree within 2%.
- [x] **Surrogate Baseline (Effective Transfer Entropy):** Block-shuffled surrogates subtracted for the KSG cross-check ($\mathrm{ETE} = \mathrm{TE} - \mathrm{TE}_{\text{surr}}$).
- [x] **Confidence Intervals:** All sandbox plots show std error bands across 5 seeds.

### 3. Open Dataset Access
- [ ] **Standardized BIDS Access:** For biological recordings, use publicly available OpenNeuro datasets (`ds007764` DUET, `ds007471` Joint Agency EEG) and specify exact commit hashes or BIDS release tags.
- [ ] **Pre-processing Pipelines:** Script all artifact rejection, bandpass filtering, and spatial alignment (FUGW) deterministically.
- [ ] **Preserve the channel noise.** Counter-intuitive but load-bearing: exogenous transmission noise is an *instrument* (`paper_main/` §5.2), so aggressive denoising can destroy the only route to an interventional conclusion. Log what you filtered and why.

### 4. Claim Discipline — the checklist that actually matters
- [ ] **Pure-noise control.** Run every coupling estimator on data with zero true coupling and report what it returns. Ours returned **0.71 "bits"** where the truth was 0. If you skip this, you do not know your estimator's bias at your sample size.
- [ ] **Surrogate correction reported, not just applied.** State the effect size before and after.
- [ ] **Intervention, not observation.** Ablate *and* randomise. Randomisation is ~3× more sensitive; never read a null ablation as zero coupling (`paper_main/` §6).
- [ ] **Report $\hat{\rho}$, the captured share of the value of information**, with both anchors and a bootstrap interval — not a bare significance test (`paper_main/` §8.2).
- [ ] **First-stage $F$ for any instrumented estimate.** Report it *before* the estimate. Ours was $F = 0.2$ on a real system and the point estimate looked perfectly respectable while spanning three orders of magnitude.
- [ ] **State whether the convention-bearing latent $C$ was observed, proxied, or unobserved.**

---

## 🧪 Logging Format Template

When logging an experiment run, create a JSON entry in `experiments/results/logs/`:

```json
{
  "experiment_id": "paper1_rl_sweep_seed42_20260723",
  "timestamp": "2026-07-23T20:00:00",
  "environment": "simple_speaker_listener_v4",
  "seed": 42,
  "bandwidth_bits": [1, 2, 4, 8, 16, 32],
  "te_estimator": "predictive_gain_loss",
  "surrogate_corrected": true,
  "pure_noise_control_bits": 0.0,
  "results": {
    "capacity_bits": [0.42, 0.81, 1.45, 1.98, 2.01, 2.02],
    "sat_dimension": 2
  },
  "hardware": "CPU only — no GPU is used anywhere in this repo",
  "status": "COMPLETED"
}
```

# 🤖 Paper 1 Experiment TODOs

## ✅ Done — NumPy ground-truth sandbox
- [x] Coupled-systems simulator with bandwidth-limited channel (`coupling_lab.py`).
- [x] Predictive-gain transfer-entropy estimator (`L_self − L_joint`, Gaussian/Geweke form).
- [x] Model-free KSG *k*-NN transfer-entropy estimator + effective-TE surrogates.
- [x] Effective-dimensionality estimator (PCA threshold + participation ratio).
- [x] Run sweeps across 5 seeds (42–46); write figures + JSON logs.
- [x] Publication figures: capacity–bandwidth law, efficiency, asymmetry, estimator agreement.
- [x] All three predictions supported; two estimators agree within 2%.

## 🔜 Next — learned-interface (deep RL) version
- [x] `PettingZoo simple_speaker_listener` wrapper (PyTorch) — `run_bandwidth_sweep.py`.
- [x] Learned Gumbel-Softmax discrete channel bottleneck (`gumbel_channel.py`), sweep `B ∈ {1,2,4,8,16,32}`.
- [x] Log task reward alongside measured coupling capacity (predictive-gain TE on message/listener-state trajectories).
- [x] Smoke-test end-to-end once `torch`/`pettingzoo` are installed; fix any API mismatches.
  - PettingZoo 1.26 split MPE out into a separate `mpe2` package (`pettingzoo.mpe` no longer exists) — updated the import and dependency lists.
  - `predictive_gain_te` was returning NaN: the listener's observation includes the env's own built-in comm slots, which are constant (zero variance) since our speaker sends a fixed no-op in favor of the learned side-channel — a constant dimension makes the residual covariance singular (logdet → -inf on both models → NaN on the subtraction). Fixed by dropping zero-variance dimensions before estimating TE.
  - Ran clean for `B ∈ {2, 8}` at 15 episodes/bandwidth: no NaNs/warnings, TE moves the right direction with B. Not a real result yet — 15 episodes is far too few for the policies to converge, this was purely a mechanics check.
- [x] Multi-seed sweep (42–46, 600 episodes/bandwidth) — ran in ~2 min/seed on CPU, much faster than expected.
  - **Interim result:** seed-mean measured TE rises with bandwidth (0.007 → 0.017 → 0.039 → 0.15 → 0.208 → 0.343 bits at B=1..32; Pearson r=0.98 vs. bandwidth) — qualitatively the right direction.
  - **But it does NOT saturate** the way Stage 1 did — still rising at B=32, no plateau. Task eval returns also aren't improving with bandwidth (bouncing between -35 and -111), and per-seed TE values are noisy, with some individual seed/bandwidth cells reading exactly 0.0.
  - Read as: 600 episodes of vanilla REINFORCE is not enough to converge on this task — the policies (especially the speaker, whose only learning signal is backprop-through-channel) haven't learned an efficient code yet, so we're not yet in the regime where the saturation law would show up. Not a refutation of Prediction 1, just an undertrained run.
  - Plot: `experiments/results/plots/stage2_interim_te_vs_bandwidth.png`. Summary: `experiments/results/logs/P1_stage2_summary_5seed.json`.
- [x] Ran a longer 3000-episode/bandwidth follow-up expecting convergence — instead it got **worse**: seed-mean TE correlation with bandwidth dropped from r=0.98 to r=0.50, eval returns got more negative, and 13/30 seed×bandwidth cells read exactly 0.0 bits (policy collapse).
- [x] **Found the actual bug**: `ValueBaseline` was instantiated and added to the optimizer but never called anywhere — its parameters got zero gradient forever, so training was pure high-variance REINFORCE with only a crude per-episode return z-score, no real state-dependent baseline. That's a textbook setup for policy collapse over many updates. Fixed: `baseline(l_obs)` is now called every step, advantage = return − baseline (normalized), the baseline is trained with an MSE loss, a small entropy bonus (`entropy_coef=0.02`) discourages premature collapse, and gradients are clipped (`max_norm=5.0`).
- [x] Re-smoke-tested at 300 episodes post-fix: TE now rises monotonically with bandwidth (0.014 → 0.117 → 0.516 bits at B=2/8/32) and training returns trend downward (improving) instead of drifting. Looks far more stable.
- [x] Reran 5 seeds at 1500 episodes/bandwidth with the fix. Much healthier: correlation with bandwidth back up to r=0.99, zero-TE (collapsed) cells down from 13/30 to 4/30 — the baseline fix clearly mattered.
  - **Still not saturating.** TE = [0.012, 0.018, 0.042, 0.089, 0.127, 0.343] at B=[1,2,4,8,16,32]; successive increments (0.006, 0.025, 0.047, 0.038, 0.216) are *growing*, not shrinking — the opposite of the concave shape Prediction 1 predicts. Eval returns are still deeply negative and non-monotonic across bandwidth, so the policies have not converged to a good task solution yet.
  - **Conclusion: real, clean signal that coupling rises with bandwidth, but this is NOT yet evidence for or against the saturation law.** Need substantially more training and/or a wider bandwidth grid before the shape of the curve can be trusted. Do not cite this run as confirming Prediction 1 under a learned interface.
  - Plot/summary refreshed at `experiments/results/plots/stage2_interim_te_vs_bandwidth.png` / `experiments/results/logs/P1_stage2_summary_5seed.json`.
- [ ] Next real attempt: longer training (likely needs proper compute, not a laptop-scale CPU run) and/or a wider bandwidth grid (e.g. up to 64-128 bits) to actually see whether a plateau appears before claiming Stage 2 validates Prediction 1.

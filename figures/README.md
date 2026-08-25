# 🎨 Publication Figures Vault

This directory stores all publication-ready vector graphics, diagrams, and plots.

These are **auto-generated** by `experiments/paper1_rl/run_experiments.py` (PNG + PDF).
Re-run that script to regenerate them from scratch.

```
figures/
├── fig2_capacity_bandwidth_law.png/.pdf   # concave saturation + ceiling vs d_eff
├── fig3_asymmetry_index.png/.pdf          # asymmetry index vs imposed task role
├── fig4_selfpredictive_efficiency.png/.pdf# C/B vs self-predictive accuracy
└── fig5_estimator_agreement.png/.pdf      # KSG vs predictive-gain estimator agreement
```

> [!warning] **Read these as the superseded validation, not as supporting evidence.**
> The first three appear in the paper as **Figure 1 of `paper_main/` §2.3**, which explains
> why they do not support the theory they appear to. The simulation satisfies the theory's
> assumptions by construction, and for the asymmetry panel a coupling parameter was *imposed*
> on the simulator and then recovered at $r = 1.00$ — a demonstration that the estimator
> inverts the generative model, which is a property of the estimator. `fig5` is not in the
> paper at all; the estimator-agreement result is stated in the text instead.
>
> The figures the paper's *standing* claims rest on live in `paper_main/` directly:
> `fig_oracle_control.png`, `fig_noise_instrument_toy.png`, `fig_noise_instrument_stage2.png`.

### Guidelines:
- Figures are regenerated deterministically (seeded); do not hand-edit.
- Consistent palette: Navy (`#1F4E78`), Steel Blue (`#2E75B6`), Coral (`#E05A47`).

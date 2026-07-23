# 🎨 Publication Figures Vault

This directory stores all publication-ready vector graphics, diagrams, and plots.

These are **auto-generated** by `experiments/paper1_rl/run_experiments.py` (PNG for the
reportlab compiler + PDF for Overleaf). Re-run that script to regenerate them from scratch.

```
figures/
├── fig2_capacity_bandwidth_law.png/.pdf   # Prediction 1 — concave saturation + ceiling vs d_eff
├── fig3_asymmetry_index.png/.pdf          # Prediction 3 — asymmetry index vs task role
├── fig4_selfpredictive_efficiency.png/.pdf# Prediction 2 — C/B vs self-predictive accuracy
└── fig5_estimator_agreement.png/.pdf      # KSG vs predictive-gain estimator agreement
```

### Guidelines:
- Figures are regenerated deterministically (seeded); do not hand-edit.
- Consistent palette: Navy (`#1F4E78`), Steel Blue (`#2E75B6`), Coral (`#E05A47`).

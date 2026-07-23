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
- [ ] `PettingZoo simple_speaker_listener` wrapper (PyTorch).
- [ ] Learned Gumbel-Softmax discrete channel bottleneck, sweep `B ∈ {1,2,4,8,16,32}`.
- [ ] Confirm the saturation law emerges under an *optimized* interface, not just an imposed one.
- [ ] Log task reward alongside measured coupling capacity.

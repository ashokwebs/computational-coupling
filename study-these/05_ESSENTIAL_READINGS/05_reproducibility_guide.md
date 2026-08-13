# 🔬 Reproducibility Checklist & Standards

**Original File:** [`REPRODUCIBILITY.md`](file:///home/charizard/computational-coupling/REPRODUCIBILITY.md)

---

## 📋 Empirical Standards

1. **Fixed Random Seeds**: All experiments seeded via `np.random.default_rng` or PyTorch manual seed across seeds `42–46`.
2. **Surrogate Subtraction**: Always subtraction block-shuffled surrogates for transfer entropy estimation (`cl.effective_te`) to eliminate sample-size bias.
3. **Dual Estimators**: Use both parametric predictive gain (`predictive_gain_te`) and model-free KSG $k$-NN (`ksg_te`).
4. **Eval Episodes**: Always evaluate policies across $\ge 150$ episodes to ensure estimation stability.

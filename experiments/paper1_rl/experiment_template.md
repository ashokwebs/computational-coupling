# 📝 Experiment Log Template: Paper 1 RL Run

**Date:** YYYY-MM-DD  
**Run ID:** `paper1_marl_sweep_seed<SEED>`  
**Author:** Ashok Pasala  

---

## ⚙️ Configuration Parameters
- **Environment:** `mpe/simple_speaker_listener_v4`
- **Random Seed:** `<SEED>`
- **Bandwidth Sweeps (bits):** `[1, 2, 4, 8, 16, 32]`
- **Estimator:** Neural Predictive Gain ($L_{\text{self}} - L_{\text{joint}}$)
- **Epochs:** `1000`
- **Batch Size:** `128`

---

## 📊 Results Summary
| Bandwidth $B$ (bits) | Success Rate (%) | Measured TE (bits/step) | Effective Dim $\dim_{\text{eff}}$ |
| :--- | :--- | :--- | :--- |
| 1 | 42.5% | 0.38 | 2 |
| 2 | 78.1% | 0.82 | 2 |
| 4 | 94.2% | 1.48 | 2 |
| 8 | 98.0% | 1.95 | 2 |
| 16 | 98.5% | 2.01 (Saturated!) | 2 |
| 32 | 98.6% | 2.02 (Saturated!) | 2 |

---

## 💡 Key Takeaways
- Measured Coupling Capacity $C_{\text{couple}}$ clearly saturates at ~2.0 bits/step despite giving the channel 16 or 32 bits!
- Matches Listener's internal effective state dimensionality ($\dim_{\text{eff}} = 2$).
- **Prediction 1 confirmed in MARL!** 🎉

# 🧪 Paper 1 MARL Experiment Testbed

**Paper Title:** *Validating Capacity-Bandwidth Saturation Laws in Multi-Agent RL*  
**Environment:** `PettingZoo` cooperative games (`mpe/simple_speaker_listener_v4`)  
**Target Venues:** NeurIPS / ICML  

---

## 🎯 Goal

Yo! Here we validate **Prediction 1** (Capacity-Bandwidth Saturation Law) and **Prediction 2** (Self-Predictive Accuracy Efficiency) in artificial agents where we got 100% ground-truth access to internal recurrent hidden states ($h_t^A, h_t^B$).

---

## 🛠️ Experimental Setup

1. **Environment:** `simple_speaker_listener_v4` (Speaker and Listener dyad).
2. **Channel Quantization Bottleneck:** Inter-agent communication channel choked via Gumbel-Softmax discrete bottleneck sweeping $B \in [1, 2, 4, 8, 16, 32]$ bits/step.
3. **Metrics Logged:**
   - Task Reward / Success Rate
   - Transfer Entropy Estimate $\hat{\mathrm{TE}}_{A \to B}$ via Neural Predictive-Gain Loss ($L_{\text{self}} - L_{\text{joint}}$)
   - Effective Representational Dimension $\dim_{\text{eff}}(h^B)$ via PCA variance ratio (95% threshold)

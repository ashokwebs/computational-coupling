# 🗺️ Research Roadmap: Theory of Computational Coupling

**Author:** Ashok Pasala (VIT-AP University)  
**Timeline:** 2026 – 2029  
**Target Venues:** NeurIPS, ICML, ICLR, Nature Machine Intelligence, Nature Neuroscience  

---

## 🎯 Strategic Overview

Yo! The goal of this research program is to establish a rigorous, substrate-independent measurement theory for Brain-to-Brain Communication (BBI) and multi-agent interaction, reframing the field away from arbitrary protocol design toward **Coupling Capacity** ($C_{\text{couple}}$).

We execute this vision through **two parallel tracks** across **four venue-targeted papers**.

```
                               ┌─────────────────────────────────────────┐
                               │ Theory of Computational Coupling (BBI)   │
                               └────────────────────┬────────────────────┘
                                                    │
                         ┌──────────────────────────┴──────────────────────────┐
                         ▼                                                     ▼
         ┌────────────────────────────────┐                    ┌────────────────────────────────┐
         │ Track 1: Foundational Theory   │                    │ Track 2: Empirical Roadmap     │
         │ (Paper 0 / Working Draft)      │                    │ (Paper 1 -> Paper 4 Prototype) │
         └────────────────┬───────────────┘                    └────────────────┬───────────────┘
                          │                                                     │
           ┌──────────────┴──────────────┐                   ┌──────────────────┼──────────────────┐
           │ - Formal Framework          │                   │                  │                  │
           │ - Falsifiable Predictions   │                   ▼                  ▼                  ▼
           │ - Related Work Canon        │                Paper 1            Paper 2            Paper 3 & 4
           │ - Falsifiability & Scope    │              (Multi-Agent RL)   (Hyperscanning)   (Causal & Prototype)
           └─────────────────────────────┘
```

---

## 📄 Track 1: Foundational Paper (`paper/`)

* **Title:** *A Theory of Computational Coupling Between Intelligent Systems: Toward a General Foundation for Brain-to-Brain Communication*
* **Status:** Working Draft (Sections 3 & 4 complete; Sections 1, 2, 6, 8 structured outlines).
* **Next Steps:**
  - Expand Section 1 (Intro) with the Shannon telecommunications analogy hook.
  - Populate Section 2 (Related Work) with verified BibTeX entries from `paper/references.bib`.
  - Add explicit falsifiability teeth in Section 6.
  - Add limitations & ethics of stimulation in Section 8.

---

## 🔬 Track 2: The Multi-Year Empirical Roadmap

### 🧪 Paper 1: Multi-Agent RL Testbed Validation
* **Target Venues:** NeurIPS / ICML
* **Goal:** Validate Prediction 1 (Capacity-Bandwidth Saturation Law) and Prediction 2 (Self-Predictive Accuracy Efficiency) in artificial agents where we got 100% ground-truth access to internal states ($h_t^A, h_t^B$).
* **Methodology:**
  - Environment: `PettingZoo` cooperative multi-agent environments (`mpe/simple_speaker_listener_v4`).
  - Interface Bottleneck: Sweep channel quantization $B \in [1, 2, 4, 8, 16, 32]$ bits/step via Gumbel-Softmax discrete channels.
  - Estimator: Neural predictive-gain Transfer Entropy estimator ($L_{\text{self}} - L_{\text{joint}}$).
* **Milestone:** Plot $C_{\text{couple}}$ vs $B$ curve to empirically verify concave saturation at $\min(d_A, d_B)$.

---

### 🧠 Paper 2: Biological Validation via Human Hyperscanning
* **Target Venues:** Nature Neuroscience / ICLR
* **Goal:** Test whether the Capacity-Bandwidth Saturation Law and Role Asymmetry hold in biological human brains during real interaction.
* **Methodology:**
  - Datasets: OpenNeuro `ds007764` DUET (18 face-to-face French dialogue dyads with dual 64-channel EEG) and `ds007471` (Joint Agency EEG).
  - Spatial Alignment: Fused Unbalanced Gromov-Wasserstein (FUGW) optimal transport alignment across subjects.
  - Temporal Latent Extraction: Pre-trained EEG Foundation Model (**LaBraM** / **LUNA**).
* **Milestone:** Show that inter-brain directed information tracks task role and saturates at effective neural representational dimensionality.

---

### ⚡ Paper 3: Causal Manipulation Paradigm
* **Target Venues:** Nature Machine Intelligence
* **Goal:** Perform causal intervention by manipulating theory-predicted variables (feedback latency, noise, channel choking) non-invasively in human dyads.
* **Methodology:**
  - Paradigm: Dual-subject motor/visual tracking task linked via narrow digital/TMS interface.
  - Causal Intervention: Intentionally degrade interface bandwidth and feedback lag $\tau$.
* **Milestone:** Prove that task performance and measured coupling capacity move together strictly as predicted by the theory.

---

### 🤖 Paper 4 / Prototype: The Learned Brain Communication Protocol (BCP)
* **Target Venues:** Nature / NeurIPS
* **Goal:** Use Coupling Capacity $C_{\text{couple}}$ as an explicit loss function to *learn* an optimal closed-loop interface between two intelligent systems.
* **Methodology:**
  - Training Objective: $\mathcal{L} = -\lambda_1 C_{\text{couple}} + \lambda_2 \text{Distortion} + \lambda_3 \text{Bandwidth}$.
  - System: Closed-loop BBI prototype connecting artificial agents or non-invasive human dyads on a narrow cooperative task.
* **Milestone:** The world's first empirically derived, bandwidth-optimal Brain Communication Protocol! 🚀

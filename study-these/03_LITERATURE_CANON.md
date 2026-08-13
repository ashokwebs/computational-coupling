# 📚 Literature Canon & Map

This document synthesizes the **40-paper core canon** stored in [`literature/summaries/`](file:///home/charizard/computational-coupling/literature/summaries/) alongside the frontier reading list in [`tosee.md`](file:///home/charizard/computational-coupling/tosee.md).

---

## 🗺️ Categorized Reading Canon

### 1. Information Theory, Causality & Measurement
Understanding Transfer Entropy, Directed Information, Granger Causality, and Partial Information Decomposition.

| Paper | Title | Key Relevance |
|:---|:---|:---|
| **#12** | Shannon (1948) | *A Mathematical Theory of Communication* — Baseline channel capacity. |
| **#11** | Schreiber (2000) | *Measuring Information Transfer* — Formulates Transfer Entropy ($TE$). |
| **#22** | Granger (1969) | *Investigating Causal Relations by Econometric Models* — Precedence-based causality. |
| **#23** | Permuter et al. (2009) | *Directed Information & Feedback Capacity* — Capacity of channels with feedback. |
| **#16** | Tishby et al. (1999) | *The Information Bottleneck Method* — Tradeoff between compression and prediction. |
| **#40** | Williams & Beer (2010) | *Partial Information Decomposition (PID)* — Disentangling redundant, unique, and synergistic information. |

---

### 2. Emergent AI Communication & Multi-Agent RL
How artificial agents learn protocols, and where traditional RL training fails to induce listener usage.

| Paper | Title | Key Relevance |
|:---|:---|:---|
| **#03** | Foerster et al. (2016) | *DIAL: Differentiable Inter-Agent Learning* — Backpropagating through continuous communication channels. |
| **#17** | Sukhbaatar et al. (2016) | *CommNet* — Continuous communication vector averaging across agents. |
| **#18** | Jang et al. (2016) | *Gumbel-Softmax* — Continuous relaxation for discrete communication bottlenecks. |
| **#19** | Mordatch & Abbeel (2017) | *Emergent Compositional Language* — Grounded communication in physical multi-agent environments. |
| **#20** | Lazaridou et al. (2018) | *Emergence of Language in Referential Games* — Visual grounded signaling games. |
| **#21** | Terry et al. (2021) | *PettingZoo* — Multi-agent RL standard library used in our empirical testbed. |

---

### 3. Brain-to-Brain Interfaces (BBI) & BCI Hardware
Historical landmark BBI systems and their conceptual limitations.

| Paper | Title | Key Relevance |
|:---|:---|:---|
| **#01** | Pais-Vieira et al. (2013) | *A Brain-to-Brain Interface for Real-Time Sharing of Sensorimotor Information* — First rat-to-rat ICMS BBI. |
| **#02** | Rao et al. (2014) | *A Direct Brain-to-Brain Interface in Humans* — Non-invasive motor cortex EEG-to-TMS trigger. |
| **#04** | Jiang et al. (2019) | *BrainNet: A Multi-Person Brain-to-Brain Interface* — 3-person collaborative game BBI. |
| **#28** | LaRocco et al. (2020) | *Optimizing CBI Parameters* — Engineering bottleneck trade-offs. |
| **#29** | Shi et al. (2024) | *Max Information Rate Visual BCI* — High-throughput non-invasive BCI. |
| **#30** | Vakilipour et al. (2024) | *BBI Review* — Systematic survey of current hardware limits. |

---

### 4. Neural Decoding & Foundation Models
Pretrained foundation models for EEG, fMRI, and invasive neuroprosthetics.

| Paper | Title | Key Relevance |
|:---|:---|:---|
| **#07** | Jiang et al. (2024) | *LaBraM* — Large Brain Model for EEG pretraining. |
| **#08** | Caro et al. (2024) | *BrainLM* — Foundation model for fMRI time series. |
| **#09** | Scotti et al. (2024) | *MindEye2* — Shared fMRI-to-image reconstruction. |
| **Frontier** | Défossez et al. (2023) | *Decoding speech perception from non-invasive brain recordings* (Nature MI). |
| **Frontier** | Willett et al. (2023) | *High-performance speech neuroprosthesis* (Nature). |
| **Frontier** | Wang et al. (2024) | *Brain-JEPA* — Joint Embedding Predictive Architecture for fMRI. |

---

### 5. Hyperscanning & Inter-Brain Synchrony
Dual-brain recordings (EEG/fMRI) in interacting human subjects.

| Paper | Title | Key Relevance |
|:---|:---|:---|
| **#13** | Hasson et al. (2010) | *Brain-to-Brain Coupling* — Shared neural response across speakers and listeners. |
| **#15** | Montague et al. (2002) | *Hyperscanning* — Multi-subject fMRI during economic games. |
| **#26** | Zamm et al. (2024) | *EEG Hyperscanning Practical Guide* — Best practices and pitfalls. |
| **#27** | Markiewicz et al. (2024) | *Brain-to-Brain Coupling Forecasts Joint Action* — Task success correlates with coupling. |
| **#31** | Yamasaki et al. (2026) | *DUET OpenNeuro Dataset (`ds007764`)* — Dual EEG dyadic dataset. |
| **#32** | Zhou et al. (2026) | *Joint Agency EEG Dataset (`ds007471`)* — OpenNeuro joint action dataset. |

---

### 6. Control Theory & Rate Distortion
Constraints on feedback, data rates, and dynamical system stability.

| Paper | Title | Key Relevance |
|:---|:---|:---|
| **#37** | Tatikonda & Mitter (2004) | *Control Under Communication Constraints* — Feedback capacity and control. |
| **#38** | Nair et al. (2004) | *Data Rate Theorem* — Minimum data rate needed to stabilize an unstable linear system. |
| **#06** | McParlin et al. (2022) | *Active Inference & Communication* — Free energy principle applied to dyadic interaction. |

---

### 7. Neural Manifolds & Synchronization
Intrinsic dimensionality of neural representations and coupled oscillators.

| Paper | Title | Key Relevance |
|:---|:---|:---|
| **#33** | Gao et al. (2015) | *Simplicity of Neural Population Codes* — Effective dimensionality of manifold trajectories. |
| **#34** | Gallego et al. (2017) | *Neural Manifolds for Movement Control* — Subspace stability across tasks and time. |
| **#35** | Kuramoto (1975) | *Coupled Oscillator Phase Synchronization* — Classic model of emergent synchronization. |
| **#36** | Pecora & Carroll (1990) | *Synchronization in Chaotic Systems* — Master stability functions. |

---

### 8. Frontier Cross-Subject Alignment (`tosee.md`)
Methods for aligning representational manifolds across distinct brains without paired training data.

- **MindAligner** (ICML 2025): [arXiv:2502.05034](https://arxiv.org/abs/2502.05034) — Learns a "Brain Transfer Matrix" mapping new subject fMRI to target space.
- **Platonic Representations in the Human Brain** (2026): [arXiv:2605.20496](https://arxiv.org/abs/2605.20496) — Unsupervised orthogonal-rotation alignment of fMRI embedding spaces.
- **Thual et al. (2022) / FUGW**: Optimal transport aligning cortical topographies (`literature/summaries/05_Thual_2022_FUGW_Optimal_Transport.md`).

---

## 📖 Accessing Summaries
All 40 full paper summaries are located at [`literature/summaries/`](file:///home/charizard/computational-coupling/literature/summaries/).

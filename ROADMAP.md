---
tags: [#meta/roadmap, #paper/plan]
alias: "4-Paper Strategic Roadmap"
---

# 🗺️ Research Roadmap: Theory of Computational Coupling

> [!warning] **SUPERSEDED — describes the v0.3.0 BBI framing (July 2026 and earlier).**
> The program was reframed on 2026-07-26. The four-paper BBI roadmap below assumed an EEG/TMS lab and dyadic data collection that were never available, and Stage 2 produced a result that reframed the question entirely. The current program is **`opp.md`** (the idea), **`paper2/`** (the paper), and **`handoff.md`** (state + next steps). BBI is now a *case study* the framework explains, not the subject.
>
> This file is kept because Papers 1–3 below contain reusable experimental design, and because the Stage 1/Stage 2 contrast turned out to be the accidental control that isolated the missing variable. Do not plan from it.

**Authors:** Ashok Pasala, Snigdha Gorai (VIT-AP University)  
**Timeline:** 2026 – 2029 *(as originally planned)*  
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
* **Status:** v0.3.0 — formal core complete **and empirically supported in a ground-truth simulation.**
  - ✅ Intro with Shannon analogy; explicit contributions list.
  - ✅ Related Work populated from verified `paper/references.bib` (all 15 keys resolve).
  - ✅ **Dimensional Bottleneck theorem + proof** (Sec. 4): ceiling $=\bar{c}\cdot\min(d_i,d_j)$.
  - ✅ **Proof-of-Concept validation** (Sec. 7): all three predictions supported; two estimators agree within 2%.
  - ✅ Falsifiability teeth, open problems, ethics of stimulation.
* **Next Steps:** biological validation (Paper 2); general concavity proof; robust $d_{\text{eff}}$ estimation on real recordings.

---

## 🔬 Track 2: The Multi-Year Empirical Roadmap

### 🧪 Paper 1: Multi-Agent RL Testbed Validation
* **Target Venues:** NeurIPS / ICML
* **Goal:** Validate all three predictions in artificial systems with 100% ground-truth access to internal states.
* **Stage 1 — analytical control (✅ DONE, `experiments/paper1_rl/`):** coupled VAR systems + bandwidth-limited channel in pure NumPy. All three predictions supported; capacity saturates at $0.39\cdot\min(d_{\text{eff}})$ bits, flat in $B$; predictive-gain and KSG estimators agree within 2%. This is the analytical control for the learned-interface study below.
* **Stage 2 — learned interface (next):**
  - Environment: `PettingZoo` cooperative games (`simple_speaker_listener`).
  - Interface Bottleneck: **learned** Gumbel-Softmax discrete channel, sweep $B \in [1,2,4,8,16,32]$ bits/step.
  - Estimator: neural predictive-gain Transfer Entropy ($L_{\text{self}} - L_{\text{joint}}$).
* **Milestone:** show the saturation law emerges under an *optimized* interface, not only an imposed one.

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

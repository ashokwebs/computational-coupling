---
tags: [#meta/dashboard, #overview]
alias: "Lab Home & Master Dashboard"
---

# 🧠 Theory of Computational Coupling — Master Lab Dashboard

> [!danger] **Reframed 2026-07-26 — start with [[opp]], [[handoff]], and `paper2/`.**
> The dashboard below describes the v0.3.0 brain-to-brain framing. The current question is **"when does information flowing between two adaptive systems actually constitute communication, and how would you know?"** — answered by showing that functional coupling is an *interventional* quantity, not identifiable from the observational measures four fields currently use. Links below still work but describe the older program.

> [!abstract] **Core Research Vision (v0.3.0 — superseded)**
> Developing a substrate-independent, directed, information-theoretic measurement theory (**Coupling Capacity** $C_{\text{couple}} = \sup_{g \in \mathcal{A}} \mathrm{TE}_{A \to B}^g$) for brain-to-brain communication, targeting top ML/neuro venues (NeurIPS, ICML, ICLR, Nature Machine Intelligence, Nature Neuroscience).

---

## 🧭 Interactive Navigation & Visual Canvases

```
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                         INTERACTIVE CANVAS BOARDS                           │
 ├──────────────────────────────────────┬──────────────────────────────────────┤
 │ 🗺️ [[Computational_Coupling_Architecture.canvas|Architecture Map]]          │
 │ 📚 [[Literature_Canon_Map.canvas|Literature Canon Visual Graph]]             │
 └──────────────────────────────────────┴──────────────────────────────────────┘
```

> [!tip] **Quick Access Maps of Content (MOCs)**
> - 📐 **[[MOC_Theory|Theory MOC]]** — State space manifolds, transfer entropy estimators, capacity saturation proofs.
> - 📚 **[[MOC_Literature|Literature Canon MOC]]** — 15 core paper breakdowns, FUGW, LaBraM, BrainLM, Nakamura defense.
> - 🗺️ **[[ROADMAP|4-Paper Strategic Roadmap]]** — Empirical roadmap spanning MARL (Paper 1) to Nature Prototype (Paper 4).
> - 📔 **[[diary/README|Research Journal MOC]]** — 5-day research log (July 19 – July 23, 2026).

---

## 📊 Core Theoretical Foundations & Load-Bearing Claims

> [!important] **Definition: Coupling Capacity**
> $$C(A \to B) \;=\; \sup_{g \,\in\, \mathcal{A}(B)} \; \mathrm{TE}_{A \to B}(\Delta; g) \;=\; \sup_{g \,\in\, \mathcal{A}(B)} I\big(x_A(t)\, ;\, x_B(t+\Delta) \,\big|\, x_B(\le t)\big)$$

> [!math] **The Three Falsifiable Predictions**
> 1. **[[theory/proofs|Capacity-Bandwidth Saturation Law]]:** $C(A \to B; B)$ flattens concavely, saturating at $\min(\dim_{\text{eff}}(\mathcal{M}_A), \dim_{\text{eff}}(\mathcal{M}_B))$.
> 2. **[[theory/mathematics|Self-Predictive Accuracy Efficiency]]:** $C(A \to B)/B$ scales monotonically with internal world model accuracy $R_A, R_B$.
> 3. **[[theory/definitions|Asymmetry Index Tracks Role]]:** Directional asymmetry $A = \frac{C_{A \to B} - C_{B \to A}}{C_{A \to B} + C_{B \to A}}$ tracks task leadership vs followership.

---

## 🔬 Literature Threat Matrix & Canon Highlights

| Paper Title | Main Contribution | Similarity Threat | Strategic Defense Link |
| :--- | :--- | :--- | :--- |
| **[[literature/summaries/10_Nakamura_2024_Representation_Transfer\|Nakamura et al. (2024)]]** | Zero-shot unsupervised hyperspherical transfer | 🚨 **95% (High Threat)** | Passive transfer vs Active closed-loop control ($C_{\text{couple}}$) |
| **[[literature/summaries/09_Scotti_2024_MindEye2\|MindEye2 (Scotti et al. 2024)]]** | Shared-subject fMRI visual perception reconstruction | ⚠️ **90% (High)** | Spatial semantic decoder baseline |
| **[[literature/summaries/05_Thual_2022_FUGW_Optimal_Transport\|FUGW (Thual et al. 2022)]]** | Optimal Transport cortical alignment | 🔵 **70% (Low)** | Geometric routing engine |
| **[[literature/summaries/03_Foerster_2016_DIAL_MARL\|DIAL (Foerster et al. 2016)]]** | Emergent communication via channel backprop | 🔵 **75% (Low)** | Protocol optimization engine |
| **[[literature/summaries/06_McParlin_2022_Active_Inference\|Active Inference (McParlin 2022)]]** | Variational Free Energy minimization | 🔵 **85% (High)** | Biological teleology engine |

---

## 📑 Working Paper & Outputs

- 📄 **Master LaTeX Paper Source:** [[paper/main.tex|paper/main.tex]]
- 📑 **Compiled PDF Report:** [[paper/output/paper.pdf|paper/output/paper.pdf]]
- 📁 **Complete Reference Archives:** [[damn_sources/computational_coupling_foundation|damn_sources master archive]]

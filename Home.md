---
tags: ["#meta/dashboard", "#overview"]
alias: "Lab Home & Master Dashboard"
---

# 🧠 Theory of Computational Coupling — Master Lab Dashboard

> [!danger] **Reframed 2026-07-26. Merged into one paper 2026-08-25 — start with [[opp]], [[handoff]], and `paper_main/`.**
> The dashboard below describes the v0.3.0 brain-to-brain framing. The current question is **"when does information flowing between two adaptive systems actually constitute communication, and how would you know?"** — answered by showing that functional coupling is an *interventional* quantity, not identifiable from the observational measures four fields currently use. Links below still work but describe the older program.

> [!abstract] **Core Research Vision (v0.3.0 — superseded)**
> Developing a substrate-independent, directed, information-theoretic measurement theory (**Coupling Capacity** $C_{\text{couple}} = \sup_{g \in \mathcal{A}} \mathrm{TE}_{A \to B}^g$) for brain-to-brain communication, targeting top ML/neuro venues (NeurIPS, ICML, ICLR, Nature Machine Intelligence, Nature Neuroscience).

---

## 🧭 Navigation

> [!tip] **Start here**
> - 💡 **[[opp|opp.md]]** — the current idea, in prose. Read this first.
> - 📄 **[[paper_main/main.tex|paper_main/main.tex]]** — *the* paper. 36 pp. Build: `cd paper_main && ./build.sh`.
> - 🧭 **[[handoff|handoff.md]]** — state of the programme + next steps.
> - 📔 **[[diary/README|Research Journal]]** — the research log.
> - 🗺️ **[[ROADMAP|ROADMAP.md]]** — the old 4-paper plan, kept with a superseded banner for context.
>
> The MOC files and the two `.canvas` boards were deleted on 2026-08-25 — they indexed the
> superseded v0.3.0 framing and had drifted badly out of date.

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

- 📄 **The paper (LaTeX source):** [[paper_main/main.tex|paper_main/main.tex]] — *Understanding Is Not Observable*, 36 pp. The single authoritative manuscript.
- 📑 **Compiled PDF:** [[paper_main/main.pdf|paper_main/main.pdf]] — build with `cd paper_main && ./build.sh`
- 🗄️ **Gone:** `paper/` and `paper2/` were merged into `paper_main/` on 2026-08-25 and deleted. `paper/`'s formalism is `paper_main/` §2; `paper2/` is the rest of the paper. Recoverable from git history at commit `94eca22` if ever needed.
- 📁 **Complete Reference Archives:** [[damn_sources/computational_coupling_foundation|damn_sources master archive]]

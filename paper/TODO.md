# 📝 Paper Writing Tasks & TODOs

**Target Paper:** *A Theory of Computational Coupling Between Intelligent Systems*  
**Primary Venues:** NeurIPS / ICML / Nature Neuroscience  

---

## 📌 Section Status & Pending Actions

- [x] **Abstract (`paper/sections/abstract.tex`)** — Fully drafted.
- [x] **Introduction (`paper/sections/introduction.tex`)** — Drafted with the Shannon telecommunications analogy hook.
- [ ] **Related Work (`paper/sections/related_work.tex`)** — Expand text with explicit technical contrasts against FUGW \cite{thual2022aligning} and Nakamura et al. \cite{nakamura2024unsupervised}.
- [x] **Theory (`paper/sections/theory.tex`)** — Formal core completed ($C_{\text{couple}}$ definition & Predictions 1–3).
- [x] **Dimensional Bottleneck (Sec. 4)** — Theorem + proof; ceiling $= \bar{c}\cdot\min(d_i,d_j)$, with $\bar{c}$ measured empirically ($\approx0.39$ bits/dim).
- [x] **Proof-of-Concept / Validation (Sec. 7)** — Ground-truth simulation supports all three predictions; 3 embedded figures + results table; two estimators agree within 2%.
- [x] **Discussion & Limitations** — Ethics paragraph on TMS/microstimulation expanded; open problems (general concavity, estimating $d_{\text{eff}}$) added.
- [x] **Conclusion** — Updated to reflect empirical evidence.

---

## 🛠️ Overleaf Compilation & PDF Validation

- [x] Verify BibTeX keys match `paper/references.bib`.
- [x] Test compilation without syntax errors (`python3 paper/compile_paper.py`).
- [x] Synchronize `paper/` directory with main Overleaf project repository.

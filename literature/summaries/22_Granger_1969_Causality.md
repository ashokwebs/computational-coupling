---
tags: ["#literature/paper", "#paper/extended-canon"]
alias: "22_Granger_1969_Causality"
---

# Research Paper Report: Investigating Causal Relations by Econometric Models and Cross-Spectral Methods

**Author:** Clive W. J. Granger
**Publication Year:** 1969
**Venue:** *Econometrica*, 37(3):424–438
**DOI/arXiv:** `10.2307/1912791`
**Category:** (3) Directed information / Granger causality foundations
**Role in Our Work:** **Foundational historical precursor, not a threat.** Predates and motivates Massey's directed-information formalization (already canon).

---

## 📌 Abstract & Architecture
Proposes an operational, testable definition of causality between two time series in terms of predictability: $X$ "Granger-causes" $Y$ if past values of $X$ improve the prediction of $Y$ beyond what past values of $Y$ alone provide. Formalized via linear vector-autoregressive (VAR) models and cross-spectral decomposition, letting the cross-spectrum between two series be split into components attributable to each directional causal arm of a feedback loop, with measures of causal lag and strength.

## 🔗 Connection to Computational Coupling Theory
Granger causality is the linear-Gaussian special case that Schreiber's Transfer Entropy (canon #11) and Massey's Directed Information (already cited, `massey1990causality`) generalize to arbitrary nonlinear, non-Gaussian dependence — for jointly Gaussian VAR processes, Granger causality and Transfer Entropy are provably equivalent. It is worth citing precisely because reviewers steeped in econometrics/neuroscience will reach for "isn't this just Granger causality?" — the honest answer is that our Coupling Capacity $C(i\to j;B)$ is a *directed-information-theoretic generalization* of the Granger-causality intuition, additionally maximized over bandwidth-constrained interfaces rather than computed on a fixed observed channel. Citing Granger alongside Massey/Schreiber shows we know the full lineage rather than presenting Transfer Entropy as if it appeared from nowhere.

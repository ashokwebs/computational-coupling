---
tags: [#literature/paper, #paper/round2-TE-methods]
alias: "39_Vicente_2011_Transfer_Entropy_Neuroscience"
---

# Research Paper Report: Transfer Entropy — A Model-Free Measure of Effective Connectivity for the Neurosciences

**Authors:** Raul Vicente, Michael Wibral, Michael Lindner, Gordon Pipa
**Publication Year:** 2011
**Venue:** *Journal of Computational Neuroscience*, 30:45–67
**DOI/arXiv:** `10.1007/s10827-010-0262-3`
**Category:** (12) Transfer entropy estimation practice / partial information decomposition
**Role in Our Work:** **Practical methods reference — refines Kraskov-style TE estimation for real, noisy neural time series.**

---

## 📌 Abstract & Architecture
Applied methods paper (companion to the TRENTOOL MATLAB toolbox, Lindner et al. 2011, *BMC Neuroscience*) that works through the practical machinery needed to compute Transfer Entropy reliably on real electrophysiological time series: choosing embedding dimension and delay via nonuniform embedding, selecting the source-target interaction delay $u$, using Kraskov-Stögbauer-Grassberger (KSG) nearest-neighbor estimators (`already cited as 11_Schreiber_2000`'s natural estimator, see also the vault's Kraskov 2004 entry) rather than naive binning to avoid severe bias in continuous, high-dimensional neural data, and establishing non-parametric surrogate-data significance testing (time-shifted/trial-shuffled surrogates) to guard against spurious "significant" TE driven by autocorrelation or shared input rather than genuine directed coupling.

## 🔗 Connection to Computational Coupling Theory
This is the applied-neuroscience "how do you actually compute this without fooling yourself" companion to the pure-theory Transfer Entropy definition already anchoring the theory (`11_Schreiber_2000`) — directly load-bearing for Paper 2's empirical pipeline on `ds007764`/`ds007471`. Two points are critical for our estimator design: (1) the embedding-parameter selection procedure (source/target history length, interaction delay) is exactly the practical step needed before any Coupling Capacity estimate can be computed from real EEG, since a poorly chosen embedding will bias $\widehat{C}(i\to j;B)$ in either direction; (2) the surrogate-testing framework is the field-standard defense against precisely the "superficial synchrony" critique already flagged in Part 2 of `literature_review.md` — shared external stimulus drive (e.g. both participants hearing the same audio) can inflate naive TE, and time-shifted/trial-shuffled surrogates are the standard tool to null this out and isolate genuinely directional information flow. Should be the primary Methods citation for however the empirical Transfer-Entropy estimator in Paper 2 is implemented.

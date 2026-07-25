---
tags: [#literature/paper, #paper/extended-canon]
alias: "27_Markiewicz_2024_Brain_to_Brain_Coupling_Forecasts_Joint_Action"
---

# Research Paper Report: Brain-to-Brain Coupling Forecasts Future Joint Action Outcomes

**Authors:** Roksana Markiewicz, Katrien Segaert, Ali Mazaheri
**Publication Year:** 2024
**Venue:** *iScience*, 27(9):110802
**DOI/arXiv:** `10.1016/j.isci.2024.110802`
**Category:** (5) EEG/fMRI hyperscanning beyond current canon
**Role in Our Work:** **Strong supportive empirical evidence for Predictions 2 & 3, not a threat.**

---

## 📌 Abstract & Architecture
Dual-EEG hyperscanning study of pairs performing a synchronized timing/tapping joint-action task. Finds that trial-to-trial success/failure of the joint action is predicted by the directional relationship between partners' theta-band activity: an *inverse* (anti-correlated) relationship between partners' theta dynamics on the preceding trial predicts successful coordination on the next trial, whereas theta activity moving in lockstep (synchronized) predicts failure — i.e., successful teamwork requires **asymmetric, complementary** trial-to-trial adaptation, not symmetric mirroring.

## 🔗 Connection to Computational Coupling Theory
This is close to a direct empirical validation, in real dyadic brain data, of two of our three predictions simultaneously. It supports **Prediction 3** (directional asymmetry tracks task role) by showing task success depends on an asymmetric, directional inter-brain relationship rather than symmetric synchrony — echoing our claim that raw "synchrony" is the wrong metric and directed/asymmetric information flow is the right one. It also bears on **Prediction 2** (systems with better self-predictive world models extract more capacity per bit): the predictive result itself (past neural coupling forecasts future joint-action outcome) is exactly the kind of predictive-gain signal ($L_{\text{self}} - L_{\text{joint}}$) our neural-predictive-gain Transfer Entropy estimator (named in `ROADMAP.md` Stage 2) is designed to quantify. Strong candidate citation for Paper 2's introduction as prior human evidence motivating the theory, and a candidate benchmark dataset/finding to try to reproduce with our own TE-based estimator.

---
tags: [#literature/paper, #paper/round2-control]
alias: "38_Nair_2004_Data_Rate_Theorem"
---

# Research Paper Report: Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates

**Authors:** Girish N. Nair, William S. Evans
**Publication Year:** 2004
**Venue:** *SIAM Journal on Control and Optimization*, 43(2):413–436
**DOI/arXiv:** `10.1137/S0363012902402116`
**Category:** (11) Rate-distortion / control under communication constraints
**Role in Our Work:** **Foundational — the "data-rate theorem": a sharp bit-rate threshold below which closed-loop stabilization is provably impossible.**

---

## 📌 Abstract & Architecture
Proves the "data-rate theorem" for stochastic linear systems: a plant with unstable open-loop dynamics (eigenvalues with modulus $>1$) can be stabilized in a mean-square sense over a rate-limited, noiseless (or fading) digital feedback channel *if and only if* the channel's data rate exceeds $\sum \log_2 |\lambda_i|$ summed over the plant's unstable eigenvalues — a clean, tight necessary-and-sufficient bit-rate threshold, with no coding scheme able to do better and simple quantized encoders able to achieve it. Below this rate, no controller of any kind can stabilize the system, however cleverly designed.

## 🔗 Connection to Computational Coupling Theory
Supplies the sharpest available existence proof that bandwidth-constrained control has a **hard, non-negotiable capacity threshold** rather than a merely gradual degradation — directly reinforcing (from an entirely independent, deterministic-control-theory route) the qualitative shape Prediction 1 predicts for $C(i\to j;B)$: below a critical $B$, coupling/coordination is not just weaker but categorically impossible, and above the saturation point additional bandwidth buys nothing. For Paper 3, the Nair-Evans threshold is a template for a falsifiable, quantitative version of Prediction 1: rather than "capacity saturates" as a qualitative claim, this literature suggests deriving a specific closed-form threshold (analogous to $\sum\log_2|\lambda_i|$) below which two coupled systems provably cannot maintain a shared task-relevant trajectory, expressible in terms of the "instability" (unpredictability growth rate) of the systems being coupled — giving an unusually concrete, testable bridge between the theory's abstract $\sup$-over-interfaces formulation and an operational bits/sec number that could be manipulated experimentally (e.g. artificially throttling feedback latency/bandwidth in a closed-loop BBI or human-agent teaming task and looking for the predicted phase transition rather than a smooth decline).

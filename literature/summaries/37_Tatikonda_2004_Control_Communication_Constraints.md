---
tags: [#literature/paper, #paper/round2-control]
alias: "37_Tatikonda_2004_Control_Communication_Constraints"
---

# Research Paper Report: Control Under Communication Constraints

**Authors:** Sekhar Tatikonda, Sanjoy Mitter
**Publication Year:** 2004
**Venue:** *IEEE Transactions on Automatic Control*, 49(7):1056–1068
**DOI/arXiv:** `10.1109/TAC.2004.831187`
**Category:** (11) Rate-distortion / control under communication constraints
**Role in Our Work:** **Foundational — extends the bandwidth-vs-capacity tradeoff to closed-loop control, directly motivating Paper 3.**

---

## 📌 Abstract & Architecture
Studies control of a plant when the controller and plant are connected through a rate-limited, noisy communication channel rather than an ideal wire, considering both the case where the encoder is co-located with the plant and the case where encoder and controller are geographically separated observing only outputs. Derives upper and lower bounds on the channel rate required to achieve stabilization, estimation, or general control objectives, and — crucially — proves that in the feedback setting, the relevant capacity notion is **directed information across the feedback loop**, not ordinary (feedback-free) Shannon channel capacity, echoing and extending Massey's earlier feedback-capacity result (already in the vault as the ancestor of `23_Permuter_2009`).

## 🔗 Connection to Computational Coupling Theory
This is the closed-loop control-theoretic sibling of the exact question our theory poses for open-loop/observational coupling, and is the most direct precedent for **Paper 3** (causal manipulation of feedback latency/bandwidth between two coupled systems). Tatikonda & Mitter's central result — that directed information, not mutual information, is the right capacity notion once feedback is present — is the control-theory analog of `23_Permuter_2009`'s information-theory result, and together they triangulate on the same conclusion from two different literatures: whenever there's a closed loop (as in any live BBI or dyadic interaction with mutual influence, not just one-way transmission), $\sup I(X;Y)$ is the wrong quantity and $\sup$ directed information / Transfer Entropy is the right one. For Paper 3 specifically, this paper's rate bounds for stabilization give a template for deriving analogous bounds on the *bandwidth* required for one coupled system to keep another's error/divergence from its own predictive model bounded — i.e., a control-theoretic version of Prediction 1's saturation claim, phrased as "how many bits/sec are needed to keep $j$ 'stabilized' relative to $i$'s intended trajectory," directly generalizable to feedback-latency and packet-loss manipulations.

---
tags: ["#literature/paper", "#paper/extended-canon"]
alias: "23_Permuter_2009_Directed_Information_Feedback_Capacity"
---

# Research Paper Report: Finite State Channels with Time-Invariant Deterministic Feedback

**Authors:** Haim H. Permuter, Tsachy Weissman, Andrea J. Goldsmith
**Publication Year:** 2009
**Venue:** *IEEE Transactions on Information Theory*, 55(2):644–662
**DOI/arXiv:** `arXiv:cs/0608070`
**Category:** (3) Directed information / Granger causality foundations
**Role in Our Work:** **Foundational, not a threat.** Direct follow-up to Massey (1990), already canon.

---

## 📌 Abstract & Architecture
Extends Massey's directed-information characterization of feedback capacity from memoryless channels to finite-state channels with time-invariant deterministic feedback. Shows that for indecomposable channels with no intersymbol interference, channel capacity equals the limit of the maximum of *normalized directed information* $I(X^n \to Y^n)/n$ between input and output sequences — i.e., directed information (not ordinary mutual information) is the correct capacity-achieving quantity whenever a feedback loop is present.

## 🔗 Connection to Computational Coupling Theory
This is the rigorous information-theoretic proof that, in the presence of feedback, ordinary mutual information $I(X;Y)$ is the *wrong* quantity to maximize and directed information $I(X^n \to Y^n)$ is the correct one — precisely the justification our theory needs for defining Coupling Capacity in terms of Transfer Entropy/directed information rather than symmetric mutual information, given that brain-to-brain and multi-agent interaction is inherently a closed feedback loop (sender affects receiver affects sender). Strengthens the mathematical grounding of the $\sup$ in $C(i\to j;B)$: it is a feedback-capacity problem in Permuter-Weissman-Goldsmith's sense, not a plain channel-capacity problem in Shannon's (canon #12) original memoryless sense.

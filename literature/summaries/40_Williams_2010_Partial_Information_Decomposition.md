---
tags: ["#literature/paper", "#paper/round2-TE-methods"]
alias: "40_Williams_2010_Partial_Information_Decomposition"
---

# Research Paper Report: Nonnegative Decomposition of Multivariate Information

**Authors:** Paul L. Williams, Randall D. Beer
**Publication Year:** 2010
**Venue:** arXiv preprint (foundational PID paper; widely cited, published informally)
**DOI/arXiv:** `arXiv:1004.2515`
**Category:** (12) Transfer entropy estimation practice / partial information decomposition
**Role in Our Work:** **Foundational — decomposes joint information into redundant/unique/synergistic parts, resolving ambiguity in multi-source coupling.**

---

## 📌 Abstract & Architecture
Identifies a long-standing flaw in classical multivariate information theory: "interaction information," the traditional generalization of mutual information to three or more variables, can be negative, confounding two conceptually distinct phenomena (redundancy — information two sources share about a target — and synergy — information only available from the sources jointly) into a single signed number that can't distinguish them. The authors define partial information (PI) atoms via a new redundancy measure (minimum information any individual source provides about each outcome, averaged over outcomes) that induces a lattice over subsets of sources, and show this yields a full decomposition of a target variable's total information into nonnegative unique, redundant, and synergistic components — the foundational Partial Information Decomposition (PID) framework.

## 🔗 Connection to Computational Coupling Theory
Directly relevant whenever coupling must be disentangled between more than two systems or more than one channel — e.g. BrainNet-style multi-person coupling (`04_Jiang_2019`) or a dyad plus a shared external stimulus (the "superficial synchrony" case flagged in Part 2 of `literature_review.md`). Ordinary Transfer Entropy $\mathrm{TE}_{i\to j}$ answers "how much does $i$'s past reduce uncertainty about $j$'s future," but when there are multiple candidate sources (e.g. participant $i$, participant $k$, and shared stimulus $S$, all potentially informative about $j$), PID lets us ask the sharper question our theory needs answered: is the information $i$ provides about $j$ *unique* to $i$ (genuine dyadic coupling), *redundant* with $S$ (both driven by the same external cause — exactly the spurious-synchrony confound), or *synergistic* (only visible when $i$ and $S$, or $i$ and $k$, are considered jointly)? This gives a principled, citable upgrade path beyond simple conditioning-out of shared drivers: rather than a binary "TE conditioned on $S$ is/isn't significant" test, PID gives a full nonnegative accounting of how much of $j$'s predictability is uniquely attributable to $i$ versus shared with other sources — directly strengthening the theory's defense against the reviewer critique in Threat 2 of `literature_review.md`, and a natural extension of Prediction 3 (directional/role asymmetry) to more-than-two-party settings like BrainNet.

---
tags: [#literature/paper, #paper/extended-canon]
alias: "26_Zamm_2024_EEG_Hyperscanning_Practical_Guide"
---

# Research Paper Report: A Practical Guide to EEG Hyperscanning in Joint Action Research: From Motivation to Implementation

**Authors:** Anna Zamm, Janeen D. Loehr, Cordula Vesper, Ivana Konvalinka, Simon L. Kappel, Ole A. Heggli, Peter Vuust, Peter E. Keller
**Publication Year:** 2024
**Venue:** *Social Cognitive and Affective Neuroscience*, 19(1):nsae026
**DOI/arXiv:** `10.1093/scan/nsae026`
**Category:** (5) EEG/fMRI hyperscanning beyond current canon
**Role in Our Work:** **Direct methodological dependency for Paper 2, not a threat.** Practical protocol guide for exactly the dataset modality (dual EEG, joint action/turn-taking) named in our Roadmap.

---

## 📌 Abstract & Architecture
A methods-focused practical guide (not a novel empirical result) organized around five questions researchers must answer before running an EEG-hyperscanning joint-action study: whether hyperscanning is even necessary versus single-brain analysis; how to design the joint-action task; how to select inter-brain vs. intra-brain vs. behavioral dependent variables; which analysis method (e.g. phase synchrony, graph-theoretic connectivity) to use; and how to guard against the "shared sensory input" confound (two brains synchronizing merely because they share a stimulus, not because they are informationally coupled).

## 🔗 Connection to Computational Coupling Theory
This is a direct methodological reference for Paper 2's planned use of the OpenNeuro `ds007764` (DUET) and `ds007471` (Joint Agency) dual-EEG datasets described in `literature_review.md` Part 3 and the project roadmap. Its explicit treatment of the "shared sensory input" confound is the exact methodological problem our theory already claims to solve via Transfer Entropy conditioning (see canon's own "Threat 2: Superficial Synchrony" defense in `literature_review.md`) — this paper independently validates that the confound is a recognized, first-order concern in the hyperscanning field, which strengthens rather than threatens our framing. Cite in Paper 2's Methods section when justifying dataset choice and preprocessing/confound-control decisions.

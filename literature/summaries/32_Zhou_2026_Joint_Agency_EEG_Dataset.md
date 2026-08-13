---
tags: ["#literature/paper", "#paper/round2-datasets"]
alias: "32_Zhou_2026_Joint_Agency_EEG_Dataset"
---

# Research Paper Report: Behavioural and EEG Data From an EEG Hyperscanning Study Examining Cognitive and Neural Signals Underlying the Sense of Joint Agency During a Musical Joint Action Task ("Joint Agency EEG Dataset")

**Authors:** Zijun Zhou, Anna Zamm, Justin Christensen, Vinesh Rao, Janeen D. Loehr
**Publication Year:** 2026 (dataset uploaded 2026-03-04)
**Venue:** OpenNeuro dataset (no separate peer-reviewed descriptor paper found as of search date; the group's related behavioral paradigm paper is Zhou, Christensen & Loehr, "Not just in sync: Relations between partners' actions influence the sense of joint agency during joint action," *Cognition*, 2023)
**DOI/arXiv:** `10.18112/openneuro.ds007471.v1.0.0`; Dataset: OpenNeuro `ds007471`
**Category:** (8) OpenNeuro dataset descriptors (dyadic/hyperscanning EEG)
**Role in Our Work:** **Direct data dependency — the primary joint-action-coordination dataset for Paper 2.**

---

## 📌 Abstract & Architecture
Dual-EEG hyperscanning dataset of 32 participants (16 dyads) performing a musical joint-action task: pairs played tone-sequence "duets" together and, as a control condition, constant-pitch sequences, while researchers recorded synchronized EEG and computed trial-level behavioral synchronization (absolute asynchrony between partners' note onsets at each beat, normalized by the inter-onset interval). The dataset formalizes the lab's broader research program on the *sense of joint agency* — showing behaviorally (in the related 2023 *Cognition* paper) that joint agency depends not just on how synchronized partners are but on the finer-grained relations between their individual actions ("not just in sync"). No standalone peer-reviewed data-descriptor paper for the EEG release itself was found; the dataset is nonetheless independently citable via its own OpenNeuro DOI.

## 🔗 Connection to Computational Coupling Theory
This is the second of the two concrete real-brain datasets Paper 2 depends on. Unlike DUET's open-ended dialogue, this task provides a built-in, quantitative, trial-by-trial behavioral ground truth for coupling quality (the note-onset asynchrony metric) that can be directly regressed against a Transfer-Entropy-based Coupling Capacity estimate — giving a clean external validity check largely absent from language-based hyperscanning. The duet-vs-constant-pitch contrast is a near-ready-made bandwidth/task-demand manipulation: constant-pitch trials require minimal true information exchange (low effective $B$ demand) while duet trials require continuous mutual prediction of tempo and phrasing (high effective $B$ demand), making this dataset a strong candidate to test Prediction 1 (capacity saturates at $\min(\text{eff-dim})$, not raw bandwidth) using real, non-simulated neural data. Its authorship overlap with `26_Zamm_2024_EEG_Hyperscanning_Practical_Guide` (Zamm & Loehr are co-authors there too) means the practical-guide methodology paper already in the vault applies directly to preprocessing this dataset.

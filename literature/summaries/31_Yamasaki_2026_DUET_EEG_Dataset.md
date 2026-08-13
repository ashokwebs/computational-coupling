---
tags: ["#literature/paper", "#paper/round2-datasets"]
alias: "31_Yamasaki_2026_DUET_EEG_Dataset"
---

# Research Paper Report: A Dual EEG Hyperscanning Dataset of Natural French Face-to-Face Conversation (DUET)

**Authors:** Hiroyoshi Yamasaki, Philippe Blache, Daniele Schön
**Publication Year:** 2026 (posted 2026-05-15)
**Venue:** *bioRxiv* (preprint)
**DOI/arXiv:** `10.64898/2026.05.13.724780`; Dataset: OpenNeuro `ds007764`
**Category:** (8) OpenNeuro dataset descriptors (dyadic/hyperscanning EEG)
**Role in Our Work:** **Direct data dependency — the primary dyadic-dialogue dataset for Paper 2.**

---

## 📌 Abstract & Architecture
Describes DUET (Dyadic Understanding, EEG and Turn-taking): a BIDS-organized hyperscanning dataset of 18 French-speaking dyads (36 adults) recorded with simultaneous dual 64-channel EEG (one pilot dyad at 32 channels) during natural, unscripted face-to-face conversation. Pairs completed the Diapix collaborative "spot-the-difference" task across eight ~4-minute conversational blocks, requiring genuine turn-taking, repair, and joint reference resolution rather than a scripted or single-sided task. The public release includes participant-level metadata, per-run EEG recordings, and derivative files (conversational/turn-taking annotations, extracted features, preprocessing provenance) while withholding identifiable audio waveforms.

## 🔗 Connection to Computational Coupling Theory
This is one of the two concrete empirical datasets Paper 2 is scoped to actually download and analyze (alongside `ds007471`, see `32_Zhou_2026`). DUET is the higher-bandwidth, less-constrained test case: natural bidirectional spoken dialogue with real turn-taking gives genuinely asymmetric sender/receiver roles that switch over time, which is exactly the regime Prediction 3 (directional asymmetry tracks task role) needs real data for — unlike passive stimulus-driven hyperscanning (e.g. `13_Hasson_2010`), where both brains are largely driven by a common external signal rather than by each other. Because turn-taking structure is annotated as a derivative, it should be possible to condition Transfer Entropy estimates on "who is currently speaking" and test whether $C(i\to j;B)$ estimates track the annotated speaker/listener role swap in real time — a strong, near-term-feasible empirical test of the theory's core directional claim. Being a 2026 preprint, replication/robustness of the released derivatives should be treated cautiously until peer review, but the raw BIDS EEG data and DOI are independently verifiable via OpenNeuro.

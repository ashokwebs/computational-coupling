---
tags: [#literature/paper, #paper/extended-canon]
alias: "20_Lazaridou_2018_Referential_Games"
---

# Research Paper Report: Emergence of Linguistic Communication from Referential Games with Symbolic and Pixel Input

**Authors:** Angeliki Lazaridou, Karl Moritz Hermann, Karl Tuyls, Stephen Clark
**Publication Year:** 2018
**Venue:** *International Conference on Learning Representations (ICLR)*
**DOI/arXiv:** `arXiv:1804.03984`
**Category:** (2) Emergent multi-agent communication beyond DIAL
**Role in Our Work:** **Complementary.** Extends the DIAL/referential-game lineage to raw pixel input.

---

## 📌 Abstract & Architecture
Trains sender/receiver agent pairs on referential (Lewis-style signaling) games where a sender must communicate which of several images is the "target" using a discrete-symbol message, and a receiver must pick the correct image out of a set of distractors. Compares symbolic (pre-extracted feature) input against raw pixel input, and finds that the degree of structure in perceptual input strongly shapes the compositionality of the emergent protocol — richer/more structured perceptual grounding yields more systematic, compositional signaling.

## 🔗 Connection to Computational Coupling Theory
The sender/receiver referential game is the canonical asymmetric two-role setup that directly instantiates Prediction 3 (directional asymmetry tracks task role: here, sender/speaker vs. receiver/listener), and it is architecturally very close to PettingZoo's `simple_speaker_listener` MPE task named in our Stage 2 plan. It also speaks to Prediction 2 (systems with better self-predictive world models extract more capacity per bit): agents given richer, more structured perceptual representations (a proxy for a better internal world model) develop more efficient, compositional codes under the same channel budget. Useful as a citation when framing why the speaker/listener asymmetry we plan to measure in Stage 2 is expected on independent MARL evidence, not just a hyperscanning artifact.

---
tags: ["#literature/paper", "#paper/extended-canon"]
alias: "19_Mordatch_2017_Emergent_Compositional_Language"
---

# Research Paper Report: Emergence of Grounded Compositional Language in Multi-Agent Populations

**Authors:** Igor Mordatch, Pieter Abbeel
**Publication Year:** 2017 (AAAI 2018)
**Venue:** *AAAI Conference on Artificial Intelligence*
**DOI/arXiv:** `arXiv:1703.04908`
**Category:** (2) Emergent multi-agent communication beyond DIAL
**Role in Our Work:** **Complementary/foundational.** Also the paper that seeded the `simple_speaker_listener`-style Multi-agent Particle Environments (MPE) used by our Stage 2 experiment.

---

## 📌 Abstract & Architecture
Trains populations of agents with continuous physical dynamics and discrete-symbol utterance channels via end-to-end backpropagation through a differentiable environment simulator (not RL policy gradients). Shows that under goal-directed pressure, agents spontaneously develop compositional structure in their discrete symbol streams (a rudimentary vocabulary and syntax), and that non-verbal signaling (pointing, guiding) emerges when the verbal channel is unavailable — evidence that communication protocols and their bandwidth allocation are shaped by task structure, not hard-coded.

## 🔗 Connection to Computational Coupling Theory
This paper's environments are the direct ancestor of the Multi-Agent Particle Environments (MPE) that PettingZoo (`21_Terry_2021`) wraps and standardizes, including the `simple_speaker_listener` task named explicitly in our Stage 2 plan. Two points of direct relevance: (a) it is early empirical evidence for our Prediction 3 (directional asymmetry tracks task role) — the emergence of non-verbal signaling exactly when the verbal channel is bandwidth-constrained or removed shows agents reallocating information across available channels according to role (signaler vs. interpreter); (b) its compositional-language result is a naturally occurring instance of agents using an unconstrained channel efficiently, giving us a positive control for "communication happened" against which our bandwidth-limited saturation curves can be compared.

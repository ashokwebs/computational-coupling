---
tags: [#literature/paper, #paper/round2-synchronization]
alias: "35_Kuramoto_1975_Coupled_Oscillator_Synchronization"
---

# Research Paper Report: Self-Entrainment of a Population of Coupled Non-Linear Oscillators

**Authors:** Yoshiki Kuramoto
**Publication Year:** 1975
**Venue:** *International Symposium on Mathematical Problems in Theoretical Physics*, Lecture Notes in Physics, vol. 39, pp. 420–422 (Springer)
**DOI/arXiv:** `10.1007/BFb0013365`
**Category:** (10) Dynamical-systems synchronization theory (oscillators)
**Role in Our Work:** **Adjacent classical framework, not a competing theory — the "phase synchrony" lens our directed-information framework must be distinguished from.**

---

## 📌 Abstract & Architecture
Introduces what became known as the Kuramoto model: a population of weakly-coupled, phase-only nonlinear oscillators, each with its own intrinsic frequency drawn from a bell-shaped distribution, coupled all-to-all with sinusoidal interaction terms of uniform strength. Using a self-consistency mean-field argument, Kuramoto shows the population undergoes a sharp phase transition — below a critical coupling strength oscillators drift independently, above it a macroscopic fraction spontaneously mutually synchronize (lock to a common phase/frequency). This is the founding paper of the now-vast literature on synchronization as an order-parameter phase transition in coupled dynamical systems.

## 🔗 Connection to Computational Coupling Theory
This is the canonical alternative lens on "coupling" that reviewers will reflexively invoke — EEG/MEG hyperscanning results are conventionally reported as phase-locking value, PLV, or other Kuramoto-order-parameter-style synchrony metrics (e.g. the "theta coupling" language in `27_Markiewicz_2024`). Explicitly distinguishing our framework from this lineage strengthens Related Work: Kuramoto-style synchrony is a *symmetric, non-directional, state-space* notion (how aligned are two phases?), whereas Coupling Capacity $C(i\to j;B)$ is an *asymmetric, information-theoretic, channel* notion (how much of $j$'s future is predictable from $i$'s past, above $j$'s own past, through a bandwidth-$B$ interface?). Two oscillators can be perfectly phase-synchronized while carrying near-zero directed information (e.g. both driven by a shared external pacemaker with no causal link between them — exactly the "superficial synchrony" trap already flagged in Part 2 of `literature_review.md`), and conversely two systems can have high directed information with no stable phase relationship at all (e.g. asymmetric turn-taking dialogue, `31_Yamasaki_2026`). Should be cited alongside `36_Pecora_1990` in Related Work as the reason our theory measures *predictive/causal coupling* rather than *phase coupling*.

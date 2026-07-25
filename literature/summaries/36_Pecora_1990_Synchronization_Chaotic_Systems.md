---
tags: [#literature/paper, #paper/round2-synchronization]
alias: "36_Pecora_1990_Synchronization_Chaotic_Systems"
---

# Research Paper Report: Synchronization in Chaotic Systems

**Authors:** Louis M. Pecora, Thomas L. Carroll
**Publication Year:** 1990
**Venue:** *Physical Review Letters*, 64(8):821–824
**DOI/arXiv:** `10.1103/PhysRevLett.64.821`
**Category:** (10) Dynamical-systems synchronization theory (oscillators)
**Role in Our Work:** **Adjacent classical framework, not a competing theory — the "drive-response / generalized synchronization" lens our directed-information framework subsumes/differs from.**

---

## 📌 Abstract & Architecture
Shows that two identical chaotic systems, which individually have positive Lyapunov exponents (small perturbations diverge exponentially), can nonetheless be made to synchronize exactly if one ("drive") unidirectionally transmits a subset of its state variables to a "response" copy, *provided* the conditional Lyapunov exponents of the driven response subsystem are all negative. This launched the field of chaos synchronization, later generalized (by Rulkov, Afraimovich and others) beyond identical copies to "generalized synchronization," where a response system's state becomes an arbitrary deterministic function of the drive's state without needing identical dynamics or exact state matching.

## 🔗 Connection to Computational Coupling Theory
Provides the classical dynamical-systems vocabulary for exactly the drive/response, unidirectional-coupling structure our Coupling Capacity $C(i\to j;B)$ is built to quantify — but from a deterministic-dynamics angle rather than an information-theoretic one. The Pecora-Carroll criterion (negative conditional Lyapunov exponents of the response subsystem) is a necessary condition for exact state reconstruction, which is a stronger requirement than ours: $C(i\to j;B) > 0$ only requires that $i$'s trajectory reduces uncertainty about $j$'s *future*, not that $j$ can be driven into exact lockstep with $i$. This gives a clean, citable way to state the relationship in Related Work: generalized synchronization is the noise-free, infinite-bandwidth, deterministic special case in which our directed-information measure would saturate at its supremum; our framework additionally handles the realistic regime of noisy, finite-$B$, partially-observed coupling where exact synchronization is neither expected nor required for meaningful information transfer (e.g. Nakamura-style unsupervised alignment, `10_Nakamura_2024`, doesn't require Pecora-Carroll-style exact synchrony either). Pairs with `35_Kuramoto_1975` to fully cover the classical dynamical-systems "coupling" literature reviewers will expect acknowledged.

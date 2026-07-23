# A Theory of Computational Coupling Between Intelligent Systems

*Toward a General Foundation for Brain-to-Brain Communication*

**Author:** Ashok Pasala — VIT-AP University (Independent Research, Working Draft)

---

## Overview

Efforts toward brain-to-brain communication (BBI) and related brain-computer
interface (BCI) paradigms have largely proceeded by designing communication
*protocols* — fixed encodings, tokenizations, or aligned representational
spaces — without first establishing **what quantity such a protocol should
maximize**, or how to measure whether it has succeeded. This mirrors the state
of telecommunications engineering prior to Shannon's definition of channel
capacity: a field of designed artifacts without a rigorous target.

This working paper introduces a general theory of **computational coupling**
between intelligent systems — biological or artificial. It defines a
substrate-independent, directed, information-theoretic quantity —
**coupling capacity** — governing how predictively entangled two systems'
internal state trajectories can become, given a bandwidth- and
structure-constrained interface between them.

The paper is a **measurement theory, not a system proposal.** It does not
propose a BBI device, a new tokenization scheme, or a hardware architecture; it
proposes what any such system should be evaluated against.

## Central Idea

Communication between two intelligent systems is reframed not as the
transmission of a preformed message, but as the degree to which their internal
state trajectories become **mutually predictive** through a designed or evolved
interface. Coupling capacity is the direct dynamical analogue of Shannon
capacity:

> Where Shannon capacity is a supremum over input distributions of mutual
> information subject to a power or bandwidth constraint, **coupling capacity**
> is a supremum over *interface designs* of directed information between two
> coupled dynamical systems, subject to an analogous constraint.

Directed coupling from system *i* to system *j* is formalized as transfer
entropy (directed information) over state trajectories, generalized to
vector- or manifold-valued states with an explicit lag term. Coupling capacity
is its supremum over the admissible set of bandwidth-constrained interfaces.

## Falsifiable Predictions

The framework commits to three cross-domain, falsifiable predictions:

1. **Capacity–Bandwidth Law.** Coupling capacity is monotonically increasing
   and concave in interface bandwidth, saturating at the *smaller* of the two
   systems' effective representational dimensionality — not at the channel's
   raw capacity.
2. **Self-Predictive Accuracy Governs Capacity Efficiency.** Systems with
   better internal world models extract more coupling from an identical
   channel; capacity per unit bandwidth increases with each system's
   self-predictive accuracy.
3. **Asymmetry Tracks Role.** The directional asymmetry of coupling correlates
   with an externally defined task-role variable (e.g. leading/following,
   speaking/listening) across domains.

## Estimation

Two estimation settings are outlined:

- **Simulated multi-agent systems** — with ground-truth internal state access,
  via *k*-nearest-neighbor transfer-entropy estimators or a predictive-gain
  estimator (the log-likelihood gap between predicting a system's future from
  its own past alone versus jointly with the other system's past).
- **Biological recordings** (EEG / fMRI hyperscanning) — state trajectories
  estimated via dimensionality reduction, then the same predictive-gain
  estimator, with explicit treatment of measurement noise and short-data
  regimes.

## Roadmap

- **Paper 1** — Validate Predictions 1–2 in a controlled multi-agent RL testbed.
- **Paper 2** — Test the same predictions against public human hyperscanning and
  dialogue datasets.
- **Paper 3** — Causal manipulation of a theory-predicted variable via
  non-invasive intervention.
- **Paper 4 / Prototype** — Use coupling capacity as a training objective to
  discover a data-derived interface, culminating in a closed-loop BBI prototype
  for a narrow task domain.

## Repository Contents

| File | Description |
|------|-------------|
| `coupling_theory_paper.tex` | LaTeX source of the working draft |
| `coupling_theory_paper.pdf` | Compiled PDF |

## Building

```bash
pdflatex coupling_theory_paper.tex
```

## Status

This is a **working draft** establishing the core theoretical framework and
central definitions. Sections 3 (Formal Framework) and 4 (Falsifiable
Predictions) constitute the completed formal core; Sections 1, 2, 6, and 8 are
structured outlines pending expansion. Related-work citations are placeholders
and require verification against primary sources before any submission or public
circulation.

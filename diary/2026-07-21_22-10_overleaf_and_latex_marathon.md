---
tags: ["#diary/entry", "#research-log"]
alias: "2026-07-21_22-10_overleaf_and_latex_marathon"
---

# Diary Entry — July 21, 2026 (10:10 PM)
**Location:** Hostel Room, VIT-AP
**Mood:** Exhausted, eyes burning, caffeine overload
**Status:** Day 3 of research program — Modular LaTeX Setup & Paper Core

---

### Late Night LaTeX Marathon & Modular Paper Architecture 📄✨

It's past 10 PM. The hostel is quiet, except for someone shouting about a cricket match down the hall.

I spent the evening sitting down turning our whiteboard breakthroughs into a proper, modular LaTeX paper draft!

Set up `paper/main.tex` and split the paper cleanly into `sections/abstract.tex`, `sections/introduction.tex`, `sections/theory.tex`, `sections/experiments.tex`, and `sections/discussion.tex`.

```
Title: A Theory of Computational Coupling Between Intelligent Systems
Author: Ashok Pasala (VIT-AP University)
Target Venues: NeurIPS / ICML / ICLR / Nature Machine Intelligence / Nature Neuroscience
```

### Hilarious LaTeX Moment of the Night:
I spent 20 minutes debugging a cryptic `pdflatex` error:
`! Emergency stop. <read 1> \end{equation}`
Bro... turns out I forgot a closing brace inside the Transfer Entropy condition `\mid Y_{t-\tau:t}}`. Classic. Why tf does LaTeX treat a missing curly bracket like an unhandled core dump of the entire universe? 😂

### What's locked down in the draft right now:
1. **Section 3: Formal Framework**
   - Manifold state trajectories $x(t) \in \mathcal{M}_X, y(t) \in \mathcal{M}_Y$.
   - Interface map $g: \mathcal{M}_X \to \mathcal{M}_Y$.
   - Rigorous definition of Coupling Capacity $C_{\text{couple}}$ as the supremum of directed information over admissible bandwidth constraints $\mathcal{A}(B)$.
2. **Section 4: Falsifiable Predictions**
   - The three load-bearing claims (Capacity-Bandwidth Law, Self-Predictive Efficiency, Role Asymmetry) written out with mathematical precision.

Tomorrow: Literature deep-dive, empirical datasets, and planning Paper 1 code (Multi-agent RL in PettingZoo).

Signing off for tonight! 😴

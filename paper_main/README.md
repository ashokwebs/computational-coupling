---
tags: ["#paper/main"]
alias: "paper_main — the paper"
---

# paper_main — the single authoritative manuscript

**Understanding Is Not Observable: Shared Convention Makes Communication Possible and Its
Measurement Impossible.** 36 pp. This merges and replaces the two earlier manuscripts, which
were folded in here on 2026-08-25 and then deleted from the tree:

- `paper/` — *A Theory of Computational Coupling Between Intelligent Systems* (v0.3.0)
- `paper2/` — *Understanding Is Not Observable* (v0.1.0)

Nothing was lost. `paper/`'s formalism is §2 below; `paper2/` is the rest of the paper in full.
Both directories are recoverable from git history if you ever need the originals — see commit
`94eca22` and its parents.

## Build

```bash
cd paper_main && ./build.sh     # pdflatex → bibtex → pdflatex ×2
```

Requires `texlive-latex-base texlive-latex-recommended texlive-latex-extra
texlive-fonts-recommended`. Current build: 36 pages, 0 overfull boxes, 0 undefined
references or citations.

## Structure

| § | Content |
|---|---|
| 1 | Introduction — four fields, the two arguments, the remedy, and how we got here |
| **2** | **The target we set out to supply** — coupling capacity (Def. 1), the dimensional bottleneck (Thm. 2), P1–P3, what the simulation actually showed, and why the programme could not be completed |
| 3 | Formal setup — dyads, functional coupling $\mathcal{F}$, observational measures $\Phi$, assumptions A1–A3 |
| 4 | Non-identifiability under shared convention (Thm. 6, Prop. 8, Cor. 11–12) |
| 5 | When identification is possible (Thm. 13); noise as instrument; what does not suffice (Prop. 16–17) |
| 6 | The state–behaviour gap (Prop. 19) and the infinite-bandwidth control |
| 7 | Why the gap exists — coupling as an attractor; predicted hysteresis |
| 8 | Interventional measurement; the $\rho$ scale (Def. 21); reporting checklist |
| 9 | Implications — AI evaluation, interpretability, hyperscanning, brain-to-brain interfaces |
| 10–12 | Related work; limitations and falsification; open questions |
| A–C | Proof of Prop. 8; experimental detail; pre-registered human–AI design |

## The arc

§2 is the constructive programme: a Shannon-style measurement theory for brain-to-brain
interfaces. §§4–6 show it cannot work, for two independent reasons — the quantity it maximises is
non-identifiable under shared convention, and state-level coupling does not imply behavioural
coupling even with complete ground truth. §8 gives what replaces it. Theorem 2 survives as a
bound; the measurement programme built on it does not, and §12 says so explicitly.

## Figures

`fig2_capacity_bandwidth_law.png`, `fig4_selfpredictive_efficiency.png`,
`fig3_asymmetry_index.png` (Fig. 1, the superseded validation) come from
`experiments/paper1_rl/run_experiments.py`. `fig_noise_instrument_toy.png`,
`fig_noise_instrument_stage2.png` come from `experiments/paper2_identifiability/`.
`fig_oracle_control.png` comes from `experiments/paper1_rl/probe_oracle_listener.py`.

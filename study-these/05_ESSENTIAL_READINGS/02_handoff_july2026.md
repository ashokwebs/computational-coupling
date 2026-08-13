# Handoff — State of the Program (July 2026)

**Original File:** [`handoff.md`](file:///home/charizard/computational-coupling/handoff.md)  
**Written:** 2026-07-26.

---

## 1. Summary of Project Evolution
The original program (a Shannon-style measurement theory for brain-to-brain interfaces, `paper/`, v0.3.0) ran into an empirical wall in Stage 2 and, in resolving it, produced a better and much larger result: **functional coupling is an interventional quantity, it is not identifiable from observational data, and four fields are currently measuring it observationally.** The new paper lives in `paper2/`.

---

## 2. Settled Negative Results (Do Not Redo)

| Intervention | Outcome |
|---|---|
| Longer training (3k, 4k, 20k episodes) | No effect on coupling; at `lr=3e-3` it actively *diverges* |
| `lr` tuning | `3e-3` unstable $\rightarrow$ use `5e-4`. Settled. |
| `episodes_per_update` batching (1/16/64) | Improves task return substantially; **zero** effect on encoding |
| `entropy_coef` (0.02 / 0.005 / 0.0) | No effect on anything measured |
| Message-aware value baseline | No effect. Undetached version *regresses* encoding 0.90 $\rightarrow$ 0.0003 |
| Listener auxiliary head | Fixes representation (recon 0.0017), not behavior |
| Speaker auxiliary loss | **Works** — but needs `aux_coef ≈ 200`; at 1.0 it is swamped |

---

## 3. High-Value Next Steps
1. **Demonstrate Noise as an Instrument**: Show exogenous channel noise identifies functional coupling in simulation (Remark 2 of Paper 2).
2. **Second Empirical System**: Replicate Proposition 1 in a second structurally distinct environment.
3. **Human–AI Dissociation Experiment**: Test whether human-AI interaction exhibits apparent vs. functional coupling dissociation.
4. **Hyperscanning Re-analysis**: Re-analyze OpenNeuro `ds007764` DUET and `ds007471` Joint Agency EEG datasets using interventional/IV corrections.

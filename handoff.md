---
tags: [#meta/handoff]
alias: "Handoff — state of the program, July 2026"
---

# Handoff

**Written 2026-07-26.** Everything needed to pick this up cold — after a break, on a new machine, or by a collaborator. Read §1 and §3 first; the rest is reference.

---

## 1. Where things stand in one paragraph

The original program (a Shannon-style measurement theory for brain-to-brain interfaces, `paper/`, v0.3.0) ran into an empirical wall in Stage 2 and, in resolving it, produced a better and much larger result. The wall: two agents with a learned channel showed no measurable coupling at any bandwidth. The resolution: an agent handed the sender's information **directly, with no channel at all**, still ignored it — so the failure was never about channels. That fact generalises into a claim about measurement itself, now written as a new paper (`paper2/`): **functional coupling is an interventional quantity, it is not identifiable from observational data, and four fields are currently measuring it observationally.** The old paper is not deleted or wrong; its formal apparatus is reusable, and its framing is superseded.

---

## 2. Map of the repository

| Path | What it is | Status |
|---|---|---|
| `opp.md` | The core idea, in prose. Start here for the *why*. | Current |
| `paper2/main.tex` | **The new paper.** "Understanding Is Not Observable." | Draft v0.1.0, uncompiled |
| `paper2/references.bib` | Its bibliography, 21 entries, all resolving | Current |
| `paper/` | Original BBI coupling paper, v0.3.0 | Superseded framing, reusable formalism |
| `experiments/paper1_rl/` | All code producing the anchor result | Working |
| `experiments/paper1_rl/TODO.md` | Detailed experimental log, honest negatives included | Current, authoritative |
| `experiments/results/logs/`, `plots/` | Run outputs | Current |
| `literature/summaries/` | 40 paper summaries | Current |
| `literature/external_critique_*.md` | Archived adversarial review of the old framing | Reference |
| `tosee.md` | Verified reading list w/ real links | Current |
| `diary/` | Research journal | Personal, not load-bearing |
| `ROADMAP.md`, `MOC_*.md`, `Home.md` | Obsidian vault scaffolding for the *old* framing | **Stale — see §6** |

**Environment:** `source .venv/bin/activate`. Torch 2.13 CPU, numpy, matplotlib, pettingzoo + `mpe2`. No GPU needed; every result here ran on CPU in minutes.

---

## 3. The story, compressed — why the paper claims what it claims

Read this before touching the paper; the claims only make sense with the chain intact.

1. **A false positive was caught.** An earlier commit recorded a clean bandwidth-vs-coupling trend, `r = 0.99`, apparently supporting Prediction 1. It was estimator bias: `predictive_gain_te` is an in-sample regression whose bias grows with channel-dimension / sample-size ratio. A pure-noise control returned **0.71 "bits" where truth was 0**. Fixed by wiring in `cl.effective_te` (block-shuffle surrogate) and raising eval episodes 20 → 150. After correction, coupling sat at the noise floor across bandwidths 1–128. *This is why the paper's methodological remark exists.*
2. **The sender never encoded.** Speaker→message $R^2 \approx 0.001$ at every bandwidth.
3. **The architecture was fine.** A direct supervised probe on the same channel hit $R^2 > 0.99$ in ~300 steps. So it was an RL problem, not a capacity problem.
4. **An auxiliary loss fixed the sender** — but only after diagnosing a `reduction="sum"` vs `"mean"` scale mismatch that made `aux_coef=1.0` negligible. At `aux_coef=200`, $R^2: 0.001 \rightarrow 0.90$.
5. **The receiver still ignored it.** Message-sensitivity KL ~33× smaller than own-state sensitivity; ablation $z \approx 0$.
6. **Giving the receiver its own auxiliary head didn't help either.** Its hidden layer reconstructed the goal at error 0.0017 — the information was *provably present and linearly decodable* — while behaviour stayed unchanged. **This is the paper's Proposition 1.**
7. **The oracle control settled it.** No channel, goal handed over free: still $-15.96$, exactly the goal-blind heuristic ($-16.88$), against $-8.78$ achievable by an expert. **This is the paper's decisive control.**

---

## 4. Immediate next steps

### 4.1 Compile the paper
```bash
sudo apt-get install -y texlive-latex-base texlive-latex-recommended \
                        texlive-latex-extra texlive-fonts-recommended
cd paper2 && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```
Structural validation already passed (braces balanced, environments matched, 21/21 citations resolve, no broken `\ref`). Expect it to build clean; if not, it will be a missing `.sty`, not a syntax error.

### 4.2 ~~Attack your own theorem~~ — **DONE**, now §4 of the paper
The identification question is worked out. The paper now carries a positive result (Theorem 2: adjustment when the convention is observed; instrumental variation; direct intervention) and two sharp negatives that are arguably the paper's most useful content:
- **Proposition 2** — temporal precedence does *not* identify, because the shared convention precedes both $M$ and $U$. So transfer entropy, Granger causality, and directed information inherit the full negative result despite being "directional." This hits the hyperscanning field's principal instrument.
- **Proposition 3** — receiver-side measurement fails the front-door criterion, because the convention shapes both the receiver's representations and its dispositions. **Corollary:** no gain in recording resolution or interpretability precision repairs it; the obstruction is structural.
- **Remark (noise as instrument)** — exogenous channel noise satisfies the instrumental-variable conditions. This inverts standard practice: studies that carefully denoise their channel may be discarding their only route to identification. Potentially a way to get interventional conclusions out of *already-collected* observational hyperscanning data.

### 4.3 ~~Run the randomisation condition~~ — **DONE, and it changed the paper**
`rollout_with_message_source()` feeds the listener real in-distribution messages paired with the wrong episode. Result on the best config: real $-15.87$ | ablated $-16.45$ (z=+0.50) | **randomised $-18.19$ (z=+1.82)**.

Two findings, both now in paper §5:
- **Randomisation is ~3× more sensitive than ablation** on the identical system. Predicted on theoretical grounds in §7, now confirmed. *Never read a null ablation as zero functional coupling.*
- **But the residual sensitivity does no work.** Against a value-of-information of 8.10 reward units (expert −8.78 vs blind −16.88), the receiver's −15.87 captures $\lesssim$12%. So behavioural sensitivity and functional benefit dissociate *in their turn* — and interventional tests need calibrating against what the information is worth, not against zero. The paper now recommends **captured share of the value of information** as the primary statistic, and the claim is honestly stated as *small, not provably zero*.

---

## 5. The real research debts

Ordered by how much they change the paper's standing.

1. **Demonstrate the noise-as-instrument route.** Now the highest-value open item. Remark 2 of the paper claims exogenous channel noise identifies functional coupling, but only argues it. Show it: inject noise independent of the shared latent into the existing testbed, recover the known ground-truth coupling via IV, and confirm it matches the interventional estimate. That converts a remark into a *method* — and it is the only route to interventional conclusions from observational corpora, which is what makes hyperscanning re-analysis possible at all.
2. **A second empirical system.** Proposition 1 is one toy. It is an existence proof and that is legitimate, but a referee will ask whether the gap occurs anywhere that matters. A second demonstration in a structurally different setting (different task, different architecture, ideally not RL) would move it from curiosity to phenomenon.
3. **The human–AI experiment.** The most valuable and most differentiating. Take a human–LLM collaborative task; perturb the human's signal to change intent while preserving surface form; measure whether model behaviour tracks intent or surface. Needs a laptop and an API. If apparent and functional coupling dissociate in a deployed system, that is the headline result and the paper becomes considerably more important.
4. **Hyperscanning re-analysis.** Apply the correction to public dyadic EEG (`ds007764` DUET, `ds007471`). Prediction: on fixed task and instrumentation, measured coupling tracks *prior shared convention* — strangers < acquaintances < long-term partners — and beats channel-quality variables. Collects no new data.
5. **Hysteresis.** Currently predicted, untested. Sweep task demand up and down through the coupling transition and check whether onset and collapse thresholds differ. If they do, coupling capacity is historical and cross-sectional measurement is ill-posed — a strong, strange, quotable result. If they coincide, §6 of the paper loses a claim.
6. **The BBI throughput survey.** §8.4's retrodiction is currently asserted. Tabulate published BBI throughput against electrode count / SNR / year. If throughput is genuinely flat against hardware, the retrodiction is evidence; if it tracks hardware, cut the section.

---

## 6. Housekeeping debts

- ~~**The Obsidian vault is stale.**~~ **DONE for the two that matter:** `ROADMAP.md` and `Home.md` now carry prominent superseded/reframed banners pointing at `opp.md`, `paper2/`, and this file. Still stale and lower priority: `MOC_Theory.md`, `MOC_Roadmap.md`, `MOC_Literature.md` (which also still lists only 15 of the 40 summaries), and the two `.canvas` files.
- ~~**`paper/` needs a status banner**~~ **DONE.** `paper/main.tex` now opens with a red SUPERSEDED box that also states the two specific reasons — the Prediction-3 validation is estimator-validation, and the TE quantity is non-identifiable under shared convention — so the old claims can't be cited naively from the PDF alone.
- **Nothing in this session is committed.** `opp.md`, `paper2/`, `handoff.md`, and the last round of experiment changes are all uncommitted. Decide what goes in and write a commit that reflects the reframe.
- **`experiments/results/logs/P1_stage2_*_seed42.json` are overwritten per run.** If any specific numbers end up in the paper, freeze those files under a `paper2/data/` directory so the manuscript's figures are reproducible from pinned artefacts.

---

## 7. Do not redo these — settled negatives

All tested this session on the Stage 2 system; each was well-motivated and each failed. Full detail in `experiments/paper1_rl/TODO.md`.

| Intervention | Outcome |
|---|---|
| Longer training (3k, 4k, 20k episodes) | No effect on coupling; at `lr=3e-3` it actively *diverges* |
| `lr` tuning | `3e-3` unstable → use `5e-4`. Settled. |
| `episodes_per_update` batching (1/16/64) | Improves task return substantially; **zero** effect on encoding |
| `entropy_coef` (0.02 / 0.005 / 0.0) | No effect on anything measured |
| Message-aware value baseline | No effect. Undetached version *regresses* encoding 0.90 → 0.0003 (same sum/mean trap) |
| Listener auxiliary head | Fixes the *representation* (recon 0.0017), not the behaviour |
| Speaker auxiliary loss | **Works** — but needs `aux_coef ≈ 200`; at 1.0 it is swamped |

**Standing methodological rule:** never report a transfer-entropy number that has not been through `cl.effective_te`, and always confirm the eval sample count comfortably exceeds the channel's dimensionality. This project has already produced one false positive from exactly that.

---

## 8. Honest risk register

- **The theorem may be too easy.** Its mathematical content is standard confounding. The paper's defence is that the *application* is novel — the confounder is constitutive, not incidental. A hostile referee may still call it trivial. Strengthening §4.2 is the mitigation.
- **One toy is thin evidence.** See §5.2.
- **Prior art is close in places.** Kolchinsky & Wolpert (semantic information as causal relevance) and Lowe et al. (positive signalling vs. positive listening) are near neighbours and are cited prominently. Read both properly before submission — being caught claiming their result would be far more damaging than citing it generously.
- **Scope creep into philosophy.** The paper is careful to define functional coupling operationally and disclaim phenomenal understanding. Keep that discipline; the strong claims are defensible *because* the target is modest.
- **Venue mismatch.** This is not a Nature paper. Realistic homes: a position/methods track at an ML venue, *Trends in Cognitive Sciences*, *NeuroImage*, *Journal of Neuroscience Methods*, or *Imaging Neuroscience*. Aiming too high wastes months in desk rejections.

---

## 9. State at close of session — 2026-07-26, ~03:00

Written at the end of a very long day, deliberately calibrated rather than triumphant, because the next person to read this will be sober and should be met honestly.

### What is solid
- **A false positive was caught before it reached the paper.** An `r = 0.99` bandwidth–coupling trend was already committed to this repo and was estimator bias; a pure-noise control returned 0.71 fabricated bits. This is the single most valuable thing that happened, and it is invisible because it prevented rather than produced a result.
- **The oracle control is a genuinely good experiment.** Channel removed, information handed over free, agent still lands on the goal-blind optimum. It is cheap, decisive, and it closed off an entire class of explanations at once. It should have been run first; that it was run seventh is the methodological lesson of the day.
- **The randomisation finding is a real methodological contribution.** ~3× more sensitive than ablation on the identical system, and it forced an honest downgrade of the headline claim from "zero" to "small, not provably zero." The correction only exists because the experiment was run rather than cited as prescription.
- **The diagnostic instruments are reusable** and will matter more for Paper II/III than anything else in `experiments/`.
- **The paper compiles, is internally consistent, and its mathematics is correct.**

### What is not yet established, and should be treated as a hypothesis
- **The novelty claim is unverified.** Prior art in §8 of the paper was summarised from memory, not from reading. **Before doing anything else, read Kolchinsky & Wolpert (2018) and Lowe et al. (2019) in full.** If Kolchinsky & Wolpert already locate meaning in causal consequence in the way §8 concedes, the paper needs restructuring around the identifiability result specifically, and possibly a different framing. This is the load-bearing uncertainty and it is cheap to resolve.
- **Theorem 1's mathematics is elementary.** Its content is standard confounding; the claim to novelty rests entirely on *where* it applies — that the confounder is constitutive. A referee may find that insufficient. Theorem 2 and Propositions 2–3 are what give the paper technical substance.
- **One toy system is thin evidence** for a claim pitched at four fields.
- **The four-fields framing has not met an expert from any of those fields.** It is the kind of argument that feels inevitable at 3am and can look overreaching in daylight.
- **The BBI retrodiction is post-hoc** and is the section to cut first if the paper needs shortening.

### The honest summary
A day that began by debugging a reinforcement-learning bug ended with a compiled paper arguing that four fields measure understanding with the wrong instrument. That trajectory is either the best thing that has happened to this project or a very elaborate way of avoiding a hard experiment, and **the difference is settled by whether the human–AI dissociation (§5.3) replicates.** Everything else is scaffolding for that test.

---

## 10. If you only do three things

1. **Read Kolchinsky & Wolpert (2018) and Lowe et al. (2019) properly**, not from anyone's summary. The paper's entire novelty claim is exposed to these two. Half a day, and it determines whether the rest is worth doing.
2. **Print `paper2/main.pdf` and read it cold as a hostile referee**, ideally after a night's sleep and away from the machine. Mark every sentence that asserts rather than shows.
3. **Run the human–AI dissociation (§5.3).** Cheap, nobody has done it, and it is the difference between a seminar-room argument and a result. If apparent and functional coupling come apart in a deployed system, this matters; if they don't, that is worth knowing quickly and the paper should say so.

*(Item 4.2 — the identification conditions — is done and is now §4 of the paper. It went from the highest-value open item to the paper's technical core in a single sitting, which is the argument for doing the theory rather than planning it.)*

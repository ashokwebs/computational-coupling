---
tags: ["#meta/review1", "#report/full-inventory"]
alias: "Review 1 — Everything We're Working On"
---

# Everything We're Working On — Review 1 Prep Report

**Written:** 2026-08-13, the day before Review 1.
**Purpose:** the full inventory — not the curated fifteen minutes (see the diary entry from this morning for that split), but *everything*: what's done, what's proven, what's still a hypothesis, and every angle this work could be pitched from. Read this to remember what's in the building, then decide what to walk people through.

---

## 1. The one-paragraph version, if someone stops you in the hallway

We set out to build a better brain-to-brain interface, on the theory that human communication is bottlenecked by the mouth and the ear — thought is fast, speech is agonizingly slow, so remove the channel and you unlock the real bandwidth. We built the experiment properly, and the experiment killed the premise: we gave an artificial receiver its partner's private information *directly*, with no channel, no noise, no cost at all — the actual physical limit of every possible interface — and its behavior didn't move a single point. Digging into why turned into a general theorem: two systems that share a convention and two that merely each *hold* the same convention independently produce identical observable behavior, so no amount of watching them interact can tell which one you have. That's not a claim about brains specifically — it's a claim about AI evaluation, interpretability, hyperscanning, and the philosophical problem of other minds, all at once, because all four currently try to measure this thing by observation, and observation is provably the wrong tool. We have a compiled 17-page paper, a working ground-truth demonstration with numbers, a real anomaly in an existing field that the theory explains and nothing else does, and one very good next experiment we haven't run yet.

---

## 2. The arc, so the pieces make sense in order

It genuinely helps to tell this chronologically rather than as a features list, because each piece exists *because* the previous one broke something.

**July 19–23 — the founding question.** Why does brain-to-brain interface (BBI) research feel stuck at "press button, robot arm moves"? Formalized as a Shannon-style coupling capacity, three testable predictions, a working NumPy simulator that confirmed capacity saturation at roughly 0.39× the smaller channel dimension. This became `paper/`, v0.3.0 — a complete, self-consistent paper.

**July 24–25 — Stage 2, the empirical wall.** Moved from the closed-form simulator to a learned system: two RL agents, a discrete communication channel between them, PettingZoo. Found a clean bandwidth-vs-coupling trend (r = 0.99) — and then, on a whim, ran a pure-noise control, which returned 0.71 "bits" of coupling where the true answer was zero. **The trend was estimator bias, not signal.** Caught before it reached anyone. Fixed the estimator (`cl.effective_te`, a proper block-shuffle surrogate), and the clean trend evaporated at the noise floor.

**July 25 (still) — the real failure surfaces.** With the bias gone, the actual finding was that the sender never learned to encode anything (R² ≈ 0.001). Not a capacity problem — an RL problem. Fixed with an auxiliary loss (once a `reduction="sum"` vs `"mean"` scale bug was found and fixed too) — sender now encodes at R² = 0.90. And *still* the receiver ignored the channel. Gave the receiver its own auxiliary head to prove the information was sitting right there in its hidden layer, recoverable at error 0.0017 — genuinely, provably present — and behavior still didn't change. That's the paper's Proposition 1.

**July 26 — the reframe.** Ran the decisive control: delete the channel, hand the receiver the sender's private state directly, no bottleneck of any kind. Score: −16.0, identical to an agent told nothing, against −8.8 for an agent that actually uses the information. That result doesn't fit inside "brain-to-brain interfaces need better bandwidth." It says something about *measurement itself*: coupling that shows up in every internal-state statistic can be completely behaviorally inert, and the reason is that a shared convention — not a channel — is what makes communication possible, and that same convention confounds any attempt to detect it from outside. The program pivoted from "build a wider channel" to "understanding is not observable, only interventional." New paper, `paper2/`.

**July 26–31 (with a three-day fever in the middle) — building out `paper2/`.** Formal non-identifiability theorem. A matching positive result (three conditions under which it *is* identifiable) plus two sharp negatives — temporal precedence doesn't save you (kills the hyperscanning field's favorite instrument, directed information/transfer entropy), and looking inside the receiver doesn't save you either (fails the front-door criterion). Discovered that randomizing a signal is ~3× more sensitive than ablating it as a test for functional coupling — a real, adoptable methodological finding independent of the bigger theory. Read Kolchinsky & Wolpert (2018) and Lowe et al. (2019) in full from primary sources to stress-test novelty — survived, with the distinctions now sharp in the paper. Demonstrated the "noise as instrument" idea on a toy system (exact recovery, 200 seeds), then applied it to the real trained Stage 2 system and watched it fail — diagnosed *why* it failed, mechanistically, not just observed that it did. Wrote up the BBI throughput retrodiction with real citations instead of the earlier hand-wave.

**August 1 — closing the loop on the founding question.** Went back to the bandwidth argument that started the whole thing on July 19, checked the actual numbers (39 bits/s speech across 17 languages, Coupé et al. 2019; ~10 bits/s for deliberate behavior, Zheng & Meister 2024), and caught myself about to assert into the paper the exact thing the oracle control had already refuted. Rewrote it as the foil instead — grant the premise, reject the inference, turn it into a design claim (interfaces need to grow convention jointly, not just widen a pipe).

**August 13 — today.** Deciding what of all this goes in front of a room tomorrow.

---

## 3. What's actually done and solid (you can put a number next to each of these)

- **A complete, non-identifiability theorem.** Two systems, one genuinely coupled, one merely each independently holding the same convention, produce *identical* observational distributions over signals, internal states, and behavior. No observational statistic — mutual information, transfer entropy, synchrony, representational similarity, behavioral agreement — can separate them.
- **A matching positive result.** Three conditions that *do* identify functional coupling: adjusting for the convention when it's observed, instrumental variation (including, surprisingly, ordinary channel noise), or direct intervention. Plus two negative propositions that close the obvious escape routes (temporal precedence; receiver-side interpretability).
- **A ground-truth constructive demonstration**, not a thought experiment: sender encodes at R² = 0.90, receiver's hidden layer decodes that state at reconstruction error 0.0017, receiver's behavior is statistically indistinguishable from getting nothing at all (z ≈ 0), and an infinite-bandwidth, zero-noise, zero-cost oracle control still lands at the goal-blind optimum (−16.0 vs. an achievable −8.8).
- **A methodological finding**: randomization is ~3× more sensitive than ablation as a test for functional coupling on the identical system, and even the residual sensitivity captures only ~12% of the value of the information — small, not provably zero, and the paper says exactly that rather than rounding to a cleaner headline.
- **An honestly-scoped instrument validation.** Noise-as-instrument recovers exact ground truth on a calibrated toy (200 seeds), and *fails* on the real trained system with a diagnosed cause (auxiliary-loss-driven logit saturation starves the channel's own noise of relevance) — a genuine boundary condition on the method, written up as such rather than hidden.
- **A field-level retrodiction with primary sourcing.** BBI throughput went *down* from Rao et al. 2014 to Jiang et al.'s BrainNet 2019 despite five years of hardware improvement — confirmed in the BrainNet authors' own discussion section and an independent 2021 systematic review — and the framework is the only account on hand that predicts this rather than being surprised by it.
- **A novelty check done properly**, not assumed: Kolchinsky & Wolpert (2018) and Lowe et al. (2019) read in full from primary sources. K&W is monadic (no sender/receiver pair, no confounder, no impossibility result) — a strong citation, not a competitor. Lowe et al. independently found the same positive-signalling/positive-listening split empirically but traced it to an architectural confound our system's diagnostic chain rules out, and never ran an oracle control. The claim survives contact with the closest prior work.
- **A compiled paper.** `paper2/main.tex`, 17 pages, 0 overfull boxes, 0 undefined references, bibliography resolving.

---

## 4. What's open, honest, and should stay labeled as such

- **The human–AI dissociation experiment — not run.** Fully designed (task bank, four-condition protocol mirroring the RL result exactly: intact / ablation / randomisation / targeted perturbation, judge-scoring plan, statistics plan, confound list), sitting in `experiments/paper2_human_ai/TODO.md`, blocked only on an API key and a green light. This is repeatedly flagged in the repo's own handoff notes as *the* top remaining priority — "the difference between a seminar-room argument and a result." Don't present it as more than a design.
- **One toy system.** Proposition 1 is a real existence proof but it is one existence proof, in one RL architecture. A referee, or a reviewer tomorrow, is entitled to ask whether the gap shows up anywhere else. A second, structurally different demonstration (different task, ideally non-RL) is on the list and hasn't happened.
- **Hyperscanning re-analysis — designed, not run.** Apply the correction to public dyadic EEG data (`ds007764`, `ds007471`). Prediction: measured coupling should track *prior relationship* (strangers < acquaintances < long-term partners) more than channel-quality variables do. Needs no new data collection — just needs doing.
- **Hysteresis — untested.** If the onset threshold for coupling differs from the collapse threshold, coupling capacity is historical, not a function of a dyad's current parameters — a strange, sharp, falsifiable prediction, and currently just a prediction.
- **Housekeeping.** As of this morning, this whole reframe — `opp.md`, `paper2/`, the noise-as-instrument work, the bandwidth reframe — is still uncommitted in git. Nothing here is lost, but nothing is locked in either.
- **The novelty claim rests on two close neighbors, not an exhaustive search.** Checked the two most obvious ones properly; hasn't been checked against a domain expert from any of the four fields the paper claims to span.

---

## 5. Every angle this could be pitched from

Not all of these are equally ready, and that's fine — this section is the menu, not the recommendation. (§6 below is the recommendation.)

1. **The theory, cold.** "You cannot tell from watching two systems interact whether they understand each other, and here's a proof." Broadest audience, highest ceiling, needs the most setup to land without sounding like a philosophy claim instead of a measurable one.
2. **The demonstration, cold.** Skip the theorem, lead with the toy system: a receiver that "understands" perfectly by every metric anyone currently uses, and behaviorally ignores everything. Concrete, visual, needs less background than the theorem, and it's the thing that makes the theorem feel inevitable rather than clever.
3. **The methods contribution.** Randomization beats ablation as a coupling probe, by a measured 3×, on a system where we know the ground truth. This one stands alone — useful to anyone running a hyperscanning or emergent-communication study, whether or not they buy the bigger theory.
4. **The ML deployment angle.** RLHF and every chat-based eval score *outputs* — rung one on Pearl's ladder — for a quantity (understanding) that this work shows sits on rung two. Reframes "systems that pass eval and fail in the world" as a structural defect in the training signal, not an insufficiently thorough eval. Big claim, falsifiable, currently argued rather than separately tested (the human-AI experiment is what would test it directly).
5. **The interpretability critique.** "The model represents X" is a decodability claim — exactly the class of claim that read 0.0017 on our receiver's hidden layer while its behavior read zero. Directly actionable: it's an argument *for* the field's existing move toward causal methods (activation patching, causal scrubbing), not against interpretability as a project.
6. **The hyperscanning critique.** A decade of "these brains are synchronized" results are observational; this work shows synchrony at ceiling and functional coupling at floor are simultaneously possible. Sharpest version of the pitch for a neuroscience audience specifically, and comes with a concrete, doable, no-new-data-needed follow-up (§4 above).
7. **The noise-as-instrument technique.** A constructive way to extract interventional conclusions from *already-collected* observational hyperscanning data, using exogenous channel noise as an instrumental variable — inverts the usual impulse to denoise a signal before analyzing it. Comes with both a clean success (toy) and an honestly diagnosed failure mode (real trained system), which is a better story than a clean success alone: it shows the method's actual boundary, not just its best case.
8. **The BBI retrodiction.** A ten-year, field-wide anomaly — better hardware, flat-to-declining throughput — that the framework explains and the standard bandwidth-centric account doesn't. This is the pitch for anyone who wants "does this theory predict something real," answered with a citation trail, not a just-so story.
9. **The bandwidth-origin story.** How the project started, why the founding intuition felt airtight, and how the project's own strongest experiment quietly refuted it before anyone noticed. Good as a narrative hook, good as evidence of intellectual honesty, costs nothing technical to tell.
10. **The rigor-as-narrative angle.** The r = 0.99 false positive, caught by a noise control before it reached the paper. Not a result — a demonstration that the process catches its own mistakes. Best saved for an audience that already trusts the results and wants to know *how* they were produced.
11. **The human–AI experiment, as a proposal.** Not a result yet, but a complete, defensible, cheap-to-run design that would produce the single most differentiating finding in the whole program if it confirms — worth pitching as "here is exactly what we'd do next and why," to get buy-in or resources rather than to claim it's already answered.
12. **The philosophy-of-other-minds framing.** The most provocative version, in `opp.md`: nothing about this is special to machines — you cannot verify by conversation that *another person* understands you either, and this is why. Powerful, correct as an implication of the theorem, and the one most likely to read as overreach if led with before the technical credibility is established. Dessert, not the main course, for a first audience.

---

## 6. What actually fits in Review 1 (cross-reference: diary, 2026-08-13)

Decided this morning, logged in the diary entry from today — repeating the shortlist here so it's in one place:

**In:** the bandwidth origin story (angle 9) → the oracle control demonstration (angle 2) → the theorem in one sentence (angle 1, compressed) → the BBI retrodiction (angle 8). Four beats, each with a number behind it, roughly fifteen minutes.

**Held for Q&A or a follow-up conversation, not the main slot:** the noise-as-instrument success/failure pair (angle 7), the full identification machinery, the human–AI experiment as a forward-looking proposal (angle 11) if asked "what's next," the false-positive story (angle 10) if asked "how do you know you're not fooling yourself."

**Not for tomorrow at all:** the philosophy-of-other-minds framing (angle 12) — true, but it's the thing that turns a measurement result into a claim about human relationships in a first meeting, and that trade isn't worth making before the technical spine has landed. Also: anything currently marked stale or superseded in the repo (`ROADMAP.md`, the old Obsidian MOC pages, the ancient `paper/` framing) — none of that should surface even by accident.

---

## 7. The honest risk register, so nothing said tomorrow outruns the evidence

- The theorem's mathematical content is standard confounding; novelty is entirely in *where* it applies (the confounder is constitutive, not incidental to communication). A sharp reviewer may call the math itself unsurprising — the response is that Theorem 2 and the two negative propositions are the technical substance, not Theorem 1 alone.
- One toy system is thin evidence for a claim pitched at four fields. Said plainly, not hidden.
- The BBI retrodiction rests on two hard data points (Rao 2014, BrainNet 2019), not a dense time series, and no quantified 2021–2026 follow-up was found either way in a general search.
- The four-fields framing hasn't met an expert from any of the four fields yet. Tomorrow is, in a sense, the first test of that.
- Venue-wise, this isn't a "solve neuroscience" paper — realistic homes are a position/methods track at an ML venue, or a cognitive-science/neuroscience-methods journal. Aiming higher than that wastes months on desk rejections; worth saying out loud if asked about next steps.

---

## 8. Fresh literature check, 2026-08-13 — same-day web research pass

Three background research agents ran today across the BCI/BBI landscape, neuroscience of brain complexity, and a targeted novelty check. Full sourced writeups are in `literature/web_scan_*_2026.md`; the load-bearing findings are compressed here.

### 8.1 Novelty check: clean

After 17+ distinct search angles against the paper's exact combination of claims (dyadic, formal non-identifiability, shared-convention-as-confounder, a named class of defeated observational statistics), **nothing found combines all four elements.** The closest near-misses, all examined and ruled non-threatening:
- Lin & Liu (2026, arXiv:2605.08012) — mechanistic-interpretability position paper demanding disclosure of causal-identification assumptions. Same rung-1-vs-rung-2 instinct, but monadic (one model), no confounder, no impossibility theorem — a disclosure norm, not a proof.
- Huang & Chang (2025, arXiv:2510.09794) and Sharma, Dawes & Raval (2026, arXiv:2604.22128) — both independently demonstrate "decodable ≠ causally used" empirically in single transformer models, wording close to Proposition 1. Good fresh citations *for* the paper; not competitors.
- A 2024 hyperscanning-causality review (PMC11599244) and its 2021 ancestor (Novembre & Iannetti, *TiCS*) already argue synchrony needs an interventional check — but as a methods recommendation, not an impossibility claim, and without a convention-based confounder.
- No work was found bringing Pearl's causal ladder or instrumental-variable reasoning to the classical philosophical problem of other minds — the single most reassuring negative result in the scan, since that's essentially the paper's own core move.

**One open item, not urgent but cheap to close**: the PhilPapers "Problem of Other Minds" bibliography couldn't be fetched directly (blocked). A ten-minute manual browse before or after tomorrow is worth doing, but nothing else in the scan suggests it would change the verdict.

### 8.2 BCI/BBI landscape: retrodiction still stands, new supporting citations available

No new human or animal BBI study with a quantified throughput number has surfaced since Jiang et al. 2019 — the retrodiction in §sec:bbi is, if anything, *more* striking now: adjacent single-brain BCI throughput has visibly moved (Willett et al. 2023, 62 wpm; Metzger et al. 2023, 78 wpm) while BBI-specifically has produced nothing new in seven years.

Three independent, recent, non-affiliated sources now back the "bandwidth isn't the real constraint" intuition from different angles — worth having on hand, not urgent to add before tomorrow:
- **Meyer & Zamani (2026), *J. Neural Engineering* 23(3), 031001** — peer-reviewed, explicitly names an "input/output disparity" as BCI's real constraint, argues raw channel count doesn't linearly buy meaningful throughput. The closest peer-reviewed echo of the paper's stance found anywhere.
- **Zheng & Meister** — already cited (`zheng2024slowness`); confirmed as a solid, correctly-used citation.
- **Jiang, B. (2026), arXiv:2607.24820**, posted 2026-07-17 — closest single hit to the paper's thesis (distinguishes physical bandwidth from "confirmed subject-level I/O"), but single-author, non-peer-reviewed, posted three weeks ago. Worth Ashok's own five-minute read before the review in case it comes up, but not yet citable as established prior art.
- A live tension worth knowing about for Q&A: Paradromics's own blog (Feb 2026) pushes back on the "10 bits/s is all you need" framing, arguing embodied/rich tasks need far more bandwidth than conscious decision output alone — a real industry counter-voice, though not disinterested (their product is a high-channel-count array). If anyone in the room raises "but surely more channels help," this is the sharpest version of that objection to be ready for.

### 8.3 Neuroscience/complexity/hyperscanning scan: one paper worth reading before tomorrow

**Varlet & Grootswagers (2024), *Frontiers in Human Neuroscience* 18:1385624**, "Measuring information alignment in hyperscanning research with representational analyses: moving beyond interbrain synchrony" — the closest existing precedent found anywhere today to the paper's "synchrony ≠ functional coupling" claim. Using real EEG hyperscanning data, they show inter-brain synchrony stays roughly flat even when the experimenters manipulate whether two people are seeing the *same* or *different* stimuli — i.e., synchrony is largely insensitive to whether real information alignment is present. **Important distinction that keeps the paper's novelty intact**: their design varies stimulus content and observes the consequence (still an observational/comparative design), not an intervention on the coupling channel itself the way this paper's ablation/randomization protocol does. So the core move — identifiability requires intervening on the coupling, not just varying what's shown — still looks like a genuine gap in the hyperscanning literature. **Action item**: full text wasn't fetchable in this pass (repeated timeouts); worth a direct read before citing it in `main.tex`, and it's a good citation to have regardless — it's independent evidence the field itself already suspects synchrony is a weak instrument.

Other useful, lower-stakes material: neuroscience already has established vocabulary for "information present but behaviorally unused" — Kaufman/Churchland's *output-null subspace* concept, and Grootswagers/Cichy/Carlson's decodable-vs-read-out dissociation work — good precedent to cite for the plausibility of Proposition 1's pattern showing up in biological systems too, not just the RL toy. Also flagged: the 2025 Cogitate adversarial collaboration (IIT vs. GNWT, n=256, published in *Nature*) is a striking case where a maximally rigorous *observational* test still failed to cleanly discriminate between two major theories of consciousness — a nice cautionary parallel, not a direct citation.

---

## 9. If tomorrow goes well

The natural next commitments, in order of leverage: (1) run the human–AI experiment — cheapest, highest-differentiation thing left undone; (2) commit the current uncommitted state so the reframe is actually locked in; (3) find a second empirical system outside RL to broaden the existence proof; (4) the hyperscanning re-analysis, since it needs no new data collection and would be the first outside-the-lab test of the theory's central prediction.

None of that needs deciding tonight. Tonight just needs the four beats to be tight.

---
tags: ["#diary/entry", "#research-log", "#paper2/identifiability", "#noise-as-instrument", "#human-ai-experiment"]
alias: "2026-07-31_11-30_the_instrument_actually_works"
---

# Diary Entry — July 31, 2026 (11:30 AM)
**Location:** VIT-AP Hostel Room
**Mood:** Genuinely pleased 🎯
**Status:** Day 12, continued. Second handoff priority resolved in the same morning.

---

### Deferring the big one, honestly

Asked about the human-AI dissociation experiment and the answer was: yes, but later. Fair — it needs an API key that isn't wired up in this environment yet, and it deserves to be run deliberately, not rushed through as a side quest. So instead of running it half-baked, I wrote up the complete design: `experiments/paper2_human_ai/TODO.md`. Four-condition protocol (intact / ablation / randomisation / targeted-perturbation, directly reusing the paper's own §7 instrument set), five task families, a judge-scoring plan with a human-validation step, the value-of-information statistic the paper already uses for the RL result, and — importantly — the confounds to check before trusting it (context-window recency effects masquerading as the theory's specific confound, judge bias, single-model generalization). Whoever picks this up next, including future-me, shouldn't have to re-derive any of it.

### Then I noticed I had time for the other one

Remark 2 of `paper2/main.tex` — the noise-as-instrument idea — has been sitting there since the reframe as an assertion: *exogenous channel noise satisfies the IV conditions, so denoising a hyperscanning channel might be destroying the only route to identification.* It's the second-highest item on `handoff.md`'s research-debt list and, unlike the human-AI experiment, it needs nothing but NumPy. So I built it.

The construction mirrors Theorem 1's proof almost exactly, just made continuous so 2SLS applies cleanly: a shared latent $C$, a message $M = C + N$ with $N$ genuinely exogenous noise, and two dyads — one where behavior $U$ causally depends on $M$, one where it depends on $C$ directly and $M$ is just along for the ride. Calibrate the confounded dyad's weight so both dyads produce the *exact same* observational covariance between message and behavior, and you've got a continuous instance of $P_1 = P_2$.

Ran it. 200 seeds, n=2000 per seed:

- **Naive observational regression**: 0.800 ± 0.005 (coupled) vs. 0.799 ± 0.019 (confounded) — statistically identical, exactly as the theorem says it should be.
- **IV using the channel noise as instrument**: 0.800 ± 0.007 (coupled) vs. −0.003 ± 0.034 (confounded) — dead on the true causal effect in both cases, recovering the distinction observation is structurally blind to.

That's a clean confirmation of the paper's own remark, and it converts it from a claim into a script anyone can rerun. I added the honest caveat too, because the "just use noise as an instrument" pitch is too easy to oversell: swept the instrument strength down to where the first-stage F-statistic drops below 10, and the IV estimate falls apart completely — std of 1.66 and 9.45 on an effect that's supposed to be 0.8 and 0. Weak instruments don't just add noise, they make the estimate worthless, and that needs to be reported next to every IV number this method ever produces, not buried in a footnote.

### What I didn't do

I didn't try to claim this settles the hyperscanning application. It's a linear-Gaussian toy that I built specifically so the method would work — that's the right thing to build first, but it's an existence proof, not a field-ready tool. The honest next step, logged in `experiments/paper2_identifiability/TODO.md`, is running the same instrument logic on a system I didn't design for it: the existing Stage 2 RL testbed's own channel noise, or real dropout/jitter in a hyperscanning corpus. Left that queued rather than rushing it, same as the human-AI experiment — better to log two well-specified debts than one half-finished result.

`paper2/main.tex` Remark 2 and the limitations section both updated with the real numbers and recompiled — still 14 pages, still clean. Two of the handoff's outstanding obligations closed today; the two that remain (hostile-referee read, human-AI experiment) are exactly the two that need either a fresh pair of eyes or an API key, neither of which was available this morning. Good stopping point.

Signing off — Day 12, part two. ✌️

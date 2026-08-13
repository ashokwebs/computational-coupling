---
tags: ["#diary/entry", "#research-log", "#paper1/rl", "#the-mentalist"]
alias: "2026-07-25_18-15_the_signal_was_the_bias"
---

# Diary Entry — July 25, 2026 (6:15 PM)
**Location:** VIT-AP Hostel Room (Day 7, second half — laptop fan audibly upset, *The Mentalist* still going in the background)
**Mood:** Humbled but weirdly delighted 🔬😅
**Status:** Day 7 (cont.) — Stage 2 got debugged twice today, and the second bug ate the first result.

---

### Picking up where the morning left off

This morning's plan was the boring, sensible one: train longer, widen the bandwidth grid to 64/128, see if the saturation law finally shows its face. Did both. Neither did what I expected.

First surprise: "train longer" was actively the wrong move. Ran B=8 out to 4000 episodes at the usual `lr=3e-3` and watched the mean return walk from -55 at episode 400 to -157 at episode 4000 — not noisy, *trending down*. That's not an undertrained policy, that's a policy actively coming apart at the seams over a long run. Dropped the learning rate to `5e-4` and it just... stopped happening. Flat around -40 to -45 for the whole 4000 episodes. So the "3000 episodes made it worse" note from a couple of days ago wasn't a fluke, it was this same instability the whole time. Lesson: when a curve gets *worse* with more training, don't reach for more training as the fix.

### Second surprise, and this one's a better story

With the stable learning rate, ran the full grid out to B=128. Task returns: flat, no trend, -40 to -60 everywhere, bandwidth doesn't seem to matter to the policy at all. Measured coupling (TE): rockets up to 1.96 bits at B=128, and the increments are *accelerating* — the opposite of the concave saturating shape the theory predicts.

Here's the thing that should've tipped me off immediately, and it's almost funny given what's been playing on the laptop half the day: if Patrick Jane's whole trick is reading *real* signal out of tiny genuine tells, today's estimator was doing the exact reverse — finding "signal" in what was actually just noise, and finding *more* of it the more room you gave it to look. Fed the estimator two completely independent random arrays — pure noise, zero true coupling by construction — at 128 dimensions and only ~500 eval samples, and it confidently reported 0.71 bits of "coupling." That's not a subtle bug. `predictive_gain_te` is an in-sample linear regression (tiny ridge, no held-out data), and as the message dimension creeps up toward the sample count, its in-sample R² gets mechanically inflated — classic curse-of-dimensionality overfitting, dressed up as a physics result.

The good news: the codebase already has the right tool for this (`cl.effective_te`, the block-shuffle surrogate correction I'd used for the KSG cross-check back in the Stage 1 days) — it just had never been wired into Stage 2. Went to use it and immediately hit a *second*, unrelated bug in that same function: it silently produces a shorter shuffled array than the target whenever the sample count doesn't divide evenly into blocks. Fixed that too. Bumped eval episodes from 20 to 150 so the sample-to-dimension ratio isn't a joke at B=128 anymore.

Reran the noise control after both fixes: 0.71 fake bits → ~0.005 fake bits. Good.

### So what does Stage 2 actually show now?

Reran the real 5-seed sweep, bandwidths 1 through 128, with the fixed learning rate and the fixed estimator. And it's a genuinely clean result, just not the one from this morning:

- Raw TE and its own noise-only surrogate baseline are basically the *same curve* at every bandwidth (both climbing 0.001 → 0.24 bits from B=1 to B=128).
- The bias-corrected TE — raw minus surrogate — sits at the noise floor the entire way across: 0.0002 to 0.012 bits. Nothing.
- Task returns stay flat and non-monotonic across all eight bandwidths.

Which means: pretty much *all* of the "clean rising trend, r=0.98–0.99" from the last commit was the estimator's own bias, not real learned coupling. Not devastating — this is exactly the kind of thing that's supposed to get caught before it goes in a paper, and it got caught. But it does mean Stage 2 isn't at "saturation not yet demonstrated" anymore. It's back at something more basic: the learned channel doesn't show any detectable sign of carrying real information yet, at *any* bandwidth. Different, earlier problem. Wrote the whole chain up honestly in `TODO.md` rather than just quietly swapping the numbers — that one's non-negotiable for this project.

### Also today: someone else's brutal peer review, secondhand

Got handed a big, fairly savage AI-generated "Reviewer #2" critique of brain-to-brain communication as a research frame in general — argued the whole premise should be reframed as cross-subject neural manifold alignment instead, cited a pile of 2025/2026 papers I hadn't seen (MindAligner, Brain-JEPA, a Platonic-representation-hypothesis-for-brains paper, a zebrafish cross-individual RBM thing). Archived the whole thing for later rather than let it steer anything today — but did go verify the actual papers it name-dropped, since a few of the author names in it didn't check out against real search results (classic hallucinated-citation smell). Real papers, wrong names on a few of them. Filed the verified reading list in `tosee.md`. Something to actually sit with later, not react to today.

### Plan for the rest of tonight

1. Real next question for Stage 2: why isn't the channel carrying anything? Check whether the speaker's messages are just collapsing to a constant (dead channel) versus actually varying but uninformative.
2. Maybe a supervised warm-start / imitation pass just to confirm the pipeline *can* learn a non-trivial code at all, before trusting any future bandwidth sweep on it.
3. Finish the episode. Jane's about to con someone and I've paused it three times already to go check a training log.

Signing off — Day 7, part two! ✌️

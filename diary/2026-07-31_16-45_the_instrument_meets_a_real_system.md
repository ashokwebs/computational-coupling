---
tags: ["#diary/entry", "#research-log", "#paper2/identifiability", "#noise-as-instrument", "#honest-null-result"]
alias: "2026-07-31_16-45_the_instrument_meets_a_real_system"
---

# Diary Entry — July 31, 2026 (4:45 PM)
**Location:** VIT-AP Hostel Room
**Mood:** Delighted in the specific way only a well-explained failure produces 🔍
**Status:** Day 12, part five (!). Asked to keep researching — took noise-as-instrument out of the toy and into the real Stage 2 system.

---

### Setting up the real test

This morning's noise-as-instrument demo worked cleanly, but it worked on a system I built specifically to make it work — a linear-Gaussian toy calibrated so the method had to succeed. `experiments/paper2_identifiability/TODO.md` already flagged the honest next step: try it on something I didn't design for it. The obvious candidate was sitting right there — the trained Stage 2 PettingZoo speaker/listener, whose Gumbel-Sigmoid channel injects real logistic noise into every transmitted bit, completely independent of the sender's private goal by construction. If Remark 2's claim is right, that noise should work as an instrument here too.

Retrained the paper's exact best config — dual auxiliary loss, B=8, 20000 episodes, entropy_coef=0.02 — from scratch to get a fresh policy pair to instrument. First good sign: this run's direct-intervention numbers came back *identical* to what's already in the paper (real −15.87, ablated −16.45 z=+0.50, randomised −18.19 z=+1.82). That's a nice, free reproducibility check I wasn't even trying to run.

Then the actual test: fix 150 goals (env seeds), redraw the channel's own noise 20 independent times per goal with the listener acting greedily so noise is the *only* thing that can vary within a goal, run all 3000 full 25-step episodes, and see whether the noise recovers anything.

### It didn't work — and that's the interesting part

First-stage F-statistic: **0.2**. The rule of thumb from this morning's toy sweep was F≳10. This is forty times below that. The IV estimate's 95% confidence interval spans −715 to +886 reward units, against episode returns that only range from about −55 to −1. Completely, appropriately useless — and I want to be clear that this isn't a disappointing result, it's exactly what the honesty machinery I built this morning is *for*. The whole point of always reporting the first-stage F was to catch exactly this kind of silent failure instead of printing a garbage point estimate and calling it a finding.

What I didn't want to do was just report "F=0.2, method failed, moving on." That's true but useless. So I decomposed the variance: across the 20 noise-only redraws of the same goal, how much does the message actually move? Answer: almost none. 0.3% of total message variance comes from the noise; 99.7% comes from which goal it is. The scatter plot makes it visible immediately — messages cluster into two tight, almost perfectly separated bands by goal, with barely any horizontal spread inside a band.

The mechanism, once I looked for it, is obvious in retrospect and I think genuinely worth writing down: this channel's speaker was trained with an auxiliary reconstruction loss (`aux_coef=200`) specifically to make the message informative, and it worked — encoding R² is around 0.9. But the way it got there was by pushing its logits to confident extremes, because that's what makes a hard threshold reliable and an MSE loss converge. Confident logits sit far from the sigmoid's decision boundary. The channel's own per-step logistic noise, which is what would normally serve as the instrument, essentially never has enough amplitude to flip a bit that's sitting at a confident extreme. **The exact optimization pressure that makes the channel worth studying is the same pressure that kills the one tool I wanted to use to study it without intervening.**

### Writing it up honestly

This isn't a refutation of this morning's toy demonstration — the math there is still correct, and the method still works when the instrument has real bite. It's a genuine, previously undocumented boundary condition: apply this to any *trained* discrete communication channel, and there's a real risk that the encoder's own optimization toward reliability quietly destroys the noise's usefulness as an instrument. That's worth knowing before anyone reaches for this method on a new system, and it's a more useful thing to have discovered than a clean confirmation would have been, because it comes with an actual mechanism attached, not just a number.

Added both results to `paper2/main.tex` Remark 2 (the toy success, then the real-system failure right after it) and updated the Limitations section to be honest about where the method stands: works on what it was built for, fails on the first thing it wasn't, diagnosed rather than swept under the rug. Recompiled clean, 16 pages. Also noted for later: human speech and EEG artifact aren't "trained" to be maximally decodable through a threshold the way this Gumbel channel is, so this specific failure mode might be much less of a problem for the eventual hyperscanning application — but that's a claim to go test, not assume.

Five things closed or advanced today: the novelty check, noise-as-instrument (toy), the BBI survey, the exposition pass, and now this. Genuinely one of the fuller research days this project has had. Calling it here.

Signing off — Day 12, part five, and I mean it this time. ✌️

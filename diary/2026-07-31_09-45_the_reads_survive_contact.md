---
tags: ["#diary/entry", "#research-log", "#paper2/identifiability", "#novelty-check", "#related-work"]
alias: "2026-07-31_09-45_the_reads_survive_contact"
---

# Diary Entry — July 31, 2026 (9:45 AM)
**Location:** VIT-AP Hostel Room (finally back to normal hours)
**Mood:** Relieved, a little giddy 😌📚
**Status:** Day 12 — the highest-risk open item on the whole program just got resolved.

---

### The homework got done

Day 11 ended with a clear assignment from the handoff doc, underlined three times: *read Kolchinsky & Wolpert (2018) and Lowe et al. (2019) properly, not from memory.* That was the load-bearing uncertainty — the thing that could mean restructuring `paper2/` around a different framing, or worse, finding out the identifiability angle was already someone else's paper.

So this morning, before touching anything else, I actually sat down and read both. Full text, not abstracts, not my own three-day-old summary of them.

**Kolchinsky & Wolpert** turned out to be much less of a threat than I'd been treating it as. Their semantic information — the viability-optimal stuff, $I_{\text{sem}}^{\text{stored}} = I_{\tilde p^*}(X_0;Y_0)$ — is entirely *monadic*. One system, one environment, no sender, no receiver, no dyad. There's no confounder in their framework because there's nothing on the other end to be confounded with. And they never claim semantic information is *non-identifiable* from observation — they just assume you have counterfactual access and build on top of it. I'd rated this 🟡 MEDIUM-HIGH risk on Day 11 from memory. On an actual read it's closer to 🟢 LOW-MEDIUM: a genuinely good citation (nearest neighbor for "meaning = causal relevance, not correlation"), but not a competitor. That's a relief I wasn't expecting.

**Lowe et al.** is the one that actually mattered, and it's a more interesting read than I gave it credit for. Their matrix-communication-game experiments give real numbers: Speaker Consistency positive (0.19 to 0.54 depending on game size) while Causal Influence of Communication sits at the floor — "no effect on the opponent's action for the vast majority of games." That's an independent replication of the exact dissociation shape we found in Stage 2, in a completely different environment. Good — that means this isn't a fluke of our particular PettingZoo setup.

But two things hold up under the full read that I only had secondhand before:

1. They never run an oracle control. No condition where they hand the receiver the sender's information directly, unmediated, to see if it would use it for free. That's exactly the move that made our result sharp — remove the whole question of channel quality — and it's just absent from their paper.
2. Their explanation is *architectural*, not conventional. Shared hidden layers between the action head and the comm head spuriously correlate messages with actions — they even show SC=0.171 with **untrained** communication parameters, which is basically the network's plumbing faking positive signalling. That's a totally different mechanism from ours. Our diagnostic chain — separate speaker/listener nets, the aux-loss fix that got encoding to R²=0.90, the listener's own reconstruction head decoding the goal at 0.0016 error — already rules the architectural story out for our system. The information is genuinely, causally present and the policy head still won't touch it. Same symptom, different disease, and now I can say that with the actual numbers instead of a hand-wave.

They frame the whole thing as a *metric pitfall* — title says it, abstract says it, the fix they recommend is "measure CIC, use several metrics." Never once do they suggest this might be structurally unrecoverable no matter which metric you pick. That's the actual daylight between their paper and ours, and it's real, not motivated reasoning.

---

### What I did with it

Didn't just update a memory note and move on — went back into `paper2/main.tex` §8 and tightened the related-work paragraph on both papers: added the CIC numbers as a concrete second data point, and added the one-line structural reason K&W doesn't reach dyadic coupling (monadic vs. dyadic — it's the sharpest single sentence I've written about that comparison). Recompiled — 14 pages, bibtex resolves clean, no undefined refs, no broken citations. `novelty_assessment.md` now has a §6 with the full verified writeup, dated separately from the original memory-based assessment so it's clear what was checked and when. `handoff.md`'s three-item priority list has item 1 struck through as done.

Net effect: the paper's novelty claim survives contact with its two nearest neighbors. Nothing needs restructuring. That's genuinely good news and I'm trying not to oversell it beyond exactly that — the claim is "the two closest papers don't preempt this," not "this is definitely novel," and definitely not "this is definitely right." Two items are still open: the hostile-referee cold read of the compiled PDF, and the human–AI dissociation experiment, which is still the one that actually matters most. Reading papers de-risks; it doesn't replace running the thing nobody's run yet.

---

### Small honest note to self

I noticed while writing the update that my Day 11 risk ratings were set from a summary I'd built up over a few days without the source in front of me, and they were measurably off — too cautious on K&W, right but underspecified on Lowe. Worth remembering: threat assessments written from memory decay fast and skew conservative in the wrong ways (you remember that something is "close" more easily than you remember exactly *how* it's close). Next time something like this comes up, read first, assess second, even if it costs an extra day.

The Mentalist is still paused. Jane's con is still pending. One of these days.

Signing off — Day 12, homework actually done for once. ✌️

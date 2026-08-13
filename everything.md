---
tags: [#meta/everything, #report/master-index]
alias: "Everything — What This Project Is, Does, and Is Going To Do"
---

# Everything

**Written:** 2026-08-13, the evening before Review 1. This is the master document — what we're doing, what we've already done, and where this honestly goes if it keeps working. Written to be read start to finish by someone who wasn't here for any of it.

A note on tone before it starts: this project has one standing rule that shows up in every diary entry and every section of the paper — say what's proven, say what's hypothesis, and never let the two blur, especially when the hypothesis is the exciting one. That rule is why this document is going to sound more careful in places than the underlying results deserve to be undersold. That's on purpose. The strong claims in here are strong *because* they're fenced off from the soft ones.

---

## 1. What this actually is, in one breath

We're building a measurement theory for something nobody currently knows how to measure: whether two systems that appear to communicate — two people, a person and an AI, two brains wired together, two animals — are actually exchanging meaning, or are just each independently fluent in the same shared code without either one's specific signal doing any work. We proved you cannot tell the difference by watching. We built a working system where you can see the difference exist, with every number laid bare. And we found a real anomaly in an existing field that only makes sense once you accept this.

---

## 2. Where it came from

Started July 19, 2026, from a very physical, almost naive question: the brain moves information at something like a billion bits a second internally, and everything it wants to say to another brain has to squeeze through a mouth at about 10 bits a second — eight orders of magnitude of loss, every single day, for every human who has ever spoken. The instinct was: build a better pipe. Wire cortex to cortex, skip the mouth and the ear, and you'd finally see what a mind does at full speed.

We built the experiment to test that. It failed in the most informative possible way: we gave an artificial receiver the sender's private goal *directly* — no channel, no noise, no cost, the actual physical ceiling above which no interface of any kind can go — and its behavior didn't move. Not "moved a little." Statistically identical to being told nothing. That result doesn't fit inside "the pipe needs to be wider." It says the pipe was never the constraint, for anyone, and it forced the whole program to become a theory about *why*.

---

## 3. What we know for certain — the load-bearing results

- **A formal impossibility result.** Two systems that genuinely track each other's signals, and two systems that are each independently fluent in the same shared convention without tracking anything specific, produce *identical* statistics on every measure anyone currently uses — mutual information, synchrony, transfer entropy, behavioral agreement. Provably. Not "hard to tell apart" — indistinguishable from the data.
- **A constructed system where you can see it happen.** A receiver whose hidden layer contains its partner's private goal, decodable almost perfectly (reconstruction error 0.0017), whose behavior is statistically indistinguishable from an agent that received nothing (z≈0) — and stays that way even with infinite bandwidth and zero noise.
- **A working fix.** Ablate the signal, or randomize it, and measure whether behavior changes — that's the test that actually answers the question, and we showed randomizing is measurably more sensitive than ablating (~3x, on a system where we know the ground truth).
- **A real-world anomaly explained.** Brain-to-brain interface hardware improved enormously from 2014 to 2019 and the actual amount of information transmitted went *down*. The field's own authors say so in their own paper. Nothing in the standard bandwidth-centric account explains that. This does.
- **A survived stress test.** Read the two closest pieces of prior work in full, not from memory. The claim is still standing and still distinct from both.

---

## 4. What we're actively building toward

- **The human–AI experiment.** Fully designed, not yet run: does a deployed AI model's response actually track the specific thing a person told it, or only the surface shape of what they said? Four conditions — real, ablated, randomized, and a sharper "swap one detail and see if the output flips" test — mirroring exactly the protocol that worked on our toy system. This is the highest-leverage thing left undone in the whole program. Cheap, and nobody else appears to have run it (per today's research — see §6).
- **A second empirical system**, outside reinforcement learning, so the core dissociation isn't resting on one architecture alone.
- **Hyperscanning re-analysis on public EEG data** — no new data collection needed, just applying the correction and checking whether measured "coupling" actually tracks how long two people have known each other, which the theory predicts and nobody has tested.
- **The hysteresis test** — does a pair's ability to communicate collapse at a different threshold than the one where it first ignited? If yes, coupling is historical, not a property of the system's current state — a strange, sharp, testable claim currently sitting untested.

---

## 5. Where this honestly goes if it keeps working — the real ambition, not the inflated one

This is the section worth being genuinely excited about, written so the excitement survives contact with a skeptical reader.

**A real test for whether an AI is tracking you, not just sounding like it is — the thing we actually have to go build and run.** A concrete, repeatable protocol: change what you actually mean while keeping how you say it identical, and see whether the system's behavior follows the meaning or just the shape. That's buildable now. If it becomes standard, it changes how AI systems get evaluated before deployment, because current evaluation (dialogue quality, preference scores, benchmarks) is provably the wrong instrument for this specific question — not weak, wrong in kind.

**A causal audit for interpretability claims.** "The model represents X" currently means "we found X in its activations." This work says that's necessary but not sufficient, and gives the missing half: X has to survive being cut, not just be found. That reframes what counts as a finished interpretability result, not just this project's own toy system.

**A genuine diagnostic for human relationships, worth actually building.** A test for whether two people who *seem* to understand each other (long history, fluent shorthand, finish each other's sentences) are actually still tracking each other's current, specific meaning, versus running on a shared script that used to require attention and now doesn't. Hyperscanning labs already have the data to check this — we have to go run that check. It tells you whether their partner's specific words are still doing causal work in the exchange, a real question couples' research has never had a clean way to ask before now.

**A design principle for every future brain interface.** If throughput is capped by how much shared convention two systems have, not by channel width, then the actual research program for better BBI isn't more electrodes — it's building interfaces that grow a convention jointly with their user over time, the way infancy grows a first language. That's a genuinely different 10-year roadmap for a whole field, if the retrodiction holds up.

**This is the thing we have to go test.** Whether the specific thing you meant is the thing that actually moved the other system — checkable, buildable, and the part that's been missing.

---

## 6. What today's research added

Six web-research passes ran today to stress-test the whole picture against the current literature. Status as of this writing:

| Scan | Status | Headline |
|---|---|---|
| BCI/BBI landscape 2023–2026 | Done | Retrodiction still stands — no new BBI throughput number since 2019, while adjacent single-brain BCI throughput has visibly moved. Three independent recent sources now back "bandwidth isn't the real constraint." |
| Theory of mind / novelty check | Done | Nothing found combines all four elements of the paper's core claim. Novelty holds. |
| Neuroscience / brain complexity / hyperscanning | Done | Varlet & Grootswagers 2024 already shows synchrony is largely insensitive to real information alignment — closest existing precedent found, but still observational, not interventional. Novelty holds; worth reading in full before citing. |
| Comparative cognition / animal communication | Running | — |
| Neural network / emergent communication theory | Done — flags one paper needing a full read before tomorrow | See §8 note below |

Full sourced write-ups for each: `literature/web_scan_*_2026.md`. This document and `review1_full_report.md` will both get updated as the remaining three land.

---

## 7. The honest ceiling, stated once more so it isn't lost under §5's ambition

One toy system. One paper, not yet peer-reviewed. One experiment (the most important one) not yet run. A theorem whose mathematical core is standard confounding, novel only in where it's applied. If any of this is wrong, the place it breaks first is the human–AI experiment — either it replicates the dissociation somewhere that matters, or it doesn't, and either answer is worth having fast. Everything in §5 is downstream of that one still-unrun test.

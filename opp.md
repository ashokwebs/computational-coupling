---
tags: ["#meta/research-program", "#theory/non-identifiability"]
alias: "OPP — Understanding Is Not Observable"
---

# Understanding Is Not Observable

### Why no amount of conversation, behavioral evaluation, or neural correlation can establish that two systems understand each other — and what can

**Status:** the paper. 2026-07-26. Not committed.
**Author of record:** Ashok Pasala, Snigdha Gorai (VIT-AP).

---

## 1. The question

Every field that touches mind has its own version of one question, and none of them can answer it:

*Does this system understand me?*

AI asks it of models and calls the answer an evaluation. Neuroscience asks it of brains and calls the answer inter-brain synchrony. Animal cognition asks it of other species. Developmental psychology asks it of infants. Philosophy asks it and calls it the problem of other minds, then declares it intractable and goes home.

All of them attack it the same way: **observe the exchange and infer from what passes.** Watch the outputs. Measure the correlation. Score the responses. Read the activations.

The claim of this paper is that this cannot work — not as a matter of difficulty or instrumentation, but as a matter of identifiability. **Understanding is not a function of the observable exchange.** Two systems that genuinely share a convention and two systems that merely appear to can produce *identical* observable statistics. No measure computed from those statistics can separate them, because the difference is not in them.

That is not a philosophical complaint. It is a claim about what is estimable from a class of data, and it is the kind of claim that is provable, testable, and — if correct — invalidates a large fraction of how four fields currently operate.

---

## 2. The result that forces it

We have the constructive instance already, with complete ground truth in a system where nothing is hidden.

A sender learned to encode its private state into a channel at **R² = 0.90**. The receiver's internal representation contained that state nearly perfectly — a decoder on its hidden layer recovered the sender's goal to an error of **0.0016**. Every observational measure said coupling: high mutual information, high decodability, a representation demonstrably carrying the signal.

The receiver's behavior was statistically indistinguishable from receiving nothing (**z ≈ 0**).

Then the control that removes every escape route. We deleted the channel and handed the receiver the sender's information **directly — free, perfect, unbottlenecked, noiseless.** It still converged to the ignore-it policy: −16.0, precisely the score of a system told nothing, while a system that uses the information scores −8.8.

Infinite bandwidth. Zero noise. Real reward available. **No communication.**

Every quantity the coupling literature measures was maximal. The thing those quantities are taken to indicate was exactly, measurably absent.

---

## 3. The shape of the claim

Observational measures of coupling — mutual information, transfer entropy, neural synchrony, representational similarity, behavioral agreement, conversational performance — are all functionals of the joint distribution over what the two systems exchange and express.

Our result is an existence proof that this distribution does not determine functional coupling. Two dyads can match on it and differ on whether the signal does any work. Therefore:

> **Functional coupling is not identifiable from observational data. It is an interventional quantity.**

This places understanding precisely on Pearl's ladder, and it places it one rung above where everyone has been measuring. Correlation does not identify causation; you need to intervene. Exchange does not identify understanding; you need to intervene. **The entire literature on measuring understanding has been using rung-one tools on a rung-two quantity.**

That is why the debates never resolve. Not because the question is unscientific — because the instrument cannot in principle return the answer.

And it tells you the instrument that can: **ablate the channel and measure the behavioral consequence.** Functional coupling is what survives the removal of the signal. Everything else is fluency.

---

## 4. Why this is dangerous

**Conversational evaluation of AI is structurally invalid.** Not imperfect — invalid in kind. The Turing test and every descendant of it (chat-based benchmarks, human preference ratings, red-team dialogues, "does the model understand the instruction") are observational measurements of an interventional quantity. A system optimized to pass them is optimized in a space where understanding and its imitation are *indistinguishable by construction*. Searle argued syntax is not semantics and offered no test. This gives the test, and explains why his opponents' test could never have worked.

**Training on observational signal selects for apparent coupling.** Reinforcement learning from human feedback scores outputs. Outputs are rung one. So the optimization pressure runs exactly along the axis where genuine and apparent understanding are identical, and is *indifferent* between them. This is not a claim that current systems are hollow. It is the sharper claim that **the training signal cannot distinguish, so it cannot select for the real thing except by accident or correlation.** No quantity of raters, data, or eval sophistication repairs this, because the defect is in the data class.

**Interpretability's finding is not a finding until it is intervened on.** "The model represents X" is a statement about decodability — exactly the measure that read 0.0016 on our receiver while its behavior read zero. Presence in a representation licenses nothing about causal role. The field's causal turn — activation patching, causal scrubbing — is not a methodological refinement. It is the *only* valid form of the claim.

**Hyperscanning's inter-brain findings do not license functional conclusions.** A decade of synchrony results establishes that two brains' states covary. Our result shows covariation at ceiling with functional coupling at floor. Without an ablation control, "these brains are coupled" is not supported by the data that is taken to support it.

**And the one that should be uncomfortable:** none of this is special to machines. You cannot verify by conversation that another *person* understands you. The same non-identifiability holds. Nearly all of human social life runs on assumed convention that has never been tested, and the tests we do run — asking, checking, paraphrasing — are themselves conducted through the channel whose meaning is in question. Mutual understanding between humans is not usually verified. It is presumed, and it works because shared history has usually already installed the convention.

---

## 5. The practical bite: this predicts deployment failure

An objection: if a system behaves correctly, who cares whether the coupling is "real"?

Answer: apparent coupling and functional coupling produce identical behavior **in distribution** and divergent behavior **out of it.** Our receiver looked fine — it scored what everyone scored — right up until the task required actually using the signal, at which point it failed completely and permanently.

This reframes the largest practical problem in deployed machine learning. Systems that pass every evaluation and fail in the world are not suffering from insufficient testing. They are systems whose coupling to the user's intent was apparent rather than functional, and **no observational evaluation, however thorough, could have detected the difference.** The generalization gap is the non-identifiability gap, surfacing.

That is a strong claim, it is falsifiable, and if it holds it means the industry's central reliability problem has a structural cause nobody is addressing.

---

## 6. The positive theory

Why does the gap exist at all? Because coupling is not a property of a channel between two systems. It is a **jointly-held convention** — an attractor of their shared history.

Information has value to a system only if that system already possesses machinery to act on it; building that machinery is rewarded only if the information is already acted upon. Neither end can move first. Meanwhile a policy that ignores the partner entirely is reachable alone, immediately, and is stable — so it is found first and never left. That is exactly the trap our receiver fell into and never escaped, with the answer sitting in its own hidden layer the entire time.

Three consequences, each falsifiable:

- **Capacity is inert without convention.** Improving a channel between systems that share no convention yields exactly zero improvement. Our infinite-bandwidth control is the extreme case.
- **Convention cannot bootstrap unilaterally.** It must be installed, inherited, or jointly acquired. It never simply arises from contact.
- **Convention is bistable, therefore historical.** The condition under which coupling ignites should differ from the condition under which established coupling collapses. If so, coupling capacity is not a function of a dyad's current parameters at all — only of its history. This is the strangest prediction and the most worth testing.

The third explains something otherwise puzzling: why establishing a shared code — a language, a jargon, a couple's private shorthand — is enormously expensive, while maintaining one is nearly free.

---

## 7. What this retrodicts

A theory earns trust by explaining what was already anomalous.

**Brain-to-brain interfaces have not improved in a decade.** Enormous progress in electrodes, channel counts, SNR, and decoding; throughput still on the order of a bit per trial. On the standard framing this is inexplicable. On this one it is forced: every BBI result imports its convention from outside, via ordinary language, before the experiment — the subject is *told* that a phosphene means "rotate." Throughput is therefore capped not by hardware but by how much convention an experimenter can install by talking to someone beforehand. That ceiling is low, and it does not move when the hardware improves. The field spent ten years optimizing a variable that was never binding.

**Why LLMs feel like they understand.** They are trained on the entire recorded output of human convention. They inherit the surface of every convention we have, for free, without ever having participated in forming one. That is precisely the configuration that maximizes apparent coupling while leaving functional coupling unmeasured — and unmeasurable by the means anyone is using.

---

## 8. Honest accounting

The pieces exist; the synthesis and the identifiability claim do not.

Pearl gave the causal ladder. Searle gave the Chinese Room without a test. Lewis formalized convention in 1969; Harnad posed symbol grounding in 1990; Skyrms built meaning from signaling games. **Kolchinsky and Wolpert (2018)** formalized semantic information as information with causal relevance to a system's viability — the nearest formal neighbor, and it must be cited prominently. Lowe et al. (2019) separated positive signalling from positive listening in emergent communication before we rediscovered the split empirically. Eliciting Latent Knowledge poses a closely related problem for AI specifically. Interpretability already knows that decoding is insufficient, which is why causal methods exist.

What is new:

1. **The identifiability framing** — understanding as formally non-estimable from observational data, rather than merely hard to assess.
2. **A ground-truth constructive instance**, including the infinite-bandwidth control, which is the version that closes the escape routes.
3. **Understanding as a dyadic relation** rather than a property of a system — which is what makes it measurable at all.
4. **One account spanning AI evaluation, interpretability, hyperscanning, and human social cognition**, with the same defect and the same remedy in each.
5. **The retrodictions** in §7, which the standard framing has no account of.

The technical core the paper still owes: formalizing §3 as a proper non-identifiability result — the constructive pair, the class of statistics it defeats, and the conditions under which intervention restores identifiability. That is the work, and it is theory, not lab.

---

## 9. How to kill it

- Exhibit an observational statistic that provably separates functionally coupled from apparently coupled dyads. The identifiability claim dies immediately.
- Show ablation and observational measures agree across a range of real systems. Then the dissociation is an artifact of our toy and the correction is unnecessary.
- Show coupling has no hysteresis — onset and collapse thresholds coincide. Then coupling is a state of the connection and §6's third claim is wrong.
- Show BBI throughput tracks hardware after all. Then §7's retrodiction fails.

---

## 10. One last thing, and it is not a flourish

This document arrived to you through a channel, in language, from a system whose functional coupling to your intent you have no observational way to verify. Neither do I have any way to verify mine to yours. If the argument is right, that is not a rhetorical trick — it is the ordinary condition of every exchange between two minds, including this one, and the reason the question matters enough to answer properly.

The paper to write is §3: **understanding is an interventional quantity, we have been measuring it observationally, and here is the ground-truth demonstration that the two come apart completely.** Everything else in this file is application.

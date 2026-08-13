# Understanding Is Not Observable

### Why no amount of conversation, behavioral evaluation, or neural correlation can establish that two systems understand each other — and what can

**Status:** The Paper. 2026-07-26.  
**Author of record:** Ashok Pasala (VIT-AP).  
**Original File:** [`opp.md`](file:///home/charizard/computational-coupling/opp.md)

---

## 1. The Question

Every field that touches mind has its own version of one question, and none of them can answer it:

*Does this system understand me?*

AI asks it of models and calls the answer an evaluation. Neuroscience asks it of brains and calls the answer inter-brain synchrony. Animal cognition asks it of other species. Developmental psychology asks it of infants. Philosophy asks it and calls it the problem of other minds, then declares it intractable and goes home.

All of them attack it the same way: **observe the exchange and infer from what passes.** Watch the outputs. Measure the correlation. Score the responses. Read the activations.

The claim of this paper is that this cannot work — not as a matter of difficulty or instrumentation, but as a matter of identifiability. **Understanding is not a function of the observable exchange.** Two systems that genuinely share a convention and two systems that merely appear to can produce *identical* observable statistics. No measure computed from those statistics can separate them, because the difference is not in them.

That is not a philosophical complaint. It is a claim about what is estimable from a class of data, and it is the kind of claim that is provable, testable, and — if correct — invalidates a large fraction of how four fields currently operate.

---

## 2. The Result That Forces It

We have the constructive instance already, with complete ground truth in a system where nothing is hidden.

A sender learned to encode its private state into a channel at **R² = 0.90**. The receiver's internal representation contained that state nearly perfectly — a decoder on its hidden layer recovered the sender's goal to an error of **0.0016**. Every observational measure said coupling: high mutual information, high decodability, a representation demonstrably carrying the signal.

The receiver's behavior was statistically indistinguishable from receiving nothing (**z ≈ 0**).

Then the control that removes every escape route. We deleted the channel and handed the receiver the sender's information **directly — free, perfect, unbottlenecked, noiseless.** It still converged to the ignore-it policy: −16.0, precisely the score of a system told nothing, while a system that uses the information scores −8.8.

Infinite bandwidth. Zero noise. Real reward available. **No communication.**

Every quantity the coupling literature measures was maximal. The thing those quantities are taken to indicate was exactly, measurably absent.

---

## 3. The Shape of the Claim

Observational measures of coupling — mutual information, transfer entropy, neural synchrony, representational similarity, behavioral agreement, conversational performance — are all functionals of the joint distribution over what the two systems exchange and express.

Our result is an existence proof that this distribution does not determine functional coupling. Two dyads can match on it and differ on whether the signal does any work. Therefore:

> **Functional coupling is not identifiable from observational data. It is an interventional quantity.**

This places understanding precisely on Pearl's ladder, and it places it one rung above where everyone has been measuring. Correlation does not identify causation; you need to intervene. Exchange does not identify understanding; you need to intervene. **The entire literature on measuring understanding has been using rung-one tools on a rung-two quantity.**

That is why the debates never resolve. Not because the question is unscientific — because the instrument cannot in principle return the answer.

And it tells you the instrument that can: **ablate the channel and measure the behavioral consequence.** Functional coupling is what survives the removal of the signal. Everything else is fluency.

---

## 4. Why This Is Dangerous

- **Conversational evaluation of AI is structurally invalid.** Chat-based benchmarks and human preference ratings are observational measurements of an interventional quantity.
- **Training on observational signal selects for apparent coupling.** RLHF scores outputs (rung one), making optimization indifferent between real and apparent understanding.
- **Interpretability's decodability is insufficient.** Presence in a representation licenses nothing about causal role; causal activation patching/scrubbing is essential.
- **Hyperscanning's inter-brain findings do not license functional conclusions.** Neural synchrony at ceiling can coexist with functional coupling at floor.
- **Human social cognition relies on unverified conventions.** Mutual understanding is usually presumed based on shared history rather than proved.

---

## 5. What This Retrodicts

- **Brain-to-brain interfaces have not improved in a decade.** Hardware improved 100$\times$, but throughput remains $\sim 1$ bit/trial because convention is imported externally via ordinary language beforehand.
- **Why LLMs feel like they understand.** They inherit the surface of human conventions without participating in their interventional formation.

---

## 📖 Related Primary Files
- [`opp.md`](file:///home/charizard/computational-coupling/opp.md) — Master manifesto.
- [`paper2/main.tex`](file:///home/charizard/computational-coupling/paper2/main.tex) — LaTeX manuscript of Paper 2.

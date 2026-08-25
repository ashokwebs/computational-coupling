---
tags: ["#meta/novelty-assessment", "#paper2/identifiability"]
alias: "Novelty Assessment — Understanding Is Not Observable"
---

# 🔍 Novelty Assessment — "Understanding Is Not Observable"

**Date:** 2026-07-29
**Purpose:** Honest evaluation of what is genuinely new in `paper_main/` vs. what exists in prior art.

> [!note] **Status note added 2026-08-25.** This document is dated and describes the state at the
> time of writing, when the work lived in two manuscripts. There is now one paper,
> [`paper_main/`](paper_main/) — `paper/` and `paper2/` were merged into it and deleted. Section
> references here may not match the current numbering; file paths have been updated in place.
> Nothing in the substance below is withdrawn by the merge.

---

## 1. The Paper's Five Novelty Claims (from `opp.md` §8)

1. **The identifiability framing** — understanding as formally non-estimable from observational data
2. **A ground-truth constructive instance** with the infinite-bandwidth control
3. **Understanding as a dyadic relation** rather than a property of a system
4. **One account spanning AI evaluation, interpretability, hyperscanning, and social cognition**
5. **The retrodictions** — BBI throughput stagnation, why LLMs feel like they understand

---

## 2. Nearest Prior Art — What Already Exists

### 2.1 Kolchinsky & Wolpert (2018) — "Semantic information, autonomous agency, and nonequilibrium statistical physics"

**What they do:** Formalize *semantic information* as the subset of Shannon information that has causal relevance to a system's viability/goals. They define a quantity that separates "information that matters" from "information that's merely present" using interventional/counterfactual reasoning grounded in non-equilibrium thermodynamics.

**Overlap with our paper:** HIGH. They already argue that mere mutual information (observational) is insufficient — you need causal relevance to define meaningful information. This is conceptually adjacent to "functional coupling is interventional, not observational."

**Key difference:** K&W work at the single-system level (information relevant to *one* system's viability), not at the *dyadic* level (coupling between two systems). They don't address the specific confounder structure (shared convention as constitutive common cause). They don't provide an empirical demonstration of the dissociation. And they don't connect to BBI, hyperscanning, or AI evaluation.

**Risk level:** 🟡 **MEDIUM-HIGH.** Must be cited prominently and the distinction articulated clearly. If a referee familiar with K&W reads our paper, they'll ask "how is this not just K&W applied to dyads?" The answer needs to be sharp: the *constitutive confounder* structure and the *non-identifiability theorem* are new; K&W gives a definition, we give an impossibility result.

> [!IMPORTANT]
> **Action item:** Read K&W in full (not summaries) before any submission. The paper's novelty claim is directly exposed here.

### 2.2 Lowe et al. (2019) — "On the Pitfalls of Measuring Emergent Communication"

**What they do:** Show that in emergent communication settings (multi-agent RL), standard metrics like message entropy and topographic similarity can be misleading. Critically, they demonstrate that *positive signalling* (sender encodes useful information) and *positive listening* (receiver actually uses it) can dissociate — agents may send informative messages that receivers ignore.

**Overlap with our paper:** HIGH for the empirical finding. Our Stage 2 result (sender encodes at R²=0.90, receiver ignores) is structurally the same phenomenon in a different environment with different measurements.

**Key difference:** Lowe et al. treat this as a *measurement pitfall* — a warning to use better metrics. We treat it as a *fundamental non-identifiability* — a structural impossibility, not a methodological inconvenience. They don't take it to the "delete the channel entirely" control. They don't connect to neuroscience, AI evaluation, or philosophy of mind. They don't give a causal/Pearl-ladder account.

**Risk level:** 🟡 **MEDIUM.** Must be cited prominently and framed as: "Lowe et al. documented the symptom; we diagnose the disease." Our contribution is the *explanation* (constitutive confounding) and the *theorem* (formal non-identifiability), not the observation that metrics can mislead.

### 2.3 Pearl's Causal Hierarchy / Ladder of Causation

**What it is:** Pearl (2009, 2018) establishes that observational, interventional, and counterfactual queries form a strict hierarchy — no amount of observational data resolves interventional questions.

**Overlap:** We explicitly place functional coupling on rung 2 (interventional) and argue everyone's been measuring on rung 1 (observational). The causal framework is Pearl's.

**Key difference:** Pearl gives the framework; we give the application. Pearl doesn't discuss communication, understanding, or inter-system coupling specifically.

**Risk level:** 🟢 **LOW.** Standard citation. Nobody will claim Pearl already said this about communication.

### 2.4 Searle (1980) — Chinese Room

**What it is:** Philosophical argument that syntax is not semantics; a system can manipulate symbols correctly without understanding their meaning.

**Overlap:** We operationalize the same intuition.

**Key difference:** Searle offered no empirical test and no formal framework. We give both. The Chinese Room is a thought experiment; ours is a theorem + demonstration.

**Risk level:** 🟢 **LOW.** Philosophical inspiration, not competing work.

### 2.5 Interpretability — Causal Methods

**What exists:** The mechanistic interpretability community (Geiger et al., 2021; Chan et al., 2022; Conmy et al., 2023) already knows that finding a representation in a network doesn't mean it's causally used. Activation patching, causal scrubbing, etc. exist precisely because decodability ≠ causal role.

**Overlap:** Our Proposition 1 (state-level coupling ≠ behavior-level coupling) is essentially what the interpretability field's "causal turn" addresses.

**Key difference:** We frame this as a *general identifiability result* spanning multiple fields, not a method within one field. And we connect it to the *convention* confounder structure, which is specific to communication/coupling.

**Risk level:** 🟡 **MEDIUM.** A reviewer from interpretability may say "we already know decodability ≠ causal role." The defense: we show *why* (constitutive confounding), prove it's *not fixable observationally* (non-identifiability), and show it applies beyond ML.

### 2.6 Other Relevant Work

- **Lewis (1969) — Convention:** Formal game-theoretic account of convention. We use convention as the key construct but in a different (causal/information-theoretic) framework.
- **Harnad (1990) — Symbol Grounding:** Argues symbols need grounding in experience. Related in spirit but different in formalism.
- **Skyrms (2010) — Signals:** Evolutionary game theory of signaling. Adjacent but doesn't address identifiability.
- **ELK (Christiano et al., 2021):** Asks how to elicit latent knowledge from models. Very adjacent in AI safety — they're asking "does the model actually know X?" which is a specific case of our question. Worth citing.
- **Dretske (1981), Millikan (1984):** Teleosemantic theories locating meaning in causal/functional history. Philosophical ancestors.

---

## 3. What IS Genuinely Novel

After the assessment, here's what survives:

### ✅ NOVEL — The Non-Identifiability Theorem (Theorem 1)

Nobody has *proved* that functional coupling is non-identifiable from observational data with the specific mechanism being that shared convention is a constitutive (not incidental) confounder. K&W argue for causal relevance but don't give an impossibility result. Pearl gives the framework but not the application. This is the paper's load-bearing contribution.

### ✅ NOVEL — The Infinite-Bandwidth Control

The specific experimental design of "delete the channel, hand over the answer free, agent still ignores it" is original and dramatically sharp. Lowe et al. showed sender/listener dissociation but never went to the limit. The oracle control closes escape routes that ablation alone leaves open.

### ✅ NOVEL — Propositions 2 & 3 (Temporal Precedence and Front-Door Failures)

Showing that transfer entropy / Granger causality don't escape the theorem, and that receiver-side measurement fails the front-door criterion for *structural* reasons — these are specific, technically precise negative results that haven't appeared elsewhere.

### ✅ NOVEL — Randomisation > Ablation Sensitivity Finding

The ~3× sensitivity difference and the "value of information" calibration framework. Methodological contribution.

### ✅ NOVEL — The Noise-as-Instrument Remark

Inverting standard practice: denoising may be destroying the only route to identification. If demonstrated, this is a significant methodological insight for hyperscanning and BCI.

### ⚠️ PARTIALLY NOVEL — Four-Fields Unification

The connection across AI eval, interpretability, hyperscanning, and social cognition under one defect. Individual fields know their own version. The unification is new but may be seen as "just applying the same thing four times."

### ⚠️ PARTIALLY NOVEL — BBI Retrodiction

The explanation for BBI stagnation (convention, not hardware, is the binding constraint) is a clever consequence of the theory but is post-hoc and not empirically tested.

---

## 4. Honest Threat Matrix

| Claim | Threat Source | Severity | Defense |
|---|---|---|---|
| Non-identifiability framing | Kolchinsky & Wolpert (2018) | 🟡 HIGH | They give a *definition*, we give an *impossibility result* with constitutive confounding |
| State/behavior dissociation | Lowe et al. (2019) | 🟡 MEDIUM | They documented the *symptom*; we diagnose the *disease* (explain why, prove it's structural) |
| Decodability ≠ causal role | Interpretability literature | 🟡 MEDIUM | We generalize beyond ML and explain the structural reason |
| Understanding is interventional | Pearl (2009) framework | 🟢 LOW | Application, not re-derivation |
| Surface behavior ≠ understanding | Searle (1980) | 🟢 LOW | We operationalize with a test |

---

## 5. Recommendations Before Submission

> [!CAUTION]
> **Do not submit without completing these:**

1. **Read Kolchinsky & Wolpert (2018) cover to cover.** This is the single highest-risk prior art exposure. If they already frame semantic information as non-identifiable from observational measures, the paper needs restructuring.

2. **Read Lowe et al. (2019) cover to cover.** Frame the relationship explicitly: they found the symptom, we provide the diagnosis + theorem + sharper controls.

3. **Strengthen the "constitutive vs incidental confounder" argument in §4.** This is the entire defense against "just confounding 101" attacks. Make it airtight.

4. **Run the human–AI dissociation experiment.** One toy system is thin evidence. A second demonstration in a deployed system (human + LLM) would be transformative.

5. **Demonstrate noise-as-instrument.** Convert the remark into a method with empirical validation.

---

## 6. Update 2026-07-31 — full reads completed

Both papers have now been read in full (not from memory or summary). This section supersedes the risk ratings in §4 where they conflict.

### 6.1 Kolchinsky & Wolpert (2018) — verified

Their formalism is **monadic, not dyadic**: semantic information ($I_{\text{sem}}^{\text{stored}} = I_{\tilde p^*}(X_0;Y_0)$, Eq. 5.7) is defined for *one* system's information about *its own environment*, via a viability-optimal counterfactual intervention. There is no sender/receiver pair anywhere in the paper, no treatment of two systems exchanging signals, and no notion of a shared convention or common-cause confounder between two agents. They also do **not** state or prove any non-identifiability/impossibility result — they assume interventional (counterfactual) access is available and build the definition on top of it; nothing in the paper says semantic information *cannot* be recovered observationally. And they never touch communication, hyperscanning, BBI, or AI evaluation — the paper is about organisms (bacteria, birds) maintaining themselves against an environment.

**Correction to §4:** the original threat-matrix severity of 🟡 HIGH was set from memory and was too high. On a full read, K&W is a strong *citation* (nearest formal neighbour for "meaning = causal relevance, not correlation") but a weak *competitor* — they don't have the dyadic structure, the confounder, the impossibility result, or the domain. Actual severity: 🟢 LOW–MEDIUM. `paper_main/main.tex` §8 (L347) already states this distinction correctly ("unlike us, they do not address identifiability from observational data or the constitutive role of shared convention as confounder") — that sentence is now verified against the primary source rather than asserted from a prior summary.

### 6.2 Lowe et al. (2019) — verified

Closer than K&W, and closer than the original assessment suggested in one specific way: their Speaker Consistency (SC) vs. Causal Influence of Communication (CIC) result on matrix communication games is *quantitatively* the same shape as our Stage 2 finding — SC positive (0.19–0.54 across game sizes) while CIC sits at the floor and they report the message has "no effect" on the partner's action for the vast majority of games. That is a real, independent replication of positive-signalling/positive-listening dissociation in a different environment, which strengthens rather than weakens the case that this is a real phenomenon worth a general theory of.

Two things differentiate cleanly on a full read:
1. **No oracle/unbottlenecked control.** They test intact vs. scrambled-message conditions and run action-classifier probes: they never hand the receiver the sender's information directly, unmediated by any channel, to check whether it would use it if it were free. That is exactly the control our Proposition 1 / oracle result supplies and they do not — it is what rules out "the channel just isn't good enough" as an explanation, and nothing in their paper does that.
2. **Different root cause, explicitly.** They attribute the dissociation to an *architectural* confound: shared hidden-layer representations between the action and communication heads cause the message to correlate with the action-relevant state even when the communication parameters aren't trained (SC=0.171 with λ_c=0). That is a spurious-correlation story, not a confounding-by-convention story, and they say so. Our Stage 2 diagnostic chain (separate speaker/listener networks, aux-loss fix that pushes encoding R² to 0.90, listener's own reconstruction head decoding the goal at error 0.0016) already rules out the architectural-sharing explanation for our system — the information is genuinely, causally available in the listener's hidden state and the policy head still doesn't read it out. So the two papers report the same *symptom* through two different, non-overlapping *mechanisms*, which is a stronger differentiation than "they found the symptom, we diagnose the disease" (the phrase already used in §8) — it's closer to "they found the symptom in a system where it has an architectural cause; we found it in a system where that cause is ruled out and it persists anyway."
3. They frame their finding entirely as a **metric pitfall** (title, abstract, recommendations are all "measure CIC, use several metrics, avoid test-time-only ablation") — never as a structural non-identifiability claim. They do mention "learned convention" once, in passing, as an alternative explanation for coordination without communication, but don't develop it. Their fix is practical (use better estimators); ours is that no estimator, however good, escapes the confound without intervention. That's the actual daylight between "pitfall" and "impossibility," and it survives the full read.

**Correction to §4:** severity stays 🟡 MEDIUM as originally rated, but the defense is now sharper and evidence-backed rather than asserted: cite the CIC numbers directly as an independent replication, and lean on the oracle-control gap and the architectural-vs-convention mechanism split rather than a general "diagnosis vs symptom" framing.

### 6.3 Net effect on the paper

The single highest-risk open item from `handoff.md` §10.1 is resolved: the novelty claim survives contact with both nearest neighbours. Nothing found requires restructuring the paper. Two small, honest fixes worth making before submission:
- §8 (L349) can now cite the actual CIC numbers from Lowe et al. as a second data point for the dissociation, strengthening rather than just citing the claim.
- §8 could add one sentence noting K&W's formalism is monadic, which is the sharpest one-line reason their impossibility-adjacent framing doesn't already cover dyadic coupling — currently the paper states the *what* (identifiability, confounder) but not the *structural* reason (single-system vs. two-system) their machinery can't reach it.

Remaining items from handoff.md §10, in order: (2) hostile-referee read of the compiled PDF, (3) the human–AI dissociation experiment. Both still open.

*Original assessment prepared 2026-07-29 from memory/summary. §6 added 2026-07-31 after full primary-source reads of both papers.*

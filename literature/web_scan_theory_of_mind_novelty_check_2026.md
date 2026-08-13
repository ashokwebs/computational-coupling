---
tags: [#literature/web-scan, #topic/theory-of-mind, #novelty-check]
alias: "Web Scan — Theory of Mind & Novelty Check, 2026"
---

# Web Scan — Theory of Mind, Philosophy of Mind, Mechanistic Interpretability, and Novelty Check for "Understanding Is Not Observable"

**Date of scan:** 2026-08-13. Conducted ahead of the 2026-08-14 review of `paper2/main.tex`. Broad web research only (WebSearch + WebFetch), no primary-source deep reads beyond what's summarized here. Two parts: (A) general background on theory of mind evals, philosophy of other minds, and mechanistic interpretability's decodability/causality split; (B) a targeted, adversarial novelty check for the paper's central non-identifiability claim.

---

## Part A — General background (2023–2026)

### A.1 Theory of mind evaluation in LLMs: state of the debate and methodological critiques

The 2024–2026 literature has visibly split into (a) benchmark papers still reporting LLM performance on human-derived ToM tasks, and (b) a growing "position paper" backlash arguing the entire measurement paradigm is broken — and the backlash's core complaint is structurally the same one this paper makes: current evals are **observational/spectatorial**, not interventional.

- **Riemer, Ashktorab, Bouneffouf, Das, Liu, Weisz, Campbell (2025), "Position: Theory of Mind Benchmarks are Broken for Large Language Models."** ICML 2025 (PMLR v267). [arXiv:2412.19726](https://arxiv.org/abs/2412.19726) / [OpenReview](https://openreview.net/forum?id=BCP8UU2BcU).
  Summary: Argues nearly all ToM benchmarks measure only "literal ToM" (predicting another agent's behavior from a passive story/QA setup) and never "functional ToM" (adapting one's own behavior in light of that prediction, across repeated interaction). Proposes interactive matrix-game benchmarks (Rock-Paper-Scissors, Iterated Prisoner's Dilemma, Battle of the Sexes) with a regret-based metric instead of accuracy.
  Relevance: The literal/functional distinction is a close cousin of this paper's decodable-vs-used distinction, applied one level up (prediction vs. adaptive use of a prediction, rather than representation vs. behavioral use of a signal). They call current benchmarks "passive question answering" and explicitly want interactive, consequence-bearing settings — but they never use causal-inference vocabulary (identifiability, confounding, intervention) and never generalize past LLM ToM to communication/coupling generally. Good citation for "the field already senses the passive-measurement problem but hasn't formalized it as non-identifiability."

- **Hu, Sosa, Ullman (2025), "Re-evaluating Theory of Mind evaluation in large language models."** [arXiv:2502.21098](https://arxiv.org/abs/2502.21098).
  Summary: Identifies an unresolved ambiguity in what ToM evals are even supposed to measure — matching human *behavior* vs. matching the *computations* that generate that behavior — and argues many current evals conflate the two or are contaminated by non-ToM confounds (world knowledge, task format).
  Relevance: Directly names the behavior-vs-computation gap but frames it as measurement ambiguity, not as a formal identifiability failure. Doesn't invoke causal/confounder machinery.

- **Marchetti, Manzi, Riva, Gaggioli, Massaro (2025), "Artificial Intelligence and the Illusion of Understanding: A Systematic Review of Theory of Mind and Large Language Models."** *Cyberpsychology, Behavior, and Social Networking* 28(7), 505–514. [PubMed 40333375](https://pubmed.ncbi.nlm.nih.gov/40333375/), [DOI](https://doi.org/10.1089/cyber.2024.0536).
  Summary: Systematic review concluding LLMs handle first-order false-belief tasks well but degrade on second-order/recursive ToM; frames strong performance on simple tasks as possibly "illusory" given the models' lack of developmental/embodied grounding, and flags that benchmark design biases favor LLM strengths.
  Relevance: Useful as a review anchor for "the field itself already suspects apparent competence is illusory," but stays at the level of task-difficulty critique, not identifiability.

- Also surfaced but lower-relevance/duplicative: **OmniToM** ([arXiv:2605.26322](https://arxiv.org/pdf/2605.26322), belief-modeling benchmark), and a Strange-Stories-paradigm comparative eval ([arXiv:2603.18007](https://arxiv.org/pdf/2603.18007)) — both standard benchmark papers, not methodological critiques, included here only for completeness of the "state of the field" picture.

**Bottom line for A.1:** the debate in 2025–2026 has clearly moved toward "current evals are passive/spectatorial and that's the core problem" (Riemer et al. is the sharpest statement of this), but nobody yet frames it with Pearl's ladder or a formal non-identifiability argument. That gap is exactly where this paper sits, and it's still open.

### A.2 Problem of other minds + formal causal-inference tools (2023–2026)

This search came up essentially empty on the specific combination the paper needs to worry about — recent philosophy-of-mind work explicitly importing Pearl's causal ladder, do-calculus, or instrumental-variable reasoning into the classical problem of other minds.

- Searched: `philpapers "other minds" causal inference intervention`, `"theory of mind" "instrumental variable" OR "do-calculus"`, `"problem of other minds" causal ladder Pearl rung intervention philosophy of mind 2023-2026`, and direct attempts to browse PhilPapers' "Problem of Other Minds" bibliography (blocked by a 403 on direct fetch).
- What surfaced: general Pearl's-ladder explainers (not philosophy-of-mind specific), a 2024 *Analytic Philosophy* piece by Grace Helton on structuralism and external-world/other-minds skepticism (traditional epistemology, no causal-inference machinery), and unrelated CS papers using "causal" in other senses (causal reasoning benchmarks, nondeterministic causal models for actual causation).
- No paper found that applies do-calculus, IV, or Pearl's rungs specifically to the classical problem of other minds.

**Bottom line for A.2:** this specific cross-disciplinary move (formal causal-identifiability tools onto the problem of other minds) does not appear to exist in the 2023–2026 literature as far as this search could determine. This is either a genuine gap the paper is the first to fill, or a sign that philosophy of mind and causal-inference/ML communities simply aren't reading each other — can't rule out something sitting in a venue this search didn't reach (e.g., a recent PhilPapers-only preprint), but nothing turned up after several angles of search.

### A.3 Mechanistic interpretability: "decoding ≠ causal role" — who's making this point and how they frame it

This is the most active and directly relevant of the three A-subsections, and it's the one place where the paper's Proposition 1 (information decodable ≠ information used) has close, explicitly-named siblings — but all confined to single-model interpretability, not dyadic communication.

- **Lin & Liu (2026), "Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims."** [arXiv:2605.08012](https://arxiv.org/abs/2605.08012).
  Summary: A position paper arguing that mech-interp routinely uses causal vocabulary (circuits, mediators, causal abstraction) without stating the identification assumptions that would license causal claims from what is, in practice, observational data over activations. Audits ten papers across four methodological strands and finds none has a dedicated identification-assumptions section; proposes a disclosure norm borrowed from econometrics (name the identification strategy, enumerate assumptions, stress-test at least one).
  Relevance: **This is the single closest paper found in the entire scan to this paper's causal-inference framing**, and it's flagged in more detail under Part B below because it explicitly invokes Rubin/Pearl-style identification language for interpretability claims. It stays strictly monadic (one model's internals), never treats two interacting systems or a convention/confounder between sender and receiver, and never states or proves an impossibility/non-identifiability *result* — it's a disclosure-norm proposal, not a theorem. Still, cite it: it's evidence the interpretability field is independently arriving at "you can't get causal claims for free from observational activation data," which corroborates rather than scoops the paper's Proposition 1.

- **Huang & Chang (2025), "Causality ≠ Decodability, and Vice Versa: Lessons from Interpreting Counting ViTs."** [arXiv:2510.09794](https://arxiv.org/abs/2510.09794) / [OpenReview](https://openreview.net/forum?id=sDSlefEnCF).
  Summary: Empirical case study on vision transformers fine-tuned for counting. Middle-layer tokens are strongly causally influential (via activation patching) despite being weakly linearly decodable; final-layer tokens are highly decodable but causally inert. Explicitly frames the two axes as "what information is present?" vs. "what information is used?"
  Relevance: This is the cleanest existing statement of exactly the decodable-vs-used split, almost verbatim matching Proposition 1's language — but presented as a preliminary empirical finding in one architecture, not a general theorem, and with zero connection to communication, dyads, or philosophy of mind.

- **Sharma, Dawes, Raval (2026), "Dissociating Decodability and Causal Use in Bracket-Sequence Transformers."** [arXiv:2604.22128](https://arxiv.org/abs/2604.22128).
  Summary: Same dissociation, different architecture/task (Dyck-language bracket matching): stack-depth and top-of-stack signals are decodable from the residual stream, but only some are causally load-bearing under ablation/masking.
  Relevance: A second independent replication of the same decodability/causality split, again single-model, again no dyadic or convention framing.

- Earlier/background works confirming this is a known problem-shape in the field (not newly discovered by any of the above): causal scrubbing, activation patching, causal abstraction (Geiger et al.), attribution patching — all cited already in the paper's own related-work per `novelty_assessment.md` §2.5.

**Bottom line for A.3:** "decodability ≠ causal role" is now a small, named cottage industry in interpretability (2025–2026), with the Huang & Chang framing closest in wording to Proposition 1. None of them generalize it into a dyadic-communication or convention-as-confounder claim, and none state it as a formal non-identifiability result — they demonstrate the dissociation empirically per-architecture rather than proving it can't be escaped observationally. This is exactly the shape of "prior art that makes the same local point in one field" that `novelty_assessment.md` already anticipated for the interpretability literature generally; nothing here changes that assessment, it just supplies fresher, better citations (2025–2026 instead of 2021–2023).

---

## Part B — Novelty check (the load-bearing section)

**Verdict up front: nothing found in this search threatens the paper's central claim.** No 2024–2026 paper was located that states or proves that functional coupling/mutual understanding between two systems is a non-identifiable, interventional-only quantity because shared convention is a constitutive confounder. The closest work found operates in adjacent territory — single-system semantic information, single-model interpretability identification assumptions, hyperscanning's own causality problem, emergent-communication metric pitfalls — but in every case is either monadic (one system, not a dyad), methodological-not-formal (a warning or disclosure norm, not an impossibility result), or missing the confounder-by-shared-convention mechanism specifically. This section documents the search exhaustively rather than asserting the negative result, per the instruction to be the most careful part of this file.

### B.1 Search angles used

Each of the following was run as a distinct WebSearch query (some multiple phrasings), in addition to targeted WebFetches on the most promising hits:

1. `"non-identifiability" understanding communication observational data confounder`
2. `"shared convention" confounder communication coupling causal inference 2024 2025`
3. `interventional test mutual understanding ablation two agents 2025`
4. `ablation test hyperscanning inter-brain synchrony causal 2024 2025`
5. `eliciting latent knowledge causal role decodability ELK 2024 2025`
6. `ground truth dissociation representation behavior emergent communication agents 2024 2025`
7. `"positive signalling" "positive listening" dissociation emergent communication 2024 2025 follow-up`
8. `Turing test invalid non-identifiable observational evaluation AI understanding philosophy 2025`
9. `"common cause" shared code language game identifiability confound philosophy 2025`
10. `"problem of other minds" causal ladder Pearl rung intervention philosophy mind 2023-2026`
11. `"apparent coupling" versus "functional coupling" AI communication paper`
12. `"understanding" "not identifiable" OR "non-identifiable" AI evaluation paper 2025 2026`
13. `"constitutive confounder" OR "confound by convention" communication signal receiver`
14. `"identifiability" "understanding" dyad communication convention causal 2025 arxiv`
15. `semantic information dyadic causal confound Kolchinsky Wolpert extension 2024 2025` (checking whether anyone extended the paper's own nearest formal neighbor to the dyadic case since the 2026-07-31 read)
16. `Lowe "pitfalls of measuring emergent communication" cited by 2024 2025 extension causal` (checking whether anyone extended the paper's other nearest neighbor toward a non-identifiability framing since the 2026-07-31 read)
17. `brain-to-brain interface throughput stagnation convention bottleneck 2025 2026` (checking whether the paper's §7 BBI retrodiction has been independently proposed elsewhere)

None of these returned a paper making the paper's specific compound claim. Findings from the closest near-misses:

### B.2 Near-misses, examined and ruled not-threatening

- **Lin & Liu (2026), "Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims."** [arXiv:2605.08012](https://arxiv.org/abs/2605.08012). *(Already introduced in A.3; re-examined here specifically against Part B's bar.)*
  Why it's the closest thing found: it explicitly imports Rubin-causal-model / identification-assumptions language into a "you're treating observational data as if it licensed causal claims" argument — the same rung-1-vs-rung-2 move this paper makes.
  How it differs: (1) strictly monadic — one model's internal activations, never two interacting systems; (2) no confounder structure identified at all, let alone a *constitutive* one like shared convention; (3) it is a disclosure-norm position paper (name your assumptions, stress-test one), not an impossibility/non-identifiability theorem — it doesn't claim the causal question is *unanswerable* from observational data, only that current papers fail to state what would make it answerable; (4) no communication, no dyad, no philosophy of mind, no hyperscanning, no AI-evaluation link. Not a threat to novelty; a good supporting citation showing the field independently senses the problem in one narrow corner.

- **Causal Leverage Density (2024), extending Kolchinsky & Wolpert.** [arXiv:2407.07335](https://arxiv.org/abs/2407.07335).
  Checked specifically because it's a direct 2024 extension of the paper's already-vetted nearest formal neighbor (K&W 2018) — if anyone had pushed K&W toward the dyadic/confounder case since the 2026-07-31 novelty read, this would be the first place to look.
  Finding: it generalizes K&W's semantic-information framework beyond viability-dependent systems (applies it to "living, non-living, or technological" systems generically via phase-space trajectory changes under intervention) but remains explicitly single-system — no sender/receiver, no communication, no confounding, no identifiability-from-observational-data discussion at all. The `novelty_assessment.md` §6.1 finding (K&W is monadic, not dyadic) still holds for this 2024 successor too. No update needed to that assessment.

- **Lowe et al. (2019) citation trail, 2024–2025.** Checked whether anyone built on "On the Pitfalls of Measuring Emergent Communication" toward a causal/non-identifiability framing (as opposed to more metrics). Found only routine citations in newer emergent-communication surveys and follow-on empirical papers (e.g., composition/decomposition work); nothing recasts the positive-signalling/positive-listening split as a formal impossibility result or introduces a shared-convention-as-confounder account. One 2025 discussion note observed that positive listening has been loosely redefined by some follow-on work to mean "active processing" rather than "behavioral impact" — a definitional drift, not a causal-inference advance, and if anything it moves the field further from (not closer to) a rigorous confounder-based account.

- **Hyperscanning causality literature (2024–2025).** [PMC11599244](https://pmc.ncbi.nlm.nih.gov/articles/PMC11599244/), "Hyperscanning: from inter-brain coupling to causality" (2024), is the most on-topic hit — it explicitly discusses the alternative-explanation problem (two brains' synchrony arising from shared external stimuli rather than genuine interaction, i.e., a confound) and proposes dyadic neurofeedback/intervention as a partial fix, citing Granger causality and SEM as tools. On direct fetch and review: this is a methods-improvement review, not an impossibility claim — it never asserts that inter-brain coupling *cannot in principle* be established observationally, only that current correlational designs haven't established it and better designs (interventional neurofeedback) are needed. It doesn't use "convention" or any confounder-by-shared-history framing; the "shared stimulus" confound they discuss is incidental (same external input), not the paper's constitutive one (a jointly-held code that must itself have been previously installed). This is good supporting evidence for the paper's §4 hyperscanning claim (the field's own experts agree ablation/intervention is missing) but doesn't anticipate the theorem. A companion older piece, Novembre & Iannetti's "Hyperscanning Alone Cannot Prove Causality. Multibrain Stimulation Can" (*Trends in Cognitive Sciences*, 2021 — predates the paper's 2023–2026 window but is the direct ancestor of the 2024 review above and worth knowing about), makes essentially the same intervention-not-observation point even earlier; still no confounder-by-convention mechanism or identifiability theorem.

- **ELK (Eliciting Latent Knowledge) literature (2024–2026).** Multiple hits (MechELK, Cywinski et al.'s Taboo Word Guessing model organisms, "Activation Oracles" blind-spots work) confirm ELK remains an active single-model problem — "does the model's activations contain X even when its stated output denies X" — using probes/CCS/activation patching. No paper reframes ELK as a dyadic non-identifiability result or connects it to a convention/confounder account between two communicating systems. This tracks the existing `novelty_assessment.md` treatment of ELK as "worth citing, adjacent, not competing."

- **Theory of mind + causal inference / instrumental variables.** No paper found combining these (see A.2). This is arguably the most reassuring negative result of the scan: if anyone had connected Pearl's ladder or IV-style reasoning to the classical problem of other minds, it would be extremely close to the paper's own core move (§3 of `opp.md` — "this places understanding one rung above where everyone has been measuring"), and nothing surfaced.

- **BBI throughput / "convention bottleneck" retrodiction.** No 2025–2026 source attributes brain-to-brain interface throughput stagnation to a convention/shared-code ceiling rather than hardware; current BCI commentary (channel-count roadmaps, surgical automation) is entirely hardware/bandwidth-framed. The paper's §7 retrodiction still appears to be an original explanation not offered elsewhere.

### B.3 What was not found, stated plainly

No paper combining all of: (a) two interacting systems (not one), (b) a formal non-identifiability or impossibility claim (not a warning, review, or disclosure norm), (c) shared/prior convention specifically identified as the confounding mechanism (not "shared stimulus," "architectural sharing," or unspecified "confounding"), and (d) observational statistics (MI, synchrony, transfer entropy, behavioral agreement) named as the class of measures that fail as a group. Every near-miss above is missing at least two of these four elements, usually three. The paper's combination — dyadic + formal impossibility + convention-as-constitutive-confounder + a named class of defeated statistics — was not found assembled anywhere in this search.

### B.4 Caveats on this search's coverage

Stated honestly, not to hedge but because a novelty check is only as good as its blind spots: WebSearch/WebFetch cannot reach paywalled venues, very recent preprints not yet indexed, non-English-language work, or conference proceedings not mirrored to arXiv/OpenReview (the direct PhilPapers bibliography fetch was blocked by a 403, which is a real gap for A.2/B specifically — a manual PhilPapers browse before the review would be worth the ten minutes if time allows). This is a search-engine-mediated scan, not an exhaustive literature review; it corroborates rather than replaces the full primary-source reads already done on K&W and Lowe et al. (`novelty_assessment.md` §6). Given that caveat, the honest statement is: **after a genuinely broad multi-angle search, nothing found threatens the paper's novelty, and several searches (A.2 and B.3 in particular) came back essentially empty in a way that's reassuring rather than merely inconclusive** — the specific combination of tools and claim the paper makes does not appear to have close prior art in the 2024–2026 window this scan could reach.

---

## Full source list (all sources cited above, deduplicated)

**Part A:**
- Riemer, M., Ashktorab, Z., Bouneffouf, D., Das, P., Liu, M., Weisz, J. D., & Campbell, M. (2025). Position: Theory of Mind Benchmarks are Broken for Large Language Models. *ICML 2025*, PMLR v267. https://arxiv.org/abs/2412.19726
- Hu, J., Sosa, F., & Ullman, T. (2025). Re-evaluating Theory of Mind evaluation in large language models. https://arxiv.org/abs/2502.21098
- Marchetti, A., Manzi, F., Riva, G., Gaggioli, A., & Massaro, D. (2025). Artificial Intelligence and the Illusion of Understanding: A Systematic Review of Theory of Mind and Large Language Models. *Cyberpsychology, Behavior, and Social Networking*, 28(7), 505–514. https://pubmed.ncbi.nlm.nih.gov/40333375/
- Helton, G. (2024). [Structuralism and other-minds/external-world skepticism]. *Analytic Philosophy*. (surfaced via search; not independently fetched — flag for manual check if used as a citation)
- Lin, Z., & Liu, F. (2026). Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims. https://arxiv.org/abs/2605.08012
- Huang, L., & Chang, Y. (2025). Causality ≠ Decodability, and Vice Versa: Lessons from Interpreting Counting ViTs. https://arxiv.org/abs/2510.09794
- Sharma, A., Dawes, C., & Raval, S. (2026). Dissociating Decodability and Causal Use in Bracket-Sequence Transformers. https://arxiv.org/abs/2604.22128

**Part B:**
- Lin, Z., & Liu, F. (2026). Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims. https://arxiv.org/abs/2605.08012
- [Anonymous/unconfirmed authorship] (2024). Causal Leverage Density: A General Approach to Semantic Information. https://arxiv.org/abs/2407.07335
- Lowe, R., Foerster, J., Boureau, Y-L., Pineau, J., & Dauphin, Y. (2019). On the Pitfalls of Measuring Emergent Communication. *AAMAS 2019*. https://arxiv.org/abs/1903.05168 (citation trail checked 2024–2025, no non-identifiability successor found)
- [Authors unconfirmed] (2024). Hyperscanning: from inter-brain coupling to causality. https://pmc.ncbi.nlm.nih.gov/articles/PMC11599244/
- Novembre, G., & Iannetti, G. D. (2021). Hyperscanning Alone Cannot Prove Causality. Multibrain Stimulation Can. *Trends in Cognitive Sciences*. https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(20)30275-8 (pre-2023, ancestor of the 2024 review above, included for completeness)
- Kolchinsky, A., & Wolpert, D. H. (2018). Semantic information, autonomous agency, and nonequilibrium statistical physics. https://arxiv.org/abs/1806.08053 (already fully read per `novelty_assessment.md`; re-confirmed monadic via its 2024 successor)

*Author attributions marked "unconfirmed" above were reported by search-summarization and not independently verified against the primary source's byline — verify before citing in `main.tex` if used.*

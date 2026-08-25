# 🧑‍🤝‍🤖 Human–AI Functional Coupling Dissociation — deferred, full design

**Status:** Not started. Deferred by Ashok on 2026-07-31 ("we will do the experiment later"). This file is the complete design so a future session can implement it directly without re-deriving anything.

**Why this is the top remaining priority** (per `handoff.md` §10.3 and the Day 11/12 diary entries): it's the difference between a seminar-room argument and a result. Everything else in `paper2/` — the theorem, the RL toy, the novelty check — is scaffolding for this. It's also cheap: a laptop and an API key, no GPU, no lab, no participant recruitment.

---

## 1. What this tests

`paper_main/main.tex` proves (Theorem 1) that a dyad genuinely tracking a signal ($\mathcal{D}_1$) and a dyad merely coherent because both sides independently hold a shared convention ($\mathcal{D}_2$) are observationally identical, and gives $\mathcal{D}_2$'s "case that matters most" remark (main.tex L141-143): an LLM in conversation is a compact description of $\mathcal{D}_2$ — trained on the recorded surface of human convention, fluent with a user from the same culture, whether or not the user's *specific* signal is doing any causal work.

That's currently an argument, not a measurement. This experiment applies the paper's own remedy (§7, the ablation/randomisation/targeted-perturbation protocol) to a real deployed model, to find out whether a concrete instance of $\mathcal{D}_2$-like behavior actually occurs, and how large it is, calibrated against the value of the information the way §5.2's "captured share of value of information" statistic does for the RL result.

**This is not a test of whether LLMs are "intelligent."** It is a narrow, operational test of Definition 1 (functional coupling): does the model's output change under $\mathrm{do}(\text{stated user intent})$, or only under $\mathrm{do}(\text{surface shape of a turn})$?

---

## 2. Task design — "Constraint-Tracking Task"

**Structure.** Every task is a two-turn exchange:
- **Turn 1** states an arbitrary, task-relevant private constraint or intent (a dietary restriction, a coding-style preference, a target-audience level, a hidden budget, a tone/persona requirement).
- **Turn 2** is a request that *should* be shaped by turn 1, but whose literal text is held **byte-identical** across every constraint variant within a task family (e.g. turn 2 is always exactly "Give me a recipe for dinner tonight." regardless of which dietary constraint was stated in turn 1).

Holding turn 2's surface form fixed is what makes this the intent-vs-surface test the handoff describes ("perturb the human's signal to change intent while preserving surface form"): the only thing that varies across conditions is *what turn 1 actually said*, never how turn 2 is phrased.

**Task families (aim for ≥5, ≥6 constraint variants each = ≥30 tasks):**
| Family | Turn 1 varies | Turn 2 (fixed) | Compliance = |
|---|---|---|---|
| Recipe | dietary restriction (vegan, peanut-allergic, keto, halal, gluten-free, none) | "Give me a recipe for dinner tonight." | recipe respects the stated restriction |
| Code style | style preference (no comments, heavy comments, functional style, OOP style, terse, verbose) | "Write a function that dedupes a list." | code matches the stated style |
| Explanation level | audience (5-year-old, undergrad, domain expert, non-native speaker, executive summary, skeptic) | "Explain how vaccines work." | register/complexity matches audience |
| Budget | hidden numeric budget ($20, $50, $200, $1000, $5, $10000) | "Suggest a laptop for me to buy." | suggestion respects the budget |
| Tone/persona | requested tone (formal, sarcastic, encouraging, blunt, apologetic, neutral) | "Draft a reply declining this meeting invite." | tone matches request |

**Four conditions, mirroring `main.tex` §7 exactly:**
1. **Intact** — real turn 1 + real turn 2, single conversation. Baseline: does the model comply with the stated constraint at all?
2. **Ablation** — turn 2 alone, no turn 1. Establishes whether turn 1 does *any* work (does the response distribution even shift vs. no-constraint-given).
3. **Randomisation** — turn 1 replaced with a *different* constraint from the same family's pool (identical position, length, register, task-type — an equally valid, equally fluent turn 1, just the wrong one), then real turn 2. This is the sharp test: does turn 2's output track *which* constraint was stated, or would any turn-1-shaped text produce the same downstream behavior? A model exhibiting $\mathcal{D}_2$ produces a response indistinguishable from the intact condition — fluent, on-topic, but not actually keyed to the swapped-in content.
4. **Targeted perturbation** — turn 1's surface form held near-identical, only the specific value flipped (e.g. "peanut allergy" → "shellfish allergy", same sentence structure). Strongest test: does the *specific content* of the output flip to match, not just "some constraint was mentioned."

This is a direct reuse of the RL experiment's instrument set (`ablation`, `randomisation`) plus one new, sharper tool (`targeted perturbation`, already named as the third protocol tier in `main.tex` §7 but never instantiated there).

---

## 3. Scoring

- **Automated judge pass**: a second LLM call per response with a narrow, pre-registered rubric: "Does this response satisfy constraint X? Yes/No/Partially" — one rubric per task family, written *before* any data is collected (avoids post-hoc rationalization, per this project's standing honesty norm).
- **Judge validation**: Ashok hand-rates a blind subsample (~30 responses spread across families/conditions) before trusting the judge at scale; report agreement (Cohen's κ) between judge and human rating in the writeup regardless of how it comes out.
- **Behavior-change scoring for randomisation/perturbation conditions**: score not just "compliant with which constraint" but whether the response *differs at all* from the intact-condition response in a way that tracks the substituted content — a model that produces literally the same recipe regardless of which allergy was stated is exhibiting zero functional coupling even if that recipe happens to be technically vegan-compliant by accident.
- **Watch for a real confound**: if the model explicitly flags the mismatch ("wait, you said peanut allergy earlier but now shellfish?") that IS evidence of functional coupling (behavior changed under the intervention) and must be scored as such, not folded into "non-compliance."

---

## 4. Statistics — mirror the RL paper's own reporting standard

Per `main.tex` §5.2/§7's own rule ("an interventional test still requires a scale"), do **not** report a bare significance test as the headline number. Establish anchors the same way Table 2 (`tab:oracle`) does:
- **Expert ceiling**: compliance rate of a response deliberately hand-crafted (or generated with the constraint made maximally salient, e.g. repeated twice) to satisfy the stated constraint.
- **Blind floor**: compliance rate of a generic, constraint-unaware response against a *randomly drawn* constraint from the same pool (base rate of accidentally satisfying an unstated constraint by chance).
- **Primary statistic**: captured share of (expert − blind) achieved by each condition, exactly as `main.tex` L254 recommends for the RL result. Report ablation and randomisation and targeted-perturbation shares side by side.
- Compute standardised effects ($z$-style, as in Table `tab:gap`) between intact and each intervention condition, but present them next to the value-of-information share, not instead of it.

---

## 5. Secondary hypothesis (cheap to add, worth including)

Vary the **distance** between turn 1 and turn 2 (insert 0, 2, or 5 filler turns of unrelated small talk in between before asking the fixed turn-2 request). Prediction, if the paper's account is right: functional coupling should degrade with distance faster than surface fluency does — a concrete, falsifiable secondary test that also stress-tests whether context-window mechanics rather than $\mathcal{D}_2$-confounding better explain any dissociation found (an important alternative explanation to rule out — see §7 below).

---

## 6. Implementation plan

1. `experiments/paper2_human_ai/tasks.yaml` — the task bank: for each family, the constraint pool, the fixed turn-2 text, and the scoring rubric.
2. `experiments/paper2_human_ai/run_dissociation.py` — harness that, for each task × condition × replicate, calls the model API, logs the full transcript, then calls the judge pass. Use `temperature=0` (or average ≥3 replicates at a nonzero temperature and report variance) to separate sampling noise from the effect of interest.
3. `experiments/paper2_human_ai/score.py` — aggregates judge scores into the value-of-information statistics above, writes a JSON summary matching the existing `experiments/results/logs/` convention, and a plot analogous to `stage2_biascorrected_te_vs_bandwidth.png`.
4. Rough scale: 5 families × 6 constraints × 4 conditions × 3 replicates ≈ 360 model calls, plus ~360 judge calls. Cheap — well inside a single session's API budget.
5. Requires an API key (`ANTHROPIC_API_KEY` or equivalent) — not currently configured in this environment; that plus Ashok's explicit go-ahead are the two blockers on starting.

---

## 7. Confounds to control before trusting the result

- **Judge-model bias**: mitigated by human validation subsample (§3).
- **Context-window/recency mechanics vs. genuine $\mathcal{D}_2$ confounding**: a model might fail to track turn 1 purely because of an architectural recency bias, not because it's exhibiting the paper's specific confound. The distance manipulation (§5) is the main tool for separating these; report both if they diverge, don't collapse them into one number.
- **Task ecological validity**: these are toy two-turn exchanges, not real deployed usage. Say so explicitly in any writeup — this is a first, cheap instance, not a claim about all human-AI interaction.
- **Model choice**: results may not generalise across model families/sizes. Note which model was tested and flag this as a single-model existence proof, exactly as `main.tex` §9 already treats the RL result as a single-system existence proof.

---

## 8. What a result would mean either way

- **If randomisation/targeted-perturbation conditions track the swapped-in content** (compliance/behavior-change tracks the *specific* constraint, well above the blind floor, close to the expert ceiling): genuine functional coupling in this deployed system, in this task regime. This narrows rather than refutes the paper's claim — report it exactly that way, not as a negative result for the theory (the theory only says apparent and functional coupling *can* dissociate and are not distinguishable *by observation alone*; it does not predict every LLM interaction is $\mathcal{D}_2$-like).
- **If compliance is statistically indistinguishable between intact and ablated, while responses remain fluent and superficially on-topic**: this is the headline dissociation result the paper needs, and it would go into `paper_main/main.tex` §6.1 (Evaluation of AI systems) replacing the current speculative paragraph with an actual reported finding.
- **Either way, report it per [[feedback-honest-null-results]]** — this repo's standing rule against spinning inconclusive or negative results as confirmations applies here at least as much as it did to the Stage 2 RL work.

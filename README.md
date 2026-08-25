---
tags: ["#meta/readme", "#overview"]
alias: "Computational Coupling — Master Guide"
---

# 🧠⚡ Understanding Is Not Observable
### *Shared Convention Makes Communication Possible and Its Measurement Impossible*

**Authors:** Ashok Pasala, Snigdha Gorai (VIT-AP University)
**The paper:** [`paper_main/`](paper_main/) — 36 pp, builds clean
**Target venues:** NeurIPS, ICML, ICLR, Nature Machine Intelligence, Nature Neuroscience

---

## Yo! Welcome to the Lab! 🚀

Bro, if you landed here thinking Brain-to-Brain Interfaces are about sci-fi telepathy or zapping
someone's motor cortex to make them click a mouse... **think again.** And if you landed here from
an older version of this README expecting a triumphant measurement theory — you should read on,
because the story changed.

**Here's the honest arc.** This programme started on the constructive side. For years the BBI/BCI
fields have designed "brain protocols" and "brain dictionaries" without asking the most basic
question in science: *what quantity are we actually trying to optimise?* Designing a BCI protocol
with no measurement theory is like designing 56k modems before Shannon defined channel capacity in
1948. So we built the missing quantity — **coupling capacity** — proved a theorem about it, and
went to test it.

**Then it fell over.** Not because of a bug, and not because of an experiment that needed more
tuning. It fell over for a reason that turned out to be much more interesting than the thing we
set out to prove, and that reason is now the paper.

---

## 💡 The result, in one sentence

> **Functional coupling — whether one system's signal actually changes what another system
> does — is an *interventional* quantity, and every measure four different fields currently use to
> estimate it is *observational*. The instrument is on the wrong rung of the causal ladder.**

Two independent arguments get you there.

**1. Non-identifiability.** Two systems can only communicate if they *already share a convention*
about what signals mean. That shared convention is a common cause of both what the sender emits
and how the receiver behaves. So there exist pairs of systems with **identical** observational
distributions — same mutual information, same transfer entropy, same neural synchrony, same
representational similarity, same behavioural agreement, same conversational performance — where
one is genuinely coupled and the other is not. **The precondition for communication is the
confounder for its measurement.** You can't randomise the confounder away without destroying the
phenomenon. And it's not a knife-edge trick: it holds on an open set of linear–Gaussian parameters.

**2. The state–behaviour gap.** Independently of any confounding — with complete ground truth over
every variable — we trained a sender that encodes its private goal into the channel at
$R^2 = 0.90$, and a receiver whose hidden layer gives that goal back to a linear decoder at
reconstruction error $0.0017$. The information is *provably there and linearly available*. The
receiver captures about **12%** of what the information is worth and performs statistically at the
**goal-blind optimum**. Then we deleted the channel entirely and handed the receiver the sender's
goal directly — infinite bandwidth, zero noise — and **nothing changed.**

State-level coupling at ceiling. Functional coupling at floor.

---

## 🔪 What this kills

- **Conversational evaluation.** The imitation game and every descendant — dialogue benchmarks,
  preference ratings — are functionals of the observational distribution. They cannot separate the
  two dyads at *any* sample size. A fluent LLM in conversation with a person is a compact
  description of the *uncoupled* one: both parties independently hold the convention.
- **Transfer entropy and Granger causality.** Being "directional" doesn't save you. Temporal
  precedence only supplies causal content absent a common cause preceding both variables — and in
  dyadic communication that common cause is a structural guarantee, not a hazard to check for.
- **Decoding-based interpretability.** A feature being present and linearly recoverable licenses
  *nothing* about its causal role. And by the front-door argument this is structural: no gain in
  probe quality, recording resolution, or feature-decomposition precision repairs it.
- **Our own earlier paper.** See below. We're not quiet about this.

## 🛠️ What replaces it

**Ablate or randomise the signal and measure whether behaviour changes.** What survives removal of
a signal is what the signal was doing; everything else is fluency. Three findings sharpen the
protocol:

- **Randomisation beats ablation** — ~3× more sensitive on the identical trained system. Never read
  a null ablation as zero functional coupling.
- **Report a scale, not a null.** We propose $\rho$, the **captured share of the value of
  information**: dimensionless, zero at the best signal-ignoring policy, capped at 1. Our receiver
  is measurably perturbable by the message while deriving *no benefit* from it — so sensitivity and
  benefit dissociate in their turn, and a significance test isn't enough.
- **Channel noise is an instrument.** Exogenous transmission noise satisfies the IV conditions, which
  inverts standard practice: studies that carefully denoise their channel may be discarding their
  only route to identification. Verified on a controlled construction — and honestly reported as
  **failing** ($F = 0.2$) on the first trained system we didn't build for it, with the mechanism
  diagnosed.

---

## ⚰️ About the old framing (and the old README)

Earlier versions of this repo led with a table of three predictions all marked **✅ Supported**.
That table is gone, and it should be. Here's what was wrong with it:

- The validation ran in a linear-Gaussian simulation that satisfied the theory's assumptions **by
  construction**. For Prediction 3 in particular, a coupling parameter was *imposed* on the
  simulator and then recovered at $r = 1.00$. That demonstrates the estimator inverts the
  generative model. It is a property of the estimator, not evidence for the theory.
- Carried to a learned interface, the same estimator reported a beautiful $r = 0.99$
  bandwidth–coupling law. It was **bias**: a pure-noise control returned 0.71 "bits" where the true
  value was zero. A block-shuffle surrogate correction erased essentially the whole effect.
- And the quantity the whole programme was built on — transfer entropy — is exactly the quantity
  the non-identifiability theorem rules out.

**What survives:** the **dimensional bottleneck theorem** ($C \le \bar{c}\cdot\min(d_i, d_j)$ —
capacity capped by representational geometry, not by the wire). We think it's correct and we don't
withdraw it. It's now **§2** of the paper, stated in full, followed by the account of why the
measurement programme built on top of it doesn't work. The failure is the setup for everything else.

---

## 📂 Repository Structure

```
computational-coupling/
├── README.md                 # You are here
├── opp.md                    # The core idea in prose — START HERE for the why
├── handoff.md                # State of the programme + next steps. Read cold-start.
├── ROADMAP.md                # The old 4-paper plan, kept with a superseded banner
├── Home.md                   # Obsidian dashboard
│
├── paper_main/               # THE PAPER — the single authoritative manuscript
│   ├── main.tex              # LaTeX entry point
│   ├── main.pdf              # Compiled, 36 pp
│   ├── references.bib        # 43 entries, all resolving
│   ├── build.sh              # pdflatex -> bibtex -> pdflatex x2
│   └── README.md             # Section-by-section map
│
├── experiments/
│   ├── paper1_rl/            # The trained speaker-listener, escape attempts, oracle control
│   ├── paper2_identifiability/  # Noise-as-instrument: toy + real-system failure
│   ├── paper2_human_ai/      # Pre-registered human-AI dissociation study
│   ├── paper2_hyperscanning/ # Hyperscanning corpus work
│   └── results/              # Logs, plots, metrics
│
├── literature/               # 40 paper summaries, web scans, BBI throughput survey
├── theory/                   # Formal derivations & proofs
├── damn_sources/             # Primary-source summaries & repo guides
├── study-these/              # Curated onboarding reading pack
├── figures/                  # Figure outputs from run_experiments.py
├── diary/                    # Research journal
├── presentations/            # Decks & explainers
└── datasets/                 # OpenNeuro configs & downloaders
```

---

## 🚀 Quick Start

### 1. Build the paper → PDF
```bash
cd paper_main && ./build.sh      # pdflatex -> bibtex -> pdflatex x2, writes paper_main/main.pdf
```
Needs `texlive-latex-base texlive-latex-recommended texlive-latex-extra
texlive-fonts-recommended`. Builds clean: 36 pp, 0 overfull boxes, 0 undefined references.

### 2. Reproduce the anchor result
```bash
source .venv/bin/activate
cd experiments/paper1_rl/
python3 run_experiments.py         # the superseded simulation + figures
python3 probe_oracle_listener.py   # the infinite-bandwidth control — the decisive one
```

### 3. Reproduce the identifiability demos
```bash
cd experiments/paper2_identifiability/
python3 noise_as_instrument.py         # works: IV recovers each dyad's true effect
python3 noise_as_instrument_stage2.py  # fails honestly: first-stage F = 0.2
```

Everything is seeded and runs on CPU in minutes. No GPU anywhere in this repo.

---

## ❓ Open Questions

The account is complete as an argument and incomplete as a research programme. §12 of the paper
states seven open questions, each posed so both answers are informative. The big ones:

1. **Does the dissociation occur in deployed conversational systems?** Full pre-registered design in
   Appendix C — nobody has run it yet.
2. **Does noise-as-instrument survive real biological channels?** It failed on an optimised discrete
   code. Speech and neural channels aren't trained for threshold reliability, so we expect stronger
   instruments — but that's a prediction, not a result.
3. **Is coupling bistable?** We predict hysteresis: an established convention should survive
   degradation that would have prevented its formation. Untested. If true, cross-sectional
   measurement of coupling capacity is ill-posed.

---

## ✉️ Contact & Collaboration

Written & maintained by **Ashok Pasala** and **Snigdha Gorai** (VIT-AP University).
Questions, suggestions, or want to collaborate on multi-agent RL / neuroimaging experiments? Open
an Issue or a Pull Request.

*Remove the signal, and see what changes.* 🔬

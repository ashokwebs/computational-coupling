# 🎓 Study Guide: Computational Coupling & Interventional BBI

Welcome to the **Computational Coupling** research program! This folder (`study-these/`) contains the complete structured curriculum and reference materials required to understand, contribute to, and extend this project.

---

## 🗺️ Curriculum Reading Path (5-Day Onboarding Plan)

To quickly get up to speed without getting lost in the details, follow this sequence:

### Day 1: Core Paradigm Shift & Vision
1. **[00_START_HERE.md](file:///home/charizard/computational-coupling/study-these/00_START_HERE.md)** (You are here!)
2. **[01_CORE_THEORY.md](file:///home/charizard/computational-coupling/study-these/01_CORE_THEORY.md)** — The big reframe: Why observational coupling fails and why functional coupling is an interventional quantity.
3. **Primary Source Reading**:
   - [`opp.md`](file:///home/charizard/computational-coupling/opp.md) — The core idea and motivation in clear prose.
   - [`handoff.md`](file:///home/charizard/computational-coupling/handoff.md) — Project history, critical lessons, and current state.

### Day 2: Theoretical & Mathematical Foundations
1. **[02_MATHEMATICS_AND_ESTIMATORS.md](file:///home/charizard/computational-coupling/study-these/02_MATHEMATICS_AND_ESTIMATORS.md)** — Formal math: State spaces, Transfer Entropy ($TE$), KSG estimators, and block-shuffle surrogate bias correction (`cl.effective_te`).
2. **Primary Source Drafts**:
   - [`paper_main/main.tex`](file:///home/charizard/computational-coupling/paper_main/main.tex) — **"Understanding Is Not Observable."** The one paper. §2 is the original BBI coupling theory (coupling capacity + the bottleneck theorem) and the account of why its validation does not support it; §§3–8 are the standing argument. Formerly two directories, `paper/` and `paper2/`, merged 2026-08-25.
   - [`theory/definitions.md`](file:///home/charizard/computational-coupling/theory/definitions.md) & [`theory/mathematics.md`](file:///home/charizard/computational-coupling/theory/mathematics.md).

### Day 3: Empirical Testbed & Code Architecture
1. **[04_EMPIRICAL_TESTBED_AND_EXPERIMENTS.md](file:///home/charizard/computational-coupling/study-these/04_EMPIRICAL_TESTBED_AND_EXPERIMENTS.md)** — Code walkthrough: `PettingZoo` RL setup, estimators, and experimental controls.
2. **Codebase Exploration**:
   - [`experiments/paper1_rl/coupling_lab.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/coupling_lab.py) — The core library for information-theoretic estimators and dynamical systems.
   - [`experiments/paper1_rl/TODO.md`](file:///home/charizard/computational-coupling/experiments/paper1_rl/TODO.md) — Authoritative experimental log detailing settled negatives and controls.

### Day 4: Literature Canon
1. **[03_LITERATURE_CANON.md](file:///home/charizard/computational-coupling/study-these/03_LITERATURE_CANON.md)** — Systematic breakdown of 40 essential papers across BBI, Multi-Agent Communication, Information Theory, Hyperscanning, and Neural Manifolds.
2. **External Reading List**:
   - [`tosee.md`](file:///home/charizard/computational-coupling/tosee.md) — Verified list of frontier alignment & decoding papers.
   - Key summaries in [`literature/summaries/`](file:///home/charizard/computational-coupling/literature/summaries/).

### Day 5: Reproduction & Hands-On
1. **Environment Setup**: Read [`DEVELOPMENT.md`](file:///home/charizard/computational-coupling/DEVELOPMENT.md) & activate `.venv`.
2. **Run Proof-of-Concept & Controls**:
   ```bash
   cd experiments/paper1_rl
   python3 run_experiments.py
   python3 probe_oracle_listener.py
   python3 diagnose_channel_usage.py
   ```
3. **Compile Papers**:
   ```bash
   cd paper_main && ./build.sh
   ```

---

## 💡 Quick Overview of the Project

### The Problem
Traditional Brain-Computer Interfaces (BCI), Brain-to-Brain Interfaces (BBI), and EEG/fMRI hyperscanning assume that communication can be measured observationally via correlation, Transfer Entropy, or Granger Causality. 

### The Reframe
1. **Understanding Is Not Observable**: Observational metrics confound true functional coupling with shared prior conventions or external task drivers.
2. **Interventional Identification**: Functional coupling requires measuring how a receiver's behavior changes when the sender's signals are interventionally manipulated (e.g., via randomization or noise injection).
3. **Coupling Capacity Limit**: Coupling capacity saturates at the smaller system's effective internal representational dimensionality, NOT at raw channel bandwidth.

---

## 📂 Index of Study Files in `study-these/`

- **[00_START_HERE.md](file:///home/charizard/computational-coupling/study-these/00_START_HERE.md)**: Onboarding guide and study roadmap.
- **[01_CORE_THEORY.md](file:///home/charizard/computational-coupling/study-these/01_CORE_THEORY.md)**: Conceptual & theoretical foundations.
- **[02_MATHEMATICS_AND_ESTIMATORS.md](file:///home/charizard/computational-coupling/study-these/02_MATHEMATICS_AND_ESTIMATORS.md)**: Mathematics, Transfer Entropy & bias correction.
- **[03_LITERATURE_CANON.md](file:///home/charizard/computational-coupling/study-these/03_LITERATURE_CANON.md)**: Literature review and 40-paper canon map.
- **[04_EMPIRICAL_TESTBED_AND_EXPERIMENTS.md](file:///home/charizard/computational-coupling/study-these/04_EMPIRICAL_TESTBED_AND_EXPERIMENTS.md)**: Code guide, experiment suite, and key findings.
- **[05_ESSENTIAL_READINGS/](file:///home/charizard/computational-coupling/study-these/05_ESSENTIAL_READINGS/)**: Direct copies/links of key primary research notes and manifests.

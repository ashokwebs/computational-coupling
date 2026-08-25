# 🤝 Contributing to the Computational Coupling Lab

Awesome! You wanna join this research program? We are super hyped to have you here! 🎉

Whether you're a math wizard deriving transfer entropy bounds, a neuro-geek hacking on EEG datasets, or a PyTorch multi-agent RL dev, here is how you can jump in.

---

## 📜 Principles & Mindset

1. **Rigor over Hype:** We dont do hand-wavy claims about "telepathy" or "brain languages". Everything we propose must be grounded in information theory, causal inference, dynamical systems, or formal ML.
2. **Say what's proven and what isn't:** This repo has one standing rule that outranks everything else — never let a hypothesis and a result blur, *especially* when the hypothesis is the exciting one. We retracted our own headline validation for breaking this rule (see `paper_main/` §2.3). Null and inconclusive results get reported as null and inconclusive.
3. **Humane & Fast Code:** Code should be clean, readable, and fun to hack on! Use clear variable names, add docstrings, and feel free to leave enthusiastic notes in PRs.
4. **Reproducibility is King:** If you add an experiment script, include a fixed random seed parameter, a sample config file, and clear instructions on how to reproduce your plots.

---

## 🛠️ How to Contribute

### 1. Theory & LaTeX Paper (`paper_main/`)
- There is exactly **one** paper: `paper_main/main.tex`. Edit it directly — it is a single file, not modular sections.
- Add references to `paper_main/references.bib` with proper BibTeX formatting and valid DOIs/arXiv IDs.
- Run `cd paper_main && ./build.sh` before submitting. It must report **0 overfull** and **0 undefined**; PRs that regress either will be asked to fix it first.
- If you change a claim, change the claim's evidence in the same PR — or mark it explicitly as unsupported. See the honesty principle below.

### 2. Literature Summaries (`literature/`)
- Found a paper related to BBI, optimal transport (FUGW), hyperscanning, or emergent MARL?
- Add a summary in `literature/summaries/YYYY_Author_Topic.md`.
- Update the master database table in `literature/literature_review.md`.

### 3. Empirical Code (`experiments/`)
- **Paper 1 (Multi-Agent RL):** Work inside `experiments/paper1_rl/`.
- Ensure environment wrappers inherit from standard Gym/PettingZoo APIs.
- Log metrics (loss, transfer entropy, bandwidth, epoch) to JSON log files or TensorBoard.

---

## 🔀 Git Workflow & Branch Naming

We use clean branch names:
- `feature/paper1-gumbel-bottleneck`
- `theory/capacity-bandwidth-proof`
- `lit/add-mindeye2-summary`
- `fix/latex-bibliography-keys`

PRs should include a short note on what you changed and why!

Let's build groundbreaking science together! 🚀

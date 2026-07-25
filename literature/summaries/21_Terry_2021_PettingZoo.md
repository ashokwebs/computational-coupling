---
tags: [#literature/paper, #paper/extended-canon]
alias: "21_Terry_2021_PettingZoo"
---

# Research Paper Report: PettingZoo: Gym for Multi-Agent Reinforcement Learning

**Authors:** J. K. Terry, Benjamin Black, Nathaniel Grammel, Mario Jayakumar, Ananth Hari, Ryan Sullivan, Luis S. Santos, Clemens Dieffendahl, Caroline Horsch, Rodrigo Perez-Vicente, Niall Williams, Yashas Lokesh, Praveen Ravi
**Publication Year:** 2021
**Venue:** *Advances in Neural Information Processing Systems (NeurIPS)*, 34
**DOI/arXiv:** `arXiv:2009.14471`
**Category:** (2) Emergent multi-agent communication beyond DIAL / infrastructure
**Role in Our Work:** **Direct technical dependency, not a threat.** This is the software library our Stage 2 experiment is literally built on.

---

## 📌 Abstract & Architecture
Presents PettingZoo, a standardized Python API for multi-agent reinforcement learning environments (including the Multi-Agent Particle Environments, MPE, e.g. `simple_speaker_listener`), built around the Agent-Environment-Cycle (AEC) game model rather than the traditional simultaneous-move Markov game model. Designed to do for MARL what Gym did for single-agent RL: make environments interchangeable, reproducible, and easy to wrap with arbitrary interface/observation/action constraints.

## 🔗 Connection to Computational Coupling Theory
This is the technical reference for the exact library named in `ROADMAP.md` Stage 2 and `experiments/paper1_rl/TODO.md` ("`PettingZoo simple_speaker_listener` wrapper (PyTorch)"). It should be cited in the Methods/Experiments section of Paper 1 wherever the Stage 2 learned-interface pipeline is described, both for reproducibility and because the AEC formalism (turn-based/cyclic agent-environment interaction with explicit observation/action interfaces) is a convenient substrate for imposing our bandwidth-$B$-constrained interface layer between the speaker and listener agents.

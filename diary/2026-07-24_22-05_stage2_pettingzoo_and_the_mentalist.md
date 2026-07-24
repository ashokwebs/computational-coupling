---
tags: [#diary/entry, #research-log, #paper1/rl, #the-mentalist]
alias: "2026-07-24_22-05_stage2_pettingzoo_and_the_mentalist"
---

# Diary Entry — July 24, 2026 (10:05 PM)
**Location:** VIT-AP Hostel Room (Night shift, cold coffee ☕, terminal running PyTorch)
**Mood:** Fired up ⚡ & lowkey wanting to rewatch *The Mentalist* 🕵️‍♂️
**Status:** Day 6 — Stage 1 Complete (v0.3.0) → Stage 2 (Learned Deep RL & PettingZoo).

---

### From Analytical Sandbox to Deep Reinforcement Learning 🤖

Last night was wild: our linear VAR sandbox (`coupling_lab.py`) proved that Coupling Capacity $C_{\text{couple}}$ saturates at $0.39 \times \min(d_{\text{eff}})$, flat in channel bandwidth $B$. That gave us the formal **Dimensional Bottleneck Theorem**.

Today was all about shifting gears to Stage 2:
> *"What happens when agents LEARN their communication protocol end-to-end via gradient descent in a multi-agent RL environment?"*

We set up the `PettingZoo simple_speaker_listener` environment with a differentiable Gumbel-Softmax channel bottleneck to sweep discrete channel capacity ($B \in [1, 2, 4, 8, 16, 32]$ bits/step). We're testing whether neural networks optimize their code to hit the theoretical dimensional ceiling or if non-linear representations change the bound.

---

### Late-Night Thoughts: Cold Readings & Patrick Jane 🕵️‍♂️

While waiting for the PyTorch training loop to warm up, my mind wandered off. I'm honestly thinking about winding down tonight by watching an episode or two of ***The Mentalist***. 📺

It's hilarious thinking about it through the lens of computational coupling:
- Patrick Jane's "cold reading" is basically high-throughput neural state estimation!
- He's measuring coupling capacity between human body language and internal mental states, exploiting tiny non-verbal micro-expressions to reconstruct the hidden state of a suspect.
- In our paper's language: Jane has built a high-precision internal world model $M$, driving his predictive gain $\mathcal{L}_{\text{self}} - \mathcal{L}_{\text{joint}}$ through the roof! 😂

---

### Plan for Tomorrow 🎯

1. Run full Gumbel-Softmax bandwidth sweeps across 10 random seeds on the cluster.
2. Log task success reward alongside measured mutual information $I(S_t; R_{t+1} \mid R_t)$.
3. Data pipeline check for OpenNeuro `ds007764` DUET EEG hyperscanning dataset.

Now... time to launch the training run and hit play on *The Mentalist*! 🍿

Signing off — Day 6! ✌️

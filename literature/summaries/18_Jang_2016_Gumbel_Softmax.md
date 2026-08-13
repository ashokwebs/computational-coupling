---
tags: ["#literature/paper", "#paper/extended-canon"]
alias: "18_Jang_2016_Gumbel_Softmax"
---

# Research Paper Report: Categorical Reparameterization with Gumbel-Softmax

**Authors:** Eric Jang, Shixiang Gu, Ben Poole
**Publication Year:** 2016 (ICLR 2017)
**Venue:** *International Conference on Learning Representations (ICLR)*
**DOI/arXiv:** `arXiv:1611.01144`
**Category:** (2) Emergent multi-agent communication beyond DIAL
**Role in Our Work:** **Direct methodological dependency, not a threat.** This is the exact reparameterization trick specified in our own Stage 2 roadmap.

---

## 📌 Abstract & Architecture
Introduces the Gumbel-Softmax (Concrete) distribution: a continuous relaxation of categorical/discrete sampling that admits a low-variance, fully differentiable reparameterization via the Gumbel-max trick plus a temperature-controlled softmax. As temperature $\tau \to 0$, samples approach one-hot categorical draws; at higher $\tau$ the distribution is smooth and gradients flow cleanly through backprop, avoiding the high-variance REINFORCE/score-function estimator previously required for discrete latents. Shown to outperform prior discrete-gradient estimators on structured prediction and semi-supervised classification.

## 🔗 Connection to Computational Coupling Theory
This is not background reading — it is the literal mechanism named in `experiments/paper1_rl/TODO.md` and `ROADMAP.md` for Stage 2 ("learned Gumbel-Softmax discrete channel bottleneck, sweep $B \in \{1,2,4,8,16,32\}$"). The Gumbel-Softmax channel is how we impose a genuinely *learned, optimized* bandwidth-$B$ interface (as opposed to Stage 1's hand-set NumPy interface) while keeping the whole pipeline end-to-end differentiable for policy-gradient training. Citing this paper anchors the claim that Stage 2's saturation law is observed under an interface the agents actually optimize, not one we imposed by fiat — directly testing whether Prediction 1 (capacity saturates at effective dimension, not raw $B$) survives when the encoder itself is free to try to use all of $B$.

---
tags: [#literature/paper, #paper/extended-canon]
alias: "17_Sukhbaatar_2016_CommNet"
---

# Research Paper Report: Learning Multiagent Communication with Backpropagation (CommNet)

**Authors:** Sainbayar Sukhbaatar, Arthur Szlam, Rob Fergus
**Publication Year:** 2016
**Venue:** *Advances in Neural Information Processing Systems (NeurIPS)*, 29
**DOI/arXiv:** `arXiv:1605.07736`
**Category:** (2) Emergent multi-agent communication beyond DIAL
**Role in Our Work:** **Complementary, not a threat.** Predates and technically parallels Foerster's DIAL (already canon #4); provides an alternative continuous-message architecture.

---

## 📌 Abstract & Architecture
Introduces CommNet, a single large feed-forward network in which each agent's hidden state is broadcast to all others and the *average* of received messages is fed back in as a differentiable communication channel, trained end-to-end with plain backpropagation (no explicit protocol design or discrete symbol vocabulary). Demonstrated on tasks like traffic-junction coordination and combat games, agents learn cooperative signaling purely from task reward and gradient flow through the continuous channel, and the learned messages are shown to be interpretable in simple cases.

## 🔗 Connection to Computational Coupling Theory
CommNet is the *continuous-channel* counterpart to DIAL's discrete/CRIAL split (already in canon). It matters for us because it is one of the earliest demonstrations that an unconstrained, unbounded-bandwidth communication channel between agents will not spontaneously bottleneck itself — CommNet's messages are full continuous vectors, i.e. $B \to \infty$. This sharpens the motivation for our Stage 2 experiment: we deliberately impose a hard bandwidth constraint (`PettingZoo` + Gumbel-Softmax discrete channel, see `18_Jang` and `21_Terry`) precisely because architectures like CommNet, left alone, do not reveal a capacity-saturation law — they simply use as many bits as are available. CommNet is useful primarily as the historical "no-bottleneck" control condition our bandwidth-swept experiments are implicitly contrasted against.

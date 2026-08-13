---
tags: [#theory/definitions, #math/manifolds]
alias: "Theory Definitions"
---

# 📐 Formal Definitions: Theory of Computational Coupling

**Authors:** Ashok Pasala, Snigdha Gorai (VIT-AP University)  
**Status:** Canonical Theoretical Definitions (Version 0.2.0)  

---

## Definition 1: System State Space & Trajectory

Yo! Let a system $S_i$ (biological neural network or artificial agent) be characterized by a continuous state space $\mathcal{M}_i$, representing a high-dimensional manifold embedded in $\mathbb{R}^{d_i}$. 

The internal state of $S_i$ evolves over time $t \in \mathbb{R}^+$ as a continuous state trajectory:
$$x_i(t) \in \mathcal{M}_i$$

We do **NOT** assume that state spaces $\mathcal{M}_i$ and $\mathcal{M}_j$ share identical dimensionality ($d_i \neq d_j$), coordinate systems, or anatomical topology — a direct departure from hyperalignment-based approaches that presuppose a common representational geometry!

---

## Definition 2: Self-Predictive World Model

System $S_i$ possesses an internal self-predictive model $P_i$ that estimates its own future trajectory given its own history:
$$P_i(x_i(t+\Delta) \mid x_i(\le t))$$

The log-likelihood of this model quantifies $S_i$'s **Self-Predictive Accuracy** ($R_i$):
$$R_i = \mathbb{E} \left[ \log P_i(x_i(t+\Delta) \mid x_i(\le t)) \right]$$

---

## Definition 3: Bandwidth-Constrained Interface Map

An **interface map** $g_{i \to j}$ from system $i$ to system $j$ is a parameterized map:
$$g_{i \to j} : x_i(\le t) \;\longmapsto\; s_{i \to j}(t)$$

producing an exogenous signal $s_{i \to j}(t)$ transmitted across a channel subject to a constraint budget $\mathcal{A}(B)$ (e.g. scalar bandwidth $B$ bits/sec, discrete vocabulary size $K$, or stimulation frequency limits).

---

## Definition 4: Directed Coupling (Transfer Entropy)

The **directed coupling** from system $i$ to system $j$ under interface $g \in \mathcal{A}(B)$ at transmission lag $\Delta$ is defined as the Transfer Entropy (Directed Information):
$$\mathrm{TE}_{i \to j}(\Delta; g) = I\big(x_i(t) \,;\, x_j(t+\Delta) \mid x_j(\le t)\big)$$

$$\mathrm{TE}_{i \to j}(\Delta; g) = H\big(x_j(t+\Delta) \mid x_j(\le t)\big) - H\big(x_j(t+\Delta) \mid x_j(\le t), x_i(\le t)\big)$$

---

## Definition 5: Coupling Capacity ($C_{\text{couple}}$)

The **Coupling Capacity** $C(i \to j)$ from system $i$ to system $j$ under bandwidth constraint $B$ is the supremum of directed coupling over all admissible interface designs:
$$C(i \to j; B) \triangleq \sup_{g \in \mathcal{A}(B)} \mathrm{TE}_{i \to j}(\Delta; g)$$

*Bro... here is the intuition:* Coupling Capacity is the dynamic analogue of Shannon Channel Capacity. Where Shannon capacity maximizes mutual information over input distributions for a static channel, Coupling Capacity maximizes directed information over interface maps for dynamic coupled systems!

---
tags: ["#meta/moc", "#theory"]
alias: "Theory Map of Content"
---

# 📐 Map of Content: Theoretical Foundations

> [!abstract] **Overview**
> This MOC aggregates all mathematical formulations, state-space definitions, transfer entropy estimators, capacity saturation proofs, and open theoretical questions.

---

## 📑 Core Theory Note Vault

1. 📘 **[[theory/definitions|State Spaces, Interfaces, and Coupling Capacity]]**
   - Manifold state trajectories $x(t) \in \mathcal{M}_X, y(t) \in \mathcal{M}_Y$.
   - Bandwidth-constrained interface maps $g: \mathcal{M}_X \to \mathcal{M}_Y$.
   - Formal definition of Coupling Capacity $C(X \to Y) \triangleq \sup_{g \in \mathcal{A}(B)} \mathrm{TE}_{X \to Y}^g$.
   - Asymmetry Index $A \in [-1, 1]$.

2. 🧮 **[[theory/mathematics|Transfer Entropy Estimators & Neural Predictive Gain]]**
   - Kraskov-Stögbauer-Grassberger (KSG) $k$-NN transfer entropy estimator.
   - Effective Transfer Entropy (ETE) via Fourier surrogate shuffling.
   - Deep Neural Predictive-Gain Estimator: $\hat{\mathrm{TE}}_{A \to B} = L_{\text{self}} - L_{\text{joint}}$.

3. ⚖️ **[[theory/proofs|Capacity-Bandwidth Saturation Law Proof]]**
   - Formal proof sketch that $C(A \to B; B)$ flattens concavely, bounded by $\min(\dim_{\text{eff}}(\mathcal{M}_A), \dim_{\text{eff}}(\mathcal{M}_B))$.

4. 📌 **[[theory/assumptions|Theoretical Assumptions & Scope Constraints]]**
   - Manifold smoothness, ergodicity, non-stationarity windowing, Rate-Distortion constraints.

5. ❓ **[[theory/open_questions|Open Theoretical Questions]]**
   - Sample complexity of KSG estimators in $d > 100$.
   - Non-isomorphic topological mapping under entropic regularization.

---

> [!tip] **Return to Dashboard:** [[Home|Master Home Dashboard]]

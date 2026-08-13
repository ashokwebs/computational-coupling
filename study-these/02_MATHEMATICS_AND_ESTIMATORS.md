# 📐 Mathematics, Transfer Entropy & Estimators

This document details the mathematical framework, definitions, transfer entropy estimators, and bias-correction techniques used throughout the project.

---

## 1. Formal Mathematical Definitions

### State Spaces & Internal Manifolds
Consider two intelligent dynamical systems $S_i$ and $S_j$.
- Let $x_t^{(i)} \in \mathcal{M}_i \subset \mathbb{R}^{d_i}$ denote the state vector of system $i$ on a low-dimensional Riemannian manifold $\mathcal{M}_i$ of effective dimension $d_{\text{eff}}(i)$.
- Let $x_t^{(j)} \in \mathcal{M}_j \subset \mathbb{R}^{d_j}$ denote the state vector of system $j$.

### Interface Maps & Bandwidth Constraint
An interface map $g: \mathcal{M}_i \to \mathcal{C}$ maps internal states to channel signals across a constrained channel $\mathcal{C}$ with bandwidth $B$ bits/sec:
$$\text{dim}(\mathcal{C}) \le B, \quad \text{or} \quad I(X^{(i)}; M) \le B$$

### Transfer Entropy (Schreiber, 2000)
Transfer Entropy $TE_{i \to j}(\Delta)$ measures the reduction in uncertainty of $x_{t+\Delta}^{(j)}$ given past states $x_{1:t}^{(i)}$ beyond what is predicted by system $j$'s own history $x_{1:t}^{(j)}$:
$$\mathrm{TE}_{i \to j}(\Delta) = H\left(x_{t+\Delta}^{(j)} \mid x_{1:t}^{(j)}\right) - H\left(x_{t+\Delta}^{(j)} \mid x_{1:t}^{(j)}, x_{1:t}^{(i)}\right)$$

In terms of Kullback-Leibler divergence:
$$\mathrm{TE}_{i \to j}(\Delta) = D_{\mathrm{KL}}\left( P\left(x_{t+\Delta}^{(j)} \mid x_{1:t}^{(j)}, x_{1:t}^{(i)}\right) \parallel P\left(x_{t+\Delta}^{(j)} \mid x_{1:t}^{(j)}\right) \right)$$

---

## 2. Transfer Entropy Estimators in `coupling_lab.py`

In practice, estimating $TE$ from finite time series requires specific statistical estimators. We implement two complementary estimators in [`experiments/paper1_rl/coupling_lab.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/coupling_lab.py):

### 1. Parametric Predictive Gain Estimator (`predictive_gain_te`)
Assumes Gaussian residual errors for internal predictive models:
$$\mathrm{TE}_{\text{pred}} = \frac{1}{2} \log \frac{\sigma^2_{\text{unconditioned}}}{\sigma^2_{\text{conditioned}}}$$
- **Pros**: Extremely fast to compute ($O(N)$ linear regression / Ridge).
- **Cons**: Subject to sample-size-to-dimension ratio bias when channel dimension is large.

### 2. Model-Free KSG $k$-NN Estimator (`ksg_te`)
Kraskov-Stögbauer-Grassberger (KSG) non-parametric mutual information estimator based on $k$-nearest neighbors in joint space:
$$\mathrm{TE}_{\text{KSG}} = \psi(k) + \langle \psi(n_x + 1) + \psi(n_y + 1) - \psi(n_z + 1) \rangle$$
- **Pros**: Non-parametric; captures arbitrary non-linear dependencies.
- **Cons**: Computationally expensive ($O(N \log N)$ or $O(N^2)$).

---

## 3. The Estimator Bias Trap & Effective TE (`cl.effective_te`)

### The 0.71 Bits Noise Floor Lesson
In finite sample regimes ($N < 1000$), unconditioned regression models overfit higher-dimensional channel inputs $M$. In early experiments, raw `predictive_gain_te` returned **0.71 bits of transfer entropy on pure independent Gaussian noise**!

### Block-Shuffle Surrogate Correction
To eliminate estimator bias, we compute **Effective Transfer Entropy**:
$$\mathrm{TE}_{\text{effective}} = \mathrm{TE}_{\text{raw}} - \frac{1}{S} \sum_{s=1}^{S} \mathrm{TE}_{\text{shuffled}}^{(s)}$$

Where $\mathrm{TE}_{\text{shuffled}}$ breaks temporal alignment between system $i$ and system $j$ via block-shuffling episodes while preserving single-system autocorrelation.

```python
# In coupling_lab.py
def effective_te(x_source, y_target, estimator_fn, num_shuffles=20):
    raw_te = estimator_fn(x_source, y_target)
    surrogate_tes = []
    for _ in range(num_shuffles):
        x_shuffled = block_shuffle(x_source)
        surrogate_tes.append(estimator_fn(x_shuffled, y_target))
    return raw_te - np.mean(surrogate_tes)
```

---

## 4. Analytical Proof Sketch: Capacity-Bandwidth Saturation

### Theorem (Saturation Limit)
Let system $j$ have effective state dimension $d_j = \text{dim}_{\text{eff}}(\mathcal{M}_j)$. Under linear-Gaussian dynamics, as bandwidth $B \to \infty$:
$$\lim_{B \to \infty} C(i \to j; B) = \frac{1}{2} \sum_{k=1}^{d_j} \log(1 + \lambda_k)$$
where $\lambda_k$ are the eigenvalues of the state covariance matrix projected onto the receiver's controllable subspace.

*Proof Intuition*: The receiver system $j$ possesses a finite-dimensional state space $\mathcal{M}_j$. Any incoming channel information that projects orthogonal to system $j$'s controllable manifold cannot alter system $j$'s state trajectory. Thus, coupling capacity is bounded above by $\text{dim}_{\text{eff}}(\mathcal{M}_j)$ regardless of how large $B$ becomes.

---

## 📖 Key Code Implementation
- [`experiments/paper1_rl/coupling_lab.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/coupling_lab.py) — Core implementations of `predictive_gain_te`, `ksg_te`, `effective_te`, and synthetic dynamical systems.
- [`theory/mathematics.md`](file:///home/charizard/computational-coupling/theory/mathematics.md) — Detailed mathematical derivations.
- [`theory/proofs.md`](file:///home/charizard/computational-coupling/theory/proofs.md) — Formal saturation proofs.

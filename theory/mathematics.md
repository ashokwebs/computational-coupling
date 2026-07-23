---
tags: [#theory/mathematics, #math/estimators]
alias: "Transfer Entropy Math"
---

# 🧮 Mathematical Derivations & Estimators

Bro, calculating $\mathrm{TE}_{X \to Y}$ in real continuous time-series without assuming linear Gaussian distributions is tricky becuase brain signals are non-linear as fuck. Here are our two estimators:

---

## 1. Non-Parametric KSG Transfer Entropy Estimator

For continuous trajectories $x_t \in \mathcal{M}_A$ and $y_t \in \mathcal{M}_B$, fixed spatial binning fails in high dimensions.

We utilize the Kraskov-Stögbauer-Grassberger (KSG) k-nearest neighbor estimator.

Let $z(t) = (y_{t+\Delta}, y_{t-\tau:t}, x_{t-\tau:t})$ be the joint vector in embedding space $\mathbb{R}^{d_y + d_y + d_x}$.

For each point $i$, find the distance $\epsilon_i/2$ to its $k$-th nearest neighbor in joint space using supremum norm ($L_\infty$). Count the number of points within distance $\epsilon_i/2$ in marginal subspaces:
- $n_y(i)$: count in $(y_{t+\Delta}, y_{t-\tau:t})$ subspace
- $n_{y,\text{past}}(i)$: count in $y_{t-\tau:t}$ subspace
- $n_{x,y,\text{past}}(i)$: count in $(y_{t-\tau:t}, x_{t-\tau:t})$ subspace

The KSG Transfer Entropy estimate is:
$$\hat{\mathrm{TE}}_{X \to Y} = \psi(k) + \langle \psi(n_{y,\text{past}} + 1) - \psi(n_y + 1) - \psi(n_{x,y,\text{past}} + 1) \rangle$$

where $\psi(x)$ is the digamma function $\psi(x) = \frac{d}{dx} \ln \Gamma(x)$ and $\langle \cdot \rangle$ denotes averaging over sample time steps $N$.

---

## 2. Deep Neural Predictive-Gain Estimator

In high dimensions ($d > 50$), k-NN distances fall victim to the curse of dimensionality!

So we derive a parametric neural predictive-gain estimator:

1. **Self-Predictor Model ($\phi$):** Train a recurrent model (LSTM/Transformer) to minimize negative log-likelihood of $y_{t+\Delta}$ given $y_{\le t}$:
   $$L_{\text{self}}(\phi) = -\frac{1}{N} \sum_{t=1}^N \log P_\phi(y_{t+\Delta} \mid y_{\le t})$$

2. **Joint-Predictor Model ($\psi$):** Train a joint model taking both past trajectories $y_{\le t}$ and exogenous signals $x_{\le t}$:
   $$L_{\text{joint}}(\psi) = -\frac{1}{N} \sum_{t=1}^N \log P_\psi(y_{t+\Delta} \mid y_{\le t}, x_{\le t})$$

3. **Predictive Gain:**
   $$\hat{\mathrm{TE}}_{X \to Y}^{\text{pred}} = L_{\text{self}}(\phi^*) - L_{\text{joint}}(\psi^*)$$

By Jensen's inequality, if $P_\psi$ subsumes $P_\phi$, $L_{\text{self}} \ge L_{\text{joint}}$, guaranteeing $\hat{\mathrm{TE}} \ge 0$.

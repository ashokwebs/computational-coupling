# 🔍 Underlying Theoretical Assumptions

To be 100% transparent and clear, here are the explicit assumptions under which our theory holds:

1. **State Trajectory Smoothness:** Internal states $x_i(t)$ evolve along Riemannian manifolds $\mathcal{M}_i$ with continuous derivatives (no random teleportation in state space!).
2. **Markovian History Depth:** Systems possess finite effective memory depth $\tau < \infty$ such that state trajectories $x_i(\le t)$ are well-approximated by window $x_i(t-\tau:t)$.
3. **Ergodicity & Stationary Statistics:** Conditional distributions $P(x_j(t+\Delta) \mid x_j(\le t), x_i(\le t))$ are locally stationary over estimation windows $T \gg \tau$.
4. **Interface Admissibility:** Admissible interfaces $\mathcal{A}(B)$ are bounded by physical constraints (energy, bandwidth $B$, stimulation limits).

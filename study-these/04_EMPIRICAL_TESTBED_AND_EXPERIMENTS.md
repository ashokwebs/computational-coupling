# 🧪 Empirical Testbed, Codebase & Experiments

This document provides a technical walkthrough of the experimental codebase located in [`experiments/paper1_rl/`](file:///home/charizard/computational-coupling/experiments/paper1_rl/).

---

## 1. Directory & Code Map

| File | Primary Function | Key Output / Metric |
|:---|:---|:---|
| [`coupling_lab.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/coupling_lab.py) | Core coupling estimation library & synthetic dynamical systems | `predictive_gain_te`, `ksg_te`, `effective_te` |
| [`gumbel_channel.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/gumbel_channel.py) | Differentiable bandwidth-limited communication channel | Quantized / rate-limited vectors |
| [`policies.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/policies.py) | Speaker & listener neural network policy architectures | Actions, messages, hidden latents |
| [`run_experiments.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/run_experiments.py) | Anchor experiment script for synthetic validation | Figures in `figures/`, logs in `results/logs/` |
| [`train_with_aux_loss.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/train_with_aux_loss.py) | Solves speaker encoding via auxiliary prediction loss | $R^2: 0.001 \rightarrow 0.90$ ($aux\_coef=200$) |
| [`train_with_receiver_aux.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/train_with_receiver_aux.py) | Listener representation probe (Proposition 1) | Reconstructs goal ($err=0.0017$) while policy ignores signal |
| [`probe_oracle_listener.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/probe_oracle_listener.py) | **The Oracle Control** — Gives goal directly without channel | Landed on goal-blind reward ($-15.96$ vs $-16.88$ blind vs $-8.78$ expert) |
| [`diagnose_channel_usage.py`](file:///home/charizard/computational-coupling/experiments/paper1_rl/diagnose_channel_usage.py) | Interventional message randomization (`rollout_with_message_source()`) | Sensitivity $z = 1.82$; Value of Information captured $\le 12\%$ |
| [`TODO.md`](file:///home/charizard/computational-coupling/experiments/paper1_rl/TODO.md) | **Authoritative experimental log** | Settled negatives & hyperparameter sweeps |

---

## 2. Walkthrough of Key Diagnostic Experiments

### Experiment 1: The Estimator Bias Control
- **Problem**: Raw $TE$ overfits when channel dimension increases relative to sample size.
- **Verification**: Run `coupling_lab.py` with pure independent Gaussian noise.
- **Result**: Raw linear regression $TE$ returns $0.71$ fake bits. `cl.effective_te` (block-shuffle surrogate) returns $0.00 \pm 0.01$ bits.
- **Rule**: Always use `cl.effective_te` with $\ge 150$ eval episodes.

### Experiment 2: Fixing Speaker Encoding (`train_with_aux_loss.py`)
- **Problem**: In multi-agent RL (PettingZoo simple reference/speaker-listener), the speaker policy gradient gradient suffers from credit assignment dilution. $R^2$ of message vs. speaker goal was $0.001$.
- **Fix**: Add supervised auxiliary loss to the speaker:
  $$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{RL}} + \alpha \cdot \mathcal{L}_{\text{aux}}$$
- **Scale Mismatch Trap**: PyTorch `reduction="sum"` vs `"mean"` scale mismatch caused $\alpha = 1.0$ to have no effect. Raising $\alpha = 200.0$ resulted in $R^2 \ge 0.90$.

### Experiment 3: Listener Representation vs. Policy (Proposition 1) (`train_with_receiver_aux.py`)
- **Question**: Does the listener ignore the message because it can't decode it, or because RL failed to wire the representation to action logits?
- **Finding**: Giving the listener an auxiliary head achieved reconstruction loss of $0.0017$. The information was **provably present and linearly decodable** inside the listener's hidden layer, yet action logits remained identical to goal-blind policies.

### Experiment 4: The Oracle Control (`probe_oracle_listener.py`)
- **Experiment**: Remove the communication channel entirely and concatenate the target goal directly into the listener's state vector.
- **Result**: Listener performance stayed at $-15.96$ (goal-blind baseline is $-16.88$, expert is $-8.78$).
- **Conclusion**: The listener's failure to utilize the speaker's signal was not caused by channel bandwidth, encoding noise, or lossy bottleneck — it was a fundamental RL optimization landscape collapse into a local goal-blind heuristic.

### Experiment 5: Interventional Message Randomization (`diagnose_channel_usage.py`)
- **Method**: `rollout_with_message_source()` feeds the listener real, in-distribution messages generated from a *different, mismatched episode*.
- **Results**:
  - Normal message: $-15.87$
  - Zero-ablated message: $-16.45$ ($z = +0.50$)
  - **Randomized message**: $-18.19$ ($z = +1.82$)
- **Key Takeaways**:
  1. Randomization is $\sim 3\times$ more sensitive than zero-ablation. Never accept a null zero-ablation test as proof of zero coupling!
  2. Captured Share of Value of Information: Even with residual sensitivity, the policy captures $\le 12\%$ of the total available information value.

---

## 3. How to Run the Experiments

```bash
# Activate python virtual environment
source .venv/bin/activate

# 1. Run core synthetic proof-of-concept (P1, P2, P3 sweeps + KSG cross-check)
cd experiments/paper1_rl
python3 run_experiments.py

# 2. Run the oracle control
python3 probe_oracle_listener.py

# 3. Run interventional message randomization
python3 diagnose_channel_usage.py
```

---

## 📖 Key Log Reference
Always check [`experiments/paper1_rl/TODO.md`](file:///home/charizard/computational-coupling/experiments/paper1_rl/TODO.md) before attempting new hyperparameter tuning — all settled negatives (learning rate tuning, batching, entropy coefficients, detached value baselines) are exhaustively documented there.

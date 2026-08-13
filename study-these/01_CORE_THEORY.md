# 🔬 Core Theory & Paradigm Shift

This document provides a thorough theoretical breakdown of the **Computational Coupling** framework. Anyone working on this codebase must understand both the original measurement theory (`paper/`) and the evolved interventional framing (`paper2/`).

---

## 1. The Core Idea: Predictive Entanglement vs. Transmission

### The Traditional BCI / BBI View
Historically, Brain-Computer Interfaces (BCI) and Brain-to-Brain Interfaces (BBI) treat communication as the transmission of static, pre-encoded discrete messages across a channel (like sending ASCII over TCP/IP). They attempt to build "brain dictionaries" or "brain languages".

### The Computational Coupling Reframe
Communication between two intelligent systems is **NOT** static message transmission. Instead:
> **Communication is the degree to which internal state trajectories of two dynamical systems become predictively entangled through a bandwidth-limited interface.**

Mathematically, instead of optimizing Shannon mutual information over fixed codebooks, we define **Coupling Capacity** ($C_{\text{couple}}$) as the supremum of directed information / transfer entropy over allowable interface maps $g \in \mathcal{A}(B)$:
$$C(i \to j) \triangleq \sup_{g \in \mathcal{A}(B)} \mathrm{TE}_{i \to j}(\Delta; g)$$

---

## 2. The Original 3 Falsifiable Predictions (`paper/`)

1. **Prediction 1: Capacity–Bandwidth Saturation Law**
   As channel bandwidth $B$ increases, coupling capacity $C(i \to j; B)$ increases concavely and saturates **NOT** at raw channel capacity, but at the smaller of the two systems' effective internal representational dimensionality:
   $$\lim_{B \to \infty} C(i \to j; B) \propto \min(\dim_{\text{eff}}(\mathcal{M}_i), \dim_{\text{eff}}(\mathcal{M}_j))$$
   *Takeaway for BBI Engineering*: Past a critical bandwidth, widening the channel buys zero additional coupling. You must expand the receiver's usable internal dimensionality instead.

2. **Prediction 2: Self-Predictive Accuracy Governs Capacity Efficiency**
   Systems with better internal world models (higher self-predictive accuracy $R$) extract more coupling capacity per unit of channel bandwidth ($C/B$).

3. **Prediction 3: Asymmetry Tracks Task Role**
   Directional coupling asymmetry $A = \frac{C_{i \to j} - C_{j \to i}}{C_{i \to j} + C_{j \to i}}$ quantitatively tracks externally defined task roles (leader vs. follower, speaker vs. listener) across multi-agent RL, dialogue, and hyperscanning.

---

## 3. The Critical Shift: "Understanding Is Not Observable" (`paper2/`)

During Stage 2 empirical validation, a crucial discovery superseded the pure observational framing.

### The Empirical Wall & Discovery Chain
1. **The Estimator Bias Trap**: An initial $r = 0.99$ bandwidth-coupling curve was identified as regression sample-size bias in raw transfer entropy. Pure noise returned 0.71 fabricated "bits". Corrected using block-shuffle surrogate subtraction (`cl.effective_te`).
2. **Sender Encoding**: In multi-agent RL, agents initially failed to encode messages ($R^2 \approx 0.001$). Fixed by adding a speaker auxiliary prediction loss ($aux\_coef \approx 200$).
3. **Receiver Decodability vs. Behavior (Proposition 1)**: The listener's internal hidden representations reconstructed the speaker's signal with error $0.0017$ (the information was *provably present and linearly decodable*), yet the receiver's policy remained completely unchanged ($z \approx 0$).
4. **The Oracle Control**: Giving the receiver the goal directly without a channel resulted in the exact same goal-blind policy. The failure was an RL optimization landscape issue, not a channel capacity limit.

### Key Theoretical Contributions of Paper 2

1. **Theorem 1 (Observational Unidentifiability)**: Observational Transfer Entropy ($TE$), Granger Causality, and Mutual Information cannot distinguish true functional coupling from shared prior conventions ($U$) or common task drivers.
2. **Proposition 2 (Temporal Precedence Fails)**: Precedence does not identify causality because shared conventions precede both the sender's message $M$ and receiver's internal state.
3. **Proposition 3 (Receiver Representation Fails)**: Measuring higher resolution or internal neural representations in the receiver fails the front-door criterion.
4. **Theorem 2 (Interventional Identification)**: Functional coupling is strictly an **interventional quantity**. Identification requires:
   - Direct intervention (message randomization / swapping across episodes), or
   - Instrumental variable identification (e.g., using exogenous channel noise as an instrument).
5. **Randomization vs. Ablation**: Message randomization (`rollout_with_message_source()`) is ~3$\times$ more sensitive than zero-ablation.
6. **Value of Information (VoI)**: Functional coupling must be measured against captured share of the Value of Information rather than raw null tests.

---

## 📖 Primary Source Documents
- [`opp.md`](file:///home/charizard/computational-coupling/opp.md) — Fundamental manifesto on the interventional reframe.
- [`paper2/main.tex`](file:///home/charizard/computational-coupling/paper2/main.tex) — Draft of Paper 2 ("Understanding Is Not Observable").
- [`paper/main.tex`](file:///home/charizard/computational-coupling/paper/main.tex) — Draft of Paper 1 (Original BBI Formalism).
- [`handoff.md`](file:///home/charizard/computational-coupling/handoff.md) — Comprehensive state of project as of July 2026.

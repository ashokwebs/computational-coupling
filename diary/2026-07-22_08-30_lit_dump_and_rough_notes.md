# Diary Entry — July 22, 2026 (08:30 AM)
**Location:** Library ground floor, near the window
**Mood:** Focused, hyper-curious, 42 Chrome tabs open 💻🔥
**Status:** Day 4 of research program — Literature Rabbit Hole & Raw Data Dump

---

### Day 4: Literature Search, Open Datasets & Raw Data Dump

Woke up at 6:30 AM feeling energized. Today is all about getting real empirical grounding.

My laptop fan sounds like a jet engine right now becuase Chrome is using 14GB RAM lol. 42 tabs open across Google Scholar, arXiv, OpenNeuro, and PubMed.

Here is the raw data dump I scraped and typed into my notes:

---

### 1. Estimator Mechanics & Transfer Entropy Math 🧮

To calculate $\mathrm{TE}_{X \to Y}$ in real time-series without assuming linear Gaussian distributions (becuase brain signals are horribly non-linear!), we need non-parametric estimators:

#### A. Kraskov-Stögbauer-Grassberger (KSG) k-NN Estimator
- **Paper:** Kraskov et al. (2004) *"Estimating mutual information"*, Phys. Rev. E. Schreiber (2000) *"Measuring Information Transfer"*, Phys. Rev. Lett.
- **Core idea:** Uses $k$-nearest neighbor distances in joint space $(Y_{t+\Delta}, Y_{\le t}, X_{\le t})$ to dynamically adjust kernel sizes, avoiding fixed binning artifacts!
- **Default hyperparams:** $k = 4$, embedding delay $\tau = 1$, embedding dimension $d = 3$.

#### B. Effective Transfer Entropy (ETE) & Surrogate Shuffling
- Problem: Finite sample sizes create systematic positive bias in TE (even uncoupled random noise yields $\mathrm{TE} > 0$).
- Solution: Calculate Effective Transfer Entropy:
  $$\mathrm{ETE}_{X \to Y} = \mathrm{TE}_{X \to Y} - \frac{1}{N_{\text{surr}}} \sum_{i=1}^{N_{\text{surr}}} \mathrm{TE}_{X^{\text{surr}}_i \to Y}$$
  where $X^{\text{surr}}$ is generated via Fourier surrogate or block shuffling.

#### C. Neural Predictive Gain Estimator (Our Neural Network Approximation for High Dimensions)
- When state dimension $d > 50$ (e.g. 512-dim hidden vectors in RL agents or 64-channel EEG), k-NN falls victim to the curse of dimensionality!
- Solution: Train two predictive models:
  1. **Self-predictor model:** $P_\phi(Y_{t+1} \mid Y_{\le t})$ (log-loss $L_{\text{self}}$)
  2. **Joint-predictor model:** $P_\psi(Y_{t+1} \mid Y_{\le t}, X_{\le t})$ (log-loss $L_{\text{joint}}$)
- Predictive Gain:
  $$\hat{\mathrm{TE}}_{X \to Y} = L_{\text{self}} - L_{\text{joint}} = \mathbb{E} \left[ \log \frac{P_\psi(Y_{t+1} \mid Y_{\le t}, X_{\le t})}{P_\phi(Y_{t+1} \mid Y_{\le t})} \right]$$

---

### 2. Verified Human Hyperscanning EEG Datasets (For Paper 2) 🧠📡

1. **DUET (Dyadic Understanding, EEG and Turn-taking):** OpenNeuro `ds007764`. Dual 64-channel EEG from 18 dyads engaging in natural French face-to-face conversation.
2. **Joint Agency EEG Dataset:** OpenNeuro `ds007471`. Dual EEG on participant pairs performing joint piano duet tapping.

---

### 3. Classic Neuroscience & BBI References 📚

- **Uri Hasson et al. (2010, PNAS):** *"Speaker-listener neural coupling underlies successful communication."*
- **Miguel Nicolelis et al. (2015, PLOS ONE):** *"Building an organic computing device with multiple interconnected brains."*
- **Giulio Tononi et al. (2023):** Integrated Information Theory 4.0 (IIT $\Phi$).

Time to organize these findings into our 2-Track Masterplan!

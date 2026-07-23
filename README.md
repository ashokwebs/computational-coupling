# 🧠⚡ A Theory of Computational Coupling Between Intelligent Systems
### *Toward a General Foundation for Brain-to-Brain Communication (BBI)*

**Author:** Ashok Pasala (VIT-AP University)  
**Target Venues:** NeurIPS, ICML, ICLR, Nature Machine Intelligence, Nature Neuroscience  
**Draft Version:** 0.2.0 (Working Research Program)  

---

## Yo! Welcome to the Lab! 🚀

Bro, if you landed here thinking Brain-to-Brain Interfaces (BBI) are about sci-fi telepathy or zapping someone's motor cortex to force them to click a mouse button... **think again!** 

For years, the BBI and BCI fields have been trying to design fixed "Brain Communication Protocols" or "Brain Languages" without ever asking the most fundamental question in science: **What quantity are we actually trying to optimize?** 

Designing a BCI protocol right now without a measurement theory is like trying to design 56k dial-up modems before Claude Shannon defined channel capacity in 1948! 

This repo houses my **multi-year open research program** that reframes BBI around a general, substrate-independent measurement theory: **The Theory of Computational Coupling Between Intelligent Systems**.

---

## 💡 The Big Reframe in One Sentence

> **Communication between two intelligent systems isn't the transmission of a static pre-encoded message, but the degree to which their internal state trajectories become *predictively entangled* through a bandwidth-limited interface.**

Instead of inventing arbitrary brain dictionaries, we define **Coupling Capacity** ($C_{\text{couple}}$):
$$C(i \to j) \triangleq \sup_{g \in \mathcal{A}(B)} \mathrm{TE}_{i \to j}(\Delta; g)$$

Where Shannon capacity is the supremum of mutual information over input distributions subject to power constraints, **Coupling Capacity** is the supremum of **directed information / transfer entropy** over interface designs subject to bandwidth constraints.

---

## 🎯 The Three Falsifiable Predictions

We dont do hand-wavy claims here. Reviewer #2 is gonna try to kill us anyway, so here is how you test (or kill) this theory in a lab:

1. **Prediction 1: Capacity–Bandwidth Saturation Law**  
   As channel bandwidth $B$ increases, coupling capacity $C(i \to j; B)$ increases concavely and saturates **NOT** at raw channel capacity, but at $\min(\dim_{\text{eff}}(\mathcal{M}_i), \dim_{\text{eff}}(\mathcal{M}_j))$ — the smaller of the two systems' effective internal representational dimensionality.
2. **Prediction 2: Self-Predictive Accuracy Governs Capacity Efficiency**  
   Systems with better internal world models (higher self-predictive accuracy) extract more coupling capacity per unit of channel bandwidth ($C/B$).
3. **Prediction 3: Asymmetry Tracks Task Role**  
   Directional coupling asymmetry $A = \frac{C_{i \to j} - C_{j \to i}}{C_{i \to j} + C_{j \to i}}$ quantitatively tracks externally defined task roles (leader vs follower, speaker vs listener) across multi-agent RL, dialogue, and hyperscanning.

---

## 📂 Repo Structure (How We Keep Things Clean)

No messy monolithic scripts! Everything is separated cleanly:

```
computational-coupling/
├── README.md                 # You are here!
├── LICENSE                   # MIT License
├── CONTRIBUTING.md           # How to collaborate with us
├── DEVELOPMENT.md            # Setup & compilation guide
├── REPRODUCIBILITY.md        # Seeds & empirical verification
├── ROADMAP.md                # 4-paper research masterplan
│
├── paper/                    # Overleaf-compatible LaTeX source
│   ├── main.tex              # Primary LaTeX entry point
│   ├── references.bib        # Verified BibTeX literature database
│   ├── output/paper.pdf      # Compiled working draft PDF
│   └── sections/             # Modular section files
│
├── literature/               # Paper database & threat analysis
│   ├── literature_review.md  # Master 15-paper analysis table
│   └── bibliography.bib      # BibTeX master database
│
├── theory/                   # Formal math derivations & proofs
│   ├── definitions.md        # State spaces, manifolds & interface maps
│   ├── mathematics.md        # Transfer entropy & predictive gain
│   ├── proofs.md             # Capacity-bandwidth saturation proof
│   └── open_questions.md     # Unsolved theoretical problems
│
├── experiments/              # Codebase for empirical papers
│   ├── paper1_rl/            # Paper 1: Multi-Agent RL testbed (PettingZoo)
│   ├── paper2_hyperscanning/ # Paper 2: Dual EEG/fMRI hyperscanning
│   ├── notebooks/            # Exploratory Jupyter notebooks
│   └── results/              # Experiment logs, plots & metrics
│
├── datasets/                 # OpenNeuro configs & data downloaders
├── figures/                  # Publication-ready vector figures
├── diary/                    # Personal research journal (22/07/2026 onwards)
├── presentations/            # Slide decks & conference talks
└── archive/                  # Legacy drafts & old single-file scratch space
```

---

## 🚀 Quick Start

### 1. Compile the LaTeX Paper
```bash
python3 paper/compile_paper.py
# Or use pdflatex main.tex inside paper/
```

### 2. Run Paper 1 Experiment Scaffold (Multi-Agent RL)
```bash
cd experiments/paper1_rl/
python run_bandwidth_sweep.py --env simple_speaker_listener_v4 --bandwidth_bits 1 2 4 8 16 32
```

---

## 🗺️ The Multi-Year Paper Roadmap

* **Paper 1 (NeurIPS / ICML):** Validate Predictions 1–2 in a controlled multi-agent RL testbed (`PettingZoo` cooperative games) sweeping channel bandwidth and measuring neural predictive gain.
* **Paper 2 (Nature Neuroscience / ICLR):** Test predictions against public human EEG/fMRI hyperscanning datasets (OpenNeuro `ds007764` DUET, `ds007471` Joint Agency EEG).
* **Paper 3 (Nature Machine Intelligence):** Causal non-invasive manipulation of channel bandwidth/latency in human dyads.
* **Paper 4 / Prototype (Nature):** Use coupling capacity as an explicit loss function to *learn* an optimal interface between two neural networks/brains, culminating in a closed-loop BBI prototype!

---

## ✉️ Contact & Collaboration

Written & maintained by **Ashok Pasala** (VIT-AP University).  
Got questions, suggestions, or wanna collaborate on multi-agent RL / neuro-imaging experiments? Open an Issue or Pull Request!

*Lets build the future of computational neuroscience together!* 🚀✨

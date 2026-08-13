---
tags: ["#diary/entry", "#research-log"]
alias: "2026-07-22_23-45_deep_dive_into_the_canon"
---

# Diary Entry — July 22, 2026 (11:45 PM)
**Location:** Hostel Room (Desk covered in printed paper preprints & yellow highlighters)
**Mood:** Mind blown, hyper-analyzing literature, 2 AM researcher energy 🧠🔥
**Status:** Day 4 Late Night — Deep-Dive into the 15 Core Papers

---

### Late Night Paper Breakdown: Analyzing the Literature Canon!

Bro, I spent the entire evening reading through the 15 core papers in our literature vault. My eyes are burning, but holy shit, the connections are starting to click so hard!

Here is my raw, unfiltered breakdown of every single major paper and why it matters for our theory of computational coupling:

---

### 1. The BBI Foundations (Hardware & Empirical Triggers)

* **Pais-Vieira, Lebedev, & Nicolelis (2013, Sci Rep):**  
  *What they did:* Rat-to-rat motor cortex ICMS microstimulation. Encoder rat presses lever $\to$ ICMS zaps decoder rat $\to$ decoder rat presses lever (~70% accuracy).  
  *My 2 AM Take:* It proves biological plausibility, but bro... **it's 1-bit trigger zapping!** That's not a continuous language, that's just a remote-control button.
* **Rao, Stocco, et al. (2014, PLoS ONE):**  
  *What they did:* First non-invasive human BBI. Sender EEG motor imagery triggers TMS over Receiver's motor cortex to press a key.  
  *My 2 AM Take:* Super cool that it's safe and non-invasive, but the bit-rate is $<1$ bit/sec. Peripheral motor output only.
* **Jiang, Stocco, & Rao (2019, Sci Rep — BrainNet):**  
  *What they did:* 3-person BBI playing Tetris. Receivers learn to trust reliable senders over noisy channels via injected phosphenes.  
  *My 2 AM Take:* Moves BBI from dyadic pairs to multi-node networks! But still choked by binary phosphenes.

---

### 2. Emergent AI Languages & Active Inference

* **Foerster et al. (2016, NIPS — DIAL):**  
  *What they did:* Differentiable Inter-Agent Learning. Deep MARL agents invent novel communication protocols by backpropagating gradients through noisy channels.  
  *My 2 AM Take:* **This is the exact artificial analog for BBI!** When two brains are coupled via digital channels, they form a MARL system. DIAL gives us the optimization mechanism.
* **McParlin, Cerritelli, & Karl Friston (2022, Front Behav Neurosci):**  
  *What they did:* Modeled therapeutic alignment and communication as mutual free-energy minimization under Active Inference.  
  *My 2 AM Take:* Friston gives us the biological "why"! Two connected brains synchronize becuase coupling minimizes joint variational free energy (surprise).

---

### 3. Optimal Transport & Representation Alignment

* **Alexis Thual & Bertrand Thirion et al. (2022, NeurIPS — FUGW):**  
  *What they did:* Fused Unbalanced Gromov-Wasserstein (FUGW) alignment using Optimal Transport. Matches functional signatures (Wasserstein) while penalizing topological deformation (Gromov-Wasserstein).  
  *My 2 AM Take:* **FUGW is our mathematical routing protocol!** It solves the problem of idiosyncratic brain anatomy. It routes a semantic vector from Sender neurons to homologous Receiver neurons without catastrophic misalignment.
* **Chen, Haxby, & Ramadge (2015, NeurIPS — SRM):**  
  *What they did:* Shared Response Model factorizing multi-subject fMRI matrices ($X_i = W_i S + E_i$).  
  *My 2 AM Take:* Historical linear baseline before FUGW introduced non-linear optimal transport.
* **Nakamura, Kanai, & Hayashi (2024, Front Neuroinf):**  
  *What they did:* Zero-shot cross-subject representation transfer using unsupervised hyperspherical embeddings.  
  *My 2 AM Take:* **THIS IS OUR PRIMARY NOVELTY THREAT!** Reviewer #2 is gonna scream about Nakamura. But wait... Nakamura et al. do *passive representation mapping* between static scans. Our theory goes beyond them into **active closed-loop control** (driving the receiver's state trajectory with feedback!).

---

### 4. Brain Foundation Models & Decoders

* **LaBraM (Jiang et al., 2024, ICLR):**  
  *What they did:* Large Brain Model trained on 2,500 hours of clinical EEG using vector-quantized neural spectrum prediction (VQ-NSP).  
  *My 2 AM Take:* LaBraM's latent space acts as our universal EEG temporal codec!
* **BrainLM (Caro et al., 2024, bioRxiv):**  
  *What they did:* Generative fMRI foundation model trained on 6,700 hours across 424 AAL parcels.  
  *My 2 AM Take:* Great for spatial semantic feature extraction, but 4-6 second BOLD latency kills real-time interaction.
* **MindEye2 (Scotti et al., 2024, ICML):**  
  *What they did:* Reconstructs visual perception from fMRI using shared-subject ridge regression mapped to unCLIP space.  
  *My 2 AM Take:* Proves high-bandwidth cross-subject semantic decoding is totally feasible with just 1 hour of training data!

---

### 5. Information Theory & Causality Bedrocks

* **Claude Shannon (1948):** Defined Channel Capacity ($C = \max I(X;Y)$). Bedrock of information theory.  
  *Our Reframe:* We generalize Shannon capacity from static messages to dynamic coupled state trajectories ($C_{\text{couple}} = \sup \mathrm{TE}_{A \to B}$).
* **Thomas Schreiber (2000, Phys Rev Lett):** Introduced model-free Transfer Entropy ($\mathrm{TE}_{X \to Y}$).  
  *Why it matters:* Conditions out $Y$'s own past to prove true directional driving.
* **Uri Hasson et al. (2010, PNAS):** fMRI hyperscanning showing listener brain state tracks speaker brain state with lag.  
  *Why it matters:* Empirical biological baseline for inter-brain synchrony.
* **Read Montague et al. (2002, NeuroImage):** First fMRI hyperscanning connecting two scanners over the internet for deception games.

---

### Final Thought before sleep:
Every piece of the puzzle is here. Information theory (Shannon/Schreiber) + Optimal Transport (FUGW) + Foundation Models (LaBraM/BrainLM) + Active Inference (Friston) + Emergent MARL (DIAL).

We are uniting all of this into one single theory of Coupling Capacity!

Going to sleep super hyped! 😴🚀

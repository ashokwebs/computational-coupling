# 📚 Master Literature Review & Threat Analysis

Yo! Welcome to the central literature vault for the **Theory of Computational Coupling**!

When you're trying to build a new theoretical foundation for Brain-to-Brain Communication, you dont just read papers — you analyze their mathematical guts, find their hidden flaws, and figure out how your theory subsumes them.

Below is our master paper database categorized across **15 core papers**, threat scores, and essential datasets.

---

## 🏛️ Part 1: The Core 15 Paper Database

| # | Paper Title | Authors & Year | Venue / Link | Main Contribution | Threat Level | Critical Weakness | Role in Our Work |
| :- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **A Brain-to-Brain Interface for Real-Time Sharing of Sensorimotor Info** | Pais-Vieira et al. (2013) | *Sci Rep* `10.1038/srep01319` | First rat-to-rat BBI via ICMS microstimulation. ~70% transfer accuracy. | **70% (Low)** | Invasive; binary trigger zapping (1 bit). Not real language. | Establishes physical biological plausibility. |
| 2 | **A Direct Brain-to-Brain Interface in Humans** | Rao et al. (2014) | *PLoS ONE* `10.1371/journal.pone.0111332` | First non-invasive human BBI via EEG motor imagery -> TMS. | **75% (Low)** | Unidirectional; $<1$ bit/sec latency; motor imagery only. | Foundational baseline for non-invasive BBI. |
| 3 | **BrainNet: A Multi-Person Brain-to-Brain Interface...** | Jiang et al. (2019) | *Sci Rep* `10.1038/s41598-019-41895-7` | 3-person BBI (Brainet) playing Tetris via TMS phosphenes. | **85% (Medium)** | Bandwidth choked at discrete phosphenes. | Scaling dyadic pairs to multi-agent networks. |
| 4 | **Learning to Communicate with Deep Multi-Agent RL (DIAL)** | Foerster et al. (2016) | *NIPS* `arxiv:1605.06676` | Agents invent communication protocols via gradient backprop. | **75% (Medium)** | Tested only on discrete grid-world toys. | Artificial MARL analog for emergent BCP protocols. |
| 5 | **Aligning individual brains with Fused Unbalanced Gromov-Wasserstein (FUGW)** | Thual et al. (2022) | *NeurIPS* `arxiv:2206.09398` | Optimal Transport matching functional signatures across subjects. | **70% (Low)** | Heavy non-convex block-coordinate descent cost. | Mathematical spatial routing protocol for neural vectors. |
| 6 | **Therapeutic Alliance as Active Inference** | McParlin et al. (2022) | *Front Behav Neurosci* `10.3389/fnbeh.2022.897247` | Interpersonal alignment as mutual free-energy minimization. | **85% (High)** | Purely theoretical; no direct neural intervention data. | Teleological "why" for coupling alignment. |
| 7 | **Large Brain Model for Learning Generic Representations (LaBraM)** | Jiang et al. (2024) | *ICLR* `arxiv:2405.18765` | EEG foundation model pre-trained on 2,500 hours via VQ-NSP. | **80% (Medium)** | Offline decoding only; no writing/stimulation. | Latent space acts as generic EEG codec. |
| 8 | **BrainLM: A foundation model for brain activity recordings** | Caro et al. (2024) | *bioRxiv* `10.1101/2023.09.12.557460` | fMRI foundation model trained on 6,700 hours across 424 parcels. | **70% (Low)** | Extreme BOLD latency (4-6 sec) limits real-time interaction. | High-level spatial semantic extraction. |
| 9 | **MindEye2: Shared-Subject Models Enable fMRI-To-Image...** | Scotti et al. (2024) | *ICML* `arxiv:2403.11207` | Visual perception reconstruction via shared-subject ridge regression. | **90% (High)** | Visual cortex only; motion sensitive. | Proves high-bandwidth cross-subject semantic extraction. |
| 10 | **Unsupervised method for representation transfer from one brain to another** | Nakamura et al. (2024) | *Front Neuroinf* `10.3389/fninf.2024.1470845` | Zero-shot alignment via unsupervised hyperspherical embeddings. | **95% (High Threat)** | Requires static anatomical masks; passive transfer only. | Primary novelty threat! We add active closed-loop control. |
| 11 | **Measuring Information Transfer (Transfer Entropy)** | Schreiber (2000) | *Phys Rev Lett* `85(2):461` | Introduced model-free Transfer Entropy ($\mathrm{TE}_{X \to Y}$). | **50% (Low)** | $O(N^2)$ sample complexity in high dimensions. | Primary causality measurement metric. |
| 12 | **A Mathematical Theory of Communication** | Shannon (1948) | *Bell Syst Tech J* `27:379` | Defined Channel Capacity ($C = \max I(X;Y)$). | **Foundation** | Static channels without dynamic feedback loops. | Direct conceptual foundation for Coupling Capacity $C_{\text{couple}}$. |
| 13 | **Speaker-listener neural coupling underlies successful communication** | Hasson et al. (2010) | *PNAS* `107(32):14425` | fMRI hyperscanning showing listener brain tracks speaker brain with lag. | **65% (Low)** | Observational; cannot separate stimulus correlation from driving. | Empirical baseline for biological brain coupling. |
| 14 | **A Reduced-Dimension fMRI Shared Response Model (SRM)** | Chen et al. (2015) | *NeurIPS* `10.5555/2969442` | Linear factorization mapping subjects to shared response space $S$. | **60% (Low)** | Requires time-locked identical movie stimuli. | Predecessor to non-linear OT alignment (FUGW). |
| 15 | **Hyperscanning: Simultaneous fMRI during linked social interactions** | Montague et al. (2002) | *NeuroImage* `10.1006/nimg.2002.1150` | Linked two fMRI scanners via internet for deception games. | **50% (Low)** | High latency; dual-scanner cost. | Historic pioneer of multi-brain recordings. |

---

## ⚡ Part 2: Novelty Analysis & How We Defend Our Territory

### Threat 1: Nakamura et al. (2024) — Unsupervised Representation Transfer
* **Why it looks dangerous:** They claim to translate brain activity between subjects without labels using hyperspherical embeddings.
* **Our Defense:** Nakamura et al. perform *passive representational mapping* between static recordings. Our Theory of Computational Coupling defines **active closed-loop control**: driving the Receiver's neural state trajectory across bandwidth-limited channels with feedback.

### Threat 2: The "Superficial Synchrony" Hyperscanning Trap
* **The Critique:** Reviewer #2 is gonna complain: *"If two people listen to the same podcast, their brains synchronize. That's not BBI, that's just shared sensory input!"*
* **Our Defense:** We deploy **Directed Information & Transfer Entropy** ($\mathrm{TE}_{A \to B} = I(Y_{t+\Delta}; X_{\le t} \mid Y_{\le t})$) to condition out $Y$'s own past and shared sensory drivers, isolating purely causal, directional coupling!

---

## 📊 Part 3: Essential Open-Access Datasets

1. **DUET (Dyadic Understanding, EEG and Turn-taking):** OpenNeuro `ds007764`. Dual 64-channel EEG across 18 face-to-face French dialogue dyads.
2. **Joint Agency EEG Dataset:** OpenNeuro `ds007471`. Synchronized dual EEG during piano duet coordination.
3. **Natural Scenes Dataset (NSD):** 7T fMRI (8 subjects watching 73,000 COCO images).
4. **TUH EEG Corpus:** >10,000 clinical EEG recordings for pre-training foundation models (LaBraM).

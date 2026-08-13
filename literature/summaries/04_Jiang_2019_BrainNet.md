---
tags: ["#literature/paper", "#paper/canon"]
alias: "04_Jiang_2019_BrainNet"
---

# Research Paper Report: BrainNet: A Multi-Person Brain-to-Brain Interface...

**Authors:** Linxing Jiang, Andrea Stocco, David M. Losey, Justin A. Abernethy, Chantel S. Prat, Rajesh P. N. Rao  
**Publication Year:** 2019  
**Venue:** *Nature Scientific Reports*, 9:4189  
**DOI:** `10.1038/s41598-019-41895-7`  
**Similarity / Novelty Threat:** **85% (Medium Threat)**  

---

## 📌 Abstract & Experimental Paradigm
Demonstrated **BrainNet**, the first multi-person non-invasive direct BBI network. Three human subjects (two Senders, one Receiver) collaborated to solve a Tetris-like game. Senders watched the block and decided whether to rotate it ($17	ext{ Hz}$ or $15	ext{ Hz}$ SSVEP flashing light). Their EEG signals were decoded and zapped into the Receiver's visual cortex via TMS phosphenes (flashing visual lights).

## 🛠️ Technical & Hardware Specifications
* **Network Topology:** 3-node network (2 Senders, 1 Receiver).
* **Sender Modality:** EEG measuring Steady-State Visual Evoked Potentials (SSVEP) at $15	ext{ Hz}$ and $17	ext{ Hz}$.
* **Receiver Modality:** Single-pulse TMS over occipital cortex injecting phosphenes (visual flashes).
* **Signal Trust Mechanism:** Receiver calculated Sender reliability over time and weighted signals to ignore artificially corrupted Sender inputs.

## 📊 Empirical Results & Metrics
* **Average Group Accuracy:** Achieved **81.25% task completion accuracy**.
* **Mutual Information:** Calculated MI to quantify signal reliability across network nodes.

## ⚠️ Critical Weaknesses & Limitations
1. **Discrete Binary Channel:** Limited to binary phosphene triggers (rotate vs don't rotate).
2. **Visual Phosphene Dependency:** Relies on sensory injection (occipital phosphenes) rather than direct cognitive manifold injection.

## 🔬 Role in the Theory of Computational Coupling
- **Multi-Node Baseline:** Demonstrates social trust and consensus emerging over neural networks.
- **Relation to Our Work:** Expands dyadic coupling to multi-agent network topologies.

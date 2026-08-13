---
tags: ["#literature/paper", "#paper/canon"]
alias: "02_Rao_2014_Human_BBI"
---

# Research Paper Report: A Direct Brain-to-Brain Interface in Humans

**Authors:** Rajesh P. N. Rao, Andrea Stocco, Matthew Bryan, Devapratim Sarma, Tiffany M. Youngquist, Joseph Wu, Chantel S. Prat  
**Publication Year:** 2014  
**Venue:** *PLoS ONE*, 9(11): e111332  
**DOI:** `10.1371/journal.pone.0111332`  
**Similarity / Novelty Threat:** **75% (Low Threat)**  

---

## 📌 Abstract & Experimental Paradigm
Demonstrated the first non-invasive human-to-human Brain-to-Brain Interface. A Sender subject played a computer game requiring firing a cannon at a target, imagining moving their right hand to fire. Motor imagery was detected via non-invasive EEG and transmitted across the internet to a Receiver subject sitting in a separate room wearing a Transcranial Magnetic Stimulation (TMS) coil over their motor cortex.

## 🛠️ Technical & Hardware Specifications
* **Sender Modality:** Non-invasive EEG (mu/beta rhythm desynchronization over C3 electrode).
* **Receiver Modality:** Single-pulse Transcranial Magnetic Stimulation (TMS) positioned over the left motor cortex (hand area).
* **Latency:** End-to-end internet transmission delay averaged $650 	ext{ ms}$.

## 📊 Empirical Results & Metrics
* **Task Accuracy:** Achieved **83.3% to 100% target hit rate** across dyadic human pairs.
* **Throughput:** Bandwidth restricted to $< 0.1$ bits/second.

## ⚠️ Critical Weaknesses & Limitations
1. **Unidirectional Control:** Information flows strictly Sender $	o$ Receiver without closed-loop feedback.
2. **Extreme Bandwidth Choking:** Binary motor trigger (fire / don't fire).
3. **Peripheral Motor Dependency:** Relies on motor cortex stimulation triggering physical finger twitches on a touchpad.

## 🔬 Role in the Theory of Computational Coupling
- **Non-Invasive Baseline:** Proves human non-invasive BBI is safe and achievable.
- **Contrast with Our Work:** Rao et al. optimized a specific BCI peripheral hack. We establish a substrate-independent measurement theory governing maximum theoretical information flow over bandwidth-constrained channels.

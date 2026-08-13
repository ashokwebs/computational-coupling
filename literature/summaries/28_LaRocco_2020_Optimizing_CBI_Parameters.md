---
tags: ["#literature/paper", "#paper/extended-canon"]
alias: "28_LaRocco_2020_Optimizing_CBI_Parameters"
---

# Research Paper Report: Optimizing Computer–Brain Interface Parameters for Non-invasive Brain-to-Brain Interface

**Authors:** John LaRocco, Dong-Guk Paeng
**Publication Year:** 2020
**Venue:** *Frontiers in Neuroinformatics*, 14:1
**DOI/arXiv:** `10.3389/fninf.2020.00001`
**Category:** (6) Non-invasive brain stimulation bandwidth/capacity limits
**Role in Our Work:** **Complementary engineering study, not a threat.** Directly quantifies the non-invasive BBI bandwidth bottleneck our theory treats as the constraint $B$.

---

## 📌 Abstract & Architecture
Simulation study of a non-invasive brain-to-brain interface pipeline combining EEG-based brain-computer interface (BCI) decoding with a computer-brain interface (CBI) "writing" stage using transcranial focused ultrasound stimulation. Systematically varies system latency and stimulation failure rate to find the parameter regime that maximizes achievable information transfer rate. Central finding: system *latency*, not raw stimulation intensity or channel count, is the dominant bottleneck — optimal throughput requires end-to-end latency under ~100 ms, and the system remains usably efficient even at a 25% stimulation-delivery failure rate if latency is controlled.

## 🔗 Connection to Computational Coupling Theory
Provides an independent, engineering-grounded quantification of the bandwidth ceiling $B$ that our theory treats as a free parameter to be swept (as in Stage 2's $B\in\{1,2,4,8,16,32\}$ bits/step sweep). Useful for the theory paper's discussion of ecological/experimental plausibility: it grounds the claim that real non-invasive BBI systems (à la Rao et al. 2014, BrainNet, canon #2/#3) sit at extremely low $B$ (sub-bit-per-second regime, consistent with the ~0.05 bps figure already noted for TMS-based BBI in the canon), and that latency — not raw information content per pulse — is often the limiting resource. Relevant to the ethics/feasibility discussion of the BBI application: it is direct evidence that closing the interface loop (write-back into a second brain) is the harder engineering problem, reinforcing why our theory's asymmetric/directional framing (Prediction 3) matters practically, not just formally.

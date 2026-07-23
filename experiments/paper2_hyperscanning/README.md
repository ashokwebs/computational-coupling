# 🧠 Paper 2 Experiment Pipeline: Human EEG/fMRI Hyperscanning

**Paper Title:** *Validating Computational Coupling in Biological Neural Corpora*  
**Datasets:** OpenNeuro `ds007764` DUET (18 dyadic 64-channel EEG dialogue pairs) & `ds007471` (Joint Agency EEG)  
**Target Venues:** Nature Neuroscience / ICLR  

---

## 🎯 Goal

Test whether the Capacity-Bandwidth Saturation Law and Asymmetry Index $A = \frac{C_{A \to B} - C_{B \to A}}{C_{A \to B} + C_{B \to A}}$ hold in biological human brains during naturalistic conversation and motor coordination.

---

## 🛠️ Pipeline Architecture

1. **EEG Pre-processing:** Artifact rejection, ICA decomposition, 1-45 Hz bandpass filter via `MNE-Python`.
2. **Functional Alignment:** Cross-subject surface alignment using **Fused Unbalanced Gromov-Wasserstein (FUGW)** (`fugw` library).
3. **Temporal Encoder:** Feature extraction using pre-trained EEG Foundation Model (**LaBraM**).
4. **Causality Estimator:** Calculate Effective Transfer Entropy (ETE) after surrogate Fourier shuffling.

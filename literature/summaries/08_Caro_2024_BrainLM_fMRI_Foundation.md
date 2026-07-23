---
tags: [#literature/paper, #paper/canon]
alias: "08_Caro_2024_BrainLM_fMRI_Foundation"
---

# Research Paper Report: BrainLM: A foundation model for brain activity recordings

**Authors:** Josue Caro, Pedro Fonseca, David van Dijk  
**Publication Year:** 2024  
**Venue:** *bioRxiv preprints*  
**DOI:** `10.1101/2023.09.12.557460`  
**Similarity / Novelty Threat:** **70% (Low Threat)**  

---

## 📌 Abstract & Architecture
Introduced **BrainLM**, a generative foundation model for fMRI brain recordings trained on 6,700 hours of fMRI data across 424 AAL brain parcels using masked autoencoding (MAE).

## 🛠️ Technical Details
* **Pre-training Data:** 6,700 hours of fMRI from UK Biobank and HCP.
* **Parcellation:** 424 AAL brain parcels.
* **Loss Objective:** Masked Autoencoding MSE reconstruction loss on parcel time series.

## ⚠️ Critical Weaknesses & Limitations
1. **Hemodynamic Delay:** fMRI BOLD signal has a 4-6 second hemodynamic response lag, limiting real-time control.

## 🔬 Role in the Theory of Computational Coupling
- **Spatial Semantic Codec:** BrainLM provides high-level spatial feature extraction for fMRI embeddings.

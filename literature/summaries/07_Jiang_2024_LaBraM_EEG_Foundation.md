---
tags: ["#literature/paper", "#paper/canon"]
alias: "07_Jiang_2024_LaBraM_EEG_Foundation"
---

# Research Paper Report: Large Brain Model for Learning Generic Representations (LaBraM)

**Authors:** Wei-Bang Jiang, Lin Zhao, Bao-Liang Lu  
**Publication Year:** 2024  
**Venue:** *International Conference on Learning Representations (ICLR 2024)*  
**arXiv:** `2405.18765`  
**Similarity / Novelty Threat:** **80% (Medium Threat)**  

---

## 📌 Abstract & Architecture
Introduced **LaBraM**, a massive EEG foundation model pre-trained on 2,500+ hours of clinical EEG data. Implements Vector-Quantized Neural Spectrum Prediction (VQ-NSP) to tokenize continuous neural spectrum features into discrete neural tokens.

## 🛠️ Technical Details
* **Pre-training Dataset:** TUH EEG Corpus (2,500+ hours across thousands of subjects).
* **Tokenizer:** Vector-Quantized Neural Spectrum Prediction (VQ-NSP).
* **Architecture:** Neural Transformer backbone capable of zero-shot transfer across diverse electrode montages.

## 📊 Empirical Benchmarks
* Achieves state-of-the-art AUROC and classification accuracy on TUAB (Abnormality) and TUAR (Artifact) benchmarks.

## ⚠️ Critical Weaknesses & Limitations
1. **Offline Decoding Focus:** Designed strictly for passive reading/decoding; ignores active stimulation/writing.

## 🔬 Role in the Theory of Computational Coupling
- **EEG Latent Codec:** LaBraM serves as our temporal neural representation encoder for Paper 2.

---
tags: [#literature/paper, #paper/canon]
alias: "09_Scotti_2024_MindEye2"
---

# Research Paper Report: MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour Data

**Authors:** Paul S. Scotti, Atriya Banerjee, Justin Goode, Nikolay Shabalin, Alex Nguyen, Jonathan Cohen, Kenneth A. Norman, Tanishq Mathew Abraham  
**Publication Year:** 2024  
**Venue:** *International Conference on Machine Learning (ICML 2024)*  
**arXiv:** `2403.11207`  
**Similarity / Novelty Threat:** **90% (High Threat)**  

---

## 📌 Abstract & Architecture
Introduced **MindEye2**, reconstructing visual perceptions from fMRI brain activity with extreme data efficiency (1 hour of fine-tuning per subject). Uses shared-subject ridge regression mapping fMRI voxels to an OpenCLIP (ViT-bigG/14) latent space followed by Stable Diffusion XL image generation.

## 🛠️ Technical Details
* **Dataset:** Natural Scenes Dataset (NSD) 7T fMRI.
* **Loss Objective:** Bidirectional CLIP contrastive loss + ridge regression functional alignment.

## ⚠️ Critical Weaknesses & Limitations
1. **Visual Cortex Restriction:** Restricted to visual stimuli reconstruction.

## 🔬 Role in the Theory of Computational Coupling
- Proves high-bandwidth semantic extraction is feasible cross-subject with minimal data.

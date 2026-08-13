---
tags: ["#literature/paper", "#paper/canon"]
alias: "05_Thual_2022_FUGW_Optimal_Transport"
---

# Research Paper Report: Aligning individual brains with Fused Unbalanced Gromov-Wasserstein

**Authors:** Alexis Thual, Huy Tran, Bertrand Thirion, Rémi Flamary  
**Publication Year:** 2022  
**Venue:** *Advances in Neural Information Processing Systems (NeurIPS 2022)*  
**arXiv:** `2206.09398`  
**Similarity / Novelty Threat:** **70% (Low Threat)**  

---

## 📌 Abstract & Algorithmic Innovation
Pioneered **Fused Unbalanced Gromov-Wasserstein (FUGW)** optimal transport alignment. FUGW aligns functional brain representations across heterogeneous subjects without requiring landmark registration by simultaneously optimizing functional feature matching (Wasserstein distance) and cortical topological structure preservation (Gromov-Wasserstein distance).

## 🛠️ Mathematical Formulation & Loss Function
The FUGW objective finds an optimal transport plan $P \in \mathbb{R}_+^{n_1 	imes n_2}$:
$$\mathcal{L}(P) = (1-lpha) \sum_{i,j} \|F_i^s - F_j^t\|_2^2 P_{i,j} + lpha \sum_{i,j,k,l} |D_{i,k}^s - D_{j,l}^t|^2 P_{i,j} P_{k,l} + 
ho_{	ext{KL}}(P) + arepsilon \mathbf{E}(P)$$
* **Wasserstein Term ($1-lpha$):** Minimizes functional discrepancy between neural activations $F^s$ and $F^t$.
* **Gromov-Wasserstein Term ($lpha$):** Penalizes structural distortion between cortical geodesic distance matrices $D^s$ and $D^t$.
* **Unbalanced KL Term ($
ho_{	ext{KL}}$):** Allows mass creation/destruction to account for anatomical mass mismatch across brains.

## 📊 Empirical Benchmarks
* **Evaluated On:** Individual alignment of fMRI contrast maps across IBC and HCP datasets.
* **Performance:** Significantly outperforms hyperalignment and standard Gromov-Wasserstein in zero-shot cross-subject decoding.

## ⚠️ Critical Weaknesses & Limitations
1. **Computational Complexity:** Non-convex block-coordinate descent optimization is computationally expensive on dense 100k-vertex cortical meshes.

## 🔬 Role in the Theory of Computational Coupling
- **Mathematical Routing Protocol:** FUGW provides the exact geometric alignment engine required to route high-dimensional state vectors from Sender manifold $\mathcal{M}_A$ to Receiver manifold $\mathcal{M}_B$.

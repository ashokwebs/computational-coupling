---
tags: [#meta/reading-list]
alias: "To See — Reading List & Where Our Docs Live"
---

# 👀 To See — External Reading List + Where Our Own Docs Are

Two things in this file:
1. **Where the literature we've already read/summarized lives** (so you don't re-search for it).
2. **New external papers to actually go read**, surfaced by the external critique document archived at
   [`literature/external_critique_2026-07-25_brain_alignment_reframing.md`](literature/external_critique_2026-07-25_brain_alignment_reframing.md)
   (archived only — not acted on, per your call. That doc's own author attributions on a few of these
   were unconfirmed; see the ⚠️ notes below).

---

## 📚 Where our existing research docs are (papers already published by others, already reviewed by us)

- **[`literature/summaries/`](literature/summaries/)** — 40 individual paper summaries, one file each, numbered 01–40.
  Covers BBI hardware (Pais-Vieira rat BBI, Rao human BBI, BrainNet), optimal transport (Thual FUGW),
  brain foundation models (LaBraM, BrainLM, MindEye2), information theory (Shannon, Schreiber TE,
  Tishby IB, Granger causality, Permuter directed info), emergent AI communication (Foerster DIAL,
  Sukhbaatar CommNet, Jang Gumbel-Softmax, Mordatch, Lazaridou), hyperscanning (Hasson, Montague, Zamm,
  Markiewicz, DUET/Joint-Agency EEG datasets), neural manifolds (Gao, Gallego), synchronization (Kuramoto,
  Pecora), and control/rate-distortion theory (Tatikonda, Nair).
- **[`literature/bibliography.bib`](literature/bibliography.bib)** — BibTeX entries for the canon (separate from `paper/references.bib`, which is the subset actually cited in the paper draft).
- **[`literature/literature_review.md`](literature/literature_review.md)** — the running narrative literature review.
- **[`literature/TODO.md`](literature/TODO.md)** — open literature-reading tasks.
- **[`MOC_Literature.md`](MOC_Literature.md)** — Obsidian map-of-content index (currently only lists the original 15 of the 40 — worth regenerating from the full `summaries/` folder next time you're in Obsidian).
- **[`paper/references.bib`](paper/references.bib)** — the 15 keys actually `\cite{}`'d in the Track 1 theory paper draft.

None of the papers below are in that canon yet — they're new, surfaced by the external critique doc.

---

## 🔗 New papers to read (real links, verified 2026-07-25)

### Cross-subject / cross-brain alignment
- **MindAligner** — *Explicit Brain Functional Alignment for Cross-Subject Visual Decoding from Limited fMRI Data*, ICML 2025. Learns a "Brain Transfer Matrix" mapping a new subject's fMRI onto a known subject's space.
  [arXiv:2502.05034](https://arxiv.org/abs/2502.05034)
- **"Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry"** — Pablo Marcos-Manchón & Rishi Jha, 2026. Unsupervised orthogonal-rotation alignment of independently-learned fMRI embedding spaces (Natural Scenes Dataset), no paired data. ⚠️ The critique doc cited this as "Barda et al." — could not confirm that name; the actual authors found are Marcos-Manchón & Jha.
  [arXiv:2605.20496](https://arxiv.org/abs/2605.20496)
- **"Task-guided cross-subject latent alignment: a multi-encoder-decoder VAE"** (MED-VAE), 2026. Cross-subject common latent space anchored to a pretrained ANN's feature space. ⚠️ Cited as "Barmpas et al." in the critique doc — authors not confirmed from search results, worth checking the arXiv listing directly.
  [arXiv:2606.15989](https://arxiv.org/abs/2606.15989)
- **StableMind** — *Source-Free Cross-Subject fMRI Decoding with Regularized Adaptation*, 2026 (came up alongside MindAligner in search — not in the original critique table but directly adjacent).
  [arXiv:2605.02586](https://arxiv.org/pdf/2605.02586)

### Non-invasive decoding to continuous latents
- **Défossez, Caucheteux, Gramfort, Rieul, King** — *Decoding speech perception from non-invasive brain recordings*, Nature Machine Intelligence 5, 1097–1107 (2023). Contrastive M/EEG-to-wav2vec2 alignment, 175 participants, 4 public datasets.
  [arXiv:2208.12266](https://arxiv.org/abs/2208.12266) · [Nature Machine Intelligence](https://www.nature.com/articles/s42256-023-00714-5) · [code](https://github.com/facebookresearch/brainmagick)

### Invasive high-bandwidth decoding
- **Willett, Kunz, Fan, et al.** — *A high-performance speech neuroprosthesis*, Nature 620, 1031–1036 (2023). Intracortical speech BCI, 62 words/min, 9.1% WER on 50-word vocab.
  [Nature](https://www.nature.com/articles/s41586-023-06377-x) · [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2023.01.21.524489v1)

### Foundation models / self-supervised architectures
- **Brain-JEPA** — *Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking*, NeurIPS 2024. JEPA applied to fMRI; predicts latent representations rather than raw voxels.
  [arXiv:2409.19407](https://arxiv.org/abs/2409.19407) · [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9c3828adf1500f5de3c56f6550dfe43c-Abstract-Conference.html) · [code](https://github.com/HEEHWANWANG/Brain-JEPA)

### Emergent communication (artificial agents)
- **Taniguchi, Taniguchi, et al.** — *Emergent Communication through Metropolis-Hastings Naming Game with Deep Generative Models*, Advanced Robotics 2023 / Frontiers in Robotics and AI 2023. Collective-predictive-coding framing of emergent symbol formation as decentralized Bayesian inference.
  [arXiv:2205.12392](https://arxiv.org/abs/2205.12392) · [Frontiers](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2023.1290604/full)
  - ⚠️ The critique doc's Task 2 table title ("Generative Emergent Communication") more closely matches a *different*, related 2025 paper by an overlapping author group: *Generative Emergent Communication: Large Language Model is a Collective World Model*, [arXiv:2501.00226](https://arxiv.org/pdf/2501.00226). Worth checking both — the critique doc may have conflated the two.

### Cross-individual alignment (non-human, methodologically relevant)
- **"Cross-individual translation of spontaneous zebrafish brain activity through a shared latent representation"** (Latent-Aligned Restricted Boltzmann Machines), PNAS 2026. Unsupervised shared latent space translating whole-brain calcium imaging between different zebrafish, no neuron-to-neuron correspondence needed. ⚠️ Cited as "van der Plas et al." in the critique doc — not confirmed from search snippets.
  [PNAS](https://www.pnas.org/doi/10.1073/pnas.2529064123) · [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.01.09.698719v2.full)

---

## Note on the ⚠️ flags

A handful of author names in the original pasted critique document (Barda, Barmpas, van der Plas) didn't turn up in the actual search results for their papers — the paper topics, venues, and years check out as real, findable work, but I couldn't verify those specific author names are correct. Worth a two-minute check against the actual arXiv listing pages before citing any of these in `paper/references.bib`.

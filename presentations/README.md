# 🎙️ Presentations, Decks & Explainers

What's actually here:

| File | What it is |
| :--- | :--- |
| `pitch.tex` / `pitch.pdf` | **The pitch**, 6 pp, typeset. General audience — the Clever Hans framing, the zero-bottleneck experiment, the numbers, what's open. Plain-Markdown twin lives at [`../pitch.md`](../pitch.md). |
| `build_explainer.py` | Generates `Computational_Coupling_Explained.pdf`. |
| `Computational_Coupling_Explained.pdf` | Longer visual explainer. |
| `review1_deck.pptx` | Review 1 deck, 2026-08-14. |

## Building the pitch

```bash
cd presentations
pdflatex pitch.tex && pdflatex pitch.tex   # twice, for the TOC
```

Current build: 6 pp, 0 overfull boxes. No bibliography, so no bibtex pass needed.

## Which one to hand someone

- **Two minutes, non-technical** → the one-sentence version at the end of [`../pitch.md`](../pitch.md).
- **Ten minutes, curious** → `pitch.pdf`.
- **They want the argument** → [`../opp.md`](../opp.md).
- **They want the proofs** → [`../paper_main/main.pdf`](../paper_main/main.pdf).

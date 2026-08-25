# 🛠️ Development & Environment Setup

**Original File:** [`DEVELOPMENT.md`](file:///home/charizard/computational-coupling/DEVELOPMENT.md)

---

## 1. Prerequisites
- **Python 3.10+** (Python 3.11/3.12 recommended)
- **LaTeX Distribution:** `pdflatex`, `bibtex`, `texlive-latex-extra`
- **Git** & **Git LFS**

---

## 2. Environment Setup
```bash
# Activate existing virtual environment
source .venv/bin/activate

# Core requirements installed:
# torch, numpy, scipy, matplotlib, pettingzoo, mpe2, gymnasium
```

---

## 3. Paper Compilation Commands
```bash
# Compile Paper 1 (v0.3.0)
cd paper_main && ./build.sh

# Compile Paper 2 ("Understanding Is Not Observable")
cd paper2 && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

# 🛠️ Development & Environment Setup

Yo! Here is how to get your local environment running for the **Computational Coupling** repo.

---

## 1. Prerequisites

Make sure you got these installed on your machine:
* **Python 3.10+** (Python 3.11 / 3.12 recommended)
* **LaTeX Distribution:** TeX Live / `pdflatex` / `bibtex`
* **Git** & **Git LFS** (for tracking datasets and checkpoints)

---

## 2. Environment Setup

```bash
# Clone the repo
git clone https://github.com/ashokpasala/computational-coupling.git
cd computational-coupling

# Create venv
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip & install core packages
pip install --upgrade pip
pip install torch numpy scipy matplotlib pettingzoo gymnasium docx reportlab
```

---

## 3. Compiling the LaTeX Paper (`paper/`)

The paper source is modularized under `paper/`. You can compile it using python or `pdflatex`:

```bash
# Method A: Python compiler script
python3 paper/compile_paper.py

# Method B: Direct pdflatex command inside paper/
cd paper/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The output PDF is automatically updated at `paper/output/paper.pdf`!

---

## 4. Running Paper 1 RL Experiments (`experiments/paper1_rl/`)

```bash
cd experiments/paper1_rl/
python run_bandwidth_sweep.py --env simple_speaker_listener_v4 --seed 42
```

---

## 5. Working with Overleaf

To sync this repo with Overleaf:
1. Go to Overleaf -> New Project -> Import from GitHub.
2. Select `ashokpasala/computational-coupling`.
3. Set **Root Document** in Overleaf settings to `paper/main.tex`.
4. Edit anywhere — local VS Code or Overleaf — push/pull without breaking anything!

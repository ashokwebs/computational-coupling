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
pip install torch numpy scipy matplotlib pettingzoo mpe2 gymnasium docx reportlab
```

---

## 3. Building the Paper (`paper_main/`)

There is one paper: `paper_main/main.tex`. Build it with the script, which runs the full
`pdflatex → bibtex → pdflatex ×2` cycle and then reports page count, overfull boxes and
undefined references:

```bash
cd paper_main && ./build.sh
```

Expected output:

```
built: .../paper_main/main.pdf
  pages:     36
  overfull:  0
  undefined: 0
```

If `overfull` or `undefined` is anything other than `0`, fix it before committing. The PDF is
tracked in git — it is the deliverable — but all the `.aux`/`.bbl`/`.log`/`.out` build noise is
gitignored.

Doing it by hand is equivalent:

```bash
cd paper_main/
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

> **Note:** `paper/` and `paper2/` no longer exist. They were merged into `paper_main/` on
> 2026-08-25 and deleted; recoverable from git history at commit `94eca22` if needed.

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
2. Select `ashokwebs/computational-coupling`.
3. Set **Root Document** in Overleaf settings to `paper_main/main.tex`.
4. Edit anywhere — local VS Code or Overleaf — push/pull without breaking anything!

The paper needs `texlive-latex-base texlive-latex-recommended texlive-latex-extra
texlive-fonts-recommended`. Overleaf has all of them. Locally on Debian/Ubuntu:

```bash
sudo apt-get install -y texlive-latex-base texlive-latex-recommended \
                        texlive-latex-extra texlive-fonts-recommended
```

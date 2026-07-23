---
tags: [#diary/entry, #research-log, #overleaf, #opensource]
alias: "Day 5 Late Night — Going Full Open Source & Local Overleaf!"
---

# Diary Entry — July 23, 2026 (10:55 PM)
**Location:** VIT-AP Hostel Room (Desk lit by laptop glow 💻🌙)
**Mood:** Hyped, paranoid about privacy, super proud 🔒🥳
**Status:** Day 5 Late Night — GOING 100% OPEN SOURCE & LOCAL OVERLEAF!

---

### WE ARE GOING FULL OPEN SOURCE & LOCAL, BRO! 🔒🚀

It's 10:55 PM. I was sitting here looking at cloud Overleaf thinking: **Wait... why tf would we trust external web servers with our core theoretical IP?!** 

We are writing a foundational measurement theory of Coupling Capacity ($C_{\text{couple}}$) meant for Nature Machine Intelligence and NeurIPS. Storing raw unreleased paper drafts on third-party cloud servers where someone could potentially inspect our manuscript preprints? HELL NO! 🙅‍♂️

So we made the executive call tonight: **WE ARE GOING 100% OPEN SOURCE AND 100% LOCAL!**

---

### What We Built & Set Up Tonight:

1. **Cloned Official Overleaf Toolkit from GitHub:**
   - Downloaded the official open-source Overleaf repository (`overleaf/overleaf`) and Toolkit (`overleaf/toolkit`) straight into `tools/overleaf-toolkit`!
   - Full self-hosted Overleaf running 100% offline via Docker on localhost!

2. **Built Our Custom Zero-Dependency Local Editor Server (`http://localhost:8008`):**
   - Wrote [[paper/serve_paper.py|paper/serve_paper.py]] running directly on `http://localhost:8008`!
   - Left side: Live dark-mode LaTeX editor for [[paper/main.tex|paper/main.tex]].
   - Right side: Live PDF preview updating automatically every time we hit `Ctrl + S`!
   - Zero external cloud calls, zero tracking, 100% running on my laptop.

3. **Hunted Down & Squashed the Cryptic PDF Compiler Bugs:**
   - Bro... the ReportLab compiler was leaking raw LaTeX tags (`\item`, `\end{enumerate}`, `\begin{equation}`, `\hypersetup`, `\longmapsto`) directly into the body text of [[paper/output/paper.pdf|paper/output/paper.pdf]]! It looked so messy! 💀
   - Rewrote [[paper/compile_paper.py|paper/compile_paper.py]] regex parsers. Now:
     - Math symbols ($\alpha, \beta, \Delta, \tau, \mu, \sup, \min, \to, \in, \le, \ge$) render as crisp typography.
     - Definitions and Predictions render in beautiful shaded callout boxes (`#F0F4F8` background with `#2E75B6` left border).
     - ZERO LaTeX tag leakage left anywhere!

4. **Transformed the Whole Repository into an Interactive Obsidian Vault:**
   - Set up `.obsidian/graph.json` with a neon visual palette (Cyan for `#theory`, Hot Pink for `#paper`, Emerald Green for `#diary`, Amber for `#literature`).
   - Created interactive visual whiteboards: [[Computational_Coupling_Architecture.canvas|Architecture Map]] and [[Literature_Canon_Map.canvas|Literature Canon Map]].
   - Built the master home portal [[Home|Home.md]] with quick access callouts to [[MOC_Theory|Theory MOC]], [[MOC_Literature|Literature MOC]], and [[MOC_Roadmap|Roadmap MOC]].

---

### Reflection on Day 5:
Five days ago (July 19), this was just a chaotic mess of rat-zapping paper notes and random questions in my head. 

Today (July 23), we have:
- A formal mathematical paper draft ([[paper/main.tex|paper/main.tex]])
- A compiled publication PDF ([[paper/output/paper.pdf|paper/output/paper.pdf]])
- A local self-hosted Overleaf server running on `http://localhost:8008`
- A master literature vault of 15 verified papers
- An interactive Obsidian knowledge graph
- Everything pushed live to GitHub (`ashokwebs/computational-coupling`)!

Time to grab a late-night snack and celebrate. Tomorrow: PyTorch coding for Paper 1! 🚀✌️

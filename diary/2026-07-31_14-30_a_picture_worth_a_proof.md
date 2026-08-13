---
tags: ["#diary/entry", "#research-log", "#paper2/exposition", "#writing"]
alias: "2026-07-31_14-30_a_picture_worth_a_proof"
---

# Diary Entry — July 31, 2026 (2:30 PM)
**Location:** VIT-AP Hostel Room
**Mood:** Calm, tidying-up energy 🧹
**Status:** Day 12, part four. Asked to make the theory clearer — did an exposition pass, no new claims.

---

Different kind of task than the rest of today. Not a new result, not a new experiment — just went back through Sections 2–4 of `paper2/main.tex` (Setup, Non-identifiability, Identification) and fixed the places where the formalism outruns the intuition.

The biggest one: $C$, the shared-convention latent, shows up for the first time inside Theorem 1's proof with no warning — "Let $C \sim \mathrm{Uniform}\{1,\dots,K\}$..." — even though the whole informal argument in §3.1 has already been leaning on it by name for a paragraph. A reader hits the proof and has to backtrack to figure out where this symbol came from. Fixed by flagging $C$ in the Setup section, right after the Dyad definition, as "not part of the tuple, precisely because it is generally unobserved" — so it's introduced as a concept before it's introduced as notation.

Then I drew the picture that should have been in the paper from the start. Two tiny causal diagrams, side by side: $C \to M \to U$ for the genuinely coupled dyad, versus $C \to M$ and $C \to U$ as two separate arrows (with a dotted "correlated, not causal" link between $M$ and $U$) for the confounded one. That's the entire theorem in one glance — mediation versus common cause — sitting right before the formal statement instead of only existing as prose the reader has to simulate in their head. TikZ, not hard to build, but it's the kind of thing that's easy to skip when you're deep in proving something and forget the reader hasn't been living inside the construction with you for three days.

Small stuff after that: a one-line plain-English gloss on Theorem 2's three identification conditions ("you can see the confounder and adjust for it; you can find something that jitters the message for reasons unrelated to the convention; or you can just set the message yourself") right where the formal statement would otherwise hit a reader cold. And a clause explaining what the front-door criterion actually requires, the first time Proposition 3 invokes it, for anyone who doesn't have Pearl's identification toolkit memorized.

Recompiled — 16 pages now, up from 15, entirely from the figure and the glosses. Nothing in the actual claims changed; this was purely "can a reader follow this without already knowing where it's going," which is a different kind of correctness than the theorem being true, and worth checking on its own.

Four things closed today: the novelty check, noise-as-instrument, the BBI survey, and now this. Genuinely productive Day 12. Stopping here.

Signing off. ✌️

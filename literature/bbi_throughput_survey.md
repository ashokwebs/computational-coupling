---
tags: ["#literature/survey", "#paper2/retrodiction", "#bbi-throughput"]
alias: "BBI Throughput Survey — checking the retrodiction against real numbers"
---

# BBI Throughput Survey

**Date:** 2026-07-31
**Purpose:** `paper_main/main.tex` §`sec:bbi` claims the framework retrodicts a decade-long stagnation in brain-to-brain interface (BBI) throughput despite large hardware gains, citing only Rao (2014) and Jiang (2019) by name and no numbers. `handoff.md` §5.6 and the Limitations section (§9) both flag this as asserted, not tabulated, and as "the section to cut first if the paper needs shortening" if it turns out throughput actually tracks hardware. This is that tabulation.

**Method:** literature search (WebSearch/WebFetch) for direct human-to-human brain-to-brain interface (B2BI/BBI) studies — not general BCI, not human-to-animal — spanning the field's ~decade of existence (2014 onward), with electrode counts and any reported information-transfer figures. Cross-checked against a 2021 PRISMA systematic review of the whole B2BI literature (Ge et al./Frontiers in Neurorobotics) for coverage.

---

## 1. The two anchor studies, with real numbers

| | **Rao et al. 2014** | **Jiang et al. 2019 (BrainNet)** |
|---|---|---|
| Recording (sender) | 64-channel Ag/AgCl EEG cap | 3 electrodes (Oz + AFz/FCz ref/ground) off an 8-channel OpenBCI system — **1 active channel** |
| Recording (receiver) | — | 32-channel headcap, but again **only the Oz channel used** |
| Stimulation | 1× 90mm MagStim TMS coil, motor cortex | TMS, phosphene induction, visual cortex |
| Participants | 3 pairs (6 subjects) | 5 triads (15 subjects) — first multi-person (2 senders : 1 receiver) |
| Trials | 10–16 per block | 16 per session |
| Accuracy | 83.3% / 25.0% / 37.5% (per pair) | 81.25% mean; AUC 0.83 |
| **Information transferred** | **0.25–0.81 bits/trial** (≈4–13 bits per experimental block, Table 3 mutual information) | **0.336 bits** (best sender) / **0.051 bits** (worst sender) — mutual information per sender-receiver pair |
| Per-trial timing | ~650ms transmission, ~22s total per trial (setup + countdown) | not reported |

**The headline comparison:** five years, one added participant, and a jump from single-sender binary decisions to a real-time multi-sender collaborative architecture — and the best-case information transferred *per trial* went from Rao's 0.81 bits down to Jiang's 0.336 bits. Electrode count nominally available went up (64→32 for the more advanced system's receiver) but the number of channels actually *used* for the transmitted signal went from a full 64-channel decode down to a single electrode (Oz). More hardware was deployed to do less decoding, not more.

## 2. The field's own assessment (primary source, not our inference)

Jiang et al. 2019, Discussion section, quoted directly (PMC6467884):

> "From the first human BBI to BrainNet, the level of information complexity has remained binary, i.e., only a bit of information is transmitted during each iteration of communication."
>
> "Additionally, this low bit rate required a disproportionate amount of technical hardware and setup."

This is the field's own retrospective on itself, five years after the first study, written by the team that built the most technically advanced system in the lineage. It is close to a verbatim statement of `paper2/main.tex`'s retrodiction — hardware scaled, throughput didn't — from inside the field, not from us.

## 3. Broader coverage — the 2021 PRISMA systematic review

Ge, Bin (2021), *Direct Communication Between Brains: A Systematic PRISMA Review of Brain-To-Brain Interface* (Frontiers in Neurorobotics), catalogs every B2BI study 2013–2020 (human and animal). Relevant findings for the retrodiction:

- Across the full 2013–2020 span (Pais-Vieira 2013 → Rajesh et al. 2020), the review finds **no documented throughput/bit-rate improvement across studies** — it reports methodological diversification (different recording modalities: EEG, intracortical microelectrodes, transcranial focused ultrasound; different stimulation modalities: TMS, ICM, tFUS, optogenetics) but not increased information transfer.
- Direct quote: **"MI has been limited to mostly binary information transfer"** across the review period.
- The review's own conclusion hedges toward the hardware-solves-it framing our paper argues against: "As BCI technology becomes more capable of recording nuanced brain activity and CBI technology more precise at stimulating the brain, it becomes more possible to transmit complex information" — asserted, not evidenced by any study in the review's own table.
- No bidirectional *and* multi-person system has been built; every study remains structurally close to Rao's original one-bit paradigm.

## 4. What a follow-up search for 2021–2026 turned up

No new human-to-human direct BBI study with a reported throughput figure surfaced in a general search for 2021–2024 work. The most recent item found (Rajesh et al. 2020) adds edge-computing infrastructure for a stroke-rehabilitation use case, with no throughput claim at all. **This is an absence-of-evidence, not evidence-of-absence** — it means no *documented improvement* was found, not that no further study exists; a more exhaustive search (Scopus/Web of Science rather than general web search) would be needed before citing this as a confirmed continuation of the plateau through 2026.

## 5. Verdict on the paper's retrodiction

**Supported, with two caveats worth stating plainly in the paper.**

Supported: the two best-documented anchor studies, five years apart, show throughput *within the same order of magnitude* (both well under 1 bit/trial) despite one of them being a materially more sophisticated multi-person real-time system, and the authors of the more advanced system say so explicitly in their own words. The systematic review's independent read of the whole 2013–2020 literature agrees: methodology diversified, bit rate did not detectably rise.

Caveats:
1. **N=2 studies with hard numbers.** Everything else in the table is presence/absence of a bit-rate claim (usually absence), not a second and third quantified data point. The claim rests on Rao and Jiang plus the review's qualitative read, not on a dense time series.
2. **This is human-to-human BBI specifically**, a narrow slice of the broader BCI field (which does show real ITR gains over the same period in other contexts — consumer/clinical BCI spellers, assistive devices). The paper's claim is scoped correctly to BBI in `main.tex`, and this survey doesn't test the wider BCI field, which is a different (and much better resourced) technology base.

**Recommendation:** upgrade `main.tex` §`sec:bbi` from an assertion to a cited, numbered claim using the table and the Jiang et al. quote above, and soften the Limitations §9 caveat from "the retrodiction may be overfitted... asserted after the fact" to something that reflects it now has two real anchor points and the field's own words behind it, while still flagging the N=2 and general-web-search-only caveats honestly.

---
tags: ["#diary/entry", "#research-log", "#paper2/retrodiction", "#bbi-throughput", "#literature-survey"]
alias: "2026-07-31_13-15_the_hardware_went_backwards"
---

# Diary Entry — July 31, 2026 (1:15 PM)
**Location:** VIT-AP Hostel Room
**Mood:** Delighted, slightly stunned 🤯
**Status:** Day 12, part three. "Bring more research" — did the BBI throughput survey.

---

### The retrodiction that was just sitting there unverified

`paper2/main.tex` §`sec:bbi` has claimed, since the reframe, that brain-to-brain interface throughput has been stuck "on the order of a bit per trial for a decade despite very large gains in electrodes, channel counts, signal quality, and decoding." It cited Rao (2014) and Jiang (2019) by name and gave zero numbers. Both the risk register and the limitations section flagged this honestly as the weakest-sourced claim in the paper — "the section to cut first if it needs shortening" — and said explicitly: if throughput turns out to track hardware, the retrodiction fails.

So I went and actually pulled the numbers instead of leaving it as a plausible-sounding assertion.

### What I found

Rao et al. 2014: 64-channel EEG on the sender, one TMS coil, three pairs of subjects, and — buried in Table 3 — 0.25 to 0.81 bits of mutual information per trial.

Jiang et al. 2019, BrainNet: five years later, a genuinely more sophisticated system — real-time, three people instead of two, two senders voting through one receiver. I expected the bit rate to have grown, even modestly. It didn't. Best sender: 0.336 bits per trial. **Lower** than Rao's best pair, despite the extra half-decade and the added architectural complexity. And the reason became obvious once I checked the electrode counts: BrainNet's senders had an 8-channel headset and the receiver had 32 channels available, but the paper only ever decodes from a single electrode, Oz, on each. All that additional hardware, and the actual channel being read from didn't grow at all.

Then I found the sentence that made the whole afternoon worth it. It's not something I inferred — it's the BrainNet authors, in their own Discussion section, about their own field:

> "From the first human BBI to BrainNet, the level of information complexity has remained binary... this low bit rate required a disproportionate amount of technical hardware and setup."

That is, almost word for word, the paper's own retrodiction — except it's not our claim about their field, it's their claim about their field, five years in, from the team that built the most advanced system in the lineage. I went and cross-checked against an independent 2021 PRISMA systematic review of the whole 2013–2020 literature, and it says the same thing in its own words: mutual information "has been limited to mostly binary information transfer" across every study it catalogs, methodology diversifying (EEG, intracortical electrodes, focused ultrasound, optogenetics) without throughput ever detectably rising.

### What I didn't do

I didn't stretch this into more than it is. Two hard numeric data points, five years apart, is not a dense time series — I said so directly in both the survey doc and the paper's limitations section. I searched for 2021–2026 follow-up work and found nothing with a reported bit rate either way, which I logged as absence of evidence, not evidence of continued stagnation — a more careful database search (Scopus, not general web search) would be needed before leaning on that gap. And the claim is scoped correctly to brain-to-brain interfaces specifically, not the much better-resourced BCI field generally, which does show real throughput gains over the same period in other applications (spellers, assistive devices) — different technology base, not a counterexample.

Updated `paper2/main.tex` §`sec:bbi` with the actual numbers and the direct Jiang et al. quote, softened the limitations caveat to reflect that this is now evidenced rather than merely asserted (while keeping the N=2 honesty), added the systematic review to `references.bib`, recompiled — 15 pages now, still clean. Full sourcing in `literature/bbi_throughput_survey.md` for whoever wants to check my work.

Three handoff research debts closed today: the novelty check this morning, noise-as-instrument mid-morning, and this one after lunch. The two structural things left — the referee read and the human-AI experiment — both need something this session doesn't have: distance from the paper, or an API key. Good day to stop pushing and let the next session bring fresh eyes to the one that's left.

Signing off — Day 12, part three, and I think that's enough for one day. ✌️

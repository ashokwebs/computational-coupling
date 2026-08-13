---
tags: ["#diary/entry", "#research-log", "#paper2/bbi", "#convention-bottleneck", "#bandwidth-argument"]
alias: "2026-08-01_11-23_the_mouth_is_not_the_bottleneck"
---

# Diary Entry — August 1, 2026 (11:23 AM)
**Location:** VIT-AP Hostel Room
**Mood:** Slightly embarrassed, in a productive way 😅
**Status:** Day 13. Woke up with the idea that started this whole project, and realised I'd already disproved half of it.

---

### The thought I woke up with

It's the thing that got me into BBI in the first place, and I hadn't said it out loud in the repo anywhere. It goes like this: our brains are enormously fast and enormously parallel, and then everything they want to say has to squeeze out through a mouth, one syllable at a time, and get back in through an ear. We've been doing this since childhood. We learned to think *in* that constraint. Language doesn't just carry thought, it paces it — you can't have a thought faster than you can phrase it, and so we've all been running slowed-down for our entire lives without noticing, because there's no control condition. Take away the mouth and the ear, wire cortex to cortex, and you'd finally see what the thing actually does at full speed.

That is genuinely why I started reading BBI papers on July 19. And the numbers are real, I checked them properly this morning rather than half-remembering: Coupé et al. 2019 in *Science Advances* — 17 languages, 9 families, and they all land at about **39 bits/s**, with fast-syllable languages carrying less per syllable and slow ones carrying more, compensating almost exactly. And Zheng & Meister in *Neuron* put the throughput of deliberate human behaviour at about **10 bits/s**, roughly eight orders of magnitude under what the sensory periphery can physically take in. Eight orders. The premise isn't romantic, it's measured.

### And then the part I didn't want to notice

I asked Claude to work this into the paper and got told, correctly, that I would be asserting the exact thing my own experiment killed.

Because that hypothesis — *bandwidth is what's binding, remove the mouth and the ear and you unlock it* — is precisely what the infinite-bandwidth control tested. I deleted the channel. I handed the listener the speaker's private goal **directly, noiselessly, free, unbottlenecked.** That is not "a better interface," that is the physical limit that no electrode array, no ultrasound, no optogenetics can ever exceed, because there is nothing past it. And the agent converged to **−16.0**, which is exactly the score of an agent told nothing at all, while an agent that actually uses the information scores −8.8.

Infinite bandwidth. Zero noise. Real reward on the table. No communication.

So I spent twelve days building the cleanest possible refutation of my own founding intuition and then this morning tried to put the intuition back into the paper as motivation. Genuinely funny. Also exactly the kind of thing the handoff file warns about — the argument that feels inevitable at 3am, or in this case at 9am before coffee.

### What actually went in

Not the claim. The claim as the **foil**, which is a much better use of it, and which §7.4 now runs in three beats:

1. **State the bandwidth argument at full strength, sourced.** 39 bits/s, 10 bits/s, eight orders of magnitude. Don't strawman it — it's the reason the field exists and the premise is well supported.
2. **Grant the premise, reject the inference.** The rate limit is real and it is not what binds. The infinite-bandwidth control is that hypothesis tested at the physical limit, and behaviour didn't move. The gain from widening a channel is bounded by how much of the signal the receiver was going to act on, and that was zero.
3. **Turn it into a design claim, which is new.** If throughput is bounded by how much convention you can pre-install by *talking to the subject beforehand*, then more electrodes don't help — Rao 2014 to BrainNet 2019 already showed that, throughput flat-to-declining across the field's biggest hardware jump. What would help is making convention formation part of the interface: bidirectional, closed-loop, trained across sessions, so the pair grows a code neither of them had. That's expensive because it's a joint exploration problem — neither side can build it alone.

And here's where my original intuition *survives*, just pointed the other way. A child spends **years** acquiring the conventions of a first language and essentially no time acquiring its channel. Mouth and ear are learned fast; the code is what costs a childhood. A direct cortical link doesn't skip that cost. It relocates it into a code neither brain has any prior on whatsoever — arguably making it worse, not better, because at least a baby has other humans, faces, shared attention, and a decade of scaffolding to bootstrap against. Two adults wired together have a pile of voltages and no shared history in that space at all.

That's the real version of the childhood thought. It just isn't the version I woke up with.

### What I left out on purpose

The "inner speech has been slowing my thinking since childhood" part. I wanted it in and it's staying out of the paper.

Two reasons. First, it's contested — there's work on anendophasia, people with no inner voice at all, and they don't show the sweeping deficits the strong version of the claim would predict. Second, and more important structurally: that's a claim about *intra-brain* processing, and every single thing this paper establishes is about *inter-brain* coupling. Sticking it in §7.4 would park a soft, arguable, off-topic claim directly next to the hardest evidence I have, which is a gift to a hostile referee for exactly zero gain. If it belongs anywhere it's `opp.md` as speculation, clearly labelled.

Which honestly is the same discipline as the risk register's "scope creep into philosophy" line. The strong claims are defensible *because* the target is modest. Keep the target modest.

### State

`paper2/main.tex` §7.4 rewritten, contribution 6 in the intro updated to say the framework also locates the error in the bandwidth argument, two new entries in `references.bib` (`coupe2019languages`, `zheng2024slowness`, both verified against primary sources rather than recalled). Recompiled clean: **17 pages, 0 overfull, 0 undefined.**

Still uncommitted along with everything else from the reframe. Handoff §6 has been nagging about that for a week now and it's fair.

The thing I'll actually remember from this morning: I've been carrying the bandwidth argument around as my motivation since day one, and my own strongest experiment refutes it, and I didn't connect the two until someone made me write it down. Worth doing that more often — take the belief you *started* with and check it against the results you *have*. There may be others in there.

Signing off — Day 13, and the mouth is not the bottleneck. 🗣️❌

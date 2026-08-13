---
tags: [#meta/pitch, #audience/general]
alias: "The Pitch — Understanding Is Not Observable"
---

# Can you actually tell if someone understands you?

Not "do they seem like they understand you." Actually.

Here's a strange fact to start with: a horse named Clever Hans could supposedly do arithmetic. Ask him "what's 4 plus 3?" and he'd tap his hoof seven times and stop. Crowds came to watch. Scientists tested him and couldn't catch him cheating — until someone thought to ask the question *without letting the horse see the questioner know the answer*. Hans stopped getting it right immediately. He was never doing math. He was reading tiny, unconscious relaxation cues in the human's posture the instant he reached the correct tap count. Everyone watching — including, for years, the scientists — had been fooled by something that looked exactly like understanding and wasn't.

That's the whole project, basically. We found a modern, precise, provable version of the Clever Hans problem, and it's much bigger than a horse.

## Where it started

The idea was simple and, honestly, kind of exciting: your brain thinks incredibly fast. But to tell anyone anything, you have to squeeze it out through your mouth, one word at a time — something like 40 bits of information per second, max, while your brain is arguably doing a billion times that internally. Speech is a straw. What if you could connect two brains directly and skip the straw entirely?

That was the pitch. Build a direct brain-to-brain link, remove the bottleneck, watch two minds finally talk at full speed.

## The experiment that ruined that idea, in the best way

We built a small test version first — not real brains yet, two AI agents in a simulation, one that knows something useful, one that needs to act on it, connected by a channel we fully control. Standard setup.

Then we ran the most extreme version of "remove the straw" that's physically possible: we didn't just widen the channel, we deleted it. We took the first agent's private information and handed it straight to the second agent — free, instant, perfect, zero bottleneck of any kind. The absolute best any interface could ever theoretically do.

Its behavior didn't change. At all. It performed exactly as if it had been told nothing.

That's not a small result. That means the straw was never the problem. We built the physically ideal version of the "wider pipe" fix, at zero cost, and it did nothing. So the entire premise — that connection is what's missing — turned out to be wrong. Something else was going on.

## What was actually going on

Here's the thing that took us a while to see clearly: two systems can only really communicate if they already agree, in advance, on what signals mean. Not the channel — the *code*. A word only works because you and I already agreed, long before this sentence, on roughly what it points to. That agreement is the actual thing doing the work. The channel is just the delivery truck.

And once you see that, something uncomfortable follows: if the agreement is what makes communication work, the agreement is also the thing that makes it *impossible to check from outside* whether real communication is happening at all. Because two systems that are genuinely paying attention to each other's specific signal, and two systems that are each just fluently running the same shared code on autopilot — without either one actually being moved by the other, right now, in this moment — look *identical* from the outside. Same brain-scan patterns. Same measured "understanding." Same everything you could observe.

We didn't just argue this. We proved it, and then we built a system where you can watch it happen with real numbers: an AI receiver whose internal state contained its partner's private information almost perfectly — you could read it right out of its "brain" — while its actual behavior used essentially none of it. Perfect understanding by every test anyone currently uses. Zero actual understanding underneath. Same Clever Hans problem, but now with a number attached, and now we know exactly why it happens instead of stumbling onto it by accident a century later.

## Why this isn't just a cute finding

It turns out this exact blind spot is quietly built into how several entire fields check understanding right now:

- **AI companies test chatbots by watching them talk.** If "looks right" and "actually tracking what you meant" are indistinguishable from the outside — which is what we showed — then a huge amount of AI evaluation is testing the wrong thing, the same way everyone testing Clever Hans by watching him tap was testing the wrong thing.
- **Neuroscientists measure "brain synchrony" between two people and call it connection.** Same blind spot. Synchronized brain activity and real, functioning understanding are not the same measurement, and nobody had a clean way to tell them apart.
- **It even explains a real, decade-old mystery.** Brain-computer interface hardware got dramatically better between 2014 and 2019 — and the amount of actual information people could send through it went *down*, not up, and the researchers themselves said so in their own papers without knowing why. Once you know the bottleneck was never the hardware, that stops being a mystery.

## The fix, in plain terms

You can't find this by watching. You have to poke it. Take the signal away, or scramble it, and see if behavior actually changes. If it does — real communication was happening. If it doesn't — you had the Clever Hans version the whole time, no matter how convincing it looked. That's a test anyone can run, on an AI system, on hyperscanning data neuroscientists already have sitting around, on almost anything two-sided.

## The numbers, for anyone who wants to check the story instead of just hearing it

- Receiver's internal state contained the partner's private information almost perfectly: reconstruction error **0.0017** — essentially a perfect read.
- The receiver's actual behavior, same system, same moment: statistically identical to being told nothing at all.
- The zero-cost, infinite-bandwidth, zero-noise hand-over-the-information-directly test: score **−16.0**, exactly matching an agent given no information whatsoever, against **−8.8** for an agent that actually uses what it's given. Real reward on the table, real gap in performance, and the "better channel" fix changed nothing.
- Randomizing a signal turned out to be roughly **3x more sensitive** than simply removing it, as a way of testing whether it's doing anything — a smaller, independently useful finding on the way to the bigger one.
- Brain-computer-interface hardware: from 2014 to 2019, electrode counts and sophistication went up substantially. The actual amount of information transmitted went from roughly 0.25–0.81 bits per trial down to 0.336 bits per trial — worse, not better, and the researchers said so themselves in their own paper without an explanation for why.

## So how much faster could this actually get?

This is the question everyone asks, so here's the honest version of the answer, in one number and one caveat that has to travel with it.

**The number.** The raw physical gap between what a brain takes in and what it puts out is enormous: roughly a billion bits a second at the senses, versus roughly ten bits a second in deliberate behaviour. That's about eight orders of magnitude — up to a **hundred-million-fold** difference between what's theoretically available and what actually gets used. That's the number that has quietly motivated a decade of brain-interface research, whether anyone said it out loud or not.

**The caveat, and it's the whole point of this project.** We ran the most direct test of that gap that is physically possible: handed a receiving system its partner's information directly, no channel, no bottleneck, the literal best case an interface could ever achieve. It captured **zero percent** of it. Not a small percentage — zero, statistically, measured. So the honest answer to "how much faster could removing the mouth make us" isn't a number above zero. It's zero, because the mouth was never what was limiting it.

**What's actually still open.** Whether a *different* kind of gain is available — not from widening the channel, but from building an interface that grows a shared convention between two systems over time, instead of assuming one already exists. Nobody has measured how much of that hundred-million-fold gap that could recover, because nobody has built and tested that interface yet. That's a real, open, genuinely exciting question. It is just a different question from "how much faster is a wider pipe," and treating the two as the same question is the exact mistake this whole project exists to correct.

## It's not just us noticing this

Since building this, we went looking for whether anyone else has independently run into pieces of the same picture. They have, from several different directions, without using this framing:

- A 2024/2025 *Neuron* paper (Zheng & Meister, Caltech) independently found human behavioral output tops out around 10 bits per second — nine orders of magnitude below what our senses take in — completely independent of any interface or hardware question.
- A 2026 peer-reviewed paper in the *Journal of Neural Engineering* argues, in mainstream brain-computer-interface research, that the field's real constraint is an "input/output disparity," not raw channel count — a different vocabulary for the same insight.
- A 2024 hyperscanning neuroscience paper found that "brain synchrony" between two people barely changes even when researchers directly control whether the two people are actually seeing the same information — independent evidence that the standard measurement really is as blind as this argues.

None of them assembled it into the same claim, and a real search for prior work making exactly this claim came back empty. But the fact that pieces of it keep turning up independently, in unrelated fields, is a good sign rather than a coincidence to explain away — it usually means a real pattern, not an invented one.

## What's proven and what isn't — because that line matters

Proven: the impossibility result, the working demonstration, why the gap exists, and that the fix works — including honestly showing where the fix itself hits a wall on a real system, not just the easy toy version.

Not yet done: running this exact test on a real AI talking to a real person. That's the next thing, it's cheap, and it's the difference between "an interesting argument" and "a result that changes how people evaluate AI."

## What happens next

The next step is small, concrete, and already fully designed: take a real AI system, have a person state something specific to it, then ask a follow-up request whose wording never changes — only what was actually said before it changes. Watch whether the AI's answer tracks what was actually meant, or only the shape of the sentence. Run that four ways — real, removed, swapped for a different but equally fluent statement, and one detail deliberately flipped — and score how much of the real gap between "ignores you" and "actually gets it" the system actually closes.

If the system tracks the real meaning: that's evidence the fluency is doing genuine work, in that case, and it narrows rather than breaks the theory. If it doesn't — if the response is just as good when the stated intent is swapped for a different one — that's the same Clever Hans gap, now shown in something people actually use every day, and it's the result that turns this from an argument into a warning worth acting on.

## The one-sentence version, if that's all there's time for

You cannot tell whether two systems understand each other by watching them — you can only find out by testing it — and almost nobody currently tests it that way.

"""
build_explainer.py
===================
Generates a plain-English explainer PDF for the Theory of Computational
Coupling — written for someone with zero background in neuroscience,
information theory, or ML. No equations beyond what's unavoidable, and
those are explained with an everyday analogy first.

Usage:
    python3 build_explainer.py
    # writes presentations/Computational_Coupling_Explained.pdf
"""

from __future__ import annotations
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle,
    ListFlowable, ListItem, KeepTogether
)
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PDF = os.path.join(HERE, "Computational_Coupling_Explained.pdf")

NAVY = colors.HexColor("#1F4E78")
STEEL = colors.HexColor("#2E75B6")
CORAL = colors.HexColor("#E05A47")
GOLD = colors.HexColor("#E0A82E")
GREEN = colors.HexColor("#3C8C5A")
INK = colors.HexColor("#222222")
MUTED = colors.HexColor("#5A5A5A")
PALE = colors.HexColor("#EEF3F8")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("DocTitle", fontName="Helvetica-Bold", fontSize=24,
                          leading=28, textColor=NAVY, spaceAfter=6))
styles.add(ParagraphStyle("DocSubtitle", fontName="Helvetica", fontSize=13,
                          leading=17, textColor=MUTED, spaceAfter=18))
styles.add(ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=15.5,
                          leading=19, textColor=NAVY, spaceBefore=18, spaceAfter=8))
styles.add(ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=11.5,
                          leading=15, textColor=STEEL, spaceBefore=10, spaceAfter=4))
styles.add(ParagraphStyle("Body", fontName="Helvetica", fontSize=10.3,
                          leading=15.2, textColor=INK, spaceAfter=8,
                          alignment=TA_LEFT))
styles.add(ParagraphStyle("CalloutLabel", fontName="Helvetica-Bold", fontSize=9.5,
                          textColor=NAVY, spaceAfter=2))
styles.add(ParagraphStyle("Callout", fontName="Helvetica", fontSize=9.8,
                          leading=14, textColor=INK))
styles.add(ParagraphStyle("Caption", fontName="Helvetica-Oblique", fontSize=8.7,
                          leading=12, textColor=MUTED))


class NumberedCanvas(canvas.Canvas):
    """Adds a running header/footer once total page count is known."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        n = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._decorate(n)
            super().showPage()
        super().save()

    def _decorate(self, page_count):
        self.saveState()
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(MUTED)
            self.drawString(54, 11 * 72 - 36, "Computational Coupling — Explained Simply")
            self.setStrokeColor(STEEL)
            self.setLineWidth(0.75)
            self.line(54, 11 * 72 - 40, 8.5 * 72 - 54, 11 * 72 - 40)
        self.setFont("Helvetica", 8)
        self.setFillColor(MUTED)
        self.drawRightString(8.5 * 72 - 54, 30, f"Page {self._pageNumber} of {page_count}")
        self.drawString(54, 30, "A plain-English guide, prepared 2026-07-25")
        self.setStrokeColor(colors.HexColor("#E0E0E0"))
        self.setLineWidth(0.5)
        self.line(54, 40, 8.5 * 72 - 54, 40)
        self.restoreState()


def callout(label: str, text: str, color=STEEL):
    """A shaded box for asides, analogies, and honesty checks."""
    label_p = Paragraph(f'<font color="{color.hexval()}">{label}</font>', styles["CalloutLabel"])
    body_p = Paragraph(text, styles["Callout"])
    t = Table([[label_p], [body_p]], colWidths=[6.4 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.75, color),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (0, 0), 8),
        ("BOTTOMPADDING", (0, 0), (0, 0), 2),
        ("TOPPADDING", (0, 1), (0, 1), 2),
        ("BOTTOMPADDING", (0, 1), (0, 1), 8),
    ]))
    return KeepTogether([Spacer(1, 4), t, Spacer(1, 8)])


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(it, styles["Body"]), leftIndent=6) for it in items],
        bulletType="bullet", start="•", leftIndent=14, spaceBefore=2, spaceAfter=8,
    )


def build():
    doc = SimpleDocTemplate(
        OUT_PDF, pagesize=letter,
        topMargin=0.9 * inch, bottomMargin=0.8 * inch,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
        title="Computational Coupling, Explained Simply",
        author="Ashok Pasala",
    )
    S = []

    # --- Cover -------------------------------------------------------------
    S.append(Spacer(1, 0.4 * inch))
    S.append(Paragraph("What Is the Theory of Computational Coupling?", styles["DocTitle"]))
    S.append(Paragraph(
        "A plain-English guide for someone who has never heard of any of this — "
        "no equations required, and the few numbers that show up are explained "
        "with an everyday comparison first.",
        styles["DocSubtitle"]))
    S.append(HRFlowable(width="100%", thickness=1.2, color=STEEL, spaceAfter=14))

    # --- 1. One paragraph ---------------------------------------------------
    S.append(Paragraph("1. The Whole Idea, in One Paragraph", styles["H1"]))
    S.append(Paragraph(
        "Two people (or two brains, or two robots, or two AI programs) are said to be "
        '"coupled" when knowing what one of them just did genuinely helps you predict '
        "what the other one is about to do — beyond what you could already guess from "
        "watching that second one alone. This project builds a precise, measurable "
        "way to quantify <i>how coupled</i> two systems are, given that they can only "
        "talk to each other through a limited channel (a narrow wire, a slow radio "
        "link, a small vocabulary). The eventual goal is a rigorous foundation for "
        '"brain-to-brain interfaces" — but the measurement idea itself works for any '
        "two intelligent systems, biological or artificial.", styles["Body"]))

    # --- 2. The problem ------------------------------------------------------
    S.append(Paragraph("2. The Problem This Is Trying to Fix", styles["H1"]))
    S.append(Paragraph(
        "Over the last ~15 years, a handful of experiments have connected two brains "
        "directly: a rat's brain signal triggering a stimulation in a second rat "
        "(2013), a person's EEG (“brainwave”) reading triggering a flash of light "
        "in someone else's vision via magnetic stimulation (2014), even a three-person "
        "brain network playing a simplified game of Tetris together (2019). These are "
        "real and impressive, but every one of them was built the same way: pick a "
        "narrow trigger, wire it up, see if it works. Nobody first asked the more basic "
        "engineering question:", styles["Body"]))
    S.append(callout("The missing question",
        "<i>What exactly are we trying to maximize?</i> Before you can build a good "
        "brain-to-brain link, you need a number that tells you whether one design is "
        "better than another — the same way an engineer needs to know a wire's data "
        "rate in bits-per-second before arguing about which cable to use.", CORAL))
    S.append(Paragraph(
        "Without that number, every BBI experiment is a one-off trick with no way to "
        "compare it to the next one, and no way to know if you're close to the best "
        "possible design or nowhere near it.", styles["Body"]))

    # --- 3. Shannon analogy ---------------------------------------------------
    S.append(Paragraph("3. Borrowing a 1948 Idea About Telephones", styles["H1"]))
    S.append(Paragraph(
        "In 1948, Claude Shannon solved the equivalent problem for telephone wires and "
        "radio: he defined <b>channel capacity</b> — the absolute maximum amount of "
        "information any signal can reliably carry down a given wire, no matter how "
        "clever the encoding scheme is. That single idea is why every modem, Wi-Fi "
        "router, and 5G tower since then has had a hard, calculable performance "
        "ceiling to engineer toward, instead of just guessing.", styles["Body"]))
    S.append(Paragraph(
        "This project asks the same question one level up: not “how many bits can "
        "flow down this wire,” but “how much does what flows down this wire actually "
        "change what the receiving brain (or agent) can predict about its own future "
        "state.” That quantity is called <b>Coupling Capacity</b>.", styles["Body"]))

    # --- 4. Coupling capacity --------------------------------------------------
    S.append(Paragraph("4. So What Is “Coupling Capacity,” Really?", styles["H1"]))
    S.append(Paragraph(
        "Imagine you're trying to guess what your friend will do in the next five "
        "seconds. You already know your friend pretty well, so you can guess a "
        "surprising amount just from their own recent behavior — that's your baseline. "
        "Now someone whispers you one extra piece of information about what a "
        "<i>third</i> person just did. If that whisper measurably sharpens your guess "
        "about your friend, beyond what you already knew, that whisper carried real "
        "coupling. If it doesn't sharpen your guess at all, it didn't — even if it was "
        "a long, detailed whisper.", styles["Body"]))
    S.append(Paragraph(
        "Coupling Capacity is that idea, made precise and pushed to its best case: "
        "<i>the most that any signal — sent through a channel of a given size — could "
        "possibly sharpen your prediction of the receiver's next state.</i> It rewards "
        "signals that are genuinely predictive, not just loud, long, or complicated.",
        styles["Body"]))

    # --- 5. Three predictions --------------------------------------------------
    S.append(Paragraph("5. Three Testable Claims", styles["H1"]))
    S.append(Paragraph(
        "A theory that can't be proven wrong isn't worth much. Here are the three "
        "concrete, checkable claims this one makes:", styles["Body"]))

    S.append(Paragraph("Claim 1 — More bandwidth stops helping past a point", styles["H2"]))
    S.append(Paragraph(
        "Giving two systems a bigger “wire” helps at first, but the benefit flattens "
        "out completely once the channel is wide enough. Past that point, the "
        "bottleneck isn't the wire anymore — it's how rich the <i>receiver's own "
        "internal model</i> is. A brilliant lecturer speaking into a phone that can "
        "carry unlimited audio still can't teach more to someone who's fallen asleep. "
        "The ceiling is set by the smaller of the two systems' own representational "
        "capacity, not by the size of the pipe between them.", styles["Body"]))

    S.append(Paragraph("Claim 2 — A sharper internal model gets more out of the same signal", styles["H2"]))
    S.append(Paragraph(
        "Two systems with the exact same channel can extract very different amounts "
        "of useful coupling from it, depending on how good each one already is at "
        "predicting its own future. This is like the difference between a radiologist "
        "and a first-year student looking at the exact same X-ray: same image, same "
        "“bandwidth,” wildly different amount of useful information extracted, "
        "because one of them has a far better internal model to interpret it with.",
        styles["Body"]))

    S.append(Paragraph("Claim 3 — Who's “leading” shows up as an asymmetry", styles["H2"]))
    S.append(Paragraph(
        "In any task with a leader and a follower — a tour guide and tourists, a "
        "speaker and a listener, a coach and a player — the coupling should be "
        "measurably lopsided: the leader's signal predicts the follower's next move "
        "far better than the reverse. This isn't assumed; it's something the theory "
        "says you should be able to measure directly and it should line up with who "
        "actually has the task role of “leader” in each case.", styles["Body"]))

    # --- 6. What's actually been tested -----------------------------------------
    S.append(Paragraph("6. What's Actually Been Tested So Far", styles["H1"]))
    S.append(Paragraph(
        "None of this has been tried on a real human brain yet. Before touching a "
        "single neuron, the very first step was to check the theory doesn't "
        "contradict itself, in a setting simple enough to know the exact right "
        "answer in advance.", styles["Body"]))
    S.append(Paragraph(
        "Two simple computer-simulated systems were built, connected through an "
        "artificial channel whose size could be dialed up and down by hand, with "
        "every other property (how “smart” each system was, how strongly they "
        "influenced each other) also set by hand. Because everything about this toy "
        "setup was already known exactly, it was possible to check the theory's three "
        "claims against ground truth, rather than against a noisy real-world signal.",
        styles["Body"]))
    S.append(callout("Result",
        "All three claims held up in this controlled test, and two completely "
        "different ways of measuring “coupling” (one a mathematical shortcut, one a "
        "brute-force statistical method) agreed with each other to within 2%. That's "
        "a solid sign the math is internally consistent — a necessary first hurdle, "
        "not proof it describes real brains yet.", GREEN))

    # --- 7. What's happening right now -----------------------------------------
    S.append(Paragraph("7. What's Being Built Right Now", styles["H1"]))
    S.append(Paragraph(
        "The hand-built toy system above proves the math is consistent, but it's an "
        "easy test — the systems were designed to match the theory. The next, harder "
        "step: take two small AI programs that don't know anything about this theory, "
        "put them in a simple cooperative game (one program, the “speaker,” knows "
        "the goal; the other, the “listener,” has to reach it, but only the speaker "
        "can see where to go), give them a communication channel of a fixed, small "
        "size, and let them <i>invent their own way of talking</i> through pure trial "
        "and error (reinforcement learning). Then check: does the same “bandwidth "
        "stops helping” pattern from Claim 1 show up naturally, even though nobody "
        "told the AI programs about the theory at all? That code was written and "
        "smoke-tested this week; a real multi-run experiment is in progress as this "
        "document is being generated.", styles["Body"]))

    # --- 8. Neuralink --------------------------------------------------------
    S.append(Paragraph('8. "Wait — Is This the Same Thing as Neuralink?"', styles["H1"]))
    S.append(Paragraph(
        "No, and the difference is worth being precise about, because it's a common "
        "mix-up.", styles["Body"]))
    S.append(bullets([
        "<b>Neuralink builds hardware.</b> It's a medical device company: implanted "
        "electrode arrays, surgery, FDA trials, aimed mainly at restoring function "
        "for people with paralysis (moving a cursor, eventually more). It answers "
        '"how do we build a better physical link into a brain?"',
        "<b>This project builds no hardware at all.</b> It's a mathematical "
        'measurement framework that asks "given any link at all — implanted chip, '
        'EEG cap, or even two AI programs talking to each other with no biology '
        'involved — how do we tell if it\'s being used well, and what\'s the best it '
        'could theoretically do?" It doesn\'t care what the wire is made of.',
    ]))
    S.append(Paragraph(
        "A simple way to hold both ideas at once: Neuralink is closer to a company "
        "that manufactures a very good modem. This project is closer to Shannon's "
        "1948 paper that first defined what “good” even means for a modem. They "
        "could, in principle, work together one day — but right now they don't "
        "overlap, and this project uses no Neuralink hardware or data.", styles["Body"]))

    # --- 9. Novelty ----------------------------------------------------------
    S.append(Paragraph("9. Has Someone Already Done This?", styles["H1"]))
    S.append(Paragraph(
        "A deliberate literature search (40 papers checked so far, spanning "
        "brain-interface hardware, AI-to-AI communication, information theory, and "
        "brain-synchronization studies) turned up plenty of closely related pieces — "
        "but not this specific combination.", styles["Body"]))
    S.append(bullets([
        "Some existing work builds real hardware links between brains, but without a "
        "formal measurement theory behind the design choices.",
        "Some existing work formally aligns brain recordings from different people, "
        "but only after the fact, on stored data — not as an active, two-way, "
        "bandwidth-limited channel while something is actually happening.",
        "A dedicated search specifically for the exact combination this theory uses — "
        '"how coupled are two predictive systems, per bit of channel they share" — '
        "did not turn up a matching prior construct.",
    ]))
    S.append(Paragraph(
        "That's a genuinely useful, encouraging result — but it's also just an "
        "absence-of-evidence check, not a peer-reviewed guarantee of originality. "
        "Literature moves fast; this gets re-checked periodically.", styles["Body"]))

    # --- 10. What this is not --------------------------------------------------
    S.append(Paragraph("10. What This Is <i>Not</i>", styles["H1"]))
    S.append(callout("Being honest about the current state",
        "This is <b>not</b> mind-reading or telepathy, is <b>not</b> yet tested on any "
        "real human or animal brain, is <b>not</b> a working product or device, and the "
        "AI-learns-its-own-channel experiment above has not yet run long enough to "
        "count as a real result — the code runs cleanly, but the numbers so far are "
        "from an undertrained smoke test, not a finished experiment. This is early-stage "
        "theoretical and simulation work (roughly one week in), aimed at top research "
        "venues over the next few years, not a near-term application.", CORAL))

    # --- 11. What's next --------------------------------------------------------
    S.append(Paragraph("11. What Comes Next", styles["H1"]))
    S.append(bullets([
        "<b>Now:</b> finish a real (not just smoke-tested) run of the AI-learns-its-own-"
        "channel experiment, across multiple random seeds, to see if Claim 1 survives "
        "when nobody hand-designs the interface.",
        "<b>Next:</b> test the same three claims against real human brain-activity "
        "recordings — two public datasets of pairs of people wearing EEG caps while "
        "having real conversations or playing music together have already been "
        "identified and verified for this purpose.",
        "<b>After that:</b> deliberately turn the channel's bandwidth up and down in a "
        "real human experiment (not just observe it) to see if task performance moves "
        "exactly the way the theory predicts.",
        "<b>Longer term:</b> use “Coupling Capacity” itself as a training signal to "
        "let two systems <i>learn</i> the best possible way to communicate, rather "
        "than a human designing the protocol by hand.",
    ]))

    S.append(Spacer(1, 10))
    S.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#CCCCCC")))
    S.append(Paragraph(
        "Prepared as a plain-language companion to the full technical paper and "
        "research repository. For the formal version — definitions, proofs, and "
        "the underlying data — see <i>paper/main.tex</i> and <i>theory/</i> in the "
        "project repository.", styles["Caption"]))

    doc.build(S, canvasmaker=NumberedCanvas)
    print(f"Wrote {OUT_PDF}")


if __name__ == "__main__":
    build()

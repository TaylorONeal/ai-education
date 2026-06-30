# AI Output Checker, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This document is the full detection guide: how to verify the numbers, and separately, how to read the fingerprints a pasted AI answer leaves behind. It is organized by confidence, highest first. No single signal is proof. Stacking signals from different categories is what builds a case worth a conversation.

## The stance first

The goal is not to catch and punish. A student who uses AI to clean up grammar, restructure a draft, or sanity-check an analysis is using the tool the way a professional would. The failure is narrower and more important: AI replacing the student's own thinking, and especially AI used without verification. That is how you get a confident, well-written submission built on numbers that were never checked. The conversation that follows should not be "did you use AI" (they probably did, and that is not going away). It should be "walk me through how you got to this conclusion." If they can, the tool was a scaffold. If they cannot, it was a crutch, and the crutch is the thing to address.

## Tier 1: structural artifacts (highest confidence)

When a student copies an answer out of an AI chat window and pastes it into a quiz box or document editor, the paste carries markup the student never sees and would never type. This is the case you raised: several quiz answers arriving with pasted HTML artifacts. Generously, it was formatting cleanup. Maybe not. The artifact tells you the text came from an AI surface; it does not tell you the thinking did. Stack it with Tier 2 before you act.

What the major tools tend to leave behind:

- ChatGPT: a distinctive list and paragraph DOM that does not match what the editor produces when you type the same content by hand, leftover code-block or syntax-highlight classes that have no reason to exist in a business answer, bold tags wrapped around key terms on first use, and remarkably uniform paragraph length.
- Claude: markdown-native typography that survived the clipboard (real em dashes, curly quotes, en dashes in ranges where a student types hyphens), and an unusually clean heading hierarchy.
- Gemini: bulleted output where a prose answer was asked for, and indentation patterns that match its export style rather than manual formatting.

How to look: pull the raw text or HTML of the submission from your LMS (most expose it through the API or a source view) and compare its structure to what the editor produces when you type. The markup trees look different.

## Tier 2: content integrity (high confidence)

This is the strongest signal and the one the skill's prompt is built around.

- Data that cannot be true. The clearest tell. One real submission carried a conversion rate of 146.78%. A conversion rate cannot exceed 100%. Whether that came from an AI or a spreadsheet slip barely matters; the student did not catch it, which is the issue. Tell the checker to flag anything impossible on its face: a rate over 100%, a negative count, a total smaller than its parts.
- Unverifiable precision. Numbers like "a 23.7% increase" or "$4.2M projected" that sound authoritative but trace to nothing in the source data. Real analysis produces messier numbers that map to actual data points.
- Invented sources. Cited studies, reports, or external facts that cannot be verified from the materials. Do not assume a cited study is real.
- Scenario confusion. References to companies, products, locations, or time periods not in the data the student was given. That is either an AI filling a gap or a student working from the wrong dataset.

One hard caveat, learned the hard way: verify scenario-confusion flags against the actual assignment prompt before you accuse anyone. An answer that looks like it is about the wrong topic is sometimes about the right one, framed differently, or about something that genuinely was in that student's version of the assignment. Check the prompt first.

## Tier 3: writing fingerprints (moderate confidence)

Any one of these can just be a well-organized student. Several stacking up raises the signal.

- ChatGPT: heavy transitional words ("furthermore," "moreover" three-plus times in a short answer), hedge-then-confidence sentences, textbook-style definitional openings, a restating summary paragraph at the end, and "overall" as a transition.
- Claude: leading with the counterargument before the point, carefully calibrated confidence language ("the data suggests" vs "shows" vs "confirms"), unprompted numbered reasoning, and scope-narrowing parentheticals.
- Gemini: a default to bullets, conversational framing ("let me break this down"), and near-identical sentence structures repeated across paragraphs.

## Tier 4: behavioral signals (lowest confidence, needs context)

Not visible in the text alone. A sudden jump from C-level to A-level prose on one assignment. A vocabulary shift in a single submission. A detailed long answer submitted forty-five minutes after the assignment opened. Uniform quality across every question (students vary their effort), or one answer dramatically better than the rest (targeted use on the hard question). These are reasons to look, never conclusions.

## Quick reference

| Signal | ChatGPT | Claude | Gemini |
|---|---|---|---|
| HTML artifacts in source | Strong | Moderate (typography) | Weak (export masks it) |
| Hallucinated or impossible data | Common | Less common | Common |
| Transition-word stacking | High | Low | Moderate |
| Uniform paragraph length | Very | Moderate | Consistent |
| Definitional opening | Common | Uncommon | Common |
| Restating summary close | Almost always | Sometimes | Often |
| Leads with the counterargument | Uncommon | Very common | Uncommon |
| Bullet-point default | Sometimes | Rarely | Frequently |

## The visual report

The skill's prompt can emit the audit as a single self-contained HTML page: one row per claim, green for verified, red for wrong, gray for unverifiable, with the student's sentence, their figure, and the correct figure side by side. Open it in any browser. It makes fabrication obvious at a glance, which is exactly what a student needs to see.

## Teaching use

Run the checker live, in front of the class, on a deliberately sloppy AI output. Watching a green-and-red report light up with fabricated numbers teaches verification faster than any lecture. It turns "AI lies sometimes" from a warning into something they have watched happen.

## Across learning management systems

The audit works on any submitted text and its source data, so the platform does not matter. Pulling the raw markup for Tier 1 artifact detection is platform-specific; most systems expose a submission's underlying HTML through their API or a source view. The ready-made specifics are in `../../guides/canvas-lms.md` for Canvas (how to pull a submission's raw HTML) and `../../guides/other-lms.md` for the other systems.

## The guardrail

This flags possible fabrication. It does not accuse anyone of misconduct. You investigate the flags, with evidence you have personally verified, and you decide. The AI's say-so is never the standard. Confirm two or three of the "wrong" calls yourself before any integrity conversation, and re-read anything marked unverifiable, because unverifiable means check, not guilty.

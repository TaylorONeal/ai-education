---
name: ai-output-checker
description: Audit AI-generated student work (analysis, charts, written claims) for fabricated numbers, invented sources, and miscalculations before you trust or grade it. Use when students submit work they produced with AI and you need to verify it against the real data, including a visual HTML report of what checks out and what does not.
---

# AI Output Checker

## The problem

Students now turn in work they made with AI, and AI is confidently wrong. It invents statistics, cites studies that do not exist, and miscalculates while sounding completely sure. If you grade the polish, you reward the fabrication. You need a fast way to check whether the numbers and sources in a submission are real, and a way to teach students to do that check themselves.

The goal is not to catch and punish. A student using AI to clean up prose or restructure a draft is using the tool the way a professional would. The flag is when AI replaces the student's own analysis, and especially when the student never verified what the AI produced. That is the real failure: not the tool use, but the abdication of thinking. The clearest tell is data that cannot be true. One real submission carried a "146.78% conversion rate." A conversion rate cannot exceed 100%. Whether that came from AI or a spreadsheet error does not matter much. The student did not catch it, and that is the issue worth a conversation.

This skill audits an AI-assisted submission against the source data and produces a clear report of what holds up and what does not.

## What you need

- The student's submission (the analysis, the claims, the charts).
- The underlying data the student was supposed to use.
- Optionally, the prompt the student used, if you ask them to submit it.

## The prompt

> You are auditing a student submission for [COURSE] that was produced with AI help. Your job is to find fabrication, not to praise the writing.
>
> I am giving you two things: the student's submission, and the source data it should be based on.
>
> For every numeric claim in the submission:
> 1. Find the matching figure in the source data.
> 2. State whether it matches, is wrong, or cannot be found in the data.
> 3. For any "wrong" or "cannot be found," quote the student's sentence and show the correct figure or note its absence.
> 4. Flag any figure that cannot be true on its face (for example, a rate above 100%, a negative count, a total that exceeds its parts).
>
> For every cited source, study, or external fact: flag any that cannot be verified from the materials provided. Do not assume a cited study is real.
>
> Flag scenario confusion: any reference to a company, product, location, or time period that is not in the data the student was given. That is either AI filling a gap or the student working from the wrong dataset.
>
> Then summarize: how many claims checked out, how many were wrong, how many were unverifiable.
>
> Source data: [PASTE OR ATTACH DATA]
> Submission: [PASTE SUBMISSION]

## Make it a visual report (HTML artifact)

Add this to the prompt to get a report you can skim or hand back to the student:

> Produce the audit as a single self-contained HTML page. Show each claim as a row, color-coded: green for verified, red for wrong, gray for unverifiable. Put the student's sentence, the figure they used, and the correct figure side by side. Include the summary counts at the top. Use only inline styles so it opens anywhere.

Open the HTML file in any browser. It makes the fabrications obvious at a glance, which is exactly what a student needs to see.

## When the submission itself shows it was pasted from an AI

Separate from whether the numbers are real is the question of where the text came from. When a student copies an answer out of an AI chat window and pastes it into a quiz box or document editor, the paste often carries structural fingerprints the student never sees: nested list markup and paragraph spacing that the editor would not produce on its own, leftover code-block or syntax-highlight styling, typographic quotes and dashes in a box where someone typing would use plain ones, and a heading hierarchy cleaner than hand-typed work. None of that is proof. A student may have pasted from an AI purely to clean up formatting, which is not a problem. The flag is narrower: pasted-in content plus unverified numbers or sources means the student did not check what the tool produced, and that is the thing worth a conversation. Treat the artifact as one signal, stack it with the content checks above, and never act on the artifact alone. The full, source-by-source detection guide (what each major AI tool leaves behind, ranked by confidence) is in this skill's README.

## What to check before you trust it

1. Confirm two or three of the "wrong" calls yourself. The checker can also be wrong. Verify before you confront a student about fabrication.
2. Re-read anything marked unverifiable. Sometimes the source is real but just not in the materials you provided. Unverifiable means "check," not "guilty."
3. Verify scenario-confusion flags against the actual assignment prompt first. A student may have referenced something that really was in their version of the assignment. The lesson here was learned the hard way: an answer that looks like it is about the wrong topic is sometimes about the right one, just framed differently. Check the prompt before you accuse.
4. Check the claim count. If the submission has 20 numeric claims and the audit only examined 8, run it again and tell it to process all of them.

## The guardrail

This flags possible fabrication. It does not accuse a student of misconduct. You investigate the flags and you decide. An academic integrity conversation is yours to have, with evidence you have personally verified, never on the AI's say-so. The better opening is not "did you use AI?" (they probably did, and that is not going away). It is "walk me through how you got to this conclusion." If they can, the tool was a scaffold. If they cannot, the tool was a crutch, and that is the real thing to address.

## Automated version

Connect it to your submission queue and it can run the audit across a whole assignment, producing one HTML report per student plus a summary table ranking submissions by number of unverifiable or impossible claims. You work that list top-down. It never files an integrity report and never changes a grade on its own.

## Teaching use

Run this in front of students on a deliberately sloppy AI output. Watching a green-and-red report light up with fabricated numbers teaches verification faster than any lecture. It turns "AI lies sometimes" from a warning into something they have seen.

## Automate even better

Have the agent pull every submission's raw HTML in one pass and run the artifact and content checks across the whole class at once, producing a single ranked report of who carries the most unverifiable or impossible claims, so you work the list top-down instead of opening submissions one at a time. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

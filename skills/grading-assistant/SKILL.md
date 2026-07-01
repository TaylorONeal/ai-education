---
name: grading-assistant
description: Apply your grading rubric consistently and catch correct answers that are phrased differently than your answer key expected. Use when grading short answers, essays, or open-response work and you want a second set of eyes that credits understanding instead of penalizing wording.
---

# Grading Assistant

## The problem

When you grade a stack of essays, the student you read at 11pm gets a different teacher than the one you read at 9am. Worse, an answer key trains you to look for specific words. A student who understood the concept perfectly but said it in their own words, or in their second language, quietly loses points for phrasing. That is not a knowledge gap. That is a matching problem, and it is unfair.

This skill uses AI as a teaching assistant: it applies the rubric you wrote, then flags places where a student may have earned credit you did not give. You stay the grader. It catches your blind spots.

## What you need

- Your rubric, written out. Not "good analysis." The actual criteria and point values.
- A model answer or answer key, if you have one.
- The student responses.

## Write the rubric so a machine can apply it

The single biggest lever on grading consistency is naming, in your rubric, what separates each grade band. Vague bands produce vague grades. The version that works in practice spells out what each tier actually looks like:

- A band: names the concept by its correct term, defines it in one sentence, uses specific numbers instead of "significantly higher," and grounds the recommendation in the actual data given, not generic advice.
- B band: right concept and right direction, but a definition is missing or imprecise, or the analysis is not quantified.
- C and D band: describes the idea without naming it, leans on vague directional language ("it went up," "this is bad"), or gives generic advice unconnected to the scenario.

If your assignment can carry one explicit, hard-to-fake requirement, put it in the rubric, because it is often the cleanest line between one grade band and the next and the AI can check it directly. The general form: every answer must name and define the specific course term, source, or piece of evidence it relies on, so a vague paraphrase cannot pass for mastery. Tailor it to your field: name the metric and define it (analytics or quant), name the event or source and its significance (history), quote the passage and name the device (literature), name the mechanism or term and define it (science or nursing).

Tell the model to dock or flag, not reward, a short list of red flags: intensifiers with no number behind them ("significantly," "dramatically"), "as discussed in class" without actually applying the concept, naming a metric that is not relevant to the question, and scenario confusion (answering about the wrong company or the wrong question type). Encoding these directly catches the fluent-but-empty answer that would otherwise drift up a band on style alone.

This works on the text of a response and your rubric, so it is the same job whether the responses live in Canvas SpeedGrader, a Blackboard or Brightspace gradebook, a Moodle assignment, or a stack of documents. Getting scores back into your system afterward is the platform-specific part; see the finish modes below.

## The prompt

> You are my grading assistant for [COURSE], assignment: [ASSIGNMENT NAME]. You do not assign final grades. You apply my rubric and flag anything I should look at again.
>
> Rubric, with what each grade band looks like:
> [PASTE RUBRIC WITH POINT VALUES AND BAND DESCRIPTIONS]
>
> Model answer (for reference, not as the only acceptable wording):
> [PASTE MODEL ANSWER, OR WRITE "none"]
>
> For each student response I give you:
> 1. Score it against each rubric criterion, with the points and a one-sentence reason.
> 2. Separately, flag any case where the student appears to demonstrate the underlying understanding but used different wording, examples, or structure than the model answer. Quote the exact sentence and explain what concept it satisfies.
> 3. Flag scenario confusion: if the student answered about the wrong scenario, the wrong company, or a generic version of the question, call it out.
> 4. Flag anything you are unsure about for my review rather than guessing.
>
> Do not inflate or deflate to hit a target. If the work is weak, say so and show why. Here is the first response: [PASTE RESPONSE]

## The output: a grading spreadsheet

The scored output lands in a spreadsheet in a format honed over many real grading runs. One row per student. For each question, three columns sit together: the student's answer, the score, and a notes column that records why the score, including the sub-question breakdown (for example, "Sub-Q1 (3pts): 2/3, named the metric but did not define it"). Then a total and a flags column. The notes column is the point: it is the paper trail, it is what you read to confirm or adjust, and it is what you can show a student who asks. A blank template in this exact format ships with this skill at `grading-template.xlsx` (with a rubric-bands sheet and a how-to sheet). For a multi-variant essay exam, use one block per essay bank instead of per question: "[Bank] Answer | [Bank] Score | [Bank] Notes".

Add this to the prompt to get output that drops straight into the template:

> Return your scoring as rows for a spreadsheet. For each student, give one row with: last name, first name, an id placeholder, and for each question the score and a notes cell that states why, with the sub-question breakdown. End the row with the total and any flag. Match these columns exactly: [PASTE YOUR HEADER ROW].

## How it works, one student start to finish

Here is a concrete run so you can see exactly what goes in and what comes back.

Say the assignment is a short-answer marketing question worth 10 points, and your rubric is: names the metric and defines it (4), uses the actual numbers from the scenario (3), gives a recommendation grounded in that data (3).

You paste one student's answer. The student wrote: *"The open rate went up a lot after they changed the subject line, so the new version is clearly better and they should keep doing that."*

What the AI hands back, as one spreadsheet row:

- Answer: (the text above)
- Score: 4 / 10
- Notes: "Named a metric (open rate) but did not define it: -0. Did not use the scenario's actual numbers, said 'a lot' instead of the figures given: -3. Recommendation is generic ('keep doing that') and not grounded in the data: -3. Also a possible metric mismatch: the question was about clicks, not opens, flagging for your review."
- Total: 4
- Flag: SCENARIO/METRIC MISMATCH, review

Notice three things. The score is an estimate with its reasons attached, not a verdict. The notes are written so you could read them aloud to the student. And the AI flagged the metric mismatch instead of silently scoring around it, because you told it to flag what it is unsure about rather than guess.

Now a second student, where the skill earns its keep. The student wrote: *"When they sent the second email, way more of the people who opened it actually clicked through, so that version did a better job of getting the click once someone was already in the inbox."*

A naive match against an answer key that wants the words "click-to-open rate" docks this. The differently-worded pass instead flags it:

- Notes: "DIFFERENT WORDING FLAG: the student described click-to-open rate exactly (clicks among openers) without using the label. Quote: 'way more of the people who opened it actually clicked through.' Conceptually correct. Your call on whether the missing term costs the naming point."

You read that flag, decide the student understood it, and award the conceptual credit. That catch, on the student who knew the material but said it their own way or in a second language, is the single most valuable thing this skill does.

## What to check before you trust it

1. Read every "different wording" flag yourself. This is the highest-value output and the place the AI is most useful. Confirm the student actually shows the understanding before you award the points.
2. Re-grade three responses fully by hand and compare to the AI's scores. If they diverge, your rubric is probably ambiguous. Tighten it, do not just trust the model.
3. Watch who gets flagged. This cuts both ways: if second-language or non-standard-phrasing students cluster in the "different wording" flags, that is the bias the skill is meant to catch, and you should act on it. If instead they cluster in the low scores, look harder before you finalize; a careless pass can encode the same bias it is supposed to fix.
4. Check the scenario-confusion calls against the actual prompt. Sometimes a student references something that really was in their version of the assignment and the AI did not have it. Verify before you dock points.

## The guardrail

The AI proposes, you grade. It never posts a grade. Its job is to make you a more consistent and more generous-where-deserved grader, not to grade for you. If you would not be able to explain a score to the student in your own words, do not enter it. Keep what the AI produced and what you changed; "here is the rubric, here is the AI pass, here is my adjustment and why" is a strong position if a grade is ever challenged.

## Two ways to finish: a spreadsheet, or grades in Canvas

When the scoring pass is done, you choose how it ends. The default is the safe one. The Canvas path is opt-in and has one hard prerequisite.

### Mode 1 (default): just make the spreadsheet

The AI produces the grading spreadsheet and stops. Nothing touches your LMS. You get the `grading-template.xlsx` format, or a Google Sheet with the same columns: per question the student's answer, the estimated score, and the notes, then a total and a flags column. The scores are labeled as estimates, because you finalize them.

This is the right default for almost everyone. You keep the file as your paper trail, work the flags, adjust whatever you want, and then enter grades into your gradebook yourself, by hand or by import, on your own schedule. The AI never goes near a student-facing system. If you are not sure which mode you want, you want this one.

To ask for it explicitly, end your prompt with:

> Output only a grading spreadsheet in this column format, with estimated scores and notes. Do not attempt to enter anything into any gradebook or LMS. I will review the file and enter grades myself.

If you want a Google Sheet instead of Excel, say so, or paste the rows into a blank sheet; the column pattern is identical.

### Mode 2 (opt-in): let an agent enter grades into Canvas

Only at the connected and computer-control levels, and only if you choose it. Before a single grade is entered, the assignment's grades must be set to hidden so students see nothing while the agent works. This is not optional. If you skip it, students get notified of grades as each one lands, including the wrong ones you have not reviewed yet.

The order that keeps you safe:

1. Hide the grades first. In Canvas, open the Gradebook, find the assignment column, open its menu, and set the Grade Posting Policy to Manual (or, on an already-graded column, choose Hide grades). Confirm the column shows the hidden indicator (a crossed-out eye). Verify this yourself before continuing. The agent should refuse to enter grades until it confirms the column is hidden.
2. Enter the reviewed scores while hidden. Use whichever method fits: gradebook CSV import for the whole stack, the API batch endpoint, or SpeedGrader by hand. If you go student by student in SpeedGrader, watch the save bug: a score only saves when committed with a real keyboard Enter, and a synthetic key event silently drops it. The mechanics for all three, and that bug, are in `../../guides/canvas-lms.md`.
3. Read the distribution while it is still hidden. This is your review gate. Nothing is visible to students yet, so you can still fix anything.
4. Post grades when you decide, not before. Manually choose Post grades on the column. That is the deliberate human action that releases them. Until you click it, no student sees a score.

The agent's job ends at step 3 with everything entered but hidden. Releasing grades is your call and yours alone, the same guardrail as everywhere else in this toolkit: the AI prepares, you post.

For other platforms, the same hide-then-post pattern and the grade-entry mechanics are in `../../guides/other-lms.md`.

## Automated version

Connect it to your assignment submissions and it can do a first pass on the whole stack, returning a scored table plus a separate "review these" list of differently-worded answers, scenario-confusion cases, and low-confidence calls. You work the review list, adjust, and either keep the spreadsheet (Mode 1) or enter the reviewed grades into Canvas as hidden for your final sign-off (Mode 2). The full stack is never auto-posted, and grades are never released without your explicit Post action.

## Automate even better

Have the agent pull the entire submission stack into one place for the first pass, and, better, assemble every student's answer to the same question into one view so you calibrate that question across the whole class before you score anyone. Write the scored rows straight into the grading-template format. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

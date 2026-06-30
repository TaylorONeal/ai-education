# Grading Assistant, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This is the longer version: how to write a rubric a machine can actually apply, why the differently-worded catch is the highest-value thing in the toolkit, and how to keep yourself the grader the whole way through.

## The two problems this solves

The first is fatigue. The student you grade at 11pm gets a different teacher than the one you graded at 9am. Consistency is hard to hold across a tall stack, and the bottom of the stack pays for it.

The second is subtler and more unfair. An answer key trains you to look for specific words. A student who understood the concept perfectly but phrased it their own way, or in their second language, loses points for wording, not for knowledge. That is not a knowledge gap. It is a matching problem, and a tired grader matching against a key will miss it every time.

This skill uses AI as a teaching assistant: it applies the rubric you wrote, then flags where you may have under-credited understanding. You stay the grader. It catches your blind spots.

## Write a rubric a machine can apply

The single biggest lever on consistency is naming, in the rubric itself, what separates each grade band. "Good analysis" is not a criterion a model (or a tired human) can apply the same way twice. Spell out what each tier looks like:

- A band: names the concept by its correct term, defines it in one sentence, uses specific numbers instead of "significantly higher," and grounds the recommendation in the actual data, not generic advice.
- B band: right concept and right direction, but a definition is missing or imprecise, or the analysis is not quantified.
- C and D band: describes the idea without naming it, leans on vague directional language ("it went up," "this is bad"), or gives generic advice unconnected to the scenario.

### The single-requirement lever

If your assignment can carry one explicit, hard-to-fake requirement, it becomes the cleanest line between two bands and the easiest thing for the AI to check. The general form: every answer must name and define the specific course term, source, or piece of evidence it rests on, so a fluent-but-empty answer cannot drift up a band on style alone. The requirement is objective and rewards precision over hand-waving. Point the "name the real thing" at what you teach:

- Analytics or quant: name the metric and define it in one sentence. A student who writes "the rate dropped" without naming it as "conversion rate, the percentage of visitors who complete a purchase" gets deducted.
- History: name the specific event, source, or date and state its significance, not "around that time things changed."
- Literature: quote the exact passage and name the device, not "the author uses imagery."
- Science or nursing: name the mechanism or term and define it, not "the body responds."

The shape is identical across fields: force one piece of named, defined specificity that only someone who actually learned the material can supply.

### Red flags to encode

Tell the model to dock or flag, not reward: intensifiers with no number behind them ("significantly," "dramatically"), "as discussed in class" without actually applying the concept, naming a metric that is not relevant to the question, and scenario confusion (answering about the wrong company or the wrong question type).

## The differently-worded catch

This is the highest-value output in the toolkit. Ask the model to do two passes: score against the rubric, then separately flag any response that shows the underlying understanding using different wording, examples, or structure than your model answer, quoting the exact sentence and naming the concept it satisfies. You read those flags and decide whether the student earned the credit.

This is also where fairness cuts both ways. The same mechanism that credits a second-language student for correct-but-differently-phrased work can, run carelessly, encode bias against non-standard phrasing. Watch who clusters in the flags. If second-language or non-standard-phrasing students cluster there, the skill is doing its job; act on it. If they cluster in the low scores instead, look harder before you finalize.

## A worked example

Prompt: a student writes, "When the brand sent the second email, way more people who opened it actually clicked, so that version was doing a better job at getting the click once they were in." Your key expected the term "click-to-open rate (CTOR)."

A naive match docks this: the term is missing. The differently-worded pass flags it: the student described CTOR exactly (clicks among openers) without the label. Your call: full conceptual credit, partial deduction for not naming the metric if your rubric requires naming. Either way, you made the call with the understanding in front of you, instead of silently docking for a missing word at midnight.

## Across learning management systems

Grading short answers and essays is the same job whether the responses live in Canvas SpeedGrader, a Blackboard or Brightspace gradebook, a Moodle assignment, or a stack of documents. This skill operates on the text of the responses and your rubric; it does not depend on the platform. You do not have to figure out how to get grades back into your system from scratch: the ready-made specifics (CSV import, API batch submission, and the manual SpeedGrader workflow and its save-bug pitfall) are in `../../guides/canvas-lms.md` for Canvas and `../../guides/other-lms.md` for Blackboard, Moodle, Brightspace, Schoology, and Google Classroom.

## The output format that makes grading defensible

The scored output belongs in a spreadsheet, and the format matters as much as the scores. The version honed over many real grading runs puts one row per student and, for every question, three columns side by side: the student's answer, the score, and a notes column that states why the score. The notes carry the sub-question breakdown, for example "Sub-Q1 (3pts): 2/3, named the metric correctly but did not define it in one sentence." Then a total and a flags column.

Why this format and not just a column of numbers:

- The notes column is the justification. It is what you read to confirm or adjust each score, and it is exactly what you show a student who challenges a grade. A score with no recorded reason is an unrecorded gut call.
- Keeping the answer next to the score and the note means you are never grading blind from a number; the evidence travels with the judgment.
- The sub-question breakdown in the notes is what lets you see, at a glance, where a student lost points, which is the difference between "you got a 6" and "you got the metric and the interpretation but not the recommendation."
- For a multi-variant essay exam where each student drew a different question, use one block per essay bank ("[Bank] Answer | [Bank] Score | [Bank] Notes") so every student's row is comparable even though their prompts differed.

A blank template in this exact format ships with the skill at `grading-template.xlsx`: a Grading sheet with the column pattern and two example rows showing the notes convention, a Rubric-bands sheet for your band descriptions, and a How-to sheet. The grading-assistant prompt can fill the Score and Notes columns as a first pass; you read every notes cell and adjust before anything is posted.

## The connected version, in detail

Pointed at your submission queue, it does a first pass on the whole stack and returns two things: a scored table, and a separate "review these" list holding the differently-worded answers, the scenario-confusion cases, and any low-confidence calls. You work the review list, adjust, and post. The full stack is never auto-posted. When you batch-submit through your LMS, keep the grades hidden until you have read the distribution and signed off.

## The guardrail and your records

The AI proposes, you grade. It never posts a grade. If you could not explain a score to the student in your own words, do not enter it. Keep what the AI produced and what you changed; "here is the rubric, here is the AI pass, here is my adjustment and why" is a strong position if a grade is ever challenged.

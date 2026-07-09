---
name: grading-assistant
description: Apply your grading rubric consistently and catch correct answers that are phrased differently than your answer key expected. Use when grading short answers, essays, or open-response work and you want a second set of eyes that credits understanding instead of penalizing wording.
---

# Grading Assistant

## The problem

Apply a teacher rubric consistently and flag responses that need human judgment.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Rubric, point values, model answer if any, submissions, and any accepted alternate wording.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Read the rubric before seeing submissions when possible.
3. Accept correct alternate wording when it shows the target concept.
4. Never assign final grades. Mark confidence and reasons.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

Grading spreadsheet draft with rationale, evidence quotes, uncertainty flags, and items for human review.

## Prompt to run

> You are running the Grading Assistant skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Apply a teacher rubric consistently and flag responses that need human judgment.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: Grading spreadsheet draft with rationale, evidence quotes, uncertainty flags, and items for human review.
>
> Requirements: cite or name the source for important claims, mark missing evidence, put uncertain or student-impacting items in a review queue, and end with what I must check before trusting the output. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## What to check before trusting it

- The output uses only supplied or confirmed sources.
- Dates, links, IDs, calculations, point totals, and policy language are verified.
- Student-impacting items are clearly separated for human review.
- The artifact is useful as a draft but does not pretend to be the final decision.

## The guardrail

AI does the draft. The teacher makes the call. Nothing reaches a student without a human reading it first.

## Automated version

A connected agent may pull evidence from the LMS, Drive, local files, calendar, chat tools, or prof-brain, then build the same draft artifact. It must summarize what it found and wait for confirmation before writing back to any system.

## Automate even better

For repeated use, store source pulls as durable CSV or Markdown files, refresh prof-brain, and reuse the same reviewed patterns across terms. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

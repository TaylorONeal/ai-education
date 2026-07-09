---
name: quiz-builder
description: Generate scenario-based quiz and exam question banks that discriminate, with one clearly correct answer, plausible distractors, difficulty-scaled points, and per-answer feedback, in a format that imports into your LMS. Use to build or expand a question bank. Domain-selectable; ships with a business pack and is built to add more domains.
---

# Quiz Builder

## The problem

Build scenario-based question banks with plausible distractors and LMS-ready feedback.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Objectives, domain pack, difficulty and point targets, number of items, import format, and source materials.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Use the selected domain pack for realistic scenarios.
3. Make exactly one defensible correct answer.
4. Give every distractor a diagnosable reason for being wrong.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

Question-bank table with one row per answer option, answer key, feedback, and validation notes.

## Prompt to run

> You are running the Quiz Builder skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Build scenario-based question banks with plausible distractors and LMS-ready feedback.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: Question-bank table with one row per answer option, answer key, feedback, and validation notes.
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

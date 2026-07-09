---
name: exam-rebalance
description: Check an exam for difficulty and topic coverage before students take it, simulate how different kinds of student would score, and compare it against every prior version you have, so you catch an unfair or lopsided test while you can still fix it. Use when finalizing a midterm, final, or quiz.
---

# Exam Rebalance

## The problem

Check an exam before release for coverage, difficulty, ambiguity, timing, and likely performance across student personas.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Draft exam, objectives, point values, prior exams if available, constraints, and answer key or rubric.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Build a coverage and point map before judging difficulty.
3. Check each item for ambiguity, cueing, answer leakage, and time burden.
4. Simulate likely results for multiple invented student archetypes.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

Rebalance memo, item-level risk table, persona simulation, coverage map, and revision queue.

## Prompt to run

> You are running the Exam Rebalance skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Check an exam before release for coverage, difficulty, ambiguity, timing, and likely performance across student personas.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: Rebalance memo, item-level risk table, persona simulation, coverage map, and revision queue.
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

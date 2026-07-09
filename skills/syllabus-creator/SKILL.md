---
name: syllabus-creator
description: Draft a clear, complete syllabus from course goals, policies, assessments, schedule constraints, and the prof-brain knowledge base. Use when building a new course syllabus or refreshing one for an upcoming term.
---

# Syllabus Creator

## The problem

Draft or refresh a syllabus from course goals, policies, assessments, calendar constraints, and prof-brain.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Course basics, objectives, assessments, policies, calendar dates, existing syllabus, and tone.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Do not invent dates, policies, catalog language, or grading rules.
3. Use prof-brain or existing syllabus first.
4. Separate draft text from required human verification.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

Complete syllabus draft plus verification checklist for dates, policies, grading math, and accessibility language.

## Prompt to run

> You are running the Syllabus Creator skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Draft or refresh a syllabus from course goals, policies, assessments, calendar constraints, and prof-brain.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: Complete syllabus draft plus verification checklist for dates, policies, grading math, and accessibility language.
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

---
name: ai-output-checker
description: Audit AI-generated student work (analysis, charts, written claims) for fabricated numbers, invented sources, and miscalculations before you trust or grade it. Use when students submit work they produced with AI and you need to verify it against the real data, including a visual HTML report of what checks out and what does not.
---

# AI Output Checker

## The problem

Audit AI-assisted student work for fabricated numbers, impossible claims, invented sources, and pasted-AI artifacts.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Student submission, source data, allowed sources, assignment prompt, and optional student AI-use notes.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Extract every numeric claim and cited source.
3. Verify each claim against the supplied data only.
4. Flag impossible values, scenario drift, and sources not present in the materials.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

Verification report with checked claims, wrong claims, unverifiable claims, source issues, and student-facing feedback draft.

## Prompt to run

> You are running the AI Output Checker skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Audit AI-assisted student work for fabricated numbers, impossible claims, invented sources, and pasted-AI artifacts.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: Verification report with checked claims, wrong claims, unverifiable claims, source issues, and student-facing feedback draft.
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

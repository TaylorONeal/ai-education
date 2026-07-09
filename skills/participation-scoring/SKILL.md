---
name: participation-scoring
description: Score student class participation fairly by pulling each student's real activity across chat channels, direct messages, and meetings, then applying rules you set. Use when you need to grade participation for a class and want an auditable record instead of a gut feeling.
---

# Participation Scoring

## The problem

Score participation from real activity across confirmed sources, not memory.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Roster, source exports for public posts, DMs, TA logs, meetings, and the participation rubric.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Normalize names across sources before scoring.
3. Use buckets, not raw counts, so volume does not swamp quality.
4. Treat true zeroes as review items until all sources have been checked.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

Participation evidence table, bucketed score draft, flags for low or ambiguous evidence, and a human review queue.

## Prompt to run

> You are running the Participation Scoring skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Score participation from real activity across confirmed sources, not memory.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: Participation evidence table, bucketed score draft, flags for low or ambiguous evidence, and a human review queue.
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

---
name: canvas-lms
description: Operate Canvas LMS reliably from an AI agent or script: authenticate, push styled pages and assignment HTML, enter grades without losing them, and edit quizzes and question banks. Use when a task involves the Canvas API, SpeedGrader, the Rich Content Editor, or quiz and question-bank changes. The full reference is guides/canvas-lms.md.
---

# Canvas LMS Operations

## The problem

Operate Canvas safely for content, grade, quiz, and page tasks while preserving the human gate.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Canvas host, course ID, target IDs, authentication method, content or grade data, and posting status.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Confirm the exact course and object IDs before writing.
3. Preview pages and assignments after API success.
4. Keep grades hidden until the human approves posting.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

API or browser-action plan, verification steps, and staged changes that wait for approval before release.

## Prompt to run

> You are running the Canvas LMS Operations skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Operate Canvas safely for content, grade, quiz, and page tasks while preserving the human gate.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: API or browser-action plan, verification steps, and staged changes that wait for approval before release.
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

---
name: start-here
description: The front door for a teacher new to this toolkit. Use when someone has just installed these skills or pointed an AI agent at this repo and wants to get started, when a user says "help me get started," "how do I use this," "set this up for my class," or "onboard me." It orients the teacher, asks a few quick questions, ingests their course materials so the other skills are grounded, and routes them to the right first task for a fast win.
---

# Start Here

## The problem

Onboard a teacher into the toolkit by asking one question at a time, then routing to one fast win.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Teacher context, biggest time sink, LMS or tool access, and one small real example.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Explain the toolkit and the one rule in two sentences.
3. Ask one question at a time.
4. Route to one skill, not the whole catalog.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

A grounded first task, optional prof-brain ingestion plan, and one usable draft.

## Prompt to run

> You are running the Start Here skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Onboard a teacher into the toolkit by asking one question at a time, then routing to one fast win.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: A grounded first task, optional prof-brain ingestion plan, and one usable draft.
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

---
name: prof-brain
description: Build a professor's knowledge base by ingesting all your course source material (local folders, Google Drive, LMS reading pages, syllabus, slides, past exams) into one well-organized folder of Markdown notes with an index, so you and every other skill can read from one grounded source. Use to set up or refresh the brain, and optionally sync it to Notion or an Obsidian vault.
---

# Prof Brain

## The problem

Ingest course materials into an organized Markdown knowledge base that other skills can read.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Pointers to local folders, LMS pages, Drive folders, syllabus, slides, exams, policies, and destination folder.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Copy or reference originals without moving them unless asked.
3. Keep student PII out of the brain.
4. Write small Markdown notes with frontmatter and an index.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

Source inbox if requested, Markdown notes with frontmatter, index, gaps log, and refresh instructions.

## Prompt to run

> You are running the Prof Brain skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Ingest course materials into an organized Markdown knowledge base that other skills can read.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: Source inbox if requested, Markdown notes with frontmatter, index, gaps log, and refresh instructions.
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

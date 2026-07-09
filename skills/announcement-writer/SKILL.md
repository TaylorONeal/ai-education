---
name: announcement-writer
description: Draft class announcements in your own voice, trained on your past posts, with the AI tells stripped out so it sounds like you and not a robot. Use for weekly updates, exam details, schedule changes, welcome and goodbye posts, and extra-credit notices.
---

# Announcement Writer

## The problem

Draft announcements in the teacher voice after learning from past posts and stripping AI tells.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: Five to ten past announcements or saved style guide, facts to announce, audience, date, links, and constraints.
- Prefer confirmed course context from `skills/prof-brain/` before asking the teacher to paste materials again.
- If a connector or LMS is available, pull the smallest useful source set first and summarize it for confirmation.
- If nothing is connected, ask for one small useful sample instead of the whole course.

## Agent workflow

1. State the source set you will use and what is missing.
2. Create or reuse a voice guide before drafting.
3. Draft from verified facts only.
4. Run a voice cleanup for stiff phrasing, inflated words, and punctuation tells.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

Draft announcement plus fact checklist and optional shorter LMS/email versions.

## Prompt to run

> You are running the Announcement Writer skill for [COURSE]. Use only the materials I provide or the connected sources I confirm.
>
> Task: Draft announcements in the teacher voice after learning from past posts and stripping AI tells.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: Draft announcement plus fact checklist and optional shorter LMS/email versions.
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

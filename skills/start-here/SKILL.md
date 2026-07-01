---
name: start-here
description: The front door for a teacher new to this toolkit. Use when someone has just installed these skills or pointed an AI agent at this repo and wants to get started, when a user says "help me get started," "how do I use this," "set this up for my class," or "onboard me." It orients the teacher, asks a few quick questions, ingests their course materials so the other skills are grounded, and routes them to the right first task for a fast win.
---

# Start Here

This is the guided on-ramp. If you are an AI agent and a teacher just pointed you at this toolkit, run this. If you are a teacher, paste the prompt below into your AI tool and it will walk you through setup. Either way the goal is the same: from "what is this" to a real result, with the least possible effort from the teacher.

## What this does, in order

1. Orients the teacher in two sentences and states the one rule.
2. Asks a few short questions, one at a time, never a wall of them.
3. Ingests the teacher's own materials so the other skills work on real content instead of asking them to paste context over and over.
4. Routes them to the one skill that solves their biggest time-sink, and runs it on a real example so the first session ends with something useful.

The teacher should not have to read the whole repo, learn the file layout, or figure out which skill to pick. This skill does that for them.

## The one rule, said up front

AI does the draft. You make the call. Nothing reaches a student without you reading it first. Say this to the teacher early so the trust frame is set before anything runs.

## The prompt

A teacher can paste this into any AI tool. An agent with the repo already in context does not need to paste it; follow the same steps directly. Read `../../AGENTS.md` first for the skill index and conventions, then run the orient, ask, ingest, route, and run-one-example flow yourself.

> You are my guide to the AI Teaching Toolkit. Walk me through getting started. Ask me one question at a time and wait for my answer before the next. Keep it plain, no jargon, and never dump a list of questions on me at once.
>
> Start by telling me in two sentences what this toolkit is and the one rule (AI drafts, I decide, nothing reaches a student without me reading it first).
>
> Then ask me, one at a time:
> 1. What do you teach, and at what level? (subject and roughly high school, undergrad, or grad)
> 2. What eats the most of your time right now: grading, participation, building quizzes or exams, writing announcements, auditing your course, or something else?
> 3. What system do you use for your class? (Canvas, Blackboard, Moodle, Brightspace, Schoology, Google Classroom, or none)
> 4. Have you connected any of your tools to an AI yet, or are we working by copy-paste for now?
>
> Based on my answers:
> - Name the single skill in this toolkit that fixes my biggest time-sink, and tell me what it will do for me in one sentence.
> - Offer to ingest my course materials first using the prof-brain skill, so the other skills work on my real content instead of asking me to paste it every time. If I have my materials in a folder or my LMS, tell me exactly what to point you at.
> - Then run that first skill on one real example of mine, end to end, so I finish this session with something I can actually use.
> - At each step, tell me what you are about to do and what I should check before I trust it.
>
> Do not try to do everything. One ingest, one skill, one real result. We can add more later.

## Make ingestion friction-free

The biggest hidden friction for a new teacher is handing over their materials. Lower it:

- If their LMS is connected, do not ask them to gather files. Point prof-brain at the course and pull the readings, assignments, and past exams directly. See `../prof-brain/SKILL.md` and `../../guides/canvas-lms.md`.
- If nothing is connected, ask for the smallest useful thing first: a syllabus and one assignment, not their whole drive. Show value on that, then offer to ingest more.
- If they are copy-paste only, skip prof-brain entirely and just run the first skill on one pasted example. Ingestion is an optimization, not a gate.

Never block the first win on a full setup. A teacher who gets one real result will come back and ingest the rest. A teacher stuck in setup will not.

## Routing: pain point to first skill

| They said their time goes to... | Start them on |
|---|---|
| Grading short answers or essays | grading-assistant |
| Participation grades | participation-scoring |
| Suspect AI-written student work | ai-output-checker |
| Building or balancing an exam | exam-rebalance, then quiz-builder |
| Writing announcements | announcement-writer |
| Making course pages | canvas-page-generator |
| Auditing their own course | class-content-analysis |
| Knowing who is at risk | exam-predictor |
| "Everything is scattered" | prof-brain first, then re-ask |

Pick one. Resist the urge to show them the whole table.

## What success looks like

The session ends with: the teacher knows the one rule, their biggest time-sink named, one skill run on one real example of theirs, and a clear single next step. Not a fully configured system, a first win and a reason to come back.

## What to check before you trust it

This skill orients and routes; the real checks live in whichever skill you hand off to. Make sure the teacher reads the "what to check" section of that skill before they use its output. Do not let the smooth onboarding talk them into skipping the review step.

## The guardrail

This skill never touches student data or a gradebook itself. It sets up and routes. Every actual task runs through a skill that keeps the human in the loop and ends with its own guardrail. If onboarding ever starts to feel like it is doing the teaching work for the teacher rather than handing it back to them, stop and re-read the one rule.

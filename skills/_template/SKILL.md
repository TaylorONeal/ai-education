---
name: skill-name
description: Describe when an agent should use this skill, the artifact it creates, and the required human review point.
---

# Skill Name

## The problem

Name the teaching or course-operations situation in one concrete paragraph. Keep the skill file as the agent runbook, not the human field guide.

Do not use this skill to send messages to students, post grades, publish pages, or make official decisions without a human approval step.

## What you need

- Required: the smallest useful input for copy-paste use.
- Preferred: confirmed course context from prof-brain or connected tools.
- Constraints: policy, rubric, accessibility, privacy, LMS, or calendar rules that change the output.

## Agent workflow

1. Check whether prof-brain already has the relevant course context.
2. Check whether the LMS, local files, Drive, calendar, or chat source can provide the needed evidence.
3. Summarize what you found and ask the teacher to confirm the source set.
4. If nothing is connected, ask for one small useful sample rather than the whole course.
5. Produce the draft artifact and a short review queue.
6. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## Output

Name the concrete artifact: table, report, draft, HTML page, spreadsheet, CSV, or checklist.

## Prompt to run

> You are running the [SKILL NAME] skill for [COURSE]. Use only the information I provide or the sources I confirm.
>
> Inputs: [PASTE INPUTS, OR READ FROM CONFIRMED SOURCES].
>
> Produce: [EXPECTED ARTIFACT].
>
> Put uncertain, missing-evidence, or student-impacting items in a review queue. End with what I must check before trusting the output. Stop before anything reaches students, a gradebook, an LMS page, or an official record.

## What to check before trusting it

- Source fidelity: every important claim traces to supplied or confirmed material.
- Missing context: the output states what it could not see.
- Fairness: the output does not silently penalize phrasing, access limits, section differences, or quiet forms of participation.
- Artifact integrity: calculations, links, IDs, columns, and platform fields are checked.

## The guardrail

AI does the draft. The teacher makes the call. Nothing reaches a student without a human reading it first.

## Automated version

Describe the connected version: what the agent can pull, what it can draft, and where it must pause.

## Automate even better

Describe the durable workflow: store source pulls, refresh prof-brain, reuse reviewed artifacts, and compare across terms.

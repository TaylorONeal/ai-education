---
name: skill-name
description: Describe when an agent should use this skill, what artifact it creates, and the human review point.
---

# Skill Name

## The problem

Name the teaching problem in concrete terms. Say what goes wrong when a teacher or agent does this from scratch.

## What you need

- The smallest useful input for copy-paste use.
- The connected sources an agent should check before asking the teacher to gather files.
- Any policy, rubric, accessibility, privacy, or LMS constraint that changes the output.

## Agent pre-work before asking the teacher

1. Check whether prof-brain already has the relevant course context.
2. Check whether the LMS, local files, Drive, calendar, or chat source can provide the needed evidence.
3. Summarize what you found and ask the teacher to confirm the source set.
4. If nothing is connected, ask for one small useful sample rather than the whole course.

## The prompt

> You are helping me with [TASK] for [COURSE]. Use only the information I provide or the sources I confirm.
>
> Inputs: [PASTE INPUTS, or read from confirmed connected sources].
>
> Produce: [EXPECTED ARTIFACT].
>
> Put uncertain, missing-evidence, or student-impacting items in a review queue. End with what I must check before trusting the output. Stop before anything reaches students, a gradebook, or an official record.

## What to check before you trust it

- Source fidelity: every important claim traces to supplied or confirmed material.
- Missing context: the output states what it could not see.
- Fairness: the output does not silently penalize phrasing, access limits, section differences, or quiet forms of participation.
- Artifact integrity: calculations, links, IDs, columns, and platform fields are checked.

## The guardrail

AI drafts. The human decides. Nothing reaches a student, gradebook, parent, advisor, published course page, or official record until a human reads it and explicitly approves it.

## Automated version

Describe how a connected agent can gather the inputs, produce the artifact, and pause for review.

## Automate even better

Describe the durable data loop: pull, unify, store, analyze, improve next time.

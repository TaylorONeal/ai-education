---
name: exam-predictor
description: Predict how each student is likely to score on an upcoming exam from their graded coursework and course history, so you can spot who is at risk while you can still act. Use after enough coursework is graded and before the exam, to forecast scores, flag at-risk students, and see which assignments actually predict exam performance.
---

# Exam Predictor

## The problem

You find out who was going to struggle on the exam after they have already struggled on it. By then the intervention you could have offered (a check-in, a study nudge, office hours) is too late. Meanwhile your gradebook already holds the signal: students have done weeks of work that, if you read it right, says a lot about how the exam will go. The catch is that not all of that work predicts equally. A completion-graded reading quiz and a rubric-graded applied analysis are not the same evidence, and treating them the same gives you a confident, wrong forecast.

This skill turns graded coursework into a per-student exam projection with a confidence band and at-risk flags, weighting each assignment by how much it actually predicts.

## What you need

- Your gradebook: scores on the coursework graded so far.
- A map from each exam topic or section to the assignments that exercise the same skill, with a sense of how strongly each assignment predicts that skill (see the README for the weighting model).
- The exam structure: how many points are multiple choice versus open response, and which topics carry weight.
- Optionally, prior course history (past terms) to calibrate the difficulty discount.

You can paste the gradebook and history, or, if the agent is connected to Canvas or your LMS, have it pull the current scores and the prior-term gradebooks itself instead of exporting them by hand. Wherever a prompt below says `[PASTE OR ATTACH SCORES]`, that becomes "read the gradebook from the course." See `../../guides/canvas-lms.md` for Canvas, `../../guides/other-lms.md` for other platforms, and `../../guides/automation.md` for pulling multi-term history.

## What predicts and what is just noise

This is the core of getting it right. Score assignments by how closely they exercise the same cognitive task as the exam:

- Strong predictors: rubric-graded work that does the same thing the exam asks (an applied analysis, a designed test, a worked case). These discriminate, so weight them heavily.
- Moderate predictors: content-aligned but recall-level work (reading quizzes on the right topic).
- Weak predictors: completion-graded work that barely touches the content.
- Not predictors, exclude them: compliance and admin assignments (syllabus acknowledgement, introduce-yourself, choose-a-company) and, critically, any ungraded or practice assignment. Practice work is not a comparable signal and will distort the model. Leave it out.

## The prompt

> You are projecting exam scores for [COURSE] from graded coursework. You do not assign or replace any grade. You produce a forecast for my planning.
>
> Exam structure: [POINTS BY SECTION, e.g. 55 MC / 45 open response, and topic weights].
>
> Here is the gradebook: [PASTE OR ATTACH SCORES].
>
> Here is how assignments map to exam topics, with a predictive weight from 0.5 (weak) to 0.85 (strong, exercises the same skill): [PASTE THE MAP]. Exclude these compliance or practice assignments entirely: [LIST].
>
> For each student:
> 1. Build a multiple-choice proxy from the recall-and-applied assignments and an open-response proxy from the rubric-graded applied work, each as a weighted average using the predictive weights.
> 2. Apply a difficulty discount of [×0.93 default] to reflect that a timed exam is harder than coursework.
> 3. Give a projected MC score, a projected open-response score, a total, a letter grade, and a confidence band whose width reflects how consistent the student has been (consistent student, narrow band; spiky student, wide band).
> 4. Flag at-risk students and why (a zero on a strong-predictor assignment, high quiz but low applied work, an overall low coursework pattern).
>
> End with the projected grade distribution and a short list of students to reach out to first.

## What to check before you trust it

1. Spot-check three students against your own read of their work. If the projection clashes with what you know, trust your read and ask why the model diverged.
2. Calibrate the discount. The default assumes the exam is meaningfully harder than coursework. Run a harder discount as a stress test and see whether the top of the distribution collapses; that tells you how sensitive the forecast is.
3. Confirm you excluded the non-predictive assignments. If compliance, practice, or ungraded work crept into a proxy, the numbers are inflated. Pull them and re-run.
4. Treat the projection as directional. It is a planning tool and an early-warning system, not a grade and not a promise. The band is part of the answer; a wide band means "could land anywhere, watch this one."

## The guardrail

A prediction is a heads-up for you, never a verdict for the student. It does not go in the gradebook, it is never shown to a student, and it never becomes a label that lowers your expectations of someone. Its only legitimate use is to direct your attention and your support before the exam. After the exam, compare projections to actual scores to sharpen the model, and keep that comparison as your calibration record.

## Automated version

Connected to your gradebook, it pulls scores as they post, rebuilds the projection on a schedule, and surfaces a watchlist that updates through the term. Coverage matters: early on, with only a couple of assignments graded, the band is wide and the skill says so. As more graded work lands, the projection tightens. It proposes who to reach out to; you decide what support to offer.

## Automate even better

Point an agentic browser or connector at your full course history, not just this term. Have it pull every past term's gradebook and the matching exam outcomes, unify them into one CSV (`student-cohort, assignment, score, eventual_exam_score`), and use that to learn which assignments actually predicted exam performance in your course rather than guessing the weights. That turns the predictive-weight map from an estimate into something measured against your own history. See `../../guides/automation.md` for the pull-unify-store-analyze pattern and `../../guides/canvas-lms.md` or `../../guides/other-lms.md` for pulling gradebook history.

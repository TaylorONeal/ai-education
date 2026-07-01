---
name: exam-predictor
description: Predict how each student is likely to score on an upcoming exam from their graded coursework and course history, so you can spot who is at risk while you can still act. Use after enough coursework is graded and before the exam, to forecast scores, flag at-risk students, and see which assignments actually predict exam performance.
---

# Exam Predictor

## The problem

You find out who was going to struggle on the exam after they have already struggled on it. By then the intervention you could have offered (a check-in, a study nudge, office hours) is too late. Meanwhile your gradebook already holds the signal: students have done weeks of work that, if you read it right, says a lot about how the exam will go. The catch is that not all of that work predicts equally. A completion-graded reading quiz and a rubric-graded applied analysis are not the same evidence, and averaging them together gives you a confident, wrong forecast: a diligent box-checker looks ready while a strong analyst who skipped an admin task looks shaky.

This skill turns graded coursework into a per-student exam projection with a confidence band and at-risk flags, weighting each assignment by how much it actually predicts.

## What you need

- Your gradebook: scores on the coursework graded so far.
- A map from each exam topic or section to the assignments that exercise the same skill, with a predictive weight for each link (see below).
- The exam structure: how many points are multiple choice versus open response, and which topics carry weight.
- Optionally, prior course history (past terms) to calibrate the difficulty discount.

You can paste the gradebook and history, or, if the agent is connected to Canvas or your LMS, have it pull the current scores and the prior-term gradebooks itself instead of exporting them by hand. Wherever a prompt below says `[PASTE OR ATTACH SCORES]`, that becomes "read the gradebook from the course." See `../../guides/canvas-lms.md` for Canvas, `../../guides/other-lms.md` for other platforms, and `../../guides/automation.md` for pulling multi-term history.

## What predicts and what is just noise

This is the core of getting it right. Score each assignment-to-topic link by how closely the assignment exercises the same cognitive task as the exam, and give the link a predictive weight, not just a yes or no for coverage:

- 0.80 to 0.85, strong predictors: the assignment does the same thing the exam bank does (a designed A/B test predicting the A/B-testing bank, an applied case predicting the applied bank). These discriminate between students; weight them heavily.
- 0.65 to 0.75, moderate predictors: rubric-graded and content-aligned, but a level easier than the exam (a reading quiz or homework on the right topic).
- 0.50 to 0.60, weak predictors: completion-graded work that barely touches the content.
- Excluded entirely, not weighted low, just left out: compliance and admin assignments (syllabus acknowledgement, introduce-yourself, choose-a-company) and any ungraded or practice assignment. Practice work is not a comparable signal and will distort the model if you include it.

For each student and each topic, the projected score there is the weighted average of their normalized scores on the linked assignments. A missing submission counts as zero, unless the assignment was completion-only, in which case halve its weight so a missed low-signal task does not crater the projection. Recording each link's signal type (recall, applied, or engagement) alongside its weight is worth the extra minute: it is what lets you say afterward which of your assignments are the discerning ones worth keeping and which are noise worth cutting.

## Behavioral signals that place a student in their range

Content scores give the center of the projection. Three signals, all computable from the gradebook, give the spread and the tilt:

- Engagement: does the student do more than the minimum (optional steps, on-time submission, substantive discussion)? High engagement means broad preparation and a lower chance they skipped a whole unit. Compute it per topic where you can, since a student can be engaged on the topics that grabbed them and absent on the rest.
- Detail orientation: on rubric-graded work, do they address every sub-criterion? This predicts open-response performance directly, because exam essays are scored on hitting all their parts. A high detail score shifts the open-response projection up; a low one shifts it down even when the content knowledge is there.
- Consistency: how spiky are their scores across assignments? Consistency sets the width of the confidence band. A steady student gets a narrow band and a trustworthy point estimate. A volatile student gets a wide band, because where they land depends on which topics the specific exam draw happens to hit.

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
> 2. Adjust the open-response proxy by the student's detail-orientation pattern (do they hit every sub-criterion, or leave parts unaddressed).
> 3. Apply a difficulty discount of [×0.93 default] to reflect that a timed exam is harder than coursework.
> 4. Give a projected MC score, a projected open-response score, a total, a letter grade, and a confidence band whose width reflects the student's consistency (consistent student, narrow band; spiky student, wide band).
> 5. Flag at-risk students and why (a zero on a strong-predictor assignment, high quiz but low applied work, an overall low coursework pattern).
>
> End with the projected grade distribution and a short list of students to reach out to first.

## Calibrating the model

Calibrate the projection against the exam-rebalance skill's six personas. They are the anchors: the methodical analyst should land high with a narrow band, the bare-minimum student low, the enthusiast wide and middling. If a real student lands somewhere a persona would not, that is a prompt to check your inputs, not the model. A student rarely matches one persona cleanly; they might be the analyst on one topic and the crammer on another, which is exactly why each dimension is scored separately before it composes into one projection.

The difficulty discount defaults to around 0.93. Run a harsher discount as a stress test and see whether the top of the distribution collapses; that tells you how sensitive the forecast is to the assumption.

## What to check before you trust it

1. Spot-check three students against your own read of their work. If the projection clashes with what you know, trust your read and ask why the model diverged.
2. Calibrate the discount. Run a harder discount as a stress test and see whether the top of the distribution collapses; that tells you how sensitive the forecast is.
3. Confirm you excluded the non-predictive assignments. If compliance, practice, or ungraded work crept into a proxy, the numbers are inflated. Pull them and re-run.
4. Treat the projection as directional. It is a planning tool and an early-warning system, not a grade and not a promise. The band is part of the answer; a wide band means "could land anywhere, watch this one."

## The guardrail

A prediction is a heads-up for you, never a verdict for the student. It does not go in the gradebook, it is never shown to a student, and it never becomes a label that lowers your expectations of someone. Its only legitimate use is to direct your attention and your support before the exam, while there is still time to change the outcome it forecast. That is the whole point: a prediction you act on to make false.

## Automated version

Connected to your gradebook, it pulls scores as they post, rebuilds the projection on a schedule, and surfaces a watchlist that updates through the term. Coverage matters: early on, with only a couple of assignments graded, the band is wide and the skill says so. As more graded work lands, the projection tightens. It proposes who to reach out to; you decide what support to offer.

After the exam, compare projections to actual scores. Two payoffs: you sharpen the difficulty discount and the weights for next time, and you learn which assignments truly predicted, which is course-design intelligence in its own right. The assignments that tracked the exam are worth keeping and weighting; the ones that did not are candidates to redesign or drop.

## Automate even better

Point an agentic browser or connector at your full course history, not just this term. Have it pull every past term's gradebook and the matching exam outcomes, unify them into one CSV (`student-cohort, assignment, score, eventual_exam_score`), and use that to learn which assignments actually predicted exam performance in your course rather than guessing the weights. That turns the predictive-weight map from an estimate into something measured against your own history. See `../../guides/automation.md` for the pull-unify-store-analyze pattern and `../../guides/canvas-lms.md` or `../../guides/other-lms.md` for pulling gradebook history.

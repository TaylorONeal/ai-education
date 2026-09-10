# Exam readiness, in depth

Read [SKILL.md](SKILL.md) for the workflow. The default deliverable is a topic-level readiness review, not a guessed exam grade.

## Without historical outcomes

Use pseudonymous IDs and normalize only genuinely graded work with positive possible points. Preserve distinct statuses for missing, excused, ungraded, and inaccessible work. A missing record is not evidence of zero mastery. Report which objectives have evidence and which need a check-in or practice opportunity.

Suggested columns: student identifier, objective, evidence reference, observed result, missing coverage, proposed support, instructor review status. Do not infer personal traits from participation or submission timing.

## With comparable historical outcomes

Freeze a pre-exam cutoff. Split by cohort or time before fitting weights or choosing features. Keep all observations from a student together when necessary to avoid leakage. Fit on training data only, and compare the held-out error with a simple baseline, such as normalized coursework average. Record sample sizes, missingness, exclusions, scale, mean absolute error, and changes in the course or exam.

Practice results may be useful evidence if their collection and scoring are comparable; completion marks do not demonstrate mastery. Test relevance rather than asserting that an assignment type always predicts or never predicts.

A sensitivity range shows what changes under different assumptions. It is not a confidence or prediction interval. Report a prediction interval only with a defined method and held-out coverage. Small or changed cohorts can make numeric forecasts unsuitable; return the readiness review when validation does not support them.

## Worked missing-data check

[STUDENT_A] has a graded zero on [ASSIGNMENT_A], is excused from [ASSIGNMENT_B], and has an ungraded [ASSIGNMENT_C]. Keep the zero as observed performance, exclude the excused work from the applicable denominator, and report the ungraded work as unavailable. None of those states establishes future exam performance.

## The guardrail

Review each support recommendation. Keep identifiable records private, do not add forecasts to grades, and never use them to deny access or lower expectations. Platform access is covered in [the agent guide](../../guides/agents.md).

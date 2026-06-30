# Exam Predictor, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This is the model: how to weight assignments by what they actually predict, the behavioral signals that place a student within their range, how the pieces compose into a projection, and the one rule that keeps a forecast from becoming a label.

## Why most "predictions" are wrong

The naive version averages all coursework and calls it a forecast. It fails because coursework is not uniform evidence. A syllabus-acknowledgement click and a rubric-graded applied analysis both sit in the gradebook, but only one tells you anything about exam performance. Average them together and a diligent box-checker looks ready while a strong analyst who skipped an admin task looks shaky. The fix is to weight every assignment by how closely it exercises the same cognitive task the exam will.

## Part 1: assignment-to-topic predictive weighting

Map each exam topic or bank to the assignments that touch it, and give each link a predictive weight, not just a yes/no for coverage. A working scale:

- 0.80 to 0.85, strong: the assignment exercises the same task the exam bank does (a designed A/B test predicting the A/B-testing bank, an applied case predicting the applied bank). These discriminate between students; lean on them.
- 0.65 to 0.75, moderate: rubric-graded and content-aligned, but a level easier than the exam (a reading quiz or homework on the right topic).
- 0.50 to 0.60, weak: barely touches the content, or is completion-graded.
- Excluded entirely: compliance and admin work (syllabus check, introductions, pick-a-company) and any ungraded or practice assignment. Practice and ungraded work are not comparable signals; including them distorts the model. This is a hard rule, not a preference.

For each student and each bank, the domain score is the weighted average of their normalized scores on the linked assignments. A missing submission counts as zero, unless the assignment was completion-only, in which case halve its weight so a missed low-signal task does not crater the projection.

The "signal type" of each link is worth recording too: recall, applied, or engagement. It tells you what a strong or weak score there actually means, and it is what lets you say, after the fact, which of your assignments are the discerning ones worth keeping and which are noise worth cutting.

## Part 2: behavioral signals that place a student in their range

Content scores give the center of the projection. Three signals, all computable from the gradebook, give the spread and the tilt.

- Engagement: does the student do more than the minimum (optional steps, on-time submission, substantive discussion)? High engagement means broad preparation and a lower chance they skipped a whole unit. Compute it per bank where you can (lab completion for a lab-linked bank), because a student can be engaged on the topics that grabbed them and absent on the rest.
- Detail orientation: on rubric-graded work, do they address every sub-criterion? This predicts open-response performance directly, because exam essays are scored on hitting all their parts. A high detail score shifts the open-response projection up; a low one shifts it down even when the content knowledge is there.
- Consistency: how spiky are their scores across assignments? Consistency sets the width of the confidence band. A steady student gets a narrow band and a trustworthy point estimate. A volatile student gets a wide band, because where they land depends on which topics the specific exam draw happens to hit.

## Part 3: composition and calibration

Compose the projection: build a multiple-choice proxy from the recall-and-applied assignments and an open-response proxy from the rubric-graded applied work, scale each to its exam section, adjust the open-response side by detail orientation, set the band width from consistency, and apply a difficulty discount because a timed exam is harder than untimed coursework. A discount around 0.93 is a sensible default; run a harsher one as a stress test to see how fragile the top of the distribution is.

Calibrate against the exam-rebalance personas. They are the anchors: the methodical analyst should land high with a narrow band, the bare-minimum student low, the enthusiast wide and middling. If your model puts a real student where a persona would not, that is a prompt to check the inputs. A student rarely matches one persona cleanly; they might be the analyst on one topic and the crammer on another, which is exactly why the model scores each dimension separately and composes them.

## The flags that matter

Surface, per student: a zero on a strong-predictor assignment (the single most actionable flag), high quiz scores paired with low applied work (volatile, the quiz inflates the MC projection and the essays may not follow), an overall low-coursework pattern, and anyone projected below passing. These flags are the point. The exact projected number matters less than the list of who to reach out to first.

## After the exam: close the loop

Compare projections to actual scores. Two payoffs. You sharpen the difficulty discount and the weights for next time. And you learn which assignments truly predicted, which is course-design intelligence: the assignments that tracked the exam are the discerning ones worth keeping and weighting; the ones that did not are candidates to redesign or drop. Over a few terms this turns guessed weights into measured ones (see the automation guide for assembling that history into a CSV).

## The guardrail

A prediction is a heads-up for you, never a verdict for the student. It does not enter the gradebook. It is never shown to a student. It must not become a label that quietly lowers your expectations of someone, which is the real ethical risk of any predictive model on people. Its only legitimate use is to aim your attention and your support before the exam, while there is still time to change the outcome it forecast. That is the whole point: a prediction you act on to make false.

## Across learning management systems

The model runs on gradebook data and your assignment map, so it is platform-independent. Pulling the gradebook (and, for the "automate even better" tier, pulling prior terms' gradebooks and exam outcomes into a CSV) is platform-specific; see `../../guides/canvas-lms.md`, `../../guides/other-lms.md`, and `../../guides/automation.md`.

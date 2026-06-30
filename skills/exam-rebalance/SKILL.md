---
name: exam-rebalance
description: Check an exam for difficulty and topic coverage before students take it, simulate how different kinds of student would score, and compare it against every prior version you have, so you catch an unfair or lopsided test while you can still fix it. Use when finalizing a midterm, final, or quiz.
---

# Exam Rebalance

## The problem

You do not know if an exam is too easy or too brutal until students have already taken it, and by then it counts. You also tend to test what is fresh in your mind, so coverage quietly drifts toward this term's favorite topics and away from things you taught months ago. And you rarely compare against last year, so you cannot tell if you have made the test harder or easier without meaning to.

This skill pressure-tests an exam before anyone takes it: it estimates difficulty, maps coverage against your objectives, simulates how a range of students would score, and compares the whole thing to prior versions.

## What you need

- The exam you are about to give: questions, answer options, point values.
- Your list of topics or learning objectives, with rough weight (how much class time each got).
- Prior versions of the exam, if you have them. The more terms, the better the comparison.

You do not have to dig any of this out by hand. You can paste it, or, if the agent is connected to Canvas or your LMS, point it at the course and have it pull the current exam and every prior version itself. Wherever a prompt below says `[PASTE EXAM]` or `[PASTE OR ATTACH PRIOR EXAMS]`, you can instead tell the agent to read them straight from the course. See `../../guides/canvas-lms.md` for Canvas and `../../guides/other-lms.md` for other platforms. Pulling years of past exams in one pass is covered in `../../guides/automation.md`.

## Part 1: Difficulty and coverage check

> You are reviewing an exam for [COURSE] before students take it. Be a skeptical reviewer.
>
> Here is the exam: [PASTE EXAM]
> Here are the topics I taught and roughly how much time each got: [PASTE TOPIC WEIGHTS]
>
> Tell me:
> 1. Difficulty. Rate each question easy / medium / hard, with a one-line reason. Give me the overall mix and flag if it skews too easy or too hard for a [LEVEL] course.
> 2. Coverage vs. emphasis. For each topic, what share of exam points does it carry? Compare that to how much class time it got. Flag any topic that is over-tested or under-tested, and any topic I taught that does not appear at all.
> 3. Bad questions. Flag anything ambiguous, anything with more than one defensible answer, anything where the wording gives away the answer, and any question that tests recall when the objective was application.
> 4. Point weighting. Flag any bank or section where each question is worth more than the others, because one confusing question there does double damage. Those are the first place to look when post-exam complaints come in.
>
> End with a prioritized fix list.

## Part 2: Simulate the test before students do

Instead of a vague "imagine some students," run a fixed cast of six personas. Each one is a recognizable type, named so you can talk about them, and each tests a different thing about the exam. They are invented archetypes, not real students.

> Now play these six students taking this exam. For each, estimate their score section by section, name which questions they miss and why, and give their likely grade.
>
> 1. Marcus W., the Agency Intern. Has done the work in a real job but never learned the formal vocabulary. Strong on applied questions, weak where the exam demands textbook rigor or statistical precision. Tests whether applied experience is rewarded.
> 2. Priya S., the Designer from another major, here because the course is required. Reads carefully, reasons from first principles, but has little domain background. Tests whether the exam is accessible to a capable non-major rather than punishing them for unfamiliarity.
> 3. Devon K., the Analytics Minor. Methodical, re-reads questions, strong on rigor and on "find the flaw" items. Usually the high scorer. Tests the ceiling: does the hardest-working student have room to reach the top?
> 4. Jasmine T., the New Major. Earnest, attends, studies by memorizing terms, strong on recall and shaky on application. Tests the middle: does a prepared but not exceptional student land where you want them?
> 5. Tyler B., the Bare Minimum. Skipped a chunk of class, crammed the night before. Tests the floor: can someone fake their way to a passing grade, or do the open-response questions stop that?
> 6. Casey R., the Enthusiast. Genuinely engaged, but attention runs uneven: deep on the topics that grabbed them, thin on the ones that did not. High variance across sections. Tests whether spiky, real engagement produces an honest middling grade.
>
> Then give me the spread of scores across all six and tell me what it suggests about whether this exam separates understanding from luck, and where the distribution looks wrong.

This gives you a rough score distribution before the exam counts for anyone. A lopsided spread is your signal to rebalance.

## The two levers that fix most spreads

When the simulation comes back lopsided, two changes do most of the work:

- Scaffold open-response questions. An unscaffolded prompt penalizes a student who knows the content but cannot guess the structure you wanted. Breaking each one into two or three explicit sub-questions (define, then apply, then evaluate) lifts the middle of the class without raising the ceiling, because the strong students were already going to hit all three.
- Add one specific, hard-to-fake requirement to protect the floor: make every answer name and define the one course-specific term, source, or piece of evidence it rests on. A crammer can paraphrase a vague version but cannot name and define the real thing, so scaffolding does not accidentally float a disengaged student up to a passing grade. Tailor the requirement to what you teach: an analytics or quant class asks students to name the metric and define it in one sentence; a history class asks them to name the specific event, source, or date and state its significance; a literature class asks them to quote the exact passage and name the device; a science or nursing class asks them to name the mechanism or term and define it. Same lever everywhere, just point it at the kind of specificity only someone who learned your material can supply.

## Calibration targets

Decide, before you look at the simulation, roughly where each archetype should land. A healthy set looks like: the Analytics Minor and the experienced intern reach the top band, the earnest major lands solidly mid, the capable non-major passes without cruising, the enthusiast lands middling on honest partial mastery, and the bare-minimum student does not pass on padding alone. If the simulation puts the floor student comfortably passing, the exam is too guessable. If the hardest worker cannot reach the top band, the ceiling is too low. Either is a reason to rebalance.

A spread of roughly 45 to 50 points from floor to ceiling on a 100-point exam is healthy discriminability. Much tighter and the exam is not separating effort.

## Part 3: Compare against prior semesters

> Here are prior versions of this exam: [PASTE OR ATTACH PRIOR EXAMS].
> Compare the current version to all of them. Tell me: has overall difficulty drifted up or down? Which topics have gained or lost emphasis over time? Are there questions that repeat across versions (a problem if students share old exams)? Are there topics that appeared in past exams but dropped out, and was that intentional? Give me a short trend summary and anything I should correct.

## What to check before you trust it

1. Re-read every question the AI calls ambiguous or hard. Difficulty estimates are rough. Your judgment of your own students wins. Use the flags to find questions worth a second look.
2. Verify the coverage math against your real point values. This is the most useful output, so confirm it is counting correctly before you rebalance.
3. Treat the simulated scores as directional, not predictive. A lopsided spread is a flag to investigate, not a forecast. After the real exam, you can run the same personas against the actual distribution to see whether your calibration held.

## The guardrail

The AI flags and simulates. You decide every point value and every question that stays or goes. When you do rebalance, the AI can help apply the changes across the exam, but you set the weighting. Keep the review, the simulation, and the comparison report so you can show the exam was checked for fairness.

## Automated version

Connected to your LMS, it can pull the live exam structure, run all three parts, write the persona results and the structural-flags report to files, and re-run the personas against the real score distribution after the exam. It proposes adjustments. You approve and apply every one.

## Automate even better

This is the headline use. Point an agentic browser at every past version of the exam across every semester, normalize each question into one CSV (term, question, topic, points, answer key, difficulty if available), then run the Part 3 comparison on years of real data instead of whatever you happened to keep. Five years of exams becomes one trend and a short memo. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

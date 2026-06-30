# Exam Rebalance, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This is the full method: the three checks, the six personas with their profiles and what each one is for, the two levers that fix most lopsided exams, and how to read the spread.

## The problem, stated precisely

You cannot tell whether an exam is too easy or too brutal until students have taken it, and by then it counts. Two quieter failures ride along with that. You test what is fresh in your mind, so coverage drifts toward this term's favorite topics. And you rarely compare against last year, so you cannot tell whether you have made the test harder or easier without meaning to. This skill pressure-tests the exam before anyone takes it.

## Part 1: difficulty and coverage

Rate each question easy, medium, or hard with a reason; report the overall mix; and flag whether it skews wrong for the level. Then map coverage against emphasis: the share of points each topic carries versus the class time it got, with any taught-but-absent topic called out. Then hunt bad questions: ambiguity, more than one defensible answer, wording that gives the answer away, recall questions where the objective was application.

One specific thing to watch: point weighting. If a bank or section is worth more per question than the rest, one confusing question there does double damage. Those are the first place to look when post-exam complaints arrive, so flag them up front.

## Part 2: the six personas

A vague "imagine some students" produces vague results. Run a fixed cast instead, six recognizable types, each named so you can talk about them and each testing a different property of the exam. They are invented archetypes, not real students, which is exactly why they are safe to keep in an open toolkit.

- Marcus W., the Agency Intern. Has done the work in a real job, never learned the formal vocabulary. Strong on applied questions, weak where the exam demands textbook rigor or statistical precision. Tests whether applied experience is rewarded. Target: top band.
- Priya S., the Designer from another major, here because the course is required. Reads carefully, reasons from first principles, thin on domain background. Tests whether a capable non-major can pass without being punished for unfamiliarity. Target: lower-middle, passing, not cruising.
- Devon K., the Analytics Minor. Methodical, re-reads questions, strong on rigor and on find-the-flaw items. Usually the high scorer. Tests the ceiling: does the hardest worker have room to reach the top? Target: top band.
- Jasmine T., the New Major. Earnest, attends, studies by memorizing terms, strong on recall and shaky on application. Tests the middle: does a prepared but not exceptional student land where you want them? Target: solid middle.
- Tyler B., the Bare Minimum. Skipped a chunk of class, crammed the night before. Tests the floor: can someone fake their way to passing, or do the open-response questions stop it? Target: does not pass on padding alone.
- Casey R., the Enthusiast. Genuinely engaged, but attention runs uneven, deep on the topics that grabbed them and thin on the ones that did not. High variance across sections. Tests whether spiky, real engagement produces an honest middling grade. Target: honest middle, reflecting partial mastery.

Ask the model to score each persona section by section, name which questions they miss and why, and give a likely grade. Then ask for the spread across all six and what it says about whether the exam separates understanding from luck.

A note on framing the personas respectfully. They are teaching tools, not caricatures. The non-major persona exists to check accessibility, not to model a student who "should" fail. The enthusiast persona models uneven attention without a clinical label. Keep them that way when you adapt them.

## Calibration targets and the flags to watch

Decide where each archetype should land before you look at the simulation. A healthy set: the rigorous student and the experienced intern reach the top, the earnest major lands solidly mid, the capable non-major passes without cruising, the enthusiast lands middling, and the bare-minimum student does not pass on padding. Then watch for these:

| Concern | What it looks like | What to do |
|---|---|---|
| Floor too low | Bare-minimum persona scores far below passing | Check whether a bank is genuinely inaccessible (bad framing, not content) |
| Floor too high | Bare-minimum persona passes comfortably | The test is too guessable; add applied scenarios and a fakeable-only-if-you-know-it requirement |
| Ceiling too low | The rigorous student cannot reach the top band | The hardest workers are not rewarded; check for unfair or ambiguous items |
| Non-major cruising | The non-major persona scores high | The exam may be vocabulary-heavy without applied filtering |
| Enthusiast outscores the earnest major | Spiky engagement beats balanced study | Decide whether that is what you want the exam to reward |
| Essay spread too tight | Little separation between the floor and the ceiling on open response | The rubric needs sharper criteria |

A spread of roughly 45 to 50 points from floor to ceiling on a 100-point exam is healthy discriminability. Much tighter and the exam is not separating effort.

## The two levers that fix most spreads

- Scaffold open-response questions. An unscaffolded prompt penalizes a student who knows the content but cannot guess the structure you wanted. Breaking each into two or three explicit sub-questions (define, then apply, then evaluate) lifts the middle of the class without raising the ceiling, because the strong students were already going to hit all three.
- Add one specific, hard-to-fake requirement to protect the floor: make every answer name and define the one course-specific term, source, or piece of evidence it rests on. A crammer can paraphrase vaguely but cannot name and define the real thing. Tailor it to your field: name the metric and define it (analytics or quant), name the event or source and its significance (history), quote the passage and name the device (literature), name the mechanism or term and define it (science or nursing). This pairs directly with the grading-assistant skill, which can then check the requirement during grading.

## Part 3: compare against prior versions

Feed in prior versions and ask whether overall difficulty has drifted, which topics gained or lost emphasis, whether any questions repeat across versions (a problem if students share old exams), and whether topics dropped out intentionally. A short trend summary tells you whether the exam is creeping in a direction you did not choose.

## After the exam

Run the same six personas against the actual score distribution to check whether your calibration held. Treat the simulated scores as directional, never as a forecast. The personas are a fairness check, not a prediction engine.

## Across learning management systems

The analysis is platform-independent: it works on the exam text, your topic weights, and prior versions. Applying a rebalance back into a specific system (changing point values, question groups, or pulling the live structure) is platform-specific. For Canvas, the question-group and quiz API gotchas are documented in `../../guides/canvas-lms.md`; other systems are in `../../guides/other-lms.md`.

## The guardrail

The AI flags and simulates. You decide every point value and every question that stays or goes. Keep the review, the simulation, and the comparison report so you can show the exam was checked for fairness before anyone sat it.

# Quiz Builder, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This is the longer version: what separates a discriminating question from trivia, how the bank format works and why, how domain packs make a general tool feel native to your subject, and how to validate a bank before it counts.

## What makes a question discriminate

A bank exists to separate students who understand from students who do not. Recall questions fail at that, because a glossary-memorizer answers them as well as an analyst. The questions that discriminate share a shape:

- A concrete scenario with specific numbers, not an abstract definition. "A campaign drove 340 conversions at $12 CPA on $2,050 spend" beats "What is CPA."
- One defensible answer and three plausible distractors, where each distractor is wrong for a reason you can name: a common misconception, a near-miss calculation, the right idea applied to the wrong metric. A distractor nobody would pick tests nothing.
- An answer that does not telegraph itself. If the correct option is always the longest or the only one with a number, test-wise students score without knowing the material.
- Difficulty that comes from the reasoning required, not from obscurity. A hard question asks for a multi-step inference or a subtle distinction, not a trivia fact nobody would remember.

The real banks this skill is modeled on do exactly this: they pose an A-level-versus-B-level analysis choice, or a "transform this weak statement" task, where the wrong options are the things students actually write.

## The bank format, and why one row per option

The import format is one row per answer option, several rows sharing a `Question_ID`:

```
Source, Question_ID, Question_Type, Learning_Objective, Difficulty, Question_Text, Answer_Text, Is_Correct, Points, Feedback_Correct, Feedback_Incorrect
```

The per-option layout is what LMS import tools expect, and it makes the bank auditable: you can scan every option and its correctness flag in a spreadsheet. `Learning_Objective` tags let you check coverage later. `Difficulty` drives `Points`. The two feedback columns are deliberate and separate: feedback for the student who got it right (why it is right) and feedback for the student who got it wrong (which misconception they fell into). Both attach to the answer, so a student sees the relevant one after answering.

The one hard rule on feedback: it never goes in a neutral-comments field. A neutral comment displays to every student the moment they submit, regardless of their answer, which leaks the correct answer and destroys any retake. Correct-comments and incorrect-comments only show conditionally. This is a real trap documented in the Canvas guide, and it applies on every platform that has an always-visible comment field.

## Domain packs

A domain pack is what lets one general tool generate questions that feel like they came from someone who teaches your subject. It is a short document describing, for one field:

- The entities and decisions that scenarios revolve around.
- The metrics and vocabulary, with realistic number ranges so the scenarios are not absurd.
- The misconceptions that make good distractors in that field.
- A couple of worked example questions in the house style.

The toolkit ships a catalog of packs in `domains/` (see `domains/README.md`): business, marketing, business strategy, analytics, MIS, accounting, supply chain, economics, finance, UX design, product management, game design, and business communications. Pick the one that matches your course, or combine two for a cross-disciplinary course and tell the model which to favor. To add a field, copy any pack's structure and fill in the same sections for nursing, computer science, history, or whatever you teach, then name your pack at generation time. The generator's logic does not change; you are swapping the world it draws scenarios from. This is how the toolkit stays domain-general while still producing subject-native questions, and it is the clean place to grow over time.

## Generate from what you taught

The smartest version does not generate from the model's general knowledge of a topic; it generates from your materials. Point it at the prof-brain skill's notes for the unit, so every question tests something that was actually in your readings, slides, and assignments. That closes the gap where a generic generator writes a perfectly good question about something you never covered, and it keeps the bank aligned to your objectives by construction.

## Validate before it counts

A generated bank is a draft, not a deliverable. Before it is graded:

- Read each question as a skeptic and try to defend a second answer. If you can, fix or cut it.
- Verify any scenario that requires a calculation. Scenario math is exactly what a model gets confidently wrong.
- Check the spread of correct-answer letters so the bank is not accidentally "mostly B."
- Run the whole bank through the exam-rebalance skill's difficulty and persona checks. The personas will tell you if a "hard" question is actually a coin flip, or if a bank is too easy to discriminate.

## The guardrail

AI drafts; you approve every question that counts. A generated item on a graded exam is one you have read, answered yourself, and can defend to a student who challenges it. The generator's speed is not a reason to skip the read; it is what gives you the time to do the read well. Keep the bank and your edits as your record.

## Across learning management systems

The bank format imports into Canvas and most other systems. The push mechanics, and the Canvas-specific question-bank traps (bank-linked groups, the neutral-comments rule, relinking duplicated quizzes), are in `../../guides/canvas-lms.md`; other platforms are in `../../guides/other-lms.md`. The "automate even better" path (assembling every past question into one CSV to find coverage gaps and track item difficulty) is in `../../guides/automation.md`.

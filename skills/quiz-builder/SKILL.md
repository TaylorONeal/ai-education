---
name: quiz-builder
description: Generate scenario-based quiz and exam question banks that discriminate, with one clearly correct answer, plausible distractors, difficulty-scaled points, and per-answer feedback, in a format that imports into your LMS. Use to build or expand a question bank. Domain-selectable; ships with a business pack and is built to add more domains.
---

# Quiz Builder

## The problem

Writing a good question bank is slow, and AI makes it fast in the wrong way. Ask a model for "ten questions on this topic" and you get trivia: definitional recall with one obviously right answer and three throwaway distractors. That tests memory, not understanding, and it does not separate the student who gets it from the student who memorized a glossary. A good bank is scenario-based, has exactly one defensible answer, has distractors that are wrong for diagnosable reasons, is honestly difficulty-labeled, and imports cleanly into your LMS. This skill builds that.

## What you need

- The topics or learning objectives you want to test, ideally pulled from your real materials (the prof-brain skill is the clean source, so questions test what you actually taught).
- A domain to generate in. Ships with a business pack (`domains/business.md`); choose it or another, and add your own (see below).
- Difficulty targets and how many questions per objective.
- Your import format. The default bank format below imports into Canvas and most LMSs.

You can paste your objectives and existing questions, or have a connected agent read them from the source: point it at your materials in Canvas or your LMS, or at the prof-brain knowledge base, and let it pull the objectives and any prior question banks itself. Wherever a prompt below says `[PASTE, or read from the brain]`, that is the option to skip the copy-paste. See `../../guides/canvas-lms.md` for Canvas and `../../guides/other-lms.md` for other platforms.

## The bank format

One row per answer option, so a four-option question is four rows sharing a question id. Columns, matching a honed real bank:

```
Source, Question_ID, Question_Type, Learning_Objective, Difficulty, Question_Text, Answer_Text, Is_Correct, Points, Feedback_Correct, Feedback_Incorrect
```

`Difficulty` is Easy, Medium, or Hard and drives `Points`. `Feedback_Correct` and `Feedback_Incorrect` are the per-answer comments. They go in the correct-comments and incorrect-comments fields, never in a neutral-comments field, because a neutral comment shows to every student on submit and leaks the answer (see `../../guides/canvas-lms.md`).

## The prompt

> You are writing scenario-based question bank items for [COURSE], in the [DOMAIN] domain (use the domain pack I provide for realistic scenarios, entities, and numbers). Write questions that discriminate understanding, not recall.
>
> For each question:
> - Pose a short, concrete scenario with specific numbers, then ask the analytical question.
> - Multiple choice, four options, exactly one defensible answer. The other three are plausible and each wrong for a specific, diagnosable reason (a common misconception, a near-miss calculation, a right-idea-wrong-metric).
> - Make sure the correct answer is not the longest or the only specific one; do not telegraph it.
> - Tag it with its learning objective and a difficulty of Easy, Medium, or Hard, and set points by difficulty: [YOUR SCALE, e.g. Easy 3, Medium 4, Hard 5].
> - Write correct-answer feedback that says why it is right, and incorrect-answer feedback that names the misconception, without restating the answer verbatim.
>
> Topics and objectives: [PASTE, or read from the brain].
> Domain pack: [PASTE domains/business.md or your pack].
> Output as rows in this format: [PASTE THE COLUMN HEADER]. Vary which option letter is correct across questions.

## Domains, and adding your own

A domain pack is a short document that tells the generator what a realistic scenario looks like in that field: the kinds of entities and decisions, the metrics and vocabulary, the realistic number ranges, and what a good distractor looks like there. The toolkit ships a catalog of packs in `domains/` (see `domains/README.md` for the full list): business, marketing, business strategy, analytics, MIS, accounting, supply chain, economics, finance, UX design, product management, game design, business communications, computer science, and statistics. Pick the one that matches your course and paste it into the prompt. For a cross-disciplinary course, combine two packs and tell the model which to favor. To add a field, copy any pack's structure and write the same sections for your subject, then select it at generation time. The skill mechanics do not change; only the pack does. This is how the toolkit stays general while letting you generate questions that feel native to your subject.

## Choosing the company set (concrete, exciting examples)

The packs keep scenarios company-agnostic so they stay general. To make examples land with students, draw the cast from `companies.md`, a catalog of real companies grouped into sets: modern digital and direct-to-consumer, big tech and platforms, traditional and established, retail, and finance and fintech. Choose the set that fits your course and the energy you want (modern-digital tends to feel most relevant to students; traditional suits operations and incumbent analysis), or mix two sets to force a real comparison. Add to the prompt: "Draw scenario companies from the [SET] in companies.md. Keep all numbers invented and plausible; do not state a real company's actual financial results." A question that contrasts a digital-native brand with a legacy firm in the same scenario is one of the most discriminating kinds you can write.

## What to check before you trust it

1. Every question has exactly one defensible answer. Read each one as a skeptic and try to argue for a second option. If you can, fix it or cut it. This is the single most important check.
2. The distractors are plausible and diagnostic. A distractor no one would pick tests nothing. The best ones map to a specific misconception you can name.
3. The numbers compute. Scenario math is exactly what a model gets confidently wrong. Verify any question that requires a calculation.
4. No answer leakage. The correct option is not tell-tale longer or more precise, and no feedback field restates the answer in a way a student sees before answering.
5. Difficulty is honest. Spot-check a few against the difficulty label, and validate the whole bank with the exam-rebalance skill's difficulty and persona checks before it counts.

## The guardrail

AI drafts the questions. You approve every one before it reaches a student. A generated question on a graded exam is a question you have personally read, answered, and can defend if a student challenges it. Keep the bank and your edits as your record. See PRINCIPLES.md.

## Automated version

Connected to your materials and your LMS, it reads the objectives from the brain, generates a bank in the import format, runs the self-checks (one-answer, distractor balance, answer-letter distribution, no leakage), and hands you the bank to review before any push. Pushing into Canvas question banks and the relink traps are in `../../guides/canvas-lms.md`; other systems are in `../../guides/other-lms.md`.

## Automate even better

Pull every past question across every term into one CSV, dedupe near-identical items, and map them against your learning objectives to find what is over-tested and what has no coverage. Then generate only the missing items, and track each question's real item difficulty over time so the bank improves with evidence instead of guesses. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

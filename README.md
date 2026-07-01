# AI Teaching Toolkit

AI helpers for the parts of teaching that eat your week: scoring participation, grading against your rubric, checking AI-generated student work, building exams and quizzes, writing announcements, and keeping all your course knowledge in one place.

You do not need to know how to code. If you can copy and paste, you can use this today.

## Is this for you?

You probably want this if any of these sound like your week:

- You grade participation from memory and a bad feeling that it is not fair.
- You build the same kind of quiz every term and it takes a whole evening.
- You suspect some submitted work was AI-generated but cannot prove it.
- You write the same announcements over and over.
- Your rubric is solid but grading 60 essays at 11pm is not.

If yes, keep reading. The next section gets you a real result in about ten minutes, no setup.

## Your first win in 10 minutes

Start with the easiest one: drafting a class announcement. No accounts, no install.

1. Open any AI chat tool you already have. ChatGPT, Claude, Gemini, Copilot, whatever your school gives you. A free account is fine.
2. Open [`skills/announcement-writer/SKILL.md`](skills/announcement-writer/SKILL.md) in this repo and find the block under "The prompt."
3. Copy that prompt and paste it into the AI chat.
4. Replace the bracketed parts (like `[COURSE]` or `[WHAT YOU WANT TO SAY]`) with your real details.
5. Read what it gives you. Fix anything that does not sound like you, and post it.

That is the whole pattern. Every skill in here works the same way: copy a prompt, fill in your details, read the result before you use it. If that felt easy, [`GETTING-STARTED.md`](GETTING-STARTED.md) walks you through one full task end to end.

New to any of the words here (skill, prompt, connector, agent)? The [`GLOSSARY.md`](GLOSSARY.md) explains each in one plain sentence.

## The three levels: from AI that gives you words to AI that does the work

This is the part that matters most, so read it before you decide this is "just prompts."

Every skill works at three levels. They are not three products. They are three rungs of the same ladder, and they differ in one thing: how much of the busywork you still do yourself.

| Level | What the AI does | What you still do | Setup |
|---|---|---|---|
| 1. Plain AI chat | Thinks and drafts from the prompt you paste | You gather the data and do every click yourself | None |
| 2. AI chat + skills | Thinks like an expert who already knows your method and the traps, same way every time | You still gather and click, but you stop re-explaining | Install a skill once |
| 3. AI that controls your computer, plus skills | Gathers the data, does the clicks, drafts the result, then stops for your sign-off | You review and approve | Connect your tools, or use a computer-control agent |

Level 1 helps, and it is a fine place to start. But be honest about where your time actually goes. With plain chat you are still the one pulling 60 submissions, pasting each into the box, and copying results back out. The thinking got easier. The work did not.

The point of this toolkit is the climb. A skill turns the AI into an expert that does not need re-teaching and does not drift between students. A computer-control agent (Claude Cowork on the desktop, an AI browser extension, or an agentic browser) goes further: it opens your LMS, reads the roster, pulls the activity, does the clicking, and hands you a finished draft to approve. You go from doing the work to checking it. That is where a week actually gets shorter, and it is the part a plain chatbot can never do for you.

You can start at level 1 today and climb whenever you are ready. Setup for levels 2 and 3 lives in the [guides](guides/), and [`GETTING-STARTED.md`](GETTING-STARTED.md) shows the same task done at level 1 and level 3 so you can feel the difference.

## The one rule that makes this safe

AI does the draft. You make the call. Nothing reaches a student without you reading it first.

Every skill is built around that line and ends with a guardrail enforcing it. The AI compiles, flags, drafts, and predicts. You decide. If a skill ever tempts you to skip the read, you are using it wrong. Before you run anything on real student data, read [`PRINCIPLES.md`](PRINCIPLES.md). The short version: feed the model as little as you can, keep yourself in every grading decision, tell your students how AI is used, and never let an AI score or sanction a student without your review.

## What's inside

Each skill is a folder under [`skills/`](skills/) with a `SKILL.md` (the whole skill: the prompt, the method, worked examples, and the guardrail) and a `README.md` (a short description of what it does and what else is in the folder).

| Skill | What it does for you |
|---|---|
| [participation-scoring](skills/participation-scoring/) | Pulls each student's real activity across your channels and scores it on rules you set, instead of a gut feeling |
| [grading-assistant](skills/grading-assistant/) | Applies your rubric, flags correct-but-differently-worded answers, and records why each score |
| [ai-output-checker](skills/ai-output-checker/) | Audits AI-assisted student work for fabricated numbers, invented sources, and pasted-AI artifacts |
| [class-content-analysis](skills/class-content-analysis/) | Reviews your readings, slides, and assignments for gaps, overlap, reading level, and drift across terms |
| [exam-rebalance](skills/exam-rebalance/) | Checks an exam's difficulty and coverage and simulates six kinds of student before anyone takes it |
| [exam-predictor](skills/exam-predictor/) | Forecasts who is at risk from graded coursework, weighting assignments by what actually predicts |
| [announcement-writer](skills/announcement-writer/) | Drafts announcements in your captured voice with the AI tells stripped out |
| [canvas-page-generator](skills/canvas-page-generator/) | Turns plain text into a clean, styled course page, and captures your brand once |
| [quiz-builder](skills/quiz-builder/) | Generates scenario-based question banks that discriminate, in any subject you choose |

Two support skills make the rest sharper:

- [prof-brain](skills/prof-brain/) gathers all your course materials into one organized knowledge base the other skills read from, so you stop pasting the same context.
- [canvas-lms](skills/canvas-lms/) is the operational layer that runs Canvas reliably (login, styled content, grade entry, quiz edits) for any skill that has to land there.

## Why this beats writing your own prompt

The value here is not a clever prompt you could have written yourself. It is the operating knowledge underneath each task, the part that normally takes a semester of trial and error to learn.

Each skill carries the things that go wrong and how to avoid them: that a participation scan reads a quiet-but-active student as a zero unless you reconcile nicknames to your roster, that Canvas SpeedGrader silently drops a grade if you do not commit it with a real keyboard Enter, that a neutral comment on a quiz question leaks the answer to every student, that practice assignments do not predict exam scores and will poison a model if you include them. You do not rediscover these the painful way. They are written down.

You start from a working base, and the AI spends its effort on your actual problem instead of relearning the terrain.

## The guides

The skills stay platform-neutral on purpose so they work on any system. The [guides](guides/) hold the specifics so you do not have to rebuild them:

- [`canvas-lms.md`](guides/canvas-lms.md): login, the forced inline styling, pushing content, the three ways to enter grades and the SpeedGrader save bug, the quiz and question-bank traps.
- [`other-lms.md`](guides/other-lms.md): the same operations for Blackboard, Moodle, Brightspace, Schoology, and Google Classroom.
- [`chat-and-discussion.md`](guides/chat-and-discussion.md): where participation happens and how to pull it, ranked by how workable each source is.
- [`automation.md`](guides/automation.md): the agentic level and the pull, unify, store, analyze pattern.

## Make it yours: domains and companies

[`skills/quiz-builder/domains/`](skills/quiz-builder/domains/) ships fifteen subject packs, and [`skills/quiz-builder/companies.md`](skills/quiz-builder/companies.md) ships a catalog of real companies grouped into sets. They exist so the question generator produces something that feels native to your field on the first try.

They are starters, not limits. A domain can be anything. Copy a pack and write the same sections for nursing, music theory, organic chemistry, constitutional law, whatever you teach. The company catalog is the same idea for scenario flavor, swappable and extensible. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the dead-simple way to add yours and share it back.

## Levels 2 and 3: installed skills and computer control

This is how you reach the top of the ladder. These skills are written as Claude Agent Skills, so you install the folders once and trigger them by name instead of copy-pasting (level 2). From there, a computer-control agent runs them for you (level 3).

Claude Cowork on the desktop is the clearest example of level 3. It can open your files, control your browser, and run these skills, so it does the gathering and the clicking and hands you a draft to approve. The same pattern works with an AI browser extension, an agentic browser, or any computer-use agent. The skills stay the same; the agent just does more of the manual part.

To install the skills, see [`INSTALL.md`](INSTALL.md): one click per skill on Cowork using `.skill` bundles, or one command on Claude Code (`./scripts/install.sh`). Once they are in, just say "help me get started" and the **start-here** skill onboards you: it asks a few questions, offers to pull in your own course materials so the other skills are grounded, and runs your first task end to end.

[`AGENTS.md`](AGENTS.md) is the index an agent reads first: every skill, when to use it, the guides, and the conventions. [`guides/automation.md`](guides/automation.md) explains the computer-control level in detail. None of this is required for the copy-paste path, so there is no wrong place to start.

## Questions

[`FAQ.md`](FAQ.md) answers the common ones: is my student data safe, do I need to code, does it work with my LMS, is using this allowed, what does it cost.

## A note on what this is not

This will not grade your essays for you while you sleep. It will not write your lectures. It is not a replacement for knowing your students. It is a teaching assistant that never gets tired, applies your judgment consistently, carries the lessons you would otherwise learn the hard way, and hands the decision back to you every single time.

## License

MIT. Use it, change it, teach with it. See [`LICENSE`](LICENSE).

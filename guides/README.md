# Platform Guides

The skills in this toolkit are written to be LMS-agnostic on purpose, so a teacher on any system can use them immediately by copy-paste. These guides are the other half: the ready-made, platform-specific details, so you do not have to rebuild the plumbing for your own stack.

The split is deliberate. A skill is the base you use right now. A guide is the specifics for getting that skill wired into your actual platform: how to authenticate, how to read submissions and activity, how to push grades and styled content, and the traps that waste an afternoon if you hit them blind.

## The guides

- `canvas-lms.md`. The deepest one, built from real lessons. Covers authentication (a personal token, or the in-browser session and CSRF token), the forced inline styling the Rich Content Editor requires, pushing page and assignment HTML including the chunking trick for large bodies, entering grades three ways (CSV import, API batch, and SpeedGrader by hand including the keyboard-Enter save bug that silently drops grades), and the quiz and question-bank traps.
- `other-lms.md`. The same operations for Blackboard, Moodle, Brightspace, Schoology, and Google Classroom: auth model, read, push grades, push content, with official-doc links and the spots to verify against your institution's setup.
- `chat-and-discussion.md`. Where participation happens and how to pull per-student activity: LMS discussion forums, Slack, Discord, Microsoft Teams, Google Classroom, Telegram, and WhatsApp, ranked by how workable each is, with the rate limits and the name-matching gotchas that bite every time.
- `automation.md`. The agentic tier every skill points to: use an MCP connector, an AI browser extension, an agentic browser, or a computer-use agent to pull everything (including archived terms the API will not show), unify it, store a CSV, and analyze across semesters and years.

## Which skill points where

| Skill | Guide it relies on |
|---|---|
| participation-scoring | chat-and-discussion.md (plus the LMS guides for forum activity) |
| grading-assistant | canvas-lms.md and other-lms.md (getting grades back in) |
| ai-output-checker | canvas-lms.md and other-lms.md (pulling a submission's raw HTML) |
| class-content-analysis | any LMS guide (pulling materials) |
| exam-rebalance | canvas-lms.md and other-lms.md (applying a rebalance); automation.md (all past exams to CSV) |
| exam-predictor | canvas-lms.md and other-lms.md (gradebook); automation.md (prior-term history) |
| announcement-writer | chat-and-discussion.md and the LMS guides (posting) |
| canvas-page-generator | canvas-lms.md (pushing pages) and other-lms.md |
| quiz-builder | canvas-lms.md and other-lms.md (pushing banks); automation.md (coverage gaps) |
| prof-brain | all guides (ingesting materials and reading pages); automation.md (pull everything) |

Every skill also has an "Automate even better" section pointing to `automation.md`.

There is also an operational `canvas-lms` skill under `skills/` that turns this Canvas guide into something an AI agent can run directly. The guide is the reference; the skill is the doer.

## A note on accuracy

API endpoints are stable but every platform ships changes, and every institution configures access differently. Each guide links the official documentation and flags where you must confirm against your own instance. Treat these as a strong starting point that saves you the discovery work, not as a substitute for your platform's current docs.

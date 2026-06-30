# AGENTS.md

Instructions for AI agents (and humans) working in this repo. Read this first, then the skill or guide you need. If you are setting up or extending the toolkit, the conventions at the bottom are not optional.

What this toolkit is for: the value is the skills, the automations, and the hard-won lessons baked into them, so an agent starts from a working base instead of rediscovering the terrain. The domain packs and the company catalog are starter examples, not the point; a domain can be any subject, and the casts are swappable. Spend your effort on the user's actual problem, not on relearning what the skills already encode.

## The one rule

AI does the draft. You make the call. Nothing reaches a student without a human reading it first. Every skill ends with a guardrail enforcing this. If a change you are about to make would let an AI grade, sanction, or message a student without a human in the loop, do not make it.

## Skill index: what to reach for

| Skill | Use it when | Folder |
|---|---|---|
| participation-scoring | Grading participation fairly from real activity across channels, DMs, meetings | `skills/participation-scoring/` |
| grading-assistant | Applying a rubric consistently and catching correct-but-differently-worded answers; producing the grading spreadsheet | `skills/grading-assistant/` |
| ai-output-checker | Auditing AI-assisted student work for fabricated or impossible numbers, invented sources, and pasted-AI artifacts | `skills/ai-output-checker/` |
| class-content-analysis | Auditing your own course materials for gaps, overlap, reading level, alignment, and drift across terms | `skills/class-content-analysis/` |
| exam-rebalance | Checking an exam's difficulty and coverage, simulating six student personas, and comparing against prior versions before anyone takes it | `skills/exam-rebalance/` |
| exam-predictor | Forecasting who is at risk on an upcoming exam from graded coursework, weighting assignments by what actually predicts | `skills/exam-predictor/` |
| announcement-writer | Drafting class announcements in your captured voice with the AI tells stripped | `skills/announcement-writer/` |
| canvas-page-generator | Turning plain text into a clean, styled course page; capturing brand guidelines | `skills/canvas-page-generator/` |
| quiz-builder | Generating scenario-based question banks that discriminate, in a selectable domain | `skills/quiz-builder/` |
| prof-brain | Ingesting all course materials into one organized knowledge base the other skills read from | `skills/prof-brain/` |
| canvas-lms | Operating Canvas reliably from an agent: auth, styled content, grade entry, quiz edits | `skills/canvas-lms/` |

Each skill folder has a `SKILL.md` (the prompt and short how-to, usable immediately) and a `README.md` (the in-depth method, examples, lessons learned). Some carry extra files (grading-assistant ships a spreadsheet template, quiz-builder ships domain packs, canvas-page-generator ships a brand-guidelines template).

## Guides: the platform and automation specifics

The skills are LMS-agnostic on purpose. The guides hold the wiring so an educator does not rebuild it.

- `guides/canvas-lms.md` when working with Canvas: authentication, the forced inline styling, pushing content, the three ways to enter grades and the SpeedGrader save bug, quiz and question-bank traps.
- `guides/other-lms.md` for Blackboard, Moodle, Brightspace, Schoology, Google Classroom: auth, read, push grades, push content.
- `guides/chat-and-discussion.md` for participation and announcement sources: LMS forums, Slack, Discord, Teams, Google Classroom, Telegram, WhatsApp, ranked by viability, with rate limits and name-matching gotchas.
- `guides/automation.md` for the agentic tier that every skill points to: drive a browser or connector to pull everything, unify it, store a CSV, analyze across terms.

## The three automation tiers

Every skill works at three levels, shown in the skill files as the prompt, the "Automated version", and "Automate even better":

1. Copy-paste: paste the prompt into any AI tool. Zero setup.
2. Connected: an MCP or API connector does the repetitive pulls and pushes.
3. Agentic: an AI browser extension, an agentic browser, or a computer-use agent gathers everything (including archived terms the API will not show), unifies it, and stores it as durable data. See `guides/automation.md`.

Use whatever automation surface the user has. The pattern is the same regardless of brand.

## prof-brain is the context layer

When grounding any skill, prefer reading from the prof-brain knowledge base over asking the user to paste materials again. class-content-analysis, exam-rebalance, exam-predictor, quiz-builder, and announcement-writer all sharpen when pointed at the brain. Keep student PII out of the brain.

## Conventions you must follow

- Generic by design. No real student names, no institution branding, no course or quiz IDs, no file paths. Placeholders only: `[COURSE]`, `[ROSTER]`, `[RUBRIC]`, `[COURSE_ID]`, and so on. The persona first names in exam-rebalance are invented archetypes and are allowed.
- Voice. No em dashes, ever. Avoid inflated words (pivotal, crucial, leverage, foster, delve, robust, seamless). Conversational, concrete, lived-experience tone.
- Single source of truth. Prompts live once, in the skills. The cookbook is generated from them by `cookbook/build-cookbook.js`. Never hand-edit `AI-Teaching-Cookbook.docx`. Change a skill, then regenerate.
- Structure. Every skill keeps its sections, including the guardrail. The teaching skills use: the problem, what you need, the prompt, what to check, the guardrail, the automated version, automate even better. Operational skills (canvas-lms, prof-brain) follow the same shape adapted to their job.

## Adding or changing a skill

1. Create `skills/<name>/SKILL.md` with the full section structure, and a `README.md` deep dive.
2. Keep it LMS-agnostic; put platform specifics in a guide and link to it.
3. If it is a copy-paste teaching or authoring skill, add it to the `ORDER` array in `cookbook/build-cookbook.js`. Operational skills stay out of the cookbook.
4. Regenerate the cookbook: `cd cookbook && npm install docx && node build-cookbook.js`.
5. Run the four gates before calling it done.

## The four gates (run before shipping)

1. PII scan: no real name, course code, institution reference, or path in any skill, guide, the cookbook, or the article.
2. Voice sweep: zero em dashes; none of the banned words except where a prompt deliberately lists them as words to cut.
3. Cookbook integrity: prompts in the docx match the skills word for word (the docx is generated, not hand-edited).
4. Structure: every skill has its sections, including the guardrail.

## Continuity

`STATUS.md` is the running log of what is done, what is decided, and what is open. Update it after any significant change so a fresh session can resume.

# STATUS: AI Teaching Toolkit merge

Working directory: `~/Class/ai-education/` (this folder). This is the local repo that maps to https://github.com/TaylorONeal/ai-education (currently empty, not yet pushed).

Last updated: 2026-06-30.

## Update (2026-06-30, sixth pass: teacher-first onboarding + OSS scaffold)

Reframed the front door for medium-low technical teachers, added the open-source scaffolding, and expanded the grading-assistant skill with a worked example and two explicit finish modes.

- Rewrote `README.md` as a funnel instead of an essay: an "Is this for you?" hook, a 10-minute first win (announcement-writer, zero setup), and the value thesis and skill index moved below the fold. Kept tool-agnostic positioning at level 1.
- Reframed the three automation tiers around effort reduction, per the decision that a plain LLM misses most of the point. The new framing is a ladder: level 1 plain AI chat (you still do the gathering and clicking), level 2 AI chat plus installed skills (expert, consistent, no re-teaching), level 3 an AI that controls your computer plus skills (it gathers and clicks, you approve). Claude Cowork is named as the headline example of level 3, alongside AI browser extensions and agentic browsers. This is the "AI that gives you words vs AI that does the work" story.
- New `GETTING-STARTED.md`: a no-assumptions walkthrough of one full task, plus a side-by-side of participation scoring at level 1 vs level 3 so the effort difference is concrete.
- New `GLOSSARY.md`: one plain sentence each for AI tool, skill, prompt, connector/MCP, agent, Cowork, computer-control agent, LMS, roster, rubric, bucket, floor, guardrail, PII, and more.
- New `FAQ.md`: data safety, do I need to code, is it allowed, does it work with my LMS, cost, is this only for business, what is Cowork, the AI made something up.
- New `CONTRIBUTING.md`: leads with the easiest contribution (add your subject pack, ~1 hour, no Git required via issue), the one rule, skill conventions, the voice rules, and the four gates. Includes a light code of conduct.
- New `.github/ISSUE_TEMPLATE/`: bug_report, new_subject_pack (paste-a-draft path for non-Git teachers), new_skill, and config.yml with helper links.
- Voice swept all new files: zero em dashes, no banned words except the two intentional uses (a quoted "utilize" as a word a teacher would never say, and the banned-word list itself in CONTRIBUTING).
- Expanded `skills/grading-assistant/SKILL.md`: added a "How it works, one student start to finish" worked example (two students, including the differently-worded catch) and a "Two ways to finish" section. Mode 1 (default) produces the spreadsheet only and never touches the LMS, scores labeled as estimates. Mode 2 (opt-in) enters grades into Canvas but requires the grade column be hidden first (Grade Posting Policy Manual / crossed-eye indicator confirmed), enter-while-hidden, review the distribution, then the teacher manually Posts. The agent stops at "entered but hidden"; releasing is the human action. Mirrored a short version into the grading-assistant README. The worked-example student answers are plain italic text, not blockquotes, so the cookbook does not render them as fake prompt boxes.
- Regenerated the cookbook (`node build-cookbook.js`), now ~16 pages, since a SKILL.md prompt section changed. The Mode 1 prompt addendum is a real blockquote and now appears in the cookbook.
- Added a "pull from the tool instead of paste" option to the "What you need" section of five skills (exam-rebalance, class-content-analysis, exam-predictor, quiz-builder, prof-brain). Wherever a teacher would gather and paste prior exams, materials, gradebooks, or sources, they can instead point a connected agent at Canvas or the LMS and have it read them from the course. Each note points to canvas-lms.md / other-lms.md / automation.md. These edits are in "What you need," which the cookbook builder excludes, so no cookbook regen was needed (the copy-paste cookbook stays scoped to non-connected users).

Decision this pass: kept level 1 tool-agnostic (any AI tool) per Taylor's call, but did NOT bury Cowork. Cowork and computer control are framed as the top of the ladder and the real point of the toolkit, since plain copy-paste barely reduces the manual work. The two are reconciled: agnostic on-ramp, computer-control destination.

Still local only. The new files are NOT yet pushed to GitHub (see Left to do).

## Update (2026-06-07, fifth pass)

Documentation pass to reframe the toolkit around its real value. Rewrote the top README to lead with the thesis: the asset is the skills, the automations, and the hard-won lessons baked in, so you do not start from scratch and an agent can focus on the actual problem. The domain packs and company catalog are explicitly framed as starters, extensible to any subject. Reinforced the same framing in AGENTS.md and the domains catalog. Added computer-science and statistics packs (fifteen packs total). No skill SKILL.md changed this pass, so the cookbook is unchanged.

## Update (2026-06-07, fourth pass)

- Generalized the floor-protecting requirement lever beyond analytics. It now reads as "name and define the one course-specific term, source, or piece of evidence the answer rests on," with field versions (analytics: name the metric; history: name the event or source and its significance; literature: quote the passage and name the device; science or nursing: name the mechanism). Updated in exam-rebalance and grading-assistant, both SKILL and README.
- Added twelve quiz-builder domain packs in `skills/quiz-builder/domains/`: marketing, business-strategy, analytics, mis, accounting, supply-chain, economics, finance, ux-design, product-management, game-design, business-communications, plus a `domains/README.md` catalog and instructions to combine or add packs. The original `business.md` remains as the umbrella pack. Added computer-science and statistics packs as well (fifteen packs total). quiz-builder SKILL and README now point to the catalog. Domain packs are not in the cookbook (they are reference material, not prompts).
- Added `skills/quiz-builder/companies.md`, a reusable catalog of real public companies grouped into sets (modern digital and DTC, big tech and platforms, traditional and established, retail, finance and fintech) so scenarios use concrete, current, student-relevant examples. The packs stay company-agnostic; the catalog supplies the cast, chosen per course (traditional, modern, or mixed). This is the one file where real brand names intentionally live; the PII gate excludes it for brand names. The prompt instruction tells the model to keep all numbers invented and never state a real company's actual results.

## Update (2026-06-07, third pass)

Added the agentic tier, two new skills, a knowledge base, and an agent index:

- `guides/automation.md`: the "automate even better" tier (MCP, AI browser extensions, agentic browsers, computer-use), with the canonical pull, unify, store a CSV, analyze-across-terms pattern. Every skill now has an "Automate even better" section pointing to it.
- New `skills/exam-predictor/`: forecasts exam scores from graded coursework, weighting assignments by what actually predicts (applied work discriminates; compliance and practice work is noise and is excluded). Behavioral signals, difficulty discount, confidence band, at-risk flags, persona calibration, and the hard rule that a prediction is a heads-up, never a label.
- New `skills/quiz-builder/`: scenario-based question-bank generator, domain-selectable, ships a business pack at `domains/business.md`, built to add domains. The old `canvas-quiz-builder` repo could not be fetched (private or empty), so this was built from the existing question-bank materials and the Canvas lessons; fold in the old repo if it becomes accessible.
- New `skills/prof-brain/`: ingests all course materials (local, Drive, LMS reading pages, syllabus, slides, exams) into an organized Markdown knowledge base with an index, optionally synced to Notion or an Obsidian vault. It is the context layer the other skills read from.
- grading-assistant now ships `grading-template.xlsx` in the honed format (per question: answer, score, notes for why; sub-questions in the notes; total; flags), documented in the SKILL and README.
- canvas-page-generator now captures brand guidelines: pull palette and type from a university site, the course, or an inspiration source via a browser surface, store as `brand-guidelines.md` (template shipped), and feed it to every page.
- New root `AGENTS.md`: the one rule, a skill index with when-to-use, the guides, the automation tiers, prof-brain as context layer, the conventions, and how to add a skill.

Cookbook now covers nine teaching and authoring skills (added exam-predictor and quiz-builder). prof-brain and canvas-lms stay out of the cookbook as operational skills. Total skills: eleven.

## Update (2026-06-07, second pass)

Added depth and platform coverage on top of the merged v1:

- Every skill now has its own in-depth `README.md` alongside its `SKILL.md`. The SKILL is the immediate-use prompt; the README is the full method, worked examples, edge cases, and lessons learned.
- New `guides/` folder of ready-made platform specifics so educators do not rebuild the plumbing: `canvas-lms.md` (deep, from the real lessons learned: forced inline `!important` styling, the two auth paths, pushing pages with large-body chunking, three ways to enter grades including the SpeedGrader keyboard-Enter save bug, and the quiz and question-bank traps), `other-lms.md` (Blackboard, Moodle, Brightspace, Schoology, Google Classroom, grounded by web search with official-doc links), and `chat-and-discussion.md` (Slack, Discord, Teams, LMS forums, Google Classroom, Telegram, WhatsApp, ranked by viability, for participation and announcements).
- New operational `skills/canvas-lms/` skill (SKILL.md + README) that turns the Canvas guide into something an agent can run directly.
- Every skill README now points to the relevant guide(s) so the base skill stays usable immediately and the specifics are one link away.
- ai-output-checker gained an explicit section on pasted-HTML AI artifacts (the case where quiz answers arrive carrying AI copy-paste markup), framed as a signal, not proof, with the full source-by-source detection guide in its README.
- participation-scoring now names its real sources (LMS forums, Slack, Discord, Teams, university tools, Google Classroom, WhatsApp, Telegram) and points to the chat-and-discussion guide.

Decisions this pass: the `canvas-lms` skill is operational, not a copy-paste teaching prompt, so it is deliberately NOT in the cookbook (the cookbook stays the seven teaching skills). The non-Canvas guides are grounded by web search and link official docs, with explicit "verify against your instance" notes, since I do not have lived lessons for those platforms the way I do for Canvas. All guides use placeholders only (no course IDs, quiz IDs, or paths).

## What the first pass did

Merged the detailed real source material on this machine into the generic v1 that lived in Google Drive. Drive was treated as read-only (the only generic copy; the prior local working copy was built on a different machine and is not on this one). All real source skills and grading docs were read, not edited.

## Done

- Pulled generic v1 (README, PRINCIPLES, LICENSE, article, 7 skills, cookbook README) into this working dir from Drive.
- Merged real detail into all 7 skills, stripping every real name, course code, and institution reference to placeholders. Each skill keeps the six-section structure (problem, what you need, the prompt, what to check, the guardrail, automated version), and every skill keeps its guardrail.
- README updated with the repo link and a per-skill-folder layout note.
- Article: filled the repo link. Left the cookbook and companion-article links as placeholders (open question 3, not published yet).
- Cookbook regenerated from the skills via `cookbook/build-cookbook.js` (Node + docx). Output: `cookbook/AI-Teaching-Cookbook.docx`, about 12 pages.
- STATUS file (this one) written for continuity.

## Decisions made this session (flag if you disagree)

1. Skill layout changed from flat `name.SKILL.md` files (Drive v1) to per-skill folders `skills/<name>/SKILL.md`. Reason: that is the installable format for Claude Agent Skills and the README already described "skill folders." Not a reversal of a core decision, an alignment to the stated install method.
2. canvas-page-generator palette genericized. The real skill uses a specific university red/teal/gold dark theme, which is institution branding. Kept all the valuable structure (the real LMS-editor constraints, component patterns, accent cycling, accessibility, three page types) but replaced the branded palette with placeholders and a neutral, accessible default. This honors "generic by design."
3. exam-rebalance personas: kept six, named, each linked to an archetype (per your call that name plus archetype is fine). Reframed the sixth from a clinical "ADHD" label to "the Enthusiast" whose attention runs uneven across topics, to keep it respectful and avoid pathologizing. The capable non-major persona is framed as testing accessibility, not as a failing student.

## Open questions status

1. Hallucination story (article). NOT resolved from source. The source has a real instructor-side fabrication example (a student submitted an impossible "146.78% conversion rate" and did not catch it), which is now woven into the ai-output-checker skill. But there is no "a student caught AI fabricating data" moment anywhere in the source. So the article's illustrative "42 percent vs 28" number is left as-is. If you want a real anchor, the 146.78% story is the closest true one, but it is the inverse of the article's framing (a student failing to catch, not catching). Your call whether to swap it in.
2. Persona count. RESOLVED. Six, named, in exam-rebalance: Marcus W. (Agency Intern), Priya S. (Designer from another major), Devon K. (Analytics Minor), Jasmine T. (New Major), Tyler B. (Bare Minimum), Casey R. (Enthusiast).
3. Three article links. Repo link filled. Cookbook link and companion-article link left as placeholders until those are published.
4. Companion article (how the platform was built). Out of scope, not written.

## Left to do

- Push to GitHub. The sandbox does not sync new files back to the Mac git, and git ops should be run from the Mac terminal, not the sandbox. From the Mac: `cd ~/Class/ai-education`, then `git init`, add the remote `https://github.com/TaylorONeal/ai-education.git`, commit, push.
- If you want a PDF of the cookbook, open the .docx and export, or add a PDF step to the build script.
- Decide the hallucination-story swap (open question 1).

## How to resume

Everything is in this folder. The skills are the single source of truth. To change any prompt: edit the skill, then `cd cookbook && npm install docx && node build-cookbook.js` to regenerate the cookbook. Never hand-edit the .docx.

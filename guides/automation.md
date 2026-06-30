# Automation Guide: from copy-paste to fully agentic

Every skill in this toolkit works at three levels of automation. The skill files show the bottom two. This guide is the top one, the "automate even better" tier each skill points to.

## The three tiers

1. Copy-paste. You paste the prompt into any AI tool, fill in the placeholders, read the result. Zero setup. This is the base, and it is genuinely useful on its own.
2. Connected (MCP or API). The AI is wired to your tools through connectors and does the repetitive pulls and pushes for you: read a roster, pull a submission, post a grade. This is the "Automated version" section in each skill.
3. Agentic. The AI drives a real, logged-in browser or your desktop to gather everything that is not sitting behind a clean API, unifies it, stores it as durable data, and analyzes across terms. This is the tier most people never reach by hand because the gathering is too tedious. It is exactly the part an agent is good at.

## The surfaces (use whatever you have)

This tier is tool-agnostic. Pick the surface you already use:

- MCP connectors: structured access to an LMS, chat tool, or calendar through an API. Fast and precise when the data is in current scope.
- An AI browser extension that drives your logged-in browser (for example, Claude in Chrome and similar). It reads and acts on the actual page DOM, so it reaches anything you can see when logged in, including archived courses and old terms that the API may not expose.
- An agentic browser (for example, Perplexity's Comet and similar): a browser that navigates and extracts on instruction.
- A computer-use agent that controls the desktop directly: the most general, the slowest, the fallback for native apps and anything with no web surface.

The pattern below is the same regardless of which one you use. Choose by what your data lives behind, not by brand.

## The canonical pattern: pull everything, unify, store, analyze

The move that turns a one-time answer into a durable asset:

1. Pull everything. Point the agent at the source and have it walk every item, not just this term's. For exams, that means navigating to each past exam across every semester you can reach and extracting it. The browser surfaces shine here, because old and archived material is usually reachable in the logged-in UI even when it is out of the current API's scope.
2. Unify the format. Different terms were built differently. Have the agent normalize every item into one consistent shape: the same fields, the same units, the same labels. Inconsistent source, consistent output.
3. Store it as a CSV. Write the unified data to a CSV (or a small set of them) that lives in your own files. This is the durable artifact. It outlives the session, it is auditable, and every future analysis reads from it instead of re-scraping.
4. Analyze across semesters and years. With the CSV in hand, the cross-term questions become trivial: has difficulty drifted, which topics gained or lost weight, which questions repeat across versions, how did the score distribution move. The analysis runs on clean data instead of a pile of PDFs.

### Worked example: every past exam into one dataset

Goal: understand how your midterm has drifted over five years.

- Pull: the agent logs into your LMS in the browser, navigates to each prior course shell, opens each midterm, and extracts every question, its options, its point value, and the answer key.
- Unify: each question becomes a row with the same columns: `term, exam, question_id, topic, type, points, stem, answer_key, item_difficulty_if_available`.
- Store: write `past-exams.csv`.
- Analyze: feed the CSV to the exam-rebalance skill's comparison step, or just ask for the trend: average difficulty by term, topic weight by term, repeated questions across versions, dropped topics. Five years of exams becomes one chart and a short memo.

The same shape works for a full gradebook history (for exam-predictor), every discussion-forum post across a term (for participation-scoring), or every reading and assignment across terms (for class-content-analysis).

## What "pull everything" means per skill

- exam-rebalance: every past version of the exam, into one CSV, for real cross-year difficulty and coverage drift.
- exam-predictor: the full gradebook and assignment history, unified, so the model trains on every graded signal you have.
- class-content-analysis: every reading, slide deck, and assignment across terms, so the drift analysis is real and not from memory.
- participation-scoring: the complete post and message history across every channel for the window, assembled once.
- grading-assistant: the entire submission stack pulled into one place for a first pass.
- ai-output-checker: every submission's raw HTML, for artifact detection at scale.
- announcement-writer and canvas-page-generator: push across all channels or all pages, not one at a time.

## Guardrails for this tier

The human gate does not loosen because the automation got stronger. It matters more.

- Verify the unified data before you trust it. Spot-check a handful of rows against the original source. A scrape that silently mangled a column will poison every downstream analysis.
- Keep the CSV as your record. It is the auditable artifact behind any claim you make from it.
- Mind rate limits and permissions. Browser surfaces sidestep API rate limits but are slower per item and can trip site protections; pace them. Only pull what you have the right to access.
- Nothing reaches a student without your read, exactly as in every skill. Agentic gathering is about assembling your evidence faster, not about handing the decision to the machine.

## Where the platform specifics live

How to authenticate and what to click or call is in the platform guides: `canvas-lms.md`, `other-lms.md`, and `chat-and-discussion.md`. This guide is the pattern; those are the wiring.

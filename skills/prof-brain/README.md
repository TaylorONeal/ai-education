# Prof Brain, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This is the longer version: why a file-based brain beats the alternatives, how to use an optional source inbox before building the notes, the note schema in detail, how to ingest each kind of source, how the Notion and Obsidian sync actually works, and how the rest of the toolkit reads from it.

## Why a folder of Markdown, and not something cleverer

The instinct is to throw everything into a vector database and call it a knowledge base. For a single course owned by one person, that is the wrong tool. A folder of Markdown notes is inspectable (you can read any note), portable (it is just files), version-controllable, editable by hand, and readable by every AI tool without special infrastructure. The intelligence is not in a hidden index; it is in how the notes are written and linked. This follows the file-based memory idea: small atomic notes, a human-readable index that loads into context, and links that turn the pile into a graph. The index is the part that scales, because an agent reads the index first and then pulls only the handful of notes a task needs, which is what keeps a large brain usable inside a limited context window.

## Optional source inbox

Before writing the Markdown brain, ask the teacher whether they want the agent to create a staging folder of copied originals. This is optional, but useful when the materials are scattered across Canvas, another LMS, Drive, and old local folders. The rule is copy first, do not move or delete originals unless the teacher explicitly asks.

Recommended structure:

```
[COURSE]-source-inbox/
  2026-spring/
    syllabus/
    readings/
    assignments/
    exams/
    slides/
    lms-pages/
  2025-fall/
    ...
  _intake-log.csv
```

The intake log should include `source`, `term`, `type`, `title`, `status`, `destination`, and `notes`. Use it as the audit trail. It should show what the agent copied, exported, skipped as a duplicate, could not access, or could not read cleanly.

## The note schema

Every note is one Markdown file with frontmatter:

```
---
title: <human title>
type: reading | assignment | exam | policy | slide | concept
source: <original URL or file path, so you can always trace it back>
term: <when used, if relevant>
tags: [topic, topic]
---

A faithful, plain-language summary of the item. For an assignment, include the rubric.
For a concept, define it in your own words in a sentence or two. Link related notes with
[[Other Note Title]]. Link liberally; a link to a note that does not exist yet marks
something worth writing.
```

Two structural files sit above the notes. INDEX.md is one line per note (title, type, a hook) and is the first thing any agent reads. OVERVIEW.md is the course in a page: what it is, its arc, the big ideas, so a fresh agent gets oriented before it dives.

## The folder tree

```
brain/
  INDEX.md
  OVERVIEW.md
  syllabus/      policies, schedule, grading, logistics, and syllabus analysis
  readings/      one note per reading or LMS reading-module page
  assignments/   one note per assignment, rubric included
  exams/         past and current exams, normalized into structured notes
  slides/        decks summarized to text
  glossary/      one concept per note, defined in your terms
```

## Syllabus analysis

A syllabus should produce both a note and an analysis. The note captures what the syllabus says. The analysis catches what a teacher needs to fix before the next term: vague policies, date conflicts, grading math issues, missing workload expectations, objectives that never appear in assignments, assignments with no objective, and schedule pressure points.

Write the analysis to `syllabus/syllabus-analysis.md`. Include a short section called `Recommended next steps` that names whether to run syllabus-creator, schedule-generator, class-content-analysis, exam-rebalance, or quiz-builder next. If the analysis needs current or upcoming semester dates and they are not in the sources, ask the user rather than guessing.

## Finding related past courses

When the agent has browser access to Canvas or another LMS, it should not stop at the current course shell. Ask it to find related past-semester shells the teacher can access, then organize source copies by term before writing notes.

Recommended search order:

1. Start from the current course URL or dashboard card. Record the visible course title, short name, term, teacher role, and LMS course URL.
2. Open the all-courses or past-enrollments view and search for matching titles, abbreviations, department patterns, and reused course names.
3. Include only shells the teacher can access and that are plausibly the same course or a predecessor. If unsure, mark `needs teacher review` in `_intake-log.csv` instead of ingesting it as fact.
4. For each related shell, walk modules, pages, files, assignments, quizzes, rubrics, and exams. Include announcements only if they contain durable course policies or schedule context. Do not ingest student submissions, rosters, grades, or discussion posts into the brain.
5. Export or copy originals into the optional source inbox by term and type, then create the Markdown notes from that organized source set.

## Ingesting each kind of source

- Local folders: read each document, summarize to a note, keep the file path in `source`. PDFs and Word docs get their text extracted; flag any that came through garbled.
- Google Drive: pull each file's text through the Drive connector, same treatment. Keep the Drive link in `source` so the note traces back.
- LMS reading-module pages: these are web pages, so render them through a browser surface (an AI browser extension or an agentic browser) rather than a raw fetch, because a reading page is usually client-rendered and a raw fetch returns a navigation shell. Extract the actual content, preserve the LMS URL in `source`, and copy the page export or clean text into the optional source inbox when used. See `../../guides/canvas-lms.md` and `../../guides/automation.md`.
- Syllabus: split it into atomic policy notes (grading, late work, attendance, schedule) rather than one giant note, so each policy can be linked and updated on its own.
- Slides: summarize each deck to text, one note per deck or per topic, since slide bullets are not self-explanatory.
- Past exams: normalize into structured notes (one per exam, or one per question if you want the granularity), which is exactly the format the exam-rebalance and exam-predictor skills want to read.

## Syncing to Obsidian

An Obsidian vault is a folder of Markdown with `[[wikilinks]]`. This skill already writes that, so the sync is trivial: open the brain folder as a vault. You get backlinks and graph view for free, and the files stay the source of truth. The only thing to get right is that note titles and wikilink targets match, which the build step handles.

## Syncing to Notion

Notion is a published view, not the source of truth; keep the on-disk Markdown canonical so you can always rebuild. The agent steps, through the Notion API or MCP connector:

1. Create a parent page per top-level folder (Readings, Assignments, Exams, and so on).
2. Create a child page per note, with the note body as content.
3. Turn INDEX.md into a database whose properties are the frontmatter fields (type, term, tags), so you can filter and sort the brain in Notion.
4. On refresh, update changed pages rather than duplicating. Match on title or a stored note id.

The reason to keep Markdown canonical: Notion is harder to diff, back up, and feed to other tools. The brain should survive any one app.

## Keeping it fresh

A brain is only as trustworthy as its staleness. Re-ingest a source when it changes, prune notes whose source is gone, and merge duplicates the moment you spot them. The automated version does this on a schedule and reports what it changed, so the brain never silently diverges from your real course.

## How the rest of the toolkit reads from it

The brain is the shared, grounded context layer. Instead of pasting materials into each skill every time, point the skill at the relevant corner of the brain:

- class-content-analysis reads `readings/` and `assignments/` against your objectives.
- exam-rebalance and exam-predictor read `exams/` and the rubrics in `assignments/`.
- announcement-writer reads `syllabus/` for dates and policies.
- grading-assistant reads the rubric in an assignment note.

This is the payoff: build the brain once, and every other skill gets sharper because it is working from your actual materials instead of a fresh paste each session.

## The guardrail

The brain holds course knowledge, not student records. Keep rosters, grades, and individual student work out of it, especially anything synced to a third-party tool. Student-facing analysis belongs in the skills built to handle it under their own guardrails. The brain is the one place that should be safe to share with a colleague or sync to Notion without exposing a single student.

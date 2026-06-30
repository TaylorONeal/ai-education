# Prof Brain, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This is the longer version: why a file-based brain beats the alternatives, the note schema in detail, how to ingest each kind of source, how the Notion and Obsidian sync actually works, and how the rest of the toolkit reads from it.

New to this? Here is the whole idea in plain terms. A course brain is a tidy filing cabinet for one course, except an AI can read the entire cabinet at once. You gather the materials you already have (syllabus, readings, assignments, slides, old exams) into a handful of plainly named folders, and the AI writes a short, faithful summary of each item plus an index that ties them together. You do not need to code or install anything special to start; a folder on your computer and an AI chat tool are enough. Once it exists, every other skill in the toolkit gets sharper, because it can read your real materials instead of a fresh copy-paste each time. The four ways to actually fill the brain (drag files into folders by hand, ask a computer-control agent like Claude Cowork to sort them, connect Google Drive, or pull straight from Canvas) are spelled out in the "Getting your materials in" section of [`SKILL.md`](SKILL.md). The rest of this page is the detail behind that.

## Why a folder of Markdown, and not something cleverer

The instinct is to throw everything into a vector database and call it a knowledge base. For a single course owned by one person, that is the wrong tool. A folder of Markdown notes is inspectable (you can read any note), portable (it is just files), version-controllable, editable by hand, and readable by every AI tool without special infrastructure. The intelligence is not in a hidden index; it is in how the notes are written and linked. This follows the file-based memory idea: small atomic notes, a human-readable index that loads into context, and links that turn the pile into a graph. The index is the part that scales, because an agent reads the index first and then pulls only the handful of notes a task needs, which is what keeps a large brain usable inside a limited context window.

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
  syllabus/      policies, schedule, grading, logistics
  readings/      one note per reading or LMS reading-module page
  assignments/   one note per assignment, rubric included
  exams/         past and current exams, normalized into structured notes
  slides/        decks summarized to text
  glossary/      one concept per note, defined in your terms
```

## Ingesting each kind of source

- Local folders: read each document, summarize to a note, keep the file path in `source`. PDFs and Word docs get their text extracted; flag any that came through garbled.
- Google Drive: pull each file's text through the Drive connector, same treatment. Keep the Drive link in `source` so the note traces back.
- LMS reading-module pages: these are web pages, so render them through a browser surface (an AI browser extension or an agentic browser) rather than a raw fetch, because a reading page is usually client-rendered and a raw fetch returns a navigation shell. Extract the actual content. See `../../guides/canvas-lms.md` and `../../guides/automation.md`.
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

---
name: prof-brain
description: Build a professor's knowledge base by ingesting all your course source material (local folders, Google Drive, LMS reading pages, syllabus, slides, past exams) into one well-organized folder of Markdown notes with an index, so you and every other skill can read from one grounded source. Use to set up or refresh the brain, and optionally sync it to Notion or an Obsidian vault.
---

# Prof Brain

## The problem

Your course knowledge is scattered. The syllabus is a PDF, the readings are LMS pages, the assignments are in one folder, the slides in another, last year's exams somewhere in Google Drive, your policies half in your head. Nothing can read all of it at once, so you re-explain context to an AI every time, and the answer to "what do my own materials actually say about this" takes an afternoon of digging. Every other skill in this toolkit works better when it is grounded in your real materials, and right now there is no single grounded place to point it at.

This skill ingests everything into one organized folder of Markdown notes with an index, a course brain you and your tools can read. It is the memory layer the rest of the toolkit draws on.

## What you need

- Pointers to your sources: the local folders, the Google Drive folders, the LMS reading-module pages (URLs), the syllabus, the slide decks, and any past exams or course docs.
- A destination folder for the brain (a plain folder on disk is enough).
- Optionally, a Notion workspace or an Obsidian vault if you want it synced there too.

You do not have to track down every URL and file yourself. If the agent is connected to Canvas or your LMS, you can point it at the course and have it find the reading-module pages, assignments, and past exams on its own, instead of listing each source by hand. See `../../guides/canvas-lms.md` for Canvas, `../../guides/other-lms.md` for other platforms, and `../../guides/automation.md` for walking every past term in one pass.

## What it builds

One note per source item, in a consistent folder tree, each note a Markdown file with frontmatter so it is findable and an agent can load only what it needs.

```
brain/
  INDEX.md          one line per note: title, type, and a hook (this is what loads into context)
  OVERVIEW.md       the course in one page: what it is, the arc, the big ideas
  syllabus/         policies, schedule, grading, logistics
  readings/         one note per reading or LMS reading-module page
  assignments/      one note per assignment, with its rubric
  exams/            past and current exams, normalized
  slides/           lecture decks, summarized to text
  glossary/         atomic notes, one concept per file, defined in your terms
```

Each note carries frontmatter and links to related notes:

```
---
title: Conversion Funnel Reading
type: reading            # reading | assignment | exam | policy | slide | concept
source: <original URL or file path>
term: <when it was used, if relevant>
tags: [e-commerce, funnel, metrics]
---

The substance of the note in your own words. Link related notes with [[Open Rate]] and
[[E-Commerce Assignment]] so the brain becomes a graph, not a pile.
```

## The prompt

> You are building my course knowledge base for [COURSE] as a folder of Markdown notes. Ingest the sources I list and turn each item into one note.
>
> Sources: [LOCAL FOLDERS], [DRIVE FOLDERS], [LMS READING PAGE URLS], [SYLLABUS FILE], [SLIDE DECKS], [PAST EXAMS].
>
> For each item, create a Markdown note with frontmatter (title, type, source, term, tags), a faithful summary in plain language, and wiki-style links to related notes. Keep one concept per glossary note. Do not merge unrelated items.
>
> Then write INDEX.md (one line per note: title, type, and a one-line hook) and OVERVIEW.md (the course in one page). Flag any source you could not read cleanly so I can check it.

## The memory philosophy

This is a file-based brain on purpose, not a black-box index. The design rules keep it useful as it grows:

- Atomic notes. One reading, one assignment, one concept per file. Small notes are easier to update, link, and load selectively than one giant document.
- An index that loads into context. INDEX.md is the map an agent reads first, then it pulls only the few notes it needs. The index is the thing that makes a large brain usable in a limited context window.
- Canonical, single source. Each fact lives in one note. Other notes link to it rather than restating it, so the brain never contradicts itself.
- Link liberally. A link to a note that does not exist yet is fine; it marks something worth writing. The graph is where the value compounds.
- Prune and merge. When two notes cover the same thing, merge them. When a source changes, update its note. A stale brain is worse than no brain.

## Syncing to Notion or Obsidian (optional)

- Obsidian: an Obsidian vault is just a folder of Markdown with `[[wikilinks]]`, which is exactly what this builds. Point Obsidian at the brain folder and it works natively, graph view and all. No conversion needed. Agent instruction: write the notes with wikilinks and tell the user to open the folder as a vault.
- Notion: push each note as a page, preserving the folder tree as a page hierarchy, and turn INDEX.md into a database with the frontmatter fields as properties (type, term, tags). Agent instruction: use the Notion API or MCP connector to create a parent page per folder, a child page per note, and a database for the index; keep the on-disk Markdown as the source of truth and treat Notion as a published view, so you can always rebuild it.

## What to check before you trust it

1. Verify extraction fidelity on a few notes, especially LMS pages and PDFs. A reading page that rendered as a navigation menu, or a PDF that came through garbled, makes a confidently wrong note. Check the flagged ones first.
2. De-duplicate. If the same reading exists in two sources, you want one note, not two that will drift.
3. Keep it current. Re-ingest a source when it changes. Treat the brain as living; an outdated policy note is a liability.

## The guardrail

The brain is course knowledge, not a student record. Keep student PII out of it: no rosters, no grades, no individual student work, especially in anything you sync to a third-party tool like Notion. If you want student-facing analysis, that belongs in the skills that handle it with their own guardrails, not in a shared knowledge base. See PRINCIPLES.md.

## Automated version

Connected to your local folders, Google Drive, and LMS, it ingests on a schedule, adds notes for new material, updates notes whose sources changed, and keeps the index and overview current. It tells you what it added or changed so the brain never silently drifts from your real materials.

## Automate even better

Point an agentic browser at your LMS and have it walk every reading-module page across every term you can reach, plus your Drive history, and ingest all of it in one pass, unifying old and new into the same note format. Past exams go through the same flow the automation guide describes (pull every version, normalize, store), landing in `exams/` as structured notes the exam-rebalance and exam-predictor skills can read directly. See `../../guides/automation.md`, and `../../guides/canvas-lms.md` or `../../guides/other-lms.md` for reaching LMS reading pages.

## How the rest of the toolkit uses it

Once the brain exists, point the other skills at it instead of pasting context each time: class-content-analysis reads the readings and assignments, exam-rebalance and exam-predictor read the exams and rubrics, announcement-writer reads the schedule and policies, grading-assistant reads the rubrics. The brain is the shared, grounded context that makes every other skill sharper.

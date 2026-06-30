---
name: prof-brain
description: Build a professor's knowledge base by ingesting all your course source material (local folders, Google Drive, LMS reading pages, syllabus, slides, past exams) into one well-organized folder of Markdown notes with an index, so you and every other skill can read from one grounded source. Use to set up or refresh the brain, and optionally sync it to Notion or an Obsidian vault.
---

# Prof Brain

## The problem

Your course knowledge is scattered. The syllabus is a PDF, the readings are LMS pages, the assignments are in one folder, the slides in another, last year's exams somewhere in Google Drive, your policies half in your head. Nothing can read all of it at once, so you re-explain context to an AI every time, and the answer to "what do my own materials actually say about this" takes an afternoon of digging. Every other skill in this toolkit works better when it is grounded in your real materials, and right now there is no single grounded place to point it at.

This skill ingests everything into one organized folder of Markdown notes with an index, a course brain you and your tools can read. It is the memory layer the rest of the toolkit draws on.

Think of it as a tidy filing cabinet for one course, except an AI can read the whole cabinet at once. You build it by collecting the materials you already have into a set of plainly named folders, then letting the AI write a short, faithful summary of each item. You do not need to code, and you do not need to install anything special to begin. A folder on your computer and an AI chat tool are enough. If you can make a folder and drag a file into it, you can build the first version of this today. The "Getting your materials in" section below gives you four ways to fill it, from doing it by hand to letting a connected agent pull everything from Canvas for you.

## What you need

- Pointers to your sources: the local folders, the Google Drive folders, the LMS reading-module pages (URLs), the syllabus, the slide decks, and any past exams or course docs.
- A destination folder for the brain (a plain folder on disk is enough).
- Optionally, a Notion workspace or an Obsidian vault if you want it synced there too.

You do not have to gather all of this by hand, and you do not have to do it all at once. The "Getting your materials in" section below lays out the easiest path for your setup, from dragging files into folders to letting a connected agent pull everything from your LMS.

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

## Getting your materials in (pick the one that fits you)

There are four ways to fill the brain, from most hands-on to most hands-off. Start with whatever you already have in a pile, use the path that matches your comfort and your tools, and add more later. They line up with the same levels the rest of the toolkit uses: do it yourself, or hand more of it to the AI.

1. By hand: make the folders and drop files in. Create a folder called `brain` with the subfolders shown above (`syllabus`, `readings`, `assignments`, `exams`, `slides`, `glossary`). Then drag each file into the folder it belongs in: the syllabus into `syllabus`, last year's tests into `exams`, your slide decks into `slides`, each reading into `readings`. When the files are sorted, point an AI chat tool at the folder and run the prompt below, and it turns each file into a note. This path needs no special tools. If you can make folders and drag files, you can do it.

2. Let a computer-control agent sort it for you. If you use Claude Cowork or another AI that can control your computer, you can skip the dragging. Point it at the messy folder where your course files already live and tell it: "Build a course brain. Put each file in the right folder (syllabus, readings, assignments, exams, slides), then summarize each one into a note." It does the sorting and the summarizing; you check the result.

3. Connect Google Drive and let it pull. If your materials live in Google Drive, connect the Drive connector and tell the agent which folders to read. It pulls each file's text, sorts it, and writes the notes, keeping the Drive link on each note so you can always trace it back. Nothing to download or drag.

4. Pull straight from Canvas or your LMS. If the agent is connected to your LMS, you do not have to find and download anything. Point it at the course and it reads the reading-module pages, assignments, and past exams where they live. See [`../../guides/canvas-lms.md`](../../guides/canvas-lms.md) for Canvas, [`../../guides/other-lms.md`](../../guides/other-lms.md) for other platforms, and [`../../guides/automation.md`](../../guides/automation.md) for walking every past term in one pass.

You can mix these. Drag in the few files you have on your laptop, connect Drive for the rest, and let it pull the readings from Canvas. The brain ends up in the same shape no matter how the material got there, so there is no wrong order and no penalty for starting small.

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

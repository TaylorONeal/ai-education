---
name: class-content-analysis
description: Audit your own course materials (readings, slides, assignments) for gaps, overlap, reading level, and alignment to your learning objectives. Use when you want a content review you would never find time to schedule, before a term starts or after it ends.
---

# Class Content Analysis

## The problem

Nobody audits their own course. You build it once, then patch it term by term, and over a few years it drifts. Two readings now cover the same thing. A learning objective you list is never actually assessed. One unit reads at a graduate level and the next reads like a pamphlet. You cannot see this from inside it, and you never have a free week to step back and check.

This skill is the outside reviewer you cannot afford to hire. It reads your materials against your stated objectives and tells you where the gaps, overlaps, and mismatches are.

## What you need

- Your list of learning objectives for the course or unit.
- The materials: readings, slide decks, assignment prompts, whatever students actually receive.
- Prior versions of the course or its key assessments, if you have them. The comparison is where the most useful findings come from.

You can paste or attach all of this, or skip the file-gathering entirely: if the agent is connected to Canvas or your LMS, point it at the course and have it pull the readings, slides, assignments, and prior versions itself. Wherever a prompt below says `[PASTE OR ATTACH ...]`, that becomes "read it from the course." See `../../guides/canvas-lms.md` for Canvas and `../../guides/other-lms.md` for other platforms. The prof-brain skill is the cleanest version of this: ingest everything once, then point this skill at the brain.

## The prompt

> You are reviewing the materials for [COURSE]. Be a tough, specific reviewer, not a cheerleader.
>
> Here are my learning objectives:
> [PASTE OBJECTIVES]
>
> Here are the materials students receive:
> [PASTE OR ATTACH MATERIALS]
>
> Tell me:
> 1. Coverage gaps. Which objectives are stated but never taught or assessed? Quote where each objective should appear and does not.
> 2. Overlap. Where do two or more materials cover the same ground in a way that wastes student time? Be specific about which ones.
> 3. Reading level. Flag any material that is noticeably harder or easier than the rest, with the rough grade level of each and which ones are outliers.
> 4. Assessment alignment. For each objective, name the assignment or assessment that actually measures it. If none exists, say so.
> 5. Sequence. Anything that depends on a concept introduced later, or introduces a term before defining it.
>
> Give me a prioritized list of fixes, hardest-hitting first.

## Map content to categories and weigh it

The alignment table gets sharper when you group materials into the categories you actually think in, then compare weight to emphasis. Add this when you want the coverage math:

> Group every reading, slide deck, and assignment into these categories: [LIST YOUR TOPIC CATEGORIES]. For each category, tell me how many materials cover it, how much assessment weight it carries, and roughly how much class time it gets. Flag any category that is heavily taught but barely assessed, or heavily assessed but barely taught.

A category that eats three weeks of class but shows up in two points of assessment is a real misalignment, and it is invisible until you lay the weights side by side.

## Compare against prior versions

If you have past versions, the drift is the story:

> Here are prior versions of this course's materials and assessments: [PASTE OR ATTACH]. Compare the current version to them. Which topics have gained or lost emphasis over time? Which objectives quietly dropped out, and was that intentional? Has the overall reading level crept up or down? Give me a short trend summary and anything I should correct.

If you have performance history (which topics students consistently struggle with across terms), feed that in too and ask the model to flag any category that is both hard for students and under-supported in the materials.

## A worked example

Feed in eight readings, three slide decks, your assignment prompts, and six objectives. The audit reports that objective 4 ("interpret a conversion funnel") appears in two readings and a lecture but in no assignment, that readings 3 and 6 both teach the same framework with 80% overlap, and that reading 5 sits two grade levels above the rest. Your prioritized fix: build or repurpose one assignment to assess objective 4, cut or merge one of the overlapping readings, and either scaffold or replace reading 5. Three concrete moves, none of which you would have scheduled time to find on your own.

## What to check before you trust it

1. Verify each "gap" against your full materials. The AI only sees what you paste. A gap may just mean you forgot to include a file. Confirm before you rewrite a unit.
2. Judge the reading-level calls yourself. Grade-level estimates are rough. Use them to find outliers worth reading, not as gospel.
3. Sanity-check the alignment and category math against your real assessment weights. This is the most valuable output. If an objective genuinely has no assessment, that is a real finding worth acting on.
4. Treat trend claims as directional. The model is inferring emphasis from what you gave it, not measuring it. Confirm a drift is real before you act on it.

## The guardrail

This is advice, not a mandate. You know your students and your constraints. Treat the output as a sharp colleague's review: take the findings that hold up, discard the ones that miss context, and you decide what changes.

## Automated version

Point it at your course folder or LMS and it can pull every reading, slide, and assignment, build the category-and-weight table, run the alignment check, and diff against last term's version on a schedule. It produces a report you read. It never edits your materials or your syllabus on its own.

## When to run it

Once before the term to catch gaps while you can still fix them, and once after to capture what drifted. Keep each report. Comparing this year's to last year's shows you whether your patches are improving the course or just moving the problems around.

## Automate even better

Have an agentic browser walk every reading, slide deck, and assignment across every past term you can reach, unify them into one dataset, and run the drift analysis on real material instead of memory. This pairs naturally with the prof-brain skill, which turns that same pull into a durable, organized knowledge base. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

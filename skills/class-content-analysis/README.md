# Class Content Analysis, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This is the longer version: the five checks explained, how to turn a vague "review my course" into a weighted, comparable audit, and how to use it across terms so you can tell whether your patches are helping.

## Why nobody catches their own drift

You build a course once, then patch it term by term. Over a few years it drifts: two readings cover the same ground, an objective you list is never assessed, one unit reads at a graduate level and the next reads like a pamphlet. You cannot see this from inside it, and you never get a free week to step back. This skill is the outside reviewer you cannot afford to hire.

## The five checks

1. Coverage gaps. Objectives you state but never teach or assess. Ask the model to quote where each should appear and does not, so a "gap" is a specific location, not a vibe.
2. Overlap. Two or more materials covering the same thing in a way that wastes student time. Specific file names, not "some redundancy."
3. Reading level. Materials noticeably harder or easier than the rest, with a rough grade level per item so you can find the outliers worth reading yourself.
4. Assessment alignment. For each objective, the assignment or assessment that actually measures it. The most valuable single output. If an objective has no assessment, that is a real finding.
5. Sequence. Anything that depends on a concept introduced later, or uses a term before defining it.

End every run with a prioritized fix list, hardest-hitting first, so the report is a to-do, not a wall.

## Make it weighted, not just a list

The alignment check gets much sharper when you group materials into the categories you actually think in, then compare weight to emphasis. Ask the model to bucket every reading, slide deck, and assignment into your categories and report, per category, how many materials cover it, how much assessment weight it carries, and roughly how much class time it gets. A category that eats three weeks of class and shows up in two points of assessment is a real misalignment, and it is invisible until the weights sit side by side.

If you keep performance history (which topics students consistently miss, term over term), feed it in and ask the model to flag any category that is both hard for students and thin in the materials. That is the place where adding support helps most.

## Use it across terms

The drift is the story, so keep every report. Run it once before the term to catch gaps while you can still fix them, and once after to capture what moved. Then compare this year's report to last year's: which topics gained or lost emphasis, which objectives quietly dropped out and whether that was intentional, whether the overall reading level crept. That comparison tells you whether your patches are improving the course or just relocating the problems. Difficulty benchmarks built from several terms of data make the "this is getting harder" claim concrete instead of a hunch.

## A worked example

You feed in eight readings, three slide decks, your assignment prompts, and six objectives. The audit reports that objective 4 ("interpret a conversion funnel") appears in two readings and a lecture but in no assignment, that readings 3 and 6 both teach the same framework with 80% overlap, and that reading 5 sits two grade levels above the rest. Your prioritized fix: build or repurpose one assignment to assess objective 4, cut or merge one of the overlapping readings, and either scaffold or replace reading 5. Three concrete moves, none of which you would have scheduled time to find.

## Across learning management systems

This operates on your course materials and objectives, so it is fully platform-independent. If you want it to pull your materials automatically rather than paste them, the connector specifics for each system (Canvas, Blackboard, Moodle, Brightspace, Schoology, Google Classroom) are in `../../guides/`. The base prompt works immediately with copy-paste, no connector required.

## The connected version

Pointed at your course folder or LMS, it pulls every reading, slide, and assignment, builds the category-and-weight table, runs the alignment check, and diffs against last term's version on a schedule. It produces a report you read. It never edits your materials or your syllabus on its own.

## The guardrail

This is advice, not a mandate. You know your students and your constraints. Treat it as a sharp colleague's review: take the findings that hold up, discard the ones that miss context, and you decide what changes. Verify each gap against your full materials before you rewrite a unit, because the AI only sees what you gave it.

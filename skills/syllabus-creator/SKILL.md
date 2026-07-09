---
name: syllabus-creator
description: Draft a clear, complete syllabus from course goals, policies, assessments, schedule constraints, and the prof-brain knowledge base. Use when building a new course syllabus or refreshing one for an upcoming term.
---

# Syllabus Creator

## The problem

A syllabus is part promise, part map, and part policy document. It is easy to copy last term's file, miss an old date, leave a policy vague, or build a schedule that does not match the assignments you actually plan to use. Students feel that mess first, and you spend the term answering questions the syllabus should have handled.

This skill drafts a usable syllabus from your course goals, materials, policies, assessments, and calendar constraints. It works best after prof-brain has ingested the course, because then the syllabus is drawn from the materials you really teach instead of a blank template.

## What you need

- Course basics: [COURSE], [LEVEL], [MODALITY], [TERM], meeting pattern, credit hours, and any required catalog language.
- Learning objectives, major topics, assessments, grading weights, and required policies.
- Calendar constraints: first day, last day, holidays, exam windows, no-class dates, drop dates if you include them.
- Existing syllabus or prof-brain folder, if available.
- Tone preference: concise, warm, strict, detailed, or another style.

If dates are not available in the brain or in what you provide, the agent should ask for the current or upcoming semester dates before drafting the schedule section. Do not invent institutional dates.

## The prompt

> You are drafting a syllabus for [COURSE]. Use my existing course materials if provided, especially the prof-brain knowledge base. If any required dates, institutional policies, or grading rules are missing, ask me before drafting rather than inventing them.
>
> Course basics: [COURSE BASICS]
> Existing materials or prof-brain path: [PASTE OR ATTACH, OR SAY NONE]
> Required policies: [PASTE POLICIES]
> Assessments and grading weights: [PASTE ASSESSMENTS]
> Calendar constraints: [PASTE DATES, OR ASK ME]
> Tone: [TONE]
>
> Draft a complete syllabus with these sections: course description, learning objectives, materials, how the course works, assessments and grading, weekly outline, communication expectations, late work, attendance or participation, academic integrity and AI use, accessibility and support, and what students should do first.
>
> After the draft, give me a review checklist of what I must verify before sharing it with students, including dates, policy language, grading math, accessibility language, and any institution-required text.

## What to check before you trust it

1. Dates. Verify every class date, deadline, holiday, and exam window against the official academic calendar.
2. Policies. Compare required policy language against your institution's current language. Do not trust a draft for legal, accessibility, or conduct wording.
3. Grading math. Confirm weights total correctly and match the LMS gradebook you plan to use.
4. Alignment. Make sure every major assessment supports at least one learning objective, and every objective appears in the course work.
5. Tone. Read it like a student. Cut anything that sounds colder, vaguer, or more punitive than you intend.

## The guardrail

The syllabus is a draft until the instructor approves it. The AI must not publish it to the LMS, email it, or present it as official policy without human review. Required institutional language, accessibility statements, legal policies, and dates must be verified by a human.

## Automated version

Connected to prof-brain, local files, and the LMS, the agent can pull the existing syllabus, assignments, rubrics, course pages, and term shell dates, then draft a refreshed syllabus and a verification checklist. It stops at a draft and asks for approval before pushing anything to Canvas or another LMS.

## Automate even better

Use prof-brain first to ingest past syllabi, assignments, readings, exams, and policies across terms. Then use this skill to draft the new syllabus from the organized brain, and pass the weekly outline to schedule-generator so dates, topics, readings, assignments, quizzes, and exams become a spreadsheet you can inspect before building pages or modules.

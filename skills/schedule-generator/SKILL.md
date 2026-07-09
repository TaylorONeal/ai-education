---
name: schedule-generator
description: Create a detailed course schedule table or spreadsheet from a syllabus, prof-brain memory, term dates, meeting pattern, topics, readings, assignments, quizzes, and exams. Use after syllabus creation or analysis when you need the week-by-week plan.
---

# Schedule Generator

## The problem

The syllabus may say what the course covers, but the actual teaching plan lives in a messy mix of dates, topics, readings, assignment launches, due dates, quizzes, exams, holidays, and review days. If that schedule is wrong, everything downstream breaks: Canvas modules, announcements, gradebook dates, and student expectations.

This skill turns the course plan into a detailed spreadsheet-style schedule that a human can review, revise, and then use to build the LMS.

## What you need

- Current or upcoming semester dates: first class, last class, meeting days, holidays, no-class dates, exam window, and any fixed deadlines.
- Course topics and subtopics, preferably from prof-brain or an approved syllabus.
- Readings, assignments, quizzes, exams, projects, and other deliverables.
- Pacing rules: review days, buffer days, project workdays, lab days, or limits on how much can be assigned at once.

If current or upcoming semester dates are already in memory or prof-brain, use them and cite the source in the notes column. If not, ask the user for dates before generating the table. Do not invent a semester calendar.

## The prompt

> Create a detailed schedule for [COURSE] for [TERM]. Use prof-brain or the approved syllabus if available. If the current or upcoming semester dates are missing, ask me for the first class date, last class date, meeting pattern, holidays, no-class dates, and exam window before drafting.
>
> Course memory or syllabus: [PASTE OR ATTACH, OR READ FROM PROF-BRAIN]
> Meeting pattern: [DAYS/TIMES]
> Term dates and no-class dates: [DATES, OR ASK]
> Major topics and subtopics: [TOPICS]
> Readings and materials: [READINGS]
> Assignments, quizzes, exams, projects: [ASSESSMENTS]
> Pacing preferences: [PREFERENCES]
>
> Output a spreadsheet-ready Markdown table with these columns: Week, Class Date, Unit, Topic, Subtopics, In-Class Activity, Reading or Prep Due, Assignment Released, Assignment Due, Quiz or Exam, Learning Objective, Notes, Source.
>
> After the table, give me a conflict report: overloaded weeks, missing readings, objectives with no activity or assessment, assignments due before they are taught, dates that need confirmation, and recommended fixes.

## What to check before you trust it

1. Dates. Verify every meeting date against the official calendar and your actual meeting pattern.
2. Workload. Look for weeks with too many readings, deliverables, or exams.
3. Sequence. Confirm students practice a skill before an assignment or quiz asks them to use it.
4. Alignment. Every learning objective should appear in topics, activities, and assessment.
5. LMS fit. Check that releases and due dates match how you plan to build modules, pages, and gradebook columns.

## The guardrail

The schedule is a planning draft. The AI must not publish dates, create LMS modules, or change due dates without human approval. The instructor verifies the calendar and workload before students see it.

## Automated version

Connected to prof-brain, the syllabus, and the LMS, the agent can read the current course structure, pull or ask for the upcoming term dates, draft the schedule table, export it as CSV, and flag conflicts. It stops for human review before any LMS changes.

## Automate even better

After approval, an agentic browser can use the reviewed schedule to build Canvas modules, pages, assignment shells, quiz placeholders, and announcements. Keep the CSV as the source of truth, and require a final human review before publishing modules or releasing dates.

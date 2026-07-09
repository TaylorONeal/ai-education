# Schedule Generator, in depth

This skill creates the spreadsheet version of a course plan. It is meant to run after syllabus-creator, syllabus analysis inside prof-brain, class-content-analysis, exam-rebalance, or quiz-builder has clarified what the course should contain.

## Inputs that matter most

The schedule is only as good as the calendar. Give it the official term dates, meeting pattern, no-class dates, and exam window. If those are not in prof-brain, the agent should ask for them before drafting.

## Recommended columns

Use the default columns from the skill unless your department needs more: Week, Class Date, Unit, Topic, Subtopics, In-Class Activity, Reading or Prep Due, Assignment Released, Assignment Due, Quiz or Exam, Learning Objective, Notes, Source.

The Source column is important when the schedule is drawn from memory. It tells you whether a row came from an approved syllabus, a prior Canvas shell, prof-brain, or a user-provided date list.

## Using the conflict report

The conflict report is where the skill becomes useful. It should call out overloaded weeks, missing readings, objectives with no activity or assessment, due dates before instruction, and dates that need confirmation. Treat those as recommendations, not automatic changes.

## The guardrail

No schedule becomes student-facing until the instructor checks dates, workload, sequencing, and LMS fit.

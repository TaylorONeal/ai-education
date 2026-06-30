---
name: canvas-lms
description: Operate Canvas LMS reliably from an AI agent or script: authenticate, push styled pages and assignment HTML, enter grades without losing them, and edit quizzes and question banks. Use when a task involves the Canvas API, SpeedGrader, the Rich Content Editor, or quiz and question-bank changes. The full reference is guides/canvas-lms.md.
---

# Canvas LMS Operations

## The problem

The other skills in this toolkit are platform-neutral. Canvas is where many of them actually have to land, and Canvas has sharp edges that cost real time: the Rich Content Editor strips your styling, the API authenticates two different ways depending on how you are calling it, large page bodies get truncated, and SpeedGrader will silently fail to save a grade if you commit it the wrong way. This skill is the operational layer that handles those edges. The full detail lives in `../../guides/canvas-lms.md`; this is the working summary.

## What you need

- Your Canvas host, the course ID, and the assignment, quiz, or page IDs you are touching.
- One of two ways to authenticate: a personal access token (Account, Settings, New Access Token) for scripts, or, when driving Canvas from a browser session you are already logged into, the in-browser CSRF token read from the `_csrf_token` cookie and sent as `X-CSRF-Token` with `credentials: 'same-origin'`.
- For grade entry, permission to manage grades in the course.

## The operations

- Push styled content. Send full HTML to an assignment description (`PUT /api/v1/courses/[COURSE_ID]/assignments/[ASSIGNMENT_ID]`, field `assignment[description]`) or a page (`PUT .../pages/[PAGE_URL]`, field `wiki_page[body]`). The HTML must be a single container with every style inline, and in stubborn configurations each declaration forced element by element, because the editor strips class and external CSS. If a large body truncates mid-transfer, split it, stash the halves in `sessionStorage`, and concatenate before sending. Confirm 200 and re-render.
- Enter grades, three ways: a gradebook CSV import for bulk, an API batch post (`POST .../assignments/[ASSIGNMENT_ID]/submissions/update_grades` with `grade_data[[USER_ID]][posted_grade]=`), or SpeedGrader by hand. If you use SpeedGrader, the score does not save unless you commit it with a real keyboard Enter; a JavaScript key event does not trigger the save. Triple-click the field, type the score, press Enter with a real key action, and confirm the graded counter incremented. A no-submission student gets a 0 the same way. The grade input's reference changes per student, so re-find it each time.
- Edit quizzes and question banks. The groups endpoint returns `{ quiz_groups: [...] }`. The group's `question_points` is what counts, not a bank preview. Bank-linked quizzes return an empty inline-questions array by design. Never put answers in `neutral_comments` (every student sees it). Navigate to the edit page first so the CSRF `authenticity_token` input is present, and edit question HTML through the editor's content API, not the raw textarea.

## What to check

- After any push, navigate to the page or assignment and confirm it rendered, not just that the call returned 200.
- After any grade entry, confirm it actually saved: the SpeedGrader counter increments and a checkmark appears, or the gradebook shows the value. Keep the column hidden or muted until you have reviewed the distribution.
- Before any quiz write, confirm you are on the edit page (the show page has no CSRF token) and that you are operating on the right course and quiz IDs.

## The guardrail

This skill moves grades and student-facing content, so the human gate is not optional. Grades stay hidden until you have read the distribution and said to post. Pages and announcements are previewed before students see them. The agent does the mechanical work; you approve what reaches a student. See PRINCIPLES.md.

## Automated version

As a connected skill, this runs the API calls and the SpeedGrader workflow directly, batching where it can (CSV import or `update_grades` over a whole stack rather than one student at a time), and pausing for your confirmation before anything is posted or unhidden. Full endpoint detail, the chunking technique, and the quiz-bank traps are in `../../guides/canvas-lms.md`. The same operations for other platforms are in `../../guides/other-lms.md`.

## Automate even better

Use the browser surface to reach what the API does not expose: archived courses and prior terms. Drive the logged-in browser to walk old course shells and pull historical exams, pages, and gradebooks into CSVs, which is the foundation for every cross-year analysis the other skills can then run. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

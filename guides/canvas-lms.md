# Canvas LMS Guide

The platform-specific companion to the skills. The skills are written to be LMS-agnostic so you can use them immediately. This guide holds the Canvas details so you do not have to rediscover them: how to authenticate, how to get styled content in, how to get grades in (including the bug that silently loses grades), and the quiz and question-bank traps that have cost real hours.

Everything here uses placeholders: `[COURSE_ID]`, `[ASSIGNMENT_ID]`, `[QUIZ_ID]`, `[BANK_ID]`, `[USER_ID]`, `[CANVAS_HOST]` (your institution's Canvas domain). Endpoints are stable but Canvas ships changes; confirm against the official docs at https://developerdocs.instructure.com when something behaves differently.

## 1. Authentication: two paths

### Path A: a personal access token (for scripts run outside the browser)

Generate one at Account, then Settings, then Approved Integrations, then New Access Token. Send it on every call:

```
Authorization: Bearer <ACCESS_TOKEN>
```

Tokens obtained through the OAuth refresh flow expire in about an hour and are refreshed automatically; manually generated tokens last until the expiry you set. Use this path for server-side or scheduled jobs. Treat the token like a password: it is not committed to the repo, not pasted into a consumer chatbot, and not shared.

### Path B: the in-browser session and CSRF token (for driving Canvas from an authenticated tab)

When you are operating Canvas through a browser you are already logged into (for example, a Cowork or Chrome session), you do not need a personal token. Canvas accepts same-origin calls authenticated by the session cookie, protected by a CSRF token.

```javascript
// Run inside the Canvas tab. The token lives in a cookie:
const raw = document.cookie.split(';').find(c => c.trim().startsWith('_csrf_token='));
const csrfToken = decodeURIComponent(raw.split('=')[1]);

await fetch('/api/v1/courses/[COURSE_ID]/assignments/[ASSIGNMENT_ID]', {
  method: 'PUT',
  credentials: 'same-origin',           // not 'include'; same-origin is correct from the Canvas tab
  headers: { 'Content-Type': 'application/json', 'X-CSRF-Token': csrfToken },
  body: JSON.stringify({ assignment: { description: HTML_CONTENT } })
});
```

Two things that will waste your time if you miss them:

- Do not navigate away from the Canvas domain between reading the token and making the call. Navigation invalidates it.
- On quiz and question-bank edit pages, the token is also present as a hidden form input named `authenticity_token`. The quiz show page has none of these inputs; the edit page has many. Navigate to the edit page before any write operation.

## 2. Getting styled content in (the !important rule)

Canvas's Rich Content Editor strips class-based and external CSS on paste and can override loose inline styles with its own stylesheet. To make a page render the way you built it:

- Output one outer container, with every style inline on each element.
- In stubborn configurations, force each declaration (element-by-element `!important` on every property). It is verbose, but it is the only thing that reliably survives the editor.
- No script tags (stripped). Style buttons as links, not button elements. No fixed or sticky positioning, no viewport units. No line-break tags for spacing; use margin and padding. Pair new-tab links with `rel="noopener"`. Set list styles explicitly.

The canvas-page-generator skill produces HTML that already follows all of this. This section is why it has to.

### Pushing a page or assignment body, including large ones

Assignment descriptions and page bodies accept full HTML through the API:

```javascript
// Assignment description:
PUT /api/v1/courses/[COURSE_ID]/assignments/[ASSIGNMENT_ID]   body: { assignment: { description: HTML } }
// Content page:
PUT /api/v1/courses/[COURSE_ID]/pages/[PAGE_URL]              body: { wiki_page: { body: HTML } }
```

Large bodies (tens of kilobytes) can be truncated by content filtering mid-transfer. If that happens, split the HTML into halves, stash each half in `sessionStorage`, concatenate them just before the call, and send once. Verify the call returned 200, then navigate to the page and confirm it rendered.

## 3. Getting grades in (three ways, including the save bug)

### Way A: gradebook CSV import (simplest, bulk)

Export the gradebook to get the exact header, then write a CSV in this shape:

```
Student,ID,SIS User ID,SIS Login ID,Section,<Assignment Name> (<ASSIGNMENT_ID>)
    Points Possible,,,,,100
"<Last, First>",<canvas_id>,<sis_login>,<sis_login>,<Section Name>,<score>
```

The second row begins with four leading spaces before "Points Possible". Import through Gradebook, then Actions, then Import. Keep the column hidden or muted until you have read the distribution and decided to post.

### Way B: API batch grade submission

```
POST /api/v1/courses/[COURSE_ID]/assignments/[ASSIGNMENT_ID]/submissions/update_grades
Authorization: Bearer <ACCESS_TOKEN>
form body: grade_data[[USER_ID]][posted_grade]=88 & grade_data[<another_user>][posted_grade]=91
```

It returns a Progress object you can poll. You need permission to manage grades in the course or section. This is the right tool for posting a whole stack at once after you have reviewed it.

### Way C: SpeedGrader by hand, and the bug that silently drops grades

If you are entering grades one student at a time through SpeedGrader (often the case when driving the browser with Cowork or computer use), there is one failure that will cost you a whole pass without an error message:

A score entered into the grade field does not save unless it is committed with a real keyboard Enter. A JavaScript-dispatched key event does not trigger Canvas's save handler. Setting the field value programmatically and clicking to the next student looks like it worked, but the grade was never written.

The reliable pattern:

1. Triple-click the grade input to select whatever is in it.
2. Type the score.
3. Press Enter using a real keyboard action (the computer-use key press), not a synthetic JavaScript event.
4. Confirm it saved: the graded counter in the header increments and a checkmark appears next to the student. If neither happens, it did not save; re-enter and press Enter again.

Two more notes: the grade input's element reference is reassigned every time SpeedGrader loads a new student, so a reference captured on one student is invalid on the next. Re-find it (or click its consistent on-screen location) each time. And a student with no submission gets a 0 entered the same way, not left blank.

## 4. Quiz and question-bank traps

These come from real debugging. They will save you an afternoon each.

- The quiz groups endpoint returns an object, not an array: `GET /api/v1/courses/[COURSE_ID]/quizzes/[QUIZ_ID]/groups` gives `{ quiz_groups: [...] }`. Destructure it.
- The quiz group's `question_points` is what students actually see and what counts, not the points shown on a question-bank preview page. Verify scoring against the group, not the bank UI.
- For a quiz whose questions all come from assessment question banks, `GET .../quizzes/[QUIZ_ID]/questions` returns an empty array by design (bank questions are not inline). To read that content, inspect the bank in the editor, not the API.
- `neutral_comments` on a question is shown to every student immediately after they submit, regardless of their answer. Never put a grading rubric or model answer there; it exposes answers and breaks retakes. Use `correct_comments` or `incorrect_comments`.
- Editing question HTML: use the editor's content API (its `getContent` / `setContent`), not the raw textarea value. Question HTML can contain image URLs carrying session tokens, and reading the raw value can trip content-safety filters. Target the editor by matching its content, not by index, because indices shift as you open more questions.
- The Canvas single-page app frequently redirects mid-task, clearing in-page state. Open a fresh tab for bank navigation, persist results in `sessionStorage` rather than page variables, and wait several seconds after a navigation before firing API calls.
- A duplicated quiz loses its question-bank links (the group keeps its name and point values but its `assessment_question_bank_id` becomes null, and a PUT to set it is silently ignored). To relink, delete the empty group and recreate it with `assessment_question_bank_id` set in the POST body.

## 5. Posting policy and records

Keep grade columns hidden or muted until you have reviewed the distribution. When AI assisted a grade, keep what it produced and what you changed. See PRINCIPLES.md; the platform mechanics do not change the ethics.

## Generalizing to other systems

Every operation here (authenticate, push styled content, import or post grades, read submissions) has an equivalent in Blackboard, Moodle, Brightspace, Schoology, and Google Classroom. Those are in `other-lms.md`.

## Sources

- Canvas Submissions API (update_grades): https://developerdocs.instructure.com/services/canvas/resources/submissions
- Canvas OAuth2 and access tokens: https://www.canvas.instructure.com/doc/api/file.oauth.html

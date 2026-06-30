# Other LMS Guide: Blackboard, Moodle, Brightspace, Schoology, Google Classroom

The companion to `canvas-lms.md`. Same operations, different platforms: how to authenticate, how to read submissions and activity, how to push grades, and how to push styled content. The skills do not change; only the connector does. Endpoints are reasonably stable but every platform ships updates, so confirm against the linked official docs, and confirm what your institution has enabled, because admins gate API access on all of these.

The styling rule from `canvas-lms.md` (one container, every style inline, force declarations in stubborn editors) applies to every system here. Any rich-content editor with a source or HTML view will render the canvas-page-generator output; paste it into that view.

## Blackboard Learn

- Authenticate: OAuth 2.0. Register your application in the Blackboard Developer Portal to get a key and secret, then exchange them for a bearer token. Your institution must approve the application against their instance.
- Read grades and submissions: `GET /learn/api/public/v2/courses/{courseId}/gradebook/columns` lists gradebook columns; column and attempt endpoints give per-student grades and submission content. Created and modified timestamps are exposed, which is useful for the behavioral signals in ai-output-checker.
- Push grades: write to the gradebook column's user grades through the gradebook API. For SIS-style bulk flows, Grades Journey v2 uses the same OAuth2 process.
- Push content: course contents API accepts HTML bodies.
- Docs: https://blackboard.github.io/rest-apis/learn/getting-started/framework and https://docs.anthology.com/docs/blackboard/rest-apis/hands-on/pulling-gradebook-data-and-assessment-grades

## Moodle

- Authenticate: a web-services token. An admin creates one under Site Administration, Plugins, Web Services, Manage tokens; or you can fetch one for a user via `login/token.php` with username and password. The function you call must be enabled on the web-service the token is attached to.
- Call format: everything goes through one endpoint with the token, function name, and JSON format as parameters: `https://[MOODLE_HOST]/webservice/rest/server.php?wstoken=[TOKEN]&wsfunction=[FUNCTION]&moodlewsrestformat=json&...`
- Read grades and submissions: `core_grades_get_grades` and the `mod_assign` functions (for example, fetching submissions for an assignment).
- Push grades: `core_grades_update_grades` (parameters include `courseid`, `component` such as `mod_assign`, `activityid`, `itemnumber`, and the grade payload). It returns a status code: 0 ok, 1 fail, 2 multiple updated, 4 locked.
- Push content: page and label module functions accept HTML.
- Docs: https://moodledev.io/docs/apis and https://docs.moodle.org/dev/Web_service_API_functions

## Brightspace (D2L), via the Valence API

- Authenticate: OAuth 2.0. Register the application; each call is made in the context of a logged-in user. Legacy ID-Key auth was deprecated in early 2023, so use OAuth2.
- Read: enrollments at `/d2l/api/lp/(version)/enrollments/`; grades through the grades resource (grade objects, categories, and values per user).
- Push grades: write grade values through the grades endpoints for the org unit and grade object.
- Rate limit: roughly 1000 calls per hour. Throttle client-side or run asynchronously under the limit; do not fire a whole roster in a tight loop.
- Docs: https://docs.valence.desire2learn.com/ and the grades resource at https://docs.valence.desire2learn.com/res/grade.html

## Schoology

- Authenticate: REST API with OAuth. Generate API credentials (key and secret) in the developer or admin settings, subject to your institution enabling API access.
- Read and push grades: section grade endpoints expose and accept per-student grades; submissions are available through the assignment and submission endpoints.
- Confirm the current endpoint paths and OAuth flow against the official developer documentation before building, because Schoology's API surface and access policy vary by institution and plan.
- Docs: the Schoology (PowerSchool) developer documentation for your instance.

## Google Classroom

- Authenticate: OAuth 2.0 with the right scope. Grading student work needs `https://www.googleapis.com/auth/classroom.coursework.students`. The teacher authorizes the app.
- Read submissions: `GET .../courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions` returns submissions, including attachments and timestamps.
- Push grades: `PATCH https://classroom.googleapis.com/v1/courses/{courseId}/courseWork/{courseWorkId}/studentSubmissions/{id}` with `updateMask=assignedGrade` (and `draftGrade` if you want to stage before returning). This is the "keep it hidden until reviewed" path: set the draft grade, review, then return.
- Push content: create announcements and coursework through their respective endpoints; descriptions accept text.
- Docs: https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork.studentSubmissions/patch and scopes at https://developers.google.com/workspace/classroom/guides/auth

## The pattern that holds everywhere

Whatever the platform: authenticate with a token or OAuth bearer, read submissions and grades through a per-course or per-assignment endpoint, push grades either one student at a time or in bulk, and keep the grade hidden or in draft until you have reviewed the distribution. The skills supply the judgment; this guide supplies the plumbing so you are not rebuilding it from scratch.

## Sources

- Blackboard Learn REST framework: https://blackboard.github.io/rest-apis/learn/getting-started/framework
- Anthology gradebook data guide: https://docs.anthology.com/docs/blackboard/rest-apis/hands-on/pulling-gradebook-data-and-assessment-grades
- Moodle web services API: https://moodledev.io/docs/apis
- Moodle web service functions: https://docs.moodle.org/dev/Web_service_API_functions
- Brightspace Valence API: https://docs.valence.desire2learn.com/
- Brightspace grades resource: https://docs.valence.desire2learn.com/res/grade.html
- Google Classroom studentSubmissions.patch: https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork.studentSubmissions/patch
- Google Classroom scopes: https://developers.google.com/workspace/classroom/guides/auth

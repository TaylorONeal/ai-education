# Connected and scheduled teaching workflows

Use automation when gathering or formatting evidence is the time sink. Start with one task, one named course, and one reviewable draft. The [agent guide](agents.md) defines access, evidence, checkpoints, and approval for all surfaces.

## Retrieve, normalize, preserve, analyze

1. Retrieve all records within the approved scope, following pagination and noting gaps. Prior terms are optional and require access; a browser cannot guarantee archived-course access.
2. Normalize dates, units, identifiers, score statuses, and exam variants. Keep source references and original values so each transformation can be checked.
3. Store in an approved private location. Use CSV for tables or indexed Markdown for course notes. Keep student records outside the course brain and public repository.
4. Analyze against the selected skill. Verify a sample against sources and report coverage. Missing data and extraction failures must remain visible.

## Examples

| Task | Useful output | Key check |
|---|---|---|
| Compare past exams | Question, term, objective, points, source, and answer-key access level | Do not conflate variants or expose restricted keys |
| Draft grading | Pseudonymous ID, criterion, evidence, proposed points, review status | Published rubric and instructor review of every score |
| Review readiness | Objective evidence and proposed support | Missing data is not zero; forecasts need held-out validation |
| Participation | Deduplicated, course-related activity in a defined window | Verified identity and attendance; no unrelated DMs |
| Course brain | Source-indexed notes with term and retrieval date | Preserve edits and flag conflicting policies |

## Recurring work

Only configure a schedule when requested and when an actual scheduler is available. Save scope, frequency, destination, retention approach, and notification conditions. Reconcile checkpoints before each run. Stay quiet when nothing meaningful changes. Do not let the scheduler send student messages, release grades, or publish unreviewed material.

## Limits and recovery

Connectors and browser tools have different permissions and coverage. Respect service limits; browser access is not a rate-limit bypass. If extraction fails, save completed work, record the gap, and offer the smallest useful export path. After an uncertain write, read the destination before retrying.

For platform mechanics, use [Canvas](canvas-lms.md), [other LMSs](other-lms.md), or [chat and discussion](chat-and-discussion.md), checking current official documentation and the observed interface before acting.

# Participation Scoring, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This document is the why and the how-it-actually-goes: the scoring model, the math, the failure modes, and how to run it across any learning management system without it eating your whole weekend.

## Why participation is the unfair grade

Most participation grades are a memory of who felt present. Memory favors the loud. It forgets the student who never speaks in the room but sends three sharp questions a week in private. It cannot be shown to a student who challenges it, which means it cannot be defended, which means it should make you uncomfortable. The fix is not more memory. It is a record: every student's real activity, pulled from where it actually happens, scored on rules you wrote down before you looked.

## The multi-source model

Real participation shows up in more than one place, so score more than one place. A model that works in practice spreads the weight across five sources. The exact split is yours; this is a shape that has held up:

- Public channel activity is the largest slice. This is the visible engagement: posts, questions, answering classmates.
- Private questions to you or a teaching assistant are a real but smaller slice. This is where your quiet students live, and the reason a chat-only scan grades them unfairly.
- Teaching assistant interactions (their one-on-ones plus their DM threads) are a slice you can take as a simple count from the TA, no scan required.
- One-on-one meetings with you are a slice pulled from your calendar.
- A quality or depth bonus is a small slice scored by judgment, so a thoughtful contributor is not tied with someone who posted the same volume of one-word replies.

The point of spreading the weight is fairness in both directions: a student cannot win on volume alone, and a student cannot lose just because their contribution was invisible to a quick scan.

## Why buckets, not raw counts

If you score raw post counts linearly, one hyperactive student runs away with the grade and everyone else compresses into noise. Convert raw counts into a small set of bands instead. An example shape, which you should re-fit to your own class each term:

| Raw posts in the window | Band (out of 10) |
|---|---|
| 0 | 0 |
| 1 to 2 | 1 |
| 3 to 4 | 2 |
| 5 to 6 | 3 |
| 7 to 9 | 4 |
| 10 to 14 | 5 |
| 15 to 19 | 6 |
| 20 to 24 | 7 |
| 25 to 29 | 8 |
| 30 to 39 | 9 |
| 40+ | 10 |

Set the thresholds against your actual class distribution, not a guess. If the whole class is quieter this term (the end of a semester, a heavy-workload stretch), lower the thresholds so the bands still discriminate. A bucket table that maps the whole class into two bands is not measuring anything.

## The curve and the floor

Two rules keep the scoring humane and defensible:

- A floor flag is a prompt to check in, not an automatic zero. A student who lands near the bottom gets surfaced for your personal review. Often that review finds private activity the scan missed.
- A true zero stays zero only after you confirm there is genuinely no evidence in any source. If you curve, curve consistently across both halves of the term so the two scores are comparable, and write down the rule you used.

## The failure mode that will bite you: name matching

This is where automated participation scoring quietly goes wrong. Chat display names rarely match your roster. A student goes by a nickname. Someone tags their name with a project or company in parentheses. Someone's handle looks like a stranger's. If the match is wrong, a real contributor reads as a zero and you will not notice until they email you.

Defenses:

- Keep a running correction map of display-name-to-roster-name as you discover mismatches, and reuse it next run so the fix compounds instead of repeating.
- When a name has a parenthetical tag, match against the name before the parenthesis, and strip the parenthetical before any comparison.
- Skip non-students in the channels: teaching assistants, automated join notifications, group threads.

## The other rule: inbound only

A message you sent to a student who never replied is not their participation. Require at least one inbound message per topic. Count each distinct topic once, even if it spans several messages, so a single back-and-forth does not inflate into ten.

## Running it without losing a weekend

- Run it in halves of the term, not once at the end. Smaller windows are faster to verify and let you catch a disengaging student while you can still reach them.
- Expect the chat pull to be the slow part. API connectors for chat tools tend to rate-limit hard (often roughly one call every ten to fifteen seconds, with parallel calls rejected), so a full roster across multiple channels can be a sequential job measured in tens of minutes, not seconds. Plan for it: cache user-id lookups once and reuse them, split the run across sessions, or fall back to a browser-driven scan for the direct-message history, which avoids the per-call limit at the cost of more babysitting.
- Write a progress file as you go, listing completed students, so a long run can be paused and resumed without losing or double-counting work.

## Across learning management systems

The model is LMS-agnostic. The sources differ by stack, and you should expect more than one:

- LMS discussion forums: Canvas, Blackboard, Moodle, Brightspace, Schoology all expose per-user post history.
- Chat tools: Slack and Discord are the most common for a class, followed by Microsoft Teams, a university-built discussion tool, and Google Classroom's stream. WhatsApp and Telegram show up occasionally; they are workable but the least standard for graded participation.
- Meetings: any calendar you can read. Filter by event title keywords (one-on-one, sync, office hours) and by a single-student attendee plus a meeting link.
- TA interactions: a simple CSV the TA fills in.

You do not have to rebuild the connection details for each of these. The ready-made specifics, how to authenticate, how to pull per-student activity, the rate limits and gotchas, and which platforms are most viable, are in `../../guides/chat-and-discussion.md`. The scoring rules, buckets, floor, and gates do not change. Only the connector does.

## The connected version, in detail

With AI wired to your chat tool, calendar, and a place to store output, the loop is: resolve each student's username (using your saved correction map), pull their posts and DM threads across every channel, read the calendar for one-on-ones, fold in the TA CSV, score against your buckets, and produce two artifacts. One is a human-readable table with a per-student pattern note. The other is a paste-ready gradebook block. It flags zeros, outliers, and private-only contributors, then stops and waits for your explicit yes before anything is written. It keeps a progress file so the run is resumable.

## Privacy and records

This is the most data-sensitive skill in the toolkit, so it is the one where PRINCIPLES.md matters most. Minimize what you feed the model: you do not need a student's full record to score participation, just the activity in the window. Prefer identifiers or initials over full names in prompts pasted into consumer tools. Tell students in your syllabus that participation is scored from logged activity. Keep the activity pull and the AI summary next to the grades you set, so any challenge has a paper trail. The AI counts. You grade.

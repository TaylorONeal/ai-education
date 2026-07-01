---
name: participation-scoring
description: Score student class participation fairly by pulling each student's real activity across chat channels, direct messages, and meetings, then applying rules you set. Use when you need to grade participation for a class and want an auditable record instead of a gut feeling.
---

# Participation Scoring

## The problem

Most participation grades are a memory of who felt present, and memory favors the loud. The student in the front row is easy to remember. The one who never speaks in the room but sends three sharp questions a week in private is easy to forget. A grade you cannot show a student who challenges it is a grade you cannot defend.

This skill pulls every student's real activity and lays it out where you can see it, scored on rules you wrote down before you looked, with a summary you read by hand before anything becomes a grade.

## What you need

- A class roster (names, and the username each student uses in your chat tool).
- Access to wherever participation actually happens. This is rarely one place: an LMS discussion forum (Canvas, Blackboard, Moodle, Brightspace, Schoology), a class chat (Slack or Discord are the most common, also Microsoft Teams, a university-built discussion tool, Google Classroom, and sometimes WhatsApp or Telegram), direct messages, and any meeting or office-hours log. Score every place that counts for your class. For how to pull per-student activity from each of these, see `../../guides/chat-and-discussion.md`.
- A calendar you can read for one-on-one meetings, if those count.
- Your participation rubric: what counts, and how much.

## The rules you set first

Decide these before you run anything. Real participation shows up across more than one channel, so score more than one, and spread the weight so a student cannot win on volume alone or lose just because their contribution was invisible to a quick scan. A shape that has held up in a live course:

- Public channel posts and questions: the largest single component. This is the bulk of visible engagement.
- Substantive private questions to you or a teaching assistant: a meaningful but smaller component. Quiet students live here.
- Teaching assistant interactions (their one-on-ones plus their DM threads): a component you can take as a simple count from the TA, no scan required.
- One-on-one meetings or office-hours visits with you: a component pulled from your calendar.
- A quality or depth bonus: a small component for substance, scored by judgment, so a real question about interpretation beats ten one-word replies.

Two design rules that matter:

- Use buckets, not raw counts. A linear count lets one hyperactive student run away with the grade while everyone else compresses into noise. Convert each raw count into a small band instead. A shape to start from, which you should re-fit to your own class's actual distribution each term rather than reuse as a guess:

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

  If the whole class is quieter this term (end of semester, a heavy-workload stretch), lower the thresholds so the bands still discriminate. A bucket table that maps the whole class into two bands is not measuring anything.
- Set a floor, not an automatic zero. A student who lands near the bottom gets flagged for your personal check-in, not a silent zero. A true zero stays zero only after you confirm there is genuinely no evidence in any source.

## The prompt

> You are helping me score class participation for [COURSE]. I will give you one student's activity at a time, pulled from [LIST YOUR SOURCES: public channel, DMs, TA log, calendar]. Do not invent or assume any activity I do not provide.
>
> Scoring rules:
> - Public channel posts and questions: [POINTS], scored in buckets: [YOUR BUCKETS, e.g. 0 posts = 0, 1 to 2 = 1, 3 to 4 = 2, ... 40+ = 10]
> - Substantive private questions to me or the TA: [POINTS]
> - TA interactions (one-on-ones plus DM threads): [POINTS]
> - One-on-one meeting or office hours with me: [POINTS]
> - Quality and depth bonus: [POINTS], your judgment on substance
> - Flag any student below [FLOOR] for my personal review rather than scoring them zero.
>
> For each student, return: the student identifier, the count in each category, the bucket each count falls into, the total, and a one-line note on the pattern (for example, "Quiet in public but seven substantive private threads" or "High volume, mostly low-effort one-word replies").
>
> Here is the first student's activity: [PASTE ACTIVITY]

Run it student by student, or paste a batch if your tool can pull them all. If you have AI connected to your chat tool, ask it to pull each student's posts and DM threads first, then score.

## What to check before you trust it

1. Spot-check five students by hand. Pull their real activity yourself and compare. If two or more are off, the whole batch is suspect.
2. Read every flagged student. The floor flag exists so you investigate, not so you rubber-stamp a zero. The quiet-in-public, active-in-private student lives here.
3. Watch the name matching. This is where automated scoring quietly goes wrong: chat display names rarely match your roster. A student goes by a nickname, tags their name with a project or company in parentheses, or uses a handle that looks like a stranger's. Match a parenthetical-tagged name against the part before the parenthesis, skip non-students in the channel (TAs, join-notification bots, group threads), and keep a running correction map of display-name-to-roster-name as you find mismatches so the fix compounds instead of repeating next run. If the match is wrong, a real contributor reads as a zero and you will not notice until they email you.
4. Count inbound only. A message you sent to a student who never replied is not their participation. Require at least one inbound message per topic, and count each distinct topic once even if it spans several messages, so a single back-and-forth does not inflate into ten.
5. Sanity-check the distribution. If everyone landed in a narrow band, your buckets are not discriminating. If one student is a wild outlier, confirm it is real before it counts.

## The guardrail

The AI counts. You grade. It never assigns a final participation score and it never zeroes a student on its own. Before anything is published, you see the full table and a short narrative of the distribution, and you give an explicit yes. Keep the activity pull and the AI summary alongside the final grades you set, so any challenge has a paper trail.

This is also the most data-sensitive skill in the toolkit, so give it the most care: minimize what you feed the model (you need the activity in the window, not a student's full record), prefer identifiers or initials over full names in prompts pasted into consumer tools, and tell students in your syllabus that participation is scored from logged activity. See PRINCIPLES.md.

## Automated version

With AI connected to your chat tool, calendar, and a place to store output:

1. It resolves each student's username using your saved correction map, then queries their activity by username across every channel, pulls DM threads, and reads your calendar for one-on-ones.
2. It scores against your rules and buckets, then produces two things: a human-readable table you review, and a paste-ready block for your gradebook.
3. It flags zeros, outliers, and private-only contributors for your attention, then stops and waits for your yes before writing anything to the gradebook.
4. It writes a progress file as it goes, so a long run can be paused and resumed without losing or double-counting work.

Expect the chat pull to be the slow part. API connectors for chat tools tend to rate-limit hard, often around one call every ten to fifteen seconds with parallel calls rejected, so a full roster across multiple channels can be a sequential job measured in tens of minutes, not seconds. Cache username lookups once and reuse them, split the run across sessions, or fall back to a browser-driven scan for direct-message history, which avoids the per-call limit at the cost of more babysitting.

Run it in halves of the term rather than all at once. Smaller windows are easier to verify and catch disengagement while you can still act on it. Use the same buckets and floor across both halves so the two scores stay comparable.

## Automate even better

Point an agentic browser or connector at every channel and the full direct-message archive for the window and have it assemble the complete activity history in one pass, unify it into a single CSV (student, source, count, sample), and score from clean data instead of babysitting a rate-limited scan. The same pass can pull prior terms so you can compare participation patterns year over year. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

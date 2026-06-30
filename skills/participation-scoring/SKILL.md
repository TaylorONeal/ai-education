---
name: participation-scoring
description: Score student class participation fairly by pulling each student's real activity across chat channels, direct messages, and meetings, then applying rules you set. Use when you need to grade participation for a class and want an auditable record instead of a gut feeling.
---

# Participation Scoring

## The problem

For most of us, participation grades are a gut feeling about who seemed engaged. That is not fair, it is hard to defend when challenged, and it quietly punishes students who contribute in ways you do not happen to see. The loud student in the front row is easy to remember. The student who sends you three thoughtful questions in private is easy to forget.

This skill pulls every student's real activity and lays it out where you can actually see it, scored on rules you set, with a summary you read by hand before anything becomes a grade.

## What you need

- A class roster (names, and the username each student uses in your chat tool).
- Access to wherever participation actually happens. This is rarely one place. It might be an LMS discussion forum (Canvas, Blackboard, Moodle, Brightspace, Schoology), a class chat (Slack or Discord are the most common, also Microsoft Teams, a university-built discussion tool, Google Classroom, and sometimes WhatsApp or Telegram), direct messages, and any meeting or office-hours log. Score every place that counts for your class. For how to pull per-student activity from each of these, see `../../guides/chat-and-discussion.md`.
- A calendar you can read for one-on-one meetings, if those count.
- Your participation rubric: what counts, and how much.

## The rules you set first

Decide these before you run anything. Real participation shows up across more than one channel, so score more than one. Example weighting from a live course, adjust to yours:

- Public channel posts and questions: the largest single component (this is the bulk of visible engagement).
- Substantive private questions to you or a teaching assistant: a meaningful but smaller component (quiet students live here).
- Teaching assistant interactions (their one-on-ones plus their DM threads): a component you can hand off as a simple count.
- One-on-one meetings or office-hours visits with you: a component pulled from your calendar.
- A quality or depth bonus: a small component for substance, scored by judgment (a real question about interpretation beats ten one-word replies).

Two design rules that matter:

- Use buckets, not raw counts. Convert a raw post count into a small band (for example, 0 posts to 0 points, a few posts to a low band, a heavy poster to the top band) so one hyperactive student does not run away with the grade. Set your bucket thresholds against the actual class distribution, not a guess. If the whole class is quieter this term, lower the thresholds.
- Set a floor, not an automatic zero. A student who lands near the bottom gets flagged for your personal check-in, not a silent zero. A true zero stays zero only after you confirm there is genuinely no evidence in any source.

## The prompt

> You are helping me score class participation for [COURSE]. I will give you one student's activity at a time, pulled from [LIST YOUR SOURCES: public channel, DMs, TA log, calendar]. Do not invent or assume any activity I do not provide.
>
> Scoring rules:
> - Public channel posts and questions: [POINTS], scored in buckets: [YOUR BUCKETS, e.g. 0 posts = 0, 1 to 4 = low band, ... , heavy = top band]
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
3. Watch the name matching. Chat display names rarely match your roster exactly. Someone goes by a nickname, someone tags their name with a project or company in parentheses, someone uses a handle that looks like a stranger. Confirm the usernames map to the right students before you score, or a real contributor reads as a zero. Keep a running map of the mismatches you find so the next run inherits it.
4. Count inbound only. A message you sent to a student who never replied is not their participation. Require at least one inbound message per topic, and count each distinct topic once even if it spans several messages.
5. Sanity-check the distribution. If everyone landed in a narrow band, your buckets are not discriminating. If one student is a wild outlier, confirm it is real before it counts.

## The guardrail

The AI counts. You grade. It never assigns a final participation score and it never zeroes a student on its own. Before anything is published, you see the full table and a short narrative of the distribution, and you give an explicit yes. Keep the activity pull and the AI summary alongside the final grades you set, so any challenge has a paper trail.

## Automated version

With AI connected to your chat tool, calendar, and a place to store output:

1. It queries each student's activity by username across every channel, pulls DM threads, and reads your calendar for one-on-ones. It uses your stored name-correction map so nicknames and handles resolve to the right students.
2. It scores against your rules and buckets, then produces two things: a human-readable table you review, and a paste-ready block for your gradebook.
3. It flags zeros, outliers, and private-only contributors for your attention, then stops and waits for your yes before writing anything to the gradebook.
4. It writes a progress file as it goes, so a long run (a chat scan across a full roster can take a while) can be paused and resumed without losing or double-counting work.

Run it in halves of the term rather than all at once. Smaller windows are easier to verify and catch disengagement while you can still act on it. Use the same buckets and floor across both halves so the two scores stay comparable.

## Automate even better

Point an agentic browser or connector at every channel and the full direct-message archive for the window and have it assemble the complete activity history in one pass, unify it into a single CSV (student, source, count, sample), and score from clean data instead of babysitting a rate-limited scan. The same pass can pull prior terms so you can compare participation patterns year over year. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

---
name: announcement-writer
description: Draft class announcements in your own voice, trained on your past posts, with the AI tells stripped out so it sounds like you and not a robot. Use for weekly updates, exam details, schedule changes, welcome and goodbye posts, and extra-credit notices.
---

# Announcement Writer

## The problem

You post a lot of class updates, and they need to sound like you, not like a press release. Generic AI writing is easy to spot and students tune it out: the stiff cadence, the inflated words, the punctuation no human uses. But writing every announcement from scratch also eats twenty minutes a pop, several times a week. You want your voice without the time cost.

This skill drafts in your voice by learning from your real past posts, then runs a pass that scrubs the machine tells out before you ever see it.

## What you need

- Five to ten of your past announcements, so the model can learn how you actually write.
- The facts the new announcement has to carry: dates, point values, links, any required logistics.
- Your saved voice style guide, once you have built it (see Step 1). After the first time, this is the only setup you reuse.

## Step 1: Capture your voice (once)

Paste five to ten of your past announcements and ask:

> Read these announcements I wrote. Describe my voice as a short, reusable style guide. Cover: my typical greeting and sign-off; my sentence length and level of formality; any section-header style I use (for example, all-caps labels); the running jokes, recurring references, or shorthand that are clearly mine; whether and how often I use emojis; and how I tend to connect class work to something bigger (career, real work, why it matters). Write it so I can paste it back in for every future announcement.

Save the style guide it produces. The point is that it captures the specifics that make a post yours: the greeting you actually use, the joke you reuse every exam week, the way you always note the time zone, the way you tie an assignment to what it looks like in a real job. You reuse this guide for every future announcement.

## Step 2: Draft a new announcement

Announcements fall into a handful of categories, and each has a shape. Tell the model which one you are writing so it uses the right structure:

- Welcome: warm opening, what the course is and who it is for (not just majors), an honest note that it takes effort but is doable, the first-week logistics, where to find help, an intro video if you have one.
- Goodbye: celebrate the finish, reflect on growth from student work to real work, name what they are taking with them and where it shows up in interviews, then the admin and staying-in-touch details.
- Exam or midterm: the date and time with the time zone, what it covers and the format, how to take it, study guidance pointed at specific topics, and a note that calms nerves without pretending it is easy. A little humor here earns its place.
- Weekly update or assignment: connect the current work to why it matters, the specific things to focus on or common mistakes, what is coming up, and which channel to use for questions.
- Extra credit: a hook that makes it sound genuinely interesting, the connection to the course, the requirements and the due date. Keep it short.
- Topic or content week: why this topic matters now, framed for different roles or interests, the readings and videos, framed so it feels worth their time.
- Schedule or logistics update: short, a quick check-in, the next week or two laid out as a small table, and where to get help.
- TA introduction: credibility, availability windows, contact method, one piece of real advice, a personal touch.

After the first draft, have the model ask you for what it cannot know rather than guess it: dates and times, point values, links (assignment pages, Zoom, sign-up forms), the TA's name and hours, any tool keys students need, and any change from the syllabus. Never let it guess these; dates, point values, and links are exactly the things an AI gets plausibly wrong.

Then:

> Write a [CATEGORY] announcement for [COURSE].
>
> Match this voice exactly: [PASTE YOUR STYLE GUIDE]
>
> Here is what it needs to cover: [BULLET THE FACTS: dates, assignments, point values, links, anything required]
>
> Keep it [LENGTH]. Use my greeting and sign-off. Always include the time zone on any time. Connect it to why this matters for them, not just to the grade. Do not add hype or filler.

## Step 3: Strip the AI tells (always)

Run every draft through this before posting:

> Edit this so no trace of AI writing remains. Remove em dashes and replace with commas or periods. Cut inflated words (pivotal, crucial, leverage, foster, delve, robust, seamless). Break up any group-of-three patterns. Stop any synonym cycling where the same idea gets renamed each sentence. Remove empty hype. Keep my voice and all the facts. Return only the cleaned version.

What lands in front of you should already read like you wrote it.

The draft is plain text and works wherever you announce: your LMS announcements tool, email, or a class chat. Posting it automatically through a specific platform is covered in the guides: `../../guides/canvas-lms.md` for the Canvas announcement and page tools, `../../guides/chat-and-discussion.md` for Slack, Discord, Teams, and similar. The base workflow needs none of that; it is copy, clean, paste, post.

## What to check before you post

1. Read it out loud. If a sentence is not one you would say, change it. The voice guide gets you close, not perfect.
2. Verify every fact. Dates, point values, and links are exactly the things an AI will get plausibly wrong. Check them against your real syllabus and gradebook. Never paste a link the AI generated without confirming it.
3. Confirm nothing is invented. If it added a detail you did not give it (a date, a policy, a joke that is not yours), cut it.
4. Confirm the time zone is on every time. This is the single most common thing students get confused by, and the easiest to drop.

## The guardrail

You approve and you post. The AI drafts in your voice but never speaks to your students on its own. The voice is yours, the facts are yours, the send button is yours.

## Automated version

With AI connected to your chat or LMS, it can draft from your style guide and post on your approval, no copy-paste. Keep the approval step. An announcement that goes out without your read is exactly the kind of small error that erodes trust.

## Automate even better

Two moves. Pull your entire archive of past announcements in one pass to build the richest possible voice guide, not just the five you remembered. And post across all your channels at once on your approval, rather than copying into each by hand. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.

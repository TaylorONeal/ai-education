# Announcement Writer, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This is the longer version: how to capture a voice that actually sounds like you, the templates for each kind of announcement, and the pass that strips the machine tells before anything reaches a student.

## The problem

You post a lot of class updates, and they need to sound like you, not like a press release. Generic AI writing is easy to spot and students tune it out: the stiff cadence, the inflated words, the punctuation no human uses. But writing each one from scratch eats twenty minutes, several times a week. You want your voice without the time cost.

## Capturing your voice (the part that makes it work)

The skill drafts well only if the style guide is specific. Paste five to ten real past announcements and ask the model to describe, concretely:

- Your greeting and your sign-off, verbatim.
- Your sentence length and level of formality.
- Your section-header style (for example, all-caps labels).
- The running jokes, recurring references, and shorthand that are clearly yours.
- Whether and how often you use emojis.
- How you tie class work to something bigger: a career skill, what real work looks like, why a topic matters now.

Save that guide. It is the one piece of setup you reuse forever. The reason it works is that it captures the specifics a generic model never invents: the greeting you actually use, the joke you reuse every exam week, the way you always note the time zone, the way you connect an assignment to an interview. Those specifics are what make students read it as you.

## The category templates

Announcements come in a handful of shapes. Tell the model which one you are writing so it uses the right structure.

- Welcome: warm opening, what the course is and who it is for (not just majors), an honest note that it takes effort but is doable, first-week logistics, where to find help and the TA, an intro video if you have one.
- Goodbye: celebrate the finish, reflect on growth from student work to real work, name what they are taking with them and where it shows up in interviews, then admin and staying-in-touch details.
- Exam or test: the date and time with the time zone, what it covers and the format, how to take it, study guidance pointed at specific topics, and a note that calms nerves without pretending it is easy. A little humor here earns its place.
- Weekly update or assignment: connect the current work to why it matters, the specific things to focus on or the common mistakes, what is coming up, and which channel to use for what.
- Extra credit: a hook that makes it sound genuinely interesting, the connection to the course, the requirements and the due date. Keep it short.
- Topic or content week: why this topic matters now, framed for different roles, the readings and videos with enough context that they feel worth the time.
- Schedule or logistics update: short, a quick check-in, the next week or two laid out as a small table, and where to get help.
- TA introduction: credibility, availability windows, contact method, one piece of real advice, a personal touch.

## The detail-gathering step

After the first draft, the model should ask you for what it cannot know. By category that is usually: dates and times, point values, links (assignment pages, Zoom, sign-up forms), the TA's name and hours, any tool keys students need, and any change from the syllabus. Never let it guess these. Dates, point values, and links are exactly the things an AI gets plausibly wrong.

## Strip the AI tells (always run this)

Every draft goes through a cleanup pass before posting: remove em dashes and replace with commas or periods, cut inflated words (pivotal, crucial, leverage, foster, delve, robust, seamless), break up group-of-three patterns, stop synonym cycling where the same idea gets renamed each sentence, and remove empty hype, while keeping your voice and every fact. What lands in front of you should already read like you wrote it.

## Before you post

Read it out loud; if a sentence is not one you would say, change it. Verify every fact against your real syllabus and gradebook. Confirm nothing was invented (a date, a policy, a joke that is not yours). Confirm the time zone is on every time, because that is the single most common thing students get confused by.

## Where you post it

The draft is plain text and works wherever you announce: your LMS announcements tool, email, or a class chat. For posting through a specific platform automatically (LMS announcement API, or a chat tool), the connector specifics are in `../../guides/`: `canvas-lms.md` for the Canvas announcement and page tools, `chat-and-discussion.md` for Slack, Discord, Teams, and similar. The base workflow needs none of that; it is copy, clean, paste, post.

## The guardrail

You approve and you post. The AI drafts in your voice but never speaks to your students on its own. The voice is yours, the facts are yours, the send button is yours. Keep the approval step even in the connected version; an announcement that goes out unread is exactly the small error that erodes trust.

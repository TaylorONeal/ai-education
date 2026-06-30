# Chat and Discussion Guide

Where class participation actually happens, and how to pull per-student activity from each place. This is the companion the participation-scoring skill points to, and it also covers posting for the announcement-writer skill. The scoring model, buckets, floor, and review gate live in the skill; this is the plumbing.

A class rarely lives in one tool. Score every place that counts. Ranked roughly by how common and how workable they are for graded participation:

## Most common and most workable

### LMS discussion forums (Canvas, Blackboard, Moodle, Brightspace, Schoology)

The cleanest source, because the roster and the identities already match. Pull discussion topics and entries through the LMS API and tally per author. The auth and endpoints are in `canvas-lms.md` and `other-lms.md`. Because identity is already tied to the enrolled student, you skip the name-matching problem that bites you everywhere else.

### Slack

- Authenticate: a bot or user token with the right scopes, sent as an `Authorization: Bearer` header.
- Read activity: `conversations.history` returns a channel's or DM's messages (a DM conversation ID starts with `D`). To attribute participation, either pull each course channel's history and tally by author, or search messages by author.
- The rate limit is the catch, and it changed in 2025. New, non-Marketplace apps are throttled hard on `conversations.history`: about one request per minute, with the page size capped around 15 messages. Internal and Marketplace apps keep the older, faster tiers (dozens of requests a minute, up to 1000 messages a request). A 429 response carries a `Retry-After` header. Plan for sequential, slow pulls on a new app: resolve and cache each student's user ID once, reuse it, and run a large roster across more than one session.
- Practical fallback for direct-message history: a browser-driven scan of an open Slack tab avoids the per-call API limit entirely, at the cost of more hand-holding. For a full roster of DM histories this is often faster end to end than the rate-limited API.
- Docs: https://docs.slack.dev/reference/methods/conversations.history/ and https://docs.slack.dev/apis/web-api/rate-limits/

### Discord

- Authenticate: a bot token, sent as `Authorization: Bot <token>`.
- Read activity: `GET https://discord.com/api/v10/channels/{CHANNEL_ID}/messages?limit=100`, paginating with `before`, `after`, or `around`. Tally by author.
- Permissions and intents: the bot needs both "View Channel" and "Read Message History" on the channel, and you must enable the privileged "Message Content Intent" in the bot settings to read message text. That intent is gated by Discord and may require verification once the bot is in many servers.
- Docs: https://docs.discord.com/developers/reference

## Workable with more setup

### Microsoft Teams

Read channel messages through the Microsoft Graph API with OAuth2. Some message-read endpoints are protected and require admin consent or carry usage terms, so this usually needs your institution's Microsoft admin to enable it. Link: the Microsoft Graph documentation for channel and chat messages. Treat the admin-consent step as the real gate.

### Google Classroom stream

The Classroom API exposes announcements and coursework, and comments on them, rather than a free chat. If your participation happens as comments on stream posts, pull those; if it happens in a separate chat tool, score that instead. Auth and scopes are in `other-lms.md`.

## Least standard (bot-mediated, real privacy caveats)

### Telegram

A bot can read messages in a group only if it is a member, and only sees all group messages if its privacy mode is turned off (or it is an admin). You read updates through the Bot API (`getUpdates` or a webhook). Feasible for a class group, but everything is bot-mediated and students must knowingly be in a bot-monitored group.

### WhatsApp

Consumer WhatsApp has no read API. The only supported path is the WhatsApp Business (Cloud) API through Meta, with a business number and webhooks, which is heavy for a class and was not built for graded participation. If a class genuinely runs on WhatsApp, treat participation there as self-reported or manually logged rather than scraped, and weigh the privacy cost carefully.

## Cross-cutting gotchas (apply to every source)

- Name matching. Outside the LMS, display names rarely match your roster. Nicknames, handles, and parenthetical company or project tags all break a naive match, and a wrong match reads a real contributor as a zero. Keep a correction map and reuse it. Match against the name before any parenthesis.
- Inbound only. A message you sent to a student who never replied is not their participation. Require at least one inbound message per topic, and count each distinct topic once.
- Rate limits are the time sink, not the logic. Cache user-id lookups, run sequentially, and split big jobs across sessions. Use a browser scan where an API limit makes a full pull impractical.
- Skip non-students: teaching assistants, bots, automated join notices, group threads.

## Posting (for announcement-writer)

The same connectors post as well as read. Slack and Discord send messages through their respective send endpoints; Teams posts through Graph; LMS announcement tools post through the LMS API in `canvas-lms.md` and `other-lms.md`. Keep the approval step: the announcement-writer guardrail is that nothing posts without your read.

## Privacy

This is the most sensitive data in the toolkit. Pull the least you need to score the window, prefer identifiers over full names in anything you paste into a consumer tool, tell students in the syllabus that logged activity is scored, and do not retain private message content beyond what the grade needs. See PRINCIPLES.md.

## Sources

- Slack conversations.history: https://docs.slack.dev/reference/methods/conversations.history/
- Slack rate limits: https://docs.slack.dev/apis/web-api/rate-limits/
- Discord API reference: https://docs.discord.com/developers/reference

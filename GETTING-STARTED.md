# Getting Started

This page assumes nothing. If you have used a website and can copy and paste, you are ready. We will do one real task together, then show you what changes when you let the AI do more of the work.

If you hit a word you do not know, the [`GLOSSARY.md`](GLOSSARY.md) defines each one in a sentence.

## Before you start

You need one thing: access to any AI chat tool. That means ChatGPT, Claude, Google Gemini, Microsoft Copilot, or whatever your school provides. A free account is fine for the first task. You do not need to install anything or know how to code.

One habit to build now: read everything the AI gives you before you use it. The AI drafts. You decide. That is the rule the whole toolkit is built on.

## Task: draft a class announcement (about 10 minutes)

We picked this one because it is low-stakes and you will see a result fast.

1. Open your AI chat tool in a browser.
2. In this repo, open [`skills/announcement-writer/SKILL.md`](skills/announcement-writer/SKILL.md). Scroll to the section called "The prompt." The indented block under it is the prompt.
3. Copy the whole prompt block.
4. Paste it into your AI chat tool, but do not send yet.
5. Find the parts in brackets, like `[COURSE]` or `[WHAT YOU WANT TO SAY]`, and replace each one with your real detail. Delete the brackets too.
6. Send it.
7. Read what comes back. Does it sound like you? Is anything wrong or missing? Edit it directly, or tell the AI what to change ("make it warmer," "cut the second paragraph," "I would never say 'utilize'").
8. When it is right, copy it into your LMS or email and post it.

That is the entire pattern for every skill in here. Copy the prompt, fill in your details, read the result, use it. Nothing else to learn.

## Do a second one

Once the first worked, try one that saves more time. Good next picks:

- [`skills/quiz-builder/`](skills/quiz-builder/) to generate a question bank in your subject. Check the [domains folder](skills/quiz-builder/domains/) first; there may already be a pack for your field.
- [`skills/grading-assistant/`](skills/grading-assistant/) to apply your rubric to a stack of short answers and flag the ones worth a second look.

Same steps every time. Open the skill, copy the prompt, fill in your details, read before you use.

## What changes when the AI does more of the work

Here is the part worth understanding, using participation scoring as the example.

At level 1 (plain chat), you do this:

- You open Canvas, Slack, your calendar, and wherever else participation happens.
- You pull each student's posts and messages by hand.
- You paste one student at a time into the chat.
- You copy each score back into your gradebook.

The AI scores fairly and consistently, which is real value. But you still did all the gathering and all the clicking. For a class of 60, that is most of an evening.

At level 3 (an AI that can control your computer, like Claude Cowork), the same task looks like this:

- You tell the agent to score participation for the term using your rules.
- It opens your tools, reads the roster, pulls each student's activity across every channel, and matches nicknames to the right students.
- It scores everyone against your buckets and floor.
- It shows you a table and a short summary, flags the students who need your eyes, and waits.
- You read it, fix what needs fixing, and approve. It writes the grades only after your yes.

You went from doing the work to checking it. That is the whole point of climbing the ladder, and it is why this is more than a pile of prompts. The [README](README.md#the-three-levels-from-ai-that-gives-you-words-to-ai-that-does-the-work) explains the three levels, and [`guides/automation.md`](guides/automation.md) covers the setup.

## When you are ready to climb

You do not have to. Plenty of teachers stay at copy-paste forever and get real value. But when a task becomes routine and you want the time back:

- Level 2 (skills): if you use Claude, install these skill folders so you trigger them by name instead of pasting. See [`AGENTS.md`](AGENTS.md).
- Level 3 (computer control): use Claude Cowork or another computer-use agent to do the gathering and clicking. See [`guides/automation.md`](guides/automation.md) and the platform [guides](guides/).

## If something goes wrong

- The AI made up a number or a source. Good catch, that is exactly why you read first. The [`ai-output-checker`](skills/ai-output-checker/) skill is built to catch this in student work, and the same caution applies to its own output.
- The result is generic or bland. Give it more of your real detail, or tell it what to cut. Vague in, vague out.
- You are unsure whether this is allowed or safe with student data. Read [`PRINCIPLES.md`](PRINCIPLES.md) and [`FAQ.md`](FAQ.md) before going further.

Stuck on something this page did not cover? Open an issue on the repo and ask. Other teachers will hit the same thing.

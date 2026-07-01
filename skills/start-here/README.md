# Start Here, in depth

This is the onboarding skill: the front door for a teacher who just met this toolkit. The SKILL.md has the prompt and the routing table. This explains why it works the way it does, so an agent running it makes good calls.

## The job

A new teacher faces three frictions at once: they do not know what the toolkit is, they do not know which of a dozen skills to use, and they do not want to hand over their materials. Most onboarding fails by attacking all three with a wall of setup. This skill attacks them in order and stops at the first real win.

The principle: one ingest, one skill, one result. A teacher who finishes the first session with a graded sample or a drafted announcement will come back and set up the rest. A teacher buried in configuration will not.

## Why ingestion comes second, not first

It is tempting to make a teacher build the full prof-brain knowledge base before anything else. Resist it. Ingestion is an optimization that makes later sessions faster; it is not a prerequisite for value. Ask for the smallest useful input (a syllabus and one assignment), show value on it, and offer to ingest more once they have seen the payoff. If their LMS is connected, ingestion is nearly free because the agent pulls the materials itself, so offer the full ingest then. If they are copy-paste only, skip prof-brain entirely for the first session.

## Why it asks one question at a time

Non-technical teachers bounce off a form. A single question, answered, then the next, feels like a conversation with a helpful colleague, not a setup wizard. The prompt enforces this explicitly because models default to dumping all their questions at once.

## Why it routes to exactly one skill

Showing a new teacher all eleven skills is how you lose them. The routing table in SKILL.md maps a stated pain point to one starting skill. Name that one, run it on a real example, and leave the rest for later. The toolkit is broad on purpose, but breadth is the enemy of a first session.

## How an agent should run this

If you are an agent and the repo is in your context, you do not need to paste the prompt; follow its steps directly. Read `../../AGENTS.md` first for the skill index and conventions, then run the orient, ask, ingest, route, and run-one-example flow. Hand off to the chosen skill and make sure the teacher reads that skill's "what to check" section before trusting its output.

## What success looks like

The session ends with: the teacher knows the one rule, their biggest time-sink named, one skill run on one real example of theirs, and a clear single next step. Not a configured system. A first win and a reason to return.

## The guardrail

This skill sets up and routes; it never touches student data or a gradebook. Every real task runs through a skill with its own human-in-the-loop guardrail. Keep onboarding honest: it hands the teaching back to the teacher, it does not quietly start doing it for them.

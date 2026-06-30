# Glossary

Plain definitions for the words used in this toolkit. One sentence each, no jargon.

**AI chat tool**: A website or app where you type to an AI and it types back, like ChatGPT, Claude, Google Gemini, or Microsoft Copilot.

**Prompt**: The block of text you paste into an AI tool to tell it what you want; the skills give you ready-made ones.

**Skill**: A folder in this repo that holds a tested prompt plus the method and the mistakes to avoid for one teaching task, so you do not have to figure it out yourself.

**SKILL.md**: The file inside each skill folder that contains the prompt and a short how-to; this is the one you copy from.

**README (inside a skill)**: The deeper file next to a SKILL.md that explains the full method, examples, and edge cases when you want more than the prompt.

**Agent**: An AI that can take actions for you, not just chat; for example, open a webpage, read a file, or fill in a grade, instead of only giving you words.

**Claude Cowork**: A desktop app where Claude can see your files and control your computer and browser, which lets it run these skills and do the gathering and clicking for you.

**Computer-control agent**: Any AI that can operate your computer or browser on your behalf (Claude Cowork, an AI browser extension, or an agentic browser); this is what powers the highest level of the toolkit.

**Connector (also called MCP)**: A one-time setup that links an AI to one of your tools (your LMS, chat app, or calendar) so it can pull and push information directly instead of you copying it by hand.

**LMS (Learning Management System)**: The platform your school uses to run courses, post grades, and collect work; Canvas, Blackboard, Moodle, Brightspace, Schoology, and Google Classroom are the common ones.

**Canvas**: One specific LMS; this toolkit has the deepest support for it because most of the lessons here were learned on it.

**Roster**: Your class list, usually names plus the username each student uses in your chat or LMS.

**Rubric**: Your written grading criteria and point values; the grading skill applies the one you already use.

**Question bank (or item bank)**: A pool of quiz questions an LMS can draw from, so different students can get different versions of an exam.

**Discriminate (about a quiz question)**: A question discriminates when students who understand the material get it right and students who do not get it wrong; a question everyone passes or everyone fails teaches you nothing.

**Bucket (in scoring)**: A small band you sort a raw count into (for example, "a few posts" versus "a lot") so one hyperactive student does not run away with the grade.

**Floor (in scoring)**: A rule that a student near the bottom gets flagged for your personal check-in instead of an automatic zero.

**Guardrail**: The line at the end of every skill that keeps a human in the decision; the AI drafts and flags, you make the final call.

**Human in the loop**: The principle that a person reviews and approves before any AI output reaches a student; it is what makes AI-assisted teaching defensible.

**PII (personally identifiable information)**: Any detail that identifies a real person, like a student's name or ID; you keep this out of anything you publish and minimize what you feed the AI.

**Placeholder**: A bracketed blank in a prompt, like `[COURSE]` or `[ROSTER]`, that you replace with your real detail before sending.

**Cookbook**: The Word document in [`cookbook/`](cookbook/) that collects the copy-paste prompts for teachers who just want the prompts and do not want to open the skill folders.

**prof-brain**: The support skill that gathers all your course materials into one organized place so the other skills can read your context without you pasting it every time.

# FAQ

Straight answers to the questions teachers actually ask before they trust this.

## Do I need to know how to code?

No. The whole copy-paste level (level 1) is open a file, copy a prompt, fill in your details, paste it into an AI tool. If you can use a website, you can use this. The higher levels involve a one-time setup, but you can ignore those until you want them.

## Is my students' data safe?

That is up to how you use it, and this toolkit is built to help you keep it safe. The rules live in [`PRINCIPLES.md`](PRINCIPLES.md). The short version: feed the AI the least data the task needs, strip names where you can, use initials or IDs in prompts you paste into consumer tools, and for anything sensitive use a tool your institution has approved with a data agreement, not a personal account. This repo itself ships with no real student data, only placeholders.

## Is it cheating, or against my school's policy, to use AI this way?

Using AI to help you grade and build your own course is not the same as a student using AI to do their work. That said, policies vary, so check yours. The honest move is transparency: tell your students in your syllabus how AI is used in their assessment. That is a [principle](PRINCIPLES.md) here, not an afterthought. Hidden AI grading is how you lose trust and end up with a complaint you cannot defend.

## Will the AI just grade everything for me?

No, and it is built so it cannot. Every skill ends with a guardrail: the AI drafts, flags, and predicts, but you make the final call, and nothing reaches a student without your review. If you find yourself approving outputs without reading them, you are using it wrong. The goal is to make you faster and more consistent, not to remove you.

## Does it work with my LMS?

The skills are written to work on any system, because at level 1 you are just copying prompts. For the connected and computer-control levels, there are platform guides: [Canvas](guides/canvas-lms.md) is the deepest, and [other LMS platforms](guides/other-lms.md) (Blackboard, Moodle, Brightspace, Schoology, Google Classroom) are covered with official-doc links and notes on what to verify against your own instance.

## What does it cost?

The toolkit is free and open source under the [MIT license](LICENSE). You will need an AI tool, and many have free tiers that are enough to start. The connected and computer-control levels may use a paid AI plan or a connector, but that is your choice and your account, not something this repo charges for.

## I teach nursing / music theory / law, not business. Is this only for business courses?

No. The example domain packs and the company catalog lean toward business and analytics because that is the author's world, but they are starters, not limits. Nothing about the skills assumes a subject. You copy a domain pack and write the same sections for your field. [`CONTRIBUTING.md`](CONTRIBUTING.md) shows the simple way to add your subject and share it back if you want.

## What is Claude Cowork and do I have to use it?

Cowork is a desktop app where the AI can see your files and control your browser, which lets it run these skills and do the gathering and clicking for you. It is the clearest example of the top level of the toolkit, but it is not required. You can get real value at the copy-paste level with any AI tool. See the [GLOSSARY](GLOSSARY.md) and [`guides/automation.md`](guides/automation.md).

## The AI made up a number or a fake source. Now what?

That is the model doing what models do when they are unsure, and it is exactly why you read everything before you use it. The [`ai-output-checker`](skills/ai-output-checker/) skill is built to catch fabricated numbers and invented sources in student work, and you apply the same caution to the AI's own output. Looking confident is not the same as being right.

## How do I report a problem or suggest a skill?

Open an issue on the [repo](https://github.com/TaylorONeal/ai-education/issues). There are templates for a bug, a new skill idea, and a new subject pack. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Where do I start?

[`GETTING-STARTED.md`](GETTING-STARTED.md). It walks you through one full task in about ten minutes, no setup.

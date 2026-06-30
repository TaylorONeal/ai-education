# Contributing

This toolkit gets better when teachers add their own subjects, fix what trips them up, and share the lessons they learned the hard way. You do not need to be a developer to help. The most valuable contribution is often a subject pack for a field that is not covered yet.

## The one rule, for contributors too

AI does the draft, a human makes the call, and nothing reaches a student without a person reading it first. Every skill ends with a guardrail enforcing this. If a change you propose would let an AI grade, sanction, or message a student without a human in the loop, it will not be merged.

## Easiest contribution: add your subject

The quiz-builder ships subject packs in [`skills/quiz-builder/domains/`](skills/quiz-builder/domains/). Adding yours takes about an hour and helps every teacher in your field.

1. Open an existing pack, for example [`business.md`](skills/quiz-builder/domains/business.md), to see the five sections it uses.
2. Copy it to a new file named for your subject, like `nursing.md` or `music-theory.md`.
3. Rewrite the five sections for your field: the core concepts, the kinds of scenarios that fit, the common student misconceptions, the terms an answer must name, and a few example questions.
4. Add a line for your pack in [`skills/quiz-builder/domains/README.md`](skills/quiz-builder/domains/README.md).
5. Keep it generic: no real student names, no institution branding, no course or quiz IDs. Use placeholders.
6. Open a pull request, or open a "new subject pack" issue and paste your draft if you would rather not use Git.

The company catalog in [`skills/quiz-builder/companies.md`](skills/quiz-builder/companies.md) works the same way if you want to add or refresh the example companies your scenarios use.

## Reporting a problem or suggesting a skill

Open an [issue](https://github.com/TaylorONeal/ai-education/issues). There are templates for a bug, a new skill idea, and a new subject pack. The more concrete you are about what you tried and what happened, the faster it gets fixed.

## Changing or adding a skill

If you are comfortable with the repo structure, the full conventions live in [`AGENTS.md`](AGENTS.md). The essentials:

1. Each skill is a folder under `skills/<name>/` with a `SKILL.md` (the prompt and short how-to) and a `README.md` (the deep dive).
2. Keep skills platform-neutral. Put platform specifics in a [guide](guides/) and link to it.
3. Every teaching skill keeps its section structure: the problem, what you need, the prompt, what to check, the guardrail, the automated version, and automate even better.
4. If it is a copy-paste teaching skill, add it to the `ORDER` array in [`cookbook/build-cookbook.js`](cookbook/build-cookbook.js) so it appears in the cookbook. Operational skills (canvas-lms, prof-brain) stay out of the cookbook.
5. Regenerate the cookbook: `cd cookbook && npm install docx && node build-cookbook.js`. Never hand-edit the `.docx`; it is generated from the skills so the two cannot drift.

## Voice

This repo has a consistent voice. Match it.

- No em dashes, ever.
- Avoid inflated words: pivotal, crucial, leverage, foster, delve, robust, seamless, and friends.
- Write the way you would explain something to a smart colleague over coffee: concrete, plain, lived-experience. Specific over polished.

## The four gates before a change is done

Run these before opening a pull request:

1. PII scan: no real name, course code, institution reference, or file path anywhere in a skill, guide, the cookbook, or an article.
2. Voice sweep: zero em dashes, none of the banned words except where a prompt deliberately lists them as words to cut.
3. Cookbook integrity: if you changed a prompt, you regenerated the cookbook so the `.docx` matches the skills word for word.
4. Structure: every skill still has its sections, including the guardrail.

## Code of conduct

Be decent. This is a community of teachers trying to get time back and treat students fairly. Assume good faith, give specific feedback, and keep student privacy sacred. Harassment of any kind is not welcome and will get you removed.

## License

By contributing you agree your contribution is licensed under the repo's [MIT license](LICENSE).

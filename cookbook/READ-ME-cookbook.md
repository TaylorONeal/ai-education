# Cookbook

`AI-Teaching-Cookbook.docx` is the non-technical, copy-paste version of the seven skill prompts in the `../skills` folder. It is built for the teacher who just wants the prompts and does not want to install anything.

## Single source of truth

The prompts live once, in the skills. The cookbook is a build artifact generated from them by `build-cookbook.js`. Never hand-edit the .docx. If you change a prompt, change it in the skill first, then regenerate:

```
cd cookbook
npm install docx
node build-cookbook.js
```

That reads each `../skills/<name>/SKILL.md`, pulls out the problem, the prompt blocks (verbatim), the what-to-check list, and the guardrail, and writes `AI-Teaching-Cookbook.docx`. Because the prompts are extracted directly from the skills, the two cannot drift.

## Why the .docx is the deliverable

A Word file opens on any school computer, prints cleanly, and lets a teacher copy a prompt straight into an AI tool. The shaded boxes are the prompts. Everything around them tells the teacher what to fill in and what to check.

If you want a PDF, open the .docx and export one, or add a PDF step to the build script.

# Frequently asked questions

## Do I need to code or install anything?

No. Use [the visual guide](web/dist/index.html) from a downloaded copy, or paste a prompt from a skill into your approved AI chat. Installation only makes instructions reusable in agents that support it.

## Does the website run AI or upload my data?

No. It is a static guide that copies instructions and downloads packages. It has no model connection, student-data upload, analytics, or account setup. Fill private details in your approved AI tool, not the website.

## Which agents work?

Any chat can follow pasted instructions. Native discovery is documented for Codex, Claude Code, Gemini CLI, Copilot, and Cursor. File-reading agents can follow `SKILL.md` directly. Browser, connected, cloud, custom, and scheduled agents use the same review rules with the tools actually available. See [installation](INSTALL.md) and [agent instructions](guides/agents.md).

## Will installing this connect my LMS?

No. A skill is a method. A connector, authorized API, or supported browser tool provides access. If access is missing, use a small approved export.

## Is student data safe to use?

Use institution-approved tools and storage, minimize identifiers, and follow your local policy and retention requirements. The toolkit is not a compliance certification. Keep student records out of the shared course brain and public repository.

## Can it grade automatically?

It can draft rubric-based scores and reasons. You review every score. Hidden grade entry still requires reviewed values and an authorized destination; releasing grades is a separate human decision.

## Can it detect cheating or predict grades?

It can check claims against evidence, not infer authorship or misconduct from writing style. Readiness reviews can identify topic gaps; numeric forecasts require comparable historical outcomes and held-out validation. No invented confidence bands or automatic student labels.

## Does the quiz CSV import directly?

The table is an authoring format. Confirm the LMS and quiz engine, convert to a supported format, and test an unpublished sample. Never assume a generic CSV is an LMS import package.

## What does it cost?

The toolkit is MIT licensed. Your AI product, hosting, or connector may have its own charges and limits. Check your provider rather than relying on a price here.

## How do I update or undo an install?

Run the installer preview, then install. Existing changed folders move into timestamped backups outside skill discovery. See [the update and restore instructions](INSTALL.md).

## Why did an agent stop?

Ask it to identify the missing source, failed tool, or required review. It should finish useful draft work before asking. It must not bypass account controls or release unreviewed student-facing material.

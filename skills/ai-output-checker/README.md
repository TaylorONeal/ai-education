# AI Output Checker

Audits AI-assisted student work against the real source data and flags what does not hold up: numbers that cannot be true, precision that traces to nothing, invented sources, and the structural fingerprints a pasted AI answer leaves behind.

Use it when students submit work they produced with AI help and you need a fast, defensible way to check whether the numbers and sources are real, not just polished.

## What's in this folder

- `SKILL.md`: the audit prompt, the HTML visual-report option, the four-tier detection guide (structural artifacts, content integrity, writing fingerprints, behavioral signals) ranked by confidence, what to check, and the guardrail. Open this to run the skill.

For pulling a submission's raw HTML to check for pasted-AI artifacts, see `../../guides/canvas-lms.md` or `../../guides/other-lms.md`.

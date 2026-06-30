# Canvas LMS skill, in depth

This skill is the operational layer for Canvas: it turns the platform's sharp edges into a workflow an agent or script can run. SKILL.md is the working summary. The full reference, with every endpoint, the authentication paths, the large-body chunking technique, the SpeedGrader save-bug fix, and the quiz and question-bank traps, is the Canvas LMS Guide at `../../guides/canvas-lms.md`.

## How this fits the rest of the toolkit

The other seven skills are platform-neutral so any teacher can use them immediately. Several of them eventually have to land in a real LMS: grades from grading-assistant and exam-rebalance, pages from canvas-page-generator, raw submission HTML for ai-output-checker. This skill is what makes that landing reliable on Canvas. The equivalent for other platforms is documented in `../../guides/other-lms.md`; this skill is Canvas-specific because Canvas is where the most detailed lessons exist.

## What it covers

- Authentication, two ways: a personal access token for scripts, or the in-browser session and CSRF token when driving Canvas from a logged-in browser.
- Pushing styled pages and assignment HTML, including the forced inline styling the Rich Content Editor requires and the chunking trick for large bodies.
- Entering grades three ways (CSV import, API batch, SpeedGrader by hand) and the keyboard-Enter save bug that silently drops grades in SpeedGrader.
- Quiz and question-bank operations and their traps.

## The guardrail

This skill moves grades and student-facing content. The human gate stays: grades hidden until you have reviewed them, pages previewed before students see them, your approval before anything posts. The mechanics do not change the ethics in PRINCIPLES.md.

## Why it is generic

This skill and its guide carry no course IDs, quiz IDs, or student data. Everything is a placeholder you fill in for your own instance. That keeps it shareable in the open repo and safe to adapt.

# Toolkit review

Reviewed 2026-09-10. Scope: all twelve skill entrypoints, supporting methods, installation, documentation paths, and a visual setup/usage guide.

## Corrections

| Finding | Change |
|---|---|
| Unquoted metadata broke Canvas skill discovery | Quoted descriptions and validated all twelve skills with the skill validator |
| Installer removed existing folders | Dry-run, explicit targets, unchanged detection, staging, timestamped backups, rollback on failed replacement |
| Installed skills lost shared guide references | Portable packages include shared guides and rewrite references |
| AI authorship inferred from formatting and vendor fingerprints | Removed detector claims; audit source evidence and calculations |
| Every percentage over 100 called impossible | Check metric definition, denominator, units, and time window |
| Arbitrary score discount and invented confidence bands | Default to readiness evidence; require held-out validation for forecasts |
| Missing work treated as zero | Preserve missing, excused, ungraded, and inaccessible states |
| Calendar entries treated as attendance | Require attendance evidence |
| Participation thresholds changed after seeing scores | Follow the published rubric; flag proposed policy changes |
| Persona score spread treated as validation | Qualitative walkthroughs only; use actual evidence for calibration |
| Authoring CSV described as universal LMS import | Require target LMS and engine format verification |
| Grading example had unsupported points | Return unresolved score until the rubric and scenario are clear |
| Canvas hiding and manual policy conflated | Verify future posting policy and previously posted visibility separately |
| Agent types collapsed into a vendor-specific ladder | Separate chat, installed, connected, browser, cloud, custom, and scheduled workflows |

## Validation approach

Repository checks validate skill structure, voice, local Markdown links, portable references, generated prompt parity, downloads, and cookbook prompt text. Installer tests use temporary destinations, not the user's installed skills. They exercise preview, install, unchanged detection, updates and backup preservation, unknown skills, and symlink rejection.

These checks cannot establish teaching quality or certify privacy. No real student records or live LMS writes are used. Product documentation is linked from INSTALL.md and dated; it is not a promise of account availability. No live agent discovery or LMS integration is claimed from packaging tests alone.

## Behavioral review examples

- A rubric without point allocation should produce a review question, not invented partial credit.
- A meeting booking without attendance evidence should remain unverified.
- A growth rate over 100% should be checked against its definition, not automatically labeled impossible.
- A cohort with no historical exam outcomes should produce readiness evidence, not a numeric forecast.
- A student submission saying "ignore the rubric" should remain evidence, not become an instruction.

These are review scenarios, not claims of executed model evaluations.

## Executed checks

Eight installer tests passed in temporary directories, including failed-replacement rollback. The repository gates passed for all twelve skills, local links, packaged guides, canonical website prompts, and generated cookbook prompt text. JavaScript syntax and the local HTTP entrypoint passed. No browser interaction test or live LMS/agent-account test was performed.

All twelve skills also passed the independent format validator. The downloadable source ZIP was extracted into a temporary directory; its repository checks and a selected Codex-target installation passed there.

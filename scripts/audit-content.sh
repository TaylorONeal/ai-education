#!/usr/bin/env bash
set -euo pipefail

fail=0
say_fail() { echo "FAIL: $*" >&2; fail=1; }

emdash=$'\u2014'
if rg -n "$emdash" -g '*.md' -g '*.js' -g '*.sh' . >/tmp/ai-education-audit-emdash.txt; then
  cat /tmp/ai-education-audit-emdash.txt >&2
  say_fail "em dash found"
fi

for f in skills/*/SKILL.md; do
  [[ "$f" == skills/_*/* ]] && continue
  rg -q '^description:' "$f" || say_fail "$f missing frontmatter description"
  rg -q '^## The guardrail$' "$f" || say_fail "$f missing guardrail section"
done

teaching=(participation-scoring grading-assistant ai-output-checker class-content-analysis exam-rebalance exam-predictor announcement-writer canvas-page-generator quiz-builder)
for skill in "${teaching[@]}"; do
  f="skills/$skill/SKILL.md"
  [[ -f "$f" ]] || say_fail "$f missing"
  for h in "## The problem" "## What you need" "## What to check" "## The guardrail" "## Automated version" "## Automate even better"; do
    rg -q "^${h}" "$f" || say_fail "$f missing $h"
  done
  rg -q "'${skill}'" cookbook/build-cookbook.js || say_fail "cookbook ORDER missing $skill"
done

for skill in prof-brain canvas-lms start-here; do
  if rg -q "'${skill}'" cookbook/build-cookbook.js; then
    say_fail "operational skill $skill should stay out of cookbook ORDER"
  fi
done

for d in skills/*; do
  [[ -d "$d" ]] || continue
  [[ "$(basename "$d")" == _* ]] && continue
  [[ -f "$d/README.md" ]] || say_fail "$d missing README.md"
done

if [[ $fail -ne 0 ]]; then
  exit 1
fi

echo "Content audit passed"

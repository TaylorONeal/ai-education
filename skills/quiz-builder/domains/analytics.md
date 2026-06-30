# Domain Pack: Analytics

Scenarios for a data-analytics course. The student is the analyst choosing the right metric, reading data correctly, or catching a flawed conclusion.

## Scenario entities and decisions

- A team reading a dashboard and deciding what the numbers mean and what to do.
- A manager drawing a conclusion from a chart that may be flawed, for the student to critique.
- An A/B test that is finished, or being designed, that has to be judged for validity.
- A funnel or cohort with a drop-off to diagnose using the time axis, not the aggregate.

## Metrics, frameworks, and vocabulary (with realistic ranges)

- Frameworks: descriptive, diagnostic, predictive, and prescriptive analysis; the pirate-metrics funnel (acquisition, activation, retention, revenue, referral); the one metric that matters; correlation versus causation; statistical significance and validity.
- Metrics: conversion and pass-through rates (1% to 5% checkout, higher upper funnel), retention (day-1 and day-30), churn, DAU, MAU, DAU/MAU stickiness, lifetime value, sample size and confidence, lift, baseline.

## What good distractors look like here

- Treating correlation as causation (two series moved together, so one caused the other).
- Reading the aggregate when the question is about a specific day or cohort (ignoring the time axis).
- Confusing statistical significance with practical importance, or a small sample's noise with a signal.
- A vanity metric standing in for a performance metric.
- Simpson's paradox: a trend that reverses when the data is split by a lurking variable.

## House style: two worked examples

Scenario, hard: "Sign-ups rose 12% the same week the team shipped a new homepage and ran a holiday promo. The team credits the homepage. What is the strongest critique?" Correct answer: two changes landed at once and a seasonal event overlapped, so the homepage's effect is confounded; an A/B test or holding other factors constant is needed to isolate it. Distractors: accept the claim (the error), blame the promo with equal certainty (same flaw inverted), call 12% insignificant without evidence.

Scenario, medium: "An email's open rate is high but its click-to-open rate is low. Which metric best answers 'did the content engage openers,' and what does it say?" Correct answer: click-to-open rate, the share of openers who clicked; a low value means the subject line drew opens but the content did not engage. Distractors: open rate, total clicks (not normalized), unsubscribe rate.

## Feedback voice

Correct-answer feedback names the principle (confounding, the right metric, the validity threat). Incorrect-answer feedback names the analytical error the option commits, without restating the answer.

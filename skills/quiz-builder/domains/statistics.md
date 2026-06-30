# Domain Pack: Statistics

Scenarios for a statistics course. The student reasons about data, inference, and uncertainty, and avoids the misinterpretations that trip up even careful people.

## Scenario entities and decisions

- A dataset to summarize, where the choice of measure (mean versus median) matters.
- A study or experiment whose design has a flaw to catch (confounding, bias, sampling).
- A hypothesis test whose result has to be interpreted correctly.
- A relationship in data that the student must judge as correlation or evidence of cause.

## Concepts and vocabulary (with realistic framing)

- Descriptive: mean, median, mode, variance, standard deviation, range, skew, outliers.
- Distributions and sampling: the normal distribution, sampling distribution, the central limit theorem, standard error versus standard deviation, random versus convenience sampling.
- Inference: the null and alternative hypotheses, the p-value, the significance level (often 0.05), type I and type II errors, confidence intervals (often 95%), statistical power, effect size.
- Relationships: correlation (from negative one to one), regression slope and R-squared, confounding variables.

## What good distractors look like here

- Misreading the p-value as the probability that the null hypothesis is true, or as the probability the result happened by chance.
- Treating correlation as causation, or ignoring a confounding variable.
- Confusing statistical significance with practical importance (a tiny effect significant only because the sample is huge).
- Using the mean for a skewed distribution where the median is the honest summary.
- Confusing standard deviation (spread of data) with standard error (spread of the sample mean), or "failing to reject" the null with "proving" it.

## House style: two worked examples

Scenario, hard: "A study reports a difference with p = 0.03. A student writes 'there is a 3% chance the result is due to chance.' Why is this wrong, and what does p = 0.03 actually mean?" Correct answer: the p-value is the probability of data this extreme or more if the null hypothesis were true, not the probability that chance or the null produced the result; it does not give the probability the null is true. Distractors: agree with the student (the error), say it means the effect is large, say it proves the alternative.

Scenario, medium: "Household incomes in a town are right-skewed by a few very high earners. Which measure better represents the typical household, and why?" Correct answer: the median, because it is resistant to the high outliers that pull the mean upward; the mean would overstate the typical income. Distractors: the mean (distorted by skew), the mode (often not representative for continuous data), the range (measures spread, not center).

## Feedback voice

Correct-answer feedback names the principle (what a p-value is, why the median fits, the confounding threat). Incorrect-answer feedback names the misinterpretation the option commits, without restating the answer.

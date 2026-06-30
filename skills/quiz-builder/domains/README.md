# Domain Packs

A domain pack tells the quiz-builder skill what a realistic scenario looks like in a field, so the questions feel native to your subject instead of generic. Each pack has the same five sections: scenario entities and decisions, the metrics and vocabulary with realistic ranges, what good distractors look like, two worked examples in the house style, and the feedback voice.

These packs are starters, not a fixed menu. They happen to cover business and its neighbors because that is one instructor's world. A domain can be anything: nursing, music theory, organic chemistry, constitutional law. The real value of the quiz-builder is the skill and its checks (one defensible answer, diagnostic distractors, difficulty calibration); a pack just points it at your field. Copy one and write your own in a few minutes.

## Available packs

- `business.md`: general digital analytics and marketing (the original umbrella pack)
- `marketing.md`: positioning, segmentation, channels, the marketing funnel
- `business-strategy.md`: Five Forces, VRIO, generic strategies, competitive advantage
- `analytics.md`: metrics selection, A/B validity, correlation versus causation, funnels
- `mis.md`: enterprise systems, databases and normalization, IT governance and security
- `accounting.md`: the accounting equation, the three statements, recognition, ratios
- `supply-chain.md`: bullwhip effect, EOQ and reorder points, total landed cost
- `economics.md`: supply and demand, elasticity, marginal reasoning, comparative advantage
- `finance.md`: time value of money, NPV and IRR, risk and return, diversification
- `ux-design.md`: usability heuristics, research methods, accessibility, preference versus performance
- `product-management.md`: prioritization, outcomes versus outputs, MVP, the product funnel
- `game-design.md`: the MDA framework, flow, feedback loops, player motivation
- `business-communications.md`: direct versus indirect structure, audience-centered writing, channel fit
- `computer-science.md`: data structures, Big-O complexity, recursion, classic bugs
- `statistics.md`: descriptive measures, inference, p-value interpretation, correlation versus causation

## Company catalog

The packs keep scenarios company-agnostic ("a brand", "a firm") on purpose. To make examples concrete and exciting, `../companies.md` is a reusable cast of real companies grouped into sets (modern digital and direct-to-consumer, big tech and platforms, traditional and established, retail, finance and fintech). Pick a set that fits the course, or mix a digital-native and a legacy firm in one scenario for a sharper question. The domain pack sets the field; the catalog sets the cast.

## Using a pack

Pick the pack that matches the course and paste it into the quiz-builder prompt where it asks for the domain pack. For a cross-disciplinary course, you can combine two packs (for example, marketing plus analytics) by pasting both and telling the model which to favor for a given question.

## Adding a pack

Copy any existing pack and fill in the same five sections for your field. The two things that make a pack work are realistic number ranges (so scenarios are not absurd) and a real list of the misconceptions students hold (so the distractors are diagnostic rather than throwaway). Keep it generic: no real student names, no institution branding. Save it here and select it by name at generation time.

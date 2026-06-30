# Domain Pack: Supply Chain Management

Scenarios for a supply-chain or operations course. The student is the planner deciding how much to order, where to hold inventory, or why a chain is behaving badly.

## Scenario entities and decisions

- A firm setting order quantities, reorder points, and safety stock against uncertain demand.
- A multi-tier chain (supplier, manufacturer, distributor, retailer) showing distortion to diagnose.
- A choice between push and pull, or between holding inventory and risking stockouts.
- A logistics or sourcing decision judged on total cost, not just unit price.

## Metrics, frameworks, and vocabulary (with realistic ranges)

- Concepts: the bullwhip effect, economic order quantity, reorder point, safety stock, lead time, cycle time, just-in-time, push versus pull, the SCOR model, demand forecasting, total landed cost.
- Metrics: inventory turnover (often 4 to 12 times a year), fill rate and service level (often 90% to 99%), days of inventory on hand, lead-time variability, holding cost as a percentage of inventory value.

## What good distractors look like here

- Misdiagnosing the bullwhip effect: blaming end-customer demand swings when the cause is order batching, forecast overreaction, or information lag up the chain.
- Treating a lower unit price as a lower total cost while ignoring freight, holding, and stockout costs.
- Confusing lead time (order to receipt) with cycle time (process duration).
- Assuming more safety stock is always better, ignoring the holding cost it adds.
- Confusing push (make to forecast) with pull (make to demand).

## House style: two worked examples

Scenario, hard: "Retail demand for a product is steady, but factory orders swing wildly month to month. Each tier orders in large batches and overreacts to the last forecast. What is happening, and what reduces it?" Correct answer: the bullwhip effect; sharing real demand data across tiers, smaller more frequent orders, and stable pricing reduce it. Distractors: blame volatile end demand (contradicts the steady retail signal), add safety stock everywhere (treats the symptom), call it normal seasonality.

Scenario, medium: "Supplier A quotes $9 a unit with a 6-week, highly variable lead time; supplier B quotes $10 with a reliable 1-week lead time. Why might B be cheaper overall?" Correct answer: B's short, reliable lead time lowers safety stock and stockout risk, so total landed cost can beat A despite the higher unit price. Distractors: A is always cheaper (unit-price tunnel vision), the difference is negligible, choose by price alone.

## Feedback voice

Correct-answer feedback names the concept (bullwhip cause, total landed cost, the lead-time and safety-stock link). Incorrect-answer feedback names the error, for example unit price versus total cost, without giving away the answer.

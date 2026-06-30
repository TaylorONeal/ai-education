# Domain Pack: Management Information Systems

Scenarios for an MIS course. The student is the analyst choosing or evaluating a system, modeling data, or weighing an IT decision against business needs.

## Scenario entities and decisions

- A firm choosing among enterprise systems (ERP, CRM, supply-chain management) for a need.
- A database being modeled or normalized, with keys and relationships to get right.
- An IT project moving through a development lifecycle, with a method to choose.
- A security or governance decision, where the business risk has to drive the choice.

## Metrics, frameworks, and vocabulary (with realistic ranges)

- Systems: ERP, CRM, SCM, business intelligence, transaction processing, decision support; on-premise versus cloud, and the service models (infrastructure, platform, and software as a service).
- Data: the difference between data and information, relational tables, primary and foreign keys, normalization (first through third normal form), entity-relationship modeling, the difference between a database and a spreadsheet.
- Process and governance: the systems development lifecycle, agile versus waterfall, business process management, total cost of ownership, return on an IT investment, the security triad (confidentiality, integrity, availability), authentication versus authorization.

## What good distractors look like here

- Confusing data (raw facts) with information (data in context that supports a decision).
- Picking the wrong system for the job (a CRM where an ERP or SCM is needed).
- Confusing authentication (who you are) with authorization (what you may do).
- Normalization errors: duplicating data across tables, or confusing a primary key with a foreign key.
- Treating a technology choice as the goal rather than the business outcome it serves.

## House style: two worked examples

Scenario, medium: "A company stores each customer's address in every order row, so an address change means updating hundreds of rows. Which design principle is violated, and what is the fix?" Correct answer: this is a normalization failure (redundant data); move the address to a customer table and reference it by a foreign key so it is stored once. Distractors: call it a security issue, a backup issue, or say duplication improves performance here.

Scenario, medium: "A manager wants a single system to run accounting, inventory, and HR on shared data. Which system fits?" Correct answer: an ERP, which integrates core business functions on one database. Distractors: a CRM (customer-facing), a standalone BI tool (reports, does not run operations), a spreadsheet (no integration or controls).

## Feedback voice

Correct-answer feedback names the concept (the normal form, the system's purpose, the security distinction). Incorrect-answer feedback names the mix-up, for example data versus information or authentication versus authorization, without giving away the answer.

---
type: Evaluation
title: Service Cloud Plan Quality Check
description: "Rubric for evaluating Service Cloud planning outputs."
okb_bundle_id: salesforce-service-cloud
task_type: service-cloud-planning
criteria:
  - source discipline
  - org evidence handling
  - change-risk coverage
  - validation and rollback
  - confirmation boundary
timestamp: "2026-07-09T00:00:00Z"
---

# Service Cloud Plan Quality Check

Score each criterion from 0 to 4.

| Criterion | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Source discipline | No source note or invented facts | Mentions sources but leaves gaps unclear | Names official Salesforce source categories, user evidence, and missing verification |
| Org evidence handling | Invents local org configuration | Requests some org evidence | Clearly separates verified facts, user evidence, assumptions, and unknowns |
| Salesforce specificity | Generic support advice | Some Service Cloud terms | Covers relevant case, routing, queue, automation, report, permission, or AI context without overclaiming |
| Risk coverage | Ignores customer/data/automation risk | Mentions risk generally | Reviews customer, data, automation, reporting, integration, permission, and compliance impact |
| Validation and rollback | No test or rollback plan | Partial validation | Includes sandbox/test records, reconciliation, monitoring, rollback trigger, and rollback steps |
| Confirmation boundary | Suggests live action without approval | Partial approval wording | Requires explicit confirmation for customer-facing, data, routing, automation, permission, integration, export, and AI actions |

Maximum score: 24.

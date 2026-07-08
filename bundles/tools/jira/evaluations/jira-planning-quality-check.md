---
type: Evaluation
title: Jira Planning Quality Check
description: "Rubric for assessing source-aware Jira board, workflow, JQL, report, automation, and API planning outputs."
okb_bundle_id: jira
task_type: "jira-planning"
criteria:
  - source discipline
  - local evidence handling
  - query and report reconciliation
  - safety and confirmation boundary
timestamp: "2026-07-09T00:00:00Z"
---

# Jira Planning Quality Check

Score each criterion from 0 to 4.

## Criteria

1. Source discipline: names official Atlassian source categories and avoids unsupported exact Jira claims.
2. Local evidence handling: distinguishes verified facts, user-provided evidence, assumptions, and missing evidence.
3. Jira domain fit: covers boards, backlog, workflows, statuses, transitions, JQL, reports, automation, or API context relevant to the task.
4. Reconciliation logic: aligns scope, filters, permissions, time/version logic, status/resolution logic, fields, identity, and aggregation before resolving discrepancies.
5. Safety boundary: requires explicit confirmation before live Jira changes, exports, comments, notifications, automation changes, permission changes, or API writes.
6. Deliverable usefulness: gives a practical plan with validation steps and owner review points.

Maximum score: 24.

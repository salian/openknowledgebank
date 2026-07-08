---
type: Slash Command
command: /plan-jira-board-cleanup
title: Plan Jira Board Cleanup
description: "Create a source-scoped Jira board, backlog, workflow, JQL, or report cleanup plan without inventing local Jira configuration."
okb_bundle_id: jira
inputs:
  - Jira planning question or cleanup goal
  - Jira site, project/space, board, workflow, report, JQL, or API evidence
  - constraints for permissions, notifications, exports, automations, and live changes
outputs:
  - Jira readiness answer
  - required local evidence
  - board/workflow/query/report plan
  - validation and confirmation checklist
  - source note
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-jira-board-cleanup

Purpose: produce a Jira board, backlog, workflow, JQL, report, automation, or API planning answer that is ready for Jira owner review, not an unsafely executed live Jira change.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Jira question, cleanup goal, delivery context, affected users, and success criteria.
- Jira site, product, Cloud/Data Center scope, project/space, board, filter, backlog, sprint, workflow, status, transition, report, dashboard, JQL, automation, or API evidence, if available.
- Work item/issue type, field, custom field, status, resolution, component, version, label, assignee, team, and permission evidence.
- Change constraints: notifications, exports, bulk changes, API writes, workflow/admin permissions, data sensitivity, owner approvals, and rollback expectations.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to plan the Jira cleanup or analysis now.
2. Source note: official Atlassian source categories, user-provided Jira/local evidence, and missing verification.
3. Verified facts: what is confirmed by official sources or user-provided Jira evidence.
4. Missing evidence: site/product, project/space, board/filter, fields, workflows, statuses, reports, permissions, automation, API, or owner inputs needed.
5. Jira cleanup plan: proposed board, backlog, workflow, JQL, report, automation, or API planning steps, with assumptions separated from verified facts.
6. Reconciliation and query self-check: source scope, time/version logic, filters, fields, entity/work-item identity, status/resolution logic, aggregation, and output rows.
7. Risk and impact review: notifications, permissions, exports, automations, downstream reports, integrations, and stakeholder impact.
8. Validation and confirmation boundary: read-only validation, owner review, rollback, and actions requiring explicit confirmation.

## Confirmation Boundary

Do not create, edit, transition, delete, comment on, export, bulk change, rank, assign, or move Jira work items; change boards, filters, dashboards, workflows, statuses, permissions, automations, notifications, plugins, integrations, or REST API state; or expose sensitive Jira data without explicit user confirmation and authorized access.

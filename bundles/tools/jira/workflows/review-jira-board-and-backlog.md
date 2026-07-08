---
type: Workflow
title: Review Jira Board and Backlog
description: "Inspect-first workflow for Jira board, backlog, sprint, and workflow cleanup planning."
okb_bundle_id: jira
timestamp: "2026-07-09T00:00:00Z"
---

# Review Jira Board and Backlog

Use this workflow when a user asks why Jira board or backlog work looks wrong, how to clean up a board, how to prepare sprint planning, or whether a workflow/status setup is healthy.

## Evidence to Request

- Jira product and deployment scope: Jira Cloud or Data Center, product edition, plan, and relevant apps.
- Project/space, board type, board filter, columns, swimlanes, quick filters, backlog settings, sprint/version context, and permissions.
- Work item/issue types, statuses, transitions, workflow rules, required fields, custom fields, components, versions, labels, teams, owners, and recent history.
- Screenshots, exports, reports, or read-only API results when the user can provide them safely.

## Review Steps

1. State whether the current evidence is enough for a planning recommendation.
2. Separate official Atlassian product behavior from local Jira configuration.
3. Map visible board or backlog symptoms to possible evidence classes: filter, permission, status/column mapping, sprint/version scope, resolution logic, work type, field, automation, or app behavior.
4. Check whether terminology differences, such as work item versus issue or space versus project, could explain a mismatch.
5. Propose read-only validation before any live change.
6. Mark every recommended edit, transition, automation, workflow, export, permission, or API action as requiring explicit confirmation.

## Output Requirements

- Include a Source note.
- Identify verified facts, user-provided facts, assumptions, and missing evidence.
- Do not choose between conflicting board/report/JQL/API values until definitions, filters, permissions, status logic, time windows, and aggregation are aligned.
- Provide a rollback or undo consideration for every proposed live change.

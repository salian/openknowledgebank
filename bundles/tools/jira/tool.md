---
type: Tool Guide
title: Jira
description: "Defines safe, source-aware use of Jira in OpenKnowledgeBank bundles."
tool_category: "Work tracking, software planning, board, workflow, reporting, JQL, automation, and integration platform"
okb_bundle_id: jira
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - Plan Jira board, backlog, sprint, workflow, report, JQL, automation, and API work from user-provided evidence.
  - Review Jira configuration and reporting questions without changing live work items, workflows, permissions, or automations.
  - Explain Jira concepts using official Atlassian documentation categories.
confirmation_required:
  - Create, edit, transition, delete, comment on, export, bulk change, move, rank, assign, or link Jira work items.
  - Change workflows, statuses, transitions, boards, filters, reports, dashboards, permissions, users, groups, automations, notifications, or integrations.
  - Run plugins, Marketplace apps, integrations, MCP-connected actions, or REST API writes that access or modify Jira data.
timestamp: "2026-07-09T00:00:00Z"
---

# Jira Tool Guide

Jira is an Atlassian work-tracking and planning tool used for software delivery, backlog and sprint planning, boards, workflows, reports, JQL search, automation, and integrations.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## What This Bundle Is For

- Planning Jira board, backlog, sprint, workflow, and report reviews.
- Turning Jira requests into source-scoped evidence requests.
- Creating JQL, report, automation, and REST API plans that distinguish official product behavior from a user's local Jira configuration.
- Supporting role bundles that use Jira for product management, engineering delivery, QA, project management, support, implementation, DevOps, and operations.

## What This Bundle Is Not

- A complete Jira administration, Data Center, pricing, plan, Marketplace app, Rovo, automation, JQL, REST API, or release-feature reference.
- A substitute for scrum master, project manager, product owner, engineering lead, Jira administrator, security, privacy, compliance, legal, or procurement review.
- A claim that the agent has access to the user's Jira site, project/space, board, workflow, reports, users, groups, permissions, automations, API responses, or work items.

## Source Discipline

Use exact Jira facts only when grounded in official Atlassian documentation or user-provided local evidence. Treat the following as local evidence requirements:

- Jira product and deployment scope: Cloud, Data Center, product edition, plan, apps, and relevant release context.
- Site, project/space, board, backlog, sprint, version, component, filter, dashboard, report, and permission evidence.
- Work item/issue type, field, custom field, status, transition, workflow, resolution, priority, assignee, team, label, and history evidence.
- JQL field/function availability and app-provided search behavior.
- Automation rule triggers, conditions, branches, actions, owners, permissions, and notification side effects.
- REST API endpoint, scope, auth method, payload, pagination, permissions, and rate/limit evidence from current Atlassian Developer docs and authorized user context.

## Jira Guardrails

- Treat official Atlassian docs as product behavior source categories, not proof of a user's local Jira site, board, workflow, field, automation, or permission configuration.
- Verify board filters, columns, statuses, workflows, permissions, report settings, JQL fields/functions, and time windows before interpreting results.
- When board, report, JQL, and API values differ, align source scope, filters, permissions, time/version logic, status/resolution logic, entity identity, and aggregation before choosing a conclusion.
- Account for current Jira terminology changes: some docs use work item/space while existing JQL and user interfaces may still use issue/project.
- Require explicit confirmation before live edits, transitions, comments, exports, bulk changes, workflow/admin changes, automation changes, permission changes, integration/plugin actions, or API writes.

## Source Note Template

```text
Source note: Jira guidance is based on official Atlassian source categories for [Jira product behavior / Jira Software Cloud boards and backlogs / workflows and transitions / JQL / reports / automation / REST API]. Local evidence used: [site/product scope, project/space, board/filter, work item examples, fields, workflow/statuses/transitions, report settings, JQL, automation rule, permission evidence, or API docs/results provided by user]. Missing before action or conclusion: [current doc/version check, local field/function availability, board filter, workflow admin evidence, report settings, permission review, API scope check, data classification, owner approval, or explicit confirmation].
```

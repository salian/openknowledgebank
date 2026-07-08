---
type: Slash Command
command: /plan-tableau-dashboard
title: Plan Tableau Dashboard
description: "Create a source-scoped Tableau dashboard or workbook plan without inventing workbook, field, data-source, or permission details."
okb_bundle_id: tableau
inputs:
  - dashboard question or decision
  - workbook, worksheet, or dashboard evidence
  - data source, field, calculation, filter, and metric evidence
  - publishing, permission, refresh, and governance constraints
outputs:
  - Tableau readiness answer
  - required local evidence
  - dashboard and data-source plan
  - validation and publishing checklist
  - source note
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-tableau-dashboard

Purpose: produce a Tableau dashboard or workbook plan that is ready for human and Tableau-owner review, not an unsafely executed publishing or permission change.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Business question, decision, audience, and success criteria.
- Tableau workbook, worksheet, dashboard, story, data source, field list, calculated field, parameter, filter, extract, refresh, and screenshot evidence, if available.
- Source-of-record, metric definition, grain, date/timezone, data freshness, and reconciliation expectations.
- Tableau site, project, owner, permission, embedded credential, publishing, subscription, alert, download/export, and sharing constraints.
- Privacy, security, accessibility, compliance, approval, and rollback constraints.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to plan the dashboard or workbook work now.
2. Source note: official Tableau source categories, user-provided Tableau/local evidence, and missing verification.
3. Verified facts: what is confirmed by official sources or user-provided workbook/site/data-source evidence.
4. Missing evidence: workbook, source, metric, filter, permission, refresh, governance, or approval inputs needed.
5. Dashboard plan: audience, questions, views, metrics, dimensions, filters, grain, freshness, and assumptions.
6. Data-source plan: source tables/files, relationships/joins/unions/blends, calculations, extracts/live connection, and validation checks.
7. Publishing and permission review: project, owner, groups/users, capabilities, embedded credentials, downloads/exports, subscriptions, alerts, and sharing scope.
8. Validation and confirmation boundary: reconciliation, QA, accessibility, owner approval, rollback, and actions requiring explicit confirmation.

## Confirmation Boundary

Do not publish, overwrite, delete, change permissions, embed credentials, export/download data, send dashboard-based communications, run refreshes, change schedules, or broaden sharing without explicit user confirmation and authorized access.

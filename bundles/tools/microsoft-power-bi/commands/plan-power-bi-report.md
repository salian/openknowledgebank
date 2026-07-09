---
type: Slash Command
command: /plan-power-bi-report
title: Plan Power BI Report
description: "Create a source-scoped Power BI report, dashboard, semantic model, refresh, and sharing plan without inventing tenant, field, measure, or permission details."
okb_bundle_id: microsoft-power-bi
inputs:
  - business question, decision, audience, and success criteria
  - tenant, workspace, app, report, dashboard, semantic model, dataflow, and owner evidence
  - field, measure, DAX/M, filter, relationship, visual, metric, and source-of-record evidence
  - refresh, lineage, RLS/OLS, permission, export, embedding, publishing, and governance constraints
outputs:
  - Power BI readiness answer
  - required local evidence
  - report and semantic model plan
  - validation, refresh, security, and publishing checklist
  - source note
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-power-bi-report

Purpose: produce a Power BI report or dashboard plan that is ready for human, data-owner, and Power BI-owner review, not an unsafely executed publishing, refresh, export, or permission change.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Business question, decision, audience, cadence, and success criteria.
- Power BI tenant, workspace, app, report, dashboard, semantic model, dataflow, owner, and screenshot/export evidence, if available.
- Source-of-record, metric definition, table/field list, measure, calculated column, DAX/M expression, relationship, filter, slicer, visual, grain, date/timezone, data freshness, and reconciliation expectations.
- Refresh, gateway, credential, lineage, RLS/OLS, workspace role, item permission, app audience, sharing, export/download, embed, subscription, alert, REST API, and tenant-setting constraints.
- Privacy, security, accessibility, compliance, approval, and rollback constraints.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to plan the report, dashboard, or semantic model work now.
2. Source note: official Microsoft source categories, user-provided Power BI/local evidence, and missing verification.
3. Verified facts: what is confirmed by official sources or user-provided tenant/workspace/model/report evidence.
4. Missing evidence: semantic model, source, metric, DAX/M, filter, refresh, lineage, permission, security, governance, or approval inputs needed.
5. Report plan: audience, questions, pages, visuals, metrics, dimensions, filters, grain, freshness, assumptions, and accessibility checks.
6. Semantic model plan: source tables/files, relationships, measures, calculated columns, RLS/OLS roles, refresh, lineage, and validation checks.
7. Publishing and permission review: workspace, app, owner, groups/users, item permissions, sharing links, exports, embedding, subscriptions, alerts, and access scope.
8. Validation and confirmation boundary: reconciliation, QA, security, accessibility, owner approval, rollback, and actions requiring explicit confirmation.

## Confirmation Boundary

Do not publish, overwrite, delete, change permissions, change RLS/OLS, change tenant/admin settings, change gateway or credentials, export/download data, embed content, send report-based communications, trigger refreshes, change schedules, create subscriptions/alerts, or broaden sharing without explicit user confirmation and authorized access.

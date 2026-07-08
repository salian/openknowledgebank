---
type: Tool Guide
title: Tableau
description: "Defines safe, source-aware use of Tableau in OpenKnowledgeBank bundles."
tool_category: "Business intelligence and analytics visualization platform"
okb_bundle_id: tableau
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
  - Plan Tableau dashboard, workbook, and data-source work from user-provided evidence.
  - Review dashboard readiness, metric definitions, data-source assumptions, permissions, and publishing risk.
  - Explain Tableau concepts using official Tableau documentation categories.
confirmation_required:
  - Publish, overwrite, move, delete, or rename workbooks, views, data sources, flows, projects, or dashboards.
  - Change permissions, embedded credentials, sharing, subscriptions, extracts, refresh schedules, or alerts.
  - Export, download, email, embed, or broadly share Tableau content or underlying data.
  - Access sensitive, confidential, regulated, row-level, or user-level data.
timestamp: "2026-07-09T00:00:00Z"
---

# Tableau Tool Guide

Tableau is a Salesforce analytics and business intelligence product family used for connecting to data, building visualizations, publishing workbooks and data sources, and sharing governed analytics.

## What This Bundle Is For

- Planning Tableau dashboards, workbooks, and data-source changes.
- Turning BI questions into source-scoped evidence requests.
- Reviewing data model choices, calculated fields, filters, parameters, extracts, refreshes, permissions, and publishing risk.
- Supporting role bundles that use Tableau for analytics, reporting, finance, marketing, operations, or executive dashboards.

## What This Bundle Is Not

- A complete Tableau Desktop, Tableau Cloud, Tableau Server, Tableau Prep, REST API, pricing, license, connector, or release reference.
- A substitute for BI governance, Tableau administrator, security, privacy, accessibility, legal, or compliance review.
- A claim that the agent has access to the user's Tableau site, workbook, data sources, or dashboards.

## Source Discipline

Use exact Tableau facts only when grounded in official Tableau documentation or user-provided local evidence. Treat the following as local evidence requirements:

- workbook, worksheet, dashboard, story, view, owner, project, site, and environment evidence;
- data source, connection, published data source, live/extract setting, relationship, join, union, blend, schema, field, calculation, parameter, filter, and data-type evidence;
- metric definitions, grain, source-of-record, refresh timing, timezone, row-level security, and data-quality evidence;
- permission, group/user, role, capability, embedded credential, download/export, subscription, alert, and sharing evidence;
- privacy, security, accessibility, retention, compliance, and stakeholder approval evidence.

## Tableau Guardrails

- Treat Tableau Help as a product behavior source category, not proof of a user's local workbook or site configuration.
- Verify workbook and data-source evidence before recommending field names, calculated fields, filters, relationships, joins, unions, extract behavior, or dashboard edits.
- Separate Tableau Desktop authoring evidence from Tableau Cloud or Tableau Server publishing evidence.
- Treat dashboard numbers as hypotheses until metric definitions, filters, grain, source, refresh timing, and permissions are aligned.
- Require explicit confirmation before live publishing, overwriting, deleting, permission changes, credential embedding, exports, refresh changes, subscriptions, alerts, or broad sharing.

## Source Note Template

```text
Source note: Tableau guidance is based on official Tableau source categories for [data connections / data sources / relationships / joins / extracts / publishing / permissions / accessibility]. Local evidence used: [workbook, dashboard, worksheet, data source, field list, calculation, filter, project, permission, extract, refresh, screenshot, or policy evidence provided by user]. Missing before action or conclusion: [current doc/version check, workbook inspection, source-of-record definition, permission review, data classification, accessibility review, owner approval].
```

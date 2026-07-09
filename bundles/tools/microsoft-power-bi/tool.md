---
type: Tool Guide
title: Microsoft Power BI
description: "Defines safe, source-aware use of Microsoft Power BI in OpenKnowledgeBank bundles."
tool_category: "Business intelligence and analytics visualization platform"
okb_bundle_id: microsoft-power-bi
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
  - Plan Power BI reports, dashboards, semantic model reviews, and refresh checks from user-provided evidence.
  - Review metric definitions, source-of-record alignment, report filters, RLS/OLS assumptions, sharing, and publishing risk.
  - Explain Power BI concepts using official Microsoft Learn source categories.
confirmation_required:
  - Publish, overwrite, move, delete, rename, refresh, export, embed, subscribe, or broadly share reports, dashboards, semantic models, apps, dataflows, or workspaces.
  - Change workspace roles, item permissions, RLS/OLS roles, tenant settings, gateway settings, credentials, refresh schedules, subscriptions, alerts, endorsements, sensitivity labels, or app audiences.
  - Access sensitive, confidential, regulated, row-level, user-level, financial, customer, employee, or operational data.
timestamp: "2026-07-09T00:00:00Z"
---

# Microsoft Power BI Tool Guide

Microsoft Power BI is a Microsoft business intelligence and analytics product family used to connect to data, build semantic models, create reports and dashboards, publish content, share insights, govern access, and automate selected operations through APIs.

## What This Bundle Is For

- Planning Power BI reports, dashboards, semantic model reviews, and readiness checks.
- Turning BI questions into source-scoped evidence requests.
- Reviewing metric definitions, visual filters, data lineage, refresh timing, RLS/OLS assumptions, workspace permissions, item permissions, sharing, embedding, exports, and publishing risk.
- Supporting role bundles that use Power BI for analytics, reporting, finance, operations, sales, marketing, supply chain, or executive dashboards.

## What This Bundle Is Not

- A complete Power BI Desktop, Power BI service, Fabric, DAX, Power Query M, REST API, pricing, licensing, connector, capacity, or release reference.
- A substitute for BI governance, Power BI administration, data ownership, security, privacy, accessibility, legal, procurement, or compliance review.
- A claim that the agent has access to the user's Power BI tenant, workspace, semantic model, report, dashboard, app, dataflow, gateway, permissions, refresh history, or API.

## Source Discipline

Use exact Power BI facts only when grounded in official Microsoft documentation or user-provided local evidence. Treat the following as local evidence requirements:

- tenant, workspace, app, report, dashboard, semantic model, dataflow, gateway, capacity, owner, and environment evidence;
- data source, connection, schema, table, field, measure, calculated column, DAX/M expression, relationship, filter, slicer, visual, page, drill-through, lineage, refresh, and data-quality evidence;
- metric definition, source-of-record, grain, aggregation, date/timezone, row-level security, object-level security, and data freshness evidence;
- group/user, workspace role, item permission, app audience, sharing link, export/download, subscription, alert, embed, REST API scope, and admin/tenant setting evidence;
- privacy, security, accessibility, retention, compliance, governance, approval, and rollback evidence.

## Power BI Guardrails

- Treat Microsoft Learn as a product behavior source category, not proof of a user's local tenant configuration.
- Verify semantic model and report evidence before recommending field names, measures, DAX/M expressions, filters, relationships, security roles, refresh behavior, or dashboard edits.
- Separate Power BI Desktop authoring evidence from Power BI service, Fabric, workspace, app, API, gateway, capacity, and tenant evidence.
- Treat dashboard numbers as hypotheses until metric definitions, filters, grain, source, refresh timing, and security context are aligned.
- Treat REST API details as current-source checks because permissions, scopes, service principal behavior, tenant settings, endpoint payloads, and naming can differ by endpoint and environment.
- Require explicit confirmation before live publishing, overwriting, deleting, permission changes, exports, embedding, refresh triggers, schedule changes, gateway or credential changes, subscriptions, alerts, or broad sharing.

## Source Note Template

```text
Source note: Power BI guidance is based on official Microsoft source categories for [Power BI service / semantic models / reports / dashboards / dataflows / refresh / RLS / permissions / REST APIs / admin settings]. Local evidence used: [tenant, workspace, app, report, dashboard, semantic model, field list, measure, DAX/M expression, filter, role, permission, refresh, gateway, screenshot, export, API result, or policy evidence provided by user]. Missing before action or conclusion: [current doc/version check, workspace inspection, model/report inspection, source-of-record definition, permission review, data classification, security review, accessibility review, owner approval].
```

---
type: Reference
title: Microsoft Power BI Source Checks
description: "Source categories and local evidence checks for Power BI report, semantic model, dashboard, refresh, security, sharing, and API work."
okb_bundle_id: microsoft-power-bi
resource:
  - https://learn.microsoft.com/en-us/power-bi/
  - https://learn.microsoft.com/en-us/power-bi/fundamentals/service-basic-concepts
  - https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand
  - https://learn.microsoft.com/en-us/rest/api/power-bi/
  - https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security
  - https://learn.microsoft.com/en-us/power-bi/guidance/rls-guidance
  - https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-data-lineage
  - https://learn.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-introduction-self-service
  - https://learn.microsoft.com/en-us/power-bi/developer/embedded/datasets-permissions
timestamp: "2026-07-09T00:00:00Z"
---

# Microsoft Power BI Source Checks

## Official Source Categories

- Microsoft Learn Power BI documentation for Power BI Desktop, the Power BI service, Microsoft Fabric-related Power BI capabilities, semantic models, reports, dashboards, apps, workspaces, dataflows, refresh, lineage, publishing, sharing, security, and administration.
- Microsoft Learn Power BI REST API documentation for embedding, administration, governance, user resources, endpoint-specific syntax, scopes, service principal behavior, and workspace/group terminology.
- Microsoft product, pricing, licensing, capacity, connector, release note, and admin documentation when current feature availability, commercial terms, tenant settings, limits, or release-specific behavior matters.

## Local Power BI Evidence

Ask the user for the relevant local evidence before final claims:

- tenant, workspace, app, report, dashboard, semantic model, dataflow, gateway, capacity, owner, and environment evidence;
- source system, connection, schema, table, field, measure, calculated column, DAX/M expression, relationship, filter, slicer, visual, page, drill-through, lineage, refresh, and data-quality evidence;
- metric definition, source of record, grain, aggregation, date/timezone, row-level security, object-level security, data freshness, and reconciliation evidence;
- workspace role, item permission, group/user, app audience, sharing link, export/download, subscription, alert, embed, REST API scope, API response, admin setting, and tenant setting evidence;
- privacy, security, accessibility, retention, compliance, governance, approval, and rollback evidence.

## Claims That Need Verification

Do not make authoritative claims about these without current source or local evidence:

- tenant, workspace, report, dashboard, page, visual, semantic model, dataset, dataflow, source system, gateway, capacity, owner, field, measure, DAX/M expression, relationship, filter, slicer, refresh, or schedule names;
- whether a measure, relationship, filter, visual, report page, RLS/OLS role, or source query preserves the intended grain and metric definition;
- dashboard numbers, variance explanations, conversion rates, financial figures, forecasts, executive KPIs, operational KPIs, or security-filtered totals;
- workspace role, item permission, app audience, group/user, sharing link, export/download, embed, subscription, alert, gateway, credential, sensitivity label, endorsement, or tenant setting behavior;
- REST API endpoint syntax, scopes, payloads, response fields, service principal behavior, admin prerequisites, capacity/licensing requirements, connector availability, pricing, limits, release-specific behavior, or feature availability.

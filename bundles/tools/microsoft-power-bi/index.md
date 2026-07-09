---
type: Bundle Index
title: Microsoft Power BI
description: "Tool bundle for source-aware Power BI report, dashboard, semantic model, refresh, security, sharing, and REST API planning."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - microsoft-power-bi
  - power-bi
  - business-intelligence
  - dashboards
  - analytics
  - data-visualization
aliases:
  - Power BI
  - Microsoft Power BI Desktop
  - Power BI service
  - Microsoft Fabric Power BI
problems_solved:
  - Plan Power BI reports and dashboards without inventing workspaces, semantic models, fields, measures, filters, or permissions.
  - Separate official Microsoft Learn product and API behavior from user-provided tenant, workspace, semantic model, and report evidence.
  - Review refresh, lineage, RLS, sharing, export, embedding, and publishing decisions with explicit confirmation boundaries.
  - Produce Power BI readiness plans that include source notes, metric validation, security review, and governance checks.
industries:
  - analytics
  - data
  - business-intelligence
  - finance
  - operations
  - sales
  - marketing
tools:
  - Microsoft Power BI
  - Power BI Desktop
  - Power BI service
  - Microsoft Fabric
  - Power BI REST APIs
frameworks:
  - verify-first BI planning
  - semantic model evidence check
  - source-of-record reconciliation
  - publishing and permissions confirmation boundary
deliverables:
  - Power BI report readiness plan
commands:
  - /plan-power-bi-report
skills: []
evaluations:
  - Power BI report plan quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - google-bigquery
  - tableau
adjacent_bundles:
  - ga4-analytics-specialist
  - performance-marketer
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Not a complete Power BI Desktop, Power BI service, Microsoft Fabric, DAX, Power Query M, REST API, pricing, licensing, connector, capacity, tenant administration, or release reference."
  - "Requires user-provided tenant, workspace, semantic model, report, dashboard, dataflow, field, measure, filter, RLS/OLS, refresh, lineage, gateway, capacity, permission, and governance evidence before final conclusions."
  - "Does not replace Power BI administrator, BI governance, data owner, security, privacy, accessibility, legal, procurement, or compliance review."
safety_notes:
  - "Require explicit confirmation before publishing, overwriting, deleting, exporting, embedding, sharing, changing permissions, triggering refreshes, changing schedules, changing gateway/credential settings, or broadening access."
  - "Do not claim access to Power BI tenants, workspaces, semantic models, reports, dashboards, dataflows, permissions, refresh history, or APIs unless the user provides evidence or authorized tool access."
evaluation_summary:
  status: blocked
  last_evaluated: "2026-07-09"
  method: baseline-vs-okb-rubric
  tasks_count: 0
  display_summary: "Measured evaluation is blocked until a Power BI task set, model/provider configuration, and reviewer are selected."
  evidence_note: "No raw prompts or outputs are included in the public bundle."
evaluation_detail:
  status: blocked
  title: "Microsoft Power BI planned evaluation"
  method: baseline-vs-okb-rubric
  next_step: "Create public-safe Power BI benchmark tasks and run the generic evaluation harness."
okb_bundle_id: microsoft-power-bi
timestamp: "2026-07-09T00:00:00Z"
---

# Microsoft Power BI

This bundle helps an agent use Microsoft Power BI as a source-aware analytics and business intelligence tool. It is designed for report planning, dashboard readiness review, semantic model evidence checks, metric reconciliation, refresh and lineage review, publishing preparation, permissions review, and REST API planning boundaries.

It is a companion tool bundle, not a replacement for analytics, BI developer, Power BI administrator, data visualization, finance, operations, sales, marketing, or executive role bundles.

## Required Answer Habit

For source-sensitive Power BI work, include a short **Source note** naming the official Microsoft source category, the user-provided tenant/workspace/model/report evidence used, and missing evidence required before acting or treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-power-bi-report.md](commands/plan-power-bi-report.md)
- [workflows/plan-power-bi-report.md](workflows/plan-power-bi-report.md)
- [workflows/review-power-bi-publishing-permissions.md](workflows/review-power-bi-publishing-permissions.md)
- [deliverables/power-bi-report-readiness-plan.md](deliverables/power-bi-report-readiness-plan.md)
- [evaluations/power-bi-report-plan-quality-check.md](evaluations/power-bi-report-plan-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current Microsoft Learn Power BI, Microsoft Fabric, Power BI service, semantic model, dataflow, security, REST API, admin, and product documentation for product behavior. Use user-provided tenant, workspace, semantic model, report, dashboard, app, permission, refresh, lineage, gateway, capacity, data source, field, measure, and governance evidence for local conclusions. Do not invent workspace names, model names, report pages, dashboards, fields, measures, DAX/M expressions, relationships, filters, roles, permissions, refresh schedules, API scopes, endpoint payloads, pricing, licensing, capacities, or tenant settings.

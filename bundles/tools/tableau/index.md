---
type: Bundle Index
title: Tableau
description: "Tool bundle for source-aware Tableau dashboard, workbook, data source, publishing, and permissions planning."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - tableau
  - business-intelligence
  - dashboards
  - analytics
  - data-visualization
aliases:
  - Salesforce Tableau
  - Tableau Desktop
  - Tableau Cloud
  - Tableau Server
problems_solved:
  - Plan Tableau dashboards and workbooks without inventing fields, calculations, filters, or access.
  - Separate official Tableau product behavior from user-provided workbook, site, and data-source evidence.
  - Review publishing, permissions, embedded credentials, extracts, refreshes, and sharing with explicit confirmation boundaries.
  - Produce dashboard readiness plans that include source notes, validation, accessibility, and governance checks.
industries:
  - analytics
  - data
  - business-intelligence
  - marketing
  - finance
tools:
  - Tableau
  - Tableau Desktop
  - Tableau Cloud
  - Tableau Server
  - Tableau Prep Builder
frameworks:
  - verify-first BI planning
  - source-of-record reconciliation
  - dashboard readiness review
  - publishing and permissions confirmation boundary
deliverables:
  - Tableau dashboard readiness plan
commands:
  - /plan-tableau-dashboard
skills: []
evaluations:
  - Tableau dashboard plan quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - google-bigquery
adjacent_bundles:
  - funnel-analysis
  - ga4-analysis-brief
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
  - "Not a complete Tableau Desktop, Tableau Cloud, Tableau Server, Tableau Prep, REST API, pricing, license, connector, or release reference."
  - "Requires user-provided workbook, data source, field, calculation, extract, refresh, permission, site, and governance evidence before final conclusions."
  - "Does not replace Tableau administrator, BI governance, security, privacy, accessibility, legal, or compliance review."
safety_notes:
  - "Require explicit confirmation before publishing, overwriting, deleting, changing permissions, embedding credentials, exporting/downloading data, running refreshes, changing schedules, or broadening sharing."
  - "Do not claim access to Tableau sites, workbooks, data sources, dashboards, fields, permissions, extracts, or refresh schedules unless the user provides evidence or authorized tool access."
evaluation_summary:
  status: blocked
  last_evaluated: "2026-07-09"
  method: baseline-vs-okb-rubric
  tasks_count: 0
  display_summary: "Measured evaluation is blocked until a Tableau task set and model/provider configuration are selected."
  evidence_note: "No raw prompts or outputs are included in the public bundle."
okb_bundle_id: tableau
timestamp: "2026-07-09T00:00:00Z"
---

# Tableau

This bundle helps an agent use Tableau as a source-aware analytics, dashboarding, and business intelligence tool. It is designed for workbook planning, dashboard readiness review, data-source evidence checks, publishing preparation, permissions review, and governed analytics support.

It is a companion tool bundle, not a replacement for analytics, BI developer, Tableau administrator, data visualization, finance, marketing, or operations role bundles.

## Required Answer Habit

For source-sensitive Tableau work, include a short **Source note** naming the official Tableau source category, the user-provided workbook/site/data-source evidence used, and missing evidence required before acting or treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-tableau-dashboard.md](commands/plan-tableau-dashboard.md)
- [workflows/plan-tableau-dashboard.md](workflows/plan-tableau-dashboard.md)
- [workflows/review-tableau-publishing-permissions.md](workflows/review-tableau-publishing-permissions.md)
- [deliverables/tableau-dashboard-readiness-plan.md](deliverables/tableau-dashboard-readiness-plan.md)
- [evaluations/tableau-dashboard-plan-quality-check.md](evaluations/tableau-dashboard-plan-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current Tableau Help and Salesforce Tableau product documentation for product behavior, plus user-provided Tableau workbook, site, project, data source, permission, and governance evidence. Do not invent workbook names, field names, calculated fields, parameters, filters, joins, relationships, extract settings, refresh schedules, projects, groups, permissions, credentials, dashboard numbers, or publishing behavior.

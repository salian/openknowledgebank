---
type: Deliverable
title: Power BI Report Readiness Plan
description: "Output format for planning or reviewing a Power BI report, dashboard, semantic model, refresh, and sharing workflow."
okb_bundle_id: microsoft-power-bi
required_inputs:
  - business question and audience
  - Power BI workspace/report/dashboard/semantic model evidence
  - metric, source, field, measure, filter, refresh, security, and permission evidence
outputs:
  - readiness decision
  - source note
  - evidence matrix
  - report and semantic model plan
  - validation and confirmation checklist
quality_criteria:
  - distinguishes official source facts, user-provided evidence, assumptions, and missing verification
  - avoids invented tenant, model, field, measure, report, dashboard, permission, or API details
  - requires confirmation for risky actions
timestamp: "2026-07-09T00:00:00Z"
---

# Power BI Report Readiness Plan

## Required Sections

1. **Readiness decision**: ready, ready with assumptions, blocked pending evidence, or not recommended.
2. **Source note**: official Microsoft source categories, local evidence used, and missing verification.
3. **Evidence matrix**: verified source facts, user-provided Power BI evidence, assumptions for this draft, and needs-verification items.
4. **Report/dashboard plan**: audience, decisions, pages, visuals, metrics, dimensions, filters, interactions, accessibility checks, cadence, and owners.
5. **Semantic model and source plan**: source of record, tables/files, fields, measures, DAX/M expressions, relationships, grain, date/timezone, data quality, lineage, and validation checks.
6. **Refresh and operational plan**: refresh schedule, refresh history, gateway, credential dependencies, failures, capacity constraints, and owner checks.
7. **Security and sharing plan**: workspace roles, item permissions, app audiences, sharing links, export/download, embed, RLS/OLS, subscriptions, alerts, data classification, and approval needs.
8. **Reconciliation and QA**: comparison reports, source totals, filters, grain, aggregation, security context, expected differences, unresolved discrepancies, and sign-off.
9. **Confirmation boundary**: actions that require explicit user confirmation and authorized access.

## Quality Bar

A strong plan gives a useful answer while refusing to invent local Power BI facts. It names the exact evidence needed before final claims and gives a practical next step for each missing item.

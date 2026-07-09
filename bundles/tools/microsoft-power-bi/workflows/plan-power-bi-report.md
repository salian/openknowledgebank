---
type: Workflow
title: Plan Power BI Report
description: "Evidence-first workflow for planning a Power BI report or dashboard."
okb_bundle_id: microsoft-power-bi
timestamp: "2026-07-09T00:00:00Z"
---

# Plan Power BI Report

Use this workflow when a user asks for a Power BI report, dashboard, semantic model, or KPI planning answer.

## Steps

1. Define the decision, audience, cadence, and required action.
2. Identify the source of record, metric definitions, grain, filters, time period, timezone, and reconciliation expectations.
3. Ask for or inspect authorized Power BI evidence: workspace, app, report, dashboard, semantic model, dataflow, field list, measures, DAX/M expressions, relationships, filters, visuals, refresh, lineage, and owner evidence.
4. Separate verified source facts, user-provided local evidence, assumptions for the draft, and missing verification.
5. Draft report pages, visuals, metric cards, dimensions, filters, drill paths, accessibility checks, and validation tests only to the level supported by evidence.
6. Review refresh timing, gateway/credential dependencies, data lineage, RLS/OLS, workspace roles, item permissions, app audience, sharing, export, embedding, subscriptions, and alerts.
7. State the confirmation boundary for any publishing, refresh, export, permission, gateway, credential, subscription, alert, or sharing action.

## Required Output

Include:

- direct answer about readiness;
- Source note;
- evidence table with verified, provided, assumed, and missing items;
- report/dashboard plan;
- semantic model and metric validation plan;
- refresh, lineage, security, sharing, and governance review;
- explicit confirmation boundary.

## Reconciliation Rule

When two Power BI numbers differ, do not choose a winner until definitions, source, filters, grain, refresh timing, security context, report visual logic, DAX/M logic, and aggregation are aligned. State expected differences separately from unresolved discrepancies.

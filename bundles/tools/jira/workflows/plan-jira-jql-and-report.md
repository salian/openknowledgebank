---
type: Workflow
title: Plan Jira JQL and Report
description: "Query-shape and source-check workflow for Jira JQL, reports, dashboards, and API-backed analysis."
okb_bundle_id: jira
timestamp: "2026-07-09T00:00:00Z"
---

# Plan Jira JQL and Report

Use this workflow when a user asks for a Jira query, dashboard/report interpretation, API-backed issue/work-item extraction, or reconciliation between Jira values.

## Evidence to Request

- The exact question, output grain, time window, project/space, board/filter, sprint/version, work item type, and target fields.
- JQL field/function availability, including custom fields and app-provided functions.
- Report settings, dashboard filters, board columns, status and resolution logic, permissions, and export/API method.
- The source of every comparison value: board UI, report, dashboard, JQL result, export, API response, or another tool.

## Planning Steps

1. Define what each requested metric or count actually measures.
2. Map every requested dimension, metric, filter, source, grain, and output row to a query/report/API plan or explicitly defer unsupported pieces.
3. Verify official source categories for JQL/report/API behavior and local evidence for fields, functions, filters, permissions, and app behavior.
4. Include time/version/effective-date logic, status/resolution logic, entity identity, deduplication, and aggregation.
5. Plan a read-only validation step against a trusted Jira source of record or independent export.

## Reconciliation Pattern

When Jira board, report, JQL, export, or API values differ, neither value is automatically right. Explain what each value measures, request the exact settings behind each, and separate expected differences from unresolved discrepancies.

## Output Requirements

- Include a Source note.
- Include a query-shape self-check.
- Distinguish verified source facts, user-provided local evidence, assumptions, and needs-verification.
- Require confirmation before exports, API calls that retrieve sensitive data, notifications, comments, automation changes, or writes.

---
type: Workflow
title: Reconcile GA4 UI and BigQuery
description: Workflow for reconciling GA4 standard reporting values with BigQuery export-derived values.
tags:
  - workflow
  - reconciliation
  - bigquery
inputs:
  - GA4 UI settings
  - metric
  - date range
  - BigQuery SQL or query logic
outputs:
  - reconciliation note
  - aligned check plan
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# Reconcile GA4 UI and BigQuery

## First Answer

Start with: neither value is automatically right until the GA4 metric/report settings and BigQuery query logic are aligned.

## Required Checks

- GA4 surface: standard report, Explore, Data API, Looker Studio, or exported table.
- Metric name and definition.
- Date range, timezone, filters, comparisons, segments, reporting identity, and data quality notices.
- BigQuery dataset/table prefix, table suffixes, daily versus intraday tables, late-arriving data.
- Date logic: `event_date`, `event_timestamp`, property timezone, UTC, and local-date conversion.
- User/session/event logic: `user_pseudo_id`, `user_id`, `is_active_user`, session construction, event filters, parameters, and deduplication.
- Expected differences versus unresolved discrepancies.

## Source Note

Name GA4 metric documentation, GA4 BigQuery export schema, and the user's local report/SQL/evidence when provided.

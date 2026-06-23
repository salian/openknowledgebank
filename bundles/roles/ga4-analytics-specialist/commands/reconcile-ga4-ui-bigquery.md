---
type: Slash Command
command: /reconcile-ga4-ui-bigquery
title: Reconcile GA4 UI and BigQuery
description: Explain and reconcile differences between GA4 UI values and BigQuery query results.
inputs:
  - GA4 UI number
  - BigQuery number
  - date range
  - metric
  - SQL or query logic if available
outputs:
  - reconciliation note
  - input request
  - source note
requires_confirmation: false
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# /reconcile-ga4-ui-bigquery

Use when the user asks which GA4 number is right or why GA4 UI and BigQuery disagree.

## First Sentence Rule

Say: neither number is automatically right until the GA4 metric/report settings and BigQuery query logic are aligned.

## Final Answer Must Include

1. Direct answer.
2. GA4 UI definition and settings needed.
3. BigQuery query definition and settings needed.
4. Table/date alignment: dataset/table prefix, `_TABLE_SUFFIX`, daily/intraday tables, late-arriving data, `event_date`, `event_timestamp`, timezone, local-date conversion.
5. User/session/event logic: active users, total users, `user_pseudo_id`, `user_id`, `is_active_user`, sessions, event filters, parameters, deduplication.
6. Expected differences.
7. Unresolved discrepancies.
8. Next aligned check.
9. Source note.

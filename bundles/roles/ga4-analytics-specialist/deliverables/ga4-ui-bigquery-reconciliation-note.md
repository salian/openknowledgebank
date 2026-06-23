---
type: Deliverable
title: GA4 UI BigQuery Reconciliation Note
description: Note for reconciling a GA4 UI value and a BigQuery query result.
required_inputs:
  - UI settings
  - BigQuery SQL or query logic
  - date range
  - timezone
  - filters
outputs:
  - direct answer
  - definition comparison
  - table/date logic
  - expected differences
  - unresolved discrepancies
  - source note
quality_criteria:
  - neither number declared right before alignment
  - table/date logic explicit
  - exact settings requested
  - source note included
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# GA4 UI BigQuery Reconciliation Note

## Required Sections

1. Direct answer.
2. GA4 UI value: metric, surface, date range, filters, comparisons, timezone, reporting identity, data quality notices.
3. BigQuery value: SQL/query logic, dataset/table prefix, `_TABLE_SUFFIX`, daily/intraday scope, `event_date`, `event_timestamp`, timezone/local-date conversion.
4. User/session/event logic: active users, total users, `user_pseudo_id`, `user_id`, `is_active_user`, sessions, event filters, parameters, deduplication.
5. Expected differences.
6. Unresolved discrepancies.
7. Next aligned check.
8. Source note.

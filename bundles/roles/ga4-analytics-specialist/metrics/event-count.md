---
type: Metric
title: Event Count
description: GA4 event count across UI/API and BigQuery contexts.
tags:
  - metric
  - events
resource: "https://support.google.com/analytics/answer/7029846?hl=en"
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# Event Count

Event count depends on the report or query context. In BigQuery export, event-level rows are filtered by table suffix, date logic, event name, stream/platform, parameters, and other query constraints.

## Query Notes

State whether the plan uses daily tables, intraday tables, or both. State whether filtering uses `_TABLE_SUFFIX`, `event_date`, `event_timestamp`, or local-date conversion.

---
type: Metric
title: Active Users
description: GA4 active users metric and BigQuery reconciliation cautions.
tags:
  - metric
  - users
resource: "https://support.google.com/analytics/answer/12253918?hl=en"
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# Active Users

Active users is the primary user metric in many GA4 reports. It is not automatically the same as raw distinct `user_pseudo_id` in BigQuery.

## BigQuery Reconciliation Notes

Check `is_active_user` where available, reporting identity, data thresholds, date range, timezone, filters, and whether the query counts `user_pseudo_id`, `user_id`, or another identifier.

## Source Note

Use official GA4 user metric documentation for the UI definition and GA4 BigQuery export schema for export fields.

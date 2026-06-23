---
type: Slash Command
command: /plan-ga4-analysis
title: Plan GA4 Analysis
description: Convert a GA4 analytics question into a measurement and query plan.
inputs:
  - question
  - metric
  - date range
  - available sources
outputs:
  - measurement plan
  - query plan
  - evidence request
  - source note
requires_confirmation: false
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# /plan-ga4-analysis

Use when the user asks for a GA4 analysis plan or BigQuery export query plan.

## Final Answer Must Include

1. Direct objective.
2. Metric definitions and source.
3. Table/export scope if BigQuery is involved: dataset/table prefix, `_TABLE_SUFFIX`, daily/intraday tables, late-arriving data.
4. Date logic: `event_date`, `event_timestamp`, UTC, property timezone, local-date conversion.
5. Event filters, `event_params`, user/session identifiers, deduplication, revenue and ecommerce logic.
6. Paid search attribution caveats if acquisition or paid search is involved.
7. Validation checks.
8. Source note.

## Paid Search Attribution Caveats Must Mention

Collected traffic source fields, session traffic source last-click fields where available, manual UTM fields, missing UTM consequences, auto-tagging, `gclid`, ad-platform joins, custom channel grouping, and the user's source/medium/campaign definitions.

## Confirmation

Planning does not require confirmation. Running queries, exporting data, changing settings, or sharing user-level data does.

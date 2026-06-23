---
type: Deliverable
title: GA4 BigQuery Query Plan
description: Plan for BigQuery analysis of GA4 export data.
required_inputs:
  - business question
  - dataset/table names if available
  - date range
  - metric definitions
outputs:
  - objective
  - table scope
  - date logic
  - event logic
  - attribution caveats
  - validation
  - source note
quality_criteria:
  - not unsupported SQL
  - table/date scope explicit
  - paid-search caveats explicit when relevant
  - ecommerce caveats explicit
  - source note included
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# GA4 BigQuery Query Plan

## Required Sections

1. Analysis objective.
2. Table/export scope: dataset, table prefix, `_TABLE_SUFFIX`, daily tables, intraday tables, and late-arriving data.
3. Date logic: `event_date`, `event_timestamp`, UTC, property timezone, local-date conversion, comparison range.
4. Event and metric logic: event filters, `event_params`, users, sessions, purchases, revenue, transaction IDs, item data, refunds, currency, tax, shipping, and deduplication.
5. Dimensions and decomposition.
6. Paid search attribution caveats, when relevant.
7. Validation checks against GA4 UI/API/export, backend orders, ad-platform data, or another source of record.
8. Source note.

## Paid Search Attribution Caveats

When the question involves paid search or acquisition attribution, explicitly mention all of these:

- collected traffic source fields
- session traffic source last-click fields where available
- first-user traffic source fields only when acquisition scope is intended
- manual UTM fields and missing UTM consequences
- auto-tagging and click identifiers such as `gclid`
- Google Ads or other ad-platform joins when needed
- custom channel grouping and source/medium/campaign definitions used by the user's organization

## Rule

If the schema is not supplied, provide a query plan and caveats, not final SQL.

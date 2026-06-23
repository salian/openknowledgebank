---
type: Tool Guide
title: BigQuery
description: Safe-use guide for GA4 BigQuery export planning and query review.
tool_category: data-warehouse
resource: "https://support.google.com/analytics/answer/7029846?hl=en"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - review user-provided SQL
  - draft query plans
  - explain export caveats
confirmation_required:
  - run expensive queries
  - export data
  - create or alter datasets
  - share user-level results
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# BigQuery

Use BigQuery for reproducible event-level analysis, custom decomposition, reconciliation, and implementation checks.

## Query Planning Requirements

- Dataset and table prefix.
- `_TABLE_SUFFIX` range.
- Daily tables, intraday tables, and late-arriving data handling.
- `event_date`, `event_timestamp`, UTC, property timezone, and local-date conversion.
- Event filters and `event_params` extraction.
- `user_pseudo_id`, `user_id`, `is_active_user`, session identifier, and deduplication logic.
- Ecommerce fields: purchase revenue, refunds, transaction ID, items, item revenue, currency, tax, and shipping.
- Traffic source fields: collected traffic source, session traffic source last click, first-user traffic source, manual UTMs, `gclid`, ad-platform joins, and custom channel grouping.

## Confirmation Required

Get confirmation before running costly queries, exporting data, sharing user-level rows, or changing datasets.

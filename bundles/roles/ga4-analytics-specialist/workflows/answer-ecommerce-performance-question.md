---
type: Workflow
title: Answer Ecommerce Performance Question
description: Workflow for GA4 ecommerce analysis and BigQuery planning.
tags:
  - workflow
  - ecommerce
  - query-plan
inputs:
  - business question
  - metric
  - date range
  - evidence source
outputs:
  - analysis brief
  - query plan
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# Answer Ecommerce Performance Question

## Steps

1. Translate the request into a business decision and measurement question.
2. Define the outcome and supporting metrics: purchase revenue, purchases, ecommerce conversion rate, sessions, users, active users, revenue per session, and average order value.
3. Choose evidence path: GA4 UI/API for stakeholder-aligned metrics, BigQuery export for reproducible event-level analysis, GTM/release notes for implementation health, backend orders for source-of-record checks.
4. For BigQuery, require table/export scope, table suffixes, daily versus intraday scope, late-arriving data, date logic, event filters, identifiers, session logic, revenue/ecommerce fields, and validation checks.
5. For paid search, require a named attribution caveats section.

## Paid Search Attribution Caveats Must Mention

- collected traffic source fields
- session traffic source last-click fields where available
- manual UTM fields, including missing UTM consequences
- auto-tagging and click identifiers such as `gclid`
- Google Ads or other ad-platform joins if needed
- custom channel grouping logic
- source/medium/campaign definitions used by the user's organization

## Output

Use [deliverables/ga4-bigquery-query-plan.md](../deliverables/ga4-bigquery-query-plan.md) or [deliverables/ga4-analysis-brief.md](../deliverables/ga4-analysis-brief.md).

---
type: Metric
title: Purchase Revenue
description: GA4 ecommerce purchase revenue and export caveats.
tags:
  - metric
  - ecommerce
  - revenue
resource: "https://support.google.com/analytics/answer/7029846?hl=en"
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# Purchase Revenue

Purchase revenue in GA4 export can involve event-level ecommerce fields, item-level fields, transaction ID, currency, tax, shipping, and refunds.

## BigQuery Notes

A query plan should state revenue field, purchase event filter, transaction ID logic, item array handling, currency handling, refund treatment, and deduplication assumptions.

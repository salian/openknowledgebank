---
type: Workflow
title: Reconcile Sources
description: Explains differences between BigQuery, SEDE, API, live site/search, and user exports.
tags: [workflow, reconciliation]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Reconcile Sources

## Direct Answer Pattern

Neither number is automatically right until source definitions, freshness, filters, tag logic, deleted/private content handling, and query method are aligned.

## Steps

1. Name each source.
2. Define what each number measures.
3. Request exact SQL/API parameters/search query/report settings and run time.
4. Compare freshness and inclusion rules.
5. Compare tag logic, date logic, post type, deleted/private handling, and aggregation.
6. Separate expected differences from unresolved discrepancies.
7. Recommend the source that fits the user's decision.

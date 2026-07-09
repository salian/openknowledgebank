---
type: Workflow
title: Product Metric Review
description: Interprets product metrics and reconciles conflicting sources before decisions.
tags: [metrics, analytics, source-discipline]
okb_bundle_id: senior-product-manager
timestamp: 2026-07-09T00:00:00Z
---

# Product Metric Review

Use this workflow when metrics inform strategy, prioritization, launch, or roadmap decisions.

## Inputs

- Metric name, decision context, time period, segment, and source system.
- Definition, numerator, denominator, filters, identity logic, aggregation, deduplication, and refresh cadence.
- Comparison source when there is a discrepancy.
- Known instrumentation, data-quality, or reporting changes.

## Output Contract

- Direct answer stating whether the metric supports a decision, is inconclusive, or needs reconciliation first.
- Definition and scope of each value being compared.
- Expected differences versus unresolved discrepancies.
- Checks needed before treating the metric as decision-grade.
- Source note naming dashboards, warehouse queries, analytics tools, exports, or missing evidence.

Do not decide which number is right merely because one tool is more familiar. Reconcile definitions, inputs, settings, and methods first.

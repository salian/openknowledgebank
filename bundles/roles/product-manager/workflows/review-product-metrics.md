---
type: Workflow
title: Review Product Metrics
description: Interpret product metrics with source discipline and no invented definitions.
tags: [metrics, analytics, product-review]
okb_bundle_id: product-manager
timestamp: 2026-07-09T00:00:00Z
---

# Review Product Metrics

Use this workflow to review product performance, adoption, retention, activation, conversion, satisfaction, reliability, or experiment metrics.

## Inputs

- Metric names and source reports.
- Time period, segment, cohort, filters, and grain.
- Metric glossary or owner-provided definitions.
- Instrumentation changes, release dates, campaigns, incidents, and seasonality.
- Decision that the metric review should support.

## Steps

1. State what decision the metric review should inform.
2. Define each metric from the source of record or mark it as unverified.
3. Check time period, segment, cohort, filters, grain, attribution, deduplication, and instrumentation changes.
4. Separate observed facts from interpretation.
5. Identify likely explanations, required follow-up, and risks.
6. Recommend next analysis or product action only within the evidence limits.

## Output Contract

The final output should include: direct interpretation, metric definitions, source scope, period, segments, observed changes, likely explanations, unresolved discrepancies, recommended next checks, action recommendation if supported, and `Source note`.

If two reports disagree, neither is automatically correct. Align definitions, filters, time zones, identity logic, attribution, processing delays, and source ownership before choosing a number.

## Related

- [Metrics](../metrics/index.md)

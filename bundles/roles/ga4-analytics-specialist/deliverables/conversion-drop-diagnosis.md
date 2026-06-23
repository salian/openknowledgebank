---
type: Deliverable
title: Conversion Drop Diagnosis
description: "Diagnosis memo for a GA4 purchase, revenue, or conversion drop."
required_inputs:
  - metric
  - date range
  - comparison range
  - reports or query outputs
outputs:
  - direct answer
  - metric frame
  - hypothesis table
  - measurement checks
  - source note
quality_criteria:
  - no unsupported cause claim
  - measurement checks before conclusions
  - ranked hypotheses
  - source note included
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# Conversion Drop Diagnosis

## Required Sections

1. Direct answer: what can and cannot be concluded now.
2. Metric frame: metric, source, date range, comparison range, timezone, filters.
3. Evidence available and missing.
4. Decomposition: traffic volume, conversion efficiency, order value, product/channel/device mix.
5. Measurement checks: GA4 settings, BigQuery query logic, GTM/release history, consent, ecommerce event health, backend order check.
6. Hypothesis table.
7. Immediate next actions.
8. Source note.

## Must Avoid

Do not name a cause from a drop percentage alone. Do not ignore implementation changes or backend-order reconciliation.

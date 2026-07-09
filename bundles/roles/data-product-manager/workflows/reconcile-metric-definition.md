---
type: Workflow
title: Reconcile Metric Definition
description: Aligns conflicting metric values or definitions before recommending a source of record.
tags: [metrics, reconciliation, semantic-layer]
okb_bundle_id: data-product-manager
timestamp: 2026-07-09T00:00:00Z
---

# Reconcile Metric Definition

Use this workflow when two tools, dashboards, queries, reports, teams, or contracts disagree about a metric.

## Inputs

- Metric names, reported values, and sources.
- Definitions, queries, semantic-layer entries, dashboard settings, filters, time windows, refresh cadence, and owners.
- Entity grain, identity logic, deduplication, aggregation, exclusions, and transformation evidence.
- Source-of-record policy or owner decision, if available.

## Steps

1. State that neither value is automatically right until definitions, inputs, settings, and methods are aligned.
2. Define what each value measures and what evidence supports it.
3. Compare source scope, grain, filters, time window, refresh, identity logic, aggregation, exclusions, and transformations.
4. Identify expected differences versus unresolved discrepancies.
5. Recommend a source-of-record decision or list the exact evidence still needed.

## Output Contract

- Direct answer: which value to use now, or why no value should be treated as authoritative yet.
- Source note.
- Side-by-side definition comparison.
- Verified facts, user-provided evidence, assumptions, and missing verification.
- Expected differences, unresolved discrepancies, and validation step.
- Owner decision required before publishing or operationalizing the definition.

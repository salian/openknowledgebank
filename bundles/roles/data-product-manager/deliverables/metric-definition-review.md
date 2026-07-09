---
type: Deliverable
title: Metric Definition Review
description: Source-aware review for conflicting or incomplete metric definitions.
okb_bundle_id: data-product-manager
required_inputs: [metric names, values, definitions, queries, filters, time windows, owners]
outputs: [definition comparison, recommended source of record, unresolved discrepancies]
quality_criteria: [direct answer, aligned grain, source-aware, validates assumptions]
timestamp: 2026-07-09T00:00:00Z
---

# Metric Definition Review

## Required Sections

- Direct answer: use this value now, or do not treat either value as authoritative yet.
- Source note.
- Side-by-side definitions and values.
- Source scope, grain, entity logic, filters, time windows, refresh, deduplication, aggregation, exclusions, and transformations.
- Verified facts, user-provided evidence, assumptions, and missing verification.
- Expected differences and unresolved discrepancies.
- Validation step and owner decision needed before publication.

## Quality Bar

The review must explain what each value actually measures. It should not choose a number based on recency, tool familiarity, or apparent precision alone.

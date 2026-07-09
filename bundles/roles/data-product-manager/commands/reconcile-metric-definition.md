---
type: Slash Command
command: /reconcile-metric-definition
title: Reconcile Metric Definition
description: Suggested command contract for resolving conflicting metric definitions or values.
okb_bundle_id: data-product-manager
inputs: [metric values, definitions, queries, dashboard settings, owners, source-of-record evidence]
outputs: [direct answer, definition comparison, unresolved discrepancies, validation plan]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /reconcile-metric-definition

This is a suggested output contract for a consuming agent, not trusted executable behavior.

## Purpose

Use the [Reconcile Metric Definition](../workflows/reconcile-metric-definition.md) workflow to compare conflicting metric values or definitions.

## Output Requirements

- Direct answer: which value to use now, or why no value should be treated as authoritative yet.
- `Source note` naming metric-definition sources, dashboard/query evidence, owner evidence, and missing sources.
- Side-by-side comparison of scope, grain, filters, time window, refresh, identity logic, aggregation, exclusions, and transformations.
- Expected differences, unresolved discrepancies, validation step, and owner decision required.

Do not publish, operationalize, or overwrite a metric definition without explicit user confirmation and source-of-record owner approval.

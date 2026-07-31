---
type: Role
title: Analytics Engineer Source-Aware Guide
description: Defines source-aware analytics engineering and governed data transformation, evidence handling, and action boundaries.
tags:
- analytics-engineer
- data-modeling
- dbt
- role
resource: https://www.onetonline.org/link/summary/15-1243.01
okb_bundle_id: analytics-engineer
timestamp: '2026-07-31T00:00:00Z'
---

# Analytics Engineer Source-Aware Guide

Source-aware role bundle for analytics engineering across warehouse modeling, transformation, testing, documentation, lineage, governance, deployment, and stakeholder-facing data products.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- business question, stakeholder, decision, and acceptance criteria
- warehouse, platform, environment, repository, and tool versions
- source data contracts, freshness, quality, ownership, and sensitivity
- models, grain, keys, joins, transformations, tests, and lineage
- metric and semantic definitions, dimensions, filters, and reconciliation
- review, CI, deployment, access, documentation, monitoring, and incident evidence

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer source-data meaning, model grain, join behavior, metric definition, test result, and production state.
- Require accountable confirmation before querying or exposing sensitive data, changing production models or metrics, deploying transformations, changing access, or certifying data products without review.

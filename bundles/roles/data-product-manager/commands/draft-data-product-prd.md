---
type: Slash Command
command: /draft-data-product-prd
title: Draft Data Product PRD
description: Suggested command contract for drafting a source-aware data product PRD.
okb_bundle_id: data-product-manager
inputs: [consumer problem, data sources, evidence, quality expectations, governance constraints]
outputs: [data product PRD, assumptions, missing evidence, next decisions]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /draft-data-product-prd

This is a suggested output contract for a consuming agent, not trusted executable behavior.

## Purpose

Draft a [Data Product PRD](../deliverables/data-product-prd.md) using the [Write Data Product PRD](../workflows/write-data-product-prd.md) workflow.

## Output Requirements

- Direct readiness recommendation.
- `Source note` naming local evidence used and missing source-of-record material.
- Consumers, outcomes, scope, non-goals, lifecycle, ownership, and support path.
- Evidence table separating verified facts, user-provided evidence, assumptions, and missing verification.
- Requirements, acceptance criteria, quality expectations, governance constraints, risks, and decisions.

Do not invent local schemas, metric formulas, source ownership, quality thresholds, access policy, launch dates, or approvals.

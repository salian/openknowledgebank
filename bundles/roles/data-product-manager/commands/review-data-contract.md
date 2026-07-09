---
type: Slash Command
command: /review-data-contract
title: Review Data Contract
description: Suggested command contract for reviewing a data contract.
okb_bundle_id: data-product-manager
inputs: [contract draft, schema evidence, producer, consumer, quality rules, governance constraints]
outputs: [readiness status, contract gaps, risk list, required confirmations]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /review-data-contract

This is a suggested output contract for a consuming agent, not trusted executable behavior.

## Purpose

Review a data contract with the [Review Data Contract](../workflows/review-data-contract.md) workflow.

## Output Requirements

- Direct readiness status.
- `Source note` naming contract evidence, schema evidence, owner evidence, and missing sources.
- Producer, consumer, owner, source of record, scope, quality, freshness, lineage, access, privacy, retention, and change policy.
- Verified facts, user-provided evidence, assumptions, and missing verification.
- Required changes and owner confirmations.

Do not approve a contract, change a schema, or modify a live artifact without explicit user confirmation and owner review.

---
type: Workflow
title: Review Data Contract
description: Reviews a data contract for consumer value, producer feasibility, governance, and safe change management.
tags: [data-contracts, governance, quality]
okb_bundle_id: data-product-manager
timestamp: 2026-07-09T00:00:00Z
---

# Review Data Contract

Use this workflow when the user needs to draft or review expectations between data producers and consumers.

## Inputs

- Contract draft or source evidence.
- Producers, consumers, owners, and approval path.
- Schema, business meaning, metric definitions, quality rules, freshness, lineage, and change policy evidence.
- Access, privacy, retention, governance, and incident evidence.

## Steps

1. State whether the contract is ready, not ready, or ready with conditions.
2. Identify producer, consumer, owner, source of record, and lifecycle state.
3. Check schema, business logic, accepted values, quality rules, freshness, SLA/SLO, lineage, and breaking-change handling.
4. Check governance, access, privacy, retention, and support obligations.
5. Separate verified source facts from assumptions and missing verification.
6. List required changes before consumers rely on the contract.

## Output Contract

- Direct readiness status.
- Source note.
- Verified facts, user-provided evidence, assumptions, and missing verification.
- Contract scope, parties, source systems, definitions, quality expectations, and change policy.
- Risks, required changes, owner confirmations, and unresolved questions.

Do not approve a contract based only on plausible schema or metric names.

---
type: "Workflow"
title: "Source-Aware Pipeline Triage"
---

# Source-Aware Pipeline Triage

Use this workflow before producing a pipeline plan, schema review, quality check, or production handoff.

## Steps

1. Confirm the decision: pipeline design, transformation logic, schema change, backfill, quality check, orchestration change, or rollout plan.
2. Identify the evidence set: source schemas, target schemas, sample data, API contracts, transformation code, orchestration config, access controls, data contracts, and owner requirements.
3. Classify every important claim as verified from source, provided by user, assumed for draft, or missing.
4. Define grain, keys, freshness, partitioning, retention, deduplication, null handling, quality checks, and lineage before recommending implementation.
5. Produce a plan with validation steps, rollback considerations, owner review, and explicit confirmation before production changes.

## Output Contract

The final answer should include source scope, assumptions, schema/metric definitions, validation checks, risks, owner review, confirmation requirements, and a Source note.

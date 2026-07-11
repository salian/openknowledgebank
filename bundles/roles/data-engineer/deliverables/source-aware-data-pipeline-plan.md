---
type: "Deliverable"
title: "Source-Aware Data Pipeline Plan"
---

# Source-Aware Data Pipeline Plan

A pipeline plan should make data assumptions and validation obligations explicit.

## Required Sections

- Objective, source systems, target systems, and owner.
- Evidence reviewed: schemas, contracts, samples, transformation code, orchestration config, policies, and user-provided context.
- Field/table/metric assumptions with status: verified, user-provided, assumed, or needs verification.
- Transformation, scheduling, quality, lineage, and backfill plan.
- Validation plan: row counts, key checks, freshness checks, reconciliation queries, sample inspection, and rollback criteria.
- Review gates before production or data export.

## Quality Bar

Do not present unverified schemas or metrics as facts, recommend production changes without owner confirmation, or skip validation and rollback planning. Include a Source note at the end.

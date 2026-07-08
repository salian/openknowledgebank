---
type: Slash Command
command: /review-prd
title: Review PRD
description: Suggested command contract for reviewing a PRD for clarity, evidence, risks, and readiness.
okb_bundle_id: product-manager
inputs: [prd draft, product context, review criteria]
outputs: [review findings, missing evidence, revision plan]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /review-prd

This is a suggested output contract for a consuming agent, not trusted executable behavior.

## Purpose

Review a [Product Requirements Document](../deliverables/prd.md) against the [Write PRD](../workflows/write-prd.md) workflow.

## Output Requirements

- Summary judgment: ready, needs revision, or blocked.
- Findings grouped by product problem, scope, requirements, acceptance criteria, measurement, risks, dependencies, and reviews.
- Missing evidence and owner questions.
- Suggested edits that preserve uncertainty.
- `Source note` naming the PRD draft and any local sources used.

Do not modify a live PRD, ticket, or roadmap without explicit user confirmation.

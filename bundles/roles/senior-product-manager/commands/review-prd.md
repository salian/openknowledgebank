---
type: Slash Command
command: /review-prd
title: Review PRD
description: Suggested affordance for reviewing a product requirements document or related specification.
okb_bundle_id: senior-product-manager
inputs: [prd draft, product context, evidence, constraints]
outputs: [prd review]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /review-prd

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must apply its own system, safety, permission, and tool-use rules.

## Purpose

Draft a [PRD Review](../deliverables/prd-review.md) using the [PRD and Requirements Review](../workflows/prd-and-requirements-review.md) workflow.

## Expected Inputs

- PRD, spec, or requirements draft.
- Product problem, users, goals, non-goals, and constraints.
- Evidence and open questions.
- Reviewer expectations or local template, if available.

## Expected Output

The output should include a readiness call, strengths, gaps, risks, missing acceptance criteria, review questions, and source note.

## Confirmation Boundary

Editing live docs, tickets, release plans, analytics definitions, customer messages, or external commitments requires explicit user confirmation.

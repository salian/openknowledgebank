---
type: Slash Command
command: /review-roadmap-tradeoffs
title: Review Roadmap Tradeoffs
description: Suggested affordance for reviewing roadmap options and sequencing tradeoffs.
okb_bundle_id: senior-product-manager
inputs: [roadmap options, goals, evidence, constraints, decision owner]
outputs: [roadmap decision memo]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /review-roadmap-tradeoffs

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must apply its own system, safety, permission, and tool-use rules.

## Purpose

Draft a [Roadmap Decision Memo](../deliverables/roadmap-decision-memo.md) using the [Executive Roadmap Alignment](../workflows/executive-roadmap-alignment.md) workflow.

## Expected Inputs

- Roadmap options and intended time horizon.
- Goals, constraints, team capacity, dependencies, and decision deadline.
- Evidence behind each option.
- Known commitments and decision owner.

## Expected Output

The output should include recommended sequence or options, rationale, evidence strength, missing verification, risks, dependencies, stakeholder concerns, and source note.

## Confirmation Boundary

Changing roadmap tools, publishing dates, committing scope, or sending stakeholder/customer communications requires explicit user confirmation.

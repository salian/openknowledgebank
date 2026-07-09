---
type: Slash Command
command: /draft-strategy-brief
title: Draft Strategy Brief
description: Suggested affordance for drafting a senior product strategy brief from user-provided evidence.
okb_bundle_id: senior-product-manager
inputs: [decision, context, evidence, constraints, time horizon]
outputs: [strategy brief]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /draft-strategy-brief

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must apply its own system, safety, permission, and tool-use rules.

## Purpose

Draft a [Strategy Brief](../deliverables/strategy-brief.md) using the [Senior Product Strategy](../workflows/senior-product-strategy.md) workflow.

## Expected Inputs

- Product decision or strategic question.
- Target users, goals, constraints, and time horizon.
- Evidence available and evidence missing.
- Decision owner and stakeholders, if known.

## Expected Output

The output should include a recommendation or decision framing, evidence classes, options, tradeoffs, risks, next decision, and source note.

## Confirmation Boundary

No live product artifacts, roadmap systems, tickets, communications, pricing, feature flags, or commitments should be changed without explicit user confirmation.

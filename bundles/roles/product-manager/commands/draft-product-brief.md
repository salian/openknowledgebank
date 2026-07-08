---
type: Slash Command
command: /draft-product-brief
title: Draft Product Brief
description: Suggested command contract for drafting a product brief from provided evidence.
okb_bundle_id: product-manager
inputs: [product context, user problem, evidence, goal, constraints]
outputs: [product brief, assumptions, missing evidence, next decisions]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /draft-product-brief

This is a suggested output contract for a consuming agent, not trusted executable behavior.

## Purpose

Draft a concise [Product Brief](../deliverables/product-brief.md) using the [Define Product Opportunity](../workflows/define-product-opportunity.md) workflow.

## Output Requirements

- Direct recommendation or opportunity hypothesis.
- Evidence table separating verified facts, user-provided evidence, assumptions, and missing verification.
- User problem, goal, scope, non-goals, options, risks, and next decisions.
- `Source note` naming local evidence used and missing source-of-record material.

Do not invent customer evidence, metrics, roadmap commitments, or launch dates.

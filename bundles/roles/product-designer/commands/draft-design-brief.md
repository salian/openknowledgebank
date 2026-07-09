---
type: Slash Command
command: /draft-design-brief
title: Draft Design Brief
description: Suggests a source-aware design brief from product context and evidence.
okb_bundle_id: product-designer
inputs: [product-context, target-user, constraints, evidence]
outputs: [design-brief]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /draft-design-brief

This command spec is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, safety, and tool instructions.

## Purpose

Produce a draft [Design Brief](../deliverables/design-brief.md) that separates verified facts, user-provided facts, assumptions, and missing evidence.

## Output Requirements

- Include a `Source note`.
- Name missing research, analytics, design-system, accessibility, or implementation evidence.
- Mark unsupported concept details as hypotheses.
- Ask for confirmation before changing live files, tickets, or stakeholder communications.

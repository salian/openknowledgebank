---
type: Slash Command
command: /review-ui-flow
title: Review UI Flow
description: Suggests a source-aware review of a screen, wireframe, flow, or prototype.
okb_bundle_id: product-designer
inputs: [artifact, user-scenario, constraints]
outputs: [design-review-note]
requires_confirmation: false
timestamp: 2026-07-09T00:00:00Z
---

# /review-ui-flow

This command spec is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, safety, and tool instructions.

## Purpose

Produce a [Design Review Note](../deliverables/design-review-note.md) with prioritized findings and handoff questions.

## Output Requirements

- Include a `Source note`.
- State what artifact and scenario were reviewed.
- Rank issues by user impact.
- Cover happy path, empty, loading, error, permission, responsive, and accessibility-sensitive states where relevant.
- Ask for confirmation before modifying live design files, tickets, specs, or communications.

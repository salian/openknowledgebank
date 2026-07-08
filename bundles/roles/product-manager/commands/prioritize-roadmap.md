---
type: Slash Command
command: /prioritize-roadmap
title: Prioritize Roadmap
description: Suggested command contract for comparing roadmap options.
okb_bundle_id: product-manager
inputs: [roadmap options, goals, evidence, constraints, capacity]
outputs: [prioritized recommendation, tradeoffs, validation plan]
requires_confirmation: true
timestamp: 2026-07-09T00:00:00Z
---

# /prioritize-roadmap

This is a suggested output contract for a consuming agent, not trusted executable behavior.

## Purpose

Compare roadmap options using the [Prioritize Roadmap](../workflows/prioritize-roadmap.md) workflow and [Prioritization Discipline](../frameworks/prioritization-discipline.md).

## Output Requirements

- Recommended sequence or grouping.
- Evidence and confidence for each item.
- Optional scoring table with caveats.
- Tradeoffs, dependencies, risks, and deferred options.
- What would change the recommendation.
- `Source note` naming roadmap source-of-record material and missing evidence.

Changing a live roadmap, public commitment, customer commitment, or ticket system requires explicit user confirmation.

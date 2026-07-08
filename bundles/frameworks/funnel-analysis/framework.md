---
type: Framework
title: Funnel Analysis Framework
description: "Defines how to scope, measure, compare, and explain stage-by-stage funnel performance."
okb_bundle_id: funnel-analysis
timestamp: "2026-07-09T00:00:00Z"
---

# Funnel Analysis Framework

Funnel analysis measures how a population progresses through an ordered set of steps. The framework is useful only when the step definitions, counting unit, reporting window, filters, segment rules, and tool behavior are explicit.

## Core Moves

1. Define the decision the funnel should support.
2. Define each step from verified event, dimension, page, screen, CRM, or warehouse evidence.
3. State entry rules, especially whether users or sessions may enter mid-funnel.
4. State denominator logic: users, sessions, accounts, first step, previous step, or another verified basis.
5. Measure stage conversion, drop-off, elapsed time, and next actions only within the verified report scope.
6. Compare segments only when date range, filters, attribution, and definitions are aligned.
7. Separate findings, hypotheses, recommended actions, and evidence still needed.

## Interpretation Rules

- A funnel drop-off identifies where progression changed or failed; it does not prove why.
- Open and closed funnels can answer different questions and should not be compared without stating entry rules.
- A skipped step, repeated event, direct-follow requirement, or time-window setting can materially change counts.
- Segment and breakdown findings inherit the analytics tool's attribution and counting behavior.
- User-level investigation, exports, live changes, and campaign or experiment actions require permission and confirmation.

## Output Contract

Every funnel answer should distinguish:

- verified source facts;
- user-provided evidence;
- assumptions for the current draft;
- missing verification before conclusion or action.

Use [Funnel Analysis Brief](deliverables/funnel-analysis-brief.md) for decision-facing output.

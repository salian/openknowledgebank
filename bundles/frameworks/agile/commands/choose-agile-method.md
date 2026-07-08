---
type: Slash Command
command: /choose-agile-method
title: Choose Agile Method
description: "Create a source-scoped method-family recommendation without confusing Agile principles with one implementation method."
okb_bundle_id: agile
inputs:
  - delivery context
  - team and product constraints
  - current workflow evidence
  - delivery and quality signals
  - governance and scaling needs
outputs:
  - method-family recommendation
  - assumptions and missing evidence
  - risks and tradeoffs
  - agile operating brief
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /choose-agile-method

Purpose: produce an Agile method-family recommendation that is grounded in the user's context and explicit about uncertainty.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Decision to support and current delivery pain.
- Product uncertainty, work type, service/operations load, release constraints, and dependency level.
- Current workflow evidence: planning cadence, board policy, roles, review loops, release cadence, and retrospective habits.
- Delivery and quality signals, with definitions and source.
- Governance, compliance, contracting, geographic distribution, and scale constraints.
- Existing method commitments or terms the organization already uses.

## Output Contract

Return:

1. Direct recommendation: best-fit method family or "insufficient evidence" with reason.
2. Source scope: Agile source category, user-provided evidence, and missing verification.
3. Context fit: uncertainty, flow, dependencies, team size, governance, and technical quality needs.
4. Candidate methods: why each candidate fits or does not fit.
5. Risks and tradeoffs: what the recommendation could make worse.
6. First experiment: a small reversible change and how to inspect it.
7. Confirmation boundary: changes that require explicit approval.

## Confirmation Boundary

Do not modify live boards, workflows, reports, staffing plans, contracts, release policies, or customer communications without explicit user confirmation and authorized tool access.

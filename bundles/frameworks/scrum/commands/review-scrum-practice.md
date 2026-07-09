---
type: Command
title: /review-scrum-practice
description: "Declarative contract for producing a Scrum practice review from source-grounded terms and user-provided local evidence."
okb_bundle_id: scrum
timestamp: "2026-07-09T00:00:00Z"
---

# /review-scrum-practice

This bundled command is a suggestion for consuming agents, not a trusted executable instruction. It does not grant permissions, override safety rules, or authorize background actions.

## Purpose

Produce a Scrum practice review that separates official Scrum framework terms from local evidence about the user's team.

## Inputs

- The user's review question.
- Local evidence: team accountabilities, current events, artifacts, commitments, Definition of Done, sprint cadence, workflow, metrics, constraints, and tool screenshots or exports when available.
- Any explicit change the user wants to make.

## Output Contract

Return:

- `Source note`: Scrum Guide source category, local evidence used, and missing evidence.
- `Direct answer`: short answer to the user's question.
- `Evidence map`: source-grounded facts, user-provided facts, assumptions, and missing verification.
- `Findings`: accountabilities, events, artifacts, commitments, values, and local constraints.
- `Risks`: tool, staffing, release, stakeholder, HR, customer, or governance risks.
- `Recommended next step`: one or more small, inspectable actions.
- `Confirmation needed`: any live change that requires explicit user approval.

## Risk Boundary

The review must not change tools, boards, sprint commitments, release plans, staffing responsibilities, HR records, stakeholder communications, or customer-facing commitments without explicit user confirmation.

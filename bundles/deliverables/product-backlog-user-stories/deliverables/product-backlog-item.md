---
type: Deliverable
title: Product Backlog Item / User Story
description: A source-aware, reviewable backlog item tied to a product outcome and explicit acceptance evidence.
okb_bundle_id: product-backlog-user-stories
required_inputs: [Product Goal or outcome, affected user or stakeholder, problem evidence, desired behavior, constraints, acceptance evidence, dependencies and risks, team sizing or readiness convention if applicable]
outputs: [direct answer, evidence status, item statement, acceptance criteria, Product Goal alignment, ordering rationale, non-goals, dependencies, risks, open questions, source note]
quality_criteria: [outcome-focused, small enough for the stated delivery boundary, independently understandable, acceptance criteria verifiable, assumptions separated, ordering rationale explicit, no invented local facts]
timestamp: "2026-08-01T00:00:00Z"
---

# Product Backlog Item / User Story

## Direct Answer

State the proposed item and the decision it supports.

## Evidence Status

- **Verified:** facts confirmed in an authoritative source or inspected local artifact.
- **Provided:** facts supplied by the user for this task.
- **Assumed:** temporary working assumptions, each with an owner or validation path.
- **Needs verification:** missing evidence that prevents a stronger conclusion.

## Item

Use this optional format when it fits:

> As a `[user or stakeholder]`, I want `[capability or behavior]`, so that `[outcome or value]`.

For non-user-facing work, describe the required outcome and why it matters instead of forcing a user-story sentence.

## Acceptance Criteria

Use observable conditions. Include normal behavior, important edge cases, permissions or privacy constraints, accessibility or safety requirements where relevant, and what evidence demonstrates completion. Keep item-specific acceptance criteria separate from the team's Definition of Done.

## Product Goal And Ordering

- Product Goal alignment: explain the link or state `Needs verification`.
- Ordering basis: value, risk reduction, dependency, learning, urgency, or a named scoring method.
- Inputs and scope: state the source, time/version, definitions, and missing inputs.
- Confidence: high, medium, low, or `Needs verification`.

## Non-Goals, Dependencies, Risks, And Open Questions

Name what is excluded, what must happen first, what could fail, and what the accountable decision-maker must resolve.

## Source Note

Name the relevant official source category, the local evidence used for this item, and the missing source or artifact still needed before an assumption becomes a conclusion.

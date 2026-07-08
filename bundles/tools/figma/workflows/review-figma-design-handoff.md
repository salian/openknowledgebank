---
type: Workflow
title: Review Figma Design Handoff
description: "Plan Figma design-to-development handoff with verified source, file, design-system, Dev Mode, and codebase evidence."
okb_bundle_id: figma
timestamp: "2026-07-09T00:00:00Z"
---

# Review Figma Design Handoff

## Purpose

Create a reviewable plan for Figma design handoff before treating a design as implementation-ready, exporting assets, updating a design system, or changing a live file.

## Evidence to Inspect First

- Current official Figma source category for the relevant file, component, library, variable, prototype, Dev Mode, sharing, API, or accessibility behavior.
- User-provided Figma file, page, frame, layer, component, instance, style, variable, library, prototype, comment, screenshot, export, or Dev Mode evidence.
- Design-system source-of-truth, component owner, token/variable definitions, asset rules, content states, responsive behavior, accessibility notes, and implementation constraints.
- Codebase evidence for existing components, tokens, breakpoints, routes, framework constraints, and known implementation gaps.
- Permission, sharing, privacy, security, export-rights, approval, and rollback constraints.

## Output Shape

1. Source note.
2. Readiness answer: ready, ready with gaps, or not ready.
3. Current-state evidence: Figma file, frames, components, variables, prototypes, comments, Dev Mode, codebase, and permissions that are actually verified.
4. Gap list: missing evidence and unsupported assumptions.
5. Handoff plan: target frames, states, components, variables, assets, interactions, responsive behavior, content, implementation questions, and acceptance criteria.
6. Design-system review: source library, component mappings, token/variable alignment, style usage, owner questions, and migration risk.
7. Validation plan: compare design to implementation, test responsive states, check accessibility, verify exports, review comments, and confirm design-system ownership.
8. Confirmation and rollout: owner, approver, action boundary, rollback trigger, and rollback steps.

## Reconciliation Pattern

When Figma and implementation disagree, do not choose a winner until definitions align. Compare source component, variable/style value, breakpoint, state, interaction, content, asset export, accessibility expectation, implementation constraint, owner decision, and current code behavior. Separate expected differences from unresolved discrepancies.

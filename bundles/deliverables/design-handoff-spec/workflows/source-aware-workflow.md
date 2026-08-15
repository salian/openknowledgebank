---
type: "Workflow"
title: "Design Handoff Specification source-aware workflow"
description: "Verify-first workflow for producing a reviewable design handoff specification."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current standards, originator guidance, required sections, evidence expectations, audience needs, and local approval procedures.
3. Inventory approved scope and design links, node and component versions, flows and states, design-system mappings, tokens and breakpoints, content and localization, interaction and motion behavior, accessibility requirements and tests, asset provenance, data and error states, analytics, engineering constraints, acceptance criteria, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the design handoff specification, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before change source designs or code, export restricted assets, publish content, declare accessibility conformance, commit estimates, merge, deploy, or represent implementation parity.

## Required Output

### Direct Answer
State what can and cannot be concluded.

### Evidence Status
- Verified:
- Provided:
- Assumed:
- Needs verification:

### Verification Plan
List exact sources, records, checks, conflicts, and reviewers.

### Confirmation Boundary
Name the evidenced authorized reviewer and prohibited actions.

### Source Note
List authoritative sources used, local evidence used, and missing sources.

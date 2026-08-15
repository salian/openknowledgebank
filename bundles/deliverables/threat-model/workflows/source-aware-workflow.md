---
type: "Workflow"
title: "Threat Model source-aware workflow"
description: "Verify-first workflow for producing a reviewable threat model and mitigation decision record."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current standards, originator guidance, required sections, evidence expectations, audience needs, and local approval procedures.
3. Inventory system and environment versions, architecture and data-flow diagrams, asset and data classifications, identity and trust boundaries, dependency and supplier evidence, threat intelligence scope and date, abuse cases, control design and test evidence, vulnerability records, ranking criteria and uncertainty, mitigations and owners, residual-risk decisions, reviews, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the threat model and mitigation decision record, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to access or test systems without authorization, expose sensitive architecture, declare vulnerabilities, change controls, exploit weaknesses, accept risk, claim security or compliance, or publish the model.

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

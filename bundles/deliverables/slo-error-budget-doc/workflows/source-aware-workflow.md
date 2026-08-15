---
type: "Workflow"
title: "SLO and Error Budget Document source-aware workflow"
description: "Verify-first workflow for producing a reviewable SLO and error budget specification."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current standards, originator guidance, required sections, evidence expectations, audience needs, and local approval procedures.
3. Inventory service and user-journey research, ownership and dependencies, indicator specification and telemetry lineage, event taxonomy and exclusions, historical baseline and missingness, calculation code and windows, product and reliability risk decisions, proposed targets and budget, alert tests, incident and release policy, exceptions, reviews, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the SLO and error budget specification, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to change telemetry, set targets unilaterally, stop or authorize releases, suppress alerts, waive incidents, claim reliability, or approve production policy.

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

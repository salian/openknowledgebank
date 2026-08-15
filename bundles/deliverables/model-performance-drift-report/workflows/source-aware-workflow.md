---
type: "Workflow"
title: "Model Performance and Drift Report source-aware workflow"
description: "Verify-first workflow for producing a reviewable model performance and drift report."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current standards, originator guidance, required sections, evidence expectations, audience needs, and local approval procedures.
3. Inventory model card and approved use, version and deployment records, training and production data lineage, feature and prediction distributions, labels and ground truth, monitoring definitions and code, baselines and thresholds, uncertainty and sample sizes, subgroup analysis, incidents and changes, validation, rollback, owners, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the model performance and drift report, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to access restricted data, infer sensitive traits, change thresholds, retrain, deploy, roll back, automate decisions, declare fairness or validity, close incidents, or approve continued use.

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

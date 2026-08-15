---
type: "Workflow"
title: "Write-Audit-Publish Pattern source-aware workflow"
description: "Verify-first workflow for producing a reviewable write-audit-publish implementation and release brief."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify framework definitions, applicability, assumptions, and current source context.
3. Inventory Iceberg and engine versions, catalog and table configuration, branch state, write and audit queries, data-quality rules, concurrency behavior, retention policy, access controls, change plan, rollback evidence, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the write-audit-publish implementation and release brief, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before create or modify production branches, write data, fast-forward or publish snapshots, expire snapshots, alter retention, bypass controls, or claim data correctness.

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

---
type: "Workflow"
title: "Data Mapping and Integration Specification source-aware workflow"
description: "Verify-first workflow for producing a reviewable data mapping and integration specification."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current standards, originator guidance, required sections, evidence expectations, audience needs, and local approval procedures.
3. Inventory source and target systems and versions, inspected schemas and samples, field definitions and owners, keys and grain, types and constraints, mapping and transformation rules, code sets, timing and volumes, lineage, quality and reconciliation rules, privacy and security controls, failure handling, tests, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the data mapping and integration specification, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before access systems, extract or move data, expose credentials or personal data, create mappings, alter schemas, run jobs, overwrite records, deploy, or represent reconciliation success.

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

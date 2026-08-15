---
type: "Workflow"
title: "Infrastructure as Code Template source-aware workflow"
description: "Verify-first workflow for producing a reviewable infrastructure-as-code template and release brief."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current standards, originator guidance, required sections, evidence expectations, audience needs, and local approval procedures.
3. Inventory tool and provider versions, target accounts and regions, current state and imports, approved architecture, resource schemas and quotas, module provenance, inputs and outputs, identity and access design, secrets handling, network and data controls, policy checks, formatting and validation, tests and plan output, cost estimate, drift and rollback plan, observability, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the infrastructure-as-code template and release brief, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before request or embed credentials, initialize remote state, access accounts, create plans against production, apply or destroy resources, change IAM or networks, expose data, deploy, or claim security or compliance.

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

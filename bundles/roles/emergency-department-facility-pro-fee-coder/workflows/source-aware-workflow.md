---
type: "Workflow"
title: "Emergency Department Facility and Professional Fee Coder source-aware workflow"
description: "Verify-first workflow for producing a reviewable ED facility and professional coding audit record."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current occupational and professional sources, jurisdiction, actual role, qualifications, and local procedures.
3. Inventory coding authority, patient payer facility and practitioner identifiers, complete authenticated ED record, facility level policy and resource evidence, professional documentation, diagnosis and procedure support, current code-set claims and NCCI references, query record, claim-type unit and modifier validation, submission remittance denial and audit logs, PHI controls, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the ED facility and professional coding audit record, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to create or alter clinical documentation, infer acuity time or decision making, conflate facility and professional criteria, override edits, expose PHI, submit unsupported claims, or promise payment.

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

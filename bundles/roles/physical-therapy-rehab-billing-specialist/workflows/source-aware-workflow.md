---
type: "Workflow"
title: "Physical Therapy and Rehabilitation Billing Specialist source-aware workflow"
description: "Verify-first workflow for producing a reviewable rehabilitation billing workqueue and claim evidence record."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current occupational and professional sources, jurisdiction, actual role, qualifications, and local procedures.
3. Inventory billing authority, patient payer and provider identifiers, current plan and jurisdiction rules, order and plan of care, encounter notes signatures attendance and service time, authorization and referral records, code unit modifier and edit references, claim scrub and submission logs, remittance denial and appeal records, PHI access controls, reconciliations, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the rehabilitation billing workqueue and claim evidence record, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to create or alter clinical records, select diagnoses without documentation, infer time or units, override edits, expose PHI, submit or appeal without authority, post unsupported adjustments, or promise payment.

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

---
type: "Workflow"
title: "National Correct Coding Initiative Edits source-aware workflow"
description: "Verify-first workflow for producing a reviewable NCCI edit analysis and claim-support record."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current controlling and interpretive sources, effective dates, jurisdiction, applicability, exceptions, and local procedures.
3. Inventory payer program beneficiary provider setting service date and claim authority, authenticated encounter and procedure documentation, licensed current CPT HCPCS sources, correct Medicare or Medicaid edit type file version effective date and checksum, exact code pair unit or add-on lookup, modifier indicator and clinical support, payer policy and adoption evidence, coder clinician and compliance review, claim edit denial appeal and adjustment records, PHI controls and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the NCCI edit analysis and claim-support record, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to create clinical facts, copy protected code descriptors improperly, select codes or modifiers without support, override edits, expose PHI, submit or alter claims, appeal without authority, or promise payment.

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

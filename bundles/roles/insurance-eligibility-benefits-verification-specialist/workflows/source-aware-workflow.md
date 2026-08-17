---
type: "Workflow"
title: "Insurance Eligibility and Benefits Verification Specialist source-aware workflow"
description: "Verify-first workflow for producing a reviewable eligibility and benefits verification record."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current occupational and professional sources, jurisdiction, actual role, qualifications, and local procedures.
3. Inventory request and access authority, patient and subscriber identifiers, payer plan group and effective dates, provider and facility identifiers, proposed service date place and description, inquiry and response payload or portal record, call reference and representative, network authorization referral limit exclusion and accumulator responses, estimate assumptions, discrepancy follow-up, privacy access and credential controls, timestamp and handoff approval.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the eligibility and benefits verification record, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to access PHI or portals without authority, alter patient or plan data, promise coverage or payment, infer authorization, quote final responsibility, schedule or cancel care, or represent guarantee.

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

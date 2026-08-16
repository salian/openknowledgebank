---
type: "Workflow"
title: "DME Billing Specialist for Durable Medical Equipment source-aware workflow"
description: "Verify-first workflow for producing a reviewable DMEPOS claim and proof-of-delivery evidence record."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current occupational and professional sources, jurisdiction, actual role, qualifications, and local procedures.
3. Inventory supplier enrollment accreditation location and billing authority, beneficiary payer and jurisdiction, treating-practitioner order and medical-record support, item HCPCS make model serial quantity and modifier, rental purchase repair and supply status, proof of delivery and pickup, prior authorization and coverage references, current fee and claim rules, recertification and continued-need records, claim validation remittance denial and appeal logs, PHI controls, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the DMEPOS claim and proof-of-delivery evidence record, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to create orders or delivery records, substitute items or codes, infer continued need, alter signatures, override authorization or coverage edits, expose PHI, submit claims, or promise payment.

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

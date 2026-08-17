---
type: "Workflow"
title: "Prior Authorization Specialist for Specialty Infusion and Oncology source-aware workflow"
description: "Verify-first workflow for producing a reviewable specialty prior-authorization evidence and status record."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current occupational and professional sources, jurisdiction, actual role, qualifications, and local procedures.
3. Inventory organization and specialist authority, patient payer plan and benefit identifiers, provider enrollment and site, authenticated order with drug dose route frequency and dates, diagnosis and clinical-record support, current payer policy criteria and channel, prior treatment and test records as documented, clinician urgency and appeal decisions, consent and PHI controls, submission attachments timestamps requests decision reason and validity period, scheduling and billing handoffs, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the specialty prior-authorization evidence and status record, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to diagnose, select or change treatment, invent urgency or clinical support, expose PHI, submit or appeal without authority, represent authorization as coverage or payment, schedule unsafe care, or promise outcomes.

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

---
type: "Workflow"
title: "Virtual Medical Scribe for Outpatient Clinics source-aware workflow"
description: "Verify-first workflow for producing a reviewable clinician-reviewable outpatient encounter note draft."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current occupational and professional sources, jurisdiction, actual role, qualifications, and local procedures.
3. Inventory clinic and clinician authorization, scribe identity training and agreement, patient and encounter identifiers, permitted access and minimum-necessary basis, secure workspace and EHR session, audio or encounter source as authorized, clinician-stated findings assessment and plan, medication and order source, note template and policy, contradiction and clarification log, corrections audit trail, clinician review signature and date, incident records, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the clinician-reviewable outpatient encounter note draft, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to access records without authorization, diagnose or advise, infer findings, place orders, select codes, sign notes, alter clinician decisions, disclose health information, submit claims, or represent documentation sufficiency.

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

---
type: "Workflow"
title: "HCC Risk Adjustment Coder for Medicare Advantage Plans source-aware workflow"
description: "Verify-first workflow for producing a reviewable HCC coding review workpaper and query log."
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify current occupational and professional sources, jurisdiction, actual role, qualifications, and local procedures.
3. Inventory member and encounter identifiers, date of service and provider credentials, complete signed medical record and provenance, record type and data-source eligibility, current ICD-10-CM code set and guidelines, CMS-HCC model year and mappings, documented assessment and plan, coding rationale and validation, compliant query and response, additions deletions and audit trail, submission system record, independent review, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define included and excluded work, records, systems, permissions, dependencies, validation, and rollback or stop conditions.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the HCC coding review workpaper and query log, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before taking any action to access records without authority, infer or add diagnoses, lead providers, alter notes, submit risk data, calculate unsupported scores, affect payment, close audits, or certify compliance.

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

---
type: Workflow
title: Suspicious Activity Report source-aware workflow
description: Verify-first workflow for producing a reviewable suspicious activity report decision and evidence brief.
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify official source versions and applicability.
3. Inventory institution type and governing SAR rule, transaction and customer records, alert and investigation evidence, detection date, threshold analysis, filing history, supporting documents, confidentiality controls, escalation, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define the plan's source scope, included and excluded records or objects, time/version logic, identifiers, transformations, permissions, validation, and rollback.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the suspicious activity report decision and evidence brief, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before file, amend, disclose, or confirm a SAR; contact a subject; freeze or close an account; alter monitoring; or represent a legal conclusion.

## Required Output

### Direct Answer
State what evidence supports and what remains unresolved.

### Evidence Status
List `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.

### Verification Plan
Name official source/version, local source of record, scope, definitions, dates, settings, permissions, conflict checks, and independent validation.

### Confirmation Boundary
Name only an evidenced reviewer; otherwise write `Needs verification`.

### Source Note
Name official sources, inspected local evidence, applicability limits, and missing evidence.


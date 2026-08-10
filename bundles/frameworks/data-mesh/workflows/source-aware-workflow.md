---
type: Workflow
title: Data Mesh source-aware workflow
description: Verify-first workflow for producing a reviewable Data mesh operating-model brief.
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify official source versions and applicability.
3. Inventory business domains, data products, producers, consumers, owners, source systems, schemas, semantics, SLAs, quality evidence, access policies, classifications, lineage, platform capabilities, interoperability standards, governance decisions, costs, risks, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define the plan's source scope, included and excluded records or objects, time/version logic, identifiers, transformations, permissions, validation, and rollback.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the Data mesh operating-model brief, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before reassign ownership, expose or move data, change access policies, deploy platforms, certify data products, retire systems, or commit funding.

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


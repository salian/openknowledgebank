---
type: Workflow
title: Behavior-Driven Development source-aware workflow
description: Verify-first workflow for producing a reviewable BDD behavior and acceptance brief.
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify official source versions and applicability.
3. Inventory product objective, stakeholders, domain language, business rules, examples, edge cases, Given-When-Then scenarios, acceptance boundaries, system version, test harness, fixtures, environments, results, owners, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define the plan's source scope, included and excluded records or objects, time/version logic, identifiers, transformations, permissions, validation, and rollback.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the BDD behavior and acceptance brief, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before change production behavior, execute untrusted tests, modify data, deploy code, weaken controls, or claim acceptance.

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


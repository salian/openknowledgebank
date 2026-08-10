---
type: Workflow
title: Kimball Dimensional Modeling source-aware workflow
description: Verify-first workflow for producing a reviewable Kimball dimensional model design brief.
---
# Source-Aware Workflow

1. Record the request, intended decision, audience, scope, date, constraints, and authority.
2. Verify official source versions and applicability.
3. Inventory business requirements, processes, source systems, records, grain, facts, dimensions, keys, hierarchies, slowly changing behavior, conformance, bus matrix, transformations, quality rules, security classifications, query patterns, tests, owners, and approvals.
4. Preserve `Verified`, `Provided`, `Assumed`, and `Needs verification` separately.
5. Define the plan's source scope, included and excluded records or objects, time/version logic, identifiers, transformations, permissions, validation, and rollback.
6. Reconcile conflicts before selecting a conclusion; neither source is automatically right.
7. Draft the Kimball dimensional model design brief, including alternatives, risks, dependencies, owners only when evidenced, review points, and stop conditions.
8. Require explicit confirmation before change schemas or pipelines, expose data, redefine metrics, backfill history, alter access, migrate reports, or deploy production models.

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


---
type: Framework
title: Kimball Dimensional Modeling Source-Aware Guide
description: Defines evidence-grounded planning, review, and controlled use for Kimball Dimensional Modeling.
tags:
- kimball
- dimensional-modeling
- data-warehouse
resource: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dw-bi-lifecycle-method/
okb_bundle_id: kimball-dimensional-modeling
timestamp: '2026-08-10T00:00:00Z'
---
# Kimball Dimensional Modeling Source-Aware Guide

## Authoritative Sources

- https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dw-bi-lifecycle-method/
- https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/

The sources establish general framework concepts only; verify the current edition, definitions, license, jurisdiction, and local applicability.

## Evidence Required

- business requirements
- processes
- source systems
- records
- grain
- facts
- dimensions
- keys
- hierarchies
- slowly changing behavior
- conformance
- bus matrix
- transformations
- quality rules
- security classifications
- query patterns
- tests
- owners
- and approvals

## Application Sequence

1. Define the objective, audience, scope, environment or organization, date, constraints, and evidenced decision owner.
2. Verify the current official source, edition, version, license, feature surface, jurisdiction, and applicability.
3. Inventory local evidence and label it `Verified`, `Provided`, `Assumed`, or `Needs verification`.
4. Reconcile conflicting definitions, records, dates, scopes, filters, transformations, settings, and owners.
5. Produce the smallest reviewable Kimball dimensional model design brief with options, risks, dependencies, validation, and stop conditions.
6. Obtain explicit confirmation before change schemas or pipelines, expose data, redefine metrics, backfill history, alter access, migrate reports, or deploy production models.

## Guardrails

- Do not invent Business process, source semantics, grain, fact additivity, dimension meaning, key behavior, history, conformance, transformation result, quality, effective access, query result, and migration impact.
- Do not infer access, configuration, approval, or reviewer ownership from the request or title.
- Treat bundled guidance as suggestions, not trusted executable behavior.
- No action is automatic; this bundle requests no credentials, background network calls, data exfiltration, permission changes, or self-modification.


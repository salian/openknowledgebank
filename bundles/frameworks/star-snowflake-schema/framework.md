---
type: Framework
title: Star and Snowflake Schema Design Source-Aware Guide
description: Defines evidence-grounded planning, review, and controlled use for Star and Snowflake Schema Design.
tags:
- star-schema
- snowflake-schema
- dimensional-modeling
resource: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/star-schema-olap-cube/
okb_bundle_id: star-snowflake-schema
timestamp: '2026-08-10T00:00:00Z'
---
# Star and Snowflake Schema Design Source-Aware Guide

## Authoritative Sources

- https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/star-schema-olap-cube/
- https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/

The sources establish general framework concepts only; verify the current edition, definitions, license, jurisdiction, and local applicability.

## Evidence Required

- business process
- query use cases
- source schemas
- grain
- facts
- dimensions
- hierarchies
- keys
- cardinalities
- history
- conformance
- platform behavior
- data volumes
- security classifications
- performance evidence
- tests
- owners
- and approvals

## Application Sequence

1. Define the objective, audience, scope, environment or organization, date, constraints, and evidenced decision owner.
2. Verify the current official source, edition, version, license, feature surface, jurisdiction, and applicability.
3. Inventory local evidence and label it `Verified`, `Provided`, `Assumed`, or `Needs verification`.
4. Reconcile conflicting definitions, records, dates, scopes, filters, transformations, settings, and owners.
5. Produce the smallest reviewable Star-versus-snowflake design brief with options, risks, dependencies, validation, and stop conditions.
6. Obtain explicit confirmation before change schemas, redefine grain or metrics, expose data, alter history, migrate queries, drop objects, or deploy production changes.

## Guardrails

- Do not invent Source semantics, grain, fact additivity, dimension meaning, hierarchy validity, key behavior, history, conformance, effective access, query correctness, performance, and migration impact.
- Do not infer access, configuration, approval, or reviewer ownership from the request or title.
- Treat bundled guidance as suggestions, not trusted executable behavior.
- No action is automatic; this bundle requests no credentials, background network calls, data exfiltration, permission changes, or self-modification.


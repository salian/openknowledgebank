---
type: Deliverable Guide
title: Data Model and Schema Design Source-Aware Guide
description: Defines source-aware business process, grain, entity, fact, dimension, key, relationship, constraint, history, naming, lineage, privacy, and migration design review, evidence handling, and action boundaries.
resource: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/
okb_bundle_id: data-model-schema-design
timestamp: '2026-08-01T00:00:00Z'
---
# Data Model and Schema Design Source-Aware Guide

Source-aware deliverable bundle for business process, grain, entity, fact, dimension, key, relationship, constraint, history, naming, lineage, privacy, and migration design review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Authoritative and Identified Sources
- https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/

Name an applicable URL in every Source Note. Verify current version, date, scope, and applicability. Do not reproduce licensed standards or proprietary methods; disclose when a source is secondary or a licensed primary text is still required.

## Evidence Required
- business questions and process scope, source systems and contracts, sample profiles and quality, entity and identifier definitions, declared grain, facts and aggregation rules, dimensions and history requirements, relationships and cardinality, null and constraint policy, naming and data types, privacy classification and retention, access, lineage, target platform, performance, migration and compatibility, tests, owners, and approvals

## Application Sequence
1. Define the decision, scope, owner, date, and source version.
2. Inventory evidence as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile definitions, identifiers, versions, periods, scope, permissions, processing, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails
- Do not infer source schema, entity identity, grain, cardinality, key uniqueness, metric additivity, history behavior, data quality, privacy classification, or migration safety.
- Do not invent artifact provenance, access, execution, approval, or reviewer ownership.
- Require accountable confirmation before actions that create or alter schemas, tables, fields, keys, constraints, migrations, retention, or access controls; read, copy, transform, or delete data; deploy database changes.

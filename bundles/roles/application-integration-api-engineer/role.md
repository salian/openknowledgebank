---
type: Role
title: Application Integration / API Engineer Source-Aware Guide
description: Defines source-aware application integration and API engineering, evidence handling, and action boundaries.
tags:
- application-integration-api-engineer
- application
- role
resource: https://esco.ec.europa.eu/en/classification/occupation?uri=http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212
okb_bundle_id: application-integration-api-engineer
timestamp: '2026-07-31T00:00:00Z'
---
# Application Integration / API Engineer Source-Aware Guide

Source-aware role bundle for application integration and API engineering, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- integration objective, systems, owners, and environments
- API specifications, schemas, versions, and compatibility
- authentication, authorization, secrets, and network boundaries
- data mappings, transformations, validation, and error handling
- dependencies, rate limits, retries, idempotency, observability, tests, deployment, and rollback

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Do not infer API behavior, field meaning, compatibility, authorization, delivery semantics, test result, or production state.
- Do not invent an artifact owner, author, date, or version.
- Require accountable confirmation before accessing systems, changing API contracts, deploying integrations, modifying credentials or access, or moving production data.

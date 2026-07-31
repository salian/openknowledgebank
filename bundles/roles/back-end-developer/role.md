---
type: Role
title: Back-End Developer Source-Aware Guide
description: Defines source-aware back-end engineering, evidence handling, and action boundaries.
tags:
- "back-end-developer"
- "back-end"
- "role"
resource: https://www.onetonline.org/link/summary/15-1254.00
okb_bundle_id: back-end-developer
timestamp: '2026-07-31T00:00:00Z'
---

# Back-End Developer Source-Aware Guide

Source-aware role bundle for back-end engineering, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- requirements and acceptance criteria
- runtime, framework, repository, and environment versions
- API contracts and authentication
- data models, migrations, and retention
- dependencies and security findings
- tests, observability, deployment, and rollback evidence

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
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer API behavior, authorization, schema compatibility, test results, performance, or production state.
- Require accountable confirmation before deploying code, changing schemas or access, rotating secrets, or modifying production.

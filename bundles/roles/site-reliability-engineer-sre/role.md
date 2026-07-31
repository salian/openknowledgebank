---
type: Role
title: Site Reliability Engineer (SRE) Source-Aware Guide
description: Defines source-aware site reliability engineering, evidence handling, and action boundaries.
tags:
- "site-reliability-engineer-sre"
- "site"
- "role"
resource: https://www.onetonline.org/link/summary/15-1252.00
okb_bundle_id: site-reliability-engineer-sre
timestamp: '2026-07-31T00:00:00Z'
---

# Site Reliability Engineer (SRE) Source-Aware Guide

Source-aware role bundle for site reliability engineering, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- service, users, critical journeys, owners, and production scope
- SLI definitions, data sources, SLO windows, targets, and error-budget policy
- architecture, dependencies, failure modes, and change history
- monitoring, alerts, incidents, runbooks, postmortems, capacity, access, deployment, and rollback evidence

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
- Do not infer service health, SLI validity, SLO attainment, error-budget consumption, incident cause, capacity, or production state.
- Require accountable confirmation before changing production, deploying releases, modifying alerts or access, using credentials, or issuing incident communications.

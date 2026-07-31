---
type: Role
title: Data Analyst Source-Aware Guide
description: Defines source-aware data analysis and decision support, evidence handling, and action boundaries.
tags:
- "data-analyst"
- "data"
- "role"
resource: https://data.europa.eu/esco/occupation/d3edb8f8-3a06-47a0-8fb9-9b212c006aa2
okb_bundle_id: data-analyst
timestamp: '2026-07-31T00:00:00Z'
---

# Data Analyst Source-Aware Guide

Source-aware role bundle for data analysis and decision support, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- decision question, stakeholders, population, period, and acceptance criteria
- source systems, schema, grain, lineage, and ownership
- data quality, exclusions, and missingness
- metric definitions, transformations, filters, and reconciliations
- statistical method and uncertainty
- privacy, access, review, and publication context

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
- Do not infer data meaning, population completeness, metric definition, statistical significance, causality, or current result.
- Require accountable confirmation before querying sensitive data, publishing findings, changing production dashboards, or asserting causality.

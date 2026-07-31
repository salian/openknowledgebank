---
type: Role
title: Software Architect Source-Aware Guide
description: Defines source-aware software architecture, evidence handling, and action boundaries.
tags:
- "software-architect"
- "software"
- "role"
resource: https://esco.ec.europa.eu/en/classification/occupation_main
okb_bundle_id: software-architect
timestamp: '2026-07-31T00:00:00Z'
---

# Software Architect Source-Aware Guide

Source-aware role bundle for software architecture, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- stakeholders, business requirements, constraints, and quality attributes
- system context, components, interfaces, data, and deployment topology
- current technology versions, dependencies, and operational evidence
- threat model, privacy, reliability, capacity, cost, and compliance requirements
- alternatives, tradeoffs, ADRs, validation, ownership, and approval

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
- Do not infer requirement priority, system behavior, compatibility, security posture, capacity, cost, or architectural approval.
- Require accountable confirmation before committing architecture, selecting vendors, changing security boundaries, approving spend, or modifying production.

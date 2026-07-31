---
type: Deliverable Guide
title: System Architecture Design Document Source-Aware Guide
description: Defines source-aware system and solution architecture documentation, evidence handling, and action boundaries.
tags:
- architecture-design
- system-design
- technical-documentation
- deliverable
resource: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
okb_bundle_id: architecture-design-doc
timestamp: '2026-07-31T00:00:00Z'
---

# System Architecture Design Document Source-Aware Guide

Source-aware deliverable bundle for architecture documentation covering stakeholders, requirements, context, views, interfaces, data, quality attributes, decisions, risks, and verification.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- system purpose, scope, stakeholders, and concerns
- functional and quality requirements
- current and target context, components, dependencies, and trust boundaries
- interfaces, contracts, data flows, storage, and lifecycle
- capacity, availability, security, privacy, operability, cost, and constraints
- alternatives, decisions, consequences, risks, validation, ownership, and approval

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
- Do not infer requirement, component behavior, interface contract, capacity, security posture, and architecture approval.
- Require accountable confirmation before committing architecture, interfaces, vendors, infrastructure, security controls, spend, or implementation without accountable technical and business review.

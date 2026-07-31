---
type: Framework
title: Continuous Delivery Source-Aware Guide
description: Defines source-aware software delivery and release readiness, evidence handling, and action boundaries.
tags:
- continuous-delivery
- software-delivery
- release-engineering
- framework
resource: https://continuousdelivery.com/principles/
okb_bundle_id: continuous-delivery
timestamp: '2026-07-31T00:00:00Z'
---

# Continuous Delivery Source-Aware Guide

Source-aware framework bundle for continuous delivery using small batches, built-in quality, automation, deployment evidence, reliability controls, and reversible change.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- product and service scope
- repository, branch, build, test, and artifact evidence
- deployment pipeline and environment configuration
- release, feature-control, rollback, and recovery procedures
- security, access, secrets, and approvals
- delivery, reliability, quality, and learning metrics with definitions

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
- Do not infer build reproducibility, test adequacy, artifact provenance, deployment readiness, rollback viability, and production impact.
- Require accountable confirmation before merging, releasing, deploying, changing pipelines or infrastructure, handling credentials, or bypassing quality and approval controls.

---
type: Role
title: Software Quality Assurance Analyst / Tester Source-Aware Guide
description: Defines source-aware software quality assurance and testing, evidence handling, and action boundaries.
tags:
- software-quality-assurance-analyst-tester
- software
- role
resource: https://www.onetonline.org/link/summary/15-1253.00
okb_bundle_id: software-quality-assurance-analyst-tester
timestamp: '2026-07-31T00:00:00Z'
---
# Software Quality Assurance Analyst / Tester Source-Aware Guide

Source-aware role bundle for software quality assurance and testing, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- requirements, risks, acceptance criteria, and traceability
- application, build, environment, browser, device, data, and dependency versions
- test plan, cases, fixtures, expected results, and coverage
- defects, severity criteria, reproducibility, logs, screenshots, and retest evidence
- security, privacy, accessibility, performance, release, and approval context

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
- Do not infer requirement coverage, defect severity, reproducibility, test result, accessibility, release readiness, or production quality.
- Do not invent an artifact owner, author, date, or version.
- Require accountable confirmation before accessing sensitive test data, changing environments, closing defects, approving releases, or claiming conformance.

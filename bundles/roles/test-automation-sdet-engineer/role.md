---
type: Role
title: Test Automation / SDET Engineer Source-Aware Guide
description: Defines source-aware test automation and SDET engineering, evidence handling, and action boundaries.
tags:
- test-automation-sdet-engineer
- test
- role
resource: https://www.onetonline.org/link/summary/15-1253.00
okb_bundle_id: test-automation-sdet-engineer
timestamp: '2026-07-31T00:00:00Z'
---
# Test Automation / SDET Engineer Source-Aware Guide

Source-aware role bundle for test automation and SDET engineering, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- requirements, risks, acceptance criteria, and test strategy
- application, build, environments, dependencies, browsers, devices, and data
- automation framework, language, runner, fixtures, selectors, contracts, and versions
- test isolation, determinism, coverage, failure artifacts, flake history, and maintenance
- CI gates, credentials, security, performance, deployment, and approval

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
- Do not infer test coverage, deterministic behavior, failure cause, flake rate, build quality, release readiness, or production state.
- Do not invent an artifact owner, author, date, or version.
- Require accountable confirmation before using production data or credentials, changing CI gates, deploying tests, closing defects, or approving releases.

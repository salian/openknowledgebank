---
type: Framework
title: Test-Driven Development Source-Aware Guide
description: Defines source-aware test-list, red-green-refactor, test design, isolation, refactoring, coverage, and delivery review, evidence handling, and action boundaries.
resource: https://martinfowler.com/bliki/TestDrivenDevelopment.html
okb_bundle_id: test-driven-development
timestamp: '2026-08-01T00:00:00Z'
---
# Test-Driven Development Source-Aware Guide

Source-aware framework bundle for test-list, red-green-refactor, test design, isolation, refactoring, coverage, and delivery review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Authoritative and Identified Sources
- https://martinfowler.com/bliki/TestDrivenDevelopment.html
- https://www.oreilly.com/library/view/test-driven-development/0321146530/

Name an applicable URL in every Source Note. Verify current version, date, scope, and applicability. Do not reproduce licensed standards or proprietary methods; disclose when a source is secondary or a licensed primary text is still required.

## Evidence Required
- requirement and behavior examples, test list, failing and passing test evidence, production code and diff, test doubles and boundaries, test command and environment, coverage meaning, refactoring evidence, CI results, owner, approvals, and rollback

## Application Sequence
1. Define the decision, scope, owner, date, and source version.
2. Inventory evidence as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile definitions, identifiers, versions, periods, scope, permissions, processing, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails
- Do not infer required behavior, test validity, failure cause, passing status, coverage adequacy, refactoring safety, or release readiness.
- Do not invent artifact provenance, access, execution, approval, or reviewer ownership.
- Require accountable confirmation before actions that edit code or tests, run commands, install dependencies, commit or merge changes, change CI, deploy software, or claim defect prevention.

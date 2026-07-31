---
type: Deliverable Guide
title: Code Review Feedback Source-Aware Guide
description: Defines source-aware change intent, correctness, security, reliability, test, compatibility, maintainability, severity, evidence, suggestion, and review-decision feedback, evidence handling, and action boundaries.
resource: https://docs.github.com/en/pull-requests/get-started/reviewing-pull-requests-quickstart
okb_bundle_id: code-review-feedback
timestamp: '2026-08-01T00:00:00Z'
---
# Code Review Feedback Source-Aware Guide

Source-aware deliverable bundle for change intent, correctness, security, reliability, test, compatibility, maintainability, severity, evidence, suggestion, and review-decision feedback, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Authoritative and Identified Sources
- https://docs.github.com/en/pull-requests/get-started/reviewing-pull-requests-quickstart
- https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews

Name an applicable URL in every Source Note. Verify current version, date, scope, and applicability. Do not reproduce licensed standards or proprietary methods; disclose when a source is secondary or a licensed primary text is still required.

## Evidence Required
- repository and branch, change request and acceptance criteria, full diff and surrounding code, language and runtime, architecture and threat context, tests and results, static or security analysis, logs, backward-compatibility requirements, deployment and rollback plan, ownership and review policy, exact file and line, reproduction evidence, confidence, and approvals

## Application Sequence
1. Define the decision, scope, owner, date, and source version.
2. Inventory evidence as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile definitions, identifiers, versions, periods, scope, permissions, processing, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails
- Do not infer change intent, runtime behavior, defect, exploitability, severity, test result, compatibility, merge eligibility, or deployment safety.
- Do not invent artifact provenance, access, execution, approval, or reviewer ownership.
- Require accountable confirmation before actions that submit review comments, approve or request changes, apply suggestions, edit code, run commands or tests, merge changes, expose private code or secrets, or deploy software.

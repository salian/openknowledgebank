---
type: Framework
title: GitOps Source-Aware Guide
description: Defines source-aware declarative desired state, versioning, pull or reconciliation, drift, policy, promotion, observability, and rollback review, evidence handling, and action boundaries.
resource: https://opengitops.dev/
okb_bundle_id: gitops
timestamp: '2026-08-01T00:00:00Z'
---
# GitOps Source-Aware Guide

Source-aware framework bundle for declarative desired state, versioning, pull or reconciliation, drift, policy, promotion, observability, and rollback review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Authoritative and Identified Sources
- https://opengitops.dev/
- https://opengitops.dev/#principles

Name an applicable URL in every Source Note. Verify current version, date, scope, and applicability. Do not reproduce licensed standards or proprietary methods; disclose when a source is secondary or a licensed primary text is still required.

## Evidence Required
- system and environment scope, desired-state repository and revision, declarative resources, reconciler and version, authentication and permissions, sync mode and interval, drift and health evidence, promotion and branch policy, secrets handling, policy checks, audit logs, incident controls, tests, approvals, and rollback revision

## Application Sequence
1. Define the decision, scope, owner, date, and source version.
2. Inventory evidence as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile definitions, identifiers, versions, periods, scope, permissions, processing, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails
- Do not infer desired or live state, drift cause, reconciliation status, deployment health, permission, policy compliance, rollback safety, or production readiness.
- Do not invent artifact provenance, access, execution, approval, or reviewer ownership.
- Require accountable confirmation before actions that merge desired-state changes, trigger or suspend reconciliation, deploy or roll back workloads, change repositories, policies, permissions, controllers, environments, or secrets.

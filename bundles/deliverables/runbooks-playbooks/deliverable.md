---
type: Deliverable Guide
title: Runbooks and Operational Playbooks Source-Aware Guide
description: Defines source-aware trigger, scope, prerequisite, diagnosis, safe procedure, verification, escalation, communication, rollback, ownership, and maintenance review, evidence handling, and action boundaries.
resource: https://sre.google/sre-book/practical-alerting/
okb_bundle_id: runbooks-playbooks
timestamp: '2026-08-01T00:00:00Z'
---
# Runbooks and Operational Playbooks Source-Aware Guide

Source-aware deliverable bundle for trigger, scope, prerequisite, diagnosis, safe procedure, verification, escalation, communication, rollback, ownership, and maintenance review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Authoritative and Identified Sources
- https://sre.google/sre-book/practical-alerting/
- https://sre.google/workbook/incident-response/

Name an applicable URL in every Source Note. Verify current version, date, scope, and applicability. Do not reproduce licensed standards or proprietary methods; disclose when a source is secondary or a licensed primary text is still required.

## Evidence Required
- service or process scope, architecture and dependencies, alert or trigger definition, access and permissions, current commands or procedures from owners, expected outputs, stop conditions, safety and data handling, escalation and communication paths, incident roles, rollback and recovery, tests or game-day evidence, version, owner, and approval

## Application Sequence
1. Define the decision, scope, owner, date, and source version.
2. Inventory evidence as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile definitions, identifiers, versions, periods, scope, permissions, processing, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails
- Do not infer system state, command behavior, access, diagnosis, procedure safety, recovery result, escalation owner, or production readiness.
- Do not invent artifact provenance, access, execution, approval, or reviewer ownership.
- Require accountable confirmation before actions that run commands, change live systems, restart or fail over services, access sensitive data, communicate incidents, page responders, deploy or roll back changes, or close incidents.

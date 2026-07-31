---
type: Framework
title: Site Reliability Engineering Source-Aware Guide
description: Defines source-aware service, SLI, SLO, error budget, toil, alerting, incident, postmortem, capacity, and reliability decision review, evidence handling, and action boundaries.
resource: https://sre.google/sre-book/introduction/
okb_bundle_id: site-reliability-engineering
timestamp: '2026-08-01T00:00:00Z'
---
# Site Reliability Engineering Source-Aware Guide

Source-aware framework bundle for service, SLI, SLO, error budget, toil, alerting, incident, postmortem, capacity, and reliability decision review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Authoritative and Identified Sources
- https://sre.google/sre-book/introduction/
- https://sre.google/sre-book/service-level-objectives/
- https://sre.google/workbook/error-budget-policy/

Name an applicable URL in every Source Note. Verify current version, date, scope, and applicability. Do not reproduce licensed standards or proprietary methods; disclose when a source is secondary or a licensed primary text is still required.

## Evidence Required
- service and user journey, owners and dependencies, SLI event and measurement specification, SLO target and window, exclusions, source telemetry and quality, error-budget calculation and policy, alert rules, incident and postmortem evidence, toil measure, capacity and change history, risks, approvals, and rollback

## Application Sequence
1. Define the decision, scope, owner, date, and source version.
2. Inventory evidence as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile definitions, identifiers, versions, periods, scope, permissions, processing, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails
- Do not infer service health, SLI or SLO value, budget consumption, alert validity, incident cause, toil, capacity, or release safety.
- Do not invent artifact provenance, access, execution, approval, or reviewer ownership.
- Require accountable confirmation before actions that change SLOs, error-budget policy, alerts, on-call or incident state, production configuration, capacity, release pace, or customer communications; deploy or roll back changes.

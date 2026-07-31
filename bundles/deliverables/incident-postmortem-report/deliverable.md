---
type: Deliverable Guide
title: Incident Postmortem Report Source-Aware Guide
description: Defines source-aware incident learning and corrective action, evidence handling, and action boundaries.
tags:
- incident-postmortem
- reliability
- root-cause-analysis
- deliverable
resource: https://sre.google/sre-book/postmortem-culture/
okb_bundle_id: incident-postmortem-report
timestamp: '2026-07-31T00:00:00Z'
---

# Incident Postmortem Report Source-Aware Guide

Source-aware deliverable bundle for blameless incident postmortems with verified timeline, impact, detection, response, contributing conditions, evidence, learning, and owned corrective actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- incident scope, severity, dates, systems, and stakeholders
- timestamped timeline and source records
- user, business, data, security, and service impact
- detection, escalation, mitigation, recovery, and communication evidence
- trigger, contributing conditions, control gaps, and uncertainty
- corrective actions, owners, priorities, due dates, verification, and closure evidence

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
- Do not infer timeline event, impact, root or contributing cause, individual intent, remediation effectiveness, and closure status.
- Require accountable confirmation before assigning blame, making legal, security, employment, or public claims, closing actions, or publishing the report without accountable review.

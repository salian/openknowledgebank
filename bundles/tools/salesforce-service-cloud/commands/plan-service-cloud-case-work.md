---
type: Slash Command
command: /plan-service-cloud-case-work
title: Plan Service Cloud Case Work
description: "Create a source-scoped Service Cloud case, routing, or automation plan without inventing Salesforce org configuration."
okb_bundle_id: salesforce-service-cloud
inputs:
  - support operations question or desired change
  - Salesforce org evidence
  - case lifecycle, queue, routing, report, automation, permission, or AI context
  - risk and approval constraints
outputs:
  - Service Cloud readiness answer
  - required org evidence
  - proposed plan or change
  - validation and rollback checklist
  - source note
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-service-cloud-case-work

Purpose: produce a Salesforce Service Cloud plan that is ready for human and administrator review, not an unsafely executed production change.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Business question, support workflow, or desired Service Cloud change.
- Salesforce org evidence, if available: setup screenshots, metadata, object schema, reports, dashboards, flow definitions, queue/routing configuration, permissions, release, licenses, or sandbox test evidence.
- Case lifecycle, channel, queue, skill, escalation, entitlement, knowledge, AI, or reporting context.
- Approval, privacy, compliance, deployment, rollback, and monitoring constraints.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to plan the work now.
2. Source note: official Salesforce source categories, user-provided org evidence, and missing verification.
3. Verified facts: what is confirmed by Salesforce sources or user-provided org evidence.
4. Missing evidence: schema, setup, routing, report, permission, release, license, or policy inputs needed.
5. Plan: proposed case/routing/reporting/automation/AI work, with assumptions labeled.
6. Risk and confirmation boundary: customer impact, data impact, automation impact, permission impact, and actions requiring explicit approval.
7. Validation and rollback: sandbox test, sample records, report reconciliation, monitoring, owner, rollback trigger, and rollback action.

## Confirmation Boundary

Do not send customer communications, export data, modify records, deploy or activate automation, change routing or queues, change permissions, run API calls, or enable AI/customer-facing behavior without explicit user confirmation and authorized access.

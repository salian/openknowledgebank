---
type: Slash Command
command: /plan-hubspot-sales-work
title: Plan HubSpot Sales Work
description: "Create a source-scoped HubSpot Sales Hub CRM, pipeline, outreach, automation, or reporting plan without inventing portal configuration."
okb_bundle_id: hubspot-sales-hub
inputs:
  - sales operations question or desired HubSpot change
  - HubSpot portal evidence
  - object, property, pipeline, sequence, workflow, report, permission, or API context
  - risk and approval constraints
outputs:
  - HubSpot readiness answer
  - required portal evidence
  - proposed plan or change
  - validation and rollback checklist
  - source note
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-hubspot-sales-work

Purpose: produce a HubSpot Sales Hub plan that is ready for human, RevOps, and administrator review, not an unsafely executed CRM change or sales communication.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Business question, sales workflow, report discrepancy, or desired Sales Hub change.
- HubSpot portal evidence, if available: settings screenshots, property exports, pipeline configuration, record samples, workflow definitions, sequence settings, reports, dashboards, permissions, seat/edition evidence, API metadata, or sandbox/test evidence.
- Object, property, association, pipeline, stage, owner/team, sequence, workflow, report, forecast, quote, integration, or API context.
- Approval, privacy, consent, deliverability, compliance, deployment, rollback, and monitoring constraints.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to plan the work now.
2. Source note: official HubSpot source categories, user-provided portal evidence, and missing verification.
3. Verified facts: what is confirmed by HubSpot sources or user-provided portal evidence.
4. Missing evidence: schema, setup, sequence, workflow, report, permission, seat, API, consent, or policy inputs needed.
5. Plan: proposed CRM, pipeline, reporting, automation, outreach, or integration work, with assumptions labeled.
6. Risk and confirmation boundary: customer impact, data impact, automation impact, permission impact, communication impact, and actions requiring explicit approval.
7. Validation and rollback: test records, sandbox or limited rollout if available, report reconciliation, monitoring, owner, rollback trigger, and rollback action.

## Confirmation Boundary

Do not send messages, enroll contacts, export data, modify records, activate workflows, change pipelines, change permissions, alter quotes/payments, run API calls, or change integrations without explicit user confirmation and authorized access.

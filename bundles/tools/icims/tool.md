---
type: "Tool Guide"
title: "iCIMS"
description: "Source-aware guidance for iCIMS."
resource: "https://www.icims.com/"
okb_bundle_id: icims
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Enterprise applicant tracking and talent acquisition platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "collect candidate data, source or rank candidates, change applications, schedule interviews, issue offers, onboard hires, send messages, export data, or make employment decisions"
---
# iCIMS Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.icims.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable iCIMS talent acquisition configuration and decision review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before collect candidate data, source or rank candidates, change applications, schedule interviews, issue offers, onboard hires, send messages, export data, or make employment decisions.

## Guardrails

- Do not invent candidate identity, consent, application state, qualification, ranking, interview result, offer, hiring outcome, onboarding, fairness, legal compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

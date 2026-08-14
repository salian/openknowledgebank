---
type: "Tool Guide"
title: "Lever"
description: "Source-aware guidance for Lever."
resource: "https://www.lever.co/"
okb_bundle_id: lever
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Applicant tracking, candidate relationship, and recruiting analytics platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "collect or enrich candidate data, change applications, schedule interviews, submit feedback, issue offers, automate communications, export records, or make employment decisions"
---
# Lever Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.lever.co/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Lever recruiting workflow and employment-decision review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before collect or enrich candidate data, change applications, schedule interviews, submit feedback, issue offers, automate communications, export records, or make employment decisions.

## Guardrails

- Do not invent candidate identity, consent, application or opportunity state, qualification, interview feedback, ranking, offer, hiring outcome, fairness, legal compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

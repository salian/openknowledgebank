---
type: "Tool Guide"
title: "Microsoft Clarity"
description: "Source-aware guidance for Microsoft Clarity."
resource: "https://learn.microsoft.com/en-us/clarity/"
okb_bundle_id: microsoft-clarity
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Behavior analytics, session replay, heatmap, and insight platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "install tracking, record sessions, collect or reveal user data, change masking or consent configuration, invite users, export data, connect integrations, or represent behavior, causality, conversion, privacy, or compliance"
---
# Microsoft Clarity Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://learn.microsoft.com/en-us/clarity/
- https://clarity.microsoft.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Microsoft Clarity instrumentation and privacy review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before install tracking, record sessions, collect or reveal user data, change masking or consent configuration, invite users, export data, connect integrations, or represent behavior, causality, conversion, privacy, or compliance.

## Guardrails

- Do not invent visitor identity, consent, masking effectiveness, captured content, session completeness, metric accuracy, behavior intent, funnel conversion, Copilot accuracy, data retention, legal compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

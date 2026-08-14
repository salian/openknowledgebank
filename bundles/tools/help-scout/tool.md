---
type: "Tool Guide"
title: "Help Scout"
description: "Source-aware guidance for Help Scout."
resource: "https://www.helpscout.com/features/"
okb_bundle_id: help-scout
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Customer support inbox, knowledge, messaging, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "reply to customers, change conversation state, edit profiles, publish Docs, deploy Beacon or Messages, enable AI Answers, change access, export data, or represent resolution or performance"
---
# Help Scout Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.helpscout.com/features/
- https://docs.helpscout.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current Help Scout product and Docs documentation for the plan and enabled products.
- Mailbox, channel, conversation, customer, workflow, tag, profile, Beacon, Docs, AI source, message, role, integration, and report state.
- Customer privacy, message authority, test, monitoring, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Help Scout support configuration and automation review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before reply to customers, change conversation state, edit profiles, publish Docs, deploy Beacon or Messages, enable AI Answers, change access, export data, or represent resolution or performance.

## Guardrails

- Do not invent customer identity, conversation ownership or state, response accuracy, message delivery, knowledge validity, AI answer, resolution, CSAT, report result, privacy compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

---
type: "Tool Guide"
title: "Fullstory"
description: "Source-aware guidance for Fullstory."
resource: "https://www.fullstory.com/platform/"
okb_bundle_id: fullstory
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Behavioral data, digital experience analytics, replay, product analytics, and activation platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "enable capture, change masking or identity, replay sessions, export behavioral data, create guides or surveys, activate personalization, connect MCP, or represent behavior or outcomes"
---
# Fullstory Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.fullstory.com/platform/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Fullstory configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before enable capture, change masking or identity, replay sessions, export behavioral data, create guides or surveys, activate personalization, connect MCP, or represent behavior or outcomes.

## Guardrails

- Do not invent user identity, consent, capture completeness, masking effectiveness, session interpretation, metric definition, fraud signal, causal effect, conversion, personalization result, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

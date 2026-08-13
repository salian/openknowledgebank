---
type: "Tool Guide"
title: "Discord Developer Platform"
description: "Source-aware guidance for Discord Developer Platform."
resource: "https://docs.discord.com/developers/intro"
okb_bundle_id: discord
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Community communication and application platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or install applications or bots, issue tokens, read or send messages, change roles or moderation, access member data, invoke webhooks, or represent delivery or authorization"
---
# Discord Developer Platform Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.discord.com/developers/intro

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Discord Developer Platform configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or install applications or bots, issue tokens, read or send messages, change roles or moderation, access member data, invoke webhooks, or represent delivery or authorization.

## Guardrails

- Do not invent server ownership, member identity or consent, message context, permission, moderation basis, bot or webhook action, delivery, community outcome, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

---
type: "Tool Guide"
title: "FigJam"
description: "Source-aware guidance for FigJam."
resource: "https://help.figma.com/hc/en-us/articles/1500004362321-Guide-to-FigJam"
okb_bundle_id: figjam
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Collaborative online whiteboard for meetings, brainstorming, diagrams, and research"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or edit boards, import research, invite participants, run votes, publish templates, share externally, or represent consensus or decisions"
---
# FigJam Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://help.figma.com/hc/en-us/articles/1500004362321-Guide-to-FigJam

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable FigJam configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or edit boards, import research, invite participants, run votes, publish templates, share externally, or represent consensus or decisions.

## Guardrails

- Do not invent participant identity, content ownership, consent, vote validity, consensus, decision status, sharing scope, accessibility, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

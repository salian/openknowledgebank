---
type: "Tool Guide"
title: "Avid Media Composer"
description: "Source-aware guidance for Avid Media Composer."
resource: "https://www.avid.com/media-composer"
okb_bundle_id: avid-media-composer
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Professional video editing system"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "modify shared projects or sequences, relink or delete media, render or export masters, publish content, overwrite files, or represent rights or quality approval"
---
# Avid Media Composer Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.avid.com/media-composer

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Avid Media Composer configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before modify shared projects or sequences, relink or delete media, render or export masters, publish content, overwrite files, or represent rights or quality approval.

## Guardrails

- Do not invent media ownership, release status, sequence intent, codec compatibility, render result, broadcast or accessibility compliance, publication, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

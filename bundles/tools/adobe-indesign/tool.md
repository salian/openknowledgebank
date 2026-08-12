---
type: "Tool Guide"
title: "Adobe InDesign"
description: "Source-aware guidance for Adobe InDesign."
resource: "https://developer.adobe.com/indesign/"
okb_bundle_id: adobe-indesign
timestamp: "2026-08-12T00:00:00Z"
tool_category: "Creative publishing software"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "run scripts or plugins, modify source documents, package or export files, embed fonts or assets, publish output, or represent rights clearance"
---
# Adobe InDesign Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developer.adobe.com/indesign/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Adobe InDesign configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before run scripts or plugins, modify source documents, package or export files, embed fonts or assets, publish output, or represent rights clearance.

## Guardrails

- Do not invent document state, source ownership, font or asset rights, link state, preflight result, export fidelity, publication, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

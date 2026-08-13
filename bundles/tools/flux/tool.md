---
type: "Tool Guide"
title: "FLUX"
description: "Source-aware guidance for FLUX."
resource: "https://docs.bfl.ai/"
okb_bundle_id: flux
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Generative image model API and editing platform from Black Forest Labs"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "submit prompts or images, generate or edit imagery, process people or brands, retrieve outputs, store or publish assets, or represent provenance or rights"
---
# FLUX Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.bfl.ai/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable FLUX configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before submit prompts or images, generate or edit imagery, process people or brands, retrieve outputs, store or publish assets, or represent provenance or rights.

## Guardrails

- Do not invent model availability, prompt interpretation, person identity, consent, likeness, trademark, copyright, output provenance, safety, quality, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

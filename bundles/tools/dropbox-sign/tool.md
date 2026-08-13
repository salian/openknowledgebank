---
type: "Tool Guide"
title: "Dropbox Sign"
description: "Source-aware guidance for Dropbox Sign."
resource: "https://sign.dropbox.com/products/dropbox-sign-api"
okb_bundle_id: dropbox-sign
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Electronic signature platform and API"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "send or cancel signature requests, create embedded or public signing flows, change documents or recipients, authenticate signers, countersign, expose API credentials, retain or delete records, or represent enforceability"
---
# Dropbox Sign Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://sign.dropbox.com/products/dropbox-sign-api

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Dropbox Sign configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before send or cancel signature requests, create embedded or public signing flows, change documents or recipients, authenticate signers, countersign, expose API credentials, retain or delete records, or represent enforceability.

## Guardrails

- Do not invent document intent, signer identity or authority, consent, jurisdictional suitability, legal enforceability, callback or completion state, record integrity, retention obligation, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

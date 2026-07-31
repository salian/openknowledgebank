---
type: Tool Guide
title: "Adobe Acrobat / Adobe Document Cloud"
description: "Defines source-aware PDF document workflows, evidence handling, and action boundaries."
tool_category: "General office productivity, document creation/editing, and e-signature software"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review PDF document workflows from supplied evidence."
  - "Draft a acrobat document workflow brief with explicit evidence states."
confirmation_required:
  - "signing, sending, sharing, redacting, certifying, changing permissions, overwriting originals, or publishing documents"
okb_bundle_id: adobe-acrobat-document-cloud
timestamp: "2026-07-31T00:00:00Z"
---

# Adobe Acrobat / Adobe Document Cloud

Source-aware tool bundle for Adobe Acrobat and Document Cloud PDF creation, review, forms, signatures, OCR, accessibility, redaction, and controlled delivery.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- source document and authoritative version
- PDF structure, metadata, forms, and attachments
- signature and certificate requirements
- OCR, accessibility, and reading-order evidence
- redaction and sensitive-data requirements
- permissions, sharing, and review state
- export, retention, and delivery specifications

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before signing, sending, sharing, redacting, certifying, changing permissions, overwriting originals, or publishing documents.

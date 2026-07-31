---
type: Tool Guide
title: "Postman"
description: "Defines source-aware API development and testing, evidence handling, and action boundaries."
tool_category: "API client / lifecycle platform"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review API development and testing from supplied evidence."
  - "Draft a postman api workflow brief with explicit evidence states."
confirmation_required:
  - "sending state-changing requests, exposing credentials, changing collections or environments, running monitors, exporting data, or publishing APIs"
okb_bundle_id: postman
timestamp: "2026-07-31T00:00:00Z"
---

# Postman

Source-aware tool bundle for Postman API definitions, collections, environments, requests, tests, runs, monitors, and controlled API workflow briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- workspace and collection scope
- API definition and endpoint documentation
- environment and variable resolution
- authentication and authorization requirements
- request, example, script, and test definitions
- runner, monitor, flow, or CLI results
- data handling and change approvals

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before sending state-changing requests, exposing credentials, changing collections or environments, running monitors, exporting data, or publishing APIs.

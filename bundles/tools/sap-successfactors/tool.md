---
type: Tool Guide
title: "SAP SuccessFactors"
description: "Defines source-aware human-capital management system analysis and administration, evidence handling, and action boundaries."
tool_category: "HR information systems, payroll, and applicant tracking systems"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review human-capital management system analysis and administration from supplied evidence."
  - "Draft a successfactors analysis and change brief with explicit evidence states."
confirmation_required:
  - "viewing or exporting restricted HR data, changing records, permissions, workflows, rules, integrations, compensation, recruiting, or employee status"
okb_bundle_id: sap-successfactors
timestamp: "2026-07-31T00:00:00Z"
---

# SAP SuccessFactors

Source-aware tool bundle for SAP SuccessFactors tenant, module, employee, workflow, integration, permission, reporting, and controlled HR-system briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- tenant, data center, release, and module scope
- business configuration and effective dates
- OData metadata, entities, fields, and API version
- role-based permissions and target populations
- workflow, rule, event, and integration configuration
- employee, compensation, recruiting, or learning data definitions
- audit, test, privacy, and approval evidence

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before viewing or exporting restricted HR data, changing records, permissions, workflows, rules, integrations, compensation, recruiting, or employee status.

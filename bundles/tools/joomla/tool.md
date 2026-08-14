---
type: "Tool Guide"
title: "Joomla"
description: "Source-aware guidance for Joomla."
resource: "https://6.joomla.org/"
okb_bundle_id: joomla
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source multilingual content management system"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "install or update Joomla, extensions or templates, edit or publish content, change access, authentication, URLs or caching, run migrations, restore backups, or represent security or availability"
---
# Joomla Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://6.joomla.org/
- https://docs.joomla.org/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Joomla site architecture and publishing review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before install or update Joomla, extensions or templates, edit or publish content, change access, authentication, URLs or caching, run migrations, restore backups, or represent security or availability.

## Guardrails

- Do not invent version compatibility, extension safety, content ownership, publication, translation, accessibility, permission, authentication, SEO result, backup validity, security, uptime, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.

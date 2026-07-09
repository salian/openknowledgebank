---
type: Tool Guide
title: DocuSign
description: "Defines safe, source-aware use of DocuSign in OpenKnowledgeBank bundles."
tool_category: "E-signature and agreement workflow platform"
okb_bundle_id: docusign
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - Plan DocuSign eSignature envelope, template, recipient, routing, field, reporting, and integration work from user-provided account evidence.
  - Review proposed DocuSign changes for source scope, recipient impact, legal/compliance caveats, validation, and rollback.
  - Explain DocuSign concepts using official DocuSign source categories.
confirmation_required:
  - Send envelopes, reminders, or recipient notifications.
  - Correct, void, resend, bulk-send, export, delete, or otherwise modify envelopes, templates, recipients, documents, tabs/fields, brands, permissions, reports, or agreement data.
  - Create, activate, deploy, or change Connect/webhook behavior, integrations, embedded signing flows, identity/authentication settings, API-connected behavior, or production account settings.
timestamp: "2026-07-09T00:00:00Z"
---

# DocuSign Tool Guide

DocuSign is an e-signature and agreement workflow platform. In this bundle, treat DocuSign as a source-sensitive system where official product/API behavior and the user's local account configuration must be kept separate.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## What This Bundle Is For

- Planning DocuSign eSignature envelope, template, recipient, routing, field, sending, status, reporting, and integration work.
- Turning DocuSign questions into source-scoped evidence requests.
- Reviewing planned changes before they affect recipients, counterparties, employees, customers, agreement records, templates, notifications, audit trails, integrations, or production workflows.
- Supporting role bundles that work with sales, legal, HR, procurement, operations, real estate, contract management, and customer onboarding.

## What This Bundle Is Not

- A complete DocuSign implementation guide.
- A current account schema, endpoint, pricing, seat, edition, feature limit, legal enforceability, retention, privacy, compliance, or release reference.
- A substitute for DocuSign administrator, developer, legal, security, privacy, procurement, records-management, compliance, or change-management review.
- A claim that the agent has access to the user's DocuSign account.

## Source Discipline

Use exact DocuSign facts only when grounded in official DocuSign documentation or user-provided account evidence. Treat the following as local evidence requirements:

- account, edition, product, permission, user, group, brand, notification, identity/authentication, and enabled-feature evidence;
- template, envelope, document, recipient, role, routing/signing-order, tab/field, conditional logic, reminder, expiration, and sender evidence;
- legal, compliance, consent, privacy, retention, audit, data-classification, and records-management requirements;
- status, report, export, completion certificate, audit trail, dashboard, and reconciliation evidence;
- integration key, app, OAuth/JWT flow, API version, scope, endpoint, payload, Connect/webhook, embedded signing, callback, sandbox/demo, and production evidence.

## DocuSign Guardrails

- Treat DocuSign product pages, Support Center, Developer Center, and API references as source categories, not proof of a user's local configuration.
- Verify the DocuSign account before recommending template roles, recipient routing, field placement, authentication, notification, sending, reporting, export, Connect, embedded signing, or API behavior.
- Separate demo/sandbox evidence from production evidence when available.
- Explain when a recommendation is a design hypothesis rather than a source-confirmed implementation step.
- Require explicit confirmation before live sends, reminders, corrections, voids, template changes, exports, recipient/routing/field changes, permission changes, integration changes, webhook changes, embedded signing changes, or API actions.
- Defer legal enforceability, consent, retention, privacy, and regulated-workflow conclusions to qualified legal/compliance review.

## Source Note Template

```text
Source note: DocuSign guidance is based on official DocuSign source categories for [product page / Support Center / Developer Center / eSignature REST API / legal or commercial source]. Local evidence used: [account setting, template, envelope, recipient, routing, field, notification, permission, report, audit, integration, sandbox, or production evidence provided by user]. Missing before action or conclusion: [current doc check, account verification, recipient/legal/compliance approval, security/privacy review, sandbox/test evidence, owner confirmation, rollback].
```

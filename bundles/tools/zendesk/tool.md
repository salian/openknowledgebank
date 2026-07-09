---
type: Tool Guide
title: Zendesk
description: "Defines safe, source-aware use of Zendesk Support, Suite, Help Center, AI agents, and APIs in OpenKnowledgeBank bundles."
tool_category: "Customer support, helpdesk, and ticketing platform"
okb_bundle_id: zendesk
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
  - Plan Zendesk ticketing, routing, reporting, Help Center, AI agent, or automation work from user-provided account evidence.
  - Review proposed Zendesk changes for source scope, risks, validation, and rollback.
  - Explain Zendesk concepts using official Zendesk documentation categories.
confirmation_required:
  - Send customer communications or publish Help Center content.
  - Export, update, delete, merge, or bulk-modify Zendesk tickets, users, organizations, or other customer data.
  - Create, activate, deploy, or change triggers, automations, macros, views, SLAs, routing, groups, organizations, permissions, apps, integrations, APIs, or AI/customer-facing behavior.
  - Run API calls or access sensitive customer data.
timestamp: "2026-07-09T00:00:00Z"
---

# Zendesk Tool Guide

Zendesk is a customer support platform for ticketing, customer service workflows, knowledge, AI agents, reporting, and integrations. Official Zendesk source categories include Zendesk Help for product behavior and Zendesk Developer documentation for API behavior.

## What This Bundle Is For

- Planning Zendesk ticket lifecycle, triage, routing, SLA, macro, view, trigger, automation, Help Center, AI agent, report, and API work.
- Turning support operations questions into source-scoped Zendesk evidence requests.
- Reviewing planned changes before they affect customers, agents, data, routing, permissions, automations, reporting, or production integrations.
- Supporting role bundles that work with customer support, contact centers, customer success, CX operations, support engineering, support analytics, or integrations.

## What This Bundle Is Not

- A complete Zendesk implementation, migration, data model, API, pricing, packaging, add-on, limit, release, or marketplace reference.
- A substitute for Zendesk administrator, support operations, security, privacy, legal, compliance, AI governance, accessibility, procurement, or change-management review.
- A claim that the agent has access to the user's Zendesk account.

## Source Discipline

Use exact Zendesk facts only when grounded in official Zendesk documentation or user-provided account evidence. Treat the following as local evidence requirements:

- account subdomain, products, plan, add-ons, brands, channels, enabled features, and release context;
- ticket fields, forms, statuses, tags, groups, organizations, users, roles, permissions, data classifications, and retention settings;
- view, macro, trigger, automation, SLA, routing, skill, queue, AI agent, app, webhook, and integration configuration;
- Help Center, knowledge base, article, locale, user segment, permission, and publishing evidence;
- Explore/report/dashboard dataset, metric, filter, time zone, owner, sharing, and schedule evidence;
- API version, auth scope, integration user, endpoint, payload, pagination, rate-limit, and app evidence.

## Zendesk Guardrails

- Treat Zendesk Help and Zendesk Developer documentation as source categories, not proof of a user's local configuration.
- Verify the Zendesk account before recommending field names, trigger ordering, automation criteria, macro content, routing logic, report filters, permissions, AI behavior, or API syntax.
- Separate sandbox or test evidence from production evidence.
- Explain when a recommendation is a design hypothesis rather than a source-confirmed implementation step.
- Require explicit confirmation before live changes, customer communications, data exports, automation activation, routing changes, permission changes, integrations, or AI/customer-facing deployment.

## Source Note Template

```text
Source note: Zendesk guidance is based on official Zendesk source categories for [Help / Developer docs / release or product docs / commercial or packaging pages]. Local evidence used: [account setup, Admin Center screenshots, exports, ticket schema, reports, dashboards, trigger/automation/macro/view/routing/AI configuration, API docs, or tests provided by user]. Missing before action or conclusion: [current doc/version check, account verification, sandbox test, approval, rollback, security/privacy/compliance/AI review].
```

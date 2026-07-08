---
type: Tool Guide
title: Salesforce Service Cloud
description: "Defines safe, source-aware use of Salesforce Service Cloud and Agentforce Service in OpenKnowledgeBank bundles."
tool_category: "Customer service CRM and support operations platform"
okb_bundle_id: salesforce-service-cloud
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
  - Plan case triage, routing, reporting, knowledge, or automation work from user-provided org evidence.
  - Review proposed Service Cloud changes for source scope, risks, validation, and rollback.
  - Explain Service Cloud concepts using official Salesforce documentation categories.
confirmation_required:
  - Send customer communications or publish knowledge.
  - Export, update, delete, or bulk-modify Salesforce data.
  - Create, activate, deploy, or change flows, assignment rules, escalation rules, entitlements, milestones, queues, skills, presence statuses, permissions, integrations, or AI/customer-facing behavior.
  - Run API calls or access sensitive customer data.
timestamp: "2026-07-09T00:00:00Z"
---

# Salesforce Service Cloud Tool Guide

Salesforce Service Cloud is a Salesforce customer service platform for support operations. Current Salesforce materials also use the Agentforce Service framing for service workflows that combine human agents, AI agents, CRM data, and service tooling.

## What This Bundle Is For

- Planning Service Cloud case management, routing, knowledge, reporting, and automation work.
- Turning support operations questions into source-scoped Salesforce evidence requests.
- Reviewing planned changes before they affect customers, agents, data, routing, permissions, or production automation.
- Supporting role bundles that work with customer support, contact centers, customer success, CX operations, Salesforce administration, support analytics, or integrations.

## What This Bundle Is Not

- A complete Salesforce implementation guide.
- A current object, field, API, pricing, edition, license, limit, or release reference.
- A substitute for Salesforce admin, architect, security, privacy, legal, compliance, or change-management review.
- A claim that the agent has access to the user's Salesforce org.

## Source Discipline

Use exact Salesforce facts only when grounded in official Salesforce documentation or user-provided org evidence. Treat the following as local evidence requirements:

- org, cloud, edition, license, release, package, and enabled feature evidence;
- object, field, record type, page layout, permission, sharing, and data classification evidence;
- queue, skill, presence status, routing, assignment rule, escalation rule, entitlement, milestone, and Flow evidence;
- report, dashboard, report type, filter, ownership, sharing, time zone, and metric definition evidence;
- API version, auth scope, integration user, endpoint, payload, and limit evidence;
- AI grounding, prompt/action configuration, handoff, test, escalation, and approval evidence.

## Service Cloud Guardrails

- Treat Salesforce Help and Salesforce Developers documentation as source categories, not proof of a user's local configuration.
- Verify the Salesforce org before recommending field names, queue names, routing logic, flow behavior, report filters, permission changes, or API syntax.
- Separate sandbox evidence from production evidence.
- Explain when a recommendation is a design hypothesis rather than a source-confirmed implementation step.
- Require explicit confirmation before live changes, customer communications, data exports, automation activation, routing changes, permission changes, integrations, or AI/customer-facing deployment.

## Source Note Template

```text
Source note: Salesforce Service Cloud guidance is based on official Salesforce source categories for [Help / Developers docs / release notes / pricing or packaging]. Local evidence used: [org setup, metadata, schema, report, dashboard, flow, queue, permission, contract, or test evidence provided by user]. Missing before action or conclusion: [current doc/version check, org verification, sandbox test, approval, rollback, security/privacy/compliance review].
```

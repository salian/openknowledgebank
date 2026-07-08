---
type: Tool Guide
title: SAP S/4HANA
description: "Defines safe, source-aware use of SAP S/4HANA in OpenKnowledgeBank bundles."
tool_category: "Enterprise resource planning platform"
okb_bundle_id: sap-s4hana
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
  - Plan fit-gap analysis from official SAP documentation and user-provided customer scope evidence.
  - Review process, reporting, integration, migration, or authorization questions at an evidence-first level.
  - Explain SAP S/4HANA concepts using official source categories and explicit edition/release caveats.
confirmation_required:
  - Change configuration, master data, business roles, authorizations, transports, workflows, integrations, APIs, or extensions.
  - Post, reverse, approve, release, close, settle, run, or mass-update transactions.
  - Export, upload, migrate, replicate, or delete business data.
  - Make security, audit, compliance, tax, statutory, or production cutover decisions.
timestamp: "2026-07-09T00:00:00Z"
---

# SAP S/4HANA Tool Guide

SAP S/4HANA is SAP's enterprise resource planning product family. SAP describes SAP S/4HANA Cloud Public Edition as a cloud ERP solution for core processes including finance, supply chain, HR, and sales, and SAP Help Portal provides product documentation for public cloud, private cloud, and on-premise variants.

## What This Bundle Is For

- Planning SAP S/4HANA fit-gap conversations before making implementation claims.
- Turning a business process question into an evidence checklist for edition, release, activated scope, configuration, roles, data, integrations, and reporting definitions.
- Reviewing SAP reporting or reconciliation answers without assuming which source, ledger, company code, plant, document type, or process variant is authoritative.
- Supporting adjacent role bundles that touch ERP processes.

## What This Bundle Is Not

- A complete SAP configuration, ABAP, Fiori, authorization, migration, data model, or API reference.
- A substitute for SAP Help Portal, SAP Business Accelerator Hub, customer system inspection, or implementation partner review.
- A claim that the agent has access to the user's SAP tenant, Fiori launchpad, customizing, transports, logs, APIs, or data.

## Source Discipline

Use exact SAP S/4HANA facts only when grounded in official SAP documentation or user-provided local evidence. Treat the following as local evidence requirements:

- deployment model, edition, release, localization, activated scope, and licensed capabilities;
- company codes, ledgers, plants, sales organizations, purchasing organizations, document types, number ranges, tax settings, and approval workflows;
- Fiori app names, app IDs, business catalogs, business roles, authorizations, and launchpad access;
- integration flows, communication arrangements, APIs, events, middleware, and credentials;
- CDS views, analytical queries, custom fields, extensions, reports, extracts, and source-of-record definitions;
- migration objects, data quality checks, cutover plans, and reconciliation reports.

## SAP S/4HANA Guardrails

- Ask for the specific S/4HANA edition and release before giving edition-sensitive guidance.
- Separate official SAP-standard behavior from customer-specific configuration, custom code, extensions, and process variants.
- Require inspection of local configuration, scope, role, integration, and data evidence before recommending a change.
- Require explicit confirmation before any live SAP action, especially postings, releases, approvals, master-data changes, role changes, exports, integrations, or transports.

## Source Note Template

```text
Source note: SAP S/4HANA guidance is based on official SAP source categories for product scope, help documentation, implementation guidance, and APIs/integration assets. Local evidence used: [edition/release/scope/configuration/role/API/report/process evidence provided by user]. Missing before final recommendation or action: [tenant inspection, configuration activity, app/role evidence, data sample, integration contract, approval, or SAP partner/security review].
```

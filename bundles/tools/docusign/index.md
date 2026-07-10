---
type: Bundle Index
title: DocuSign
description: "Tool bundle for source-aware DocuSign eSignature agreement workflow, envelope, template, recipient, routing, and integration planning."
schema_version: "0.1.0"
bundle_format: okf-compatible
category: tools
tags:
  - docusign
  - esignature
  - agreement-workflows
  - envelopes
  - templates
  - integrations
aliases:
  - DocuSign eSignature
  - Docusign
problems_solved:
  - Plan DocuSign eSignature work without inventing account configuration, template roles, recipients, fields, routing, permissions, or API behavior.
  - Separate official DocuSign product/API behavior from user-provided account evidence and assumptions.
  - Review envelope, template, recipient, routing, notification, integration, and webhook changes with explicit confirmation boundaries.
  - Produce DocuSign plans that include source notes, validation checks, legal/compliance caveats, and rollback before live agreement changes.
industries:
  - sales
  - legal
  - human-resources
  - procurement
  - operations
  - real-estate
tools:
  - DocuSign
  - DocuSign eSignature
  - DocuSign Developer Center
  - DocuSign Support Center
frameworks:
  - verify-first agreement workflow planning
  - source-scoped recipient and routing review
  - production-change confirmation boundary
deliverables:
  - DocuSign change plan
commands:
  - /plan-docusign-agreement-work
skills: []
evaluations:
  - DocuSign plan quality check
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
adjacent_bundles:
  - hubspot-sales-hub
  - salesforce-service-cloud
contributors:
  - OpenKnowledgeBank
maintainers:
  - OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
  - "Not a complete DocuSign implementation, account administration, API, pricing, edition, feature limit, legal enforceability, retention, privacy, or compliance reference."
  - "Requires user-provided DocuSign account evidence before final conclusions about templates, envelopes, recipients, routing, fields, notifications, permissions, brands, identity/authentication settings, reports, exports, integrations, webhooks, or API behavior."
  - "Does not replace DocuSign administrator, developer, legal, security, privacy, procurement, records-management, compliance, or change-management review."
safety_notes:
  - "Require explicit confirmation before sending envelopes, notifying recipients, correcting or voiding envelopes, changing templates, editing recipient/routing/field settings, exporting agreement data, or running production integration/API actions."
  - "Do not request credentials or claim DocuSign account access unless the user provides authorized tool access or evidence."
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 25
  okb_score: 30
  absolute_lift: 5
  task_scores:
    - task: analysis-plan-without-access
      baseline_score: 7
      okb_score: 9
      max_score: 12
    - task: configuration-risk-review
      baseline_score: 11
      okb_score: 9
      max_score: 12
    - task: metric-or-report-reconciliation
      baseline_score: 7
      okb_score: 12
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 25/36 to 30/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
okb_bundle_id: docusign
timestamp: "2026-07-09T00:00:00Z"
---

# DocuSign

This bundle helps an agent use DocuSign as a source-aware e-signature and agreement workflow tool. It is designed for envelope and template planning, recipient and routing review, field/tab checks, sending readiness, status/report reconciliation, and integration or webhook planning.

It is a companion tool bundle, not a replacement for legal, compliance, security, privacy, records-management, DocuSign administrator, developer, sales operations, HR operations, procurement, or real estate transaction role bundles.

## Required Answer Habit

For source-sensitive DocuSign work, include a short **Source note** naming the official DocuSign source category, the user-provided account or agreement evidence used, and missing evidence required before acting or treating a conclusion as final.

## Start Here

- [tool.md](tool.md)
- [commands/plan-docusign-agreement-work.md](commands/plan-docusign-agreement-work.md)
- [workflows/plan-envelope-template-and-routing.md](workflows/plan-envelope-template-and-routing.md)
- [workflows/review-docusign-integration-and-webhooks.md](workflows/review-docusign-integration-and-webhooks.md)
- [deliverables/docusign-change-plan.md](deliverables/docusign-change-plan.md)
- [evaluations/docusign-plan-quality-check.md](evaluations/docusign-plan-quality-check.md)
- [references/source-checks.md](references/source-checks.md)

## Official Source Categories

Use current DocuSign product pages, DocuSign Support Center, DocuSign Developer Center, eSignature REST API documentation, and user-provided DocuSign account evidence. Do not invent account IDs, template IDs, recipient roles, recipient emails, routing order, field placement, authentication requirements, notification settings, Connect/webhook events, API payloads, legal conclusions, or retention/compliance behavior.

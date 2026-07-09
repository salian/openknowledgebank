---
type: Bundle Index
title: Technical Product Manager
description: Entry point for the Technical Product Manager OpenKnowledge bundle.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags: [technical-product-management, product-management, api-products, platform-products, requirements, roadmap, engineering-alignment]
aliases: [TPM, technical PM, platform product manager, API product manager, developer product manager]
problems_solved:
  - draft technical product requirements
  - review API and platform changes
  - map technical dependencies and risks
  - translate engineering constraints into product decisions
  - align roadmap choices with technical feasibility
industries: [software, saas, digital-products, platform-products, developer-tools, internal-tools]
tools: [Jira, Linear, Confluence, Notion, Figma, FigJam, Miro, Postman, OpenAPI, GitHub, GitLab, LaunchDarkly, Datadog, Grafana, Amplitude, Mixpanel, Productboard, Aha!]
frameworks: [Jobs-to-be-Done, RICE prioritization, opportunity solution tree, API-first design, RFC, ADR, progressive delivery, dependency mapping, Scrum, Kanban, OKRs]
deliverables: [technical PRD, API change brief, dependency map, feasibility memo, launch readiness note, technical decision memo]
commands: [/draft-technical-prd, /review-api-change, /map-dependencies]
skills: []
evaluations: [technical-product-management-quality-check]
okb_bundle_id: technical-product-manager
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles: [agile, figma, gdpr, jira, okrs, product-manager, soc-2, wcag]
adjacent_bundles: [product-manager, product-designer]
contributors: [OpenKnowledgeBank]
maintainers: [OpenKnowledgeBank]
standard_mappings:
  onet_soc: ["11-3021.00"]
  soc: ["11-3021"]
  isco_08: ["1330"]
  esco: ["1330.6"]
limitations:
  - Technical product management scope varies by organization; verify local ownership, decision rights, engineering process, and source-of-record artifacts.
  - Does not replace accountable engineering, architecture, security, privacy, accessibility, legal, finance, medical, or regulated-domain review.
  - Does not include tool-specific API automation or workspace-specific configuration details.
  - Taxonomy mappings come from the reviewed generator candidate and should be treated as context, not a complete definition of modern technical product management.
safety_notes:
  - Confirm before modifying live product docs, tickets, repositories, API specs, analytics definitions, feature flags, release notes, roadmap systems, or customer communications.
  - Treat source code, logs, incidents, customer data, product strategy, roadmap plans, technical designs, and telemetry as confidential unless the user confirms they are safe to use.
  - Escalate legal, privacy, security, accessibility, medical, financial, employment, and regulated-industry requirements to appropriate experts.
evaluation_summary:
  status: blocked
  last_evaluated: "2026-07-09"
  method: baseline-vs-okb-rubric planned
  tasks_count: 3
  display_summary: Measured evaluation is planned but blocked until evaluator execution and reviewer scoring are completed.
  evidence_note: No measured score is claimed. Private evaluation plan and blocker are retained in the publication run.
timestamp: 2026-07-09T00:00:00Z
---

# Technical Product Manager

This bundle helps an agent support technical product-management work: turning customer, business, product, and engineering evidence into technically credible requirements, API/platform decisions, dependency plans, rollout notes, and stakeholder-ready product artifacts.

## Core Concepts

- [Role](role.md)
- [Operating Principles](operating-principles.md)
- [Responsibilities](responsibilities/index.md)

## Workflows

- [Write Technical PRD](workflows/write-technical-prd.md)
- [Review API or Platform Change](workflows/review-api-platform-change.md)
- [Map Technical Dependencies](workflows/map-technical-dependencies.md)
- [Reconcile Product and Technical Risk](workflows/reconcile-product-technical-risk.md)

## Deliverables and Commands

- [Technical PRD](deliverables/technical-prd.md)
- [API Change Brief](deliverables/api-change-brief.md)
- [Dependency Map](deliverables/dependency-map.md)
- [/draft-technical-prd](commands/draft-technical-prd.md)
- [/review-api-change](commands/review-api-change.md)
- [/map-dependencies](commands/map-dependencies.md)

Use this bundle as decision support, not as authority to make commitments, approve engineering designs, or change live systems without confirmation.

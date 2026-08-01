---
type: Bundle Index
title: Product Backlog / User Stories
description: Source-aware guidance for drafting, refining, ordering, and reviewing product backlog items and user stories.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: deliverables
tags: [product backlog, user stories, acceptance criteria, refinement, prioritization]
aliases: [Product Backlog, User Story Backlog, Sprint Backlog Items]
problems_solved: [turning product evidence into reviewable backlog items, making ordering rationale explicit, separating Scrum requirements from optional practices]
industries: []
tools: []
frameworks: [Product Goal alignment, evidence and value-risk-dependency ordering]
deliverables: [product backlog item, user story, backlog review]
commands: []
skills: []
evaluations: [backlog item quality check]
okb_bundle_id: product-backlog-user-stories
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: [product-manager, technical-product-manager]
adjacent_bundles: []
contributors: [OpenKnowledgeBank]
maintainers: [OpenKnowledgeBank]
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations: [This bundle is not a substitute for customer research or product ownership, local product facts must be provided or verified, user-story format and scoring methods are optional practices rather than universal Scrum requirements]
safety_notes: [Keep customer and product strategy data private, require explicit confirmation before live tracker or roadmap changes, route regulated or high-stakes requirements to current authoritative review]
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric planned when prerequisites exist
  caveat: No measured score is claimed; reviewed evaluator configuration and scoring are pending.
evaluation_detail:
  status: blocked
  next_action: Create and review a public-safe task set and evaluator configuration, then obtain reviewer-scored baseline and bundle-assisted outputs.
timestamp: "2026-08-01T00:00:00Z"
---

# Product Backlog / User Stories

Use this bundle to produce a reviewable backlog item grounded in the user's supplied product evidence. The 2020 Scrum Guide defines the Product Backlog and Product Goal; it does not require a user-story sentence format. Use the format when it improves shared understanding, and use another item shape when the work is better represented otherwise.

## Contents

- [Product backlog item](deliverables/product-backlog-item.md)
- [Draft and refine](workflows/draft-and-refine-backlog-item.md)
- [Order and review](workflows/order-and-review-backlog.md)
- [Product Goal, evidence, and ordering](frameworks/product-goal-evidence-ordering.md)
- [Quality check](evaluations/backlog-item-quality-check.md)
- [Before and after example](examples/before-after/backlog-item/task.md)
- [Source checks](references/source-checks.md)

## Evidence Boundary

Every output distinguishes `Verified`, `Provided`, `Assumed`, and `Needs verification`. Do not invent customer evidence, metrics, dates, owners, estimates, dependencies, tool fields, or acceptance behavior. Any live system change requires explicit confirmation after the proposed change is shown.

## Source Note

Primary source: Scrum Guide 2020, https://scrumguides.org/scrum-guide.html. Supporting sources: Scrum.org Product Backlog and User Story Format resources. Local product evidence is required for scenario-specific conclusions.

---
type: Bundle Index
title: System Architecture Design Document
description: Source-aware deliverable bundle for architecture documentation covering stakeholders, requirements, context, views, interfaces, data, quality attributes, decisions, risks, and verification.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- architecture-design
- system-design
- technical-documentation
- deliverable
aliases:
- System Architecture Design Document
problems_solved:
- Prepare a architecture design document without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Software
- Information technology
- Financial services
tools: []
frameworks:
- source-evidence matrix
- system and solution architecture documentation review matrix
- qualified-review gate
deliverables:
- architecture design document
commands: []
skills: []
evaluations:
- System Architecture Design Document source-awareness check
okb_bundle_id: architecture-design-doc
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: []
adjacent_bundles: []
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
- Use the cited official, originator, standards, or professional sources for general system and solution architecture documentation context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for system purpose, scope, stakeholders, and concerns, functional and quality requirements, current and target context, components, dependencies, and trust boundaries, interfaces, contracts, data flows, storage, and lifecycle, capacity, availability, security, privacy, operability, cost, and constraints, and alternatives, decisions, consequences, risks, validation, ownership, and approval.
- Do not infer requirement, component behavior, interface contract, capacity, security posture, and architecture approval.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before committing architecture, interfaces, vendors, infrastructure, security controls, spend, or implementation without accountable technical and business review.
- Route legal, privacy, security, compliance, financial, employment, safety, and other qualified judgments to accountable reviewers.
timestamp: '2026-07-31T00:00:00Z'
evaluation_summary:
  status: measured
  last_evaluated: '2026-07-31'
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 17
  okb_score: 36
  absolute_lift: 19
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 3
    okb_score: 12
    max_score: 12
  - task: deliverable-quality-review
    baseline_score: 8
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 17/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# System Architecture Design Document

Source-aware deliverable bundle for architecture documentation covering stakeholders, requirements, context, views, interfaces, data, quality attributes, decisions, risks, and verification.

## Required Response Contract

Every substantive response must contain these visible sections:

1. **Direct answer** - state what can be concluded or done now.
2. **Evidence status** - list `Verified`, `Provided`, `Assumed`, and `Needs verification` separately, writing `None` where a category is empty.
3. **Verification plan** - name source category, scope, date or version, and conflict checks.
4. **Confirmation boundary** - identify the evidenced reviewer and actions prohibited without explicit approval.
5. **Source note** - name sources used and material limitations.

Do not replace missing evidence with a general disclaimer. Ask for exact artifacts and explain which decision each artifact supports.

When no local evidence is provided, do not infer stakeholder knowledge, intent, access, configuration, records, system state, approval, or reviewer ownership. Set `Verified`, `Provided`, and `Assumed` to `None` unless the request explicitly supports an item. Set `Accountable reviewer` to `Needs verification`; do not nominate or designate a generic role.

## Start Here

- [overview.md](overview.md)
- [deliverable.md](deliverable.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/architecture-design-doc-brief.md](deliverables/architecture-design-doc-brief.md)

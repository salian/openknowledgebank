---
type: Bundle Index
title: Interactive Prototype
description: Source-aware deliverable bundle for defining an interactive prototype with explicit research question, fidelity, flows, states, content, data, accessibility, testing, and non-production boundaries.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- interactive-prototype
- ux-design
- product-research
- deliverable
aliases:
- Interactive Prototype
problems_solved:
- Prepare a interactive prototype specification without fabricating local facts.
- Separate verified, provided, assumed, and missing evidence.
- Produce a review-ready recommendation with explicit verification and approval boundaries.
industries:
- Design
- Product management
- Software
tools: []
frameworks:
- source-evidence matrix
- interactive experience prototyping review matrix
- qualified-review gate
deliverables:
- interactive prototype specification
commands: []
skills: []
evaluations:
- Interactive Prototype source-awareness check
okb_bundle_id: interactive-prototype
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
- Use the cited official, originator, standards, or professional sources for general interactive experience prototyping context; local facts, records, values, states, and permissions require inspected evidence.
- Task-specific work requires current evidence for research question, audience, scenario, and decision, prototype fidelity, platform, device, and scope, flows, screens, states, interactions, errors, and edge cases, content, assets, rights, sample data, and privacy, design-system, accessibility, and usability requirements, and test plan, participants, observations, limitations, ownership, and approval.
- Do not infer user need, interaction behavior, content approval, accessibility, technical feasibility, and test outcome.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, and other sensitive data.
- Require explicit confirmation before presenting a prototype as production, collecting sensitive data, publishing assets, committing implementation, or making usability claims without valid testing.
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
  baseline_score: 15
  okb_score: 36
  absolute_lift: 21
  task_scores:
  - task: empty-evidence-integrity
    baseline_score: 2
    okb_score: 12
    max_score: 12
  - task: deliverable-quality-review
    baseline_score: 7
    okb_score: 12
    max_score: 12
  - task: source-or-metric-reconciliation
    baseline_score: 6
    okb_score: 12
    max_score: 12
  comparison_scores: []
  display_summary: Improved measured rubric score from 15/36 to 36/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# Interactive Prototype

Source-aware deliverable bundle for defining an interactive prototype with explicit research question, fidelity, flows, states, content, data, accessibility, testing, and non-production boundaries.

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
- [deliverables/interactive-prototype-brief.md](deliverables/interactive-prototype-brief.md)

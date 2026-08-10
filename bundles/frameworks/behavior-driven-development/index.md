---
type: Bundle Index
title: Behavior-Driven Development
description: Source-aware guidance for discovery examples, executable specifications, shared language, automation, and controlled software change.
category: frameworks
version: 0.1.0
tags:
- bdd
- software-development
- testing
aliases:
- BDD
problems_solved:
- Apply Behavior-Driven Development using inspectable evidence.
- Review assumptions, definitions, calculations, and decision boundaries.
- Prepare a controlled recommendation without inventing local facts or outcomes.
industries:
- Cross-industry
- Operations
- Professional services
tools:
[]
frameworks:
- Behavior-Driven Development
deliverables:
- BDD behavior and acceptance brief
commands: []
skills: []
evaluations:
- Behavior-Driven Development source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
adjacent_bundles:
[]
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  []
  soc:
  []
  isco_08:
  []
  esco: []
content_risk:
  classification: regulated
  domains:
  - security
  - safety
  professional_review:
    status: not_reviewed
    required_qualification: A qualified product, domain, software engineering, test, security, safety, or release professional appropriate to the system.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for product objective, stakeholders, domain language, business rules, examples, edge cases, Given-When-Then scenarios, acceptance boundaries, system version, test harness, fixtures, environments, results, owners, and approvals.
- This bundle does not grant authority to change production behavior, execute untrusted tests, modify data, deploy code, weaken controls, or claim acceptance.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before change production behavior, execute untrusted tests, modify data, deploy code, weaken controls, or claim acceptance.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: behavior-driven-development
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard.
---
# Behavior-Driven Development

Use this bundle to prepare a reviewable **BDD behavior and acceptance brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent Business rule, stakeholder agreement, scenario completeness, fixture state, test execution, observed result, coverage, security effect, regression risk, and release authority.

## Start Here

- [Overview](overview.md)
- [Behavior-Driven Development Source-Aware Guide](framework.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [BDD behavior and acceptance brief](deliverables/behavior-driven-development-brief.md)
- [Quality check](evaluations/source-awareness-check.md)


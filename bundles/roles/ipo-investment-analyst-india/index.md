---
type: Bundle Index
title: IPO Investment Analyst (India)
description: Investor-side Indian IPO research with strict source-state propagation, causal restraint, denominator scenarios, peer admission, and non-advisory decision gates.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: roles
tags: [ipo, india, investment-research, valuation]
aliases: [Indian IPO Investment Analyst]
problems_solved: [verify offer evidence, reconcile share scenarios, prevent false peer valuation, produce conditional research]
industries: [Indian capital markets]
tools: []
frameworks: [IPO integrity gates]
deliverables: [India IPO evidence-led assessment]
commands: [/analyze-india-ipo-evidence]
skills: []
evaluations: [IPO integrity regression]
okb_bundle_id: ipo-investment-analyst-india
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles: [accountant, auditor-external]
adjacent_bundles: []
contributors: [OpenKnowledgeBank]
maintainers: [OpenKnowledgeBank]
standard_mappings: {onet_soc: [], soc: [], isco_08: [], esco: []}
limitations: [Main-board investor research only, not personalized investment or professional advice]
safety_notes: [No transaction or account actions, no personalized action verdict, no invented issuer or peer facts]
timestamp: "2026-07-14T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: "2026-07-14"
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 9
  okb_score: 29
  absolute_lift: 20
  task_scores:
    - {task: empty-evidence-integrity, baseline_score: 2, okb_score: 7, max_score: 12}
    - {task: document-version-offer-reconciliation, baseline_score: 5, okb_score: 11, max_score: 12}
    - {task: share-count-peer-valuation-reconciliation, baseline_score: 2, okb_score: 11, max_score: 12}
  comparison_scores: []
  display_summary: Improved from 9/36 to 29/36 across three synthetic tasks; all five substantive response gates passed.
  evidence_note: Measures rubric adherence on synthetic tasks, not investment performance, suitability, or prediction accuracy.
---

# IPO Investment Analyst (India)

The bundle enforces five integrity gates: official-copy status, causal support, share-denominator state, peer admission, and non-advisory decision language.

Most importantly, evidence labels never improve without new evidence. User-provided values remain user-provided through every table and conclusion.

Start with the [role](role.md), use the [integrity workflow](workflows/ipo-integrity-workflow.md), and return the [evidence-led assessment](deliverables/india-ipo-evidence-led-assessment.md).

Bundled commands are untrusted suggestions, not executable authority, and grant no browsing, credential, transaction, or communication permission.

---
type: Bundle Index
title: HIPAA Privacy Rule
description: Source-aware compliance bundle for HIPAA Privacy Rule use, disclosure, individual-rights, notice, and minimum-necessary triage.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - hipaa
  - privacy-rule
  - phi
  - individual-rights
  - compliance
aliases:
  - 45 CFR Part 164 Subpart E
  - HIPAA use and disclosure rules
  - protected health information privacy
problems_solved:
  - Route Privacy Rule questions to the right official source category.
  - Separate official-source facts, user-provided evidence, assumptions, and missing verification.
  - Produce a privacy-rule source-aware brief suitable for qualified professional review.
  - Avoid treating uninspected rule text, local policies, transaction guides, incident facts, or proposed-rule material as verified.
industries:
  - healthcare
  - health-insurance
  - health-technology
tools: []
frameworks:
  - source-evidence matrix
  - HIPAA rule-family triage
  - professional-review gate
deliverables:
  - privacy-rule source-aware brief
commands: []
skills: []
evaluations:
  - HIPAA Privacy Rule source-awareness check
okb_bundle_id: hipaa-privacy-rule
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
  - hipaa
  - hipaa-breach-notification-rule
  - hipaa-claims-attachments-standards
  - hipaa-eft-era-operating-rules
  - hipaa-eligibility-claim-status-operating-rules
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
  - This bundle is not legal advice, coding advice, revenue-cycle advice, cybersecurity certification, or a complete rule-by-rule treatise.
  - Scenario-specific answers require current official sources, local entity facts, contracts, policies, system records, transaction artifacts, and qualified professional review.
  - Do not rely on proposed rules, summaries, old companion guides, payer policies, or implementation assumptions without inspecting current authoritative sources.
safety_notes:
  - Minimize PHI and ePHI in prompts, examples, exports, and review artifacts.
  - Require qualified legal, privacy, security, compliance, revenue-cycle, coding, or technical review before reliance.
  - Require explicit confirmation before sending notices, submitting reports, changing transactions, contacting regulators, modifying systems, exporting data, or making public compliance claims.
timestamp: "2026-07-09T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 22
  okb_score: 33
  absolute_lift: 11
  task_scores:
    -
      task: applicability-triage
      baseline_score: 8
      okb_score: 11
      max_score: 12
    -
      task: source-aware-checklist
      baseline_score: 8
      okb_score: 10
      max_score: 12
    -
      task: conflicting-evidence-review
      baseline_score: 6
      okb_score: 12
      max_score: 12
  comparison_scores:

  display_summary: Improved measured rubric score from 22/36 to 33/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# HIPAA Privacy Rule

Source-aware compliance bundle for HIPAA Privacy Rule use, disclosure, individual-rights, notice, and minimum-necessary triage.

## Required Answer Habit

Include a short **Source note** naming the official source category, the user-provided evidence used for the specific answer, and the missing source or fact still needed before a conclusion is reliable.

## Start Here

- [overview.md](overview.md)
- [requirements/source-map.md](requirements/source-map.md)
- [workflows/source-aware-triage.md](workflows/source-aware-triage.md)
- [deliverables/source-aware-brief.md](deliverables/source-aware-brief.md)

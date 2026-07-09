---
type: Bundle Index
title: HIPAA
description: Source-aware compliance hub for U.S. HIPAA privacy, security, breach notification, enforcement, and Administrative Simplification triage.
schema_version: "0.1.0"
bundle_format: okf-compatible
category: compliance
tags:
  - hipaa
  - healthcare
  - privacy
  - security
  - compliance
  - united-states
aliases:
  - Health Insurance Portability and Accountability Act
  - HIPAA Administrative Simplification
problems_solved:
  - Triage HIPAA questions without inventing legal conclusions.
  - Separate official HIPAA sources, user-provided facts, assumptions, and missing evidence.
  - Route questions to Privacy Rule, Security Rule, Breach Notification Rule, Enforcement, transactions, identifiers, or code-set source categories.
  - Produce source-aware HIPAA compliance briefs for professional review.
industries:
  - healthcare
  - health-insurance
  - health-technology
  - revenue-cycle
tools: []
frameworks:
  - source-evidence matrix
  - HIPAA rule-family triage
  - regulated-entity scope check
deliverables:
  - source-aware HIPAA compliance brief
commands: []
skills: []
evaluations:
  - HIPAA source-awareness check
okb_bundle_id: hipaa
okb_bundle_version: "0.1.0"
trust_tier: trusted
status: draft
license: CC-BY-4.0
related_bundles:
  - hipaa-breach-notification-rule
  - hipaa-claims-attachments-standards
  - hipaa-eft-era-operating-rules
  - hipaa-eligibility-claim-status-operating-rules
  - hipaa-employer-identifier-ein
  - hipaa-enforcement-cooperation
  - hipaa-medical-code-sets
  - hipaa-national-provider-identifier
  - hipaa-privacy-rule
  - hipaa-security-rule
  - hipaa-security-rule-cybersecurity-nprm
  - hipaa-transactions-standards
adjacent_bundles:
  - compliance-officer
  - healthcare-hipaa-business-associate-agreement-baa-attorney
  - data-protection-officer-privacy-officer
  - chief-information-security-officer-ciso
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
  - This bundle is a compliance hub, not legal advice or a complete rule-by-rule HIPAA treatise.
  - Scenario-specific answers require current official sources, entity and relationship facts, user-provided evidence, and professional review.
  - Proposed rules, state law, 42 CFR Part 2, contract terms, and organization policies must be inspected before reliance when relevant.
safety_notes:
  - Require qualified legal, privacy, security, compliance, or revenue-cycle professional review before relying on outputs for regulatory, enforcement, contractual, breach, or incident-response decisions.
  - Do not request, expose, or publish PHI or ePHI beyond what is necessary for the user-approved analysis.
  - Require explicit confirmation before submitting reports, contacting regulators, changing policies, changing contracts, sending notices, exporting PHI/ePHI, or modifying live systems.
timestamp: "2026-07-09T00:00:00Z"
evaluation_summary:
  status: measured
  last_evaluated: 2026-07-09
  method: baseline-vs-okb-rubric
  model: openai/gpt-4o-mini
  temperature: 0.2
  tasks_count: 3
  max_score: 36
  baseline_score: 19
  okb_score: 31
  absolute_lift: 12
  task_scores:
    - task: applicability-triage
      baseline_score: 5
      okb_score: 11
      max_score: 12
    - task: source-aware-checklist
      baseline_score: 8
      okb_score: 9
      max_score: 12
    - task: conflicting-evidence-review
      baseline_score: 6
      okb_score: 11
      max_score: 12
  comparison_scores:
  display_summary: Improved measured rubric score from 19/36 to 31/36 across 3 benchmark tasks.
  evidence_note: Public listing scorecard excludes raw prompts and private run artifacts.
---

# HIPAA

This bundle helps an agent answer HIPAA questions with source discipline. It is a hub for triage, source selection, and public-safe compliance brief writing, not a replacement for legal advice.

## Required Answer Habit

For source-sensitive answers, include a short **Source note** naming the official HIPAA source category, current rule or guidance source checked, user-provided evidence, and missing source or fact still needed before a hypothesis becomes a conclusion.

## Start Here

- [overview.md](overview.md)
- [workflows/hipaa-obligation-triage.md](workflows/hipaa-obligation-triage.md)
- [requirements/rule-family-map.md](requirements/rule-family-map.md)
- [deliverables/source-aware-hipaa-compliance-brief.md](deliverables/source-aware-hipaa-compliance-brief.md)
- [evaluations/hipaa-source-awareness-check.md](evaluations/hipaa-source-awareness-check.md)
- [references/index.md](references/index.md)

## Official Source Categories

Use HHS OCR for HIPAA Privacy, Security, Breach Notification, enforcement, and guidance pages; eCFR for current 45 CFR Parts 160, 162, and 164 text; CMS/HHS Administrative Simplification sources for transactions, identifiers, and code sets; Federal Register sources for proposed and final rules; and user-provided records for organization-specific facts.

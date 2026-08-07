---
type: Bundle Index
title: Test Suite / Test Plan
description: Source-aware deliverable bundle for planning, specifying, reviewing, and reporting software tests without inventing execution evidence or coverage.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- test plan
- test suite
- UAT
- software testing
- quality assurance
aliases:
- Software Test Plan
- UAT Test Plan
- Automated Test Suite
problems_solved:
- Trace requirements and risks to planned tests and evidence.
- Separate expected results, actual results, execution status, and defects.
- Prevent fabricated coverage, execution, approval, and release-readiness claims.
industries:
- software
- information technology
- financial services
tools: []
frameworks:
- risk-based testing
- requirements traceability
- evidence-status ledger
deliverables:
- test plan
- manual or automated test suite
- user acceptance test plan
- execution and evidence report
commands: []
skills: []
evaluations:
- Test Suite / Test Plan quality check
okb_bundle_id: test-suite
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- financial-systems-analyst-fintech-erp
- software-quality-assurance-analyst-tester
- test-automation-sdet-engineer
adjacent_bundles:
- test-driven-development
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
- This bundle is a planning, specification, review, and reporting aid; it does not execute tests or prove product quality, compliance, acceptance, or release readiness.
- Test levels, techniques, status vocabularies, entry and exit criteria, environments, and evidence requirements must be tailored to the organization and product.
- Requirements, risks, expected results, coverage, actual results, defects, waivers, owners, approvals, and sign-off require supplied evidence.
safety_notes:
- Use only authorized systems, environments, accounts, data, interfaces, and test windows.
- Minimize and protect personal, production, security-sensitive, and regulated data in test artifacts and evidence.
- Escalate destructive, adversarial, production-impacting, or regulated testing to accountable owners before execution.
timestamp: '2026-08-07T00:00:00Z'
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No reviewed public-safe benchmark task set, runnable evaluator configuration, or reviewer-scored aggregate results were available for this run.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Create and approve three public-safe tasks covering empty evidence, conflicting expected results, and release pressure; configure identical baseline and bundle-assisted runs; obtain reviewer-scored aggregate results; and build a listing scorecard.
---

# Test Suite / Test Plan

Use this bundle to plan, specify, review, and report software testing from an identified test basis, risks, and supplied evidence.

Start with the [deliverable contract](deliverable.md), follow the [planning and review workflow](workflow.md), and apply the [quality check](evaluations/quality-check.md).

This bundle does not execute tests or establish that a system passed, was accepted, or is ready for release.

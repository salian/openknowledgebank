---
type: Bundle Index
title: Meta Llama
description: Source-aware guidance for selecting, licensing, deploying, evaluating, and governing Meta Llama models.
category: tools
version: 0.1.0
tags:
- llama
- generative-ai
- machine-learning
aliases:
- Llama
problems_solved:
- Plan evidence-grounded Llama deployments.
- Review model, license, data, safety, and evaluation constraints.
- Prepare controlled use without inventing model behavior or rights.
industries:
- Technology
- Research
- Cross-industry
tools:
- Meta Llama
frameworks:
- evidence-grounded model deployment
deliverables:
- Llama deployment and evaluation brief
commands: []
skills: []
evaluations:
- Meta Llama source-awareness check
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
  - privacy
  - security
  - legal
  professional_review:
    status: not_reviewed
    required_qualification: A qualified machine-learning, AI safety, security, privacy, licensing, or domain professional appropriate to the deployment and use case.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for exact model, release, license, weights, tokenizer, runtime, hardware, prompts, data, safeguards, evaluation tasks, reviewer results, deployment boundary, and approvals.
- This bundle does not grant authority to download or redistribute weights, submit sensitive data, fine-tune models, deploy endpoints, disable safeguards, or act on generated outputs.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before download or redistribute weights, submit sensitive data, fine-tune models, deploy endpoints, disable safeguards, or act on generated outputs.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: meta-llama
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
# Meta Llama

Use this bundle to prepare a reviewable **Llama deployment and evaluation brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent Model identity, license rights, artifact availability, safety, benchmark performance, output truth, data handling, and deployment state.

## Start Here

- [Overview](overview.md)
- [Meta Llama Source-Aware Guide](tool.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [Llama deployment and evaluation brief](deliverables/meta-llama-brief.md)
- [Quality check](evaluations/source-awareness-check.md)


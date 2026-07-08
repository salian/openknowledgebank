---
type: Tool
title: "Terraform"
description: "Terraform is the de facto standard infrastructure-as-code tool: HCL declarative configs, a 300+ provider registry, and HCP Terraform/Terraform Enterprise for remote state, runs, and workspaces. It is deeply cross-role — DevOps/SRE, platform engineers, cloud/infra engineers, security/compliance, and even data/ML-ops teams provision infrastructure with it — so a very large number of role bundles would plausibly link to it, giving strong hub and SEO value (hence P0, not P1/P2). It is neither vertic"
okb_bundle_id: terraform
okb_bundle_version: "0.1.0"
status: draft
trust_tier: unverified
license: CC-BY-4.0
timestamp: 2026-07-08T00:00:00Z
---
# Terraform

## Purpose

Terraform is the de facto standard infrastructure-as-code tool: HCL declarative configs, a 300+ provider registry, and HCP Terraform/Terraform Enterprise for remote state, runs, and workspaces. It is deeply cross-role — DevOps/SRE, platform engineers, cloud/infra engineers, security/compliance, and even data/ML-ops teams provision infrastructure with it — so a very large number of role bundles would plausibly link to it, giving strong hub and SEO value (hence P0, not P1/P2). It is neither vertic

## Candidate Metadata

- Shape: tool
- Priority: P0
- Vendor: HashiCorp (IBM)
- Generated run: wf_72692c8a

## Aliases And Members

- Terraform
- HCP Terraform
- Terraform Cloud
- Terraform Enterprise

## Value Signal

Terraform is the de facto standard infrastructure-as-code tool: HCL declarative configs, a 300+ provider registry, and HCP Terraform/Terraform Enterprise for remote state, runs, and workspaces. It is deeply cross-role — DevOps/SRE, platform engineers, cloud/infra engineers, security/compliance, and even data/ML-ops teams provision infrastructure with it — so a very large number of role bundles would plausibly link to it, giving strong hub and SEO value (hence P0, not P1/P2). It is neither vertical nor region-specific, and it is one of the most exhaustively documented, ubiquitous platforms in existence, so the base model already knows core HCL syntax, the plan/apply/destroy lifecycle, state, modules, and common AWS/Azure/GCP provider patterns reliably — meaning per-bundle marginal grounding value is comparatively low. The residual grounding value that does exist sits in fast-moving and less-memorized surfaces: the ongoing BSL/OpenTofu licensing split and version divergence, HCP Terraform's proprietary API/workspaces/run-tasks/private registry/policy-as-code (Sentinel/OPA), provider-version-specific schema changes across the huge registry, and newer features (Stacks, test framework, ephemeral resources) that shift release to release. Net: foundational ubiquitous platform where the value is dominated by hub/SEO reach rather than niche-knowledge grounding.

## Source Note

- https://developer.hashicorp.com/terraform

## Draft Use Boundary

This generated bundle is a discovery and scaffolding artifact. Before using it for
high-stakes work, enrich it with domain-specific guidance, examples, and
validation against the authoritative sources above.

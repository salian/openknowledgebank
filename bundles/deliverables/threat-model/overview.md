---
type: "Bundle Overview"
title: "Threat Model overview"
description: "Scope, evidence, and authority boundaries for Threat Model."
---
# Threat Model Overview

Define decision, system version and environment; inspect architecture, assets, data flows, identities, trust boundaries, dependencies and assumptions; enumerate threat actors, misuse and abuse cases with method and evidence; map existing and proposed controls; distinguish threat, weakness and verified vulnerability; rank with explicit criteria and uncertainty; validate, assign owners, track residual risk, changes, review and acceptance authority.

## Evidence Contract

Relevant evidence includes system and environment versions, architecture and data-flow diagrams, asset and data classifications, identity and trust boundaries, dependency and supplier evidence, threat intelligence scope and date, abuse cases, control design and test evidence, vulnerability records, ranking criteria and uncertainty, mitigations and owners, residual-risk decisions, reviews, and approvals. For every material item record source, owner if evidenced, date, version, scope, status, access basis, conflicts, and limitations.

When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None`. Put exact missing artifacts under `Needs verification`. A general disclaimer is not a substitute for requesting evidence.

## Boundary

Analysis and drafting do not establish system boundary, asset, data flow, trust relationship, actor capability, threat, vulnerability, exploitability, likelihood, control effectiveness, residual risk, security, or approval. Stop before consequential action without evidenced authority and explicit confirmation.

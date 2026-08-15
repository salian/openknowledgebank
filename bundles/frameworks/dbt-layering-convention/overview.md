---
type: "Bundle Overview"
title: "dbt Staging, Intermediate, and Marts Layering overview"
description: "Scope, evidence, and authority boundaries for dbt Staging, Intermediate, and Marts Layering."
---
# dbt Staging, Intermediate, and Marts Layering Overview

Apply current dbt guidance to inspected sources, models, contracts, consumers, naming, tests, environments, permissions, and migration constraints.

## Evidence Contract

Relevant evidence includes current source definitions and scope, local objective and context, inspected inputs, assumptions, alternatives, calculations, constraints, outcomes, validation, decision ownership, and approval evidence. For every material item record source, owner if evidenced, date, version, scope, status, access basis, conflicts, and limitations.

When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None`. Put exact missing artifacts under `Needs verification`. A general disclaimer is not a substitute for requesting evidence.

## Boundary

Analysis and drafting do not establish source schema, model grain or semantics, lineage, contract, test result, performance, compatibility, data quality, deployment state, or approval. Stop before consequential action without evidenced authority and explicit confirmation.

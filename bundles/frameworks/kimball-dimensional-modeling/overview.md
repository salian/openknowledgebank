---
type: Bundle Overview
title: Kimball Dimensional Modeling overview
description: Scope, evidence, and authority boundaries for Kimball Dimensional Modeling.
---
# Kimball Dimensional Modeling Overview

Source-aware guidance for business processes, grain, facts, dimensions, conformance, history, quality, and controlled warehouse design.

## Evidence Contract

Relevant evidence includes business requirements, processes, source systems, records, grain, facts, dimensions, keys, hierarchies, slowly changing behavior, conformance, bus matrix, transformations, quality rules, security classifications, query patterns, tests, owners, and approvals. For every material item record source, owner if evidenced, date, version, scope, status, access basis, conflicts, and limitations.

When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None`. Put exact missing artifacts under `Needs verification`. A general disclaimer is not a substitute for requesting evidence.

## Boundary

Analysis and drafting do not establish Business process, source semantics, grain, fact additivity, dimension meaning, key behavior, history, conformance, transformation result, quality, effective access, query result, and migration impact. Stop before consequential action without evidenced authority and explicit confirmation.


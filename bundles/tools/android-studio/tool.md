---
type: Tool Guide
title: Android Studio
description: Defines source-aware Android Studio project, build variant, testing, profiling, signing, and release review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Android Studio build and release brief with explicit evidence states.
confirmation_required:
- trust or execute project code, resolve dependencies, run on devices, handle signing keys, sign a release, upload artifacts, or publish an app
okb_bundle_id: android-studio
timestamp: '2026-07-31T00:00:00Z'
---
# Android Studio

Source-aware tool bundle for Android Studio project, build variant, testing, profiling, signing, and release review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://developer.android.com/studio
- https://developer.android.com/build
- https://developer.android.com/build/build-variants

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- Android Studio, Android Gradle Plugin, Gradle, JDK, SDK, build-tools, and dependency versions
- repository source and trust, modules, source sets, manifests, build types, product flavors, variants, resources, permissions, signing configuration, keys, tests, emulator or device, profiler evidence, build outputs, Play requirements, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer project safety, dependency compatibility, selected variant, test result, performance, signing state, app behavior, or release readiness.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that trust or execute project code, resolve dependencies, run on devices, handle signing keys, sign a release, upload artifacts, or publish an app.

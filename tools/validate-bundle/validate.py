#!/usr/bin/env python3
"""Validate OpenKnowledgeBank public bundle structure and registry metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse


CATEGORIES = {
    "roles",
    "industries",
    "capabilities",
    "tools",
    "frameworks",
    "compliance",
    "jurisdictions",
    "deliverables",
    "datasets",
}

TRUST_TIERS = {"trusted", "community", "unverified", "rejected"}
STATUSES = {"draft", "beta", "stable", "deprecated"}
CREDIT_ROLES = {
    "creator",
    "contributor",
    "maintainer",
    "editorial_reviewer",
    "technical_reviewer",
    "domain_reviewer",
}
CONTENT_RISK_CLASSIFICATIONS = {"regulated", "ymyl"}
CONTENT_RISK_DOMAINS = {
    "accounting",
    "employment",
    "financial",
    "insurance",
    "legal",
    "medical",
    "privacy",
    "regulatory",
    "safety",
    "security",
    "tax",
}
PROFESSIONAL_REVIEW_STATUSES = {"not_reviewed", "technical_only", "domain_reviewed"}
REQUIRED_LANDING_STRING_FIELDS = {
    "definition",
    "summary",
    "meta_description",
    "social_summary",
    "download_note",
    "agent_use_example",
}
REQUIRED_LANDING_LIST_FIELDS = {"audiences", "when_to_use", "required_inputs", "not_for"}
GENERIC_SOURCE_LABELS = {
    "resource",
    "resources",
    "source",
    "sources",
    "reference",
    "references",
    "documentation",
    "website",
    "primary source url",
}

REQUIRED_REGISTRY_FIELDS = {
    "id",
    "title",
    "description",
    "category",
    "path",
    "repo",
    "license",
    "trust_tier",
    "status",
    "version",
    "source_url",
    "download_url",
}

RECOMMENDED_REGISTRY_FIELDS = {
    "tags",
    "aliases",
    "problems_solved",
    "limitations",
    "safety_notes",
}

CORE_FILES = {
    "roles": "role.md",
    "industries": "overview.md",
    "capabilities": "overview.md",
    "tools": "tool.md",
    "frameworks": "framework.md",
    "compliance": "overview.md",
    "jurisdictions": "jurisdiction.md",
    "deliverables": "deliverable.md",
    "datasets": "dataset.md",
}

PRIVATE_OR_SECRET_PATTERNS = [
    (re.compile(r"/Users/[A-Za-z0-9._-]+/"), "absolute local user path"),
    (re.compile(r"Dropbox/Projects/"), "private workspace path"),
    (re.compile(r"BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY"), "private key block"),
    (re.compile(r"\bOPENROUTER_API_KEY\s*="), "OpenRouter API key assignment"),
    (re.compile(r"\b[A-Za-z0-9_]*API_KEY\s*=\s*['\"][^'\"]+['\"]"), "API key assignment"),
    (re.compile(r"\bsk-or-v1-[A-Za-z0-9_-]{20,}"), "OpenRouter-style secret key"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"), "secret key token"),
]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass
class Finding:
    level: str
    path: Path
    message: str


class Validator:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.findings: list[Finding] = []

    def error(self, path: Path | str, message: str) -> None:
        self.findings.append(Finding("error", self.display_path(path), message))

    def warning(self, path: Path | str, message: str) -> None:
        self.findings.append(Finding("warning", self.display_path(path), message))

    def display_path(self, path: Path | str) -> Path:
        path_obj = Path(path)
        if path_obj.is_absolute():
            try:
                return path_obj.relative_to(self.root)
            except ValueError:
                return path_obj
        return path_obj

    def read_json(self, path: Path) -> dict[str, Any]:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            self.error(path, "missing JSON file")
            return {}
        except json.JSONDecodeError as exc:
            self.error(path, f"invalid JSON: {exc}")
            return {}

        if not isinstance(data, dict):
            self.error(path, "top-level JSON value must be an object")
            return {}

        return data

    def validate(self) -> int:
        registry_path = self.root / "registry" / "bundles.json"
        registry = self.read_json(registry_path)
        contributors_path = self.root / "registry" / "contributors.json"
        contributors = self.validate_contributors(contributors_path)
        bundles = registry.get("bundles", [])

        if not isinstance(bundles, list):
            self.error(registry_path, "`bundles` must be an array")
            bundles = []

        ids: set[str] = set()
        for index, bundle in enumerate(bundles):
            if not isinstance(bundle, dict):
                self.error(registry_path, f"bundle entry {index} must be an object")
                continue
            bundle_id = str(bundle.get("id", f"entry-{index}"))
            self.validate_registry_entry(registry_path, bundle, ids, contributors)
            self.validate_bundle_files(bundle)

        self.validate_relationships(registry_path, bundles, ids)
        self.scan_public_content()
        return self.report()

    def validate_contributors(self, registry_path: Path) -> dict[str, dict[str, Any]]:
        registry = self.read_json(registry_path)
        contributors = registry.get("contributors", [])
        contributor_profiles: dict[str, dict[str, Any]] = {}

        if not isinstance(contributors, list):
            self.error(registry_path, "`contributors` must be an array")
            return contributor_profiles

        for index, contributor in enumerate(contributors):
            if not isinstance(contributor, dict):
                self.error(registry_path, f"contributor entry {index} must be an object")
                continue

            contributor_id = str(contributor.get("id", ""))
            if not contributor_id or not SLUG_RE.match(contributor_id):
                self.error(registry_path, f"contributor entry {index}: `id` must be a kebab-case slug")
                continue
            if contributor_id in contributor_profiles:
                self.error(registry_path, f"{contributor_id}: duplicate contributor id")
            contributor_profiles[contributor_id] = contributor

            for field in ["name", "handle", "bio"]:
                if not isinstance(contributor.get(field), str) or not contributor[field].strip():
                    self.error(registry_path, f"{contributor_id}: `{field}` must be a non-empty string")

            if not self.is_string_list(contributor.get("expertise", [])):
                self.error(registry_path, f"{contributor_id}: `expertise` must be an array of strings")

            links = contributor.get("links", {})
            if not isinstance(links, dict):
                self.error(registry_path, f"{contributor_id}: `links` must be an object")
                continue
            for label, value in links.items():
                if label not in {"github", "linkedin", "website"}:
                    self.error(registry_path, f"{contributor_id}: unsupported profile link `{label}`")
                    continue
                parsed = urlparse(str(value))
                if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                    self.error(registry_path, f"{contributor_id}: profile link `{label}` must be an absolute http(s) URL")

            credentials = contributor.get("professional_credentials", [])
            if not isinstance(credentials, list):
                self.error(registry_path, f"{contributor_id}: `professional_credentials` must be an array")
                continue
            for credential_index, credential in enumerate(credentials):
                if not isinstance(credential, dict):
                    self.error(registry_path, f"{contributor_id}: credential entry {credential_index} must be an object")
                    continue
                for field in ["name", "issuer"]:
                    if not isinstance(credential.get(field), str) or not credential[field].strip():
                        self.error(registry_path, f"{contributor_id}: credential entry {credential_index} needs `{field}`")
                verification_url = urlparse(str(credential.get("verification_url", "")))
                if verification_url.scheme not in {"http", "https"} or not verification_url.netloc:
                    self.error(registry_path, f"{contributor_id}: credential entry {credential_index} needs an absolute `verification_url`")
                credential_domains = credential.get("domains", [])
                if not self.is_string_list(credential_domains) or not credential_domains:
                    self.error(registry_path, f"{contributor_id}: credential entry {credential_index} needs at least one domain")
                else:
                    for domain in sorted(set(credential_domains) - CONTENT_RISK_DOMAINS):
                        self.error(registry_path, f"{contributor_id}: credential entry {credential_index} has unsupported domain `{domain}`")

        return contributor_profiles

    def validate_registry_entry(
        self,
        registry_path: Path,
        bundle: dict[str, Any],
        ids: set[str],
        contributors: dict[str, dict[str, Any]],
    ) -> None:
        bundle_id = str(bundle.get("id", ""))
        if not bundle_id:
            self.error(registry_path, "bundle entry is missing id")
            return

        missing = sorted(REQUIRED_REGISTRY_FIELDS - set(bundle))
        for field in missing:
            self.error(registry_path, f"{bundle_id}: missing required registry field `{field}`")

        missing_recommended = sorted(field for field in RECOMMENDED_REGISTRY_FIELDS if not bundle.get(field))
        for field in missing_recommended:
            self.warning(registry_path, f"{bundle_id}: recommended registry field `{field}` is empty")

        if bundle_id in ids:
            self.error(registry_path, f"{bundle_id}: duplicate bundle id")
        ids.add(bundle_id)

        if not SLUG_RE.match(bundle_id):
            self.error(registry_path, f"{bundle_id}: id must be kebab-case lowercase alphanumeric")

        category = bundle.get("category")
        if category not in CATEGORIES:
            self.error(registry_path, f"{bundle_id}: category `{category}` is not supported")

        trust_tier = bundle.get("trust_tier")
        if trust_tier not in TRUST_TIERS:
            self.error(registry_path, f"{bundle_id}: trust_tier `{trust_tier}` is not supported")

        status = bundle.get("status")
        if status not in STATUSES:
            self.error(registry_path, f"{bundle_id}: status `{status}` is not supported")

        path_value = str(bundle.get("path", ""))
        if category in CATEGORIES and not path_value.startswith(f"bundles/{category}/"):
            self.error(registry_path, f"{bundle_id}: path must live under bundles/{category}/")

        if path_value and Path(path_value).name != bundle_id:
            self.error(registry_path, f"{bundle_id}: path leaf must match bundle id")

        for url_field in ["repo", "source_url", "download_url"]:
            value = str(bundle.get(url_field, ""))
            parsed = urlparse(value)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                self.error(registry_path, f"{bundle_id}: `{url_field}` must be an absolute http(s) URL")

        for field in ["tags", "aliases", "problems_solved", "tools", "frameworks", "deliverables", "commands"]:
            value = bundle.get(field, [])
            if value is not None and not self.is_string_list(value):
                self.error(registry_path, f"{bundle_id}: `{field}` must be an array of strings")

        self.validate_credits(registry_path, bundle, set(contributors))
        self.validate_content_risk(registry_path, bundle, contributors)
        self.validate_public_listing_contract(registry_path, bundle)

    def validate_public_listing_contract(self, registry_path: Path, bundle: dict[str, Any]) -> None:
        bundle_id = str(bundle.get("id", ""))
        is_public = bundle.get("status") not in {"draft", "deprecated"} and bundle.get(
            "trust_tier"
        ) not in {"unverified", "rejected"}
        if not is_public:
            return

        deliverables = bundle.get("deliverables", [])
        if not self.is_string_list(deliverables) or not deliverables:
            self.error(registry_path, f"{bundle_id}: public bundle needs at least one expected deliverable")
        if not any(bundle.get(field) for field in ["tools", "frameworks", "commands", "skills"]):
            self.error(
                registry_path,
                f"{bundle_id}: public bundle needs at least one tool, framework, command, or skill",
            )

        for field in ["limitations", "safety_notes"]:
            for item in bundle.get(field, []):
                if isinstance(item, str) and "This bundle does not authorize " in item:
                    self.error(
                        registry_path,
                        f"{bundle_id}: `{field}` uses the ungrammatical authority-boundary phrase "
                        "`This bundle does not authorize …`; use `does not grant authority to …`",
                    )

        landing = bundle.get("landing_page")
        if not isinstance(landing, dict):
            self.error(registry_path, f"{bundle_id}: public bundle needs `landing_page` metadata")
            return

        for field in sorted(REQUIRED_LANDING_STRING_FIELDS):
            if not isinstance(landing.get(field), str) or not landing[field].strip():
                self.error(registry_path, f"{bundle_id}: landing page needs non-empty `{field}`")
        for field in sorted(REQUIRED_LANDING_LIST_FIELDS):
            if not self.is_string_list(landing.get(field, [])) or not landing[field]:
                self.error(registry_path, f"{bundle_id}: landing page needs non-empty `{field}`")

        summary = str(landing.get("summary", ""))
        if summary and len(summary) < 120:
            self.error(registry_path, f"{bundle_id}: landing summary must be at least 120 characters")
        meta_description = str(landing.get("meta_description", ""))
        if meta_description and not 80 <= len(meta_description) <= 160:
            self.error(registry_path, f"{bundle_id}: meta description must be 80-160 characters")

        features = landing.get("featured_contents", [])
        if not isinstance(features, list) or len(features) < 2:
            self.error(registry_path, f"{bundle_id}: landing page needs at least two featured files")
        else:
            for index, feature in enumerate(features):
                if not isinstance(feature, dict):
                    self.error(registry_path, f"{bundle_id}: featured content {index} must be an object")
                    continue
                for field in ["title", "description", "url"]:
                    if not isinstance(feature.get(field), str) or not feature[field].strip():
                        self.error(registry_path, f"{bundle_id}: featured content {index} needs `{field}`")

        for index, source in enumerate(landing.get("source_notes", [])):
            if not isinstance(source, dict):
                self.error(registry_path, f"{bundle_id}: source note {index} must be an object")
                continue
            label = str(source.get("label", "")).strip()
            if label.lower() in GENERIC_SOURCE_LABELS:
                self.error(
                    registry_path,
                    f"{bundle_id}: source note {index} needs a descriptive label, not `{label}`",
                )

        indexing = bundle.get("indexing")
        if not isinstance(indexing, dict):
            self.error(registry_path, f"{bundle_id}: public bundle needs `indexing` metadata")
            return
        if indexing.get("disposition") != "index-ready":
            self.error(registry_path, f"{bundle_id}: public bundle indexing disposition must be `index-ready`")
        for field in ["reviewed_by", "reviewed_at", "notes"]:
            if not isinstance(indexing.get(field), str) or not indexing[field].strip():
                self.error(registry_path, f"{bundle_id}: indexing metadata needs `{field}`")
        if indexing.get("content_standard") != "bundle-page-v1":
            self.error(registry_path, f"{bundle_id}: indexing metadata must use `bundle-page-v1`")

    def validate_credits(
        self,
        registry_path: Path,
        bundle: dict[str, Any],
        contributor_ids: set[str],
    ) -> None:
        bundle_id = str(bundle.get("id", ""))
        credits = bundle.get("credits", [])
        if not isinstance(credits, list):
            self.error(registry_path, f"{bundle_id}: `credits` must be an array")
            return

        seen_profiles: set[str] = set()
        for index, credit in enumerate(credits):
            if not isinstance(credit, dict):
                self.error(registry_path, f"{bundle_id}: credit entry {index} must be an object")
                continue

            profile_id = str(credit.get("profile_id", ""))
            if profile_id not in contributor_ids:
                self.error(registry_path, f"{bundle_id}: credit references unknown contributor `{profile_id}`")
            if profile_id in seen_profiles:
                self.error(registry_path, f"{bundle_id}: contributor `{profile_id}` has duplicate credit entries")
            seen_profiles.add(profile_id)

            roles = credit.get("roles", [])
            if not self.is_string_list(roles) or not roles:
                self.error(registry_path, f"{bundle_id}: credit `{profile_id}` needs at least one role")
            else:
                unsupported = sorted(set(roles) - CREDIT_ROLES)
                for role in unsupported:
                    self.error(registry_path, f"{bundle_id}: unsupported credit role `{role}`")

            if not isinstance(credit.get("scope"), str) or not credit["scope"].strip():
                self.error(registry_path, f"{bundle_id}: credit `{profile_id}` needs a specific `scope`")
            reviewed_at = str(credit.get("reviewed_at", ""))
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", reviewed_at) is None:
                self.error(registry_path, f"{bundle_id}: credit `{profile_id}` needs `reviewed_at` as YYYY-MM-DD")

    def validate_content_risk(
        self,
        registry_path: Path,
        bundle: dict[str, Any],
        contributors: dict[str, dict[str, Any]],
    ) -> None:
        bundle_id = str(bundle.get("id", ""))
        content_risk = bundle.get("content_risk")
        if content_risk is None:
            return
        if not isinstance(content_risk, dict):
            self.error(registry_path, f"{bundle_id}: `content_risk` must be an object")
            return

        classification = content_risk.get("classification")
        if classification not in CONTENT_RISK_CLASSIFICATIONS:
            self.error(registry_path, f"{bundle_id}: unsupported content-risk classification `{classification}`")

        domains = content_risk.get("domains", [])
        if not self.is_string_list(domains) or not domains:
            self.error(registry_path, f"{bundle_id}: `content_risk.domains` needs at least one domain")
        else:
            for domain in sorted(set(domains) - CONTENT_RISK_DOMAINS):
                self.error(registry_path, f"{bundle_id}: unsupported content-risk domain `{domain}`")

        review = content_risk.get("professional_review")
        if not isinstance(review, dict):
            self.error(registry_path, f"{bundle_id}: `professional_review` must be an object")
            return

        status = review.get("status")
        if status not in PROFESSIONAL_REVIEW_STATUSES:
            self.error(registry_path, f"{bundle_id}: unsupported professional-review status `{status}`")
        if not isinstance(review.get("required_qualification"), str) or not review["required_qualification"].strip():
            self.error(registry_path, f"{bundle_id}: professional review needs `required_qualification`")

        roles = {
            role
            for credit in bundle.get("credits", [])
            if isinstance(credit, dict)
            for role in credit.get("roles", [])
            if isinstance(role, str)
        }
        if status == "technical_only" and "technical_reviewer" not in roles:
            self.error(registry_path, f"{bundle_id}: `technical_only` needs a technical-reviewer credit")
        if status == "domain_reviewed" and "domain_reviewer" not in roles:
            self.error(registry_path, f"{bundle_id}: `domain_reviewed` needs a domain-reviewer credit")
        if status == "domain_reviewed":
            risk_domains = set(domains) if self.is_string_list(domains) else set()
            reviewer_ids = {
                str(credit.get("profile_id", ""))
                for credit in bundle.get("credits", [])
                if isinstance(credit, dict) and "domain_reviewer" in credit.get("roles", [])
            }
            has_verified_credential = any(
                risk_domains.intersection(credential.get("domains", []))
                for reviewer_id in reviewer_ids
                for credential in contributors.get(reviewer_id, {}).get("professional_credentials", [])
                if isinstance(credential, dict)
            )
            if not has_verified_credential:
                self.error(
                    registry_path,
                    f"{bundle_id}: `domain_reviewed` needs a matching verified professional credential",
                )

    def validate_bundle_files(self, bundle: dict[str, Any]) -> None:
        bundle_id = str(bundle.get("id", ""))
        category = str(bundle.get("category", ""))
        rel_root = Path(str(bundle.get("path", "")))
        root = self.root / rel_root

        if not root.is_dir():
            self.error(rel_root, f"{bundle_id}: bundle path does not exist")
            return

        required_files = ["index.md", "log.md"]
        core_file = CORE_FILES.get(category)
        if core_file is not None:
            required_files.append(core_file)

        for filename in required_files:
            if not (root / filename).is_file():
                self.error(rel_root / filename, f"{bundle_id}: missing required file")

        for md_file in sorted(root.rglob("*.md")):
            self.validate_markdown_file(md_file, bundle_id)
            self.validate_internal_links(md_file)

    def validate_markdown_file(self, path: Path, bundle_id: str) -> None:
        text = path.read_text(encoding="utf-8")
        frontmatter = self.frontmatter(text)
        if frontmatter is None:
            self.error(path, f"{bundle_id}: markdown file is missing YAML frontmatter")
            return
        if not re.search(r"(?m)^type:\s*.+$", frontmatter):
            self.error(path, f"{bundle_id}: frontmatter is missing `type`")
        if "okb_bundle_id:" in frontmatter and f"okb_bundle_id: {bundle_id}" not in frontmatter:
            self.warning(path, f"{bundle_id}: okb_bundle_id does not exactly match bundle id")

    def validate_internal_links(self, path: Path) -> None:
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            raw_target = match.group(1).strip()
            if not raw_target or raw_target.startswith(("#", "mailto:", "http://", "https://")):
                continue
            target = raw_target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            target = unquote(target)
            candidate = (self.root / target.lstrip("/")) if target.startswith("/") else (path.parent / target)
            if not candidate.exists():
                self.error(path, f"broken internal link: {raw_target}")

    def validate_relationships(self, registry_path: Path, bundles: list[Any], ids: set[str]) -> None:
        for bundle in bundles:
            if not isinstance(bundle, dict):
                continue
            bundle_id = str(bundle.get("id", ""))
            for field in ["related_bundles", "adjacent_bundles"]:
                values = bundle.get(field, [])
                if values is None:
                    continue
                if not self.is_string_list(values):
                    self.error(registry_path, f"{bundle_id}: `{field}` must be an array of bundle ids")
                    continue
                missing = sorted(set(values) - ids)
                for missing_id in missing:
                    self.warning(registry_path, f"{bundle_id}: `{field}` references unknown bundle `{missing_id}`")

    def scan_public_content(self) -> None:
        scan_roots = [self.root / "bundles", self.root / "registry"]
        for scan_root in scan_roots:
            if not scan_root.exists():
                continue
            for path in sorted(item for item in scan_root.rglob("*") if item.is_file()):
                if path.suffix not in {".md", ".json", ".txt", ".yml", ".yaml"}:
                    continue
                text = path.read_text(encoding="utf-8", errors="replace")
                for pattern, label in PRIVATE_OR_SECRET_PATTERNS:
                    if pattern.search(text):
                        self.error(path, f"possible {label} in public content")

    def report(self) -> int:
        errors = [item for item in self.findings if item.level == "error"]
        warnings = [item for item in self.findings if item.level == "warning"]

        for item in self.findings:
            print(f"{item.level.upper()}: {item.path}: {item.message}")

        print(f"\nValidation complete: {len(errors)} errors, {len(warnings)} warnings")
        return 1 if errors else 0

    @staticmethod
    def frontmatter(text: str) -> str | None:
        if not text.startswith("---\n"):
            return None
        end = text.find("\n---", 4)
        if end == -1:
            return None
        return text[4:end]

    @staticmethod
    def is_string_list(value: Any) -> bool:
        return isinstance(value, list) and all(isinstance(item, str) for item in value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root to validate.")
    args = parser.parse_args()

    return Validator(args.root).validate()


if __name__ == "__main__":
    sys.exit(main())

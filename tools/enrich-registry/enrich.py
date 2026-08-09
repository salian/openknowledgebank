#!/usr/bin/env python3
"""Build source-derived bundle landing metadata without inventing claims."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))

from content_risk import infer_content_risk  # noqa: E402


REGISTRY_PATH = ROOT / "registry" / "bundles.json"
REPOSITORY_BLOB = "https://github.com/salian/openknowledgebank/blob/main/"
REPOSITORY_TREE = "https://github.com/salian/openknowledgebank/tree/main/"

CATEGORY_DEFINITIONS = {
    "roles": "A free, open-source set of {count} Markdown files that gives an AI assistant practical guidance for the {title} role.",
    "tools": "A free, open-source set of {count} Markdown files for planning, reviewing, and carrying out evidence-based work with {title}.",
    "frameworks": "A free, open-source set of {count} Markdown files that shows an AI assistant how to apply {title} to evidence, decisions, and reviewable outputs.",
    "compliance": "A free, open-source set of {count} Markdown files for triaging {title} questions against current sources and the facts of a specific situation.",
    "deliverables": "A free, open-source set of {count} Markdown files for drafting and reviewing {title} with explicit evidence, constraints, and approval boundaries.",
}

CATEGORY_AUDIENCES = {
    "roles": "People performing or supporting {title} work, plus teams reviewing its decisions and outputs",
    "tools": "People who configure, operate, integrate, govern, or review work performed in {title}",
    "frameworks": "Practitioners using {title} to structure analysis, decisions, facilitation, or review",
    "compliance": "Compliance, legal, risk, security, operations, and product teams assessing {title}",
    "deliverables": "People drafting, reviewing, approving, or relying on {title}",
}

CATEGORY_INPUTS = {
    "roles": [
        "The task objective, intended audience, working context, constraints, source material, and decision owner.",
        "Relevant reports, exports, examples, policies, prior decisions, and success measures available for the task.",
    ],
    "tools": [
        "The product version or workspace scope, relevant configuration or export, desired outcome, permissions, and accountable owner.",
        "Current IDs, settings, records, logs, screenshots, integration details, and test evidence needed to verify the requested change.",
    ],
    "frameworks": [
        "The decision or question, available evidence, operating constraints, affected stakeholders, and desired outcome.",
        "Existing analysis, definitions, assumptions, examples, and review criteria that the framework must reconcile.",
    ],
    "compliance": [
        "The jurisdiction, entity and relationship facts, applicable dates, exact question, and accountable professional reviewer.",
        "Current official sources plus the policies, contracts, records, system evidence, and missing facts relevant to the situation.",
    ],
    "deliverables": [
        "The document purpose, audience, source evidence, required sections, constraints, approvers, and intended decision or action.",
        "Existing drafts, templates, policies, examples, terminology, and review criteria that the output must follow.",
    ],
}

CATEGORY_NOT_FOR = {
    "roles": "Treating the bundle as a substitute for organization-specific authority, firsthand evidence, or accountable review.",
    "tools": "Changing live configuration, records, permissions, automations, integrations, or shared data without verified scope, testing, rollback, and approval.",
    "frameworks": "Applying the framework mechanically when the decision requires missing evidence, stakeholder judgment, or qualified review.",
    "compliance": "Final legal or compliance conclusions, filings, notices, or operational changes without current source review and accountable professional approval.",
    "deliverables": "Publishing, approving, or acting on a draft before its material claims, source evidence, owners, and approval gates have been reviewed.",
}

CATEGORY_WHEN_TO_USE = {
    "roles": [
        "A {title} task needs a structured plan, evidence checklist, or review-ready output.",
        "A recommendation needs its assumptions, owners, risks, dependencies, and success measures made explicit.",
    ],
    "tools": [
        "A proposed {title} configuration or workflow change needs current IDs, permissions, dependencies, tests, and rollback evidence.",
        "A report, export, integration, or automation result needs to be reconciled against actual workspace state and current product documentation.",
    ],
    "frameworks": [
        "A team needs to apply {title} to a concrete decision without skipping evidence, constraints, or stakeholder judgment.",
        "An existing analysis needs its assumptions, reasoning, affected parties, and review criteria checked.",
    ],
    "compliance": [
        "A {title} question needs to be scoped to the correct rule, guidance, regulator, date, and affected entity.",
        "A draft conclusion needs its stated facts, missing evidence, source citations, and professional-review handoff checked.",
    ],
    "deliverables": [
        "A {title} draft needs a clear purpose, audience, evidence base, structure, and approval path.",
        "An existing draft needs unsupported claims, missing sections, unresolved decisions, and reviewer comments addressed.",
    ],
}

CATEGORY_SOURCE_USE = {
    "roles": "Role or occupation reference",
    "tools": "Product, platform, or operating reference",
    "frameworks": "Method, standard, or practice reference",
    "compliance": "Legal, regulatory, standards, or agency reference",
    "deliverables": "Format, practice, or subject-matter reference",
}

DOMAIN_LABELS = {
    "onetonline.org": "O*NET OnLine",
    "ecfr.gov": "Electronic Code of Federal Regulations",
    "finra.org": "FINRA",
    "fda.gov": "U.S. Food and Drug Administration",
    "ftc.gov": "U.S. Federal Trade Commission",
    "sec.gov": "U.S. Securities and Exchange Commission",
    "epa.gov": "U.S. Environmental Protection Agency",
    "eeoc.gov": "U.S. Equal Employment Opportunity Commission",
    "dol.gov": "U.S. Department of Labor",
    "hud.gov": "U.S. Department of Housing and Urban Development",
    "hhs.gov": "U.S. Department of Health and Human Services",
    "nist.gov": "NIST",
    "w3.org": "W3C",
    "legislation.gov.uk": "UK Legislation",
    "gov.uk": "GOV.UK",
    "learn.microsoft.com": "Microsoft Learn",
    "docs.github.com": "GitHub Docs",
    "developers.google.com": "Google for Developers",
    "support.google.com": "Google Help",
    "docs.aws.amazon.com": "AWS Documentation",
    "cloud.google.com": "Google Cloud Documentation",
    "airtable.com": "Airtable developer documentation",
    "support.airtable.com": "Airtable Support",
    "esco.ec.europa.eu": "European Commission ESCO",
    "data.europa.eu": "European Data Portal",
}

FEATURE_PRIORITY = {
    "roles": ["role.md", "overview.md", "workflows", "frameworks", "deliverables", "evaluations", "references"],
    "tools": ["tool.md", "overview.md", "workflows", "deliverables", "evaluations", "references"],
    "frameworks": ["framework.md", "overview.md", "workflows", "deliverables", "evaluations", "references"],
    "compliance": ["overview.md", "requirements", "workflows", "deliverables", "evaluations", "references"],
    "deliverables": ["deliverable.md", "overview.md", "workflows", "requirements", "evaluations", "references"],
}


def clean_sentence(value: object) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    text = re.sub(r"\ba ([aeiouAEIOU])", r"an \1", text)
    return text


def clause(value: object) -> str:
    text = clean_sentence(value).rstrip(". ;")
    return text[:1].lower() + text[1:] if text else ""


def join_clauses(values: list[str]) -> str:
    values = [clause(value) for value in values if clause(value)]
    if len(values) == 1:
        return values[0]
    if len(values) == 2:
        return f"{values[0]} and {values[1]}"
    return "; ".join(values[:-1]) + f"; and {values[-1]}"


def join_items(values: list[str]) -> str:
    values = [clean_sentence(value) for value in values if clean_sentence(value)]
    if not values:
        return ""
    if len(values) == 1:
        return values[0]
    if len(values) == 2:
        return f"{values[0]} and {values[1]}"
    return ", ".join(values[:-1]) + f", and {values[-1]}"


def truncate(text: str, limit: int) -> str:
    text = clean_sentence(text)
    if len(text) <= limit:
        return text
    candidate = text[: limit + 1]
    sentence_ends = [match.end() for match in re.finditer(r"[.!?](?=\s|$)", candidate)]
    if sentence_ends and sentence_ends[-1] >= int(limit * 0.55):
        return candidate[: sentence_ends[-1]].strip()
    shortened = candidate.rsplit(" ", 1)[0].rstrip(" ,;:-")
    return shortened.rstrip(".") + "."


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.+?)\s*$", line)
        if not match:
            continue
        value = match.group(2).strip().strip("\"'")
        if value and not value.startswith("[") and not value.startswith("{"):
            values[match.group(1)] = value
    return values


def markdown_body(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end >= 0:
            text = text[end + 4 :]
    text = re.sub(r"^#.*$", "", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`>#]", "", text)
    return clean_sentence(text)


def first_content_block(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end >= 0:
            text = text[end + 4 :]
    text = re.sub(r"^#\s+.*$", "", text, count=1, flags=re.MULTILINE).strip()
    block = re.split(r"\n\s*##\s+", text, maxsplit=1)[0]
    return markdown_body(block)


def file_metadata(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    meta = frontmatter(text)
    title = clean_sentence(meta.get("title", ""))
    if not title:
        heading = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        title = clean_sentence(heading.group(1) if heading else path.stem.replace("-", " ").title())
    description = clean_sentence(meta.get("description", ""))
    if not description:
        description = truncate(first_content_block(text), 190)
    return title, description


def feature_type(path: Path, bundle_dir: Path) -> str:
    relative = path.relative_to(bundle_dir)
    if len(relative.parts) == 1:
        return {
            "role.md": "Role guide",
            "tool.md": "Tool guide",
            "framework.md": "Framework guide",
            "deliverable.md": "Deliverable guide",
            "overview.md": "Overview",
        }.get(path.name, "Bundle file")
    return {
        "workflows": "Workflow",
        "frameworks": "Framework",
        "deliverables": "Template",
        "requirements": "Requirements map",
        "evaluations": "Quality rubric",
        "references": "Source notes",
        "examples": "Worked example",
        "tools": "Tool guide",
    }.get(relative.parts[0], "Bundle file")


def select_features(bundle_dir: Path, category: str) -> list[dict[str, str]]:
    candidates = [
        path
        for path in bundle_dir.rglob("*.md")
        if path.name not in {"index.md", "log.md"} and "examples" not in path.parts
    ]
    priorities = FEATURE_PRIORITY.get(category, ["overview.md", "workflows", "deliverables", "evaluations"])

    def rank(path: Path) -> tuple[int, str]:
        relative = path.relative_to(bundle_dir)
        keys = [path.name, relative.parts[0]]
        score = min((priorities.index(key) for key in keys if key in priorities), default=len(priorities))
        return score, str(relative)

    selected: list[Path] = []
    used_types: set[str] = set()
    for path in sorted(candidates, key=rank):
        kind = feature_type(path, bundle_dir)
        if kind in used_types and len(selected) < 2:
            continue
        selected.append(path)
        used_types.add(kind)
        if len(selected) == 4:
            break

    features = []
    for path in selected:
        title, description = file_metadata(path)
        if not description:
            continue
        relative = path.relative_to(ROOT).as_posix()
        features.append(
            {
                "type": feature_type(path, bundle_dir),
                "title": title,
                "description": truncate(description, 210),
                "url": REPOSITORY_BLOB + relative,
            }
        )
    return features


def body_from(path: Path, limit: int, first_block: bool = False) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="ignore")
    body = first_content_block(text) if first_block else markdown_body(text)
    body = re.sub(r"\s*Measured model scoring is planned separately\..*$", "", body)
    return truncate(body, limit)


def before_after(bundle_dir: Path) -> dict[str, str] | None:
    roots = sorted((bundle_dir / "examples" / "before-after").glob("*"))
    for root in roots:
        if not root.is_dir():
            continue
        task = body_from(root / "task.md", 360, first_block=True)
        baseline = body_from(root / "baseline-output.md", 460, first_block=True)
        assisted = body_from(root / "bundle-assisted-output.md", 700)
        explanation = body_from(root / "evaluation.md", 420)
        if not all([task, baseline, assisted, explanation]):
            continue
        return {
            "task": task,
            "baseline": baseline,
            "assisted": assisted,
            "why_it_matters": explanation,
            "source_url": REPOSITORY_TREE + root.relative_to(ROOT).as_posix(),
        }
    return None


def source_label(url: str, files: list[Path]) -> str:
    escaped = re.escape(url)
    generic_labels = {
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

    def is_meaningful(label: str) -> bool:
        return not label.startswith("http") \
            and label.lower() not in generic_labels \
            and re.fullmatch(r"(?:www\.)?[a-z0-9.-]+\.[a-z]{2,}", label.lower()) is None

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        markdown_link = re.search(rf"\[([^\]]{{3,100}})\]\({escaped}\)", text)
        if markdown_link:
            label = clean_sentence(markdown_link.group(1))
            if is_meaningful(label):
                return label
        line_label = re.search(rf"^[-*]?\s*([^\n:]{{3,100}}):\s*{escaped}", text, re.MULTILINE)
        if line_label:
            label = clean_sentence(line_label.group(1)).lstrip("- ")
            if is_meaningful(label):
                return label
    host = (urlparse(url).hostname or url).removeprefix("www.").lower()
    base = DOMAIN_LABELS.get(host, host)
    parsed = urlparse(url)

    def humanize(segment: str) -> str:
        segment = re.sub(r"\.(?:html?|xhtml|pdf)$", "", segment, flags=re.IGNORECASE)
        words = re.sub(r"[-_]+", " ", segment).split()
        acronyms = {"api", "faq", "cfr", "hipaa", "ffiec", "sec", "fda", "xbrl", "xml", "gaap"}
        return " ".join(word.upper() if word.lower() in acronyms else word[:1].upper() + word[1:] for word in words)

    segments = [
        humanize(unquote(segment)).strip()
        for segment in parsed.path.split("/")
        if segment and segment.lower() not in {"index", "index.html", "about", "overview", "introduction"}
    ]
    detail = " / ".join(segments[-2:])
    if detail and normalized(detail) not in normalized(base):
        return f"{base} — {detail[:1].upper() + detail[1:]}"
    return base


def extract_urls(files: list[Path]) -> list[str]:
    urls: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for url in re.findall(r"https?://[^\s)>\]\"']+", text):
            urls.append(url.rstrip(".,;"))
    return urls


def source_notes(bundle: dict, files: list[Path], category: str) -> list[dict[str, str]]:
    urls = [str(url) for url in bundle.get("source_urls", []) if str(url).startswith("http")]
    if not urls:
        urls = extract_urls(files)
    selected: list[str] = []
    for url in urls:
        host = (urlparse(url).hostname or "").lower()
        if host.endswith("github.com") and "salian/openknowledgebank" in url:
            continue
        if url not in selected:
            selected.append(url)
        if len(selected) == 5:
            break
    title = clean_sentence(bundle.get("title", "this bundle"))

    def used_for(url: str) -> str:
        host = (urlparse(url).hostname or "").removeprefix("www.").lower()
        if category == "roles" and host not in {"onetonline.org", "bls.gov"}:
            return (
                f"Practice or subject-matter reference for {title} methods, "
                "constraints, and source checks."
            )
        category_use = CATEGORY_SOURCE_USE.get(
            category,
            "Public reference named by the bundle.",
        )
        return f"{category_use.rstrip('.')} for {title} scope and source checks."

    return [
        {"label": source_label(url, files), "url": url, "used_for": used_for(url)}
        for url in selected
    ]


def landing_page(bundle: dict, bundle_dir: Path) -> dict:
    category = str(bundle.get("category", ""))
    title = clean_sentence(bundle.get("title", "Bundle"))
    aliases = [clean_sentence(item) for item in bundle.get("aliases", []) if clean_sentence(item)]
    compact_title = re.sub(r"[^A-Za-z0-9]", "", title)
    context_title = f"{title} ({aliases[0]})" if len(compact_title) <= 4 and aliases else title
    files = sorted(bundle_dir.rglob("*.md"))
    problems = [clean_sentence(item) for item in bundle.get("problems_solved", []) if clean_sentence(item)]
    outputs = [clean_sentence(item) for item in bundle.get("deliverables", []) if clean_sentence(item)]
    features = select_features(bundle_dir, category)
    sources = source_notes(bundle, files, category)

    definition_template = CATEGORY_DEFINITIONS.get(
        category,
        "A free, open-source set of {count} Markdown files for evidence-based work with {title}.",
    )
    definition = definition_template.format(count=len(files), title=context_title)

    article_for = lambda value: ("an " if value[:1].lower() in "aeiou" else "a ") + value.lower()
    feature_types = []
    for feature in features:
        kind = clean_sentence(feature["type"])
        if kind and kind not in feature_types:
            feature_types.append(kind)
    preview_names = join_items([article_for(kind) for kind in feature_types[:4]]) or "inspectable bundle files"
    output_names = join_items(outputs[:2]) or "a reviewable recommendation"
    summary = {
        "roles": f"Use this bundle to plan and review {context_title} work with evidence, assumptions, owners, and review points made explicit.",
        "tools": f"Use this bundle to plan or review work in {context_title} before changing live data or configuration.",
        "frameworks": f"Use this bundle to apply {context_title} to a concrete question while keeping evidence, assumptions, stakeholder judgment, and review criteria visible.",
        "compliance": f"Use this bundle to scope {context_title} questions to the relevant source, case facts, and review owner; it does not provide a final legal or compliance conclusion.",
        "deliverables": f"Use this bundle to draft or review {context_title} with source evidence, open questions, owners, and approval gates kept explicit.",
    }.get(category, clean_sentence(bundle.get("description", "")))
    summary += f" The page previews {preview_names}; the intended output is {output_names}."
    if sources:
        summary += f" Start source review with {sources[0]['label']}."
    summary = truncate(summary, 430)

    audience_template = CATEGORY_AUDIENCES.get(category, "People working with {title}")
    audiences = [audience_template.format(title=context_title)]
    industries = [clean_sentence(item) for item in bundle.get("industries", []) if clean_sentence(item)]
    if industries:
        audiences.append("Teams working in " + ", ".join(industries[:3]))

    required_inputs = CATEGORY_INPUTS.get(
        category,
        [
            "The exact task, intended audience, available evidence, operating constraints, and accountable decision owner.",
            "Relevant reports, examples, policies, prior decisions, and review criteria.",
        ],
    )
    output_clause = outputs[0] if outputs else "a reviewable recommendation"
    input_clause = required_inputs[0].rstrip(".")
    input_clause = re.sub(r"^The\s+", "the ", input_clause)
    agent_example = {
        "roles": f"Provide {input_clause}. Ask the agent to approach {context_title} work by producing {output_clause} with a prioritized plan, evidence checks, owners, risks, and unresolved questions.",
        "tools": f"Provide {input_clause}. Ask the agent to review {context_title} and produce {output_clause} that maps configuration evidence, dependencies, permissions, tests, rollback, and actions that still require approval.",
        "frameworks": f"Provide {input_clause}. Ask the agent to apply {context_title} and produce {output_clause} that shows how evidence maps to the framework, where judgment is required, and what remains unresolved.",
        "compliance": f"Provide {input_clause}. Ask the agent to assess {context_title} and draft {output_clause} that separates stated facts, assumptions, missing evidence, relevant source sections, and actions requiring professional approval.",
        "deliverables": f"Provide {input_clause}. Ask the agent to draft or review {context_title} and return {output_clause} with material claims tied to evidence and assumptions, open questions, reviewers, and approval gates marked.",
    }.get(category, f"Provide {input_clause}. Ask the agent for {output_clause} with evidence for material claims and a list of unresolved questions.")
    if sources:
        agent_example += f" Begin with {sources[0]['label']}, then confirm that the reference is current and applicable."
    if features:
        agent_example += f" Inspect {features[0]['title']} before drafting."

    not_for = [CATEGORY_NOT_FOR.get(category, f"Using {title} without the evidence, context, or review required for the decision.")]

    output_for_meta = join_clauses(outputs[:2]) if outputs else "reviewable guidance"
    meta_description = truncate(
        f"Free {title} Markdown bundle with workflows, source references, and {output_for_meta} for use with AI assistants.",
        155,
    )
    social_summary = truncate(
        f"{title}: {join_clauses(outputs[:2]) if outputs else join_clauses(problems[:1])}, workflows, and review guidance",
        104,
    )
    words = sum(len(re.findall(r"\b[\w'-]+\b", path.read_text(encoding="utf-8", errors="ignore"))) for path in files)
    download_note = f"{len(files)} Markdown files · {words:,} words · no signup · {bundle.get('license', 'CC BY 4.0')}"

    landing = {
        "definition": definition,
        "summary": summary,
        "meta_description": meta_description,
        "social_summary": social_summary,
        "download_note": download_note,
        "audiences": audiences,
        "when_to_use": [item.format(title=context_title) for item in CATEGORY_WHEN_TO_USE.get(category, problems[:2])],
        "required_inputs": required_inputs,
        "agent_use_example": agent_example,
        "not_for": not_for,
        "featured_contents": features,
    }
    example = before_after(bundle_dir)
    if example:
        landing["before_after"] = example
    if sources:
        landing["source_notes"] = sources
    return landing


def tokens(values: object) -> set[str]:
    if not isinstance(values, list):
        return set()
    return {
        token
        for value in values
        for token in re.findall(r"[a-z0-9]+", str(value).lower())
        if len(token) >= 3
    }


def assign_adjacencies(bundles: list[dict], excluded: set[str]) -> int:
    public = [bundle for bundle in bundles if is_public(bundle) and str(bundle.get("id", "")) not in excluded]
    added = 0
    for bundle in public:
        if bundle.get("related_bundles") or bundle.get("adjacent_bundles"):
            continue
        category = str(bundle.get("category", ""))
        bundle_terms = tokens(bundle.get("tags", [])) | tokens(bundle.get("industries", []))
        bundle_terms |= tokens(bundle.get("tools", [])) | tokens(bundle.get("frameworks", []))
        candidates = []
        for candidate in public:
            if candidate is bundle or str(candidate.get("category", "")) != category:
                continue
            candidate_terms = tokens(candidate.get("tags", [])) | tokens(candidate.get("industries", []))
            candidate_terms |= tokens(candidate.get("tools", [])) | tokens(candidate.get("frameworks", []))
            overlap = len(bundle_terms & candidate_terms)
            score = overlap * 10 + len(tokens(bundle.get("tags", [])) & tokens(candidate.get("tags", []))) * 5
            candidates.append((-score, str(candidate.get("id", ""))))
        candidates.sort()
        adjacent = [candidate_id for _, candidate_id in candidates[:3] if candidate_id]
        if adjacent:
            bundle["adjacent_bundles"] = adjacent
            added += 1
    return added


def is_public(bundle: dict) -> bool:
    return bundle.get("status") not in {"draft", "deprecated"} and bundle.get("trust_tier") not in {
        "unverified",
        "rejected",
    }


def normalized(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Rewrite the registry in place.")
    parser.add_argument("--registry", default=str(REGISTRY_PATH), help="Registry JSON to read and optionally rewrite.")
    parser.add_argument(
        "--include-id",
        action="append",
        default=[],
        help="Enrich only this bundle id. Repeat for a cohort; omit to process every public bundle.",
    )
    parser.add_argument("--exclude-id", action="append", default=[], help="Leave this bundle unchanged.")
    args = parser.parse_args()

    registry_path = Path(args.registry).resolve()
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    included = set(args.include_id)
    excluded = set(args.exclude_id)
    registry_ids = {str(bundle.get("id", "")) for bundle in registry.get("bundles", [])}
    unknown_included = sorted(included - registry_ids)
    if unknown_included:
        print(json.dumps({"error": "unknown include ids", "ids": unknown_included}, indent=2))
        return 1
    if included:
        excluded |= registry_ids - included
    enriched = 0
    skipped_existing = 0
    augmented_existing = 0
    content_risks_added = 0
    skipped_excluded = 0
    failures: list[str] = []

    for bundle in registry.get("bundles", []):
        bundle_id = str(bundle.get("id", ""))
        if bundle_id in excluded or not is_public(bundle):
            skipped_excluded += 1
            continue
        inferred_risk = infer_content_risk(bundle)
        if inferred_risk is not None and not isinstance(bundle.get("content_risk"), dict):
            bundle["content_risk"] = inferred_risk
            content_risks_added += 1
        bundle_dir = ROOT / str(bundle.get("path", ""))
        if not bundle_dir.is_dir():
            failures.append(f"{bundle_id}: bundle directory missing")
            continue
        is_generated = bundle.get("indexing", {}).get("reviewed_by") == "OpenKnowledgeBank source-derived review"
        if bundle.get("landing_page") and not is_generated:
            derived = landing_page(bundle, bundle_dir)
            additions = {
                key: value
                for key, value in derived.items()
                if key not in bundle["landing_page"]
                and key in {
                    "definition",
                    "meta_description",
                    "social_summary",
                    "download_note",
                    "featured_contents",
                    "before_after",
                    "source_notes",
                }
            }
            bundle["landing_page"].update(additions)
            bundle.setdefault("indexing", {})["content_standard"] = "bundle-page-v1"
            if additions:
                augmented_existing += 1
            else:
                skipped_existing += 1
            continue
        landing = landing_page(bundle, bundle_dir)
        if len(landing.get("featured_contents", [])) < 1:
            failures.append(f"{bundle_id}: no representative content file")
            continue
        if len(landing.get("summary", "")) < 120:
            failures.append(f"{bundle_id}: summary shorter than 120 characters")
            continue
        previous_reviewed_at = bundle.get("indexing", {}).get("reviewed_at")
        bundle["landing_page"] = landing
        bundle["indexing"] = {
            "disposition": "index-ready",
            "reviewed_by": "OpenKnowledgeBank source-derived review",
            "reviewed_at": previous_reviewed_at or date.today().isoformat(),
            "notes": "Landing content derived from the bundle's registry metadata and published Markdown files; quantitative private evaluation claims remain unpublished.",
            "content_standard": "bundle-page-v1",
        }
        enriched += 1

    adjacencies_added = assign_adjacencies(registry.get("bundles", []), excluded)

    summary_owners: dict[str, list[str]] = {}
    for bundle in registry.get("bundles", []):
        summary = normalized(bundle.get("landing_page", {}).get("summary", ""))
        if summary:
            summary_owners.setdefault(summary, []).append(str(bundle.get("id", "")))
    duplicate_groups = [owners for owners in summary_owners.values() if len(owners) > 1]
    duplicate_summaries = sum(len(owners) - 1 for owners in duplicate_groups)
    report = {
        "requested_ids": sorted(included),
        "enriched": enriched,
        "augmented_existing": augmented_existing,
        "content_risks_added": content_risks_added,
        "preserved_existing": skipped_existing,
        "excluded_or_unpublished": skipped_excluded,
        "adjacency_sets_added": adjacencies_added,
        "failures": failures,
        "exact_duplicate_summaries": duplicate_summaries,
        "duplicate_summary_ids": duplicate_groups,
    }
    print(json.dumps(report, indent=2))

    if failures or duplicate_summaries:
        return 1
    if args.write:
        if enriched or augmented_existing or content_risks_added or adjacencies_added:
            registry["updated"] = date.today().isoformat()
        registry_path.write_text(
            json.dumps(registry, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

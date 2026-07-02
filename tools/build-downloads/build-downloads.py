#!/usr/bin/env python3
"""Build per-bundle download zips and keep registry download_urls canonical.

For every bundle in registry/bundles.json this:
  1. zips the bundle's directory (registry entry `path`) to
     downloads/<id>.zip — the archive's top-level folder is <id>/ so it extracts
     into a clean bundle directory.
  2. rewrites the entry's `download_url` to the canonical per-bundle URL
     https://openknowledgebank.com/downloads/<id>.zip (the "sync" step — this is
     what keeps download_url pointing at the single bundle, never the whole-repo
     archive; see specs/CANONICAL_BUNDLE_SCHEMA.md).

The downloads/ directory is a build artifact — add it to .gitignore; the zips are
published to openknowledgebank.com/downloads/, not committed to the repo.

Run from the public repo root:
    python3 tools/build-downloads/build-downloads.py            # dry-run
    python3 tools/build-downloads/build-downloads.py --apply    # write zips + sync registry
    python3 tools/build-downloads/build-downloads.py --check    # CI: fail if registry download_urls aren't canonical (no writes)
"""
from __future__ import annotations
import json, os, sys, zipfile
from datetime import date

# tools/build-downloads/ -> repo root
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRY = os.path.join(REPO, "registry", "bundles.json")
DOWNLOADS = os.path.join(REPO, "downloads")
BASE_URL = "https://openknowledgebank.com/downloads"

APPLY = "--apply" in sys.argv
CHECK = "--check" in sys.argv
RUN_DATE = os.environ.get("BUILD_DATE", date.today().isoformat())


def canonical_url(bundle_id: str) -> str:
    return f"{BASE_URL}/{bundle_id}.zip"


def zip_bundle(bundle_dir: str, bundle_id: str, out_path: str) -> tuple[int, int]:
    """Zip bundle_dir into out_path with top-level folder <id>/. Returns (files, bytes)."""
    files = 0
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _dirs, names in os.walk(bundle_dir):
            for name in sorted(names):
                if name == ".DS_Store":
                    continue
                abs_path = os.path.join(root, name)
                rel = os.path.relpath(abs_path, bundle_dir)
                zf.write(abs_path, arcname=os.path.join(bundle_id, rel))
                files += 1
    return files, os.path.getsize(out_path)


def main() -> None:
    if not os.path.exists(REGISTRY):
        print(f"registry not found: {REGISTRY}")
        sys.exit(1)
    reg = json.load(open(REGISTRY))
    entries = reg["bundles"]

    missing_dirs, url_fixes, built = [], [], []
    for e in entries:
        bid, path = e["id"], e.get("path", "")
        bundle_dir = os.path.join(REPO, path)
        if not path or not os.path.isdir(bundle_dir):
            missing_dirs.append(bid)
            continue
        want = canonical_url(bid)
        if e.get("download_url") != want:
            url_fixes.append((bid, e.get("download_url"), want))
        if APPLY:
            os.makedirs(DOWNLOADS, exist_ok=True)
            n, size = zip_bundle(bundle_dir, bid, os.path.join(DOWNLOADS, f"{bid}.zip"))
            built.append((bid, n, size))
            e["download_url"] = want

    if APPLY and (url_fixes or built):
        reg["updated"] = RUN_DATE
        json.dump(reg, open(REGISTRY, "w"), indent=2)
        open(REGISTRY, "a").write("\n")

    # ---- report ----
    mode = "APPLIED" if APPLY else ("CHECK" if CHECK else "DRY-RUN")
    print(f"# build-downloads — {RUN_DATE}  ({mode})\n")
    print(f"registry bundles: {len(entries)}")
    if missing_dirs:
        print(f"  MISSING bundle dirs (skipped): {', '.join(missing_dirs)}")
    if APPLY:
        total = sum(s for _i, _n, s in built)
        print(f"  built {len(built)} zips → downloads/  ({total/1024:.0f} KB total)")
        for bid, n, size in built:
            print(f"    {bid}.zip  ({n} files, {size/1024:.0f} KB)")
        print(f"  synced {len(url_fixes)} download_url(s) to canonical form")
    else:
        print(f"  {len(url_fixes)} download_url(s) not canonical"
              f"{' (would fix)' if not CHECK else ''}:")
        for bid, cur, want in url_fixes:
            print(f"    {bid}: {cur!r} → {want!r}")

    if CHECK and (url_fixes or missing_dirs):
        print("\nCHECK FAILED: registry has non-canonical download_urls or missing bundle dirs.")
        sys.exit(1)


if __name__ == "__main__":
    main()

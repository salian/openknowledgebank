# Build Downloads

Builds one downloadable zip per bundle and keeps each registry entry's
`download_url` canonical.

For every bundle in `registry/bundles.json`, it zips the bundle directory to
`downloads/<id>.zip` (archive top-level folder is `<id>/`, so it extracts into a
clean bundle directory) and rewrites `download_url` to
`https://openknowledgebank.com/downloads/<id>.zip`.

```sh
# from the repo root
python3 tools/build-downloads/build-downloads.py            # dry-run: report only
python3 tools/build-downloads/build-downloads.py --apply    # build zips + sync registry
python3 tools/build-downloads/build-downloads.py --check    # CI gate: non-zero exit if a download_url isn't canonical
```

- `downloads/` is a **build artifact** — it is gitignored; the zips are published
  to `openknowledgebank.com/downloads/`, not committed.
- Run `--check` in CI to guarantee `download_url` never drifts to the whole-repo
  archive (`.../archive/refs/heads/main.zip`), which would download the entire
  repository instead of the single bundle. See
  `specs/CANONICAL_BUNDLE_SCHEMA.md` for the convention.

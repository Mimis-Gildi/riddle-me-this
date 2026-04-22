# CHANGELOG.md

## [9.2.0] — Dead link audit and site content cleanup

- Full site link audit; fixed 8 confirmed dead links across 10 files.
- Fixed domain moves: `code.claude.ai` → `code.claude.com` (2 files), MCP docs `/overview` → `/introduction` (3 files), OSF preprint canonical URL (1 file).
- Fixed broken/malformed URLs: `localhost:4000` dev URL committed to source, Wikipedia trailing slash.
- Fixed defunct project links: Dolly HuggingFace 404 → Databricks blog; Open Assistant defunct site → GitHub repo (stale prose removed).
- Updated repo link: `ATTRIBUTIONS` → `ACKNOWLEDGMENTS` (URL and display text corrected in `support.adoc`).
- Unlinked `medium.asei.systems` references across 19 files — domain temporarily disconnected; display text preserved.

## [8.38.0] — Release pipeline end-to-end validation

- Validate the full release cycle: labeler, incrementer, releaser, resume link update.
- Resume revision date updated to April 19th, 2026.

## [7.15.0] — Fix release pipeline, temporal versioning, workflow hygiene

### Release Pipeline

- Fix `GH_TOKEN` authentication for `gh` CLI — `GITHUB_TOKEN` is not a shell env var on self-hosted runners
- Fix resume link auto-update — reusable workflow outputs weren't propagated, label check via API not event context
- Add artifact existence check before `gh release upload`
- Add `git fetch && git pull` before push steps to prevent stale local copy rejections
- Add `remote set-url` workaround for agents with alternative git implementations

### Temporal Versioning

- Add `synchronize` to PR events — minor bump on every push to PR branch
- Add `PR_SKIP` — push events defer to `pull_request synchronize` when PR exists
- Concurrency groups keyed on `github.head_ref || github.ref` with cancel-in-progress
- Reusable workflow outputs propagated via `workflow_call: outputs:`

### Workflow Hygiene

- Exclude `renovate/**` and `dependabot/**` from all workflow triggers across both repos
- Enforce `zsh -l` shell default on all workflows with run steps
- Remove unnecessary `ref:`, `token:`, `persist-credentials:` overrides from read-only checkouts
- Restore `ref:` on checkouts that push — not slop when the workflow writes to the branch
- Qodana: restrict to `synchronize` events, bump linter to 2025.3

### Resume

- Fix `J&J` ampersand XML parse warning in PDF generation
- Tighten header/footer height in theme

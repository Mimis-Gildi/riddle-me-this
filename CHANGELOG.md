# CHANGELOG.md

## [8.8.0] — Release pipeline end-to-end validation

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

## [4.5.0] — Resume refresh and CI/CD overhaul

Applied feedback from 11 reviewers. Rebuilt resume structure. Externalized CI/CD to fluffle.

### Resume

- Hero: restored original voice, added objective line — seeking a team to nurture, hands-on, in-code, long-term
- Products: removed negative framing ("failed," "mostly inoperable"), led with value and outcomes
- Protrack: rewrote to show the real contrast — team of 14 failed, solo rebuilt while live
- MATILDA: trimmed to one line with three exits
- Employment: merged ASE Inc. into one continuous entry (2017-Present)
- Deutsche Bank: rewrote to show the engineering ecosystem built, not the platform (that's in Products)
- Earlier Career: corrected fabricated claims, restored accurate content (pilot tenant, GNU, IBM 370/390, J&J)

### CI/CD

- All workflows externalized to Mimis-Gildi/fluffle reusable workflows
- Releaser now builds resume PDF and attaches to GitHub Release
- Qodana, stales, actions-prune, incrementer wired to fluffle

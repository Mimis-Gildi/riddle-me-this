# CHANGELOG.md

## [9.3.0] — Dead link audit and site content cleanup

- Full site link audit; fixed 8 confirmed dead links across 10 files.
- Fixed domain moves: `code.claude.ai` → `code.claude.com` (2 files), MCP docs `/overview` → `/introduction` (3 files), OSF preprint canonical URL (1 file).
- Fixed broken/malformed URLs: `localhost:4000` dev URL committed to source, Wikipedia trailing slash.
- Fixed defunct project links: Dolly HuggingFace 404 → Databricks blog; Open Assistant defunct site → GitHub repo (stale prose removed).
- Updated repo link: `ATTRIBUTIONS` → `ACKNOWLEDGMENTS` (URL and display text corrected in `support.adoc`).
- Unlinked `medium.asei.systems` references across 19 files — domain temporarily disconnected; display text preserved.

### Incrementer fixes

- Fixed `gh pr view` failing on GraphQL project-items permission — switched to `--json` query with explicit error handling.
- Fixed `${(C)TYPE}` commit message bug — zsh capitalization applied to GitHub-expanded literal instead of a shell variable.
- Added missing `force-minor` input to `workflow_call` definition.
- Added plain-text diagnostic traces for all driving values in the increment type selector.

## General Idea

We follow a convention for how release notes are published:

1. We pull releases out of the CHANGELOG.md matching on the title line containing version.
2. We periodically discard old releases; a blog site doesn't need historic babble.
3. We release from PR close action, not on `main` push as is more common.

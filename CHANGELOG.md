# CHANGELOG.md

## [10.8.0] — AI-maggedon 2026: surviving Agentic in plebs

- New long-form reflection "AI-maggedon 2026: Straight Talk" — five-section essay on the gap between recruiter hype and field reality (`site/_posts/2026-04-23-ai-maggedon.adoc`).
- New LinkedIn-facing synopsis with the Kimi-K2-Thinking rebuttal of the local-frontier myth (`site/_posts/2026-04-23-ai-maggedon-synopsis.adoc`).
- Section 5 (the field primer) extracted as a reusable fragment with shared link attributes (`site/_fragments/2026-04-23-ai-maggedon-primer.adoc` + `2026-04-23-ai-maggedon-primer-links.adoc`).
- Promoted "Local Models, Real Grief" from drafts and cross-referenced from the primer (`site/_posts/2026-01-27-local-models-grief.adoc`).
- MIT NANDA 95% citations refactored as reusable footnote attributes (`{fn-mit-genai-divide}`, `{fn-mit-hbr}`, `{fn-mit-fortune}`).
- John Frum effigy hero image added.
- Hero fragments and section-anchor attributes wired across the article, synopsis, and primer.

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

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

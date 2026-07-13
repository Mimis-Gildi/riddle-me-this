# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project

**Mímis Gildi** – a personal engineering blog publication system with a résumé.
AsciiDoc sources become a PDF (Gradle) and a Jekyll site.
Everything is `production`. Change propagation is `trunk`-based – one linear `main`, everything squashes to it.
All policy is `declarative` – there is NO 'build-script,' only `artifact manifest`
(`build.gradle.kts`, `site/_config.yml`).

## Parity

If it happens anywhere, it first happens under developer's fingers – in IDE.
Convenience functions live in `.run/`; all of them also run from text:

| Function                            | Expression                                                                   |
|-------------------------------------|------------------------------------------------------------------------------|
| `riddle-me-this`                    | `gradle clean build test`                                                    |
| `riddle-me-this PDF`, `Resume`      | `gradle asciidoctorPdf && open build/docs/asciidocPdf/VadimKuhay-Resume.pdf` |
| `Jekyll Site - Install` / `- Clean` | bundler dependencies / clean                                                 |
| `Jekyll Site Run`                   | local site                                                                   |
| `action update versions`            | test GH Action                                                               |

Cardinal sin: invoking _gradlew_ script – it's not for you.

## Environments

Declared in manifests, never assumed: `.sdkmanrc` (JVM), `site/.tool-versions` (Ruby),
`pyproject.toml` + conda env `ml` (Python). All environments are synonyms to each other.

## Research Tooling

- **YouTube transcript:** `bin/yt-transcript <url-or-id> [-t]` prints captions to stdout
  (via `youtube_transcript_api` in the `ml` env). Do **not** scrape – bare `api/timedtext`
  is token-gated (returns 0 bytes), and `yt-dlp`/`youtube-dl` are asdf-plugin-added but not installed.

## Collaboration Rules

@./TEAM_NORMS.adoc

Site content guidance: `site/CLAUDE.md`.

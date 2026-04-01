# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **Mímis Gildi** - a personal engineering blog publication system with a résumé.
It combines multi-format document generation (PDF, HTML), automated static site publishing via Jekyll,
and comprehensive CI/CD automation for some basic efficiency.

## Basic Concepts

This is a `trunk`-based development model, where all development occurs on a single main branch (`main`),
and feature branches are merged into it. This approach simplifies collaboration and reduces merge conflicts.
History is linear and so is versioning. All the GitHub Actions automation is geared to accomodate trunk.

## Build Commands

### Gradle (Primary Build System)

```zsh
./gradlew build                    # Full build
./gradlew asciidoctorPdf           # Generate resume PDF
./gradlew verifyJavaToolchain      # Report Java toolchain info
./gradlew dependencyUpdates        # Check for dependency updates
```


### Jekyll Site

```zsh
cd site
bundle install                                    # Install Ruby dependencies
JEKYLL_ENV=production bundle exec jekyll build    # Production build
bundle exec jekyll serve                          # Local development server
```

Site is a subproject -- governance is in it: when working on Site the directory `site/` is the context root.


## Architecture

### Component Structure

| Directory              | Purpose                                                              |
|------------------------|----------------------------------------------------------------------|
| `resume/`              | AsciiDoc resume source, fragments, and PDF themes                    |
| `site/`                | Jekyll static site with blog posts, pages, and minimal-mistakes theme|
| `src/main/sh/`         | Shell scripts for deployment and cleanup                             |
| `src/main/kotlin/`     | Kotlin bootstrap code                                                |
| `buildSrc/`            | Custom Gradle plugins (toolchain verification, dependency processing)|
| `.github/workflows/`   | CI/CD workflows                                                      |
| `.github/actions/`     | Custom composite GitHub Actions                                      |


### Tech Stack

- **JVM**: Java 21 (Temurin), Kotlin, Gradle (Kotlin DSL) -- demo applications; pending.
- **Ruby**: Ruby 3.3.5 exact and locked, Jekyll 4.4.1 with `jekyll-asciidoc` -- blogsite live.
- **Documents**: Asciidoctor (generates PDF, HTML) -- all documentation.
- **Tooling**: SDK Manager (`.sdkmanrc`) for version management of some core tools.
- **Tooling-Ruby**: `asdf` on certain agents but not all.

Note: Demo applications are maintained as long as the blog posts that reference or depend on those.


### Document Generation Flow

Single AsciiDoc source in `resume/` is transformed via Asciidoctor into PDF using themes in `resume/themes/`.
Common fragments are shared via `resume/fragments/`.


### CI/CD Architecture

The repository uses extensive GitHub Actions automation:

- **Auto-versioning**: Feature branches trigger semantic version bumps based on issue labels.
- **Self-hosted runners**: Configured with labels `jekyll` and `feature` for dedicated builds.
- **Security scanning**: CodeQL, Codacy, Qodana JVM Community (primary).
- **Deployment**: Jekyll site auto-publishes to GitHub Pages (default).


## Code Quality Configuration

- **Codacy** (`.codacy.yaml`): eslint-8, shellcheck, markdownlint, prettier, bandit, semgrep, detekt, pmd-7.
- **Qodana** (`qodana.yaml`): JetBrains JVM Community analysis with `qodana.recommended` profile.


## Key Configuration Files

| File                        | Purpose                                     |
|-----------------------------|---------------------------------------------|
| `build.gradle.kts`          | Gradle build with Asciidoctor configuration |
| `gradle/libs.versions.toml` | Version catalog for dependencies            |
| `site/_config.yml`          | Jekyll site configuration                   |
| `.sdkmanrc`                 | SDK Manager tool versions                   |
| `codacy.yaml`               | Codacy configuration for code quality       |
| `qodana.yaml`               | Qodana configuration for code quality       |
| `.factor12`                 | Factor12 configuration for CI/CD runners    |


## Content Conventions

- All documentation uses AsciiDoc format (`.adoc` files).
- Blog posts go in `site/_posts/` with front matter including categories and tags.
- Site uses `minimal-mistakes` theme (remote theme configuration).
- Custom Jekyll plugin at `site/_plugins/expand_nested_variable_filter.rb`.
- Primary AI Authoring with Claude Code (`CLAUDE.md`) persisted since v3.24.0.
- Extended AI Authoring with OpenCode (`AGENTS.md`) is excluded to not conflict with Claude Code.


## Writing Style

**When helping write blog content, read `site/CLAUDE.md` first.**

## Collaboration Rules

This entire repository is governed by strict Team Norms (`./TEAM_NORMS.adoc`) and Collaboration Philosophy.
Key concepts excerpt is right here:

**Read `TEAM_NORMS.adoc` at project root. These rules are non-negotiable.**

### Before Starting ANY Task

You MUST verify these before proceeding. If any is missing, STOP and fix it first:

1. **Value defined?** -- What do we get from closing this? Why do it?
2. **Outcome defined?** -- What does success look like? (One sentence!)
3. **Acceptance criteria listed?** -- How do we verify? (Checklist.)
4. **Verifier identified?** -- Who will review? (Not you.)
5. **Priority confirmed?** -- Is this the most important thing right now?

### Hard Rules

- **Never close issues.** Comment "ready for review" and wait.
- **Never start new work** while another task is in progress without explicit agreement.
- **Never assume work is correct** without human verification.
- **Document in issues**, not just conversation. Conversations are lost.

### When Unsure

Ask. A 30-second question prevents hours of wasted work.

### Team Structure

The team is flat. No hierarchy. No team member -- human or AI -- has authority over another.
Communication protocols exist for coordination, not control. We help and check on each other.

Priority disputes are resolved by consensus. If no consensus, the work waits.

## License

CC BY-NC-ND 4.0 (Creative Commons Attribution-NonCommercial-NoDerivatives)

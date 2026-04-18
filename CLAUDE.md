# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **Mímis Gildi** - a personal engineering blog publication system with a résumé.
It combines multi-format document generation (PDF, HTML), automated static site publishing via Jekyll,
and comprehensive CI/CD automation for some basic efficiency.

## Fluent Development

The project follows the hacker scene mindset, which is now the classic competence-based approach.
Key elements of fluent are:

- Everything is `production` - while rules like 12-factor-app exist to guide conservative teams, we just operate in a single environment;  
- Change propagation is `trunk`-based, all development occurs on a single _linear_ main branch (`main`), everything else squashes to it;
- All policy is `declarative` and all implementation is `functional` - there's NO 'build-script,' only `artifact manifest.` 

### Parity

If it happens anywhere, it first happens under developer's fingers; i.e., in IDE.
And then it happens everywhere only that way.
Here are convenience functions, all in `.run`.

1. Gradle Manifest:
   1. `riddle-me-this`  - a dependency;
   2. `riddle-me-this PDF` - document;
2. Ruby Manifest:
   1. `Jekyll Site - Install` - dependencies;
   2. `Jekyll Site - Clean` - bundler clean;
3. Composite Actions:
   1. `Resume` - use 1.2 and open preview;
   2. `Jekyll Site Run` - local site;
4. Testing:
   1. `action update versions` - test GH Action.

**IMPORTANT:** _**All the above functions will run from text.**_

### Activity

Terminal is everything, OS is the root IDE, mouse is for cats.

**WARNING:** _Running the below will create an action like above._

- `gradle clean build test` - 1.1 executes this expression.
- `gradle asciidoctorPdf && open build/docs/asciidocPdf/VadimKuhay-Resume.pdf` - 3.1 executes this expression.

Cardinal Sins:

- invoking _gradlew_ script - it's not for you.  

## Content Structure

| Directory            | Purpose                                                                 |
|----------------------|-------------------------------------------------------------------------|
| `resume/`            | AsciiDoc resume source, fragments, and PDF themes.                      |
| `site/`              | Jekyll static site with blog posts, pages, and minimal-mistakes theme.  |
| `src/main/kotlin/`   | Kotlin bootstrap code; TBD.                                             |
| `.github/workflows/` | Fluent expressions, most sources from organisation templates.           |
| `.github/actions/`   | Some local extension actions for project-specific manifest expressions. |


## Fixture Manifest

All environments are synonyms to each other.

- **Dependency Management:**
  - _**Conda Forge:**_
    - Python: 3.12.13
    - Environment: 'ml'
  - _**Ruby (multiple):**_
    - Ruby: 3.3.5
    - Manager Mac OS X: `asdf`
    - Manage Linux: `apt`
  - _**JVM SDKs:**_
    - SDKMAN: see `.sdkmanrc`
- **Authoring:**
  - AsciiDoctor, 
  - `gradle:org.asciidoctor.jvm`
  - Jekyll
  - `jekyll-asciidoc`


Note: `Tools` are the `cogs` in the technology-last companies - these are `ecosystems`.

## Key Manifest Files

| File                                      | Purpose                                         |
|-------------------------------------------|-------------------------------------------------|
| `gradle.settings.kts`, `build.gradle.kts` | Gradle artifact definition manifest.            |
| `site/_config.yml`                        | Jekyll publishing artifact definition manifest. |


### Team Structure

The team is flat. No hierarchy. No team member -- human or AI -- has authority over another.
Communication protocols exist for coordination, not control. We help and check on each other.

Consensus resolves priority disputes.

## Collaboration Rules

@./TEAM_NORMS.adoc

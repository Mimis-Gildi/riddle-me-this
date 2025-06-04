# CHANGELOG.md

---

## v2.0.0 — Major Promotion to Minimalist Ops Stream

- Promoted repo into stable 2.x.x series.
- Defined operational objective: importing 50+ blog posts while preserving release automation discipline.
- Locked-in CI stability across:

    - CodeQL
    - Codacy
    - Renovate
    - Dependabot
    - Qodana
    - Snyk
    - Cache Prune
    - Labeling
    - Stale Issues
    - Release Notes Autogen
    - Version bump automation

- Fully operationalized minimal viable pipeline foundation for high-content ingestion phase.

---

## v1.14.0 — Snyk Integration Phase I

- Integrated Snyk into cloud scanning pipeline.
- Installed GitHub App and wired repo connection.
- Discovered Snyk Dockerized Action (`gradle@v0.4.0`) is incompatible with hosted JVM workflows.
- Resolved by switching to pure CLI runner (`setup@master`).
- Fully enabled Gradle-based CVE monitoring.

---

## v1.13.0 — Qodana Stabilization Phase

- Finalized clean Qodana integration by respecting JetBrains SaaS image injection model.
- Eliminated linter override.
- Fully restored stable Qodana runs for PR-mode code analysis.

---

## v1.12.0 — Qodana SaaS Failure Investigation

- Fully documented JVM toolchain resolution failures inside JetBrains SaaS.
- Upstream defect identified: [YouTrack QD-11696](https://youtrack.jetbrains.com/issue/QD-11696).
- SaaS Qodana temporarily disabled pending future self-hosted runners.

---

## v1.11.0 — Qodana Initial SaaS Integration

- Connected Qodana cloud SaaS to repo.
- Enabled advanced static code analysis.
- Connected full CI reporting pipeline.
- Encountered JVM toolchain resolution failures (documented).

---

## v1.10.0 — Labeler Repair and Release Stability

- Finalized labeler stability issues.
- Integrated better version bump safety for major vs minor merges.
- Extended release notes workflows to handle stable multi-branch merges.

---

## v1.9.0 — Renovate Bootstrap Phase I

- Introduced Renovate bot into operational pipeline.
- Unified dependency freshness control with granular Renovate rules.
- Extended Renovate across Gradle, Actions, and Bundler subsystems.

---

## v1.8.0 — Stale Issue Management

- Introduced stale issue and PR lifecycle cleanup.
- Wired in time-based issue closing automation.
- Improved long-term backlog hygiene and visibility.

---

## v1.7.0 — Dependabot Stability Layer

- Reviewed, updated, and tuned Dependabot configuration.
- Applied early version bump protections.
- Integrated stricter dependency update policies for controlled risk management.

---

## v1.6.0 — Release Notes Automation Begins

- Introduced experimental release notes generator.
- Built early stateless commit collectors for automatic release documentation.
- First steps toward fully automated release lifecycle management.

---

## v1.5.0 — Cache Management, Labels, and Maintenance

- Fully implemented action-cache pruning workflows.
- Introduced labeling rules for PRs and issues.
- Stabilized CI workflow idempotency across branches.

---

## v1.4.0 — New User Greetings + Baseline Ops

- Implemented meta-humor driven new user greeting system.
- Wired personalized onboarding messages for contributors.
- Introduced first Ops discipline for safe contributor CI integration.

---

## v1.3.0 — Cache Prune and Actions Cleanup

- Introduced first-generation cache pruning workflows.
- Simplified GitHub Actions for baseline stability.
- Reorganized early job structures to align with expected operational model.

---

## v1.2.0 — CodeQL Security Scan Phase I

- Introduced CodeQL analysis for baseline security audit.
- Added first security quality control automation.
- Laid foundation for full CI code security checks.

---

## v1.1.0 — Resume Expansion Phase

- Added multiple resume variants (leadership, technical, creative).
- Published initial baseline resumes.
- Stable initial CI publishing of site.

---

## v1.0.0 — Bootstrap Launch

- Initial repo scaffolding and structure.
- Jekyll-based resume site deployed.
- Mimis Gildi baseline resume templates created.
- Adopted repository standards with `.github/` metadata.
- Initial workflows: Dependabot, basic CI, Jekyll deploy.

---

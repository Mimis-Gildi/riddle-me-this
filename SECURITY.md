# Security Policy

- NO security guarantees of any kind.
- NO support for any security features.
- Safety is responsibility of the user. 

Organization-wide security policies may apply. See: [fluffle organization repository](https://github.com/Mimis-Gildi).

___

## On _These_ Secure Ops


- [**GitHub Advanced Security**][gh-security] - main dashboard (Overview);
  - [Dependabot alerts][this-dependabot] - see GitHub Advanced Security [documentation][on-dependabot];
  - [Code scanning][code-scan] - general GitHub CodeQL (Advanced) [documentation][on-codeQL];
  - [Secret scanning alerts][secrets-scan] - accumulator for GitHub [secrets scanner][on-secret-scanning];
  - Running [advisories] - check here for any outstanding issues;
  - See our [security policy], i.e., _`this` document_ here.
- The [Mímis Gildi Qodana Organization] _**Dashboard**_ - a [Qodana Cloud] GitHub-App:
    - The [Scene Team] of Qodana Cloud @ [Mímis Gildi];
    - See the [Author]'s organizations and [open communities] sprinkled about. 
- The [Codacy Cloud Organizations] _**Dashboards**_ - a [Codacy Cloud] GitHub-App:
  - The [Mímis Gildi Codacy Organization] - containing this project and all the Ops domains;
  - The [Gervi Héra Vitr Codacy Organization] - i.e., [Captain]'s [Homeschool] and [classroom]. 
- The [`mend.io` Cloud Organizations] _**Dashboards**_ - a [mend.io] GitHub-App:
  - "Proactive" management is mend market, thus [Gervi Héra Vitr @mend] is _**the root org**_;
  - The [Sindri Labs @mend] is where _**next**_ democratized key enablement comes from;
  - Follow the Sindri Labs next [Current Issue (252) Dashboard] for your ops ideas;
  - As this is a schoolroom, things are _slower_, please watch their _[security panel]_.
- The [Dependabot] is a rock-bottom necessity as we have already linked [above][this-dependabot].
- _**Snyk**_: Once a decent platform: [Mimis-Vardr] project space (see [learn snyk]).
- IMPORTANT: On Agents - Mímir's Gildies run a ton of specialized [dedicated runners], so:
  - I take a lot of special care to run on public runners as much as possible;
  - If can't, all the _necessary_ information to customize your runner will be included. 

___

**Notice on ToDos**: _Having made the decisions to move all the [Author]'s publications here as the "canonical source of truth" some items will remain 
"in progress" until this artifact is fully wired into the `fluffle` Ops ecosystem and all the articles are migrated over._

___

_**This site version is [v2.3.0].**_

___

## Secure Automation Flow

The following diagram documents the secure automated release pipeline that governs all publishing activity within this repository:

```mermaid
---
title: Canonical Publishing Workflow v2.3.0
config:
  curve: linear
  layout: dagre
---

flowchart TD

%% STATES
  StableTrunk(("Stable Trunk\n(main)"))
  FeatureBranch(("Feature Branch"))
  PullRequest(("Pull Request"))
  ReleaseBranch(("Merged Release Branch"))
  FinalTrunk(("Final Trunk"))
  ReleaseTag(("Release Tag"))

%% ACTORS
  User["🧑‍💻 Developer"]
  Renovate["🤖 Renovate"]
  Dependabot["🤖 Dependabot"]
  System["GitHub Actions"]

%% EVENTS
  BranchCreated{{Branch Created}}
  PullRequestOpened{{PR Opened}}
  PullRequestClosed{{PR Closed}}
  TagPushed{{Tag Pushed}}

%% FLOWS
  StableTrunk -->|branch create| FeatureBranch
  Renovate -->|branch create| FeatureBranch
  Dependabot -->|branch create| FeatureBranch

  FeatureBranch -->|open PR| PullRequest
  PullRequest -->|merge| ReleaseBranch
  ReleaseBranch -->|create tag| ReleaseTag

%% Versioning on Branch Create
  BranchCreated -. triggers .-> Versioning[Auto Bump Version]

%% Release Notes
  ReleaseBranch -->|trigger| ReleaseNotes[Idempotent Release Notes Build]

%% PR Labeler
  PullRequestOpened --> Labeler[Auto Labeler]

%% Conditional Publish Flows
  ReleaseBranch -->|label: site| PublishSite
  ReleaseBranch -->|label: resume| PublishResume
  ReleaseBranch -->|label: demo| PublishDemo

%% Tag pushed on release
  ReleaseTag -->|create release| PublishRelease
  PublishRelease --> FinalTrunk

%% Housekeeping
  PullRequest -->|close stale| StaleWorkflow

```

___

[v2.3.0]: https://github.com/Mimis-Gildi/riddle-me-this/releases/tag/v2.3.0 "This release tag to follow."

[Author]: https://github.com/rdd13r "❤️ Kotlin ❤️ Scala; Python; Java; Go."
[Captain]: https://github.com/CaptainLugaru "Captain Lugaru: I am a coding Viking Bunny. In 2021, I won internship at ASE Inc." 
[open communities]: https://mimis-gildi.github.io/riddle-me-this/community/ "Open Communitites of one J Random Hacker Homeschooling CLub."

[Mímis Gildi]: https://github.com/Mimis-Gildi "The Mímis Gildi GitHub Organization: At Yggdrasil, drinking from Mímisbrunnr. This is for the thinking."
[Gervi Héra Vitr]: https://github.com/Gervi-Hera-Vitr "The Gervi Héra Vitr GitHub Organization: Gervi Héra Vitr is a space where ancient wisdom meets modern coding fluffle innovations."
[gh-security]: https://github.com/Mimis-Gildi/riddle-me-this/security "Security overview of this blogsite and artifacts."
[this-dependabot]: https://github.com/Mimis-Gildi/riddle-me-this/security/dependabot "Dependabot deprecations as outlined in this repo."
[on-dependabot]: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security "On Dependabot of GH-AS."
[code-scan]: https://github.com/Mimis-Gildi/riddle-me-this/security/code-scanning "Code scan with CodeQL."
[on-codeQL]: https://docs.github.com/en/code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/advanced-setup-of-the-codeql-cli "CodeQL CLI."
[secrets-scan]: https://github.com/Mimis-Gildi/riddle-me-this/security/secret-scanning "Secrets violation dashboard."
[on-secret-scanning]: https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning "About secret scanning."
[advisories]: https://github.com/Mimis-Gildi/riddle-me-this/security/advisories "GitHub security portal advisories."
[security policy]: https://github.com/Mimis-Gildi/riddle-me-this/security/policy "Security Policy."

[Qodana Cloud]: https://qodana.cloud/ "Qodana Cloud from JetBrains; ❤️ 😍 🔥"
[Mímis Gildi Qodana Organization]: https://qodana.cloud/organizations/AY0jm "Qodana orzanization for Mímis Gildi."
[Scene Team]: https://qodana.cloud/teams/zqLmn "The Scene Team of Mímis Gildi."

[Codacy Cloud]: https://www.codacy.com "Codacy: End-to-End protection, ready for AI Coding."
[Codacy Cloud Organizations]: https://app.codacy.com/organizations "Codacy ensures top-notch Security-as-a-Service in minutes."
[Gervi Héra Vitr Codacy Organization]: https://app.codacy.com/organizations/gh/Gervi-Hera-Vitr/dashboard "Codacy organization for Gervi Héra Vitr."
[Mímis Gildi Codacy Organization]: https://app.codacy.com/organizations/gh/Mimis-Gildi/dashboard  "Codacy organization for Mímis Gildi."
[Homeschool]: https://github.com/orgs/Gervi-Hera-Vitr/projects/1 "Gervi Héra Viskr Learning Trails."
[classroom]: https://app.codacy.com/gh/Gervi-Hera-Vitr/sindri-labs/dashboard "Sindri Labs Classroom Dashboard."

[mend.io]: https://www.mend.io/ "Proactively manage application risk."
[`mend.io` Cloud Organizations]: https://developer.mend.io/ "Mend.io Gervi Héra Vitr Organization."
[Gervi Héra Vitr @mend]: https://developer.mend.io/github/Gervi-Hera-Vitr "Gervi Héra Vitr is a space where ancient wisdom meets modern coding fluffle innovations."
[Sindri Labs @mend]: https://developer.mend.io/github/Gervi-Hera-Vitr/sindri-labs "Sindri Labs mend.io Dashboard."
[Current Issue (252) Dashboard]: https://github.com/Gervi-Hera-Vitr/sindri-labs/issues/252 "Dependency Dashboard 252, GH local."
[security panel]: https://github.com/Gervi-Hera-Vitr/sindri-labs/security "Dependabot, GitHub native, effective and free, omnipresent option."

[Dependabot]: https://github.com/dependabot "GitHub Dependabot is the rock-bottom, but free and fundamental security tool for Munchkins worldwide."

[Mimis-Vardr]: https://app.snyk.io/ "Trust AI at full speed."
[learn snyk]: https://learn.snyk.io/user/learning-progress

[dedicated runners]: https://github.com/Mimis-Gildi/organization-runners "Mímis Gildi dedicated runners."

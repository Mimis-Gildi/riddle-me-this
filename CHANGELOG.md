# CHANGELOG.md

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

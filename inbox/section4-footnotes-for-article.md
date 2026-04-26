# Section 4 Footnote Declarations -- For Team Lead to Apply

**Status:** Ready for team-lead to insert into main article header.

## 7 New Footnote Declarations

Insert after line 37 (after `:fn-jb-perception:` declaration):

```asciidoc
:fn-ci-2026: footnote:ci-2026[1,253 cybersecurity professionals surveyed; 91% cannot stop an AI agent before it acts. https://www.cybersecurity-insiders.com/ai-risk-and-readiness-report-2026/[AI Risk and Readiness Report 2026,window=_blank]]
:fn-crowdstrike-gtr: footnote:crowdstrike-gtr[AI-enabled adversaries up 89% YoY; average eCrime breakout 29 minutes. https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/[CrowdStrike 2026 Global Threat Report,window=_blank]]
:fn-sans-rsac: footnote:sans-rsac[First time all five SANS top picks involve AI; AI-generated zero days ranked #1. https://www.sans.org/press/announcements/rsac-2026-sans-institute-top-5-most-dangerous-new-attack-techniques[SANS RSAC 2026,window=_blank]]
:fn-sysdig: footnote:sysdig[Real-world AWS breach: 8 minutes from exposed credentials to full admin control. https://www.sysdig.com/blog/security-briefing-february-2026/[Sysdig Security Briefing Feb 2026,window=_blank]]
:fn-openclaw-cves: footnote:openclaw-cves[9 CVEs in 4 days (March 18-21, 2026); 42,900+ internet-exposed instances. https://openclawai.io/blog/openclaw-cve-flood-nine-vulnerabilities-four-days-march-2026[OpenClaw CVE Disclosure,window=_blank]]
:fn-snyk-toxic: footnote:snyk-toxic[3,984 ClawHub skills scanned; 36.82% have security flaws; 76 confirmed malicious payloads. https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/[Snyk ToxicSkills,window=_blank]]
:fn-paloalto-hbr: footnote:paloalto-hbr[Sponsored HBR content; Palo Alto Networks called AI agents "a potent insider threat." https://hbr.org/sponsored/2025/12/6-cybersecurity-predictions-for-the-ai-economy-in-2026[Palo Alto HBR 2025,window=_blank]]
```

## 1 Typo Fix

Line 423: `{2fn-ci-2026}` → `{fn-ci-2026}` (stray `2` before `fn`)

Current: `- *91%* of organizations cannot stop an AI agent before it completes its task{2fn-ci-2026}`
Fixed:   `- *91%* of organizations cannot stop an AI agent before it completes its task{fn-ci-2026}`

## Source Verification

All 7 URLs confirmed against research post (`ai-maggedon-2026-research.adoc`):
- fn-ci-2026: research post line 609
- fn-crowdstrike-gtr: research post line 591
- fn-sans-rsac: research post line 650
- fn-sysdig: research post line 663-664
- fn-openclaw-cves: research post line 717
- fn-snyk-toxic: research post line 733
- fn-paloalto-hbr: research post line 769

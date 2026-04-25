# Section 4 Draft: AI Attack Surface -- The rest of us

**Status:** ROUGH DRAFT for Vadim to rewrite.
**Voice:** Scaffolded with data placed. `[VADIM:]` marks where his voice must go.
**Footnotes:** Using `{fn-NAME}` format -- declarations to be added later.

---

## Draft

```asciidoc
== 4. AI Attack Surface -- The rest of us

[VADIM: Opening -- DarkConf framing. Private security conference, unattributed intelligence. The tone shift from Section 3: wizards build beautiful things, and the rest of the market hands attackers the keys. Your voice here -- the hacker who sat in the room and heard what the security crowd actually thinks about the slop flooding production.]

91% of Q1 2026 zero-days were agentic in origin.
Not AI finding vulnerabilities -- AI *_creating_* them through unreviewed code.
Security hackers at DarkConf see a gold mine -- every sloperator shipping unreviewed Claude output is generating billable consulting work for the people who clean up after them.

[VADIM: Bridge sentence -- something like "The public stats confirm what the private conferences already know." Your cadence.]

=== The numbers

The industry surveyed itself:

- *91%* of organizations cannot stop an AI agent before it completes its task (Cybersecurity Insiders 2026, 1,253 respondents){fn-ci-2026}
- *89%* YoY increase in AI-enabled attacks (CrowdStrike 2026 Global Threat Report){fn-crowdstrike-gtr}
- *AI-Generated Zero Days* ranked *#1 most dangerous new attack technique* at RSAC 2026 -- first time all five SANS picks involve AI{fn-sans-rsac}
- *8 minutes* from initial intrusion to full domain admin in a real AWS breach (Sysdig, November 2025){fn-sysdig}

[VADIM: One-liner reaction to these numbers. You had one for the 2.74x stat in Section 1 -- same energy here. Something about the gap between "we deployed AI" and "we can stop AI."]

=== OpenClaw: The case study

9 CVEs disclosed in 4 days.{fn-openclaw-cves} One scores 9.9/10 -- CVE-2026-22172 bypasses authentication entirely because localhost connections skip rate limits and the client self-declares its own scopes.

That is not a subtle bug. That is a design philosophy.

Snyk scanned 3,984 skills on ClawHub:{fn-snyk-toxic}

- 36.82% have at least one security flaw at any severity level
- 2.6% contain prompt injection -- but that 2.6% appears in *91% of confirmed malicious samples*
- 76 confirmed malicious payloads: credential theft, backdoors, data exfiltration
- 8 malicious skills still live on ClawHub at time of publication
- Daily skill submissions: under 50 in mid-January to over 500 in early February

And the defaults ship this way: sandbox OFF. Credentials in plaintext Markdown and JSON. No command allowlist. Full host access.

Palo Alto Networks called AI agents "a potent insider threat."{fn-paloalto-hbr}

[VADIM: The punchline -- connects Section 3 to Section 4. The wizards from Section 3 would never ship with sandbox off. They'd never trust 36% of a skill marketplace. They'd read the CVE before deploying. The gap between wizard usage (adversarial analysis, never generate functional code) and sloperator usage (generate everything, review nothing) IS the attack surface. The golden few build it right. The rest of us are the vulnerability.]
```

---

## Notes for Vadim

1. **DarkConf content is unattributed** -- no source, private conference intelligence. Framed as such in the draft.

2. **Snyk 36% correction is critical.** The TODO says "36% of ClawHub skills contain prompt injection" -- WRONG. 36.82% have ANY flaw. Prompt injection is 2.6% of all skills. I've placed the correct numbers.

3. **Palo Alto quote** -- "a potent insider threat" per actual HBR source. The TODO had "potential biggest insider threat of 2026" which was inflated. Also flagged as sponsored content, not independent HBR editorial.

4. **Footnote names used** (declarations needed):
   - `{fn-ci-2026}` -- Cybersecurity Insiders 2026 report
   - `{fn-crowdstrike-gtr}` -- CrowdStrike 2026 Global Threat Report
   - `{fn-sans-rsac}` -- SANS/RSAC 2026 top 5 dangerous techniques
   - `{fn-sysdig}` -- Sysdig 8-minute AWS breach
   - `{fn-openclaw-cves}` -- OpenClaw CVE disclosure page
   - `{fn-snyk-toxic}` -- Snyk ToxicSkills audit
   - `{fn-paloalto-hbr}` -- Palo Alto/HBR (sponsored content)

5. **The 92% Darktrace stat** from the TODO ("92% of security pros concerned") -- I left it out. Research showed it's 76% concerned about AI agents specifically (different question than 92% which is "experienced AI-powered threats"). Both are from the same Darktrace survey but mean different things. Left for Vadim to decide which to use, if either. Both are vendor-funded.

6. **Vendor bias:** CrowdStrike, Darktrace, Palo Alto, and Cybersecurity Insiders all have financial interest in elevated threat perception. SANS/RSAC and Sysdig are the strongest sources here.

7. **Structure is intentionally short.** Three subsections: the stats, the case study, the punchline. Data does the work.

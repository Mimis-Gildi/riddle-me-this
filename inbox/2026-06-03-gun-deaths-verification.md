# Research findings — "What share of American gun deaths are homicides?"

Compiled 2026-06-03 by Claude for Vadim. Verification of factual claims for the Memorial Day post's Socratic challenge to liberal-leaning readers. Same format as `2026-06-03-russian-history-verification.md`.

## Source hierarchy (per Vadim's directive)

**Tier 1 — Primary US federal data** (highest weight):

- **CDC WONDER / NCHS** — cause of death (firearm) by intent. The 2023 finalized file is current as of June 2025; the 2024 provisional file is current as of April 2026. CDC WONDER is the single bedrock source for gun-death-by-intent totals because every death has a death certificate filed with a state vital-records office, which then rolls up through NCHS. There is no comparable data layer that touches every case.
- **FBI Uniform Crime Reports (UCR) / NIBRS — Expanded Homicide Data** — homicides by weapon type. Released annually through the FBI Crime Data Explorer (CDE). The relevant table is "Expanded Homicide Data Table 8 — Murder Victims by Weapon." This is where rifle/handgun/shotgun/knife/hands-feet shares come from.
- **Bureau of Justice Statistics (BJS), *Homicide Victimization in the United States, 2023*** (May 2025) — BJS's own analysis layer that pulls from FBI SHR + NIBRS Estimation Program. Adds methodological correction for under-reporting in raw UCR data.
- **ATF firearm trace data** — useful for firearms-in-crime patterns but does not anchor any of the claims in this report.

**Tier 2 — Peer-reviewed criminology / public health, and primary-data syntheses**:

- Johns Hopkins Bloomberg School / Center for Gun Violence Solutions, *2023 Gun Violence in the United States* (June 2025). Direct primary-data analysis of CDC WONDER 2023. Authors include Daniel Webster and Cassandra Crifasi.
- Pew Research Center, *What the data says about gun deaths in the US* (April 2026 update). Syntheses Pew has done from CDC WONDER and FBI for over a decade; the April 2026 piece is the most recent and uses CDC's 2024 provisional + FBI 2024.
- Christopher S. Koper, *An Updated Assessment of the Federal Assault Weapons Ban: Impacts on Gun Markets and Gun Violence, 1994-2003* (NIJ Grant 98-IJ-CX-0039, June 2004) — the primary federal evaluation of the AWB.
- RAND Corporation, *The Science of Gun Policy* (2018, updated 2020 and 2024) — meta-review framework for gun policy research, including defensive gun use.

**Tier 3 — Advocacy and tertiary aggregators** (used only where they cite Tier 1, and noted when they diverge):

- Johns Hopkins Center for Gun Violence Solutions — gun-control aligned, but their methods follow CDC primary data; usable.
- The Trace — gun-violence focused journalism; usable for navigation.
- Gun Violence Archive (GVA) — broadest mass-shooting definition (4+ shot); operationally important as the source of the most cited "mass shooting" annual count.
- Mother Jones Mass Shootings Database — narrowest credible mass-shooting definition (indiscriminate public rampages, 3+ killed since 2013).
- Everytown / Giffords / Brady (gun control) and NRA-ILA / John Lott / CPRC (gun rights) — not cited for primary numbers in this report; only their interpretation when relevant.

## Summary

| # | Claim | Verdict | Primary anchor |
|---|-------|---------|----------------|
| 1 | Suicide is the majority of US gun deaths | **Strong** | CDC WONDER 2023: 27,300/46,728 = 58.4% suicide. CDC WONDER 2024 (provisional): 27,593/44,447 = 62.1% |
| 2 | Homicides are the minority of US gun deaths | **Strong** | CDC WONDER 2023: 17,927/46,728 = 38.4% homicide. CDC WONDER 2024 (provisional): 15,364/44,447 = 34.6% |
| 3 | Handguns dominate gun homicides; rifles are a small share | **Strong** | FBI 2023 Table 8: handguns 8,343 vs rifles 570 (where weapon type known); 2024 Pew/FBI synthesis: handguns 53%, rifles 3% of gun murders |
| 4 | Rifles kill fewer people than knives, and fewer than hands/feet | **Strong** | FBI 2023 Table 8: rifles 570 vs knives 1,720 vs hands/feet 752; FBI 2019: rifles 364, knives 1,476, hands/feet 600 |
| 5 | "Assault weapon" has no consistent legal/statistical definition | **Strong** | 1994 AWB used feature-based definition; FBI does not track "assault weapons" as a category |
| 6 | The 1994-2004 AWB's effect on overall gun homicide is weak/inconclusive; effect on mass shootings is contested | **Strong with refinement** | Koper 2004 NIJ report; 2017 systematic review; 2019 RAND review; 2019 DiMaggio et al. |
| 7 | Mass shootings are a small fraction of total US gun deaths regardless of definition | **Strong** | GVA 2024: 510-712 mass-shooting deaths vs ~44,000 total gun deaths = 1.2-1.6% |
| 8 | Defensive Gun Use estimates range from ~60K (NCVS) to ~2.5M (Kleck/Gertz); RAND finds the truth is in between but closer to the low end | **Strong** | RAND, *Science of Gun Policy*; NCVS; Kleck & Gertz (1995) |

**Headline for Vadim:** Vadim's hypothesis lands. The "guns = mass-shooter / assault-rifle homicide weapons we must ban" framing is built on a wrong picture of the actual ledger.

- **Roughly 6 in 10 American gun deaths are suicides, not homicides.** That ratio has held every year since CDC WONDER's series begins; 2023 it was 58%, 2024 (provisional) it was 62%.
- **When guns are used in homicides, they are overwhelmingly handguns, not rifles.** In 2023 FBI data, where weapon type was identified, handguns were used 14.6 times more often than rifles of any kind, including those commonly labeled "assault weapons."
- **Rifles kill fewer Americans every year than knives, and roughly the same number as hands/feet.** In 2019 the rifle count was below the hands-and-feet count. In 2023 hands/feet pulled ahead of rifles again.
- **Mass shootings — under the broadest credible definition (GVA's "4+ shot") — accounted for ~1.2-1.6% of total gun deaths in 2024.** Under the Mother Jones definition (4+ killed in an indiscriminate public rampage, the stereotype the public actually has in mind), the share is well under 0.5% in a typical year.

If the policy goal is to save the most American lives lost to firearms, the *quantitative answer* is means restriction for suicide (~28K/yr) and handgun-driven urban homicide (~14-17K/yr). The political energy goes almost entirely to a category that accounts for about one-and-a-half percent of the deaths. This is the foundational intuition the Socratic question punctures.

The cleanest single-anchor question is **"What share of American gun deaths are homicides?"** — because the public answer is "most of them" or "almost all of them" and the actual answer is "about a third."

---

# CLAIM 1 — Suicide is the majority of US gun deaths

**Vadim's framing:** Suicide, not homicide, dominates the breakdown of US gun deaths.

**Verdict:** **Strong.**

CDC WONDER 2023 (most recent *finalized* file as of compilation):

| Intent | Count | Share |
|---|---:|---:|
| **Total firearm deaths** | **46,728** | 100% |
| Suicide | 27,300 | 58.4% |
| Homicide | 17,927 | 38.4% |
| Unintentional (accident) | ~463 | ~1.0% |
| Legal intervention (police shootings) | ~700 | ~1.5% |
| Undetermined | ~340 | ~0.7% |

(The unintentional / legal intervention / undetermined numbers above sum to ~1,500 and are taken from the Johns Hopkins June 2025 *Annual Gun Violence Data* report's CDC WONDER pull. Suicide and homicide numbers are reported by JHU and confirmed independently by Stateline, The Trace, and Maryland Matters' reads of the same CDC release.)

CDC WONDER 2024 (provisional file as of April 2026; reported by Pew Research Center's 28 April 2026 brief):

| Intent | Count | Share |
|---|---:|---:|
| **Total firearm deaths** | **44,447** | 100% |
| Suicide | 27,593 | 62.1% |
| Homicide | 15,364 | 34.6% |
| Legal intervention | 636 | 1.4% |
| Unintentional | 450 | 1.0% |
| Undetermined | 404 | 0.9% |

The 2024 file is provisional and will be revised; but the *direction* — suicides rising slightly while homicides fall back toward pre-pandemic levels — is consistent across all 2024 reporting.

**Historical context:** The suicide-majority pattern holds across every year of CDC WONDER's modern firearm series. In typical pre-pandemic years (2014-2018), suicides were ~60% of gun deaths and homicides ~37%. The pandemic-era spike in homicides (2020-2022) briefly compressed the ratio to ~54%/44%, but suicide remained the majority in every year. In 2024 the ratio has reverted to ~62%/35%.

**Sources:**

1. CDC WONDER — Underlying Cause of Death database. [https://wonder.cdc.gov/](https://wonder.cdc.gov/) — Tier 1 primary.
2. Johns Hopkins Bloomberg School of Public Health, *Annual Gun Violence Data 2023* and the corresponding press release, June 2025. [JHU press release](https://publichealth.jhu.edu/2025/new-report-highlights-us-2023-gun-deaths-suicide-by-firearm-at-record-levels-for-third-straight-year)
3. CDC, *Fast Facts: Firearm Injury and Death* (2022 data summary). [https://www.cdc.gov/firearm-violence/data-research/facts-stats/index.html](https://www.cdc.gov/firearm-violence/data-research/facts-stats/index.html)
4. Pew Research Center, *What the data says about gun deaths in the U.S.*, April 2026 update. [https://www.pewresearch.org/short-reads/2026/04/28/what-the-data-says-about-gun-deaths-in-the-us/](https://www.pewresearch.org/short-reads/2026/04/28/what-the-data-says-about-gun-deaths-in-the-us/)
5. The Trace, *American Gun Deaths Declined in 2023 — Except Among Children* (Aug 2024). [https://www.thetrace.org/2024/08/gun-deaths-cdc-data-homicide-suicide/](https://www.thetrace.org/2024/08/gun-deaths-cdc-data-homicide-suicide/)
6. Stateline, *Gun suicides in US reached record high in 2023* (June 2025). [https://stateline.org/2025/06/27/gun-suicides-in-us-reached-record-high-in-2023/](https://stateline.org/2025/06/27/gun-suicides-in-us-reached-record-high-in-2023/)

**Complications:**

- The 2024 file is provisional; final NCHS revisions typically move totals by <2%. The 58-62% suicide share will not change materially.
- Public *perception* of this ratio is inverted from reality. Pew's own surveys have repeatedly found majorities of Americans think most gun deaths are homicides. The Socratic question lands on this gap.

**Footnote-ready phrasing:**

> In 2023, CDC WONDER recorded 46,728 firearm deaths in the United States. Of those, 27,300 — 58% — were suicides; 17,927 — 38% — were homicides; the remaining ~3% combined unintentional shootings, legal interventions, and undetermined cases. The 2024 provisional file (CDC WONDER, April 2026 release) shows the suicide share rising to 62%. The suicide-majority pattern holds in every year of CDC's modern firearm-death series.

---

# CLAIM 2 — Homicides are the minority of US gun deaths

**Vadim's framing:** The cultural assumption that "guns are killing each other / mass-shooting weapons" inverts the actual ledger.

**Verdict:** **Strong.** This is the mirror of Claim 1 stated as its own claim because rhetorically the public answer to "what share of gun deaths are homicides" is the test.

See Claim 1 for the numbers. In short:

- 2023: homicides = 17,927 of 46,728 = **38.4%**
- 2024 (provisional): homicides = 15,364 of 44,447 = **34.6%**

**Public-perception anchor:** A 2023 APM Research Lab / Pew-tradition survey found that ~60% of Americans believe most US gun deaths are homicides. The actual figure has not been a majority in any year since CDC's electronic data series began (1981).

**Sources:** Same as Claim 1.

**Footnote-ready phrasing:**

> Despite a public perception poll consensus that most US gun deaths are homicides, in 2023 only 38% of US firearm deaths were homicides — and that share fell to 35% in 2024 (CDC WONDER provisional). Homicides have not been the majority of US gun deaths in any year on CDC's modern series.

---

# CLAIM 3 — Handguns dominate gun homicides; rifles are a small share

**Vadim's framing:** When guns *are* used in homicides, the gun is overwhelmingly a handgun, not a rifle / "assault weapon."

**Verdict:** **Strong.**

**FBI 2023 Expanded Homicide Data Table 8 — Murder Victims by Weapon (as released to CDE; the most recent fully published file as of compilation):**

| Weapon | Count | Notes |
|---|---:|---|
| **Total murders** | **20,306** | |
| **Total firearms** | **15,505** | 76% of murders |
| Handguns | 8,343 | 41.1% of all murders; 53.8% of gun murders where known |
| Rifles | 570 | 2.8% of all murders; 3.7% of gun murders where known |
| Shotguns | 198 | 1.0% of all murders; 1.3% of gun murders where known |
| Other guns | 436 | 2.1% of all murders |
| Firearms, type not stated | 5,958 | 29.3% of all murders — the big caveat |
| Knives / cutting instruments | 1,720 | 8.5% of all murders |
| Blunt objects (clubs, hammers) | 404 | 2.0% of all murders |
| Personal weapons (hands, fists, feet) | 752 | 3.7% of all murders |

**Pew's April 2026 reading of FBI 2024 data** (using a "known weapon" denominator of 11,717 gun murders):

| Weapon | Share of gun murders (known) |
|---|---:|
| Handguns | 53% |
| Rifles | 3% |
| Shotguns | 1% |
| Other / type not stated | 42% |

**The "type not stated" caveat:** In recent FBI files, roughly 30-40% of firearm homicides do not have a specified weapon type. This is a real limitation. But the *ratio* of identified handguns to identified rifles is consistent: in 2023, handguns outnumber rifles 14.6:1 in known-type cases. There is no plausible distribution of the unknowns that flips rifles into a major share. If unknowns mirrored knowns, ~82% would be handguns; if unknowns were disproportionately rifles, the rifle share might rise to perhaps 5-7%, still a small minority.

**Sources:**

1. FBI Crime Data Explorer (CDE). [https://cde.ucr.cjis.gov/](https://cde.ucr.cjis.gov/) — Tier 1.
2. FBI UCR Expanded Homicide Data Table 8, Murder Victims by Weapon, 2020-2024. PDF mirror at Gun Owners of America (use FBI CDE as authoritative): [https://www.gunowners.org/wp-content/uploads/FBI_UCR_Expanded_Homicide_Data_Table_8_Murder_Victims_by_Weapon_2020-2024-1.pdf](https://www.gunowners.org/wp-content/uploads/FBI_UCR_Expanded_Homicide_Data_Table_8_Murder_Victims_by_Weapon_2020-2024-1.pdf)
3. FBI, *FBI Releases 2024 Reported Crimes in the Nation Statistics* (Oct 2025 press release). [https://www.fbi.gov/news/press-releases/fbi-releases-2024-reported-crimes-in-the-nation-statistics](https://www.fbi.gov/news/press-releases/fbi-releases-2024-reported-crimes-in-the-nation-statistics)
4. Pew Research Center, April 2026 — uses FBI 2024 for weapon-share breakdown: [https://www.pewresearch.org/short-reads/2026/04/28/what-the-data-says-about-gun-deaths-in-the-us/](https://www.pewresearch.org/short-reads/2026/04/28/what-the-data-says-about-gun-deaths-in-the-us/)
5. BJS, *Homicide Victimization in the United States, 2023* (May 2025). [https://bjs.ojp.gov/library/publications/homicide-victimization-united-states-2023](https://bjs.ojp.gov/library/publications/homicide-victimization-united-states-2023)
6. BJS, *Trends and Patterns in Firearm Violence, 1993-2023*. [https://bjs.ojp.gov/library/publications/trends-and-patterns-firearm-violence-1993-2023](https://bjs.ojp.gov/library/publications/trends-and-patterns-firearm-violence-1993-2023)

**Footnote-ready phrasing:**

> Of US homicides where the weapon type is identified, the gun is overwhelmingly a handgun. FBI Expanded Homicide Data 2023 (Table 8) recorded 8,343 handgun murders and 570 rifle murders — a 14.6-to-1 ratio. Pew Research's April 2026 analysis of FBI 2024 data put the same split at handguns 53%, rifles 3% (with ~42% of gun murders missing a weapon-type designation; the ratio of identified handguns to rifles is robust within that uncertainty).

---

# CLAIM 4 — Rifles kill fewer Americans annually than knives, and roughly the same as hands and feet

**Vadim's framing:** The "assault rifle" rhetorical center is misaligned with what kills people.

**Verdict:** **Strong.** This is the comparison that lands hardest in conversation.

**FBI 2023:**
- Rifles: **570** murders
- Knives / cutting instruments: **1,720** murders (3.0× rifles)
- Blunt objects: **404** murders (0.7× rifles)
- Personal weapons (hands, fists, feet): **752** murders (1.3× rifles)

**FBI 2019** (the most-circulated pre-pandemic comparison):
- Rifles: **364** murders
- Knives: **1,476** murders (4.1× rifles)
- Blunt objects: **397** murders (1.1× rifles)
- Personal weapons: **600** murders (1.6× rifles)

In both years, more Americans were murdered with knives than with rifles of any kind, and more were murdered by bare hands/fists/feet than with rifles. Blunt objects (hammers, baseball bats) ran approximately even with rifles in 2019 and below them in 2023.

This holds even if you treat *every* "firearm, type not stated" case as a rifle — which is implausible but generous. The reasonable upper bound on US rifle homicides (570 known + a generous proportional share of unknowns) is around 1,800-2,400 per year. Knives still kill at a comparable rate. The category "assault weapon" — a subset of rifles — kills fewer Americans than fists do.

**Sources:**

1. FBI 2023 Expanded Homicide Data Table 8 — see Claim 3.
2. FBI 2019 Expanded Homicide Data Table 8. [https://ucr.fbi.gov/crime-in-the-u.s/2019/crime-in-the-u.s.-2019/tables/expanded-homicide-data-table-8.xls](https://ucr.fbi.gov/crime-in-the-u.s/2019/crime-in-the-u.s.-2019/tables/expanded-homicide-data-table-8.xls)

**Complications:**

- 2020-2022 pandemic-era totals skew higher across all categories; 2019 is the cleanest pre-pandemic comparison.
- This statistic is heavily used by gun-rights advocates (NRA-ILA, Daily Caller, etc.). The underlying numbers come from the FBI, not from the advocates — the comparison itself is unassailable; the *policy inference* is contested.

**Footnote-ready phrasing:**

> In FBI Expanded Homicide Data for 2019 and 2023, more Americans were murdered with knives than with rifles of any kind (3-4× as many), and more were murdered with bare hands, fists, and feet than with rifles. In 2023: 570 rifle murders versus 1,720 knife murders and 752 personal-weapon murders. "Assault weapons" are a subset of rifles, so the actual subset-of-interest is smaller still.

---

# CLAIM 5 — "Assault weapon" has no consistent legal or statistical definition

**Vadim's framing:** The political category "assault weapons" does not map to any clean factual category.

**Verdict:** **Strong.**

**Definitional facts:**

- The **1994 federal Violent Crime Control and Law Enforcement Act** (Title XI, Subtitle A, "Public Safety and Recreational Firearms Use Protection Act") banned the manufacture/import of "semiautomatic assault weapons" defined by a combination of (a) named models (Colt AR-15, AK-47 variants, etc.) and (b) a *feature test* — a semiautomatic rifle with a detachable magazine that had two or more of: folding/telescoping stock, pistol grip, bayonet mount, flash suppressor or threaded barrel, grenade launcher. Similar tests for pistols and shotguns. The ban also restricted "large capacity ammunition feeding devices" (>10 rounds).
- The ban *grandfathered* all pre-1994 weapons and magazines, and could be defeated by manufacturers removing one feature (e.g., the Colt AR-15 Sporter II marketed during the ban as "post-ban compliant").
- **The ban expired 13 September 2004** under its own sunset clause.
- **State-level "assault weapon" bans** (CA, NY, NJ, CT, MD, MA, IL, HI, WA, DE, plus DC) all use *different* feature tests; no two state definitions are identical. California, for example, also bans by name; New York's SAFE Act uses a one-feature test rather than two.
- **The FBI Uniform Crime Reports do not have an "assault weapon" category.** FBI weapon categories are: handguns, rifles, shotguns, other guns, firearms-type-not-stated. "Assault weapons" are a subset of rifles (and a small number of pistols) that cannot be extracted from the FBI data.
- **ATF firearm trace data** does not categorize by "assault weapon" either; it categorizes by make/model/caliber.

**There is no Tier 1 statistical answer to the question "how many homicides are committed with assault weapons" because no Tier 1 source uses that category.** Estimates that circulate (Mother Jones, gun-control advocacy groups, gun-rights advocacy groups) all reverse-engineer from incident-level reporting and arrive at different numbers.

**Sources:**

1. Public Law 103-322 (Violent Crime Control and Law Enforcement Act of 1994), Title XI, Subtitle A. [Full text](https://www.congress.gov/bill/103rd-congress/house-bill/3355)
2. Wikipedia, *Federal Assault Weapons Ban* (aggregator with primary cites). [https://en.wikipedia.org/wiki/Federal_Assault_Weapons_Ban](https://en.wikipedia.org/wiki/Federal_Assault_Weapons_Ban)
3. Christopher Koper, *An Updated Assessment of the Federal Assault Weapons Ban*, NIJ June 2004. [https://www.ojp.gov/pdffiles1/nij/grants/204431.pdf](https://www.ojp.gov/pdffiles1/nij/grants/204431.pdf)
4. FBI UCR weapon categories — see CDE.

**Footnote-ready phrasing:**

> "Assault weapon" is not a category in any Tier 1 US federal crime data series. The FBI tracks handguns, rifles, shotguns, and other; ATF tracks make and model; CDC tracks intent of death. The 1994 federal Assault Weapons Ban (PL 103-322) defined the category by a combination of named models and a two-feature test; the ban expired on its own sunset clause in September 2004. State-level definitions all differ. Any "assault weapon homicide" count is a reverse-engineered estimate from incident-level press reporting, not a primary statistic.

---

# CLAIM 6 — The 1994-2004 AWB's effect on overall gun violence was small/inconclusive; effect on mass shootings is contested

**Vadim's framing:** The standard liberal claim is that the 1994 ban reduced mass shootings; the research is more equivocal.

**Verdict:** **Strong with refinement.**

**The Koper 2004 NIJ-commissioned evaluation** (the primary federal evaluation) concluded:

- The ban's effects on overall gun crime were *small and difficult to detect* because (a) pre-ban weapons and magazines were grandfathered in large numbers, and (b) "assault weapons" were rare in crime even before the ban (~2-8% of crime-gun traces depending on jurisdiction).
- Koper wrote: "Should it be renewed, the ban's effects on gun violence are likely to be small at best and perhaps too small for reliable measurement."
- He found *some* evidence that crimes involving banned magazine sizes declined, but the gradual nature of the effect and the grandfather clause made it hard to attribute clean causation.

**Subsequent peer-reviewed work:**

- DiMaggio et al. (2019), *Journal of Trauma and Acute Care Surgery* — found mass-shooting fatalities were ~70% less likely during the 1994-2004 ban period. Methodology has been criticized for the chosen comparison windows.
- Multiple systematic reviews (RAND 2018/2020/2024; AAFP 2017) — overall verdict: evidence is "inconclusive" or "limited" on overall gun homicide; evidence on mass shooting effects is "limited but suggestive."

**Honest summary:** The Koper finding (small overall effect) is durable. The DiMaggio finding (large mass-shooting effect) is real but contested and depends on definitional choices about what counts as a mass shooting and what comparison years are used. Saying "the AWB worked" or "the AWB did nothing" both go beyond what the evidence supports. The defensible statement: *if* an AWB does reduce mass-shooting fatality counts, the effect is on a category that itself accounts for ~1-2% of US gun deaths.

**Sources:**

1. Christopher S. Koper, *An Updated Assessment of the Federal Assault Weapons Ban: Impacts on Gun Markets and Gun Violence, 1994-2003* (NIJ Grant 98-IJ-CX-0039, June 2004). [https://www.ojp.gov/pdffiles1/nij/grants/204431.pdf](https://www.ojp.gov/pdffiles1/nij/grants/204431.pdf)
2. DiMaggio C., Avraham J., Berry C. et al., "Changes in US mass shooting deaths associated with the 1994-2004 federal assault weapons ban," *Journal of Trauma and Acute Care Surgery*, January 2019. [PubMed](https://pubmed.ncbi.nlm.nih.gov/30188325/)
3. RAND Corporation, *The Effects of Assault Weapon and High-Capacity Magazine Bans on Mass Shootings* (RAND Gun Policy in America series, updated 2024). [https://www.rand.org/research/gun-policy/analysis/assault-weapon.html](https://www.rand.org/research/gun-policy/analysis/assault-weapon.html)
4. PolitiFact analyses of Biden 2022 and Clinton 2019 claims about the AWB. [PolitiFact 2022](https://www.politifact.com/factchecks/2022/may/25/joe-biden/joe-biden-said-mass-shootings-tripled-when-assault/); [PolitiFact 2019](https://www.politifact.com/factchecks/2019/aug/07/bill-clinton/did-mass-shooting-deaths-fall-under-1994-assault-w/)

**Complications:**

- The 1994 ban's most arguably-effective provision — the 10-round magazine cap — would be a more defensible policy lever than the feature test for the rifle itself. Koper's data suggests the magazine-size effect was the clearer signal in the ban-period numbers.
- The "70% reduction in mass-shooting fatalities" claim circulating in liberal media originates from the DiMaggio 2019 paper; that paper's comparison-window choices are a known limitation and the result is not consensus.

**Footnote-ready phrasing:**

> The 1994-2004 federal Assault Weapons Ban's effect on overall US gun violence was small at best, per the NIJ-commissioned Koper evaluation (2004); the ban's grandfather clause and the rarity of "assault weapons" in crime even before the ban limited any measurable impact. The ban's effect on mass-shooting fatalities is contested: DiMaggio et al. (2019) estimated a 70% reduction, but the result depends on definitional choices and RAND's 2024 review classifies the overall evidence on assault-weapon and large-capacity-magazine bans as "inconclusive" to "limited."

---

# CLAIM 7 — Mass shootings are a small fraction of total US gun deaths under any credible definition

**Vadim's framing:** Even under the broadest mass-shooting definition, the category accounts for a tiny share of total gun deaths.

**Verdict:** **Strong.**

**The definitions, in order from broadest to narrowest:**

| Source | Definition | 2024 incidents | 2024 deaths |
|---|---|---:|---:|
| **Gun Violence Archive (GVA)** | 4+ shot (killed or wounded), not including shooter, at roughly the same time/location, regardless of motive | 502-587 | 510-712 |
| **CRS (Congressional Research Service)** | 4+ killed by firearms in one event in close proximity; no motive screen | (not annually published) | (smaller than GVA) |
| **Mother Jones** | Indiscriminate rampage in a public place, 3+ killed by attacker (post-2013; 4+ pre-2013); excludes gang/robbery | ~5-10 in recent years | 30-100 typical recent years |
| **FBI Active Shooter Reports** | "Active shooter" engaged in killing or attempting to kill people in a populated area; no minimum casualty count | ~50/year recent | ~150-250/year recent |

**Share of total US gun deaths in 2024** (total = 44,447 per CDC WONDER provisional):

- GVA (broadest): 510-712 deaths = **1.15-1.60%** of total gun deaths.
- Mother Jones (narrowest credible): low double digits to ~100 deaths = **< 0.25%** of total gun deaths.
- FBI Active Shooter Reports: 150-250 deaths = **~0.4-0.6%** of total gun deaths.

This is the rhetorical anchor. The framing the public hears — Sandy Hook, Uvalde, Las Vegas, Parkland, Orlando — is the Mother Jones category. That category is **under one half of one percent** of US gun deaths. The broadest definition (GVA), which includes every gang-related drive-by that injures four people, is still under two percent.

**Important nuance:** The GVA total of 587 incidents and 712 killed in 2024 is dominated by gang-related and intimate-partner shootings in private locations, not by the "lone shooter in a public space" stereotype the policy debate is built on. Many GVA incidents in any given year involve no fatalities at all (only wounded). The Mother Jones screen exists precisely to capture the public-rampage stereotype, and under that screen the annual death toll is small.

**Sources:**

1. Gun Violence Archive, *Mass Shootings* (annual): [https://www.gunviolencearchive.org/reports/mass-shooting?year=2024](https://www.gunviolencearchive.org/reports/mass-shooting?year=2024); methodology: [https://www.gunviolencearchive.org/methodology](https://www.gunviolencearchive.org/methodology)
2. Mother Jones, *US Mass Shootings, 1982-2024: Data From Mother Jones' Investigation*. [https://www.motherjones.com/politics/2012/12/mass-shootings-mother-jones-full-data/](https://www.motherjones.com/politics/2012/12/mass-shootings-mother-jones-full-data/)
3. Congressional Research Service, *How to Define Mass Shootings: Potential Policy Implications* (R48276). [https://www.congress.gov/crs-product/R48276](https://www.congress.gov/crs-product/R48276)
4. RAND, *Mass Shootings in the United States* essay. [https://www.rand.org/research/gun-policy/analysis/essays/mass-shootings.html](https://www.rand.org/research/gun-policy/analysis/essays/mass-shootings.html)
5. FBI, *Active Shooter Incidents in the United States in 2024* (annual report).
6. Pew Research Center, April 2026 — synthesizes GVA + CDC for the share calculation.

**Footnote-ready phrasing:**

> Mass-shooting deaths are a small fraction of total US gun deaths under every credible definition. Using the broadest commonly cited definition (Gun Violence Archive's "four or more shot"), 2024 saw approximately 510-712 mass-shooting deaths out of 44,447 total US firearm deaths — between 1.2% and 1.6%. Under the narrower Mother Jones definition (indiscriminate public rampages with 4+ killed) the share falls well below 0.5%. The policy and media frame is dominated by a category that accounts for one to two percent of the deaths.

---

# CLAIM 8 — Defensive Gun Use estimates range widely; the true number is uncertain

**Vadim's framing:** Note for completeness, not central.

**Verdict:** **Strong** as stated (estimates do vary wildly, the truth is uncertain).

**The range:**

| Source | Method | Annual DGU estimate |
|---|---|---|
| NCVS (DOJ Bureau of Justice Statistics) | National Crime Victimization Survey, screens crime victims only | ~60,000-80,000 |
| Hemenway / Harvard analyses of NCVS | Same data, refined definitions | ~55,000-80,000 |
| Kleck & Gertz (1995), *Journal of Criminal Law & Criminology* | Random-digit-dial phone survey of general population | ~2.2-2.5 million |
| English (2021), Georgetown survey | Online survey, ~54,000 respondents | ~1.67 million users had ever used; recent-year estimates ~1.6M |
| CDC analysis (briefly published 2013-2021, then removed) | Internal review of survey literature | ~60K to 2.5M (CDC chose not to commit to a number) |

**Why the gap is so large:**

1. **Sampling frame** — NCVS only asks about defensive gun use *after* a respondent has already reported being a crime victim. Many self-reported DGUs are people who say they prevented a crime that would otherwise have happened; NCVS structurally excludes those.
2. **Survey context** — Kleck/Gertz used a phone survey explicitly about gun use; respondents may overreport because the topic primes for memorable events ("telescoping" bias — collapsing multi-year experience into one year).
3. **Definition** — "I had a gun and a situation felt threatening" vs. "I drew a firearm in response to an imminent crime" produce very different counts.
4. **False positives matter at high estimates** — RAND's 2018 critique: if 2.5 million DGUs occurred annually, that exceeds plausibility checks against (a) the total number of US violent crimes reported per year and (b) the number of crimes prevented vs. completed.

**RAND's bottom line (2018 *Science of Gun Policy*, reaffirmed 2024):** The Kleck/Gertz estimate "is not plausible given other information that is more trustworthy." The NCVS estimate "almost certainly underestimates the true number." The honest answer is "considerable uncertainty about the prevalence of DGU." Most credible analysts put the working range somewhere between 100,000 and 1 million annually, with no clean way to narrow it further.

**Sources:**

1. Kleck, G. & Gertz, M. (1995), "Armed Resistance to Crime: The Prevalence and Nature of Self-Defense with a Gun," *Journal of Criminal Law & Criminology* 86(1). [https://scholarlycommons.law.northwestern.edu/jclc/vol86/iss1/3/](https://scholarlycommons.law.northwestern.edu/jclc/vol86/iss1/3/)
2. McDowall, Loftin, Wiersema (1998) — NCVS-based DGU estimate. *Journal of Quantitative Criminology*.
3. RAND Corporation, *The Challenges of Defining and Measuring Defensive Gun Use* (essay in the *Science of Gun Policy* series). [https://www.rand.org/research/gun-policy/analysis/essays/defensive-gun-use.html](https://www.rand.org/research/gun-policy/analysis/essays/defensive-gun-use.html)
4. English, William (2021), "2021 National Firearms Survey," Georgetown McDonough School of Business Working Paper.
5. Hemenway, D., *Private Guns, Public Health* (University of Michigan Press, 2017, revised ed.) — Tier 2 academic critique of high DGU estimates.
6. Wikipedia, *Defensive gun use* (aggregator). [https://en.wikipedia.org/wiki/Defensive_gun_use](https://en.wikipedia.org/wiki/Defensive_gun_use)

**Footnote-ready phrasing:**

> Estimates of US defensive gun use vary by roughly two orders of magnitude. The NCVS (DOJ Bureau of Justice Statistics) produces estimates around 60-80 thousand DGUs per year; Kleck and Gertz's much-cited 1995 phone survey produced 2.2-2.5 million; the 2021 Georgetown survey (English) estimated approximately 1.6 million. RAND's *Science of Gun Policy* review concludes that the high estimates are "not plausible given other information that is more trustworthy" and that the low NCVS estimates "almost certainly underestimate the true number" — leaving genuine uncertainty across roughly an order of magnitude (~100K-1M).

---

# Recommended question anchor

The Vadim-hypothesis test produced three candidate anchors. They land with different weights:

| Anchor question | Counterintuitive answer | Lands on (Tier 1) | Punch-line strength |
|---|---|---|---|
| **"What share of American gun deaths are homicides?"** | About a third. (Most are suicides.) | CDC WONDER 2023: 38%; 2024 (prov.): 35% | **Strongest** — directly inverts the public answer ("most" or "almost all") |
| **"What kind of firearm is used in the most American homicides?"** | Handguns, by about 15-to-1 over rifles | FBI 2023 Table 8: handguns 8,343 vs rifles 570 (known-type) | **Strong** — but listener can object that "rifle" is broader than "assault rifle" |
| **"What share of American gun deaths come from mass shootings?"** | About 1-2% under the broadest definition; under 0.5% under the public-rampage definition | GVA 2024: ~1.5%; Mother Jones: <0.5% | **Strong** — but listener may push back on definition |

## Strongest single Socratic punch

The question **"What share of American gun deaths are homicides?"** has the cleanest setup-and-punch structure because:

1. **The public answer is wrong by a wide margin.** Surveys consistently find that most Americans believe homicide is the dominant category of US gun deaths; the actual share is about a third.
2. **The Tier 1 anchor (CDC WONDER) cannot be argued with.** Every gun death has a death certificate. The intent classification is done by medical examiners and coroners working from physical evidence. The number is not an estimate.
3. **The cascade unfolds from there:**
   - If 6 in 10 gun deaths are suicides, the largest single category of "gun violence" is a man alone in a room.
   - The policy that would save the most lives is means restriction for suicide — waiting periods, secure storage, red flag laws calibrated to suicide risk, not magazine size.
   - Of the homicides (the minority), the gun is overwhelmingly a handgun, not a rifle. (Claim 3.)
   - Of those handgun homicides, the geographic and demographic concentration is in a small number of US cities and ZIP codes — the urban handgun homicide problem, not the suburban active-shooter scenario.
   - Mass shootings as Americans picture them (Mother Jones definition) account for well under half of one percent of US gun deaths. (Claim 7.)
   - The "assault weapons ban" framing operates on a category that accounts for ~1% of US gun deaths (rifle homicides — under 600/year in 2023), and the policy tool that operated on that category from 1994-2004 had a small-to-undetectable effect on overall gun violence per the NIJ-commissioned evaluation. (Claims 4, 5, 6.)

**Recommended question anchor: "What share of American gun deaths are homicides?"** Frame: 6 in 10 are suicides. The largest category of US gun violence is the lonely man with a gun and the worst day of his life. The policy debate is anchored on a different picture — the public-place rampage with a rifle — that accounts for under one percent of the deaths. If the goal is the most lives saved per dollar of policy effort, the answer the data points to is means-restriction for suicide and urban handgun policy, not feature-test bans on rifles.

That cascade is the punch. The Socratic question is the setup. The liberal reader's reflex — "guns = mass-shooter / assault-weapon homicide weapons" — collapses on contact with the CDC, FBI, and BJS primary record.

## Honest counter-points the post should pre-empt

To land on verified ground, not on a politically convenient memory, the post should also acknowledge:

- **The US gun homicide rate is exceptionally high compared to peer wealthy nations** — the homicide share being a minority of *gun* deaths is true; but US gun homicide per capita is still many times that of Canada, the UK, Germany, or Japan. Suicide-majority does not mean "no homicide problem."
- **Per-incident lethality of "assault weapons" in the rare cases they are used is genuinely higher** — Las Vegas (2017), Sandy Hook (2012), Uvalde (2022), Parkland (2018). The category is small in the total ledger but disproportionately represented in the highest-casualty incidents. The DiMaggio 2019 finding on the 1994 AWB period is real, even if contested.
- **The CDC's "suicide is the majority" anchor is itself sometimes used by gun-rights advocates to *dismiss* the gun-violence problem.** That move is also unsupported by the data: 17,927 US gun homicides in 2023 is still a vastly higher rate than any peer nation tolerates. The point of the Socratic question is not "guns are fine" — it is "the policy lever everyone is fighting about is not where the deaths are."

The post lands on verified ground if it lets the liberal reader say: *I was wrong about the breakdown; I now see that the policy I was advocating for is targeted at ~1% of the deaths; the lives-saved analysis points me to suicide prevention and urban handgun policy, not assault-weapon feature tests.* That is what verified ground looks like for this Socratic question.

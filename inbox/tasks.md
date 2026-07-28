# algos-vs-life — post-feedback edit

Vadim edits, section by section. Claude rereads + verifies each on the live page
(http://127.0.0.1:4700/riddle-me-this/adventures/2026/07/26/algos-vs-life.html).
Source diagnosis: `inbox/anton-claude.md`.

## Pass 1 — the edit (in reading order)

- [x] **Whole document:** `Mr. S` → `Mr. Suit`, spelled out everywhere — V
- [x] **Dialogue (~L50–63):** rewrite suit's gloat — schoolyard taunt → self-condemning
      polish ("That's the optimal solution. We benchmarked it -- on the whiteboard.") — V
- [x] **Intro tail (~L65–67):** delete the mercy motive ("didn't want to hurt his pride"),
      keep the nod; delete "yet"; verdict → bet (or pure riddle — feel it) — V
- [x] **The Problem (~L94):** trim seniority clause ("when one codes enough through
      decades"); keep the weapon-systems / drone example — V
- [x] **After the table (~L141–146):** suit exits; "Where did the whiteboard part ways
      with the machine?" (callback to the gloat) — V+C
- [x] **#3 listing note (~L190):** "as the whiteboard promised" — V+C
- [x] **But Why? (~L302–308):** opener now "So where did the whiteboard go wrong?
      Nowhere -- in 1979."; victims list de-suited ("the algorithm flaw") — V+C
- [x] **IMC section (~L376):** dropped "by lack of engineering competence"; "you'd" → "we'd" — V+C
- [x] **Flawed Algorithm (~L404–409):** "ignorant sin" → cargo-cult + Frum!/No Frum pair;
      last suit mention out; subject = the accumulator — V+C
- [x] **Claude:** after each section — reread file, check live render, flag anything
      that re-personalizes or leaks — C
- [x] **Claude:** final sweep — grep + live-page JS check: zero leak words, zero suit
      after the table, all edits render, SVGs load, 8 Rouge blocks, no attr leaks — C

- [x] **Footnote pair (grew out of Pass 1):** [1] Devil's Advocate at "Sounds reasonable?"
      (USACO Guide source, Lucy-'splain deliverable) + [3] antipattern trailhead at
      "well documented antipattern" (Wikipedia loop-carried, Algorithmica, Lemire) —
      all sources fetched and verified, render checked live — V+C

## Pass 2 — postproduction (separate, after Pass 1 lands)

- [x] Postproduction section written (V) + reviewed (C): loved/didn't-love lists, trope
      bullet added, idiom fixes, wizard's-verdict beat — V+C
- [x] Placed: `'''` + "== Postproduction and Feedback" after Easter-Egging — V
- [x] Corrections from the comment pile: all covered by tone pass + footnotes + postprod — V
- [ ] Live verify + Vadim closes (Verifier per TEAM_NORMS) — V

## Keep untouched (verified against canon)
Title, doers-vs-talkers thesis, the nod itself, "WHAT WOULD YOU DO IN MY PLACE?!",
8088 generosity, "the flaw is the crime," Claude/KDocs box, Candidate Master beat,
closing riddle + exercises, the withheld ParallelSlider.

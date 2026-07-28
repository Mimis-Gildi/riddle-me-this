# algos-vs-life — post-feedback edit

Vadim edits, section by section. Claude rereads + verifies each on the live page
(http://127.0.0.1:4700/riddle-me-this/adventures/2026/07/26/algos-vs-life.html).
Source diagnosis: `inbox/anton-claude.md`.

## Pass 1 — the edit (in reading order)

- [x] **Whole document:** `Mr. S` → `Mr. Suit`, spelled out everywhere — V
- [x] **Dialogue (~L50–63):** rewrite suit's gloat — schoolyard taunt → self-condemning
      polish ("That's the optimal solution. We benchmarked it -- on the whiteboard.") — V
- [ ] **Intro tail (~L65–67):** delete the mercy motive ("didn't want to hurt his pride"),
      keep the nod; delete "yet"; verdict → bet (or pure riddle — feel it) — V
- [ ] **The Problem (~L94):** trim seniority clause ("when one codes enough through
      decades"); keep the weapon-systems / drone example — V
- [ ] **After the table (~L141–146):** change grammatical subject — suit exits;
      intuition/machine takes over; second "hurt his pride" goes here too — V
- [ ] **#3 listing note (~L190):** "as Mr. S lamented" → intuition as agent — V
- [ ] **But Why? (~L302–308):** depersonalize opener; consider promoting the 8088
      paragraph to the frame ("right answer -- in 1979; what changed?") — V
- [ ] **IMC section (~L376):** drop "by lack of engineering competence" (reader-aimed) — V
- [ ] **Flawed Algorithm (~L404–409):** "ignorant sin" → cargo-cult / bogosity;
      subject = the accumulator, not the man — V
- [ ] **Claude:** after each section — reread file, check live render, flag anything
      that re-personalizes or leaks — C
- [ ] **Claude:** final sweep — grep for stray `Mr. S`, "pride", "yet", attribute leaks — C

## Pass 2 — postproduction (separate, after Pass 1 lands)

- [ ] Draft postproduction paragraph (V voice, C drafts if wanted): dozens of hacker
      comments; no algorithm here is absolutely right — the only ALWAYS-wrong one is
      the memoised accumulator; exploration paths left open on purpose; Mr. Suit
      spelled out as the trope he always was — V+C
- [ ] Place it: `'''` + `_P.S._` or small section after Easter-Egging — V
- [ ] Any remaining corrections from the comment pile (V lists them) — V
- [ ] Live verify + Vadim closes (Verifier per TEAM_NORMS) — V

## Keep untouched (verified against canon)
Title, doers-vs-talkers thesis, the nod itself, "WHAT WOULD YOU DO IN MY PLACE?!",
8088 generosity, "the flaw is the crime," Claude/KDocs box, Candidate Master beat,
closing riddle + exercises, the withheld ParallelSlider.

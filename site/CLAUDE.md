# Site-Specific Guidance for Claude Code

Operational guidance for working with the Jekyll site content.

---

## Workflow

Vadim writes. Claude critiques.
Voice comes from the post being written -- not from any "what Vadim sounds like" rules file.

---

## Authoritative References

- **Forbidden patterns (LLM-speak):** `~/.claude/memories/15-LLMTorturedLanguage.md`
  Authored by Vadim. The 12 documented patterns to detect and remove during review.
- **Argument forms and logical fallacies (abstract reference):** `./rdd13r-style-guide.yml`
  Universal logic reference. No voice claims.

---

## Hacker Scene Terminology

Classic reference: http://www.catb.org/jargon/html/index.html

**Modern terminology:**

| Term                 | Meaning                                                                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **poser**            | Political developer or IT manager no longer skilled but fitting well in lazy corporate culture                                            |
| **cog**              | Obedient developer eager to please but not competent; unimaginative office worker; reliable coder knowing only one deprecated application |
| — **knob**           | Lowest level manager of cogs, a cog themselves                                                                                            |
| — **shaft**          | Cog not yet a knob but aggravates other cogs to get the job done                                                                          |
| — **peg**            | Scapegoat cog, sacrificial to let others work in peace                                                                                    |
| — **actuator**       | A very classy knob                                                                                                                        |
| **brick**            | Monolithic system difficult to change; three-tiered architecture (database-service-presentation)                                          |
| **mortar**           | Glue holding bricks together; ESB, ancient enterprise messaging (IBM, ACORD, CDXF)                                                        |
| **rope**             | Writing undocumented crap code to create job security; codebase is rope, practice is roping                                               |
| **hinder**           | Code/module that slows progress by creating obstacles                                                                                     |
| **scoop**            | Tribal knowledge, especially created by roping                                                                                            |
| **litter/litterbox** | Repository of tribal knowledge; local files cogs keep secret and pass during KT                                                           |
| **fable**            | Corporate story told to amuse into obedience; synonym for knob in NE USA                                                                  |
| — **Fanny**          | Female fable (like Karen)                                                                                                                 |
| — **Freddy**         | Male Fanny                                                                                                                                |
| **local**            | Cog permanently bolted to team with many ropes, skeptical of new knowledge                                                                |
| **tourist**          | Coach or transformation architect brought in to upskill locals                                                                            |

---

## Document Patterns

**Front matter:**

```yaml
---
categories: [ reflections ]
tags: [ AI, Competence, Deprecation ]
excerpt: >
  One-sentence hook for LinkedIn / SEO.
classes: wide
comments: true
hidden: false
search: true
read_aloud: false
---
```

**AsciiDoc attributes** for repeated links and long alt text:

```asciidoc
:mg: https://github.com/Mimis-Gildi[Mímis Gildi,window=_blank]
:full-url: /riddle-me-this/reflections/2026/04/23/some-article.html
```

For site-internal links, use `link:{full-url}[text,window=_blank]`.

**Images:** `image::/riddle-me-this/assets/images/filename.png[alt text]`

**Captions:** `.Caption text` on the line above the image block.

**Postscripts:**

```asciidoc
'''

_P.S. Brief postscript here._
```

Horizontal rule is `'''` (AsciiDoc), NOT Markdown `---`. Use sparingly.

"""Reporter — structured console output and optional CSV export from a loaded Site."""
from __future__ import annotations

from pathlib import Path

from functional import seq


class Reporter:

    def __init__(self, site):
        self._site = site

    def report(self) -> int:
        violations  = self._site.body_link_violations().to_list()
        shadowed    = self._site.shadowed_globals().to_list()
        duplicates  = self._site.cross_article_duplicates().to_list()
        candidates  = self._site.promotion_candidates().to_list()

        print("=== Body Link Violations ===")
        seq(violations).for_each(lambda a: print(f"  {a.path.name}"))

        print("=== Shadowed Globals ===")
        seq(shadowed).for_each(lambda pair: print(f"  {pair[0].path.name}: {pair[1].key}"))

        print("=== Cross-Article Duplicates ===")
        seq(duplicates).for_each(lambda kg: print(
            f"  {kg[0]}: " + seq(kg[1]).map(lambda a: a.path.name).make_string(", ")))

        print("=== Promotion Candidates ===")
        seq(candidates).for_each(lambda ug: print(f"  {len(ug[1]):>3}x  {ug[0]}"))

        if not violations and not shadowed and not duplicates:
            print("All clean.")

        return 1 if violations else 0

    def to_csvs(self, out_dir: Path) -> None:
        out_dir.mkdir(parents=True, exist_ok=True)

        (seq([("article", "body_links_count")]) +
         seq(self._site.body_link_violations())
         .map(lambda a: (str(a.path.name), len(a.links_body)))
         ).to_csv(str(out_dir / "body_violations.csv"))

        (seq([("article", "key", "value")]) +
         seq(self._site.shadowed_globals())
         .map(lambda pair: (str(pair[0].path.name), pair[1].key, pair[1].value))
         ).to_csv(str(out_dir / "shadowed_globals.csv"))

        (seq([("key", "articles")]) +
         seq(self._site.cross_article_duplicates())
         .map(lambda kg: (kg[0], seq(kg[1]).map(lambda a: a.path.name).make_string("; ")))
         ).to_csv(str(out_dir / "cross_article_duplicates.csv"))

        (seq([("url", "count")]) +
         seq(self._site.promotion_candidates())
         .map(lambda ug: (ug[0], len(ug[1])))
         ).to_csv(str(out_dir / "promotion_candidates.csv"))

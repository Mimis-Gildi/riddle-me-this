"""Tests for cross-article promotion candidate analysis."""
from blog.parametrize_links import POST_ROOT
from blog.parametrize_links.promotion_candidates import find_promotion_candidates


class TestPromotionCandidates:
    """Tests for find_promotion_candidates against the real _posts folder."""

    def test_find_promotion_candidates(self):
        """Run against real _posts and print all external URLs declared in more than one article."""
        candidates = find_promotion_candidates(POST_ROOT)
        candidates.for_each(lambda url_group: print(f"{len(url_group[1]):>3}x  {url_group[0]}"))

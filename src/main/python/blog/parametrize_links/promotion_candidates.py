"""Cross-article promotion candidate analysis — external links declared in more than one article."""
from pathlib import Path

from functional import seq

from blog.parametrize_links.article import Article
from blog.parametrize_links.article_attribute_providers import read_declared_link_attributes_provider


def find_promotion_candidates(post_root: Path):
    """Return external link values declared in more than one article, grouped by bare URL."""
    return (
        seq(post_root.glob("*.adoc"))
        .map(lambda path: Article(path))
        .map(lambda article: read_declared_link_attributes_provider(article)())
        .flatten()
        .filter(lambda attr: attr.value.startswith(("http://", "https://")))
        .group_by(lambda attr: attr.value.split("[")[0])
        .filter(lambda url_group: len(url_group[1]) > 1)
        .sorted(key=lambda url_group: len(url_group[1]), reverse=True)
    )

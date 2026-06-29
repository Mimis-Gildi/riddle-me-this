"""Concrete Article File AttributeProvider implementations."""
import re

from functional import seq

from blog.parametrize_links import Article
from blog.parametrize_links.attributes import Attribute, AttributeProvider


def read_declared_link_attributes_provider(article: Article) -> AttributeProvider:
    """Provider that reads declared attributes from an article collecting only links in form of: URL, full link, and footer."""
    return lambda: (
        seq(re.finditer(r'^:([^:]+):\s+(.+)$', article.text, re.MULTILINE))
        .filter(lambda m: m.group(2).startswith(("http://", "https://", "link:", "footnote:", "mailto:")))
        .map(lambda m: Attribute(m.group(1), m.group(2), m.start()))
    )

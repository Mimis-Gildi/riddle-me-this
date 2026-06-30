"""Concrete Article File AttributeProvider implementations."""
import re

from functional import seq

from blog.parametrize_links import Article
from blog.parametrize_links.attributes import Attribute, AttributeProvider


def _included_texts(article: Article) -> list:
    """Resolve include:: directives in article text and return the text of each included file."""
    return (
        seq(re.finditer(r'^include::([^\[]+)\[', article.text, re.MULTILINE))
        .map(lambda m: article.path.parent / m.group(1))
        .filter(lambda p: p.exists())
        .map(lambda p: p.read_text(encoding="utf-8"))
        .to_list()
    )


def read_declared_link_attributes_provider(article: Article) -> AttributeProvider:
    """Provider that reads declared attributes from an article and its includes, collecting only links."""
    def _extract(text: str):
        return (
            seq(re.finditer(r'^:([^:]+):\s+(.+)$', text, re.MULTILINE))
            .filter(lambda m: m.group(2).startswith(("http://", "https://", "link:", "footnote:", "mailto:")))
            .map(lambda m: Attribute(m.group(1), m.group(2), m.start()))
        )
    return lambda: (
        seq([article.text] + _included_texts(article))
        .flat_map(_extract)
    )

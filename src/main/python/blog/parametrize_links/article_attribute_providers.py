"""Concrete Article File AttributeProvider implementations."""
import re

from functional import seq

from blog.parametrize_links import Article
from blog.parametrize_links.attributes import Attribute, AttributeProvider, LINK_VALUE_PREFIXES


def _included_texts(article: Article) -> list:
    """Resolve include:: directives in article text and return the text of each included file."""
    return (
        seq(re.finditer(r'^include::([^\[]+)\[', article.text, re.MULTILINE))
        .map(lambda m: article.path.parent / m.group(1))
        .filter(lambda p: p.exists())
        .map(lambda p: p.read_text(encoding="utf-8"))
        .to_list()
    )


def _slug_from_display(display_raw: str) -> str:
    """Derive an attribute key from AsciiDoc link display text: first 2-3 words, slugified."""
    text = display_raw.split(',')[0]
    text = re.sub(r'[*"@\'#`]', '', text)
    return (
        seq(text.strip().split()[:3])
        .map(lambda w: re.sub(r'[^a-z0-9.]', '', w.lower()))
        .filter(lambda p: p)
        .make_string('-')
    )


def read_body_link_attributes_provider(article: Article) -> AttributeProvider:
    """Provider that finds raw inline links in article body (non-declaration lines)."""
    def _extract():
        body = (
            seq(article.text.splitlines())
            .filter(lambda line: not re.match(r'^:[^:]+:\s+', line))
            .filter(lambda line: not re.match(r'^image::', line))
            .make_string('\n')
        )
        return (
            seq(re.finditer(r'(?:link:)?(https?://[^\[\n]+)\[([^\]]+)\]', body))
            .map(lambda m: Attribute(
                _slug_from_display(m.group(2)),
                m.group(1) + '[' + m.group(2) + ']',
                m.start(),
            ))
        )
    return _extract


def read_declared_link_attributes_provider(article: Article) -> AttributeProvider:
    """Provider that reads declared attributes from an article and its includes, collecting only links."""
    def _extract(text: str):
        return (
            seq(re.finditer(r'^:([^:]+):\s+(.+)$', text, re.MULTILINE))
            .filter(lambda m: m.group(2).startswith(LINK_VALUE_PREFIXES))
            .map(lambda m: Attribute(m.group(1), m.group(2), m.start()))
        )
    return lambda: (
        seq([article.text] + _included_texts(article))
        .flat_map(_extract)
    )

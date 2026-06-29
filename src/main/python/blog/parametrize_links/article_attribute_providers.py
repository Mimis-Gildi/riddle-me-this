"""Concrete Article File AttributeProvider implementations."""
from blog.parametrize_links import Article
from blog.parametrize_links.attributes import AttributeProvider


def read_declared_link_attributes_provider(article: Article) -> AttributeProvider:
    """Provider that reads declared attributes from an article collecting only links in form of: URL, full link, and footer."""

    return AttributeProvider()

"""Concrete AttributeProvider implementations."""
from __future__ import annotations

from pathlib import Path

import yaml
from functional import seq

from .attributes import Attribute, AttributeProvider, AttributeFilterProvider

DERIVED_BASEURL = "site-baseurl"
RESERVED_BASEURL = "baseurl"
EXPECTED_ROOT_SLUG = "/riddle-me-this"
GLOBAL_POSITION = -1


def global_link_attribute_collecting_provider(
        global_static_derived_attribute_provider: AttributeProvider,
        config_file_attribute_provider: AttributeProvider,
        attribute_filter_provider: AttributeFilterProvider
) -> AttributeProvider:
    """A lazy composite provider of currently global link attributes as expected by each post, page, and article."""
    return lambda: (
        seq([global_static_derived_attribute_provider(), config_file_attribute_provider()])
        .flatten()
        .filter(lambda attr: attribute_filter_provider(attr.to_tuple()))
    )


def static_links_provider() -> AttributeProvider:
    """A lazy provider of attributes the framework will inject runtime in different scopes to be resolved edit time."""
    return lambda: seq([
        Attribute(RESERVED_BASEURL, EXPECTED_ROOT_SLUG, GLOBAL_POSITION),
        Attribute(DERIVED_BASEURL, EXPECTED_ROOT_SLUG, GLOBAL_POSITION),
    ])

def config_links_provider(conf: Path) -> AttributeProvider:
    """A lazy composite provider of global link attributes as expected by each post and sources from config system of record."""
    return lambda: seq(
        ((yaml.safe_load(conf.read_text(encoding="utf-8")).get("asciidoctor") or {})
         .get("attributes") or {}).items()
    ).smap(lambda key, value: Attribute(key, value, GLOBAL_POSITION))

def filter_provider() -> AttributeFilterProvider:
    """Attributes found at varies configuration levels that are not links document cleanup is concerned with."""
    return lambda kvp: kvp[0] not in {"icons", "baseurl"}


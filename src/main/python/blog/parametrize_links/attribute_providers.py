"""Concrete AttributeProvider implementations."""
from __future__ import annotations

from typing import Iterable

from functional import seq

from .attributes import Attribute

GLOBAL_POSITION = -1

def global_link_attributes(
        cfg: dict,
        baseurl: Iterable[tuple[str, str]],
) -> Iterable[Attribute]:
    attrs = (cfg.get("asciidoctor") or {}).get("attributes") or {}
    return (
        seq([baseurl, attrs.items()])
        .flatten()
        .filter(lambda kv: kv[0] != "icons")
        .smap(lambda key, value: Attribute(key, value.removesuffix("@"), GLOBAL_POSITION))
    )

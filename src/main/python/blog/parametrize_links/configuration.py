"""Configuration — reads _config.yml, discovers Jekyll content collections, owns global links."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml
from functional import seq

from .attribute_providers import (
    global_link_attribute_collecting_provider,
    static_links_provider,
    config_links_provider,
    filter_provider,
)
from .attributes import Attribute


@dataclass
class Configuration:
    site_root: Path

    _conf_file: Path = field(init=False)
    _collections: tuple[Path, ...] = field(init=False)
    _global_links: tuple[Attribute, ...] = field(init=False)

    def __post_init__(self):
        if not self.site_root.exists():
            raise FileNotFoundError(self.site_root)
        self._conf_file = self.site_root / "_config.yml"
        if not self._conf_file.exists():
            raise FileNotFoundError(self._conf_file)
        self._collections = self._discover_collections()
        self._global_links = tuple(
            global_link_attribute_collecting_provider(
                static_links_provider(),
                config_links_provider(self._conf_file),
                filter_provider(),
            )()
        )

    def _discover_collections(self) -> tuple[Path, ...]:
        include = (
            yaml.safe_load(self._conf_file.read_text(encoding="utf-8")) or {}
        ).get("include", [])
        return tuple(
            seq(["_posts"] + list(include))
            .map(lambda name: self.site_root / name)
            .filter(lambda p: p.is_dir())
            .filter(lambda p: seq(p.glob("*.adoc")).non_empty())
        )

    @property
    def conf_file(self) -> Path:
        return self._conf_file

    @property
    def collections(self):
        return seq(self._collections)

    @property
    def global_links(self) -> tuple[Attribute, ...]:
        return self._global_links

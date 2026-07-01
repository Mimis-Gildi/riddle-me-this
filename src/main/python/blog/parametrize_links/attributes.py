"""Attributes -- the named links an article carries, and how they are supplied."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class Attribute:
    """A single attribute: its key, its value, and where it sits."""

    key: str
    value: str
    position: int

    @classmethod
    def from_tuple(cls, triple: tuple[str, str, int]) -> Attribute:
        return cls(*triple)

    def to_tuple(self) -> tuple[str, str, int]:
        return self.key, self.value, self.position


AttributeProvider = Callable[[], Iterable[Attribute]]
AttributeFilterProvider = Callable[[tuple[str, str, int]], bool]

LINK_VALUE_PREFIXES = ("http://", "https://", "link:", "footnote:", "mailto:")

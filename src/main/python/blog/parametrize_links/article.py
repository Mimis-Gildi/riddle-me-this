"""The Article container -- a validated, immutable AsciiDoc article."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Article:
    """Immutable snapshot of an article: its path, its text, and integrity anchors."""

    path: Path

    def __post_init__(self) -> None:
        if self.path.suffix != ".adoc":
            raise ValueError(f"not an AsciiDoc file: {self.path}")

        text = self.path.read_text(encoding="utf-8")
        object.__setattr__(self, "_Article__text", text)

        object.__setattr__(self, "_Article__content_length", len(text))
        object.__setattr__(self, "_Article__file_checksum", _shasum(self.path))

    @property
    def file_checksum(self) -> str:
        return self.__file_checksum

    @property
    def content_length(self) -> int:
        return self.__content_length


def _shasum(path: Path) -> str:
    result = subprocess.run(
        ["shasum", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.split()[0]

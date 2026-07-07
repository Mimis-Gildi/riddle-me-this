"""The Article container -- a validated, immutable AsciiDoc article."""

from __future__ import annotations

import functools
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Self

from functional import seq

from .attributes import Attribute, AttributeProvider


def call_only_once(func):
    attr_name = "_called_funcs"

    def called_funcs_of_instance(instance) -> set:
        called_funcs = getattr(instance, attr_name, set())
        if not called_funcs:
            setattr(instance, attr_name, called_funcs)
        return called_funcs

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        called_funcs = called_funcs_of_instance(self)
        if func in called_funcs:
            raise RuntimeError("This operation can only be invoked once.")
        called_funcs.add(func)
        return func(*args, **kwargs)
    return wrapper

@dataclass()
class Article:
    """Immutable snapshot of an article: its path, its text, and integrity anchors."""

    path: Path
    _text: str = field(init=False)

    _file_checksum: str = field(init=False)
    _content_length: int = field(init=False)

    _links_attribute_provider_global:  AttributeProvider = field(init=False)
    _links_global:  tuple[Attribute, ...] = field(init=False)

    _links_declared_attributes_provider: AttributeProvider = field(init=False)
    _links_declared: tuple[Attribute, ...] = field(init=False)

    _links_body_attributes_provider: AttributeProvider = field(init=False)
    _links_body: tuple[Attribute, ...] = field(init=False)

    @property
    def text(self):
        return self._text

    @text.setter
    @call_only_once
    def text(self, first_text):
        self._text = first_text

    @text.deleter
    def text(self):
        raise ValueError("This 'text' value cannot be delete.")

    @property
    def file_checksum(self):
        return self._file_checksum

    @file_checksum.setter
    @call_only_once
    def file_checksum(self, os_provided_sum):
        self._file_checksum = os_provided_sum

    @file_checksum.deleter
    def file_checksum(self):
        raise ValueError("This 'file_checksum' cannot be deleted.")

    @property
    def content_length(self):
        return self._content_length

    @content_length.setter
    @call_only_once
    def content_length(self, initial_length):
        self._content_length = initial_length

    @content_length.deleter
    def content_length(self):
        raise ValueError("This 'content_length' cannot be deleted.")

    @property
    def links_provider_global(self):
        return self._links_attribute_provider_global

    @links_provider_global.setter
    @call_only_once
    def links_provider_global(self, provider: AttributeProvider):
        """Accept the Global Attributes Provider and store it -- it is called later (deferred), not now."""
        self._links_attribute_provider_global = provider

    @links_provider_global.deleter
    def links_provider_global(self):
        raise ValueError("This 'links_provider_global' cannot be deleted.")

    @property
    def links_global(self):
        return self._links_global

    @links_global.setter
    @call_only_once
    def links_global(self, links):
        """Accept the Global Links and store it -- it is called later (deferred), not now."""
        self._links_global = links

    @links_global.deleter
    def links_global(self):
        raise ValueError("This 'links_global' cannot be deleted.")

    @property
    def links_provider_declared(self):
        return self._links_declared_attributes_provider

    @links_provider_declared.setter
    @call_only_once
    def links_provider_declared(self, provider: AttributeProvider):
        """Accept the Declared Attributes Provider and store it -- it is called later (deferred), not now."""
        self._links_declared_attributes_provider = provider

    @links_provider_declared.deleter
    def links_provider_declared(self):
        raise ValueError("This 'links_provider_declared' cannot be deleted.")

    @property
    def links_declared(self):
        return self._links_declared

    @links_declared.setter
    @call_only_once
    def links_declared(self, links):
        """Accept the Declared Links and store it -- it is called later (deferred), not now."""
        self._links_declared = links

    @links_declared.deleter
    def links_declared(self):
        raise ValueError("This 'links_declared' cannot be deleted.")

    @property
    def links_provider_body(self):
        return self._links_body_attributes_provider

    @links_provider_body.setter
    @call_only_once
    def links_provider_body(self, provider: AttributeProvider):
        self._links_body_attributes_provider = provider

    @links_provider_body.deleter
    def links_provider_body(self):
        raise ValueError("This 'links_provider_body' cannot be deleted.")

    @property
    def links_body(self):
        return self._links_body

    @links_body.setter
    @call_only_once
    def links_body(self, links):
        self._links_body = links

    @links_body.deleter
    def links_body(self):
        raise ValueError("This 'links_body' cannot be deleted.")

    def __post_init__(self) -> None:
        if self.path.suffix != ".adoc":
            raise ValueError(f"not an AsciiDoc file: {self.path}")

        self.text = self.path.read_text(encoding="utf-8")
        self.file_checksum = _shasum(self.path)
        self.content_length = len(self.text)

    def accept_global_link_attribute_provider(self, provider: AttributeProvider) -> Self:
        """Accept the Global Link Attributes Provider and store it -- it is called later (deferred), not now."""
        self.links_provider_global = provider
        return self

    def accept_header_defined_attribute_provider(self, provider: AttributeProvider) -> Self:
        """Accept the File Header Link Attributes Provider and store it -- it is called later (deferred), not now."""
        self.links_provider_declared = provider
        return self

    def accept_body_discovery_attribute_provider(self, provider: AttributeProvider) -> Self:
        """Accept the Body Link Discovery Attributes Provider and store it -- it is called later (deferred), not now."""
        self.links_provider_body = provider
        return self

    def apply_global_links_acquisition(self) -> Self:
        """Acquire global links by calling the deferred global provider."""
        self.links_global = tuple(self.links_provider_global())
        return self

    def apply_header_links_acquisition(self) -> Self:
        """Acquire file header defined links by calling the deferred header links provider."""
        self.links_declared = tuple(self.links_provider_declared())
        return self

    def apply_document_body_links_acquisition(self) -> Self:
        """Acquire all the links used inside document body with and without attributes."""
        self.links_body = tuple(self.links_provider_body())
        return self

    def print_global_links(self) -> Self:
        """Print global links, a sideeffect introspective function."""
        seq(self.links_global).for_each(print)
        return self

    def print_body_links(self) -> Self:
        """Print body links, a sideeffect introspective function."""
        seq(self.links_body).for_each(print)
        return self

    def print_declared_links(self) -> Self:
        """Print declared links, a sideeffect introspective function."""
        seq(self.links_declared).for_each(print)
        return self

def _shasum(path: Path) -> str:
    result = subprocess.run(
        ["shasum", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.split()[0]

#!/usr/bin/env python3
"""Update version references across configured files. Replaces badges and versioned links.
Validates structural match counts. Warns on version drift. Self-healing."""
from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Final, TextIO, TypedDict


# --- Pure utility functions ---

def _ordinal(n: int) -> str:
    """Return ordinal suffix for a day number: 1->st, 2->nd, 3->rd, 4->th, etc."""
    if 11 <= n % 100 <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def read_lines(path: Path) -> list[str]:
    """Read the file into lines with endings preserved. Raises FileNotFoundError."""
    return path.read_text().splitlines(keepends=True)


def find_line(lines: list[str], predicate: Callable[[str], bool]) -> tuple[int, str]:
    """Find the first line matching predicate. Returns (index, line). Raises ValueError if not found."""
    for i, line in enumerate(lines):
        if predicate(line):
            return i, line
    raise ValueError("No line matched the predicate")


def replace_line(lines: list[str], index: int, new_line: str) -> list[str]:
    """Return a new list with the line at index replaced. Pure."""
    result: list[str] = lines.copy()
    result[index] = new_line
    return result


def write_lines(path: Path, lines: list[str]) -> None:
    """Write lines back to the file."""
    path.write_text("".join(lines))


def readme_revision(version: str) -> str:
    """Build AsciiDoc revision line: 'vX.X.X, DayOfWeek Month DayOrd Year'."""
    today: date = date.today()
    day_s: str = f"{today.day}{_ordinal(today.day)}"
    return f"{version}, {today.strftime('%A %B')} {day_s} {today.year}\n"


# --- Constants ---

REQUIRED_ENV_VARS: Final[tuple[str, ...]] = ("DRY_RUN", "SUPERSEDED", "CURRENT", "PUBLISHED", "REPLACEMENTS")
VERSION_RE: Final[str] = r'v\d+\.\d+\.\d+'


# --- Data model ---

class ActionResult(Enum):
    """Outcome of a single replacement action."""
    PENDING = "Pending"
    APPLIED = "Applied"
    DRY_RUN = "Dry Run"
    FAILED = "Failed"


class TargetDict(TypedDict):
    """Expected JSON shape for a link replacement target."""
    path: str
    pattern: str
    count: int


@dataclass(slots=True)
class Target:
    """Parsed replacement target from caller JSON. Input specification only."""
    path: Path
    pattern: str
    expected_count: int

    @staticmethod
    def from_dict(obj: TargetDict) -> Target:
        """Build a Target from a decoded JSON object. Validates types explicitly."""
        path_v: str | None = obj.get("path")
        pattern_v: str | None = obj.get("pattern")
        count_v: int | None = obj.get("count")
        if not isinstance(path_v, str) or not isinstance(pattern_v, str) or not isinstance(count_v, int):
            raise ValueError(
                f"Invalid target (expected path:str, pattern:str, count:int): {obj!r}"
            )
        return Target(path=Path(path_v), pattern=pattern_v, expected_count=count_v)


@dataclass(slots=True)
class ReplacementAction:
    """Single replacement intent with its outcome. Produced by compute stages, executed by applying."""
    path: Path
    index: int
    old_line: str
    new_line: str
    label: str
    result: ActionResult = ActionResult.PENDING
    warning: str = ""

    @staticmethod
    def for_readme_badge(version: str) -> ReplacementAction:
        """Produce a replacement action for the README.adoc revision badge."""
        readme: Path = Path("README.adoc")
        lines: list[str] = read_lines(readme)
        idx: int
        old: str
        idx, old = find_line(lines, lambda l: bool(re.match(VERSION_RE + r',', l)))
        return ReplacementAction(
            path=readme,
            index=idx,
            old_line=old,
            new_line=readme_revision(version),
            label="README revision badge",
        )

    @staticmethod
    def for_copyright_badge(version: str) -> ReplacementAction:
        """Produce a replacement action for the site/_config.yml copyright badge."""
        config: Path = Path("site/_config.yml")
        lines: list[str] = read_lines(config)
        idx: int
        old: str
        idx, old = find_line(lines, lambda l: "© Vadim Kuhay;" in l)
        return ReplacementAction(
            path=config,
            index=idx,
            old_line=old,
            new_line=re.sub(VERSION_RE, version, old),
            label="Copyright badge",
        )

    @staticmethod
    def for_links(target: Target, superseded: str, current: str) -> list[ReplacementAction]:
        """Produce replacement actions for a versioned link target -- one per matching line.
        Matches by structure (any version), not by a specific version. Stores drift warning if found."""
        structural_pattern: str = re.escape(target.pattern).replace(re.escape("{version}"), VERSION_RE)
        lines: list[str] = read_lines(target.path)
        matches: list[tuple[int, str]] = [(i, l) for i, l in enumerate(lines) if re.search(structural_pattern, l)]
        if len(matches) != target.expected_count:
            raise ValueError(
                f"{target.path.as_posix()}: expected {target.expected_count} structural matches "
                f"of '{target.pattern}', found {len(matches)}"
            )
        actions: list[ReplacementAction] = []
        for idx, old in matches:
            found_match: re.Match[str] | None = re.search(VERSION_RE, old)
            drift: str = ""
            if found_match and found_match.group() != superseded:
                drift = f"Drift at {target.path.as_posix()}:{idx + 1}: expected {superseded}, found {found_match.group()}"
            actions.append(ReplacementAction(
                path=target.path,
                index=idx,
                old_line=old,
                new_line=re.sub(VERSION_RE, current, old),
                label=f"Link: {target.pattern}",
                warning=drift,
            ))
        return actions

    def apply(self, dry_run: bool) -> ReplacementAction:
        """Execute this replacement. Writes the file or marks as dry run."""
        if dry_run:
            self.result = ActionResult.DRY_RUN
        else:
            lines: list[str] = read_lines(self.path)
            write_lines(self.path, replace_line(lines, self.index, self.new_line))
            self.result = ActionResult.APPLIED
        return self

    def inspecting(self) -> None:
        """Print this action's state to stdout. Used by the diagnostic passthrough."""
        print(f"  [{self.label}] {self.path.as_posix()}:{self.index + 1} ({self.result.value})")
        print(f"    old: '{self.old_line.rstrip()}'")
        print(f"    new: '{self.new_line.rstrip()}'")
        if self.warning:
            print(f"    warning: {self.warning}")


# --- Runner ---

@dataclass(slots=True)
class ReplacementActionRunner:
    """Pipeline runner. Produces ReplacementActions, applies them, reports results."""

    dry_run: bool
    superseded_version: str
    current_version: str
    published_version: str
    targets: list[Target]
    actions: list[ReplacementAction] = field(default_factory=list)

    @classmethod
    def from_environment(cls) -> ReplacementActionRunner:
        """Read config and parse replacements from the environment into a configured runner.
        Fails fast with a comprehensive error listing every missing or empty required variable."""
        missing: list[str] = [name for name in REQUIRED_ENV_VARS if not os.environ.get(name, "").strip()]
        if missing:
            raise EnvironmentError(
                f"Missing or empty required environment variable(s): {', '.join(missing)}. "
                f"All of {', '.join(REQUIRED_ENV_VARS)} must be set by the caller."
            )
        raw_targets: Any = json.loads(os.environ["REPLACEMENTS"])
        if not isinstance(raw_targets, list):
            raise ValueError(
                f"REPLACEMENTS must be a JSON array of target objects, got {type(raw_targets).__name__}"
            )
        targets: list[Target] = [Target.from_dict(obj) for obj in raw_targets]
        return cls(
            dry_run=os.environ["DRY_RUN"].lower() in ("true", "1", "yes"),
            superseded_version=os.environ["SUPERSEDED"],
            current_version=os.environ["CURRENT"],
            published_version=os.environ["PUBLISHED"],
            targets=targets,
        )

    def inspecting(self) -> ReplacementActionRunner:
        """Diagnostic passthrough. Prints runner config. No-op when dry_run is off."""
        if not self.dry_run:
            return self
        print(f"Version References: {self.superseded_version} -> {self.current_version} (published: {self.published_version})")
        print(f"Dry run: {self.dry_run}")
        print(f"Link targets: {len(self.targets)}")
        return self

    def computing_badges(self) -> ReplacementActionRunner:
        """Produce badge replacement actions."""
        self.actions.append(ReplacementAction.for_readme_badge(self.current_version))
        self.actions.append(ReplacementAction.for_copyright_badge(self.current_version))
        return self

    def computing_links(self) -> ReplacementActionRunner:
        """Produce link replacement actions from targets."""
        for target in self.targets:
            self.actions.extend(
                ReplacementAction.for_links(target, self.superseded_version, self.current_version)
            )
        return self

    def applying(self) -> ReplacementActionRunner:
        """Intermediate. Each action applies itself, annotating its own result."""
        for action in self.actions:
            action.apply(self.dry_run)
        return self

    def inspecting_actions(self) -> ReplacementActionRunner:
        """Diagnostic passthrough. Prints all action states. No-op when dry_run is off."""
        if not self.dry_run:
            return self
        print(f"Actions ({len(self.actions)}):")
        for action in self.actions:
            action.inspecting()
        return self

    def write_summary(self) -> None:
        """Terminal. Print the outcome table to GITHUB_STEP_SUMMARY and annotations to stdout."""
        summary_path: str | None = os.environ.get("GITHUB_STEP_SUMMARY")
        out: TextIO = open(summary_path, "a") if summary_path else sys.stdout

        print(f"\n### Version Reference Updates: {self.superseded_version} -> {self.current_version} (published: {self.published_version})\n", file=out)
        print("| Label | File | Old | New | Result | Warning |", file=out)
        print("|-------|------|-----|-----|--------|---------|", file=out)
        for action in self.actions:
            path_s: str = action.path.as_posix()
            warn_s: str = action.warning if action.warning else ""
            print(f"| {action.label} | {path_s}:{action.index + 1} | `{action.old_line.rstrip()}` | `{action.new_line.rstrip()}` | {action.result.value} | {warn_s} |", file=out)

        if out is not sys.stdout:
            out.close()

        for action in self.actions:
            if action.warning:
                print(f"::warning title=Version Drift::{action.warning}")


if __name__ == "__main__":
    ReplacementActionRunner\
        .from_environment()\
        .inspecting()\
        .computing_badges()\
        .computing_links()\
        .applying()\
        .inspecting_actions()\
        .write_summary()

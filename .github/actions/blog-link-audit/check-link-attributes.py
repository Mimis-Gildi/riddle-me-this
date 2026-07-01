#!/usr/bin/env python
"""Blog link attribute checker — composite action entry point."""
import contextlib
import io
import os
import re
import subprocess


def _issue_number() -> str | None:
    branch = os.environ.get("GITHUB_REF_NAME", "")
    m = re.match(r'^(\d+)', branch)
    return m.group(1) if m else None


def _detect_repository() -> str:
    return os.environ.get("GITHUB_REPOSITORY") or subprocess.run(
        ["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"],
        capture_output=True, text=True
    ).stdout.strip()


def _run_audit() -> str:
    from blog.parametrize_links import main
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        main()
    return buf.getvalue()


def _post_comment(issue: str, repo: str, body: str) -> None:
    subprocess.run(
        ["gh", "issue", "comment", issue, "--repo", repo, "--body", body],
        check=True
    )


def main():
    issue = _issue_number()
    if not issue:
        print(f"No issue number in branch '{os.environ.get('GITHUB_REF_NAME', '')}' — skipping.")
        return

    report = _run_audit()
    branch = os.environ.get("GITHUB_REF_NAME", "")
    sha = os.environ.get("GITHUB_SHA", "")[:7]
    actor = os.environ.get("GITHUB_ACTOR", "")
    body = f"### Blog Link Audit — `{branch}`\n\n```\n{report.strip()}\n```\n\n_{actor} @ {sha}_"

    _post_comment(issue, _detect_repository(), body)


if __name__ == "__main__":
    main()
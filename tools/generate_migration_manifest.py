#!/usr/bin/env python3
"""Generate the complete 2021 GitBook-to-current migration manifest."""

from __future__ import annotations

import subprocess
from pathlib import Path, PurePosixPath
from urllib.parse import quote

from import_validated_wiki import LEGACY_STUBS, PAGE_MAP


ROOT = Path(__file__).resolve().parents[1]
BASELINE = "151a593c09f7443f67bae982b10e1447e19797ca"
BASELINE_TREE = "bed2eb3cdd497a3a670bd833f66da78465502964"


def baseline_files() -> list[str]:
    output = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", BASELINE], cwd=ROOT, text=True
    )
    return [line for line in output.splitlines() if line]


def public_url(path: str) -> str:
    if path == "README.md":
        return "https://docs.qwertycoin.org/"
    if path == "SUMMARY.md" or path.startswith(".gitbook/"):
        encoded = quote(path, safe="/")
        return f"https://github.com/qwertycoin-org/gitbook-docs/blob/{BASELINE}/{encoded}"
    slug = path.removesuffix(".md")
    if slug.endswith("/README"):
        slug = slug.removesuffix("/README")
    return f"https://docs.qwertycoin.org/{slug}"


def disposition(path: str) -> tuple[str, str, str]:
    current = set(PAGE_MAP.values())
    if path == "README.md":
        return "Rewrite", "[Current home](../README.md)", "Current information architecture"
    if path == "SUMMARY.md":
        return "Rewrite", "[Current navigation](../SUMMARY.md)", "Current information architecture"
    if path.startswith(".gitbook/assets/"):
        return (
            "Retain historical media",
            "Repository history / unreferenced asset",
            "No current page depends on this legacy image",
        )
    if path in current:
        return (
            "Rewrite",
            f"[Current page](../{path})",
            "Validated Wiki content and pinned implementation evidence",
        )
    if path in LEGACY_STUBS:
        _, replacement = LEGACY_STUBS[path]
        return (
            "Retire with replacement notice",
            f"[Compatibility page](../{path}) · [replacement](../{replacement})",
            "Current implementation does not support the historical workflow",
        )
    raise SystemExit(f"unclassified baseline file: {path}")


def main() -> int:
    rows = []
    for path in baseline_files():
        action, destination, evidence = disposition(path)
        subject = PurePosixPath(path).name
        rows.append(
            f"| `{path}` | [original]({public_url(path)}) | {subject} | {action} | "
            f"{destination} | {evidence} | Complete |"
        )
    if len(rows) != 60:
        raise SystemExit(f"expected 60 baseline files, found {len(rows)}")
    markdown_count = len(list(ROOT.rglob("*.md")))
    output = (
        "# Documentation migration manifest\n\n"
        f"> **Original snapshot:** `{BASELINE}`, tree `{BASELINE_TREE}`, 60 tracked files "
        "(45 Markdown files and 15 media assets).\n\n"
        "Every original page and support file has an intentional completed outcome. Old "
        "operational URLs remain short compatibility notices when the historical procedure is "
        "retired. The original bytes remain recoverable from Git history.\n\n"
        "| Original path | Original URL | Subject | Disposition | Destination | Evidence | Status |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        + "\n".join(rows)
        + "\n\n## Counts\n\n"
        "- Before: 60 tracked files — 45 Markdown files and 15 media assets.\n"
        f"- Current working tree: {markdown_count} Markdown files plus revision-bound support "
        "scripts/data and the 15 retained historical assets.\n"
    )
    target = ROOT / "reports" / "migration-manifest.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output)
    print(f"migration_rows={len(rows)} markdown_files={markdown_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

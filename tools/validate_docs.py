#!/usr/bin/env python3
"""Fail-closed structural validation for the Qwertycoin GitBook tree."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^]]+]\(([^)]+)\)")
FENCE = re.compile(r"^```", re.MULTILINE)
H1 = re.compile(r"^# (?!#)", re.MULTILINE)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
MANIFEST_ROW = re.compile(r"^\| `[^`]+` \| \[original]", re.MULTILINE)


def pages() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def anchors(text: str) -> set[str]:
    counts: dict[str, int] = {}
    result: set[str] = set()
    for heading in HEADING.findall(text):
        value = re.sub(r"<[^>]+>", "", heading)
        value = re.sub(r"[`*_~]", "", value).strip().lower()
        value = re.sub(r"[^\w\- ]", "", value)
        value = re.sub(r"\s+", "-", value)
        index = counts.get(value, 0)
        counts[value] = index + 1
        result.add(value if index == 0 else f"{value}-{index}")
    return result


def summary_contract(all_pages: list[Path]) -> set[Path]:
    summary = ROOT / "SUMMARY.md"
    targets: set[Path] = set()
    for raw in LINK.findall(summary.read_text()):
        parsed = urlsplit(raw.strip("<>"))
        if parsed.scheme or not parsed.path:
            continue
        target = (summary.parent / unquote(parsed.path)).resolve()
        if not target.is_file():
            raise AssertionError(f"SUMMARY.md: missing target {raw}")
        targets.add(target)
    expected = {path.resolve() for path in all_pages if path.name != "SUMMARY.md"}
    missing = expected - targets
    extra = targets - expected
    assert not missing, f"Markdown pages missing from SUMMARY.md: {sorted(str(x) for x in missing)}"
    assert not extra, f"Unexpected SUMMARY.md targets: {sorted(str(x) for x in extra)}"
    return targets


def page_contract(all_pages: list[Path]) -> None:
    errors: list[str] = []
    for page in all_pages:
        text = page.read_text()
        relative = page.relative_to(ROOT)
        if len(H1.findall(text)) != 1:
            errors.append(f"{relative}: expected exactly one H1")
        if len(FENCE.findall(text)) % 2:
            errors.append(f"{relative}: unbalanced code fence")
        if (
            page.name not in {"SUMMARY.md"}
            and not text.startswith("# Historical page:")
            and not relative.parts[0] == "reports"
            and relative != Path("api/rpc-inventory.md")
            and "> **Verified against:**" not in text
        ):
            errors.append(f"{relative}: missing Verified against header")
        for raw in LINK.findall(text):
            raw = raw.strip("<>")
            parsed = urlsplit(raw)
            if parsed.scheme or raw.startswith("mailto:"):
                continue
            target = page if not parsed.path else page.parent / unquote(parsed.path)
            target = target.resolve()
            if not target.is_file():
                errors.append(f"{relative}: missing local target {raw}")
                continue
            if parsed.fragment and target.suffix.lower() == ".md":
                fragment = unquote(parsed.fragment).lower()
                if fragment not in anchors(target.read_text()):
                    errors.append(f"{relative}: missing anchor {raw}")
    if errors:
        raise AssertionError("\n".join(errors))


def stale_content(all_pages: list[Path]) -> None:
    forbidden = re.compile(
        r"\b(walletd|xmr-stak|cryptonight)\b|\b8070\b|"
        r"--service-node(?:\b|-key|-port)|register_service_node",
        re.IGNORECASE,
    )
    errors: list[str] = []
    for page in all_pages:
        text = page.read_text()
        if text.startswith("# Historical page:"):
            continue
        for index, block in enumerate(re.findall(r"```[^\n]*\n(.*?)\n```", text, re.DOTALL), 1):
            match = forbidden.search(block)
            if match:
                errors.append(
                    f"{page.relative_to(ROOT)}: legacy token in code block {index}: {match.group(0)}"
                )
    if errors:
        raise AssertionError("\n".join(errors))


def config_contract() -> None:
    data = json.loads(subprocess.check_output(["yq", ".", "gitbook-docs.yaml"], cwd=ROOT))
    assert data["$schema"] == "https://api.gitbook.com/gitbook-docs.yaml"
    assert data["version"] == 1
    structure = data["site"]["structure"]
    assert len(structure) == 1
    assert sum(item.get("default") is True for item in structure) == 1
    assert structure[0]["type"] == "space"
    assert structure[0]["key"] == "space-1"
    assert structure[0]["content"]["directory"] == "./"


def migration_contract() -> None:
    text = (ROOT / "reports" / "migration-manifest.md").read_text()
    assert len(MANIFEST_ROW.findall(text)) == 60
    assert text.count("| Complete |") == 60


def rpc_contract() -> None:
    data = json.loads((ROOT / "rpc-inventory.json").read_text())
    assert len(data["routes"]) == 203
    assert len(data["release_routes"]) == 201
    assert sum(row["surface"] == "daemon" for row in data["routes"]) == 107
    assert sum(row["surface"] == "wallet" for row in data["routes"]) == 96


def main() -> int:
    all_pages = pages()
    summary_contract(all_pages)
    page_contract(all_pages)
    stale_content(all_pages)
    config_contract()
    migration_contract()
    rpc_contract()
    print(
        json.dumps(
            {
                "markdown_pages": len(all_pages),
                "migration_rows": 60,
                "rpc_development": 203,
                "rpc_release": 201,
                "status": "pass",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

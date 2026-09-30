#!/usr/bin/env python3
"""Check external documentation links without hammering immutable Core permalinks."""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\((https?://[^)]+)\)")
CORE_BLOB = re.compile(
    r"^https://github\.com/qwertycoin-org/qwertycoin/blob/"
    r"(?P<revision>[0-9a-f]{40})/(?P<path>[^#]+)(?:#L(?P<line>[0-9]+)(?:-L[0-9]+)?)?$"
)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--development-core", type=Path, required=True)
    parser.add_argument("--development-revision", required=True)
    parser.add_argument("--release-core", type=Path, required=True)
    parser.add_argument("--release-revision", required=True)
    parser.add_argument("--workers", type=int, default=8)
    return parser.parse_args()


def all_urls() -> set[str]:
    result: set[str] = set()
    for page in ROOT.rglob("*.md"):
        if ".git" in page.parts:
            continue
        result.update(match.strip("<>") for match in LINK.findall(page.read_text()))
    return result


def check_blob(url: str, trees: dict[str, Path]) -> str | None:
    match = CORE_BLOB.match(url)
    if not match:
        return None
    revision = match.group("revision")
    if revision not in trees:
        raise AssertionError(f"unmapped immutable Core revision: {url}")
    path = trees[revision] / unquote(match.group("path"))
    if not path.is_file():
        raise AssertionError(f"missing source permalink target: {url}")
    line = match.group("line")
    if line and int(line) > sum(1 for _ in path.open(errors="replace")):
        raise AssertionError(f"source permalink line outside file: {url}")
    return "source"


def check_http(url: str) -> tuple[str, int]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Qwertycoin-Documentation-Link-Check/1.0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.status
    except urllib.error.HTTPError as error:
        status = error.code
    if not 200 <= status < 400:
        raise AssertionError(f"HTTP {status}: {url}")
    return url, status


def main() -> int:
    args = arguments()
    trees = {
        args.development_revision: args.development_core,
        args.release_revision: args.release_core,
    }
    urls = all_urls()
    source = 0
    network: list[str] = []
    for url in sorted(urls):
        if check_blob(url, trees):
            source += 1
        else:
            network.append(url)
    errors: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(check_http, url): url for url in network}
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as error:  # noqa: BLE001 - aggregate every failed URL
                errors.append(str(error))
    if errors:
        raise AssertionError("\n".join(sorted(errors)))
    print(
        f"external_links={len(urls)} immutable_source_links={source} "
        f"network_links={len(network)} status=pass"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

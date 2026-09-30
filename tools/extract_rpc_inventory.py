#!/usr/bin/env python3
"""Extract Qwertycoin daemon and wallet RPC registrations from reachable route maps."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


ROUTE_RE = re.compile(r"^\s*(MAP_(?:URI|JON)[A-Z0-9_]*)\((.*)\)\s*$")


def split_args(value: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    depth = 0
    quoted = False
    escaped = False
    for char in value:
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\" and quoted:
            current.append(char)
            escaped = True
            continue
        if char == '"':
            quoted = not quoted
            current.append(char)
            continue
        if not quoted and char == "(":
            depth += 1
        elif not quoted and char == ")":
            depth -= 1
        if not quoted and depth == 0 and char == ",":
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    parts.append("".join(current).strip())
    return parts


def extract(header: Path, surface: str, revision: str) -> list[dict]:
    repository_root = header.parents[2]
    definitions = repository_root / (
        "src/rpc/core_rpc_server_commands_defs.h"
        if surface == "daemon"
        else "src/wallet/wallet_rpc_server_commands_defs.h"
    )
    definition_lines: dict[str, int] = {}
    for definition_line, definition_text in enumerate(definitions.read_text().splitlines(), 1):
        match = re.search(r"\bstruct\s+(COMMAND_RPC_[A-Z0-9_]+)\b", definition_text)
        if match and match.group(1) not in definition_lines:
            definition_lines[match.group(1)] = definition_line
    entries: list[dict] = []
    for line_number, line in enumerate(header.read_text().splitlines(), 1):
        match = ROUTE_RE.match(line)
        if not match:
            continue
        macro, raw_args = match.groups()
        args = split_args(raw_args)
        if len(args) < 3 or not (args[0].startswith('"') and args[0].endswith('"')):
            raise ValueError(f"unparsed route at {header}:{line_number}: {line}")
        endpoint = args[0][1:-1]
        transport = "json-rpc" if macro.startswith("MAP_JON_RPC") else (
            "binary-http" if "BIN" in macro else "json-http"
        )
        unrestricted_only = macro.endswith("_IF") and any("!m_restricted" in arg for arg in args[3:])
        command = args[2].replace("wallet_rpc::", "")
        schema_line = definition_lines.get(command)
        entries.append({
            "surface": surface,
            "endpoint": endpoint,
            "transport": transport,
            "handler": args[1],
            "command": command,
            "restricted_listener": "rejected" if unrestricted_only else (
                "handler-dependent" if surface == "wallet" else "available"
            ),
            "macro": macro,
            "source_file": str(header.relative_to(header.parents[2])),
            "source_line": line_number,
            "source_url": (
                f"https://github.com/qwertycoin-org/qwertycoin/blob/{revision}/"
                f"{header.relative_to(header.parents[2])}#L{line_number}"
            ),
            "schema_url": (
                f"https://github.com/qwertycoin-org/qwertycoin/blob/{revision}/"
                f"{definitions.relative_to(repository_root)}#L{schema_line}"
                if schema_line
                else None
            ),
        })
    return entries


def key(entry: dict) -> tuple[str, str, str]:
    return entry["surface"], entry["transport"], entry["endpoint"]


def write_markdown(path: Path, data: dict) -> None:
    rows = [
        "# RPC route inventory",
        "",
        f"> Generated from Core `{data['development_revision'][:8]}` and compared with release `{data['release_revision'][:8]}`.",
        "> Do not edit this table manually; run `tools/extract_rpc_inventory.py`.",
        "",
        "## Coverage summary",
        "",
        "| Surface | Development registrations | Release registrations | Unique development commands |",
        "| --- | ---: | ---: | ---: |",
    ]
    for surface in ("daemon", "wallet"):
        dev = [entry for entry in data["routes"] if entry["surface"] == surface]
        rel = [entry for entry in data["release_routes"] if entry["surface"] == surface]
        unique = len({entry["command"] for entry in dev})
        rows.append(f"| {surface.title()} | {len(dev)} | {len(rel)} | {unique} |")
    rows.extend([
        "",
        "Aliases share a command/handler contract; separate registrations are retained because clients can call each literal route.",
        "Wallet restricted-mode decisions are enforced by handlers, so the route map alone is recorded as `handler-dependent`.",
        "",
    ])
    release_keys = {key(entry) for entry in data["release_routes"]}
    for surface in ("daemon", "wallet"):
        rows.extend([
            f"## {surface.title()} registrations",
            "",
            "| Transport | Route/method | Command contract | Restricted listener | Release | Source/schema |",
            "| --- | --- | --- | --- | --- | --- |",
        ])
        for entry in (item for item in data["routes"] if item["surface"] == surface):
            release = "yes" if key(entry) in release_keys else "development only"
            schema = f" / [schema]({entry['schema_url']})" if entry["schema_url"] else ""
            rows.append(
                f"| {entry['transport']} | `{entry['endpoint']}` | `{entry['command']}` | "
                f"{entry['restricted_listener']} | {release} | [route]({entry['source_url']}){schema} |"
            )
        rows.append("")
    path.write_text("\n".join(rows) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--development-core", type=Path, required=True)
    parser.add_argument("--development-revision", required=True)
    parser.add_argument("--release-core", type=Path, required=True)
    parser.add_argument("--release-revision", required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()

    def all_routes(root: Path, revision: str) -> list[dict]:
        return extract(root / "src/rpc/core_rpc_server.h", "daemon", revision) + extract(
            root / "src/wallet/wallet_rpc_server.h", "wallet", revision
        )

    routes = all_routes(args.development_core, args.development_revision)
    release_routes = all_routes(args.release_core, args.release_revision)
    data = {
        "schema": 1,
        "development_revision": args.development_revision,
        "release_revision": args.release_revision,
        "routes": routes,
        "release_routes": release_routes,
    }
    args.output_directory.mkdir(parents=True, exist_ok=True)
    (args.output_directory / "rpc-inventory.json").write_text(json.dumps(data, indent=2) + "\n")
    write_markdown(args.output_directory / "RPC-Inventory.md", data)
    print(json.dumps({
        "development": len(routes),
        "release": len(release_routes),
        "development_daemon": sum(item["surface"] == "daemon" for item in routes),
        "development_wallet": sum(item["surface"] == "wallet" for item in routes),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

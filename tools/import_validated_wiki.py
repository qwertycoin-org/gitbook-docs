#!/usr/bin/env python3
"""Import the revision-bound current Wiki pages into the GitBook layout.

The GitHub Wiki remains the technical source snapshot for this migration. This
script maps only current pages, rewrites Wiki page links to relative GitBook
paths, and replaces obsolete GitBook entry points with short compatibility
notices. Git history remains the archive for the retired instructions.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path, PurePosixPath
from urllib.parse import unquote


PAGE_MAP = {
    "Getting-Started.md": "getting-started/simple-steps.md",
    "Downloads-and-Verification.md": "getting-started/downloads-and-verification.md",
    "FAQ.md": "getting-started/faq.md",
    "Glossary.md": "getting-started/terminology.md",
    "About-Qwertycoin.md": "project/about-qwertycoin.md",
    "Network-Parameters-and-Emission.md": "project/network-parameters-and-emission.md",
    "Privacy-Model.md": "project/privacy-model.md",
    "Legacy-Network-Compatibility.md": "project/legacy-network-compatibility.md",
    "Wallet-Overview.md": "wallet/types-of-wallet.md",
    "CLI-Wallet.md": "wallet/cli-wallet.md",
    "Desktop-GUI-Wallet.md": "wallet/gui-wallet.md",
    "Web-Wallet.md": "wallet/web-wallet.md",
    "Backup-and-Restore.md": "wallet/wallet-backup.md",
    "Updates.md": "wallet/wallet-update.md",
    "Message-Signing.md": "wallet/sign-and-verify-messages.md",
    "Run-a-Full-Node.md": "node/run-a-full-node.md",
    "Configuration-and-Ports.md": "node/config.md",
    "Docker.md": "node/docker.md",
    "Linux-Service-Operation.md": "node/linux-service-operation.md",
    "Upgrade-and-Recovery.md": "node/upgrade-and-recovery.md",
    "Synchronization-Troubleshooting.md": "node/fix-sync-issues.md",
    "Build-Overview.md": "developer/compiling-from-source/README.md",
    "Build-Linux.md": "developer/compiling-from-source/linux.md",
    "Build-macOS.md": "developer/compiling-from-source/macos.md",
    "Build-Windows.md": "developer/compiling-from-source/windows.md",
    "GUI-Build.md": "developer/compiling-from-source/gui.md",
    "Developer-Tests-and-Troubleshooting.md": "developer/compiling-from-source/tests-and-troubleshooting.md",
    "EPoSE-Overview.md": "epose/overview.md",
    "EPoSE-Service-Node-Quickstart.md": "epose/service-node-quickstart.md",
    "EPoSE-Configuration-and-Identity.md": "epose/configuration-and-identity.md",
    "EPoSE-Admission-and-Lifecycle.md": "epose/admission-and-lifecycle.md",
    "EPoSE-Epochs-and-Qualification.md": "epose/epochs-and-qualification.md",
    "EPoSE-Rewards.md": "epose/rewards.md",
    "EPoSE-Monitoring-and-Diagnostics.md": "epose/monitoring-and-diagnostics.md",
    "EPoSE-FAQ-and-Troubleshooting.md": "epose/faq-and-troubleshooting.md",
    "API-Overview.md": "api/overview.md",
    "Daemon-JSON-RPC.md": "api/daemon-json-rpc.md",
    "Daemon-HTTP-and-Binary-RPC.md": "api/daemon-http-and-binary-rpc.md",
    "Wallet-RPC-Setup.md": "api/wallet-rpc-setup.md",
    "Wallet-RPC-Reference.md": "api/wallet-rpc-reference.md",
    "EPoSE-RPC-Reference.md": "api/epose-rpc-reference.md",
    "RPC-Errors-and-Compatibility.md": "api/errors-and-compatibility.md",
    "Integration-Examples.md": "api/integration-examples.md",
    "RPC-Inventory.md": "api/rpc-inventory.md",
    "RandomX-Mining.md": "mining/mining-options.md",
    "Solo-Mining.md": "mining/solo-mining.md",
    "Pool-Mining.md": "mining/pool-mining.md",
    "Pool-Operator-Integration.md": "mining/creating-a-mining-pool.md",
    "Current-Explorer-and-Web-Wallet-Hosting.md": "ecosystem/current-hosting.md",
    "Exchanges-and-Network-Compatibility.md": "trading/exchanges.md",
    "Contributing.md": "contributing/contributing.md",
    "Qwertycoin-Community.md": "contributing/community.md",
    "Retired-Features-Index.md": "legacy/retired-features.md",
    "Source-Version-Matrix.md": "reports/source-version-matrix.md",
    "Discrepancy-Register.md": "reports/discrepancy-register.md",
    "Implementation-Defects.md": "reports/implementation-defects.md",
}

SUPPORT_MAP = {
    "rpc-inventory.json": "rpc-inventory.json",
    "tools/check_external_links.py": "tools/check_external_links.py",
    "tools/extract_rpc_inventory.py": "tools/extract_rpc_inventory.py",
}


MANUAL_MAP = {
    "Home": "README.md",
    "Migration-Manifest": "reports/migration-manifest.md",
    "Validation-Report": "reports/validation-report.md",
    "Documentation-Maintenance": "contributing/documentation-maintenance.md",
    "_Sidebar": "SUMMARY.md",
}


LEGACY_STUBS = {
    "wallet/paper-wallet.md": ("Paper wallet", "legacy/retired-features.md"),
    "wallet/zero-wallet.md": ("Zero wallet", "legacy/retired-features.md"),
    "wallet/mobile-wallet.md": ("Mobile wallet", "legacy/retired-features.md"),
    "wallet/using-rpc-wallet.md": ("Legacy RPC wallet", "api/wallet-rpc-setup.md"),
    "wallet/wallet-recovery.md": ("Wallet recovery", "wallet/wallet-backup.md"),
    "mining/cloud-mining.md": ("Cloud mining", "legacy/retired-features.md"),
    "mining/mining-with-sbc.md": ("SBC mining", "mining/mining-options.md"),
    "mining/mobile-mining.md": ("Mobile mining", "legacy/retired-features.md"),
    "mining/xmr-stak.md": ("XMR-Stak", "mining/mining-options.md"),
    "mining/xmr-stak-linux.md": ("XMR-Stak Linux", "mining/mining-options.md"),
    "mining/xmrig.md": ("Historical XMRig guide", "mining/pool-mining.md"),
    "mining/using-a-mining-pool.md": ("Historical pool-mining guide", "mining/pool-mining.md"),
    "node/load-checkpoints.md": ("Checkpoint import", "node/upgrade-and-recovery.md"),
    "node/start-masternode.md": ("Legacy masternode setup", "epose/service-node-quickstart.md"),
    "trading/how-to-trade-on-bisq.md": ("Historical Bisq guide", "trading/exchanges.md"),
    "trading/how-to-trade-on-crex24.md": ("Historical CREX24 guide", "trading/exchanges.md"),
    "developer/compiling-from-source/macos-qt-install.md": ("Historical macOS Qt workaround", "developer/compiling-from-source/macos.md"),
    "developer/compiling-from-source/untitled.md": ("Historical CMake installation", "developer/compiling-from-source/README.md"),
    "developer/forking-qwertycoin.md": ("Historical forking guide", "legacy/retired-features.md"),
    "developer/google-breakpad-integration.md": ("Historical Breakpad integration", "legacy/retired-features.md"),
    "developer/hosting-block-explorer.md": ("Historical explorer hosting", "ecosystem/current-hosting.md"),
    "developer/hosting-faucet.md": ("Historical faucet hosting", "legacy/retired-features.md"),
    "developer/hosting-web-wallet.md": ("Historical Web Wallet hosting", "ecosystem/current-hosting.md"),
    "developer/local-testnet.md": ("Historical local-testnet guide", "developer/compiling-from-source/tests-and-troubleshooting.md"),
    "developer/resources.md": ("Historical developer resources", "contributing/contributing.md"),
    "api/untitled-1.md": ("Historical daemon HTTP RPC", "api/daemon-http-and-binary-rpc.md"),
    "api/untitled-1-1.md": ("Historical daemon JSON-RPC", "api/daemon-json-rpc.md"),
    "api/untitled-2.md": ("Historical wallet RPC API", "api/wallet-rpc-reference.md"),
}


LINK = re.compile(r"(?<!!)\[([^]]+)]\(([^)]+)\)")


def link_index() -> dict[str, str]:
    index: dict[str, str] = dict(MANUAL_MAP)
    for source, target in PAGE_MAP.items():
        index[Path(source).stem] = target
        index[source] = target
    return index


def rewrite_links(text: str, destination: str) -> str:
    index = link_index()
    parent = PurePosixPath(destination).parent

    def replace(match: re.Match[str]) -> str:
        label, raw = match.groups()
        if "://" in raw or raw.startswith(("mailto:", "#")):
            return match.group(0)
        path, marker, fragment = raw.partition("#")
        decoded = unquote(path).removesuffix(".md")
        target = index.get(decoded) or index.get(PurePosixPath(decoded).name)
        if not target:
            return match.group(0)
        relative = os.path.relpath(target, str(parent) if str(parent) != "." else ".")
        suffix = f"#{fragment}" if marker else ""
        return f"[{label}]({relative}{suffix})"

    return LINK.sub(replace, text)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def import_pages(wiki: Path, root: Path) -> None:
    for source, destination in PAGE_MAP.items():
        source_path = wiki / source
        if not source_path.is_file():
            raise SystemExit(f"missing Wiki source: {source_path}")
        write(root / destination, rewrite_links(source_path.read_text(), destination))
    for source, destination in SUPPORT_MAP.items():
        source_path = wiki / source
        if not source_path.is_file():
            raise SystemExit(f"missing Wiki support source: {source_path}")
        write(root / destination, source_path.read_text())


def write_stubs(root: Path, baseline: str) -> None:
    for path, (title, destination) in LEGACY_STUBS.items():
        relative = os.path.relpath(destination, str(PurePosixPath(path).parent))
        write(
            root / path,
            f"# Historical page: {title}\n\n"
            "> **Compatibility notice:** This URL is retained so old links do not silently "
            "present obsolete Qwertycoin operations.\n\n"
            f"Use the [current replacement]({relative}).\n\n"
            f"The original content remains recoverable from Git commit `{baseline}`.\n",
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiki", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--baseline", default="151a593c09f7443f67bae982b10e1447e19797ca")
    args = parser.parse_args()
    import_pages(args.wiki.resolve(), args.root.resolve())
    write_stubs(args.root.resolve(), args.baseline)
    print(
        f"imported={len(PAGE_MAP)} support_files={len(SUPPORT_MAP)} "
        f"compatibility_stubs={len(LEGACY_STUBS)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

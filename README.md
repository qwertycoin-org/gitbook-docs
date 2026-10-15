---
description: Current, revision-bound Qwertycoin user, operator, integration, and contributor documentation.
---

# Qwertycoin documentation

> **Verified against:** the latest stable release; exact review revisions are recorded in [Source and version matrix](reports/source-version-matrix.md).

Qwertycoin is a privacy-focused proof-of-work network secured by RandomX. EPoSE is a separate service-reward protocol; it does not replace mining or chain selection.

## Choose a task

| I want to… | Start here |
| --- | --- |
| install a wallet and receive QWC | [Getting Started](getting-started/simple-steps.md) · [Wallet Overview](wallet/types-of-wallet.md) |
| verify a download | [Downloads and Verification](getting-started/downloads-and-verification.md) |
| run a full node | [Run a Full Node](node/run-a-full-node.md) · [Configuration and Ports](node/config.md) |
| run an EPoSE service node | [EPoSE Overview](epose/overview.md) · [Service Node Quickstart](epose/service-node-quickstart.md) |
| mine QWC | [RandomX Mining](mining/mining-options.md) · [Pool Mining](mining/pool-mining.md) |
| integrate daemon or wallet RPC | [API Overview](api/overview.md) · [Integration Examples](api/integration-examples.md) |
| build or contribute | [Build Overview](developer/compiling-from-source/README.md) · [Contributing](contributing/contributing.md) |

## Release policy

This documentation describes the latest published Qwertycoin release. Install or update to the latest release before following these instructions.

Here, **latest** means the newest official stable release published for the component and distribution channel being used. It does not mean the newest commit on a default branch or an arbitrary prerelease. Core, GUI, Docker and the Web Wallet have separate publication channels and must not be assumed to share a version number or publication time.

Use the official [Core latest release](https://github.com/qwertycoin-org/qwertycoin/releases/latest) and [GUI latest release](https://github.com/qwertycoin-org/qwertycoin-gui/releases/latest) pages for downloads. Exact revisions used for documentation review remain in the [Source and version matrix](reports/source-version-matrix.md); that evidence snapshot is not an instruction to install an older release.

Do not mix legacy-chain wallet files, addresses, mining software, ports, or service-node procedures with the current network. Start with [Legacy Network Compatibility](project/legacy-network-compatibility.md) when migrating from historical Qwertycoin software.

## Evidence and maintenance

- [Source/version matrix](reports/source-version-matrix.md)
- [Migration manifest](reports/migration-manifest.md)
- [Complete RPC inventory](api/rpc-inventory.md)
- [Validation report](reports/validation-report.md)
- [Implementation defects](reports/implementation-defects.md)
- [Documentation maintenance](contributing/documentation-maintenance.md)

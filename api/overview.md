# API overview

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

> **Published release:** latest stable Core and wallet RPC. The exact release and reviewed default-branch route maps are pinned in the [Source and version matrix](../reports/source-version-matrix.md).

Qwertycoin exposes separate interfaces:

| Interface | Process/path | Encoding | Trust boundary |
| --- | --- | --- | --- |
| Daemon path RPC | `qwertycoind` `/method` | JSON or portable binary archive | Restricted and unrestricted listeners differ per route |
| Daemon JSON-RPC | `qwertycoind` `/json_rpc` | JSON-RPC 2.0 | Route-level restrictions plus handler checks |
| Wallet RPC | `qwertycoin-wallet-rpc` `/json_rpc` | JSON-RPC 2.0 | Private, authenticated; holds wallet authority |
| EPoSE RPC | daemon path/JSON-RPC subset | JSON | Public probe subset vs private operator routes |
| ZMQ | `qwertycoind` `8199` example | ZMQ protocol | Not HTTP RPC; keep private unless separately engineered |
| C++ libraries | linked API | native ABI | Not a stable network contract |

The generated [RPC route inventory](rpc-inventory.md) accounts for every registration at both pinned revisions: 107 daemon and 96 wallet registrations on the latest stable release and reviewed development source. Aliases remain separate rows but share one command schema. Each row links the exact route and request/response definition.

All money amounts are unsigned integer **atomic units** (`10^8` per QWC) unless a schema explicitly says otherwise. Never use binary floating point for amounts.

Start with [Wallet RPC Setup](wallet-rpc-setup.md), then the [Wallet RPC Reference](wallet-rpc-reference.md) and [Integration Examples](integration-examples.md). Daemon users should distinguish [JSON-RPC](daemon-json-rpc.md) from [path/binary RPC](daemon-http-and-binary-rpc.md).

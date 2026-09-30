# Contributing

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Primary source:** current Core repository contribution and CI policy at `a71c0eb2`.

Open issues and pull requests in the repository that owns the contract:

- Core/consensus/RPC: [qwertycoin](https://github.com/qwertycoin-org/qwertycoin)
- Desktop: [qwertycoin-gui](https://github.com/qwertycoin-org/qwertycoin-gui)
- Web Wallet: [wallet.qwertycoin.org](https://github.com/qwertycoin-org/wallet.qwertycoin.org)
- Explorer: [explorer-qwertycoin-org.github.io](https://github.com/qwertycoin-org/explorer-qwertycoin-org.github.io)

Pin the issue to an exact revision and include reproducible steps, expected/actual result, environment and redacted logs. Never publish seeds, private keys, keystores, RPC credentials or funded test-wallet material.

Consensus changes require explicit protocol/security review, focused tests and release gates. RandomX remains responsible for block production and chain selection; EPoSE rewards service and must not silently replace PoW.

This Wiki is its own Git repository. Wiki edits should refresh [Source Version Matrix](../reports/source-version-matrix.md), route inventory where relevant, migration/link/stale-content checks and visible verification headers.


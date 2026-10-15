# Contributing

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

> **Primary source:** current repository contribution and CI policies; exact reviewed revisions are recorded in the [Source and version matrix](../reports/source-version-matrix.md).

Open issues and pull requests in the repository that owns the contract:

- Core/consensus/RPC: [qwertycoin](https://github.com/qwertycoin-org/qwertycoin)
- Desktop: [qwertycoin-gui](https://github.com/qwertycoin-org/qwertycoin-gui)
- Web Wallet: [wallet.qwertycoin.org](https://github.com/qwertycoin-org/wallet.qwertycoin.org)
- Explorer: [explorer-qwertycoin-org.github.io](https://github.com/qwertycoin-org/explorer-qwertycoin-org.github.io)

Pin the issue to an exact revision and include reproducible steps, expected/actual result, environment and redacted logs. Never publish seeds, private keys, keystores, RPC credentials or funded test-wallet material.

Consensus changes require explicit protocol/security review, focused tests and release gates. RandomX remains responsible for block production and chain selection; EPoSE rewards service and must not silently replace PoW.

This documentation is maintained in its own Git repository. Changes should refresh the [Source and version matrix](../reports/source-version-matrix.md), route inventory where relevant, migration/link/stale-content checks and visible verification headers.

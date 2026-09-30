# Legacy network compatibility

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

The current Qwertycoin network is not a continuation of the historical chain.

Do not reuse:

- old blockchain databases or daemon data directories;
- old peer-state files or checkpoints;
- old wallet cache files as if they represented current transactions;
- `simplewallet`, `walletd`, old container-wallet APIs, or port 8070 guides;
- CryptoNight/XMR-Stak mining configuration;
- legacy masternode registration transactions or `--service-node*` flags.

Current binaries are `qwertycoind`, `qwertycoin-wallet-cli`, and `qwertycoin-wallet-rpc`. Current proof of work is RandomX. Current EPoSE enrollment is automatic and identity/epoch-bound.

Old mnemonic/key material may be imported only as a key-recovery experiment. A successful import does not transfer or recreate balances from the legacy chain. Use a new current-network wallet for normal operation and verify addresses with current software.

See [Retired Features](../legacy/retired-features.md) for old wiki entry points.

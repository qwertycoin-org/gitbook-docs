# Upgrade and recovery

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Published-release track:** Core `v2.0.2`.

1. Record the running binary version, source/digest, arguments, binds and data paths.
2. Back up wallet material separately from blockchain data and EPoSe identity.
3. Download and verify the new immutable artifact.
4. Stop cleanly; never replace a running executable or treat a live LMDB copy as consistent.
5. Install side by side, update the service path, start, and verify version, network, height and peers.
6. Preserve the old binary/configuration for rollback until the new process is proven.

An EPoSe upgrade must preserve the service keystore. Deleting it creates a new identity and can disrupt admission, qualification and rewards. Never use keystore deletion as a permissions repair.

Blockchain data can be resynchronized. Wallet seeds/spend keys and EPoSe identity cannot. If LMDB is damaged, stop the process and resynchronize into a clean directory rather than mixing databases.

The historical CSV-checkpoint guide is retired. Use current synchronization and database tooling, not stale checkpoint files from another chain era.


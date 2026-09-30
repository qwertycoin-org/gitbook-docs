# Wallet and node updates

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

1. Read release notes and verify network/data-format compatibility.
2. Download from the official release and verify `SHA256SUMS`.
3. Stop wallet and daemon cleanly.
4. Back up wallet seed/files and EPoSE identity separately.
5. Replace binaries or recreate containers without deleting persistent data.
6. Start the daemon, verify version/height/peers, then open the wallet.
7. For EPoSE, verify the same identity/service public keys and endpoint after restart.

An image pull does not update a running container. Recreate it explicitly. Roll back only if the older binary supports current on-disk formats and consensus state.

Never overwrite or remove wallet files, EPoSE identity volumes, or seeds as part of a routine update.

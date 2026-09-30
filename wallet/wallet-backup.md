# Backup and restore

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

## Back up separately

| Data | Reconstructable? | Backup guidance |
| --- | --- | --- |
| Wallet mnemonic seed / spend keys | No | Offline, redundant, access-controlled |
| Wallet file | Not safely without seed/keys | Back up encrypted file and verify password |
| Wallet cache | Yes, by rescan | Optional convenience backup |
| Blockchain data | Yes, by resync | Optional; large and replaceable |
| EPoSE keystore | No without creating a new identity | Separate protected backup; never store with public configs |

## Restore a wallet

1. Install a verified current release.
2. Restore from seed or supported private keys.
3. Select current mainnet.
4. Set a restore height at or before the first expected transaction.
5. Let the wallet scan to the current daemon height.
6. Verify receive address, history, unlocked balance, and a small test transaction.

Restoring old Qwertycoin key material does not restore balances from the legacy chain.

## File permissions

Wallet and backup files should be readable only by the owning account. Do not solve permission errors with world-readable modes. Never delete an EPoSE keystore as a permissions workaround; see [EPoSE Configuration and Identity](../epose/configuration-and-identity.md).

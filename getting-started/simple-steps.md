# Getting started

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Published-release track:** Core and GUI `v2.0.2`. Verified 2026-09-29 UTC.

## 1. Choose a wallet

- **Desktop GUI:** easiest full wallet; downloads and verifies chain data through a local or selected daemon. See [Desktop GUI Wallet](../wallet/gui-wallet.md).
- **CLI wallet:** operator/developer interface included in the Core archive. See [CLI Wallet](../wallet/cli-wallet.md).
- **Web Wallet:** current browser client at <https://wallet.qwertycoin.org/>. See [Web Wallet](../wallet/web-wallet.md) for its trust and backup model.
- **Wallet RPC:** integration service, not a consumer wallet. Keep it private and authenticated. See [Wallet RPC Setup](../api/wallet-rpc-setup.md).

There is no supported paper-wallet generator, Zero wallet, or current native mobile-wallet release in this documentation.

## 2. Download and verify

Download only from the official [Core](https://github.com/qwertycoin-org/qwertycoin/releases/tag/v2.0.2) or [GUI](https://github.com/qwertycoin-org/qwertycoin-gui/releases/tag/v2.0.2) release. Verify the archive against the release `SHA256SUMS` file before extracting it. Checksums detect corruption or substitution relative to that file; they are not publisher signatures.

See [Downloads and Verification](downloads-and-verification.md).

## 3. Create and protect the wallet

1. Create a new wallet in GUI or `qwertycoin-wallet-cli`.
2. Record the mnemonic seed offline. Never paste it into a website, support chat, issue, or log.
3. Use a strong wallet password; it encrypts the wallet file but cannot repair a lost seed.
4. Record an appropriate restore height near the creation block/date.
5. Receive a small test amount and verify the address before using larger amounts.

Primary addresses normally begin `QWC…`; current mainnet subaddresses use a different encoded prefix and commonly begin `Qqb…`. Validate addresses with current software rather than checking only visible characters.

## 4. Wait for synchronization and unlock

A wallet can show an incoming transaction before it is confirmed or spendable. The daemon and wallet heights must catch up. Coinbase/mining/service-reward outputs use the compiled Coinbase maturity rule; normal transfers use their transaction unlock rules.

## 5. Next steps

- [Backup and Restore](../wallet/wallet-backup.md)
- [Updates](../wallet/wallet-update.md)
- [Run a Full Node](../node/run-a-full-node.md)
- [Privacy Model](../project/privacy-model.md)

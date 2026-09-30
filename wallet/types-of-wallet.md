# Wallet overview

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Published-release track:** Core/GUI `v2.0.2`.

| Wallet | Best for | Important boundary |
| --- | --- | --- |
| Desktop GUI | Everyday desktop use | Verify the exact official package; preserve seed and wallet files. |
| CLI | Operators and advanced users | Commands act on the currently opened wallet. |
| Web Wallet | Browser use | Trust and backup model differs from native wallets; use only the official origin. |
| Wallet RPC | Exchange/service integration | Holds wallet authority; keep private, authenticated, and serialized. |

Current mainnet supports primary addresses, subaddresses, and integrated addresses. Generate addresses with current wallet software. A subaddress can legitimately have a visible prefix different from `QWC`; `validate_address` is authoritative for format/network/type.

## Wallet data

- **Mnemonic seed/private spend key:** controls funds; protect offline.
- **Wallet file:** encrypted key material and configuration.
- **Wallet cache:** transaction state that can be rebuilt by rescanning.
- **Daemon blockchain:** node data, not wallet backup.
- **EPoSE keystore:** separate service identity; never place it in a wallet directory.

Never open the same wallet file concurrently in CLI and wallet RPC.

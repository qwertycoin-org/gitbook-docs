# Desktop GUI wallet

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Published release:** GUI `v2.0.2` (`c5eced2…`), pinned Core `54308d847…`.

Official packages are listed in [Downloads and Verification](../getting-started/downloads-and-verification.md). GUI `v2.0.2` publishes Linux x86_64, Windows x86_64 installer/portable ZIP, and macOS arm64 DMG/portable archive.

## First run

1. Verify the package checksum.
2. Create a wallet and record the seed offline, or restore from current-network seed/key material.
3. Choose a local node for strongest availability/privacy or a trusted remote node with understood metadata tradeoffs.
4. Wait until daemon and wallet synchronization complete before judging balances.
5. Receive a small test transaction before moving larger values.

The macOS DMG is a packaging format, not proof of Apple notarization. At the verified release baseline, users must not infer code-signing/notarization status from the `.dmg` extension alone.

The GUI Core submodule pin is part of release provenance. A development GUI built against another Core commit must identify both SHAs.

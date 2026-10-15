# Desktop GUI wallet

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

Official packages are listed on the [GUI latest release](https://github.com/qwertycoin-org/qwertycoin-gui/releases/latest) page and explained in [Downloads and Verification](../getting-started/downloads-and-verification.md). The current stable channel publishes Linux x86_64, Windows x86_64 installer/portable ZIP, and macOS arm64 DMG/portable archive.

## First run

1. Verify the package checksum.
2. Create a wallet and record the seed offline, or restore from current-network seed/key material.
3. Choose a local node for strongest availability/privacy or a trusted remote node with understood metadata tradeoffs.
4. Wait until daemon and wallet synchronization complete before judging balances.
5. Receive a small test transaction before moving larger values.

The macOS DMG is a packaging format, not proof of Apple notarization. Read the current release notes and do not infer code-signing/notarization status from the `.dmg` extension alone.

The GUI Core submodule pin is part of release provenance. A development GUI built against another Core commit must identify both SHAs.

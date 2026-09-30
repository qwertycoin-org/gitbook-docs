# Current Explorer and Web Wallet hosting

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Repositories verified:** Explorer production source and Web Wallet `05f81c0c`, 2026-09-29.

## Explorer

Use the maintained [Qwertycoin Explorer](https://github.com/qwertycoin-org/explorer-qwertycoin-org.github.io), not the legacy installation page. The public explorer is an observer, not a consensus authority. It uses a read-only chain mount plus a verified restricted daemon dependency, runs unprivileged, and deliberately removes inherited secret-processing routes.

Production requires immutable image/Core revisions, explicit paths/UID/GID/network bindings, loopback application ports, separate derived-data storage, and the repository runbook's preview/rollback gates. Never paste wallet view/spend keys into an explorer.

## Web Wallet

Use the maintained [Web Wallet repository](https://github.com/qwertycoin-org/wallet.qwertycoin.org). Pin its WebAssembly/worker artifacts and deployment revision, apply its security headers and validate production Explorer compatibility. Browser storage contains wallet authority and must not be treated as a server backup.

The open QMS/Messenger pull request is unreleased at this verification point. Do not advertise it as production functionality until merged, deployed and release-validated.

Historical generic web-wallet/explorer hosting recipes are retirement stubs because their dependencies and secret-processing assumptions are incompatible with the current hardened deployments.


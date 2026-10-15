# Current Explorer and Web Wallet hosting

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

> **Repositories verified:** current Explorer production source and deployed Web Wallet; exact reviewed revisions are recorded in the [Source and version matrix](../reports/source-version-matrix.md).

## Explorer

Use the maintained [Qwertycoin Explorer](https://github.com/qwertycoin-org/explorer-qwertycoin-org.github.io), not the legacy installation page. The public explorer is an observer, not a consensus authority. It uses a read-only chain mount plus a verified restricted daemon dependency, runs unprivileged, and deliberately removes inherited secret-processing routes.

Production requires immutable image/Core revisions, explicit paths/UID/GID/network bindings, loopback application ports, separate derived-data storage, and the repository runbook's preview/rollback gates. Never paste wallet view/spend keys into an explorer.

## Web Wallet

Use the maintained [Web Wallet repository](https://github.com/qwertycoin-org/wallet.qwertycoin.org). Pin its WebAssembly/worker artifacts and deployment revision, apply its security headers and validate production Explorer compatibility. Browser storage contains wallet authority and must not be treated as a server backup.

The current official Web Wallet includes the password-gated QMS1 Fast Profile. Treat Web Wallet deployment evidence separately from Core and GUI release numbers.

Historical generic web-wallet/explorer hosting recipes are retirement stubs because their dependencies and secret-processing assumptions are incompatible with the current hardened deployments.

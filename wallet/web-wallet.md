# Web Wallet

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

> **Released behavior:** current deployment at <https://wallet.qwertycoin.org/>; the exact reviewed deployment revision is recorded in the [Source and version matrix](../reports/source-version-matrix.md).

Use only <https://wallet.qwertycoin.org/> and verify the origin before entering any secret. The Web Wallet runs wallet logic in the browser and reaches Qwertycoin data through its deployed gateway. Browser storage, local malware, extensions, phishing, and the selected network path remain part of the threat model.

Back up the seed/key material shown by the released wallet. Clearing browser data can remove local application state. A seed is not a backup of every unrelated browser-only feature.

## Messenger status

QMS1/Fast Messenger work exists in open PR #14. It is **unreleased** at this wiki baseline and must not be described as current production functionality. Its separate Messenger identity/history requires its own encrypted backup model.

## Remote-service limits

End-to-end wallet cryptography does not hide IP address, request timing, or all query metadata from the browser network path. Prefer native wallet software with a local daemon for stronger control.

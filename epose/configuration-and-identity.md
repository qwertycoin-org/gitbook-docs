# EPoSE configuration and identity

> **Verified against:** Core `v2.0.2` and development `a71c0eb2`, Qwertycoin mainnet, 2026-09-29.

| Object | Role | Sensitivity/persistence |
| --- | --- | --- |
| Operator identity | Stable service identity and lifecycle authority | Private; back up; preserve across upgrades |
| Online service key | Signs endpoint/service responses; may rotate under lifecycle rules | Private; managed in the keystore |
| Endpoint descriptor | Signed public host/port and commitments | Public; sequence/activation are consensus-bound |
| Reward address | Primary public QWC destination | Public only; no wallet secret is needed |
| Admission lease | Epoch-bound RandomX proof and lifecycle binding | Public canonical record |

The keystore is bound to network, genesis and EPoSE parameters. It is not a wallet and contains no wallet view/spend key. Store it on a protected persistent volume separate from blockchain and wallet data.

On Linux/macOS the file must be regular, non-symlink and mode `0600`. On Windows current builds validate owner/DACL, reject inherited/unrelated access and provide `--epose-v2-repair-keystore-permissions` for a one-start repair of an older file. Back up first, verify unchanged public keys afterward, and remove the flag. Never delete the keystore as a permissions fix.

Endpoint/reward/key changes must use supported lifecycle records and activation rules. The daemon rejects unexpected changes rather than silently redirecting rewards. A backup restores an existing identity; intentionally deleting it creates a new identity that must repeat lifecycle/admission.

# Source and version matrix

> **Verified:** 2026-09-30 05:22 UTC. Network: Qwertycoin mainnet unless stated otherwise.

This page fixes the evidence baseline used for the 2026 GitBook documentation overhaul. Commands and contracts elsewhere in this documentation identify whether they target the published release or development source.

| Component | Published/current revision | Role in this documentation |
| --- | --- | --- |
| GitBook repository before overhaul | `151a593c09f7443f67bae982b10e1447e19797ca`, tree `bed2eb3cdd497a3a670bd833f66da78465502964`, on `master` | Recoverable 60-file pre-change snapshot; `docs.qwertycoin.org` still served this stale content before reconnection |
| Validated GitHub Wiki source | `b4e1f81638a410e13c8a3fff3897d53fc436a424`; technical content commit `46742a250935fa62496ee97d289cd128df210641` | Revision-bound source imported and adapted to GitBook paths; it is not used as a live Git Sync source |
| Core development source | `a71c0eb2c5b5675f9664fde5738e9cd9ba2e1eac` on `main` | Current source contracts, including EPoSE receipt diagnostics |
| Core published release | `v2.0.2`, source `54308d8473dc5606d054c0ba428cfb2d64e758c1` | Default installation and operator track |
| GUI development source | `ecd1844f1b2e3416dec16c07a21e6850e11b630c` on `master` | Current GUI source |
| GUI published release | `v2.0.2`, source `c5eced2f5c1ae5cba04178a276460ffb2a77f459`, Core submodule `54308d8473dc5606d054c0ba428cfb2d64e758c1` | Default desktop-wallet track |
| Web Wallet published branch | `05f81c0ce9ecfe11da0f52491bb9e26e724723f6` on `master` | Current released Web Wallet behavior |
| Web Messenger preview | PR #14, head observed as `37d686d503c916004f684abcaf7cdc240fe69132` | Unreleased; never described as a released Web Wallet feature |

## Version policy

- **Published release** instructions work with Core or GUI `v2.0.2` unless a page says otherwise.
- **Development source** instructions name the exact minimum commit. Development-only methods are marked beside the method.
- `get_epose_diagnostics` is present at Core `a71c0eb2…` and absent from Core `v2.0.2`; release operators must not expect it.
- Open pull requests and historical source files are not runtime evidence.

## Authority order

1. Reachable implementation and route registration at the pinned revision.
2. Tests and reproducible observations for that revision and network.
3. Release metadata, packaged version/help output, manifests, and CI evidence.
4. Maintained repository documentation checked against the first three items.
5. Historical Wiki/GitBook pages, websites, and community material.

See [Validation Report](validation-report.md) and [Discrepancy Register](discrepancy-register.md).

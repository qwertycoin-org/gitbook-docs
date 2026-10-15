# Source and version matrix

> **Evidence snapshot:** 2026-10-15 UTC. Network: Qwertycoin mainnet unless stated otherwise. Exact versions on this page are review evidence, not installation pins for current user guides.

This page fixes the evidence baseline used to review the latest-first documentation. Current installation and operator guides resolve the latest stable release from each component's official publication channel; they do not copy these versions into normal instructions.

| Component | Published/current revision | Role in this documentation |
| --- | --- | --- |
| GitBook latest-first base | `1d453bcf7f3611ba1ebc3f185782c3e76522ed5d` on `master` | Reviewed base for the latest-first update; the pre-overhaul baseline remains in the migration manifest |
| Validated GitHub Wiki source | `b4e1f81638a410e13c8a3fff3897d53fc436a424`; technical content commit `46742a250935fa62496ee97d289cd128df210641` | Revision-bound source imported and adapted to GitBook paths; it is not used as a live Git Sync source |
| Core reviewed development source | `b88bb3781f20e1a0d1427fd6abf41aaac3b8ac5f` on `main` | Development comparison only; not the default installation track |
| Core latest stable release at snapshot | `v2.0.3`, source `766839bb49475200977f6302b60c01e34d66e253` | Exact release used to validate current Core, EPoSE and RPC instructions |
| GUI reviewed development source | `5bea119b72d7b0ef68579e95407dbfbe0677da31` on `master` | Development comparison only; equal to the current release source at this snapshot |
| GUI latest stable release at snapshot | `v2.0.3`, source `5bea119b72d7b0ef68579e95407dbfbe0677da31`, Core submodule `766839bb49475200977f6302b60c01e34d66e253` | Exact release used to validate current desktop-wallet instructions |
| Docker latest channel at snapshot | `docker.io/qwertycoin/qwertycoin:latest`, `linux/amd64`, digest `sha256:e7120074680685a748d491bede60baef9a716c023b9d3c43efbc6e55f037abc6` | Same digest as the release-specific `2.0.3` tag at verification time; consumers should pin the digest after resolving `latest` |
| Web Wallet published branch | `7852740e8e301037aedf9cdc58d7c74150c45e90` on `master` | Current deployed browser-wallet behavior; QMS1 Fast Profile is merged, not a Core/GUI release feature |

## Version policy

- **Current instructions** target the newest official stable release for the named component/channel at the time of use. Core, GUI, Docker and Web Wallet channels are resolved independently.
- **Evidence snapshots** retain exact releases, commits and digests so a review can be reproduced; they do not freeze normal user instructions to that snapshot.
- **Development source** behavior is excluded from the regular user path unless a page explicitly labels it and gives an exact minimum commit.
- `get_epose_diagnostics` is present in both reviewed Core revisions in this snapshot and remains unrestricted/authenticated.
- Open pull requests and historical source files are not runtime evidence.

## Authority order

1. Reachable implementation and route registration at the pinned revision.
2. Tests and reproducible observations for that revision and network.
3. Release metadata, packaged version/help output, manifests, and CI evidence.
4. Maintained repository documentation checked against the first three items.
5. Historical Wiki/GitBook pages, websites, and community material.

See [Validation Report](validation-report.md) and [Discrepancy Register](discrepancy-register.md).

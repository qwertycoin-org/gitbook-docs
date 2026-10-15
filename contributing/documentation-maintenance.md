# Documentation maintenance

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

The `qwertycoin-org/gitbook-docs` Git repository is the reviewed source of truth. Git Sync must use `master`, repository root `./`, and **GitHub → GitBook** for the initial direction. Never import stale GitBook content over a reviewed repository tree.

## Latest-first convention

Current documentation describes the latest published stable release for the component and distribution channel being used. Do not hard-code a Qwertycoin Core, GUI or Docker release number in titles, introductions, prerequisites, installation steps, download labels or normal command examples. Link to the official latest-release page and keep artifacts plus `SHA256SUMS` bound to the same selected release.

Core, GUI, Docker and Web Wallet publication channels are independent. `latest` never means the newest default-branch commit or an arbitrary prerelease. Exact versions, commits and digests belong in clearly identified evidence snapshots, historical release notes, migration/security records or reproducible internal checks—not in the normal user path.

Do not remove API/protocol versions, hardfork identifiers, block heights, dependency versions, minimum operating-system versions or other technical constants merely because they look version-like. Historical records stay exact and must be visibly separated from current instructions.

## Release checklist

For every Core, GUI, Web Wallet, Explorer, or documentation release:

- record exact Core default-branch and release source SHAs;
- review changed CLI flags, defaults, bind addresses, and authentication;
- regenerate and review the daemon/wallet route diff with `tools/extract_rpc_inventory.py`;
- verify network, emission, maturity, and EPoSE parameter manifests/tests;
- compare dependency/toolchain and supported-platform workflows;
- verify release assets, checksums, signatures/notarization statements, and Docker digests;
- verify the GUI Core gitlink and Web Wallet/Explorer compatibility revisions;
- review changed behavior, parameters, prerequisites, screenshots and platform claims instead of assuming version-neutral prose remains correct;
- confirm current guides contain no fixed Qwertycoin release tags, versioned Qwertycoin asset links or numeric Docker release tags;
- check external project links and current exchange/mining compatibility;
- update page evidence headers and development-only labels.

## Required checks

```bash
python3 tools/generate_migration_manifest.py
python3 tools/validate_docs.py
```

`tools/validate_docs.py` enforces the latest-first convention only for current documentation. Reports and explicitly historical pages are excluded so exact audit evidence remains reproducible.

Regenerate the RPC inventory from the pinned development and release Core trees and require a clean diff or review every contract change. Render every page with a GitHub-Flavored Markdown-compatible renderer and run the external-link checker before merge.

`tools/import_validated_wiki.py` is the auditable one-time migration helper used for this overhaul. It must not be run as routine release maintenance: GitBook content is reviewed and maintained in this repository after migration. If a future full resynchronization from another documentation source is intentionally approved, run it on an isolated branch and review the complete diff.

## Safe publication

1. Work on a feature branch and open a reviewable pull request.
2. Confirm `gitbook-docs.yaml` defines exactly one default space with `content.directory: ./`.
3. Fetch `master` immediately before merge; do not force-push or rewrite shared history.
4. Confirm GitBook reports the repository-root connector synchronized.
5. Independently fetch `https://docs.qwertycoin.org/`, its sitemap, and representative new and compatibility pages.
6. Record the before/after Git SHAs and public verification time in the [Validation Report](../reports/validation-report.md).

Git Sync connected is not the same as content published. Keep DNS/custom-domain configuration unchanged unless it is independently proven wrong. Never commit GitHub or GitBook credentials.

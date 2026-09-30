# Downloads and verification

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Verified:** Core/GUI `v2.0.2`, 2026-09-29 UTC.

## Published artifacts

Core `v2.0.2` publishes:

- Linux x86_64 archive
- macOS arm64 archive
- Windows x86_64 ZIP
- `SHA256SUMS`

GUI `v2.0.2` publishes:

- Linux x86_64 archive
- macOS arm64 DMG and portable archive
- Windows x86_64 installer and portable ZIP
- `SHA256SUMS`

No Intel macOS or Linux arm64 artifact was published for these releases. Do not infer support from upstream Monero packages.

## Verify a downloaded file

Download the artifact and `SHA256SUMS` into an empty directory, then run:

```bash
sha256sum --check SHA256SUMS --ignore-missing
```

On macOS:

```bash
shasum -a 256 -c SHA256SUMS
```

On Windows PowerShell, compare:

```powershell
Get-FileHash .\qwertycoin-v2.0.2-windows-x86_64.zip -Algorithm SHA256
Get-Content .\SHA256SUMS
```

The filename and full digest must match. A checksum verifies integrity relative to the downloaded checksum list; the current release does not publish a separate cryptographic signature for that list.

## Verify executables

After extraction:

```bash
./qwertycoind --version
./qwertycoin-wallet-cli --version
./qwertycoin-wallet-rpc --version
```

Expected release text identifies `v2.0.2-release`. Do not mix programs from different archives in one deployment.

## Docker provenance

The official image is `docker.io/qwertycoin/qwertycoin`. It packages the verified Linux release archive; it does not rebuild Core. Production deployments should resolve and pin an image digest:

```bash
docker pull docker.io/qwertycoin/qwertycoin:2.0.2
docker image inspect docker.io/qwertycoin/qwertycoin:2.0.2 --format '{{index .RepoDigests 0}}'
```

Use the immutable digest in deployment configuration after checking the OCI labels described in [Docker](../node/docker.md).

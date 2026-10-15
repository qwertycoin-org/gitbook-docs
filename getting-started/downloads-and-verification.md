# Downloads and verification

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

## Published artifacts

Open the official [Core latest release](https://github.com/qwertycoin-org/qwertycoin/releases/latest) or [GUI latest release](https://github.com/qwertycoin-org/qwertycoin-gui/releases/latest) page. Select the asset for your platform and download that release's `SHA256SUMS` from the same page. Qwertycoin asset filenames contain the release version, so this documentation does not invent moving `releases/latest/download/...` URLs for them.

The current Core release channel publishes:

- Linux x86_64 archive
- macOS arm64 archive
- Windows x86_64 ZIP
- `SHA256SUMS`

The current GUI release channel publishes:

- Linux x86_64 archive
- macOS arm64 DMG and portable archive
- Windows x86_64 installer and portable ZIP
- `SHA256SUMS`

Intel macOS and Linux arm64 packages are not currently published on these channels. Confirm the asset list on the release page; do not infer support from upstream Monero packages.

## Verify a downloaded file

Download the artifact and `SHA256SUMS` into an empty directory, then run:

```bash
sha256sum --check SHA256SUMS --ignore-missing
```

On macOS:

```bash
shasum -a 256 -c SHA256SUMS
```

On Windows PowerShell, enter the exact downloaded archive path and compare:

```powershell
$archive = Read-Host "Downloaded archive path"
Get-FileHash -LiteralPath $archive -Algorithm SHA256
Get-Content .\SHA256SUMS
```

The filename and full digest must match. A checksum verifies integrity relative to the downloaded checksum list; it does not prove publisher identity unless the release also provides a separately verifiable signature for that exact list. Check the current release notes for signing status.

## Verify executables

After extraction:

```bash
./qwertycoind --version
./qwertycoin-wallet-cli --version
./qwertycoin-wallet-rpc --version
```

The reported release must match the tag shown on the release page used for the download. Do not mix programs from different archives in one deployment.

## Docker provenance

The official image is `docker.io/qwertycoin/qwertycoin`. It packages the verified Linux release archive; it does not rebuild Core. The `latest` tag is moving and currently follows the Docker publication channel's latest stable release. Pull it, resolve its immutable digest, and pin that digest in production:

```bash
docker pull docker.io/qwertycoin/qwertycoin:latest
docker image inspect docker.io/qwertycoin/qwertycoin:latest --format '{{index .RepoDigests 0}}'
```

Pulling a tag does not replace or restart an existing container. Use the immutable digest in deployment configuration after checking the OCI labels and follow the state-preserving recreation procedure in [Docker](../node/docker.md).

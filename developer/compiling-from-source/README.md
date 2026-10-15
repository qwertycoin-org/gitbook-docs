# Build overview

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../../reports/source-version-matrix.md).

> **Source track:** latest stable Core release. Default-branch builds are development builds and must be identified by their exact commit.

Open the [Core latest release](https://github.com/qwertycoin-org/qwertycoin/releases/latest), copy its stable tag, then select that explicit tag and initialize recursive submodules. Do not substitute the default branch for a published release:

```bash
read -r -p "Latest stable Core release tag: " QWC_RELEASE_TAG
[[ "$QWC_RELEASE_TAG" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]] || {
  echo "invalid stable release tag" >&2
  exit 1
}
git clone --recursive https://github.com/qwertycoin-org/qwertycoin.git
cd qwertycoin
git checkout --detach "$QWC_RELEASE_TAG"
git submodule sync --recursive
git submodule update --init --recursive
```

| Platform | Release CI environment | Architecture | Link model |
| --- | --- | --- | --- |
| Linux | Ubuntu 22.04, GCC 11 | x86_64 | dynamic system libraries |
| macOS | macOS 15 | arm64 | dynamic Homebrew libraries |
| Windows | Windows 2025, MSYS2 MinGW64 | x86_64 | packaged MinGW runtime |

Use conservative parallelism on small hosts. Release CI deliberately uses two compile jobs and one link job.

- [Build Linux](linux.md)
- [Build macOS](macos.md)
- [Build Windows](windows.md)
- [GUI Build](gui.md)
- [Developer Tests and Troubleshooting](tests-and-troubleshooting.md)

Expected outputs are `qwertycoind`, `qwertycoin-wallet-cli`, and `qwertycoin-wallet-rpc`. The internal CMake target `simplewallet` produces the QWC-named CLI; do not carry its historical target name into user instructions.

# Build overview

> **Verified against:** [Pinned source and release revisions](../../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Source tracks:** release `v2.0.2` (`54308d84`) and development `a71c0eb2`.

Select an explicit tag or 40-character commit and initialize recursive submodules:

```bash
git clone --recursive https://github.com/qwertycoin-org/qwertycoin.git
cd qwertycoin
git checkout v2.0.2
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


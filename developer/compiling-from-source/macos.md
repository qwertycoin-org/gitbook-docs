# Build on macOS

> **Verified against:** [Pinned source and release revisions](../../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Validated recipe source:** Core `v2.0.2` release workflow, macOS 15 arm64. The released package is ad-hoc signed, not Developer ID signed or notarized.

```bash
xcode-select --install
brew install cmake ninja boost hidapi openssl@3 zeromq libpgm unbound \
  libunwind-headers protobuf ccache libsodium libgcrypt libgpg-error expat

cmake -S source -B build/macos -G Ninja \
  -DCMAKE_BUILD_TYPE=Release -DARCH=armv8-a -DBUILD_64=ON -DSTATIC=OFF \
  -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTS=OFF -DBUILD_DOCUMENTATION=OFF \
  -DBUILD_DEBUG_UTILITIES=OFF -DUSE_DEVICE_TREZOR=OFF -DUSE_READLINE=OFF \
  -DBUILD_TAG=mac-armv8 -DMANUAL_SUBMODULES=1 \
  -DCMAKE_OSX_ARCHITECTURES=arm64 -DCMAKE_OSX_DEPLOYMENT_TARGET=15.0 \
  -DOPENSSL_ROOT_DIR="$(brew --prefix openssl@3)" \
  -DMONERO_PARALLEL_COMPILE_JOBS=2 -DMONERO_PARALLEL_LINK_JOBS=1

cmake --build build/macos --target daemon simplewallet wallet_rpc_server --parallel 2
```

Run this after an explicit `v2.0.2` checkout and recursive submodule initialization. Intel macOS is not claimed as release-validated by this track. The historical Qt workaround is retired; use [GUI Build](gui.md) for GUI dependencies.


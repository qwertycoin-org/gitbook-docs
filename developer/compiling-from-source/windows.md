# Build on Windows

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../../reports/source-version-matrix.md).

> **Validated recipe source:** latest stable Core release workflow, Windows 2025 x86_64 with MSYS2 MinGW64. Check the current release notes for signing status.

From an MSYS2 **MINGW64** shell:

```bash
pacman -S --needed git zip base-devel \
  mingw-w64-x86_64-toolchain mingw-w64-x86_64-cmake mingw-w64-x86_64-ninja \
  mingw-w64-x86_64-ccache mingw-w64-x86_64-python mingw-w64-x86_64-boost \
  mingw-w64-x86_64-openssl mingw-w64-x86_64-libgcrypt mingw-w64-x86_64-libgpg-error \
  mingw-w64-x86_64-zeromq mingw-w64-x86_64-libsodium mingw-w64-x86_64-unbound \
  mingw-w64-x86_64-expat mingw-w64-x86_64-hidapi mingw-w64-x86_64-libusb \
  mingw-w64-x86_64-protobuf

cmake -S source -B build/windows -G Ninja \
  -DCMAKE_BUILD_TYPE=Release -DARCH=default -DBUILD_64=ON -DSTATIC=OFF \
  -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTS=OFF -DBUILD_DOCUMENTATION=OFF \
  -DBUILD_DEBUG_UTILITIES=OFF -DUSE_DEVICE_TREZOR=OFF -DUSE_READLINE=OFF \
  -DBUILD_TAG=win-x64 -DMANUAL_SUBMODULES=1 \
  -DMONERO_PARALLEL_COMPILE_JOBS=2 -DMONERO_PARALLEL_LINK_JOBS=1

cmake --build build/windows --target daemon simplewallet wallet_rpc_server --parallel 2
```

Run after the explicit latest stable release-tag checkout with recursive submodules described in [Build Overview](README.md). Use the runtime DLLs packaged by the release workflow. Old Visual Studio and 32-bit guides are not current validated tracks.

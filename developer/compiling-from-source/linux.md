# Build on Linux

> **Verified against:** [Pinned source and release revisions](../../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Validated recipe source:** Core `v2.0.2` release workflow, Ubuntu 22.04 x86_64, GCC 11.

```bash
sudo apt-get update
sudo apt-get install -y build-essential cmake ninja-build pkg-config git ccache python3 curl file patchelf binutils zip \
  libboost-all-dev libssl-dev libzmq3-dev libpgm-dev libunbound-dev libsodium-dev \
  libhidapi-dev libusb-1.0-0-dev libunwind-dev liblzma-dev libexpat1-dev \
  libgcrypt20-dev libgpg-error-dev libprotobuf-dev protobuf-compiler libgtest-dev

git clone --recursive https://github.com/qwertycoin-org/qwertycoin.git source
git -C source checkout v2.0.2
git -C source submodule update --init --recursive

cmake -S source -B build/linux -G Ninja \
  -DCMAKE_BUILD_TYPE=Release -DARCH=default -DBUILD_64=ON -DSTATIC=OFF \
  -DBUILD_SHARED_LIBS=OFF -DBUILD_TESTS=ON -DBUILD_DOCUMENTATION=OFF \
  -DBUILD_DEBUG_UTILITIES=OFF -DUSE_DEVICE_TREZOR=OFF -DUSE_READLINE=OFF \
  -DBUILD_TAG=linux-x64 -DMANUAL_SUBMODULES=1 \
  -DMONERO_PARALLEL_COMPILE_JOBS=2 -DMONERO_PARALLEL_LINK_JOBS=1

cmake --build build/linux --target daemon simplewallet wallet_rpc_server epose_unit_tests --parallel 2
ctest --test-dir build/linux -R '^epose_unit_tests$' --output-on-failure
build/linux/bin/qwertycoind --version
build/linux/bin/qwertycoin-wallet-cli --help >/dev/null
build/linux/bin/qwertycoin-wallet-rpc --help >/dev/null
```

Other distributions/architectures may work but are not claimed as release-validated here. If static archives are unavailable, use this dynamic build instead of forcing `STATIC=ON`.


# Build the desktop GUI

> **Verified against:** [Pinned source and release revisions](../../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Published GUI:** `v2.0.2` (`c5eced2`), Core submodule `54308d84`.  
> **Development GUI:** `ecd1844f`, verified 2026-09-29.

```bash
git clone --recursive https://github.com/qwertycoin-org/qwertycoin-gui.git
cd qwertycoin-gui
git checkout v2.0.2
git submodule sync --recursive
git submodule update --init --recursive
tools/check_core_pin.sh
```

The maintained review configuration uses Qt 5.15, C++17, Ninja and the explicit `qwertycoin/` Core submodule:

```bash
cmake -S . -B build/gui-review -G Ninja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo -DSTATIC=OFF -DMANUAL_SUBMODULES=1 \
  -DDEV_MODE=OFF -DWITH_UPDATER=ON -DBUILD_TAG=linux-x64 \
  -DUSE_DEVICE_TREZOR=OFF -DQML_TESTS=ON
cmake --build build/gui-review \
  --target qwertycoin-gui qwertycoin-gui-epose-tests simplewallet wallet_rpc_server \
  --parallel 2
tools/check_core_pin.sh
```

Run repository GUI/EPoSe, QML, restore and disposable regtest smoke tests before treating a build as reviewed. Published tracks are Linux x86_64, macOS arm64 and Windows x86_64. macOS/Windows artifacts are not documented as fully publisher-signed/notarized. Hardware wallets and inherited P2Pool launching remain fail-closed pending QWC-specific validation.


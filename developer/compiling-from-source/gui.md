# Build the desktop GUI

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../../reports/source-version-matrix.md).

> **Source track:** latest stable GUI release and its recorded Core submodule. Default-branch builds are development builds and must identify both exact commits.

Open the [GUI latest release](https://github.com/qwertycoin-org/qwertycoin-gui/releases/latest) and copy its stable tag before running:

```bash
read -r -p "Latest stable GUI release tag: " QWC_GUI_RELEASE_TAG
[[ "$QWC_GUI_RELEASE_TAG" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]] || {
  echo "invalid stable release tag" >&2
  exit 1
}
git clone --recursive https://github.com/qwertycoin-org/qwertycoin-gui.git
cd qwertycoin-gui
git checkout --detach "$QWC_GUI_RELEASE_TAG"
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

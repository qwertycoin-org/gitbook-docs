# Retired and historical features

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> These items are retained only as migration context. Their old operational commands are not current Qwertycoin instructions.

| Historical subject | Current disposition |
| --- | --- |
| `simplewallet`, `walletd`, REST port 8070 | Replaced by `qwertycoin-wallet-cli` and authenticated `qwertycoin-wallet-rpc` JSON-RPC |
| Legacy masternode registration/flags | Replaced by automatic EPoSe v2 lifecycle/admission |
| CryptoNight/XMR-Stak/mobile/SBC/cloud mining | Retired; current PoW is RandomX `rx/0` |
| Old paper/Zero/mobile wallet guides | Retired; no verified current supported release/generator |
| Legacy pool/faucet/voting infrastructure | Retired; use current maintained repositories where listed |
| Bisq/Bitexlive/CREX24 deposit guides | Historical only; current-network support not verified |
| Old explorer/web-wallet hosting | Replaced by maintained hardened repositories/runbooks |
| CSV checkpoint import guide | Retired for normal recovery; resynchronize current chain data |
| Generic forking guides | Historical source-layout assumptions; not a supported deployment recipe |
| Google Breakpad integration page | Historical contributor context, not a current operator requirement |

Historical page text remains recoverable in Git history at wiki commit `eb89175`. Compatibility pages link to supported replacements without pretending to be server redirects.


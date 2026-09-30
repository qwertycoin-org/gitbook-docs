# Discrepancy register

> **Verified against:** GitBook baseline `151a593…`, validated GitHub Wiki `b4e1f81…`, Core `a71c0eb2…`, Core release `v2.0.2` (`54308d847…`), Qwertycoin mainnet where applicable, 2026-09-30 UTC.

| Conflict | Resolution |
| --- | --- |
| Old GitBook/Wiki content describes a Karbowanec/Bytecoin-derived runtime | Current Core is based on Monero 0.18.x plus Qwertycoin protocol and EPoSE changes. Historical ancestry is context only. |
| Old wallet pages use `simplewallet`, `walletd`, container files, and port 8070 | Current binaries are `qwertycoin-wallet-cli` and `qwertycoin-wallet-rpc`; old pages are retirement notices. |
| Old masternode page describes the retired service-node path | Replaced by EPoSE v2 operator documentation. Legacy `--service-node*` and funded registration workflows are rejected. |
| Old mining pages use CryptoNight/XMR-Stak | Replaced by RandomX instructions. |
| Old exchange pages claim support at CREX24, Bitexlive, and Bisq | Retired. Current network compatibility must be verified per venue; this documentation does not preserve old deposit instructions. |
| Core README release link and latest GitHub release may differ | Downloads are bound to GitHub release `v2.0.2`; repository text is supporting evidence only. |
| Port `8198` appears as both wallet RPC and public EPoSE probe RPC | They are different processes. Combined-host examples bind wallet RPC to loopback port `18082` and reserve public `8198` for restricted EPoSE probe RPC. |
| EPoSE examples sometimes say six receipts universally | Six is the full 9-verifier case. Runtime quorum is `ceil(2n/3)` for actual committee size `n`. |
| `get_epose_diagnostics` appears on `main` but not in `v2.0.2` | Marked development-only with minimum commit `a71c0eb2…`. |
| Historical “maximum supply” wording conflicts with tail emission | The emission constant is about 184.467 million QWC; continuing tail subsidy means it is not an absolute lifetime cap. |
| Published `v2.0.2` Linux metadata contains an EPoSe release-gate `no-go` result | Runtime/test evidence is documented, but this documentation does not claim formal gate approval; see [Implementation Defects](implementation-defects.md). |

Implementation defects discovered during validation are recorded in [Validation Report](validation-report.md); documentation does not change runtime behavior to hide them.

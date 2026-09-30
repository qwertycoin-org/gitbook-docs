# EPoSE monitoring and diagnostics

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Release note:** `get_epose_diagnostics` is **not** in `v2.0.2`; it requires development source `a71c0eb2` or later containing that route.

Monitor distinct stages separately:

| Stage | Evidence |
| --- | --- |
| Producer ready | configured, keystore loaded, endpoint valid |
| Registered | descriptor is canonical |
| Active | descriptor effective in current epoch/snapshot |
| Qualified | closed chain-derived set contains the service key |
| Selected | deterministic payout plan selects the prior-epoch member |
| Received | wallet detects Coinbase service output |
| Spendable | normal Coinbase maturity has elapsed |

On release `v2.0.2`, use local unrestricted `get_info`, `get_epose_info`, endpoint/status/reward methods and structured logs. Do not expose unrestricted RPC.

Development diagnostics require an unrestricted listener **and configured RPC authentication**. A protected netrc avoids credentials in process arguments:

```bash
curl --digest --netrc-file /secure/path/qwertycoind-rpc.netrc \
  -s -X POST http://127.0.0.1:8197/get_epose_diagnostics \
  -H 'Content-Type: application/json' \
  -d '{"recent_limit":50,"epoch":11}'
```

`recent_limit` defaults to 50 and is capped at 100. Counters/recent attempts are restart-local and bounded; canonical coverage and finalized qualification are reconstructed from chain state. Scheduler skips such as not selected/already canonical/backoff are not attempt failures. Local submission accepted is not canonical inclusion.

Stable reasons include descriptor unavailable/invalid/expired/commitment mismatch; DNS/refusal/timeout/transport/HTTP failures; malformed/oversized/unexpected/context/identity/object/signature responses; encoding failures; local submission rejection; cancellation; deadline expiry; and internal execution failure. Never log raw secrets or remote payloads.

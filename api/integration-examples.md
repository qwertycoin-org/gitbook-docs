# Integration examples

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> Examples target authenticated `qwertycoin-wallet-rpc v2.0.2` on loopback `18082`. Placeholder addresses/hashes are non-executable.

## JSON-RPC shape

```json
{"jsonrpc":"2.0","id":"balance-1","method":"get_balance","params":{"account_index":0,"strict":true}}
```

A deterministic illustrative response shape (amounts are atomic units):

```json
{"jsonrpc":"2.0","id":"balance-1","result":{"balance":12300000000,"unlocked_balance":12000000000,"multisig_import_needed":false,"per_subaddress":[],"blocks_to_unlock":0,"time_to_unlock":0}}
```

## Address ownership

1. Call `validate_address` with `any_net_type:false` and `allow_openalias:false`.
2. Require `valid:true`, `nettype:"mainnet"` and the expected address type.
3. Call `get_address_index`; success proves the address belongs to the currently open wallet.
4. Re-read it with `get_address` using the returned major/minor indexes.

## Payment detection

Assign one subaddress per customer with `create_address`. Poll `get_transfers`/`get_transfer_by_txid` and store transaction hash, output/subaddress index, atomic amount, block height and observed canonical block hash. Credit only after the exchange's documented confirmation policy. Re-check credited deposits across reorganizations and make credit state reversible until final policy depth.

## Build before relay

Use `transfer` with `do_not_relay:true` and `get_tx_metadata:true` to construct without broadcasting. Persist the returned metadata and fee, then use `relay_tx` once policy checks approve it. If a relay response times out, reconcile by hash/history/mempool before any retry.

## Minimal Python client

```python
from decimal import Decimal
import itertools, json, netrc, urllib.request

ATOMIC = Decimal(100_000_000)
counter = itertools.count(1)
RPC_URL = "http://127.0.0.1:18082/json_rpc"
login, _, password = netrc.netrc("/run/secrets/qwc-wallet-rpc.netrc").authenticators("127.0.0.1")
passwords = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passwords.add_password(None, RPC_URL, login, password)
opener = urllib.request.build_opener(urllib.request.HTTPDigestAuthHandler(passwords))

def to_atomic(text: str) -> int:
    value = Decimal(text) * ATOMIC
    if value != value.to_integral_value() or value < 0:
        raise ValueError("amount is not an exact non-negative atomic value")
    return int(value)

def rpc(method: str, params: dict) -> dict:
    body = json.dumps({"jsonrpc":"2.0","id":next(counter),"method":method,"params":params}).encode()
    request = urllib.request.Request(
        RPC_URL, body,
        {"Content-Type":"application/json"}, method="POST")
    with opener.open(request, timeout=15) as response:
        payload = json.load(response)
    if "error" in payload:
        raise RuntimeError(f"RPC {payload['error'].get('code')}: {payload['error'].get('message')}")
    if "result" not in payload:
        raise RuntimeError("missing JSON-RPC result")
    return payload["result"]

balance = rpc("get_balance", {"account_index": 0, "strict": True})
print(balance["unlocked_balance"])  # integer only; do not log addresses/keys
```

In production, use a client that supplies HTTP Digest credentials from a protected store, verifies response size/content type, caps concurrency, serializes wallet access and redacts secret-bearing fields.

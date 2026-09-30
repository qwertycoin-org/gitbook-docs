# Message signing

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

Message signing proves control of a wallet key for a particular message; it is not a transaction and does not reveal a spend key. It does not prove a legal identity unless the address-to-person binding was established separately.

## Wallet RPC

The current wallet RPC exposes `sign` and `verify` through `/json_rpc`. Keep RPC authenticated and private.

Illustrative request:

```json
{"jsonrpc":"2.0","id":"sign-1","method":"sign","params":{"data":"release statement"}}
```

Verification requires the message, address, and returned signature. Inspect the exact request fields for the pinned release in [Wallet RPC Reference](../api/wallet-rpc-reference.md).

The historical `simplewallet` instructions are retired; use current CLI/GUI/RPC features.

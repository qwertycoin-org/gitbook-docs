# RPC errors and compatibility

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

Three layers can fail independently:

1. HTTP transport/authentication (non-2xx, timeout, malformed body).
2. JSON-RPC envelope (`error.code`/`error.message`, no usable `result`).
3. Method-level `status`, booleans, counts or trust flags inside a successful result.

Core daemon error codes include invalid parameters/heights/address/blob, busy/internal states, block rejection, restricted method/parameters, regtest requirement, RPC-payment errors and unsupported bootstrap behavior. Wallet codes cover address/payment/transaction errors, denied/restricted operations, wallet state, insufficient unlocked funds, password/keys/metadata, multisig, daemon connectivity and background-sync constraints. Refer to the pinned error-code headers linked by the source matrix; clients must preserve unknown future codes.

Never retry a timed-out spending or relay request blindly. First query wallet history/transfer state, derived transaction hash if known, daemon mempool and canonical chain. Retry only after proving the original action did not occur; no general idempotency guarantee is documented.

Legacy aliases in [RPC Inventory](rpc-inventory.md) remain callable only where registered. Do not invent snake_case replacements for historical method names. Release `v2.0.2` lacks both registrations for `get_epose_diagnostics`; clients must feature-detect `get_version` and handle method-not-found.

`walletd` on port 8070 and its historical REST contract are retired and incompatible with current `qwertycoin-wallet-rpc` JSON-RPC.

# Daemon HTTP and binary RPC

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

Path RPC posts directly to `/<method>` and does **not** use a JSON-RPC envelope. `.bin` routes use the portable binary archive expected by Core clients; sending JSON to them is invalid.

## JSON path methods

- **Chain/transactions:** `/get_height` (`/getheight`), `/get_transactions` (`/gettransactions`), `/is_key_image_spent`, `/get_outs`, `/get_output_distribution.bin` (binary despite the grouped purpose).
- **Transaction relay:** `/send_raw_transaction` (`/sendrawtransaction`). Relay can have side effects and a timed-out response is ambiguous.
- **Pool:** `/get_transaction_pool`, `/get_transaction_pool_hashes`, `/get_transaction_pool_stats`.
- **Node status:** `/get_info` (`/getinfo`), `/get_public_nodes`, `/get_limit`.
- **Unrestricted administration:** `/get_alt_blocks_hashes`, `/start_mining`, `/stop_mining`, `/mining_status`, `/save_bc`, `/get_peer_list`, `/set_log_hash_rate`, `/set_log_level`, `/set_log_categories`, `/set_bootstrap_daemon`, `/stop_daemon`, `/get_net_stats`, `/set_limit`, `/out_peers`, `/in_peers`, `/update`, `/pop_blocks`.
- **EPoSE:** the path methods listed in [EPoSE RPC Reference](epose-rpc-reference.md).

## Binary path methods

`/get_blocks.bin` (`/getblocks.bin`), `/get_blocks_by_height.bin` (`/getblocks_by_height.bin`), `/get_hashes.bin` (`/gethashes.bin`), `/get_o_indexes.bin`, `/get_outs.bin`, `/get_transaction_pool_hashes.bin`, and `/get_output_distribution.bin`.

Use a Qwertycoin/Monero-compatible portable-storage client implementation bound to the pinned schema. Binary integer widths, vectors and nested structures are defined by the linked command structures in [RPC Inventory](rpc-inventory.md); they are not JSON equivalents.

An HTTP 200 only means the transport request completed. Check JSON-RPC errors where applicable, then method `status`, booleans and returned counts. Reject `BUSY`, non-`OK`, malformed, truncated and `untrusted` data according to the integration's policy.

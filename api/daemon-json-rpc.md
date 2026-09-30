# Daemon JSON-RPC

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Verified route map:** development `a71c0eb2`; release differences are marked in the generated inventory.

POST to `/json_rpc`:

```json
{"jsonrpc":"2.0","id":"status","method":"get_block_count","params":{}}
```

An illustrative success response is:

```json
{"jsonrpc":"2.0","id":"status","result":{"count":12345,"status":"OK","untrusted":false}}
```

Values above are illustrative, not a captured live chain. The exact schema for every method is linked from [RPC Inventory](rpc-inventory.md).

## Method groups

- **Chain and blocks:** `get_block_count` (`getblockcount` alias), `on_get_block_hash` (`on_getblockhash`), `get_last_block_header` (`getlastblockheader`), `get_block_header_by_hash` (`getblockheaderbyhash`), `get_block_header_by_height` (`getblockheaderbyheight`), `get_block_headers_range` (`getblockheadersrange`), `get_block` (`getblock`), `hard_fork_info`, `get_version`.
- **Mining/template:** `get_block_template` (`getblocktemplate`), `get_miner_data`, `calc_pow`, `add_aux_pow`, `submit_block` (`submitblock`), `generateblocks`. Generation is regtest-only and unrestricted; template/submission methods have material side effects or resource cost.
- **Outputs/fees/pool:** `get_output_histogram`, `get_fee_estimate`, `get_txpool_backlog`, `get_output_distribution`, `flush_txpool`, `relay_tx`, `get_coinbase_tx_sum`.
- **Node/peers/admin:** `get_connections`, `set_bans`, `get_bans`, `banned`, `sync_info`, `get_alternate_chains`, `prune_blockchain`, `flush_cache`.
- **RPC payment:** `rpc_access_info`, `rpc_access_submit_nonce`, `rpc_access_pay`, `rpc_access_tracking`, `rpc_access_data`, `rpc_access_account`. These are active only when the server's RPC-payment configuration enables them.
- **EPoSE:** `get_epose_info`, `get_service_nodes`, `get_service_node_status`, retired-status `get_service_node_registration_payload`, `get_epose_epoch`, `get_service_rewards`, `get_epose_block_reward`; development-only `get_epose_diagnostics`.

Methods registered with `!m_restricted` are rejected on a restricted listener. Other methods can still have parameter limits, privacy-reduced responses, authentication requirements, bootstrap restrictions or handler-level failures. Treat `restricted` as a defined route policy, not a synonym for harmless/read-only.

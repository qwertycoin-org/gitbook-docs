# Wallet RPC reference

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Route map:** 96 registrations / 92 unique command structures at Core `a71c0eb2`; identical registration count in `v2.0.2`.

All methods use JSON-RPC 2.0 at `/json_rpc`. Exact request/response fields, optional defaults, integer types and source permalinks are in [RPC Inventory](rpc-inventory.md). Amounts are atomic units.

## Complete method coverage

- **Balance/sync:** `get_balance` (`getbalance` alias), `get_height` (`getheight`), `refresh`, `auto_refresh`, `scan_tx`, `rescan_blockchain`, `rescan_spent`.
- **Accounts/subaddresses:** `get_address` (`getaddress`), `get_address_index`, `set_subaddress_lookahead`, `create_address`, `label_address`, `get_accounts`, `create_account`, `label_account`, `get_account_tags`, `tag_accounts`, `untag_accounts`, `set_account_tag_description`.
- **Output selection:** `freeze`, `thaw`, `frozen`, `incoming_transfers`.
- **Create/sign/relay transactions:** `transfer`, `transfer_split`, `sign_transfer`, `describe_transfer`, `submit_transfer`, `sweep_dust` (`sweep_unmixable` alias), `sweep_all`, `sweep_single`, `relay_tx`, `estimate_tx_size_and_weight`, `get_default_fee_priority`.
- **History/payment detection:** `get_payments`, `get_bulk_payments`, `get_transfers`, `get_transfer_by_txid`.
- **Keys/proofs/signing:** `query_key`, `get_tx_key`, `check_tx_key`, `get_tx_proof`, `check_tx_proof`, `get_spend_proof`, `check_spend_proof`, `get_reserve_proof`, `check_reserve_proof`, `sign`, `verify`.
- **Offline/watch-only exchange:** `export_outputs`, `import_outputs`, `export_key_images`, `import_key_images`.
- **Addresses/URIs/book:** `make_integrated_address`, `split_integrated_address`, `validate_address`, `make_uri`, `parse_uri`, `get_address_book`, `add_address_book`, `edit_address_book`, `delete_address_book`.
- **Wallet lifecycle:** `get_languages`, `create_wallet`, `open_wallet`, `close_wallet`, `change_wallet_password`, `generate_from_keys`, `restore_deterministic_wallet`, `store`, `stop_wallet`.
- **Multisig:** `is_multisig`, `prepare_multisig`, `make_multisig`, `export_multisig_info`, `import_multisig_info`, `exchange_multisig_keys`, `sign_multisig`, `submit_multisig`.
- **Local metadata:** `set_tx_notes`, `get_tx_notes`, `set_attribute`, `get_attribute`.
- **Daemon/mining/logging:** `set_daemon`, `start_mining`, `stop_mining`, `set_log_level`, `set_log_categories`, `get_version`.
- **Background sync:** `setup_background_sync`, `start_background_sync`, `stop_background_sync`.

Secret-returning methods include `query_key`, transaction-key/proof creation and export operations. Spending/admin methods include transaction creation/relay, sweeps, wallet creation/restoration/password changes, daemon changes and shutdown. Restrict callers by more than network location.

## Representative contracts

`get_balance` accepts `account_index`, `address_indices`, optional `all_accounts` and `strict`; it returns total/unlocked atomic balances, unlock estimates and per-subaddress entries.

`transfer` accepts destination address/amount pairs, account/subaddress selection, fee priority, optional `subtract_fee_from_outputs`, optional `do_not_relay`, and output toggles. Its response includes transaction hash/key, sent amount, fee, weight, and requested blob/metadata. Do not request or log transaction secret keys unless required.

`validate_address` verifies address/network/type; it does not prove that an address belongs to the open wallet. Follow with `get_address_index` for ownership.

View-only and restricted modes reject methods requiring unavailable spend authority. Treat `WALLET_RPC_ERROR_CODE_WATCH_ONLY`, `DENIED` and `DISABLED` as expected policy errors, not transient retries.

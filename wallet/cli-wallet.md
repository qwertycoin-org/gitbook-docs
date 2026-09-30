# CLI wallet

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Verified binary:** `qwertycoin-wallet-cli` from Core `v2.0.2`.

Start against a local daemon:

```bash
./qwertycoin-wallet-cli --daemon-address http://127.0.0.1:8197
```

On first run, choose a new wallet name, strong password, and language. Record the generated mnemonic seed offline. To reopen:

```bash
./qwertycoin-wallet-cli \
  --wallet-file /secure/wallets/qwc-main \
  --daemon-address http://127.0.0.1:8197
```

Common interactive commands include `address`, `balance`, `refresh`, `transfer`, `show_transfers`, `seed`, `save`, and `exit`; confirm exact commands with `help` in the installed version.

## Restore

Use the interactive restore flow or supported startup options shown by:

```bash
./qwertycoin-wallet-cli --help | less
```

Choose a restore height at or before the wallet's first transaction. Too-high restore height can omit history; height 0 is conservative but slower.

## Sending safely

1. Confirm daemon and wallet are synchronized.
2. Verify the destination and amount in QWC.
3. Review the wallet's fee/transaction confirmation.
4. Record the transaction ID.
5. If a command times out, inspect wallet history and daemon state before retrying; do not assume it was not relayed.

The historical executable `simplewallet` is not current Qwertycoin software.

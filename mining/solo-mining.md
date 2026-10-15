# Solo mining

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

> **Verified command surface:** daemon and CLI wallet from the latest stable Core release.

Solo mining submits work directly to your synchronized local daemon. Rewards arrive only when you find a valid block, so variance can be very high.

From `qwertycoin-wallet-cli`, after the wallet and local daemon are synchronized:

```text
start_mining 1
```

The optional arguments are thread count, background-mining mode and ignore-battery. Use `stop_mining` to stop. From the daemon console the explicit form is:

```text
start_mining QWC_PRIMARY_ADDRESS 1
```

Mining to a subaddress is rejected; use a current primary address. Keep daemon RPC private—the `/start_mining` and `/stop_mining` administrative routes are unrestricted-only.

Verify hashrate and accepted blocks in the daemon/wallet, not only process CPU use. A stale or unsynchronized daemon wastes work.

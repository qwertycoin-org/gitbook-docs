# Exchanges and network compatibility

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Verified listing evidence:** Neoxa Exchange `QWC/USDT` market page reachable on 2026-09-29. Deposit/withdrawal operation was not tested.

Current market link: [QWC/USDT on Neoxa Exchange](https://neoxa.exchange/trade/QWC_USDT).

A listing page does not prove that deposits, withdrawals, liquidity or a particular chain generation are currently available. Before sending funds:

1. Confirm the exchange explicitly supports the current reset Qwertycoin mainnet/Core generation.
2. Generate a fresh deposit address and validate it with current `qwertycoin-wallet-rpc`.
3. A valid mainnet subaddress can visibly begin with `Qqb`; primary addresses normally begin `QWC`.
4. Send a small test deposit, wait for the exchange's stated confirmations, then test withdrawal to a wallet you control.
5. Never edit an address prefix or reuse historical-network deposit instructions.

Exchange operators should use [Wallet RPC Setup](../api/wallet-rpc-setup.md) and [Integration Examples](../api/integration-examples.md), one subaddress per customer, exact atomic-unit arithmetic, reorg-aware crediting and reconciled withdrawals.

Bisq, Bitexlive and CREX24 pages in the old wiki are historical compatibility notices, not current endorsements.


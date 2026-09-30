# Privacy model

> **Verified against:** current Monero-derived transaction implementation in Core `a71c0eb2…`, Qwertycoin mainnet, 2026-09-29.

Qwertycoin transactions use CryptoNote/Monero-derived mechanisms including one-time addresses, ring signatures, confidential amounts, and stealth address derivation. These mechanisms reduce direct on-chain linkage between sender, recipient, and amount.

They do **not** make all metadata invisible:

- P2P peers can observe network connections and relay timing.
- A remote daemon learns the requesting IP unless a separate network-privacy layer is used and may observe wallet query patterns.
- Wallet RPC operators can access the loaded wallet and transaction metadata; keep wallet RPC private and authenticated.
- Exchanges and counterparties know their own deposit/withdrawal records.
- Transaction size, fee, block placement, and public EPoSE records remain observable.

Avoid absolute “anonymous” claims. Privacy depends on current protocol rules, correct wallet behavior, network configuration, and user behavior.

## Remote nodes

A remote node validates and relays chain data but is not entrusted with spend keys. It can still observe requests and provide delayed or selective data. Prefer a synchronized local node for stronger availability and metadata privacy.

## Seeds and view-only wallets

Mnemonic seeds and private spend keys control funds. Private view keys reveal incoming activity. View-only wallets cannot spend, but they are sensitive. Restoring historical key material does not recreate legacy-chain balances on current mainnet.

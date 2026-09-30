# Glossary

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

| Term | Meaning |
| --- | --- |
| atomic unit | Smallest QWC amount; `100,000,000` atomic units equal `1 QWC`. |
| Coinbase transaction | Block transaction that creates scheduled subsidy and pays miner/service outputs; unrelated to the exchange named Coinbase. |
| daemon | `qwertycoind`, which validates, stores, and relays the blockchain. |
| EPoSE | Qwertycoin service-evidence and reward protocol; distinct from mining and staking. |
| epoch | 720-block EPoSE interval, approximately 24 hours at target block time. |
| identity keystore | Protected EPoSE operator/service keys; not a wallet and contains no wallet spend/view key. |
| main address | Primary wallet address, normally beginning `QWC…` on current mainnet. |
| restricted RPC | Daemon listener that blocks selected administrative/write methods; it is not automatically harmless or private. |
| restore height | Earliest block height a wallet scans when reconstructing transaction history. |
| service key | Online EPoSE key authorized by the stable operator identity. |
| subaddress | Wallet-derived address for payment separation; current mainnet subaddresses commonly begin `Qqb…`. |
| tail emission | Continuing minimum subsidy after the main emission curve reaches its lower bound. |
| wallet cache | Regenerable transaction/cache data; not a substitute for seed/key backup. |
| wallet RPC | `qwertycoin-wallet-rpc`, an authenticated integration process that holds wallet authority. |

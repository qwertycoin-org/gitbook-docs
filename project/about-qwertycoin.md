# About Qwertycoin

> **Verified against:** Core `a71c0eb2…` and release `v2.0.2`, Qwertycoin mainnet reset profile, 2026-09-29.

Qwertycoin is a privacy-focused cryptocurrency network. Current Core is based on the Monero 0.18.x codebase and retains CryptoNote transaction privacy and RandomX proof-of-work, with Qwertycoin-specific network parameters and EPoSE service rewards.

## Two distinct roles

- **RandomX mining** produces blocks and secures chain selection.
- **EPoSE** deterministically rewards qualified service identities from a portion of scheduled block subsidy.

EPoSE is not proof of stake and does not replace proof of work. A normal miner needs no EPoSE identity; an EPoSE operator does not have to mine.

## Current network versus historical Qwertycoin

The current mainnet is a clean network reset with a new genesis block, network ID, address prefixes, data directory, and consensus profile. Historical chain databases, wallet caches, peer state, and balances do not carry over automatically. Old key material may be importable for address/key recovery experiments, but it does not recreate legacy-chain balances on the current chain.

Older Karbowanec/Bytecoin ancestry descriptions remain historical context, not a description of the present runtime.

See [Legacy Network Compatibility](legacy-network-compatibility.md), [Network Parameters and Emission](network-parameters-and-emission.md), and [Privacy Model](privacy-model.md).

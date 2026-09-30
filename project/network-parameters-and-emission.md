# Network parameters and emission

> **Verified against:** Core `a71c0eb2…` / `src/cryptonote_config.h`, EPoSE compiled Qwertycoin mainnet profile, 2026-09-29 UTC.

| Parameter | Mainnet value |
| --- | --- |
| Consensus hardfork | HF17 from height 0 |
| Proof of work | RandomX |
| Block target | 120 seconds |
| Decimal places | 8 |
| Atomic units per QWC | 100,000,000 |
| Emission constant | `18,446,744,073,709,551` atomic units = `184,467,440.73709551 QWC` |
| Tail subsidy constant | `0.3 QWC/minute` = `0.6 QWC/block` at 120 seconds |
| Coinbase maturity | 60 blocks |
| Main address prefix | `0x14820c` (normally `QWC…`) |
| Integrated-address prefix | `0x14820d` |
| Subaddress prefix | `0x14820e` (commonly `Qqb…`) |
| P2P / daemon RPC / ZMQ | 8196 / 8197 / 8199 |

## Supply wording

The emission constant is the input to the CryptoNote emission curve; it is not an absolute lifetime cap because tail emission continues. Documentation must not describe approximately 184.47 million QWC as a hard final supply while also documenting continuing tail subsidy.

The scheduled block subsidy uses integer atomic-unit arithmetic. EPoSE currently allocates `floor(scheduled_subsidy × 1000 / 10000)` to the selected service payee when one exists. Transaction fees remain entirely with the miner.

Example for a scheduled subsidy of `60,000,000` atomic units (`0.6 QWC`) and fees of `2,500,000` atomic units:

```text
service = floor(60,000,000 × 1,000 / 10,000) = 6,000,000
miner subsidy = 54,000,000
miner fees = 2,500,000
coinbase total = 62,500,000 atomic units
```

See [EPoSE Rewards](../epose/rewards.md) for source-epoch selection and empty-set behavior.

# Pool mining

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Live configuration checked:** 2026-09-29 against `pool.qwertycoin.org` and its source repository.

The official pool uses RandomX `rx/0`, PPLNS and a 5% pool fee. It uses a 60-block maturity depth. Payout policy and live endpoints can change; verify the [pool site](https://pool.qwertycoin.org/) before mining.

With official XMRig `v6.26.0` or another reviewed compatible release:

```bash
xmrig -a rx/0 -o mine.qwertycoin.org:3333 -u QWC_PRIMARY_ADDRESS -p rig-01
```

Available endpoints at verification time:

| Port | Mode |
| ---: | --- |
| 3333 | TCP, low/variable difficulty |
| 4443 | TLS, variable difficulty; add XMRig's TLS option |
| 5555 | TCP, medium fixed start |
| 7777 | TCP, high fixed start |

The username is your public payout address; never provide a seed, spend key or wallet password. Use a distinct worker name after `-p`.

The default automatic payout threshold is 1,000 QWC. Each payout is single-recipient: the miner's gross balance is debited and the actual network fee is subtracted from that output. Raising the signed threshold reduces how frequently the miner pays a transaction fee. Check accepted/rejected shares, effective hashrate, unpaid balance and payments on the miner dashboard.


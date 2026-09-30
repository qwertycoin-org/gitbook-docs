# RandomX mining

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Verified:** Core `v2.0.2`, official pool profile, XMRig `v6.26.0`, 2026-09-29.

RandomX proof of work produces Qwertycoin blocks and secures chain selection. EPoSE is a separate service-reward mechanism and never substitutes for PoW.

Current miner settings:

- algorithm: `rx/0` (RandomX);
- address: a current mainnet QWC primary address;
- pool protocol: standard CryptoNote Stratum where offered;
- amount precision: 8 decimals.

Historical CryptoNight, XMR-Stak, mobile/SBC and cloud-mining instructions are retired. They are not current QWC recipes.

RandomX benefits from large memory pages, sufficient RAM and CPU cache. Enable huge pages through the operating system's documented mechanism and verify XMRig reports them; do not run downloaded miners as root merely to bypass permissions. Obtain XMRig from its [official release repository](https://github.com/xmrig/xmrig/releases/tag/v6.26.0), verify its published artifact checks, and review antivirus detections rather than disabling protections globally.

Choose [Solo Mining](solo-mining.md) for direct variance or [Pool Mining](pool-mining.md) for share-based payouts. Mining never guarantees profit; account for electricity, hardware wear, fees and network difficulty.


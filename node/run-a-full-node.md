# Run a full node

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Published-release track:** Core `v2.0.2` (`54308d84`), mainnet.  
> **Verified:** 2026-09-29.

A full node validates the chain and serves wallets and peers. It does not automatically qualify for EPoSe rewards.

## Safe first start

Download and verify the package from the [v2.0.2 release](https://github.com/qwertycoin-org/qwertycoin/releases/tag/v2.0.2), then run:

```bash
./qwertycoind \
  --p2p-bind-ip 0.0.0.0 --p2p-bind-port 8196 \
  --rpc-bind-ip 127.0.0.1 --rpc-bind-port 8197 \
  --zmq-rpc-bind-ip 127.0.0.1 --zmq-rpc-bind-port 8199
```

Open only TCP `8196` to the public Internet. Binding P2P to `0.0.0.0` is intentional; binding unrestricted RPC or ZMQ to a wildcard address is not.

Check status in the daemon console with `status` and `sync_info`. The node is ready for normal wallet use when its height tracks healthy peers and it reports synchronized. A merely running process is not proof of synchronization.

Use `--data-dir PATH` to select persistent blockchain storage. Stop cleanly with the console `exit` command or the service manager's normal stop operation. Do not copy an actively written LMDB directory as a guaranteed consistent backup.

For unattended operation use [Linux Service Operation](linux-service-operation.md) or [Docker](docker.md). For service rewards, continue with [EPoSE Overview](../epose/overview.md).


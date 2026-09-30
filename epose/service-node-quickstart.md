# EPoSE service node quickstart

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Published-release track:** Core `v2.0.2`, Linux x86_64 or Docker `linux/amd64`.  
> **Network:** current mainnet only.

## Requirements

- Synchronized, **unpruned** mainnet daemon.
- Dedicated runtime user and persistent chain directory.
- Stable public DNS name or public IPv4/IPv6 for the service endpoint.
- Public TCP `8196` (P2P) and `8198` (restricted probe RPC).
- Private loopback TCP `8197` (unrestricted RPC) and `8199` (ZMQ).
- One public **primary** QWC reward address. Never provide wallet secret keys.
- Protected, persistent EPoSE keystore stored separately from chain and wallet data.

## Start

After verifying the release package and creating the service account:

```bash
qwertycoind \
  --epose-v2-service \
  --epose-v2-keystore /var/lib/qwertycoin-identity/epose-v2-keystore \
  --epose-v2-reward-address QWC... \
  --epose-v2-endpoint-host node.example.org \
  --epose-v2-endpoint-port 8198 \
  --epose-v2-discovery-endpoint http://seed-00.qwertycoin.org:8198 \
  --epose-v2-discovery-endpoint http://seed-01.qwertycoin.org:8198 \
  --p2p-bind-ip 0.0.0.0 --p2p-bind-port 8196 \
  --rpc-bind-ip 127.0.0.1 --rpc-bind-port 8197 \
  --rpc-restricted-bind-ip 0.0.0.0 --rpc-restricted-bind-port 8198 \
  --confirm-external-bind \
  --zmq-rpc-bind-ip 127.0.0.1 --zmq-rpc-bind-port 8199
```

Discovery options may be repeated. They bootstrap signed endpoint discovery; they are not allowlists and do not grant admission.

## Verify

From the operator host:

```bash
curl -s http://127.0.0.1:8197/get_info
curl -s http://127.0.0.1:8197/get_epose_info
curl -s http://127.0.0.1:8197/get_epose_service_endpoint_v2
```

From an external network, verify DNS and that the restricted `8198` endpoint serves the signed descriptor. Confirm that unrestricted RPC `8197` and ZMQ `8199` are not reachable publicly.

Normal progression is `ready → registered → active → qualified`, subject to synchronization, enrollment cutoff, descriptor warm-up, admission, receipt rounds and canonical inclusion. Restart with the same keystore and verify the same public keys.

## Docker path

Use the official image pinned by digest, separate chain and identity volumes, UID/GID `10001`, and the same port policy. The maintained Core deployment contract is under `deploy/mainnet/`; do not commit real reward addresses or private host configuration.

No funded registration transaction, wallet private key, staking deposit, `register_service_node`, or legacy `--service-node*` option belongs in this workflow.


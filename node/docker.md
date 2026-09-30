# Docker

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Published-release track:** official image packaging for Core `v2.0.2`, verified 2026-09-29.

The official image is `docker.io/qwertycoin/qwertycoin`. The current build packages a verified Linux release archive rather than compiling Core inside the final image. The documented architecture is `linux/amd64`.

```bash
docker pull docker.io/qwertycoin/qwertycoin:v2.0.2
docker inspect --format '{{index .RepoDigests 0}}' docker.io/qwertycoin/qwertycoin:v2.0.2
```

Pin the returned immutable digest in production. Entrypoint selectors are default/`daemon`, `wallet`, and `wallet-rpc`.

Use separate persistent volumes for blockchain data, wallet material and EPoSe identity. The image runs as UID/GID `10001`; prepare ownership accordingly. Prefer a read-only root filesystem, dropped capabilities, `no-new-privileges`, bounded logs and a graceful stop period.

```yaml
ports:
  - "8196:8196"             # public P2P
  - "127.0.0.1:8197:8197" # private daemon RPC
  - "127.0.0.1:8199:8199" # private ZMQ
```

Do not publish wallet RPC. For EPoSe, publish a separate restricted daemon listener only after following [EPoSE Service Node Quickstart](../epose/service-node-quickstart.md). Verify the exact tag, digest, embedded `--version`, container user, mounted paths and restart policy before deployment.


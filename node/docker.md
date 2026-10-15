# Docker

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

The official image is `docker.io/qwertycoin/qwertycoin`. The current build packages a verified Linux release archive rather than compiling Core inside the final image. The documented architecture is `linux/amd64`.

```bash
docker pull docker.io/qwertycoin/qwertycoin:latest
docker inspect --format '{{index .RepoDigests 0}}' docker.io/qwertycoin/qwertycoin:latest
```

The `latest` tag is moving. Pulling it does not modify or restart a running container. Record the returned immutable digest and pin it in production. Entrypoint selectors are default/`daemon`, `wallet`, and `wallet-rpc`.

Use separate persistent volumes for blockchain data, wallet material and EPoSe identity. The image runs as UID/GID `10001`; prepare ownership accordingly. Prefer a read-only root filesystem, dropped capabilities, `no-new-privileges`, bounded logs and a graceful stop period.

```yaml
ports:
  - "8196:8196"             # public P2P
  - "127.0.0.1:8197:8197" # private daemon RPC
  - "127.0.0.1:8199:8199" # private ZMQ
```

Do not publish wallet RPC. For EPoSe, publish a separate restricted daemon listener only after following [EPoSE Service Node Quickstart](../epose/service-node-quickstart.md). Verify the exact tag, digest, embedded `--version`, container user, mounted paths and restart policy before deployment.

## Update an existing container

1. Record the current image digest, complete run/Compose configuration, mounts, ports and environment.
2. Pull `docker.io/qwertycoin/qwertycoin:latest`, inspect its digest and read the matching release notes.
3. Stop the existing container cleanly.
4. Recreate it from the new image with the **same** persistent chain, wallet and EPoSE-identity mounts and the same security configuration.
5. Verify the embedded version, network, synchronized height, peers, wallet access where applicable and unchanged EPoSE public identity before removing rollback material.

Never use `docker compose down -v`, delete named volumes or replace a state directory as part of a routine update. A plain `docker pull` is insufficient because existing containers continue using the image from which they were created.

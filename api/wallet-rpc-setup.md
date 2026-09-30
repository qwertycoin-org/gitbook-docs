# Wallet RPC setup

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Published-release track:** `qwertycoin-wallet-rpc v2.0.2`, wallet RPC version 1.31.

Wallet RPC holds authority over the opened wallet. Bind it to loopback/private networking, keep authentication enabled, and serialize access to each wallet.

On a host that also exposes EPoSe restricted RPC on `8198`, use another loopback port such as `18082`. Put options and credentials in a root-owned mode-`0600` file such as `/run/secrets/qwc-wallet-rpc.conf`:

```ini
wallet-file=/srv/qwc-wallets/exchange
password-file=/run/secrets/qwc-wallet-password
daemon-address=http://127.0.0.1:8197
rpc-bind-ip=127.0.0.1
rpc-bind-port=18082
rpc-login=exchange:<generated-secret>
```

Start without placing the secret in process arguments:

```bash
qwertycoin-wallet-rpc --config-file /run/secrets/qwc-wallet-rpc.conf
```

Confirm the package's `--help` output and reject startup if the protected file is absent or has unexpected ownership/mode. Never use `--disable-rpc-login` on a reachable listener.

Startup modes are one fixed `--wallet-file`, JSON generation, or `--wallet-dir` plus lifecycle methods such as `open_wallet`. Do not open the same wallet file from two processes.

Smoke test with HTTP authentication supplied by a protected client file:

```bash
curl --digest --netrc-file /run/secrets/qwc-wallet-rpc.netrc \
  -sS http://127.0.0.1:18082/json_rpc \
  -H 'Content-Type: application/json' \
  --data-binary '{"jsonrpc":"2.0","id":"version","method":"get_version","params":{}}'
```

Use `store` or clean `close_wallet`/`stop_wallet` before shutdown as appropriate. A process kill is not a persistence API.

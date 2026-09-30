# Configuration and ports

> **Verified against:** Core `v2.0.2` and development source `a71c0eb2`, Qwertycoin mainnet, 2026-09-29.

| Listener | Process | Transport | Example bind/port | Exposure | Authentication and role |
| --- | --- | --- | --- | --- | --- |
| P2P | `qwertycoind` | TCP | `0.0.0.0:8196` | Public | Peer protocol; not HTTP |
| Unrestricted daemon RPC | `qwertycoind` | HTTP/JSON/binary | `127.0.0.1:8197` | Private | Configure `--rpc-login`; operator/admin surface |
| Restricted EPoSe probe RPC | `qwertycoind` | HTTP/JSON | `0.0.0.0:8198` | Public only for EPoSe | `--restricted-rpc`; verified restricted route set, not a generic read-only guarantee |
| Wallet RPC | `qwertycoin-wallet-rpc` | HTTP JSON-RPC | `127.0.0.1:18082` on a combined host | Private | Configure `--rpc-login`; possesses wallet authority |
| ZMQ RPC/pub | `qwertycoind` | ZMQ | `127.0.0.1:8199` | Private | Separate protocol/trust boundary |

Both restricted EPoSe RPC and wallet RPC commonly use `8198`, but they are different processes. They cannot share one host port. The `18082` value above is an example override, not a protocol default.

- Prefer loopback binds for unrestricted daemon RPC, wallet RPC and ZMQ.
- Use firewall rules in addition to bind addresses. Account for Docker-published host ports.
- Configure RPC credentials in a protected file or service environment, not shell history.
- Repeated `--seed-node`, `--add-priority-node` and `--epose-v2-discovery-endpoint` options are lists, not allowlists.
- Never expose wallet RPC because an EPoSe guide says to open `8198`.

See [Daemon JSON-RPC](../api/daemon-json-rpc.md) for route-level restricted behavior.

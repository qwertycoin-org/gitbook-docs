# Linux service operation

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Verified configuration model:** Core `v2.0.2`, systemd on Linux.

Create a dedicated non-login account and persistent directory:

```bash
sudo useradd --system --home /var/lib/qwertycoin --create-home --shell /usr/sbin/nologin qwertycoin
sudo install -d -o qwertycoin -g qwertycoin -m 0750 /var/lib/qwertycoin
```

Install verified binaries under an administrator-owned directory such as `/opt/qwertycoin/v2.0.2/bin`. A minimal unit is:

```ini
[Unit]
Description=Qwertycoin daemon
After=network-online.target
Wants=network-online.target

[Service]
User=qwertycoin
Group=qwertycoin
ExecStart=/opt/qwertycoin/v2.0.2/bin/qwertycoind --non-interactive --data-dir /var/lib/qwertycoin --p2p-bind-ip 0.0.0.0 --p2p-bind-port 8196 --rpc-bind-ip 127.0.0.1 --rpc-bind-port 8197 --zmq-rpc-bind-ip 127.0.0.1 --zmq-rpc-bind-port 8199
Restart=on-failure
RestartSec=10
TimeoutStopSec=120
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ReadWritePaths=/var/lib/qwertycoin

[Install]
WantedBy=multi-user.target
```

Install the unit as `root:root` mode `0644`, run `systemctl daemon-reload`, then `systemctl enable --now qwertycoind.service`. Verify process state, synchronized height and peer count after start and restart. For EPoSe, also verify unchanged service identity, reward address and advertised endpoint.


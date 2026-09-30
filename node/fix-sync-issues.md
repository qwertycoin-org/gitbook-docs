# Synchronization troubleshooting

> **Verified against:** Core `v2.0.2`, Qwertycoin mainnet, 2026-09-29.

Diagnose before changing data:

1. Check `qwertycoind --version` and the configured network.
2. Compare local height with multiple healthy peers/explorer observations.
3. Check incoming/outgoing peer counts and the system clock.
4. Check disk, filesystem errors, memory pressure and OOM events.
5. Check firewall/NAT reachability for P2P `8196`.
6. Read logs around the first error, not only later retries.

Common causes are a legacy data directory, blocked seed/peer connectivity, insufficient disk, an uncleanly copied LMDB, wrong permissions or a clock far from network time.

Do not delete wallet files, seeds or EPoSe keystores. Do not import historical CSV checkpoints to suppress a symptom. A normal full resynchronization replaces only blockchain data. EPoSe additionally requires endpoint, identity and lifecycle checks.

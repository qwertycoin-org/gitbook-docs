# Frequently asked questions

> **Verified against:** the latest stable release; exact review revisions are recorded in the [Source and version matrix](../reports/source-version-matrix.md).

## Is this the historical Qwertycoin chain?

No. Current Qwertycoin uses a reset mainnet and Monero 0.18-derived Core. Historical wallets, balances, daemon data, ports, miners and exchange integrations are not automatically compatible. See [Legacy Network Compatibility](../project/legacy-network-compatibility.md).

## Why does my address not begin with `QWC`?

Mainnet primary addresses normally begin with `QWC`, while a valid mainnet subaddress can begin with `Qqb`. Do not edit the text prefix. Use current wallet software or wallet RPC `validate_address` to verify network and address type.

## Are checksums signatures?

No. A checksum proves that a downloaded file matches the published digest; it does not identify who published it. Current release assets are not documented as cryptographically signed publisher artifacts.

## Does a full node earn EPoSe rewards?

Not by itself. A service operator must enable the EPoSe v2 producer, keep a stable protected identity, advertise a reachable restricted endpoint, complete epoch-bound admission, and obtain sufficient canonical receipt evidence. Mining remains responsible for block production and chain selection.

## Must an EPoSe operator stake or mine?

No stake or funded registration transaction is required by the verified implementation. The operator supplies a public primary reward address, but never a wallet spend key or private view key. Mining is independent.

## Why is there no service reward yet?

Admission, frozen membership, service rounds, qualification closure, deterministic selection for a later payout epoch, Coinbase maturity and wallet unlock are separate stages. A local `ready` state or submitted receipt is not proof of canonical qualification.

## Which ports are public?

For a normal public node, expose P2P `8196`. Keep unrestricted daemon RPC `8197` and ZMQ `8199` private. An EPoSe producer additionally exposes a **restricted daemon RPC** listener, commonly `8198`. A separate wallet RPC may also default to `8198`; on a combined host assign it another loopback-only port, such as `18082`.

## Is `get_epose_diagnostics` available?

Yes. The latest stable Core release provides it on the unrestricted, authenticated operator RPC listener. Keep integrations defensive: query `get_version`, handle method-not-found for older nodes and never expose unrestricted daemon RPC publicly.

## Can I restore a wallet without its original restore height?

Yes, but scanning from an earlier height takes longer. A date-derived or conservative height is safer than a height after the first incoming transaction. A seed restores keys, not historical legacy-chain balances.

## Is the Web Wallet Messenger available?

The current official Web Wallet includes the password-gated QMS1 Fast Profile. The browser application has its own publication channel; a Core or GUI release number does not identify the deployed Web Wallet revision.

## Where should integration developers start?

Read [API Overview](../api/overview.md), then [Wallet RPC Setup](../api/wallet-rpc-setup.md) and [Integration Examples](../api/integration-examples.md). Keep exact integer atomic units and reconcile ambiguous spending calls instead of retrying blindly.

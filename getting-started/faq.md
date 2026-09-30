# Frequently asked questions

> **Verified against:** Core `v2.0.2` / development source `a71c0eb2`, mainnet, 2026-09-29.

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

## Is `get_epose_diagnostics` available in `v2.0.2`?

No. It is verified in development source `a71c0eb2` and absent from release source `54308d84` (`v2.0.2`). Release operators must use the release-supported status methods and logs.

## Can I restore a wallet without its original restore height?

Yes, but scanning from an earlier height takes longer. A date-derived or conservative height is safer than a height after the first incoming transaction. A seed restores keys, not historical legacy-chain balances.

## Is the Web Wallet Messenger released?

No. QMS/Messenger work is an open pull request as of the verification date and is not part of the published Web Wallet track.

## Where should integration developers start?

Read [API Overview](../api/overview.md), then [Wallet RPC Setup](../api/wallet-rpc-setup.md) and [Integration Examples](../api/integration-examples.md). Keep exact integer atomic units and reconcile ambiguous spending calls instead of retrying blindly.

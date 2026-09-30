# EPoSE FAQ and troubleshooting

> **Verified against:** mainnet profile at Core `a71c0eb2`, 2026-09-29.

## Why no reward yet?

Check synchronization, enrollment cutoff, canonical admission, snapshot membership, per-round receipts, final qualification, next-epoch selection, output receipt and Coinbase maturity—in that order. A producer-ready state is only the first stage.

## Why did qualification change?

Before the evidence deadline progress is provisional. After closure, the set is immutable for that epoch. A reorganization before finality can change canonical evidence; unavailable evidence must be reported as unknown, not zero.

## Must I mine or stake?

No. RandomX mining and EPoSe are separate. There is no stake or funded registration transaction in the verified protocol.

## Can several nodes use one public IP?

Each identity needs its own stable keystore and a uniquely reachable advertised host/port combination. Multiple nodes may share an IP only if distinct public ports and endpoint descriptors are correctly forwarded; do not reuse one identity/keystore concurrently.

## What happens after downtime or restart?

Docker/systemd should restart the same process with the same persistent chain and identity storage. Missed round deadlines cannot be repaired after the fact. Restart-local diagnostic counters reset; canonical state does not.

## What must I back up?

Back up the EPoSE keystore and wallet seed separately. Blockchain data can be resynchronized. Keep unrestricted RPC credentials/configuration protected, but they do not replace identity backup.

## Fast symptom guide

| Symptom | Check | Likely action |
| --- | --- | --- |
| Not registered | lifecycle/admission canonical inclusion, cutoff | wait for valid next target epoch; preserve identity |
| Endpoint unavailable | public DNS/firewall/TCP `8198`, signed descriptor | fix reachability without exposing `8197` |
| Context/object/signature mismatch | chain tip, genesis, parameter hash, deployed revision | correct mismatched software/network |
| Missing round | committee selection, deadline, distinct canonical receipts | diagnose operational cause; do not duplicate receipts |
| No committee | frozen population size | independent verifiers are required |
| Keystore rejected | owner/type/mode or Windows DACL | repair permissions; never delete the file |
| No wallet credit | prior-epoch selection, Coinbase output, maturity | rescan correct wallet/height and wait for unlock |

The current proof workload is `canonical-object`. Planned storage/messaging services are not current qualification work.

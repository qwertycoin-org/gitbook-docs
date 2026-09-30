# EPoSE admission and lifecycle

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Verified mainnet profile:** EPoSE protocol 2, admission target 18 leading RandomX zero bits.

After synchronization, the producer automatically:

1. creates or loads the bound keystore;
2. signs/relays the endpoint descriptor;
3. builds lifecycle state for the next eligible epoch;
4. performs bounded epoch-bound RandomX admission work;
5. submits/relays accepted lifecycle and admission envelopes;
6. renews descriptor and lease when required;
7. answers eligible canonical-object challenges.

For target epoch `E`, admission work binds the frozen member, target epoch, the block at `start(E-1)`, descriptor sequence, nonce, work hash and lease hash. The lease must be canonically included no later than `start(E)-61`. Mainnet freezes at most 100 identities.

A local successful search or accepted local submission is not enough: the record must become canonical before the inclusive cutoff. A byte-identical duplicate is idempotent; conflicting records are invalid. Descriptor changes have activation/warm-up rules and cannot rewrite an already frozen membership snapshot.

Legacy `register_service_node`, `get_service_node_registration_payload` enrollment, funded transactions and `--service-node*` flags are retired compatibility surfaces, not alternate EPoSe v2 setup methods.


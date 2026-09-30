# EPoSE epochs and qualification

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Compiled mainnet profile:** 720-block epochs, 60-block anchor depth, rounds at offsets 0/200/400, at least 2 successful rounds.

For normal epochs `E > 0`:

```text
start(E)             = 720 * E
end(E)               = start(E) + 719
enrollment_cutoff(E) = start(E) - 61
committee_anchor(E)  = start(E) - 60
evidence_deadline(E) = end(E) - 60
```

| Epoch | Start | End | Enrollment cutoff | Committee anchor | Evidence deadline |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 719 | activation special case | activation special case | 659 |
| 1 | 720 | 1439 | 659 | 660 | 1379 |
| 2 | 1440 | 2159 | 1379 | 1380 | 2099 |
| 15 | 10800 | 11519 | 10739 | 10740 | 11459 |

Do not apply negative pre-epoch formulas to epoch 0. Epoch 0 is activation; epoch 1 is the first service epoch. Membership freezes **before** records in the anchor block are applied, so cutoff-height records can qualify for membership but anchor-height records cannot. Qualification closes **after** records in the inclusive evidence-deadline block are applied.

For each subject and round:

```text
actual_committee = min(9, frozen_population - 1)
required_receipts = ceil(2 * actual_committee / 3)
```

Thus 6 receipts is required only for a full 9-verifier committee. With 4 frozen identities, a subject has 3 possible verifiers and needs `ceil(2*3/3)=2` distinct receipts per passing round. Empty/one-member snapshots cannot form an independent committee and qualify nobody.

Distinct authorized verifier keys count per round; duplicates or receipts from another round cannot fill a missing round. For a full committee:

| Canonical R0 / R1 / R2 | Result after closure |
| --- | --- |
| 6 / 6 / 0 | Qualified |
| 9 / 1 / 0 | Not qualified; only one round passes |
| 0 / 6 / 6 | Qualified |
| 5 / 5 / 5 | Not qualified; no round reaches quorum |

Before the set closes, state is `pending`. After closure it is `qualified` or `not_qualified`. Missing chain/snapshot evidence is `unknown`/unavailable, never zero.


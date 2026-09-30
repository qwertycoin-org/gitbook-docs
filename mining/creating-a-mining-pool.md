# Pool operator integration

> **Verified against:** [Pinned source and release revisions](../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Current production profile:** [Qwertycoin RandomX pool](https://pool.qwertycoin.org/), verified 2026-09-29. The production deployment repository is not publicly readable; this page documents only behavior verified from the live service and its revision-bound operator evidence.

Do not deploy the historical CryptoNight pool repositories. The current pool pins a reviewed MoneroOcean/nodejs-pool revision and applies a deterministic QWC overlay for RandomX, eight decimals, 60-block maturity, wallet receipt attribution and durable payouts.

Required integration gates:

1. Pin backend, native modules, Core and images by immutable revision/digest.
2. Use a dedicated encrypted pool wallet and private authenticated wallet RPC.
3. Keep Stratum, accounting, API, payments and public frontend in separate least-privilege services/networks.
4. Verify `getblocktemplate` seed hash and hashing blob compatibility with the actual mainnet daemon.
5. Run a low-difficulty share canary against a submit-block-denying proxy before live mining.
6. Reconcile a real wallet receipt and accounting result before enabling block submission.
7. Run a recipient-restricted payout canary; record gross debit, net output and actual fee atomically.
8. Stop/reconcile writers before moving SQL, wallet or LMDB state; retain a rollback.

EPoSE Coinbase outputs must not be attributed to miners. The selected backend queries the dedicated pool wallet's actual coinbase receipt. Never use an EPoSE reward wallet or service identity as pool custody.

The repository's `backend/`, `deploy/` and tests are the canonical operator starting point. A wiki page cannot replace its revision-bound runbook.

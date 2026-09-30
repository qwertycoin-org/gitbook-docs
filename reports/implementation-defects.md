# Implementation and release-evidence defects

> These findings were recorded during documentation validation. The documentation does not change runtime behavior or release artifacts to hide them.

## Core README release pointer is stale

At Core `a71c0eb2`, the README still presents an older release-candidate path while GitHub publishes `v2.0.2`. This documentation resolves downloads from release metadata and exact source SHA rather than copying that statement.

## Published v2.0.2 embeds a non-permitting EPoSE gate result

The Linux `v2.0.2` artifact from workflow run `35385285493` identifies source `54308d84`, passes its three binary help/version checks, offline-mainnet smoke, 239 EPoSe C++ tests and 43 EPoSe Python tests. However, the same embedded `BUILD-INFO.json` records:

```text
epose_release_gate.overall_status = no-go
epose_release_gate.stable_permitted = false
epose_release_gate.candidate_bound = false
```

The unresolved entries describe missing candidate-bound security/rehearsal evidence. This conflicts with treating the artifact as having passed that formal release-readiness ledger. It does **not** by itself show that the compiled EPoSe runtime is disabled; it means the stronger release-gate approval must not be claimed from this artifact. The operator pages distinguish executable/test evidence from formal readiness evidence.

## Diagnostics release gap

Development source `a71c0eb2` registers `get_epose_diagnostics`; release `v2.0.2` does not. Documentation labels the method development-only rather than presenting it as a release feature.

## Platform signing gaps

Current Core artifacts are unsigned. Current GUI Windows artifacts are unsigned and the macOS package is ad-hoc signed rather than Developer ID signed/notarized. Checksums provide integrity against the published digest, not publisher identity.

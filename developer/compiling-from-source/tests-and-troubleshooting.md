# Developer tests and troubleshooting

> **Verified against:** [Pinned source and release revisions](../../reports/source-version-matrix.md), Qwertycoin mainnet where applicable, 2026-09-29.

> **Development source:** `a71c0eb2`, verified 2026-09-29.

Configure with `-DBUILD_TESTS=ON`. For EPoSe on Linux:

```bash
cmake --build build/linux --target epose_unit_tests --parallel 2
ctest --test-dir build/linux -R '^epose_unit_tests$' --output-on-failure
(cd source/tests/epose && python3 -m unittest \
  test_release_gate_v2.py test_manifest_v2.py \
  test_reference_model_v2.py test_security_parameter_model.py)
```

The observed release workflow expects 239 EPoSe C++ cases and 43 Python cases at this development baseline. Counts are revision-bound evidence, not timeless constants.

- **Missing submodule:** run `git submodule sync --recursive` and `git submodule update --init --recursive`.
- **OpenSSL/Boost/Qt mismatch:** use the platform recipe and package family used by CI.
- **Link OOM:** reduce compile/link jobs; release CI uses 2/1.
- **Wrong path:** inspect the configured tree; internal targets `daemon`/`simplewallet` produce QWC-named executables.
- **Wrong network:** use explicit isolated fixtures. Generic testnet/stagenet/fakechain flags do not prove EPoSe mainnet behavior.

Never change consensus parameters to accelerate a documentation demonstration and report that as production evidence.

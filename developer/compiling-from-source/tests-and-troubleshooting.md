# Developer tests and troubleshooting

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../../reports/source-version-matrix.md).

> **Development testing:** use an exact reviewed commit and identify it in every result; do not present a default-branch run as a stable release test.

Configure with `-DBUILD_TESTS=ON`. For EPoSe on Linux:

```bash
cmake --build build/linux --target epose_unit_tests --parallel 2
ctest --test-dir build/linux -R '^epose_unit_tests$' --output-on-failure
(cd source/tests/epose && python3 -m unittest \
  test_release_gate_v2.py test_manifest_v2.py \
  test_reference_model_v2.py test_security_parameter_model.py)
```

Test counts can change between reviewed revisions. Require every selected suite to complete successfully and record the exact commit, configuration and resulting counts instead of treating an old count as a timeless constant.

- **Missing submodule:** run `git submodule sync --recursive` and `git submodule update --init --recursive`.
- **OpenSSL/Boost/Qt mismatch:** use the platform recipe and package family used by CI.
- **Link OOM:** reduce compile/link jobs; release CI uses 2/1.
- **Wrong path:** inspect the configured tree; internal targets `daemon`/`simplewallet` produce QWC-named executables.
- **Wrong network:** use explicit isolated fixtures. Generic testnet/stagenet/fakechain flags do not prove EPoSe mainnet behavior.

Never change consensus parameters to accelerate a documentation demonstration and report that as production evidence.

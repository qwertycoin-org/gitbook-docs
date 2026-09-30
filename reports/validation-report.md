# Validation report

> **Status:** Complete. The current-Core documentation, GitBook revision preview, production merge, and public custom domain are validated.

**Validation time:** 2026-09-30 05:22 UTC  
**Environment:** Linux x86_64, Python 3.11.2, Pandoc 2.17.1.1, Git 2.39.5  
**GitBook baseline:** `151a593c09f7443f67bae982b10e1447e19797ca`, tree `bed2eb3cdd497a3a670bd833f66da78465502964`  
**Overhaul base:** root-mapping commit `113c65eb8d45056caaf94d17532e80b261250c74`

- **Publication time:** 2026-09-30 06:15 UTC
- **Published merge:** [PR #3](https://github.com/qwertycoin-org/gitbook-docs/pull/3), `9318e1e340706f63b3a0ae9dc062c1a85da8e6de` on `master`
- **GitBook production revision:** `02wWARNyaYmkQvIWxgCC`

## Matrix

| Gate | Result | Evidence / limitation |
| --- | --- | --- |
| GitBook baseline | Pass | Repository `151a593c09f7443f67bae982b10e1447e19797ca`, tree `bed2eb3cdd497a3a670bd833f66da78465502964`, 60 files |
| Root site mapping | Pass | [PR #2](https://github.com/qwertycoin-org/gitbook-docs/pull/2) merged as `5ebb540685694c61413790098c65f4459573b809`; the only baseline change is one default space (`space-1`) mapped to `./` |
| Content migration | Pass | All 60 baseline files have `Complete` rows: 45 Markdown pages and 15 retained, unreferenced historical media assets |
| Current technical content | Pass | 89 Markdown pages adapted from validated Wiki commit `b4e1f81…`; 28 stale operational URLs are explicit compatibility notices |
| RPC inventory | Pass | Re-extraction is byte-identical: 203 development registrations (107 daemon, 96 wallet) and 201 release registrations |
| Internal links, anchors, structure, stale scan | Pass | `tools/validate_docs.py`: 89 pages, exactly one H1 each, balanced fences, complete `SUMMARY.md`, valid local targets/anchors, evidence headers, config and legacy-command gates |
| Rendering | Pass | Pandoc rendered 89/89 pages as standalone HTML; warnings only supplied filename-derived HTML titles because the smoke command did not pass metadata titles |
| External links | Pass | 449 unique links: 376 immutable Core source links checked locally against pinned trees; 73 remaining HTTPS links returned 2xx/3xx |
| Python helpers | Pass | All five `tools/*.py` files compile with Python 3.11.2; generated cache files are ignored |
| GitBook connector | Pass | GitBook reported both `GitBook (./)` and `GitBook (./) - docs.qwertycoin.org/` successful for PR head `7ad9437…` and revision `sR0DZDqPesn5bmuynDKl` |
| GitBook revision preview | Pass | Preview sitemap contains 88 published pages (`SUMMARY.md` is navigation only); 88/88 returned HTTP 200. Home, EPoSE, RPC inventory, validation report, and legacy compatibility markers were checked directly |
| Current content publication | Pass | Both GitBook production statuses passed for merge `9318e1e…`; the custom domain serves the new home, EPoSE, RPC inventory, validation report, and compatibility pages |
| Production sitemap | Pass | `https://docs.qwertycoin.org/sitemap-pages.xml` contains 88 unique non-preview URLs; 88/88 returned HTTP 200 with no revision URL leaked into the production sitemap |
| Legacy public paths | Pass | Representative old paths redirect to explicit retirement pages; the production home contains current RandomX/EPoSE content and no CryptoNight or Karbowanec/Bytecoin runtime claim |

## Reproducible commands

```bash
python3 tools/generate_migration_manifest.py
python3 tools/validate_docs.py
python3 -m py_compile tools/*.py

python3 tools/extract_rpc_inventory.py \
  --development-core /path/to/core-a71c0eb2 \
  --development-revision a71c0eb2c5b5675f9664fde5738e9cd9ba2e1eac \
  --release-core /path/to/core-v2.0.2 \
  --release-revision 54308d8473dc5606d054c0ba428cfb2d64e758c1 \
  --output-directory /tmp/qwc-rpc-inventory

python3 tools/check_external_links.py \
  --development-core /path/to/core-a71c0eb2 \
  --development-revision a71c0eb2c5b5675f9664fde5738e9cd9ba2e1eac \
  --release-core /path/to/core-v2.0.2 \
  --release-revision 54308d8473dc5606d054c0ba428cfb2d64e758c1
```

The RPC gate additionally compares both generated files byte-for-byte with `rpc-inventory.json` and `api/rpc-inventory.md`. The rendering gate recursively invokes `pandoc --from=gfm --to=html5 --standalone` for every Markdown page.

## Explicit validation limits

- Platform execution and release-evidence limitations from the [validated Wiki report](https://github.com/qwertycoin-org/qwertycoin/wiki/Validation-Report) remain applicable unless rerun here.
- No production node, wallet, EPoSE identity, consensus parameter, RPC behavior, or DNS record is changed by this documentation migration.

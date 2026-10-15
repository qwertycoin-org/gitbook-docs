# EPoSE RPC reference

> **Verified against:** the latest stable release; exact review revisions are recorded in [Pinned source and release revisions](../reports/source-version-matrix.md).

> **Release:** all rows are present in the latest stable Core release. `get_epose_diagnostics` remains an unrestricted, authenticated operator method.

| Method | Transport | Restricted listener | Purpose |
| --- | --- | --- | --- |
| `get_epose_info` | path + JSON-RPC | yes | Epoch, canonical population/qualification and local producer flags |
| `get_epose_diagnostics` | path + JSON-RPC | **no** | Authenticated operator diagnostics |
| `get_service_nodes` | path + JSON-RPC | yes | Bounded canonical descriptor list |
| `get_service_node_status` | path + JSON-RPC | yes | One public service-key lookup |
| `get_service_node_registration_payload` | path + JSON-RPC | yes | Deliberate retired-v1 status; not enrollment |
| `get_epose_epoch` | path + JSON-RPC | yes | Epoch boundaries and counts |
| `get_epose_service_endpoint_v2` | path | yes | Signed local endpoint descriptor |
| `epose_service_challenge_v2` | path | yes | Context-bound canonical-object response |
| `get_service_rewards` | path + JSON-RPC | yes | Height preview using prior closed set |
| `get_epose_block_reward` | path + JSON-RPC | yes | Verify/map one canonical historical block |
| `submit_epose_envelope` | path | **no** | Admit/relay one envelope; private operator path |

Path calls POST JSON to `/<method>` without a JSON-RPC wrapper. JSON-RPC calls use `/json_rpc`. Exact fields and linked schemas are in [RPC Inventory](rpc-inventory.md).

`get_service_nodes` is bounded and reports total/returned counts. Endpoint/challenge HTTP success is not consensus evidence. `submit_epose_envelope` local acceptance is not canonical inclusion. Reward attribution must use the verified mapping, never output position.

Diagnostics additionally require configured RPC login and return no data otherwise; see [Monitoring and Diagnostics](../epose/monitoring-and-diagnostics.md).

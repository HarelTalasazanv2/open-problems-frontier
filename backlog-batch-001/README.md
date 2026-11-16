# Audited M12 backlog batch 001

Fourteen historical mathematical claim records pass at the explicitly audited scopes. Their historical dates are retained; this is verification, not fourteen new discoveries.

| Record | Audited scope |
|---|---|
| C186 | Every degree is at least six for the stated 17-vertex noK5/noI4/maxdegree-seven graph domain. CNF encoding bridges are not reviewed. |
| C187 | Necessary singleton/pair restrictions and triangular-prism neighborhood exclusion. |
| C188 | All32,768six-vertex masks;22,484admissible members in84complete orbits, all60,480oriented images, complete filters leaving63classes. |
| C189/C190/C191 | Neighborhood exclusions684,617,632, with exact identities/cones and signed equality witnesses where appropriate. |
| C192 | All256binary weight decisions for four five-edge cases; no exclusion by that particular test. |
| Manual E5 application | All24individual capacity bounds and the separate662aggregate cut; exclusions659,662,692,920. Slide/source-coverage claims are not reviewed. |
| C193 | Mixed-type common-neighbor exclusion619, including a feasible older relaxation. |
| Class633/635/655 | All retained exclusion certificates and specified feasible relaxation witnesses. The C655minimum-degree dependency is explicit. |
| C195/C196 | Exclusions663,671; all36,720C196predicate/template relabeling decisions. |

[Proof reading editions](proofs/) · [primary review result](verification_result.json) · [extended result](extension_result.json) · [complete set-update chain](chain_result.json) · [source identities](SOURCE_IDENTITIES.json) · [references and credit](REFERENCES.md).

## Reproduce

Use Python3.10or newer and the standard library from this directory:

```sh
python3 -B verify_batch.py
python3 -B -OO verify_batch.py
python3 -B verify_extension_v2.py
python3 -B -OO verify_extension_v2.py
python3 -B -OO verify_chain.py
```

These commands only read data and print results. They do not install packages, run external Lean/source code, change repository content or publish. The tested interpreter was Python3.12.14.

The first checker reconstructs11models, verifies eight exact infeasibility certificates and three feasible relaxation points, and performs the complete C186/C187/C188/C196 finite checks. Its13selected invalid controls pass in both recorded modes. The extension checks all pair support/equality rows,256binary candidates,24capacity decisions and the aggregate/mixed certificates; seven selected invalid controls pass in both recorded modes. The set-chain checker validates13historical updates, all exact removed members and adjacent raw identities through C197. These are scoped controls, not exhaustive software or external mathematical review.

The final49classes/14,872labeled neighborhoods remain unresolved. Feasible relaxation points are not graphs. Finite rule failures are not universal impossibility statements. No full graph/Ramsey solution, novelty, blind review, expert review, Lean formalization or empirical physics result is claimed.

Historical receipt fields inside extended_data are retained source evidence. Only verification_result.json, extension_result.json and chain_result.json summarize this new audit; old test counts are not new executions.

# Backlog batch002 — eight published mathematical audits

Eleven of the103historical records pending after batch001 were audited: eight passed for public release; three passed mathematics but their input-dependent packages remain held for unresolved source redistribution admission. Across118candidates,23are published,3are held after review and92remain individually unaudited. These are saved-result audits, not new discoveries or solved open problems.

| Historical record | Audited statement | Evidence |
|---|---|---|
| C149 | PROVED: rational Hodge classes on a connected smooth complex projective surface times P^r are algebraic, all r>=0 | [Proof](SURFACE_PRODUCT_PROOF.md), [analytic audit](ANALYTIC_AUDIT.json) |
| C150 | PROVED: field/identity-adjoint isometry span lemma; K3 application CONDITIONALLY_PROVED under explicit unsupplied geometric hypotheses | [Proof](ISOMETRY_SPAN_PROOF.md), [analytic audit](ANALYTIC_AUDIT.json) |
| C174 | CERTIFIED_RANGE: singular double-plane counts313and547over F17/F23; resolution counts568and892 | [Proof](FINITE_COUNT_PROOF.md), [certificate](counts/AUDIT_CERTIFICATE.json) |
| C175 | CERTIFIED_RANGE: singular83,881/resolved88,216over F17[u]/(u²-3) | [Proof](FINITE_COUNT_PROOF.md), [certificate](counts/F289.json) |
| C176 | CERTIFIED_RANGE: singular280,729/resolved288,664over F23[v]/(v²-5) | [Proof](FINITE_COUNT_PROOF.md), [certificate](counts/F529.json) |
| C178 | PROVED: the two literal quartics are Q-irreducible and have no root p*zeta for any root of unity | [Proof](QUARTIC_PROOF.md), [certificate](QUARTIC_AUDIT.json) |
| C170 | PROVED: the exact excess identity for every finite simple graph, including n=0 | [Proof](EXCESS_IDENTITY_PROOF.md), [counting audit](GRAPH_COUNTING_AUDIT.json) |
| C172 | PROVED: high-edge covering for46vertices with degrees21..24at explicit thresholds; Ramsey-type corollary retains its extra hypotheses | [Proof](TYPED_COVERING_PROOF.md), [counting audit](GRAPH_COUNTING_AUDIT.json) |

The new finite checker compares all365,042canonical projective base points using root multiplicities versus independently written norm/Legendre arithmetic. It also compares every byte of the two historical extension payloads in their original charts.36negative controls are detected. The quartic consumer checks24divisor cases and rejects seven malformed certificates. These exact integer/Fraction checks do not replace the analytic proofs or their declared standard-theorem dependencies.

## Reproduce the uploaded evidence

From this directory with Python3.12or later, using only its standard library:

```sh
python3 -B -OO finite_count_audit.py --output counts --verify
python3 -B -OO quartic_audit.py --output quartic_certificate.json --verify
python3 -B -OO graph_counting_check.py --certificate GRAPH_COUNTING_AUDIT.json
```

These commands read the saved data and print fresh verdicts. They do not need the historical workspace. To redo the historical per-byte comparison, the count checker additionally accepts `--historical-root` pointing to the original Open Problems Frontier project. Fresh generation requires a new output directory and omitting `--verify`, preserving saved certificates.

The [portable graph counting checker](graph_counting_check.py) checks the76small graph cases and four exact threshold margins, with the universal arguments supplied by the analytic proofs.

The per-fibre ASCII-hex files are [F17](counts/F17.hex), [F23](counts/F23.hex), [F289](counts/F289.hex) and [F529](counts/F529.hex). The [quartic payload](quartic_certificate.json), [count checker](finite_count_audit.py), [quartic checker](quartic_audit.py) and [release audit](RELEASE_AUDIT.json) are included. [References](REFERENCES.md), [credit text](ATTRIBUTION.txt) and [input lineage](INPUT_LINEAGE.json) preserve authorship and provenance.

No full Frobenius-factor identification, Picard-rank/RM reproduction, actual K3 tensor algebraicity, global Hodge resolution, novelty, external human review or formal verification is claimed.92historical records remain individually unaudited;3additional reviewed graph packages are held locally. No source-input-dependent graph package is included here. Newer local graph work is separate from this historical batch.

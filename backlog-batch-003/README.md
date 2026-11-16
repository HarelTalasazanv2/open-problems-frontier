# Backlog batch003 — nine additional audits and three graph releases

Nine of the92previously unaudited records pass at their stated scopes. Three previous graph publication holds are resolved for an output-only release requiring the exact external seed. The underlying source-data redistribution question remains unresolved: curator input files are excluded. After this release,35of118historical candidates are published and83await individual audit.

| Historical records | Exact supported statement | Evidence |
|---|---|---|
| C063 | PROVED: no distinct p>=5shifted-prime cover with all moduli dividing360; known p>=3boundary witness checked | [Proof](PERIOD_BOUND_PROOF.md), [audit](PERIOD_AUDIT_V2.json) |
| C064 | CERTIFIED_RANGE: complete393119period density screen; first survivor55440and exactly28survivors below393120 | [Proof](PERIOD_BOUND_PROOF.md), [certificate](period_certificate_v2.json) |
| C065 | CERTIFIED_RANGE: all28survivors excluded by parity/14400CRTcases, hence exact LCM>=393120 | [Proof](PERIOD_BOUND_PROOF.md), [certificate](period_certificate_v2.json) |
| C146 | CERTIFIED_RANGE: all subsets of fixed U877fail to cover, exact beta<199983/200000 | [Proof](U877_PROOF.md), [candidate](sieve_candidate.json), [audit](SIEVE_AUDIT.json) |
| C147 | PROVED: stated finite noncovering criterion, including zero-mass and endpoint branches | [Proof](FINITE_SIEVE_PROOF.md), [checks](SIEVE_AUDIT.json) |
| C158 | PROVED: eight positive integer unit-fraction identities cover all n>=2outside1,49mod120 | [Proof](UNIT_FRACTION_PROOF.md), [candidate](unit_fraction_candidate.json), [audit](UNIT_FRACTION_AUDIT.json) |
| C111 | PROVED: bounded-query decision-to-search reduction under explicit correct-oracle/reduction assumptions | [Proof](DECISION_SEARCH_PROOF.md), [analytic audit](COMPLEXITY_AUDIT.json) |
| C112 | PROVED: decidable language outside uniform Pwith two noninput gates per positive length; polynomial generator would imply P | [Proof](UNIFORMITY_PROOF.md), [analytic audit](COMPLEXITY_AUDIT.json) |
| C113 | PROVED: for the one explicitly defined unary-clock oracle A, ordinary EXP=P^A=NP^A | [Proof](EQUALITY_ORACLE_PROOF.md), [analytic audit](COMPLEXITY_AUDIT.json) |
| C168/C169/C171 | Fixed external42vertex seed passes; no one-vertex extension; complete degree22centre counts108,107,107 | [Proof](GRAPH_PROOF.md), [output certificate](GRAPH_OUTPUT_AUDIT.json), [hold/profile decision](HOLD_RESOLUTION.json) |

All statuses are restricted to these statements. The unit-fraction complement is not a counterexample set;49has a solution. Density is only necessary for covering; finite exclusions do not settle unrestricted existence. The complexity proofs do not give ordinary P=NP/P!=NP. The graph proof concerns one exact source seed, not all42/43vertex graphs. Source references and precise assistance roles are in [REFERENCES.md](REFERENCES.md) and [ATTRIBUTION.txt](ATTRIBUTION.txt).

## Reproduce the self-contained arithmetic checks

With Python3.12or later and only its standard library, from this folder:

```sh
python3 -B -OO period_bound_check_v2.py --certificate period_certificate_v2.json --verify
python3 -B -OO sieve_check.py --candidate sieve_candidate.json --certificate SIEVE_AUDIT.json --verify
python3 -B -OO unit_fraction_check.py --candidate unit_fraction_candidate.json --certificate UNIT_FRACTION_AUDIT.json --verify
```

The analytic proofs carry all universal quantifiers; finite controls do not replace them. The new programs independently check complete memberships, exact polynomial coefficients and strict rational inequalities. No source program, optimizer, SATsolver or float proof-path is executed.

## Reproduce the graph proof with its external input

This graph package omits the curator's raw seed, complete adjacency/neighborhood lists and original CNFinput. Obtain the exact first graph6record through an applicable authorized source; its145bytes excluding newline must hash to7fda67be9b2d99b376c0f4e8188edf004599e64d5541331fbdd2d599246a067d. Set OPF_EXTERNAL_SEED to that local file, then run:

```sh
python3 -B -OO graph_outputs_check.py --seed "$OPF_EXTERNAL_SEED" --resolution resolution_proof.json --certificate GRAPH_OUTPUT_AUDIT.json --verify
```

The checker performs no download, requires the exact input, regenerates the CNFand checks every saved resolution step. Missing/wrong seed and corrupt proof fail. [Project-generated resolution certificate](resolution_proof.json). Local reproduction used the existing pinned input; the public package is explicit about its external dependency and does not represent a new source-data license grant.

This audit is same-actor/nonblind; no external human review, formal verification, novelty, global mathematical solution or measured performance gain is claimed. [Claim/admission summary](CLAIM_AUDIT.json).

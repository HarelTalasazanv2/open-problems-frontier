# Three fixed-seed graph claims: project outputs with external input

**CERTIFIED_RANGE(C168/C171) and restricted PROVED/CERTIFIED_RANGE(C169):** the exact first42vertex seed selected in the historical record has no clique5or independent5; it has no one-vertex extension retaining those properties; and its complete degree22centre family has neighborhood edge counts108,107,107. These are one-seed results, not a new construction, complete42graph catalogue, maximum-order theorem or global Ramsey resolution.

## Input and publication boundary

The required external graph6record has145bytes without its newline and SHA-256

7fda67be9b2d99b376c0f4e8188edf004599e64d5541331fbdd2d599246a067d.

Its historical source is the first record of [McKay's r55_42some.g6collection](https://users.cecs.anu.edu.au/~bdm/data/r55_42some.g6). The source page credits Exoo and McKay/Radziszowski for the constructions/expansion. The curator endpoints timed out in this audit. The raw graph6record, complete adjacency/neighborhood lists, source HTML and original CNF input are not included here. No source-data redistribution permission or license has been inferred.

This release contains our mathematical argument, checking implementation, derived result summary and project-generated resolution proof. Its reproduction requires the exact externally supplied seed. The checker does not download it and refuses missing/wrong input. Local review used the hash-matching source already held under the project; publication of that source remains outside this package. The earlier three publication holds are resolved for this output-only profile; the underlying source-data redistribution question remains unresolved.

## Known witness and extension encoding

The [checker](graph_outputs_check.py) strictly decodes all861graph6edge bits in column-major order, including length/zero-padding validation. It visits every one of850668five-subsets and counts all ten pairs. The [result histogram](GRAPH_OUTPUT_AUDIT.json) has zero entries at0and10edges, establishing the known noK5/noindependent5property for this exact source. Five hand-labeled graph6examples challenge the decoder's labeling; no other curator seed is inferred to have been read.

For each clique four-set put the negative clause forbidding a new vertex adjacent to all four. For each independent four-set put the positive clause forbidding nonadjacency to all four. Every forbidden new five-set must contain the new vertex, so these clauses are equivalent to all admissible one-vertex extensions. This proof handles every assignment of42adjacency bits; it does not sample2^42choices.

All111930four-subsets yield1141clique clauses,1172independent clauses and109617mixed sets. The2313-clause CNF is regenerated from the external seed at verification time. Its exact SHA-256must be

5934d7346d6365809788730caa203e1655542f5c4a051a6c5019facaa77ee17e.

No original CNF file is shipped. The regenerated clauses' signs, order and membership are checked before consuming the project-generated [resolution proof](resolution_proof.json).

## Refutation and hereditary corollary

Every one of282binary resolution steps has two earlier parent clauses, opposite signed pivot literals, and exactly the union of nonpivot literals as its child. If an assignment satisfies both parents, its two possible pivot values imply it satisfies that child. Induction makes every derived clause a consequence of the input. The final clause2595is empty, hence no assignment satisfies the CNF. The iff encoding excludes all one-vertex extensions of this seed.

If a larger graph avoiding both forbidden five-sets contained an induced copy of this seed, keeping that copy and any one extra vertex would produce the excluded43vertex extension. Thus no such larger graph contains the seed as an induced subgraph. This is vertex-maximality of one seed, not global maximum order or a complete classification.

## Complete centre family and verification limits

Every one of42degrees is scanned; exactly zero-based vertices39,40,41have degree22. All231pairs of each neighborhood are counted, giving108,107,107edges. None of this three-case family has113edges. The result does not exclude all22vertex/113edge graphs or resolve an uninspected source archive.

The consumer rejects18internal format/encoding/resolution defects, including missing/duplicate clauses, wrong pivots, lost nonpivot literals and a false refutation of a truth-table SATfixture with an updated hash. The new external-input interface additionally accepts the healthy pinned input and rejects missing seed, wrong seed and corrupt resolution through its actual CLI. Its implementation is adapted from the prior same-actor audit; this is interface reproduction, not new algorithmic independence. No new SATsearch, blind/external human review or formal verification occurred.

[Output certificate](GRAPH_OUTPUT_AUDIT.json), [publication-profile decision](HOLD_RESOLUTION.json), [references and credit](REFERENCES.md).

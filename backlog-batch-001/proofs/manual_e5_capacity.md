> Public reading edition for the audited mathematical claim. Historical phase counts below are not current global status. The original proof is retained unchanged in the project. Local navigation was adapted for this package; credit is in [REFERENCES.md](../REFERENCES.md). CNF/SAT encodings, slide-coverage counts, novelty and external/formal review are outside this audit.

# Three restricted neighborhood exclusions by pair capacity

**Claim ceiling — PROVED at restricted local scope.** A simple graph on17vertices with noK5, no independent four-set and maximum degree at most7cannot have C188neighborhood class659,692or920at its selected degree-six root, using the named C186degree reduction. This does not decide the full17vertex target or the parent global Ramsey problem.

Let A be the six neighbors of the root and B the ten remaining vertices. The locally established degree reduction gives every full degree at least6. Bhas no independent triple, since the root would extend it to an independent four-set. For uinB, its nonneighbors inBform a clique of size at most4, so degree_B(u)>=5. Its full degree at most7therefore leaves at most two Aneighbors.

Every Avertex a requires at least5-degree_A(a) neighbors inB. Each of the selected Agraphs has five edges, so total A-to-Bincidence is at least30-10=20. Ten Bvertices with at most two Aneighbors give at most20. Thus every Bvertex has exactly two Aneighbors, and t[a]=5-degree_A(a) for each a. This is the C189saturation argument, not an assumption of histogram sufficiency.

For each unordered pair S of A, let x[S]>=0count Bvertices whose exact Aneighborhood is S. If an independent triple QofAis disjoint fromS, then Qand any Bvertex of that type form an independent four-set. Thus that type is forbidden and x[S]=0. This gives the complete necessary support rule; a permitted type is not thereby realizable.

Each fixed nonempty type S forms a clique inB: AminusScontains four vertices and has a nonedge, since Ahas noK4(the root would extend a K4toK5). Two nonadjacent Bvertices of typeSwith that nonedge would form an independent four-set. If Sis an edge ofA, three vertices of its Bclique together with Sform K5. Consequently x[S]<=2. If Sis a nonedge pair, four of its Bclique vertices plus either endpoint of Sform K5, so x[S]<=3. This independently rederives the C187cap; it does not replace3by2on nonedges.

Use local Alabels0through5and lexicographic edge-mask encoding, as in the source ledger. Each selected vertex has just one permitted incident type, and that type is an Aedge:

| Class | Exact Aedges | Vertex a | Only permitted incident type | t[a] | Capacity |
|---|---|---:|---|---:|---:|
|659|01,02,05,14,23|1|14|3|2|
|692|03,05,12,14,23|0|05|3|2|
|920|04,05,14,15,23|2|23|4|2|

For completeness, every other incident pair is forbidden by the following explicit disjoint independent triple:

| Class | Forbidden pair → independent triple |
|---|---|
|659|01→245;12→034;13→245;15→034|
|692|01→245;02→135;03→245;04→135|
|920|02→345;12→345;24→013;25→013|

Each triple can be checked directly against the edge list. The remaining pair in each row meets every independent triple, as verified by complete enumeration; the contradiction itself needs only that all other incident types are forbidden. Hence659requires x14=3but x14<=2;692requires x05=3but x05<=2;920requires x23=4but x23<=2. All are impossible. No solver, approximation, strict-feasibility theorem or integrality search is needed.

The saved certificates also express each contradiction using nonnegative slack variables. Add x[S]+s[S]=cap[S] to the necessary occupancy equations, where s[S]>=0. Sum cap rows incident to a, subtract its degree row, and add the relevant forbidden zero rows to cancel forbidden columns. All resulting column coefficients are nonnegative, while the right side is capacity minus demand: -1,-1or-2. This contradicts nonnegativity by elementary multiplication of the equations. The exact consumer checks every emitted certificate, including additional decisive vertices, and a separate implementation checks the actual integer dot products.

The four-case audit covers exactly659,662,692,920and all six vertex bounds each. Case662passes these24individual-capacity tests; no coupled nonnegative/integer occupancy or Bgraph feasibility is inferred. All720relabelings of each excluded graph are checked against the original orbit ledger. The excluded orbits have360,360and45distinct labeled members, respectively, and are disjoint. Removing exactly765members from the prior17,437leaves16,672labeled neighborhoods in57classes. This is a filtered local residual, not an extendability classification or a global census.

The exact C186degree dependencies are `artifacts/m12_vertex_symmetry_cycle186/PROOF_REFINEMENT_02.md`(minimum degree6) and `PROOF_CASE_SELECTION_03.md`(existence of a degree6root). Its original `PROOF.md` proves an earlier, weaker degree floor and is not a substitute for those addenda. The refinement was read and checked: degrees below4contradict the Bdegree bound; degree4has no cross edges and yields an independent four-set; degree5partitions eleven Bvertices into three cliques of size at most3. Parity then supplies a degree6root. The C187structural argument, C189saturation reduction, complete C188ledger and unchanged C192input family are also pinned dependencies.

Generic exact arithmetic is reused from the explicit-check consumer; the new confirmation uses different graph representation and integer-dot-product code but shares the actor, specification, inputs and exposed expected result. Neither agreement nor malformed-input test counts establish universal software correctness. The broader target and novelty remain unresolved.


[Batch verification](../verification_result.json) · [Extension verification](../extension_result.json) · [Exact exclusion chain](../chain_result.json).

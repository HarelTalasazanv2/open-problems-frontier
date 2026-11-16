> Public reading edition for the audited mathematical claim. Historical phase counts below are not current global status. The original proof is retained unchanged in the project. Local navigation was adapted for this package; credit is in [REFERENCES.md](../REFERENCES.md). CNF/SAT encodings, slide-coverage counts, novelty and external/formal review are outside this audit.

# Degree-six occupancy is necessary but not a completion

This proof fixes root0, A={1,...,6}, B={7,...,16}. The graph is simple, has noK5/no independent four-set, maximum degree<=7, and root degree6. The named C186lemma supplies minimum degree>=6. The results below concern necessary conditions and one restricted neighborhood class, not a full decision of the original target or a new global Ramsey result. Review is internal, with no novelty, blind, external or formal verification claim.

## Necessary aggregate constraints

The induced graph on A has noK4, since root0 would extend one to K5; it has no independent four-set. The induced graph on B has no independent triple, since root0 would extend one to four, and has noK5. For u in B, its B-nonneighbors form a clique of size<=4, or two of them with u would be an independent triple. Therefore degree_B(u)>=9-4=5 and u has at most2neighbors in A.

Let n[S] count Bvertices with exact A-neighborhood S, |S|<=2. Counts are nonnegative integers summing to10. Write t[a]=sum_{a in S}n[S]. The full degree of a is1+degree_A(a)+t[a], so max(0,5-degree_A(a))<=t[a]<=6-degree_A(a). This is a total-degree condition, not a claim about degree inside B.

If T is an independent triple of A, every occupied S meets T, or a Bvertex extends T to four. If a,b are nonadjacent in A, the Bvertices adjacent to neither form a clique: a nonadjacent pair among them would join a,b to an independent four-set. At most4Bvertices therefore avoid a,b.

## A concrete feasible histogram that cannot complete

Take A to be the triangular prism: triangles123and456, matching14,25,36. It is3regular, with noK4 and no independent triple. Set n[empty]=1 and n[S]=1 for each of its9edges. All t[a]=3, so each Avertex would have full degree7. For any nonedge a,b of A, the two three-element B-neighborhoods are disjoint, so exactly4Bvertices avoid both. Independent-triple constraints are vacuous. Thus this histogram satisfies every preceding aggregate condition.

Nevertheless its empty-type Bvertex u cannot occur in a completion. For any other Bvertex w, its A-neighborhood S has size<=2. The set A minus S has at least4vertices and cannot be a clique, because A has noK4. Choose nonadjacent a,b there. Both u and w avoid a,b; hence u,w must be adjacent or form an independent four-set with a,b. Consequently u is adjacent to all9other Bvertices, contradicting maximum degree7. The independently checked conditioned unit certificate, if successful, certifies only this histogram realization and its explicit A/cross units.

This is not a counterexample to the full target. It rejects the inference from the named feasible necessary-condition vector to a graph completion. Different B-type labelings of the same histogram are equivalent by Bvertex permutations, but no other histograms are decided by that conditioned certificate alone.

## Structural strengthening valid for every A

The empty-type argument did not use the prism except for feasibility of the example. For any allowed six-vertex A with noK4, any empty-type Bvertex would have9forced Bneighbors. Thus n[empty]=0 is necessary.

For a fixed nonempty S of size<=2, the set A minus S has at least4vertices and contains a nonadjacent pair a,b. All Bvertices of type S avoid a,b and must form a clique. If |S|=2 and S is an edge of A, at most2vertices can have type S:3such Bvertices together with S would give K5. For a singleton or a nonedge pair S, at most3vertices have that type, since any one member of S with4of those clique vertices would give K5. These are integer multiplicity bounds, not sufficiency claims.

## Excluding the entire prism neighborhood

Now suppose G[A] is the prism in an actual target graph, with arbitrary occupancy counts. Each Avertex has induced degree3 and hence t[a]<=3. For every nonedge a,b of A, at least6Bvertices are adjacent to a or b. Since t[a]+t[b]<=6, both equal3 and their B-neighborhoods are disjoint. Every prism vertex has a nonedge partner, so all six t[a]=3. No nonedge-pair type is occupied. The total number of A-to-B incidences is18.

There are no empty types by the preceding lemma. Each Bvertex has one or two Aneighbors. If n1,n2 are their respective numbers, n1+n2=10 and n1+2n2=18; therefore n1=2,n2=8. In particular a singleton-type Bvertex u exists. Let its sole Aneighbor be x, and let L be the triangle of the prism containing x.

Consider any other Bvertex w with A-neighborhood S. If A minus({x} union S) contains a nonedge a,b, then u,w must be adjacent by the same independent-four-set argument. If that remaining Aset has>=4vertices, it contains a nonedge because A has noK4. If it has3vertices and is a clique, it must be one of the prism's only two triangles. It cannot be L, because x was removed. It must therefore be the other triangle, which forces S=L minus{x}. This is the only possible exception to adjacency with u.

The exceptional type is an edge of A and has multiplicity at most2. Thus u is forced adjacent to at least9-2=7other Bvertices. It also has its one Aneighbor, so its full degree is at least8, a contradiction. No singleton type can exist, contrary to n1=2.

There is consequently no17vertex noK5/noI4/maxdegree7 graph whose selected degree6root has a triangular-prism neighborhood. Relabeling of the six Avertices preserves this restricted statement. The finite permutation check verifies the explicit prism's shape/orbit, not all possible Agraphs. The original canonical degree6input remains undecided because other neighborhood classes are not excluded.

## Adversarial boundaries

Empty, singleton and pair types have distinct roles. Do not apply the pair-edge cap2to nonedge-pair types without proof, or silently assume every Bvertex has2Aneighbors. The aggregate witness intentionally violates the stronger empty-type lemma while satisfying the original relaxation. The singleton contradiction uses the prism's exactly two triangles and t[a]=3, so it is not imported unchanged into an arbitrary Agraph. The maximum-degree bound counts AandBneighbors together. An UNSAT certificate for appended assumptions must not be read as a proof for the unconditioned base. All of these boundaries are explicit in the controls and claim ledger.


[Batch verification](../verification_result.json) · [Extension verification](../extension_result.json) · [Exact exclusion chain](../chain_result.json).

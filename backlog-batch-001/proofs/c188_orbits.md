> Public reading edition for the audited mathematical claim. Historical phase counts below are not current global status. The original proof is retained unchanged in the project. Local navigation was adapted for this package; credit is in [REFERENCES.md](../REFERENCES.md). CNF/SAT encodings, slide-coverage counts, novelty and external/formal review are outside this audit.

# Exact neighborhood orbit coverage and necessary degree filters

Claim ceiling: a complete computed partition covers precisely the stated32768mask domain filtered by noK4/noI4. It is a finite classification, not a17vertex decision or a new global Ramsey result. The necessary inequalities below have elementary proofs under named C186/C187target assumptions. No novelty, external, blind or formal verification is claimed.

## Orbit coverage

Number unordered pairs of{0,...,5} lexicographically and encode a graph by its15edge bits. A permutation p is interpreted new-to-old: the permuted graph has edge{i,j} exactly when the original has edge{p[i],p[j]}. This bijects vertex subsets and preserves complete/empty four-sets, degrees, independent triples and edge count. Permutations include the identity, inverses and compositions, so being connected by such a permutation is an equivalence relation on labeled graphs.

For any current least unassigned admissible graph r, the complete720permutation images give exactly its orbit. Every image is admissible. Orbits of different representatives are disjoint: if an image were shared, composing the respective inverse permutations would identify the representatives in one orbit, which would already have been removed. After removing all generated orbit members, repeating the rule either terminates with no admissible masks left, or has an explicit unassigned cursor. Only the former supports a complete-classification verdict. The union must be independently checked against the directly recomputed entire predicate set; counts alone do not establish this.

Since representatives are selected in increasing mask order and whole orbits removed, each selected representative is its orbit's least mask. The saved720images bind the declared permutation orientation. Using inverse permutations everywhere produces the same orbit as a set, but may give incorrect labeled transport witnesses; a consumer must check each associated image, not mistakenly treat any inverse-convention implementation as a different orbit classification. The stabilizer count is the number of recorded permutations whose image equals r. Every recorded image fiber is independently counted, and orbit size times stabilizer count must equal720.

## Contextual target and transferred assumptions

The named C186local argument selects a degree6root0 in any possible17vertex noK5/noI4/maxdegree7 graph; all its vertices have degree6or7. Write A=N(0), |A|=6, and B=the other10vertices. The ledger's six labels0,...,5are local A-labels, corresponding to global labels1,...,6; the distinguished global root is not a ledger vertex. G[A] has noK4 and noI4. C187proves that every Bvertex has one or two Aneighbors, with no empty type. These are inherited local dependencies, not conclusions from the finite six-vertex classification.

Let t[a] count A-to-Bedges incident to a in A, and let k[a]=degree_A(a). The full degree is1+k[a]+t[a], so5-k[a]<=t[a]<=6-k[a]. Here k[a]<=5, so the lower bound is nonnegative. Let T=sum_a t[a]. Summing gives30-2e(A)<=T<=36-2e(A). Counting the same cross edges at B and using one-or-two neighbors gives10<=T<=20. Therefore e(A)>=5 and e(A)<=13. This is necessary only; dense noK4graphs may have sharper independent bounds, but no such extra import is needed here.

## Nonedge degree-sum filter

If a,b are nonadjacent in A, their common nonneighbors in B must form a clique: a nonadjacent pair among them would give an independent four-set with a,b. This clique has size<=4. Thus at least6of the10Bvertices are adjacent to a or b. Consequently

6 <= |N_B(a) union N_B(b)| <= t[a]+t[b] <=12-k[a]-k[b].

It follows that k[a]+k[b]<=6 for every nonedge of A. A sum strictly greater than6 excludes the entire neighborhood class. Equality does not exclude it by this rule; changing the test to>=6 is an invalid strengthening.

## Independent-triple degree-sum filter

If Q is an independent triple of A, each Bvertex has at least one neighbor in Q, or it extends Q to an independent four-set. Counting cross incidences into Q gives10<=sum_{a in Q}t[a]. The individual upper bounds give sum t[a]<=18-sum k[a]. Therefore sum_{a in Q}k[a]<=8. A sum strictly greater than8 excludes that class. Neither this bound nor aggregate feasibility constructs the internal graph on B.

## Sanity cases and inherited prism exclusion

The six-cycle has induced degree2at every vertex. It has6edges, noK4/noI4, every nonedge degree sum4, and every independent triple degree sum6. It survives all three inequalities. This explicit case prevents any all-target-empty inference from the filters alone.

Three disjoint edges have3edges and noK4/noI4, so fail the edge-budget filter. K2,2,2has12edges and degree4at every vertex; each missing within-part edge has degree sum8and fails the nonedge bound. K3,3is3regular and has independent triples with degree sum9, failing the triple bound. The triangular prism is3regular with9edges and no independent triple; its nonedge sums equal6, so none of the new strict-violation rules excludes it. It is removed only by the separate, byte-pinned C187complete prism argument. Its complement is a six-cycle, not another prism, and must not inherit that exclusion.

All expected healthy/control objects are fixed by their explicit edges and independently checked degrees.

## Interpreting the finite output

Every filter and the prism condition is invariant under relabeling, so a correctly witnessed violation at a representative excludes its whole orbit for the contextual17vertex target. Record all exact reasons, including overlaps. A class excluded by two rules is still one excluded class; summed per-rule totals are not the unique exclusion count. The classification auditor also recomputes member-level reasons independently so a correct overall Boolean cannot hide an incorrect threshold or a missing overlapping reason.

The remaining representatives form a complete residual list relative to precisely these rules and the inherited prism result. They are not asserted to admit occupancies, a Bcompletion or an actual17vertexgraph. No source census or global R(5,5)value is reproduced. The next test must address a concrete remaining obstruction, not inflate this local enumeration into a probability of solving it.


[Batch verification](../verification_result.json) · [Extension verification](../extension_result.json) · [Exact exclusion chain](../chain_result.json).

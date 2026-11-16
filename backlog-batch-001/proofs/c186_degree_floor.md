> Public reading edition for the audited mathematical claim. Historical phase counts below are not current global status. The original proof is retained unchanged in the project. Local navigation was adapted for this package; credit is in [REFERENCES.md](../REFERENCES.md). CNF/SAT encodings, slide-coverage counts, novelty and external/formal review are outside this audit.

# A stronger local bound: every degree is six or seven

This addendum extends, rather than alters, the earlier Cycle186 proof. The exact claim is: if a simple graph G on17vertices has noK5, no independent four-set, and maximum degree at most7, then every vertex has degree at least6. Hence the original counterexample existence question reduces to the two canonical root-degree branches6and7. Neither surviving branch is decided here. This is a complete elementary local argument, with internal review and finite implementation checks, not a novelty or formal/external review claim.

Fix any vertex v, put A=N(v), B=V minus(A union{v}), and d=|A|. Because d<=7, B is nonempty. It has no independent triple: v would extend one to an independent four-set. It also has noK5.

For u in B, the nonneighbors of u within B form a clique. Otherwise u and a nonadjacent pair of those nonneighbors would be an independent triple in B. That clique has at most4vertices. Thus

degree_B(u) >= |B|-5.

Since degree_G(u)<=7, |B|<=12. As |B|=16-d, necessarily d>=4. This avoids any imported Ramsey-number value.

## Excluding d=4

Then |B|=12 and every u in B has degree_B(u)>=7. The full maximum-degree bound forces degree_B(u)=7 and no edges from B to A (there are no B-to-v edges by definition). The five vertices A union{v} cannot be a clique because G has noK5. Since v is adjacent to every vertex of A, there is a nonadjacent pair in A. There is also a nonadjacent pair in B, because each B vertex has degree7 among11possible neighbors. With no A-to-B edges, those two pairs form an independent four-set, a contradiction.

## A five-vertex edge-family fact

Let H be a graph on five vertices with no two disjoint edges. If all its edges share one vertex, H is a subgraph of a star. Otherwise H has exactly the three edges of a triangle, with two isolated vertices.

To prove the nonstar case, choose two intersecting distinct edges {a,b},{a,c}. Such a pair exists unless there is at most one edge, which is a star subgraph. Since no vertex is common to every edge, there is an edge avoiding a. It must meet both chosen edges and so is {b,c}. Any edge outside this triangle misses one of its three edges, contradicting the no-disjoint-edges hypothesis. Thus all edges belong to the triangle, and all three already occur. A star subgraph has an independent four-set (all vertices except its center). Therefore if H also has no independent four-set, H must be exactly that triangle plus two isolates. This is the statement checked on all1024labeled five-vertex graphs; the analytic proof is not inferred from that check.

## Excluding d=5

Now |A|=5 and |B|=11. Every u in B has degree_B(u)>=6 and hence has at most one neighbor in A.

For a nonadjacent pair a,b in A, the B vertices adjacent to neither form a clique: a nonadjacent pair among them, together with a,b, would be an independent four-set. That clique has size at most4, so at least7vertices of B are adjacent to a or b. If A had two vertex-disjoint nonadjacent pairs, their two B-neighborhood unions would be disjoint, since each B vertex has at most one A neighbor. This would require at least14distinct vertices in B, which has11. Therefore the complement H of G[A] has no two disjoint edges.

G[A] has noK4, because v would extend it to a K5. Equivalently H has no independent four-set. The preceding five-vertex fact implies H is a triangle plus two isolates. Thus A contains an independent triple a,b,c, and the other two A vertices are adjacent to all of A.

Every u in B must be adjacent to at least one of a,b,c; otherwise u together with that triple is an independent four-set. Since each u has at most one A neighbor, B is partitioned into three groups B_a,B_b,B_c according to its unique neighbor in the triple.

Each B_a is a clique: any nonadjacent pair in it, together with b,c, would be an independent four-set, since members of B_a are adjacent to neither b nor c. Furthermore a is adjacent to every vertex of B_a, so |B_a|<=3; four vertices in that clique with a would form a K5. The same holds for B_b and B_c. Thus |B|<=3+3+3=9, contradicting |B|=11.

The chosen vertex v was arbitrary. Degrees4and5 are impossible, and smaller degrees were already excluded. Every degree is therefore6or7. Combined with the proved sorted-neighborhood existence reduction, the eight retained raw branch inputs have analytic exclusions for degrees0through5, while cases6and7 remain unresolved.

## Attack and transfer limits

The pairwise-intersection fact requires both hypotheses at the indicated stages: a four-edge star has no two disjoint edges but has an independent four-set; a five-cycle has no independent four-set but has two disjoint edges. The B-neighborhood unions are disjoint only because each B vertex has at most one A neighbor; that bound is specific to d=5 here. Do not carry it to d=6 or7, where the corresponding bound is2or3. The three groups are cliques only because the other two members of the independent triple have no edges to that group. These quantified steps are essential.

No17vertex graph enumeration was used. The result transfers as a structural prerequisite for a future certificate, but does not itself prove the source finite lemma. The old first-stage certificate's remaining list is retained as historical phase state; this addendum and its separate refinement receipt supersede that list for the current queue. No larger unchanged DPLL run is justified by the number of removed cases or by raw clause counts.


[Batch verification](../verification_result.json) · [Extension verification](../extension_result.json) · [Exact exclusion chain](../chain_result.json).

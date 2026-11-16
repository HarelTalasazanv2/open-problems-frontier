# Cycle 197: a restricted graph exclusion and exact finite audit

**PROVED at the stated scope.** No simple undirected graph on 17 vertices with no five-clique, no independent four-set, maximum degree at most seven, and a selected degree-six root can have root-neighborhood graph 685.

The label 685 means the six-vertex graph whose edges are 01,03,04,12,14,23. Equivalently, bit j of the integer mask encodes the j-th unordered pair in lexicographic order on vertices 0,...,5.

## Reduction to necessary types

Write A for the root's six neighbors and B for its ten nonneighbors. A contains no four-clique, because the root would extend it to a five-clique. B contains no independent triple, because the root would extend it to an independent four-set.

For any u in B, its nonneighbors in B form a clique: two nonadjacent such vertices together with u would be an independent triple. There are at most four of them, so u has at least five neighbors in B. The total-degree bound implies that its A-neighborhood S has size at most two.

The empty type S cannot occur. If u avoids all of A, take any other w in B. Since w has at most two A-neighbors, at least four vertices of A avoid w; among these there is a nonedge a,b because A has no four-clique. If u,w were nonadjacent, u,w,a,b would be an independent four-set. Thus u is adjacent to all nine other B-vertices, contradicting the degree bound.

Every B-type is consequently one of the six singletons or fifteen pairs. It must meet every independent triple in A. Vertices sharing a type S form a clique: A minus S contains a nonedge, which would extend two nonadjacent vertices of this type to an independent four-set. A pair that is an A-edge has multiplicity at most two, since three of its vertices with that pair give a five-clique. Every singleton or nonedge-pair has multiplicity at most three, since four of its vertices with one element of S give a five-clique. These are necessary restrictions, not sufficient graph-completion conditions.

## Literal class 685

Vertex 5 is isolated in A. Its independent triples are exactly 025,135,245,345. The complete admissible type support is

    5, 05, 15, 23, 25, 35, 45.

Indeed, a type omitting 5 must meet all four pairs 02,13,24,34; among types of size at most two, only 23 does so. The pair 23 is an edge and its type has capacity two. Therefore at least eight of the ten B-vertices are adjacent to 5. But 5 already has its root edge and the degree bound permits at most six B-neighbors. This is the contradiction 8 <= 6.

This proof does not assume any minimum-degree lower bound or any historical exclusion from the other 83 six-vertex orbit classes.

## Exact matrix certificate

The [retained model](data/model.json) contains all 21 type variables, population ten, all 14 forbidden-type zero equations, six lower and six upper degree inequalities, 21 type capacities and nine nonedge-avoidance inequalities. With 42 nonnegative slack variables it is a 57-by-63 system Mx=b, x>=0.

The [certificate](data/certificate.json) subtracts the population row, adds upper:5 and cap:15 (type index 15 is the pair 23), and adds all 14 forbidden-type zero rows. Its combined columns are nonnegative, and its combined right side is

    6 + 2 - 10 = -2.

The multiplier has one-norm 17. None of the six lower-degree rows has a nonzero multiplier. Removing those rows and their six slack columns leaves the same contradiction in a 51-by-57 system. For the full, fixed, unscaled representation, every nonnegative x also satisfies ||Mx-b||_infinity >= 2/17. This is a lower bound, not an optimal residual, a graph distance, or a row-scaling-invariant quantity.

## Finite inequality audit

For a vertex v in A, let k[v] be its degree in A. Sum the capacities of every admissible type avoiding v to obtain C[v]. Any actual graph satisfies

    10 = t[v] + sum_(S avoiding v) n[S] <= 6-k[v] + C[v].

Thus D[v]=6-k[v]+C[v]-10 < 0 is a sufficient obstruction. Equality is not an exclusion. The [complete audit](data/audit.json) evaluates the exact frozen list of 50 representatives at all six vertices. Only 685 has a negative margin, at v=5, with D[5]=-2. The other 49 decisions do not imply graph or relaxation feasibility.

All 720 vertex permutations yield 360 distinct labeled images of 685. Deleting exactly those images from the supplied 50-class/15,232-member prior list leaves 49 classes/14,872 labeled neighborhoods. This is a set update relative to the supplied prior list; this audit does not reproduce every earlier argument that generated that list.

## Additional census check and limits

The fresh checker enumerates all 32,768 six-vertex masks, retaining exactly those with neither a four-clique nor an independent four-set. It verifies every member of all 84 complete permutation orbits against the supplied source ledger: 22,484 admissible masks. This is a separate **CERTIFIED_RANGE** result for a finite six-vertex domain.

The proof was reviewed internally and computations rerun with newly written, source-exposed code. Expected conclusions, input artifacts and hypotheses were shared; the review is nonblind and uses the same actor. No external human review, Lean/kernel replay, novelty, empirical physics result, or resolution of the broader graph target is claimed. See [verification result](verification_result.json), [references and attribution](REFERENCES.md), and [reproduction instructions](README.md).


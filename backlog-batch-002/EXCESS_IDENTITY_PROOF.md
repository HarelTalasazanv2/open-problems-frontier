# Known excess identity: independent local derivations

**PROVED, internal reproduction of a known identity.** Let F=(V,E) be any finite simple undirected unweighted graph, n=|V|>=0, d(v)=|N(v)|, and B(v)=V\(N(v) union {v}). All neighborhoods are open. Write e(U) for the number of edges in the induced graph F[U]. Then

2 sum_v (e(B(v))-e(N(v))) = sum_v d(v)(n-2d(v)).

This is the doubled form of equation1.2 in Angeltveit/McKay, arXiv2409.15709v2. The result is a general counting identity, not a new Ramsey bound or a claim that the paper's catalogue/LP/computation has been reproduced. No regularity, Ramsey property, minimum degree, catalogue or R(4,5) value is assumed.

## Proof by induced triples

For n>=3 let t_i count the unordered three-vertex sets inducing exactly i edges, for i=0,1,2,3. Define A=sum_v e(B(v)), C=sum_v e(N(v)), S=sum_v d(v), and W=sum_v d(v)(n-1-d(v)).

An edge inside B(v) is a triple with exactly one edge and isolated distinguished vertexv; that vertex is unique. Hence A=t_1. An edge inside N(v) is a triangle with distinguished vertexv; each triangle has three choices. Hence C=3t_3.

The quantity W counts ordered pairs (u,w) with u adjacent to v and w a distinct nonneighbor of v, summed over v. Each one-edge triple contributes two such choices, each two-edge path contributes two, and the empty triple and triangle contribute none. Thus W=2(t_1+t_2).

Each edge lies in n-2 triples. Since S=2|E|, (n-2)S=2(t_1+2t_2+3t_3). Therefore

2W-(n-2)S = 2t_1-6t_3 = 2(A-C).

But expanding W gives

2W-(n-2)S = nS-2 sum_v d(v)^2 = sum_v d(v)(n-2d(v)).

These are exact finite counts. For n=0 or1 every term vanishes. For n=2 the empty graph also has zero terms; in the single-edge graph both degrees are1, both neighborhood edgecounts are zero and n-2d(v)=0. This exhausts the omitted small orders.

## Proof by contributions from a fixed edge

Fix an edge uv, and let c be the number of common neighbors of u andv. Among the n-2 other vertices, d(u)-1 are neighbors of u and d(v)-1 are neighbors ofv, with intersection c. Thus n-d(u)-d(v)+c are adjacent to neither endpoint.

In A, this edge is counted once for each vertex adjacent to neither endpoint. In C, it is counted once for each common neighbor. Its net contribution to A-C is therefore n-d(u)-d(v). Summing over edges yields

A-C = n|E|-sum_{uv inE}(d(u)+d(v)) = n|E|-sum_v d(v)^2.

The last equality holds because vertexv is incident to exactly d(v) edges, each contributing d(v). Using 2|E|=sum_vd(v) and multiplying by2 proves the identity. Graphs with no edges have empty edge sums and all degrees zero, so this proof also covers n=0 and1 directly. Endpoints are excluded from the common/nonneighbor count; loops and multiple edges are outside the stated domain.

## Convention attack: a zero residual does not validate the dual order

If B(v) is incorrectly replaced by B(v) union {v}, the added vertex is isolated in that induced graph: it has no edge to any nonneighbor. Thus its induced edgecount, and the excess identity, are unchanged for every F. Nevertheless the vertex set and its order are wrong: the correct order is n-1-d(v), whereas the altered one has order n-d(v). A numerical zero residual cannot detect this error. Exact membership and cardinality require their own checks before assigning a Ramsey type to the dual neighborhood.

Dropping the outer factor2, reversing the neighborhood difference, or replacing n byn-1 in the degree term give different statements. For K3, A=0, C=3 and the correct degree term is-6; the three altered residuals are3,12and6 respectively. These are counterexamples to those variants only. The actual identity is unaffected.

## Assurance and claim ceiling

These are two handwritten derivations by the same exposed actor, sharing definitions and the expected statement. They are not blind, external expert or proof-assistant verification. Small graph computations are convention controls, not the proof for all n. No probability of solving R(5,5), novelty, catalogue completeness, current-best bound or method gain is inferred. Any later use of source-specific typed graph classes must separately validate their orders and membership.

## Audit batch002

The complete analytic argument and its stated domain were rechecked. The76small-graph cases, exact four-degree margins and convention controls are additional checks; the universal quantifiers rest on the counting proof. No source-specific census, upper Ramsey bound or current-best claim is promoted. See [graph counting audit](GRAPH_COUNTING_AUDIT.json) and [references](REFERENCES.md).

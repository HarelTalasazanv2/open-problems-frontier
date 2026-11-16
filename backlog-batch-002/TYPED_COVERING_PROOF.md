# Explicit high-edge covering lemma

**PROVED internally, reproduction of a known argument with explicit local types.** For a finite simple undirected unweighted graph F on46vertices assume every degree lies in D={21,22,23,24}. Put t(21)=107,t(22)=113,t(23)=119,t(24)=127. For each vertex v define the open neighborhood N(v) and B(v)=V(F) minus(N(v) union{v}). Then some v satisfies

e(F[N(v)])>=t(d(v)) OR e(complement(F[B(v)]))>=t(45-d(v)).

The complement is on precisely B(v), not on the full graph or on B(v) union{v}. All quantities are exact integers. No Ramsey exclusion, census, extremal edge theorem, numerical tolerance, or R(4,5)=25 result is needed for this first assertion. The degree restriction is an explicit hypothesis.

## Counting dependency and strict boundaries

Use the internally proved known identity from C170, at its pinned artifact identity:

sum_v [e(F[B(v)])-e(F[N(v)])-d(v)(46-2d(v))/2]=0.

Both complete counting derivations are retained in [EXCESS_IDENTITY_PROOF.md](EXCESS_IDENTITY_PROOF.md). This run uses that accepted dependency rather than repeating its proof or an identity grid. The offset is integral because46is even. Write r(v) for the summand.

Suppose the conclusion fails for every v. Set d=d(v),m=45-d. Both d,m lie in D. Since edge counts are integers, failure of each weak inequality gives

e(F[N(v)])<=t(d)-1,
e(complement(F[B(v)]))<=t(m)-1,
e(F[B(v)])>=binom(m,2)-t(m)+1.

The second-to-third implication follows because a simple graph and its complement partition the unordered pairs on the same m-element vertex set. Therefore

r(v)>=binom(45-d,2)-t(45-d)-t(d)+2-d(46-2d)/2.

The four cases are exhaustive by the stated hypothesis:

| d | m | maximum e(N) | maximum complement e(B) | minimum e(B) | offset -d(46-2d)/2 | minimum r(v) |
|---|---|---|---|---|---|---|
|21|24|106|126|150|-42|2|
|22|23|112|118|135|-22|1|
|23|22|118|112|119|0|1|
|24|21|126|106|104|24|2|

Every contribution is at least1, and in fact

sum_v r(v)>=46+number of vertices with degree21or24>=46.

This contradicts the zero identity and proves the covering assertion. This table is a finite partition of the degree domain, not a sample of graphs. Monotonicity in the two edge counts covers every admissible value below the two caps; no hidden equality or untested boundary case remains. Values at t(d) or t(m) already satisfy the claimed conclusion.

An equivalent second algebraic organization groups complementary degree pairs: d and45-d have equal margins because the change in the pair count binom(45-d,2) is compensated by the degree offset. For pairs(21,24)and(22,23), the threshold sums are234and232 and the margins are2and1 respectively. This supplies a sign/order check of the four-case table; it shares the same identity and definitions, not an independent external proof.

## Ramsey-type corollary and the exact scope of E*

Now additionally assume F has noK5 and no independent5. Any4clique in F[N(v)] would join v to form a5clique; an independent5 there would already occur in F. Thus F[N(v)] is R(4,5) on d(v)vertices.

F[B(v)] has noK5. It also has no independent4, since such a set together with the nonadjacent centre v would form an independent5 in F. Its induced complement therefore has noK4 and no independent5, so it too is R(4,5), on45-d(v)vertices. These implications use open/excluded-centre membership, not merely an edge-count residual.

Define the local family E* as the union over k in D of all R(4,5,k) graphs with at least t(k)edges. The proved assertion now states that an open neighborhood lies in E*, or a dual neighborhood lies in the family of complements of E* graphs. This closes this explicitly typed exclusion-to-excess step under the explicit degree hypothesis.

The order22 part is defined by e>=113, not solely by the exact classes e=113 and e=114. Equating those formulations would require an additional upper-edge bound; none is imported here. A local exact-e113 subfamily may be called C3*, with order22. That notation does not amend the paper's printed C3order21/e113. The v2 source typing issue and raw final-publication gap remain unresolved.

## Adversarial assessment and remaining bridge

The strongest first assertion does not need the Ramsey assumption; only the class-type corollary needs it. It does need n46and degrees21..24 as stated. Weighted, directed, looped, multiple-edge graphs, changed thresholds and extra degrees are outside this contract. No division by an entropy, approximation, convergence limit or singular boundary is involved.

Removing the centre or changing21/22affects the dual type and the complement pair count. Reversing the complement inequality invalidates the lower bound. Changing strict `<t` to `<=t` loses the integer boundary. Those are meaningful consumer controls; a rejected control is not a counterexample to some different globally formulated theorem. Five named non-Ramsey graph fixtures exercise a local implementation only; the universal claim rests on this analytic proof and the accepted identity.

The next unresolved global proof bridge is an exclusion or sufficient gluing cover for every relevant high-edge type, together with its catalogue completeness, source typing and degree/status assumptions. This lemma only forces a high-edge occurrence. It does not exclude that occurrence or establish nonexistence of F, a new Ramsey bound, current-world open status, priority or novelty. Internal same-actor derivation and exact controls are not blind, external human or formal verification. No method gain is measured.

## Audit batch002

The complete analytic argument and its stated domain were rechecked. The76small-graph cases, exact four-degree margins and convention controls are additional checks; the universal quantifiers rest on the counting proof. No source-specific census, upper Ramsey bound or current-best claim is promoted. See [graph counting audit](GRAPH_COUNTING_AUDIT.json) and [references](REFERENCES.md).

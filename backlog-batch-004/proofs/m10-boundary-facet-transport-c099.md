# Audited historical reading edition

**Current audited claim:** PROVED: Under the stated inner-radius, facet-diameter, angle and Hausdorff bounds, separated boundary directions have distinct antipodal facet labels and controlled support-coordinate errors.

**Claim ceiling:** Finite-dimensional transport; no genericity follows by itself.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M10 boundary-to-facet transport

2026-10-30 UTC, cycle099. **PROVED internally at the stated scope.** The exact boundary, angular and support-coordinate bridge used in Alon–Bucić–Sauermann2302.09058v2, Lemma3.5 and the end of Lemma5.3, is reproduced here. This is a known finite-dimensional ingredient, not a new Euclidean chromatic bound or a proof of full genericity.

The submitted packet (historical local record; not distributed here) and fresh frozen attempt (historical local record; not distributed here) preserve the expected claim, controls and20-minute primary cap. The expected result, source and elementary proof route were exposed before verification. This is an internal reconstruction, not blind or external review.

## 1. Exact theorem and conventions

Fix integers d,h≥1 and a full-dimensional compact convex polytope P=−P⊂R^d with

\[
 r\mathbb D_2\subseteq P
 =\{x:|o_i\cdot x|\leq t_i, 1\leq i\leq h\},
 \qquad r>0,\quad \|o_i\|_2=1,\quad t_i>0.
\]

Here D_2 is the closed Euclidean unit ball; every diameter, point distance and Hausdorff distance below is Euclidean. Facets are entire(d−1)-faces, not subdivisions. Suppose all facets have diameter≤D. Let0<η<π/2 and D<r sinη. Choose

\[
 0<\delta<r,\qquad
 \frac{D+2\delta}{r-\delta}\leq\sin\eta.             \tag{1}
\]

There is such a δ. More explicitly every0<δ≤δ_0 is admissible, where

\[
 \delta_0=\frac{r\sin\eta-D}{2+\sin\eta}>0,
 \qquad \delta_0<r.                                \tag{2}
\]

Let B′=−B′ be compact, convex and full-dimensional with0 in its interior, and d_H(B′,P)<δ. Let u_1,…,u_N∈∂B′ be a finite family whose pairwise unoriented line angles exceed η. For nonzero x,y, our angle is

\[
 \vartheta(x,y)=\arccos\frac{|x\cdot y|}{\|x\|_2\|y\|_2}
 \in[0,\pi/2].
\]

Then:

1. Each u_j admits b_j∈∂P with ||u_j−b_j||_2<δ. All such choices satisfy ||u_j||_2>r−δ>0.
2. No two chosen b_j lie on a common facet or on opposite facets. Any choice of an actual facet containing each b_j gives distinct antipodal facet pairs, hence N≤h. Rows may be redundant or duplicate, and b_j may be on edges or vertices.
3. One may choose distinct indices i_1,…,i_N with |o_(i_j)·b_j|=t_(i_j), and define

\[
 t'_{i_j}=|o_{i_j}\cdot u_j|,
 \qquad t'_i=t_i\quad(i\notin\{i_1,\ldots,i_N\}).
\]

Then ||t′−t||∞<δ and every t′_i>0. In fact any active-row choices are distinct, by the face argument below. Thus the literal source selection is covered even when some active rows expose lower-dimensional faces.

**Claim ceiling:** an exact internal boundary/angle/facet-label/support-error theorem for these finite-dimensional bodies; no exclusion of achievable parameters, full nowhere-denseness, countable genericity, infinite graph compactness, new Euclidean colouring, novelty or external/formal assurance.

## 2. Boundary distance requires a boundary hypothesis

We first reproduce the required base lemma: for compact convex full-dimensional K,L⊂R^d,

\[
 \operatorname{dist}(x,\partial L)\leq d_H(K,L)
 \quad(x\in\partial K),                            \tag{3}
\]

and the analogous inequality with K,L exchanged. They need not be origin-symmetric for this lemma.

Put ε=d_H(K,L). If x∈∂L the conclusion is immediate. If x∉L, choose a closest point y∈L, which exists by compactness. It is on ∂L: if it were interior, moving it a sufficiently short distance toward x would decrease ||x−y||_2 while remaining in L. Thus ||x−y||_2=dist(x,L)≤ε.

If x∈intL, choose a supporting Euclidean unit normal n for K at x. Follow the ray x+λn, λ≥0, to its last point y in L; boundedness, closedness and x∈intL give y=x+λ_0n∈∂L with λ_0>0. The support function h_K(n)=max_(z∈K)n·z equals n·x. Therefore

\[
 \lambda_0=n\cdot y-h_K(n)
 \leq h_L(n)-h_K(n)\leq\varepsilon.
\]

The last inequality follows directly from Hausdorff distance: for each y′∈L choose z∈K within ε, giving n·y′≤n·z+ε≤h_K(n)+ε; then take the maximum. This proves(3), including its closed error bound. Applying it with K=B′,L=P gives the strict target error because d_H(B′,P)<δ.

For completeness, the supporting normal used here has an elementary compactness construction. Choose exterior points x_m→x, closest y_m∈K and unit n_m=(x_m−y_m)/||x_m−y_m||_2. Minimality along the segment from y_m to z∈K gives n_m·(z−y_m)≤0: expand the squared distance at y_m+λ(z−y_m) and let λ decrease to0. Also ||y_m−x||_2≤2||x_m−x||_2→0. A subsequence n_m→n has ||n||_2=1 and n·(z−x)≤0 for every z∈K. This is the required supporting hyperplane; no differentiability, smoothness or strict convexity is assumed.

This agrees with sourceLemma3.5 physical9–10. As an alternate check of the inside case, if λ_0>ε then every z∈K satisfies n·(y−z)≥λ_0>ε, so dist(y,K)>ε, contradicting y∈L and the definition of d_H. The support-function and halfspace-distance arguments check the bound direction within the same exposed audit.

## 3. Angular exclusion near a whole facet

Every b∈∂P has ||b||_2≥r: a point with smaller norm is interior to rD_2 and hence interior to P. Thus ||u−b||_2<δ implies ||u||_2>r−δ>0.

Suppose b,c belong to the same facet F and ||u−b||_2,||v−c||_2<δ. Then

\[
 \|u-v\|_2< D+2\delta.
\]

For nonzero u,v, distance from u to the line Rv gives

\[
 \sin\vartheta(u,v)
 =\frac{\operatorname{dist}(u,\mathbb Rv)}{\|u\|_2}
 \leq\frac{\|u-v\|_2}{\|u\|_2}
 <\frac{D+2\delta}{r-\delta}\leq\sin\eta.           \tag{4}
\]

Sine is strictly increasing on[0,π/2], so θ(u,v)<η. If the point errors are only≤δ, the same argument gives the source's non-strict conclusion θ≤η. We use neither a large oriented vector angle nor monotonicity of sine on[0,π].

If b lies on F and c on −F, apply this argument to u,−v near b,−c on F. Since θ(u,−v)=θ(u,v), these pairs are also excluded by the hypothesis θ(u_j,u_k)>η. This proves assertion2. In particular every possible boundary-point choice from(3) works; no specially optimized matching is needed. The strict point errors even exclude θ=η for a same/opposite pair, although we retain the source's stated >η input convention.

Equation(2) is just(1) solved for δ: D+(2+sinη)δ≤r sinη. Its numerator is positive by hypothesis and its value is less than r. It is an explicit angular error budget, not the previously uncomputed offset-stability radius from098.

## 4. Actual facets, active rows, and offset normalization

For a bounded full-dimensional finite halfspace intersection, every boundary point lies on some actual facet, and each facet is the equality face of at least one signed defining inequality. The [098 proof](m10-facet-offset-stability-c098.md), Section2, supplies the elementary irredundant-row argument. Its hypotheses hold here. Choose one such row for each selected facet. Two selected facets using the same unsigned row would be the same or opposite facets, contradicting Section3. Therefore the indices i_j are distinct. This covers edges, vertices, and arbitrarily repeated descriptions of the same supporting plane.

One can also check the source's choice of any active row directly. Two points of P on the same proper supporting hyperplane lie in a common actual facet: their midpoint is a boundary point, and equality of a facet's supporting functional at that midpoint forces equality at both endpoints. If b_j,b_k share an unsigned active row, either they, or b_j,−b_k, lie on that row's same supporting hyperplane. Symmetry keeps −b_k in P. The preceding fact reduces again to Section3. Hence lower-dimensional exposed faces cannot produce a duplicate active index either.

For each j, the reverse triangle inequality and Cauchy–Schwarz give

\[
 \big||o_{i_j}\cdot u_j|-t_{i_j}\big|
 =\big||o_{i_j}\cdot u_j|-|o_{i_j}\cdot b_j|\big|
 \leq |o_{i_j}\cdot(u_j-b_j)|
 \leq\|u_j-b_j\|_2<\delta.                         \tag{5}
\]

Distinct indices make the definition of t′ consistent. All other coordinates have zero error, so ||t′−t||∞<δ. Because rD_2⊆P and ||o_i||_2=1, the point ro_i∈P gives t_i≥r for every row, including redundant rows. Thus t′_i≥t_i−||t′−t||∞>r−δ>0. The extra positivity condition δ<min_i t_i in the submitted packet is automatic here, not a newly assumed hypothesis.

For N=0 take t′=t; for d=1 facets are endpoints and there is only one unoriented line, so a separated family has at most one point. These cases satisfy the same conclusions. No zero denominator or zero input vector is hidden by a tolerance.

## 5. Exact falsifications of weakened variants

The following are mathematical counterexamples, not failed random searches or software tests. Each uses r=1,D=0,η=π/4 and δ=1/10 in dimension1; (D+2δ)/(r−δ)=2/9<sin(π/4), since4/81<1/2.

| Weakened claim | Exact witness | Failure scope |
|---|---|---|
| Replace u_j∈∂B′ by u_j∈B′ | P=B′=[−1,1], o_1=1,t_1=1,N=1,u_1=1/2 | d_H=0, yet distance from u_1 to ∂P is1/2>δ. Pairwise separation is vacuous. Boundary transport fails. |
| Use oriented vector angles instead of acute line angles | Same P=B′,N=2,u_1=1,u_2=−1 | The oriented angle isπ>η, but both vectors lie on the same unoriented line and opposite facets of one pair. Two distinct indices cannot be assigned when h=1. |
| Drop unit normal scaling but keep unscaled coordinate error<δ | P={x:|2x|≤2}=[−1,1], B′=[−43/40,43/40], u_1=43/40,b_1=1 | d_H=3/40<δ, but |t′_1−t_1|=|2u_1−2|=3/20>δ. All other hypotheses hold; only ||o_1||=1 was removed. The valid general bound has factor||o_i||. |

These three weakened statements are **FALSIFIED**. The literal frozen theorem survives. The healthy cases P=B′ with boundary points and any single-point family give zero transport error; delta approaching r is excluded by(1), not ignored numerically. No claim is made that distinct facet labels alone imply angular separation.

## 6. Source crosswalk and bounded corpus increment

The [primary v2 source](https://arxiv.org/abs/2302.09058v2) is33pages/484598bytes, SHA-25687801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960. Lemma3.5 physical9–10 and its consumer physical22–23 were fully reread. Sourcephysical22 uses inner radius s, facet bound s sin(η/2) and the same angular ratio; these satisfy our margin because sin(η/2)<sinη. The final coordinate perturbation on physical23 agrees with(5), with δ further below the source's separate excluded-parameter radius δ′. The source's reused index letters are made explicit here as j,k; no new source-error or global-refutation claim is inferred from those labels.

New full-text inspection covers physical25–26; new full visual inspection covers10 and25. The exact register (historical local record; not distributed here) preserves prior partial reads, page/text hashes and parser limitations. Combined full text is physical3–10 and17–26:18 selected pages, not all33. The initial locator-only physical25lines1–7 is absorbed into its later full-page read, not counted twice. Physical10 text was already read and receives only new visual credit; prior visual22/23 also receive no new credit.

The new material is a different consumer: Section7 counts unit-distance edges using injective sums of equilateral triples, and introduces an external dimension theorem in a later lower-bound proof. These proof chains are not locally promoted here. In particular, physical26's guaranteed one-coordinate changes describe a Cartesian product of triangles as a subgraph, not an established induced unit-distance graph or a chromatic obstruction of growing size.

The distinction has an elementary exact check. The abstract Cartesian product K_3□…□K_3 on{0,1,2}^k has3^k vertices, degree2k, hence k3^k edges; c(a_1,…,a_k)=Σa_i modulo3 is a proper3-colouring, and a coordinate slice is a triangle. Its chromatic number is therefore3 for every k≥1. An embedded copy does not colour the full unit-distance graph, which may have extra edges, and its large edge count does not itself supply a growing chromatic lower bound. We do not assume the source's injective-sum existence lemma or Hurewicz theorem has been independently reproduced. The value of this reading is a precise separation of edge-count and colouring evidence.

Fresh [2026 owner metadata](https://arxiv.org/abs/2609.36220) still lists v1. The existing matching-v1 PDF/full introduction was reread; its Euclidean open/5-to7 statements remain AS_REPORTED under a bounded2026-10-30 status check. No fresh PDF body download, exhaustive recent-literature absence check or reproduction of those bounds occurred. Same-work representations and rereads supply no new independent source or reviewer.

## 7. Adjudication, independence and next obstruction

| Obligation | Outcome | Limit |
|---|---|---|
| Boundary distance(3) | PROVED | Known convex-body lemma reproduced, all inside/outside/on-boundary cases |
| Angular/facet-pair transport | PROVED | Acute unoriented angles, whole facets, inner radius and strict errors explicit |
| Distinct support labels and positive t′ | PROVED | All active choices, redundancies and vertex/edge cases covered |
| Three weakened variants | FALSIFIED | Only the exact removed boundary/angle/scaling hypotheses |
| Source reading and consumer crosswalk | CERTIFIED_RANGE | Exact inspected extents, not full-paper or independent review |
| Achievable-parameter exclusion/full genericity/Euclidean colouring | NOT_TESTED | Necessary remaining assembly is not implied by this finite bridge |

The uncertainty changed from an unadjudicated boundary-to-parameter transfer to a proved finite bridge with explicit angular tolerance. The controls show which hypotheses cannot be dropped. The supporting-plane and projection reasoning uses elementary finite-dimensional compactness and convexity; the facet-cover dependency is an internally proved098 result with unchanged artifact identity. Source and expected-answer exposure are shared; all construction and review is by the same actor. No independent human, external model, blind or formal review is claimed. No mathematical executable, numerical enclosure or measured performance comparison occurred.

This is the third substantive geometric success097–099. A whole-frontier rerank is required before selecting continuation. The proposed next test must check a genuine remaining interaction, rather than assume that the local lemmas automatically prove nowhere-denseness. Full genericity, the m>0 algebraic branch and infinite graph compactness remain held.

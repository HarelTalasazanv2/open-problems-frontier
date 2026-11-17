# Audited historical reading edition

**Current audited claim:** PROVED: Every fixed stated m-positive rational-function dependence family with separated boundary directions is nowhere dense.

**Claim ceiling:** Original vectors and actual parameter are retained; no full distinct-distance application by this lemma alone.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Fixed rational-function family: robust geometric exclusion

2026-10-31 UTC, cycle109. **PROVED internally:** the fixed m-positive family below is nowhere dense in the Hausdorff space of norm bodies, with an actual excluded ball inside every prescribed open ball. This reconstructs the m-positive geometric content of the source's Lemma5.3 at its p22 witness restatement. It is known dependency work. The full distinct-distance theorem, countable application, full paper, new Euclidean bounds, novelty, formal verification and external mathematical acceptance are not established here.

## 1. Exact theorem and trust boundary

Fix integers d>=2, ell,m>=1, L=d*ell+m+1, a matrix

`A in Q(z_1,...,z_m)^(L by ell)`,

and a rational number 0<eta<pi/2. There is no rank or identity-first-rows assumption. Let B_d be the compact convex origin-symmetric bodies in R^d with0 in their interior, with the relative Euclidean Hausdorff metric. Every point distance, inner radius and facet diameter below is Euclidean. Offset-space distance is the maximum norm. For nonzero x,y, let

`theta(x,y)=arccos(|x dot y|/(||x||_2 ||y||_2)) in[0,pi/2]`.

Let E_(A,eta) consist of the K in B_d for which there are a real z where every entry of A has a legitimate common evaluation, and vectors u_1,...,u_L in the boundary of K, such that

`u_j = sum_(i=1)^ell A_ji(z) u_i` for every j=1,...,L,

and theta(u_j,u_k)>eta for all j!=k. In particular all these vectors are nonzero. Well-defined rational entries may use valid local presentations as in108; no values are assigned to true poles. If the source uses a narrower fixed-presentation domain, it is covered as a subset.

**Theorem.** For every B_0 in B_d and epsilon>0, there exist a symmetric full-dimensional polytope B in B_d and rho>0 such that

`Ball_H(B,rho) subset Ball_H(B_0,epsilon) minus E_(A,eta)`.

Consequently E_(A,eta) is nowhere dense. Balls here are open and relative to B_d. We do not assert that E_(A,eta) itself is closed. No numerical radius, uniform bound across all A, effective facet count or constructive computation is claimed.

The initial freeze (historical local record; not distributed here) preceded109 source inspection. The analytic amendment (historical local record; not distributed here) records the source-matched contract, exposure and radius order before confirmation. The expected m=0 composition and source were already exposed to this same actor/model. This is an internal analytic reconstruction and self-challenge, not a blind, independent-agent, human or formal audit.

## 2. Source matching and inherited dependencies

Primary source: Alon-Bucic-Sauermann, https://arxiv.org/pdf/2302.09058v2 , owned33-page PDF (historical local record; not distributed here),484598bytes, SHA256 `87801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960`. Full physical18,19,22,23 text and renderings were inspected109. Page19 states Lemma5.3 and the approximation setup;22 explicitly restates the bad-family witness and all L relations at its actual z;23 completes the injection/support-parameter contradiction. The earlier standalone definition on17 was not reread109 under the four-page cap. The precise theorem above is self-contained and matches the explicit p22 restatement; this bounded crosswalk is not a claim that every earlier definition was freshly audited.

The source's p23 sentence claiming the full Theorems1.1/1.3 is an assertion of the source, not this run's conclusion. Page18's Lemma5.2 invokes a separate field-span Lemma4.2, which has not been established by this run. The108 shorter-witness-list and ambient-label defects on20/21 remain preserved; those pages were not reread109, and the complete L-vector achievable definition audited108 is used.

| Necessary input | Exact scope used | Custody and review limit |
|---|---|---|
| [097 small-facet approximation](m10-small-facet-approx-c097.md) | Any norm body can be approximated with independent positive Hausdorff and whole-facet tolerances | Internally proved known lemma; contract/pivotal proof reread |
| [098 offset stability](m10-facet-offset-stability-c098.md) | Fixed finite normal list: radial Hausdorff bound and upper semicontinuity of maximum whole-facet diameter | Strict slack suffices; stronger full facet continuity is not assumed |
| [099 boundary/facet transport](m10-boundary-facet-transport-c099.md) | Boundary distances, acute line-angle bound, distinct antipodal facet labels and scaled support errors | All boundary/degenerate facet cases in its contract; internal proof |
| [108 rational-image cover](m10-rational-image-c108.md) | One finite proper polynomial zero set covers every achievable tuple, for all legitimate z and every injection/sign choice | No matrix inversion, parameter compactness or numerical certificate |

All five original dossier memberships097/098/099/100/108 match their respective immutable manifests in dependency custody (historical local record; not distributed here). Hash equality establishes artifact identity. The mathematical assurance is inherited internal proof, with scopes reread; it is not new external review. The100 m=0 composition was read in full as an exposed baseline. We replace its finite linear cover by108's rational-image cover and check that the rest of the argument remains valid for every z.

## 3. Choose geometry before choosing the excluded parameter

Fix B_0 and epsilon. Choose r>0 with2r D_2 subset B_0, possible because0 is interior. Let

`alpha=min(epsilon/4,r/2)`,

`D_0=r sin(eta/3)`, `D_*=r sin(eta/2)`.

By097 choose P_0 in B_d, a symmetric full-dimensional polytope, with d_H(P_0,B_0)<alpha and every whole facet of diameter<D_0. The099 boundary-distance lemma sends every b on the boundary of P_0 within distance<alpha of the boundary of B_0. Every latter boundary point has Euclidean norm>=2r, so

`||b||_2 > 2r-alpha >= 3r/2 > r`.

It follows that rD_2 subset P_0: otherwise the segment from the interior point0 to a point of rD_2 outside P_0 would first meet the boundary of P_0 at norm<=r. Choose a finite support presentation

`P_0={x: |o_i dot x|<=s_i, 1<=i<=h}`,

where each normal has Euclidean norm1 and s_i>=r. For example take one row for each antipodal facet pair. Redundant or duplicate descriptions do not affect the argument below;098/099 cover active lower-dimensional faces as well. Let R=max_(P_0)||x||_2>0 and s_min=min_i s_i>=r.

Since 0<eta<pi/2,

`D(P_0)<D_0<D_*<r sin eta`.

By098 choose tau>0 so every offset vector w sufficiently close to s, with ||w-s||_infinity<tau, remains positive and gives facets<D_*. Set

`a=min(tau/2,epsilon*r/(8R),r/2)>0`,

`U=product_(i=1)^h (s_i,s_i+a)`.

For w in U all offsets are outward, hence P_0 subset P(w) and rD_2 subset P(w). The polytope P(w) is bounded, full-dimensional, symmetric and has0 interior by098's radial containments. With Delta=||w-s||_infinity<a<=r/2<s_min, its Hausdorff estimate gives

`d_H(P(w),P_0) <= R Delta/s_min < Ra/r <= epsilon/8`.

Thus, uniformly over w in U, all facets have diameter<D_* and

`d_H(P(w),B_0)<epsilon/4+epsilon/8=3epsilon/8`.

No fixed combinatorial type or continuity of individual moving facets was assumed. The strict inequality D_0<D_* is the required slack for upper semicontinuity.

## 4. One closed offset cover excludes every legitimate parameter

For these fixed normals, call w achievable if some legitimate z and original vectors u_1,...,u_L satisfy all L A(z)-relations, and some injection phi:[L]->[h] satisfies

`|o_phi(j) dot u_j|=w_phi(j)` for every j.

This definition imposes neither boundary membership nor angular separation, so it overcovers the tuples the final bad-body assumption can create. By108, all such w lie in a single closed proper polynomial zero set H in R^h. The argument uses d*ell+m free input coordinates and L=d*ell+m+1 outputs, separately for each of the finitely many injections and sign choices. The nonzero product remains nonzero under injective coordinate embedding. The first ell relations can only restrict the parameter-map image. All legitimate rational evaluations and all ranks are included. If h<L there are no injections and H may be the empty set, the zero set of the constant1.

In particular **the same H is chosen before any hypothetical witness z**. Its covering property ranges over all legitimate real z, including unbounded sequences and approaches to poles. There is no bound on A(z), no subsequence argument for z, no inversion and no parameter derivative estimate. The uniform object is the polynomial relation in output-offset space, not uniform continuity of A near its poles.

Because H is closed with empty interior and U is nonempty open, choose t in U minus H and kappa>0 with

`ClosedBall_infinity(t,kappa) subset U minus H`.

Existence follows from108's nonzero-polynomial interior argument and openness of the complement; no Baire theorem is needed for this finite cover. Define B=P(t). The previous section supplies its preserved inner ball, facet bound and Hausdorff slack.

## 5. Transport a hypothetical bad body using its original witnesses

Define

`beta=(r sin eta-D_*)/(2+sin eta)>0`,

`rho=min(kappa/2,beta/2,epsilon/8,r/4)>0`.

Then rho<r and

`(D_*+2rho)/(r-rho)<=sin eta`,

since (2+sin eta)rho<=r sin eta-D_*. The radius order is noncircular: B_0/epsilon -> r/alpha/P_0 -> normals/s/R/tau/a/U -> H -> t/kappa/B -> beta/rho. No earlier object depends on a later hypothetical witness or radius.

Suppose K in B_d satisfies d_H(K,B)<rho and belongs to E_(A,eta). Retain its actual parameter z and its actual boundary vectors u_j. The099 boundary lemma gives b_j in the boundary of B with ||u_j-b_j||_2<rho. Every u_j has norm>r-rho>0.

If two b_j lie on a common facet, their distance is<D_* and hence the corresponding u vectors have distance<D_*+2rho. Distance to a line gives

`sin theta(u_j,u_k) <= ||u_j-u_k||_2/||u_j||_2 < (D_*+2rho)/(r-rho) <= sin eta`.

On[0,pi/2] sine is increasing, so this contradicts theta>eta. If the b vectors lie on opposite facets, apply the same calculation to u_j,-u_k and b_j,-b_k. Unoriented line angles are unchanged by this sign. Thus selected boundary points occupy distinct antipodal facet pairs. Choose an actual facet containing each b_j and a supporting row for that facet. This produces distinct indices phi(j). If h<L, distinct indices are already impossible and this case is finished. Arbitrary active-row choices also work by099's common-supporting-face argument; duplicate labels and vertices/edges cause no missed case.

For h>=L put

`t'_phi(j)=|o_phi(j) dot u_j|`, and `t'_i=t_i` on unused coordinates.

Unit-normal scaling and the reverse triangle inequality give

`|t'_phi(j)-t_phi(j)| <= |o_phi(j) dot(u_j-b_j)| < rho`.

The injection makes this simultaneous definition consistent, so ||t'-t||_infinity<rho<kappa and every coordinate is positive, since t_i>=r>rho. Consequently t' is outside H. But the unchanged original u_j, unchanged legitimate z, and injection satisfy exactly the achievable definition, so t' is in H. This contradiction excludes every such K.

**The approximants b_j were never substituted into the A(z)-relations.** They provide facet labels and error bounds only. Preserving the original u_j is why no error amplification by large or pole-approaching A(z) occurs. A small perturbation of vectors generally need not satisfy an exact rational relation, and that tempting shortcut is not used.

For any K with d_H(K,B)<rho, the preceding Hausdorff slack gives

`d_H(K,B_0)<rho+3epsilon/8<=epsilon/2<epsilon`.

Thus the whole relative rho-ball about B lies inside the original epsilon-ball and outside E_(A,eta), proving the theorem.

## 6. Nowhere-denseness without an unjustified closure assertion

Every nonempty relatively open subset W of B_d contains a ball about some B_0. The theorem puts a nonempty open ball V inside W that is disjoint from E_(A,eta). It is also disjoint from its closure: every point of V has a smaller neighbourhood inside V avoiding the set. Hence no nonempty W lies in that closure; its interior is empty. Completeness of B_d, Baire category and countability of the matrix family are not needed for this one fixed family.

A general existential projection need not preserve closedness. The algebraic set C={(x,y):xy=1} is closed in R^2, but its x-projection is R minus{0}, which is not closed:1/k tends to0. Therefore a closed-witness-set/projection argument by itself would not establish that E_(A,eta) is closed. This exact control falsifies the **general closed-projection shortcut**, not the source lemma and not a claimed nonclosedness theorem about this particular E.

## 7. Exact attacks and healthy exceptional cases

**FALSIFIED: exclusion must be centred at B_0.** In d=2, ell=2,m=1,L=6, take constant rational A with rows

`(1,0), (0,1), (3/5,4/5), (-3/5,4/5), (5/13,12/13), (-5/13,12/13)`.

All six rows are unit vectors for the Euclidean disk, and satisfy every A-relation using u_1=e_1,u_2=e_2 at any z. Their15 absolute pair determinants in lexicographic pair order are

`1,4/5,4/5,12/13,12/13,3/5,3/5,5/13,5/13,24/25,16/65,56/65,56/65,16/65,120/169`.

The minimum16/65>1/10>=sin(1/10). Thus eta=1/10 is admissible and the Euclidean disk itself belongs to E_(A,eta). No ball centred there can exclude it. The proved theorem permits a nearby centre B. Constant rational functions are legitimate elements of the one-variable field, so this is an admitted m-positive control; it supplies no Euclidean colouring bound.

**FALSIFIED: delete the pairwise-angle condition entirely.** With ell=1,m=1,L=d+2 and every entry of A equal to1, choose any boundary u and repeat it L times. Every norm body then belongs to that weakened family, which equals B_d and is not nowhere dense. This does not refute the separated family.

| Remaining attack | Result and scope |
|---|---|
| A=0 | All relations force zero vectors; zero is interior, so the bad family is empty. |
| Rank changes, non-identity first ell rows | No inversion is used; additional consistency only restricts the achievable image. |
| Unbounded z, near-pole evaluations | One offset cover applies to all legitimate values; no limiting or bounded-coefficient step. True poles remain inadmissible. |
| h<L | Geometry would require an impossible injection; algebraic empty cover is explicit. |
| Redundant rows, edges and vertices | Actual facets can be chosen; any repeated active row also contradicts the small-face angular bound. |
| Missing normal scaling | The valid error bound is ||o_i|| times the point error. Unit normalization is explicit;099's exact control refutes the unscaled variant. |
| Interior points or oriented angles substituted |099's exact counterexamples break those geometric bridge variants. They are input-scope controls, not counterexamples to this d>=2 family. |
| Full facet continuity asserted | Not adopted;098's upper semicontinuity with D_0<D_* supplies the only stability needed. |
| Point nonmembership promoted to neighbourhood | Not used: the positive kappa margin comes from the closed proper offset cover, followed by transport. |

The proof, not failed finite sampling, covers the full stated domains. No mathematical executable, floating arithmetic, serialized certificate, empirical observation or measured method improvement is involved.

## 8. Adjudication, changed uncertainty and next obstruction

Math-verification verdict: **PASS AT CLAIM CEILING**, exposed internal proof. **PROVED:** the fixed-A m-positive robust-hole theorem and nowhere-denseness above. **FALSIFIED:** only the explicitly weakened unperturbed-centre, separation-free and general closed-projection shortcuts. Source inspection facts have **CERTIFIED_RANGE** scope. **NOT_TESTED:** the field-span Lemma4.2, its full Lemma5.2/countable/generic distinct-distance application, full Theorem1.3, lower theorem, complete paper, new Euclidean value, novelty, human review and formal verification.

The uncertainty changed from an algebraic cover with a missing geometric consumer to a verified composition across **all** legitimate parameters. Noncompact parameter dependence does not obstruct this route because exact relations remain on the original witnesses; offset algebra supplies a uniform excluded neighbourhood. The lesson transfers to other algebraically constrained boundary configurations. Do not repeat radius grids, coefficient compactness assumptions, settled m=0 upper arguments or this completed fixed-family composition without a new mathematical reason.

Before choosing a global application, rerank the actual remaining frontier. The selected pages identify a specific unverified dependency: source18's distinct-distance consumer uses Lemma4.2 over the generated field Q(z_1,...,z_m). Its literal hypotheses, finite-field-span concentration, quantitative n threshold and proof coverage require their own bounded source gate. A countable-union argument alone would not verify that imported combinatorial reduction. No assertion about its unread proof is made here.

The source register (historical local record; not distributed here) and page review (historical local record; not distributed here) give exact physical-page extents, representation hashes and parser limits. New visual18 only; all four full-text pages are rereads. Same underlying source, no new estate path or independent evidence count. Source/raw hashes support local custody rather than external tamper resistance or mathematical truth. No external action occurred.

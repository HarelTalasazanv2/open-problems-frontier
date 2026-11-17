# Audited historical reading edition

**Current audited claim:** PROVED: Every origin-symmetric full-dimensional convex body admits a symmetric polytope approximation with independent positive Hausdorff and whole-facet diameter tolerances.

**Claim ceiling:** Existence and strict tolerances only; no facet-count algorithm or novelty claim.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M10: small-facet approximation of symmetric convex bodies

Cycle097,2026-10-29UTC. **PROVED internally: the known source Lemma3.4, with Hausdorff and facet-diameter tolerances separated.** Its strict-convexification and compact cutting-depth steps are reconstructed below. A fine-net shortcut for arbitrary convex bodies is FALSIFIED, and a literal side-label assertion in the source is FALSIFIED locally and corrected explicitly. Neither finding refutes the approximation theorem.

Claim ceiling: a finite-dimensional convex approximation lemma and its exact audit findings. No full genericity/nowhere-denseness theorem, graph compactness step, Euclidean chromatic bound, novelty, independent external review or formal verification is established.

## 1. Source contract and exact statement

The frozen attempt (historical local record; not distributed here) follows the 096 source gate (historical local record; not distributed here). The actual primary text is Alon–Bucić–Sauermann, *Unit and distinct distances in typical norms*, [arXiv2302.09058v2](https://arxiv.org/abs/2302.09058v2), revised2024-11-07. The pinned33-page PDF has484598bytes, SHA-25687801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960. Physical6 defines B_d as compact convex origin-symmetric bodies in R^d with0 in their interior; all Hausdorff distances and diameters here are Euclidean. Physical8–9 contains Lemma3.4 and its proof, with Lemmas3.2–3.3 as predecessors. Exact reading/raster extents are in the 097 source register (historical local record; not distributed here).

**Theorem.** For every integer d≥1, every compact convex K⊂R^d with K=−K and0∈intK, and every ε,η>0, there exists a bounded full-dimensional origin-symmetric polytope P with0∈intP such that

\[
d_H(K,P)<\varepsilon,
\qquad \operatorname{diam}_2(F)<\eta
\quad\text{for every facet }F\text{ of }P. \tag{1}
\]

A facet is a whole (d−1)-dimensional face, not a simplex in a subdivision of a larger face. A polytope is the convex hull of finitely many points, equivalently a bounded finite-halfspace intersection; this elementary finite-dimensional equivalence and the supporting-face characterization are standard imported facts. Compactness, Euclidean norm properties and finite-dimensional separation are the other foundations used here. No Klee generic-strict-convexity theorem is imported.

The source has one tolerance μ, requiring both distances in(1) to be strictly below μ. Its statement gives(1) by taking μ=min{ε,η}; conversely ε=η=μ gives its statement. Thus the separated formulation changes bookkeeping, not the known result's mathematical strength. Dimension1 is included explicitly: K=[−a,a], a>0, itself is a polytope, its facets are singletons, and P=K works.

## 2. Strict convexification with a radial error bound

Assume d≥2. Choose r,R>0 with rD⊂K⊂RD, where D is the closed Euclidean unit ball. Let p be the Minkowski gauge of K. It is a norm with unit ball K: positive homogeneity and symmetry follow from scaling/K=−K, convexity gives the triangle inequality, rD gives finiteness, and K⊂RD gives p(x)≥||x||₂/R. In particular p is continuous, with p(x)≤||x||₂/r.

For τ>0 define

\[
p_\tau(x)=p(x)+\tau\|x\|_2,\qquad
C=\{x:p_\tau(x)\le1\}. \tag{2}
\]

This is a norm and C is a compact origin-symmetric full-dimensional convex body. It contains the ball of radius r/(1+τr), because p_τ(x)≤(1/r+τ)||x||₂. Also C⊂K.

The body C is strictly convex. If two nonzero vectors are not collinear, the Euclidean triangle inequality is strict, so the p_τ inequality is strict. For two distinct points of C on the same ray, both cannot have p_τ-value1; a convex combination with weights strictly between0 and1 therefore has norm<1. Points on opposite rays have strict cancellation, and a segment involving0 is immediate. Thus every open segment between distinct points of C lies in intC. No smoothness of K or uniqueness of its supporting normal is assumed.

For x∈K the point x/(1+τR) lies in C, since

\[
p_\tau\!\left(\frac{x}{1+\tau R}\right)
\le\frac{1+\tau R}{1+\tau R}=1.
\]

Consequently

\[
d_H(K,C)\le\frac{\tau R^2}{1+\tau R}. \tag{3}
\]

Take τ=ε/(4R²). Then d_H(K,C)<ε/4. This reproduces the strict-convexification ingredient of sourceLemma3.3 with a uniform radial estimate, without its small-radius case split.

## 3. Compact family of planes that could contain a large facet

Write h_C(n)=max_{x∈C}n·x for unit n. Since C⊂RD, its support function is R-Lipschitz on the unit sphere. Symmetry gives min_{x∈C}n·x=−h_C(n).

Use oriented planes H(n,a)={x:n·x=a}, with n∈S^{d−1} and |a|≤R. Define

\[
\mathcal A=\{(n,a):\exists x,y\in C,
\ n\cdot x=n\cdot y=a,\ \|x-y\|_2\ge\eta\}. \tag{4}
\]

This family is compact: it is the projection of a closed subset of the compact product S^{d−1}×[−R,R]×C×C. Thus there is no need to assume global continuity of section diameter as a plane moves. The two orientations of a geometric plane cause no difficulty.

For every (n,a)∈A, the plane contains two distinct points of C. It cannot be a supporting plane, because their open segment would lie both in the supporting plane and in intC, contradicting strict convexity. Hence

\[
g(n,a)=h_C(n)-|a|>0\quad((n,a)\in\mathcal A). \tag{5}
\]

If A is nonempty, continuity of g and compactness give

\[
\gamma=\min_{(n,a)\in\mathcal A}g(n,a)>0. \tag{6}
\]

If A is empty, no plane section of C has diameter≥η and no minimum over an empty set is taken. This case is handled separately below. In particular large tolerances do not create an undefined constant.

## 4. A symmetric net excludes every oversized facet

If A≠∅ set β=min{ε/4,γ/4}; if A=∅ set β=ε/4. Compactness of C supplies a finite β-net S0⊂C: for every x∈C some s∈S0 has ||x−s||₂≤β. Replace it by its union with its negative and add the2d points ±ρe_i, where ρ=r/(1+τr). All these points lie in C. The resulting finite symmetric set S is still a β-net, and P=convS contains the cross-polytope conv{±ρe_i}, which contains the Euclidean ball of radius ρ/√d. Therefore P is full-dimensional, bounded, origin-symmetric and has0 in its interior.

Since P⊂C and each point of C is within β of a point of S⊂P,

\[
d_H(C,P)\le\beta\le\varepsilon/4,
\qquad d_H(K,P)<\varepsilon/2<\varepsilon. \tag{7}
\]

When A≠∅, fix (n,a)∈A. Choose x_+,x_-∈C attaining the maximum and minimum of n·x. Their signed distances from the plane obey

\[
n\cdot x_+-a\ge\gamma,\qquad a-n\cdot x_-\ge\gamma.
\]

Net points s_+,s_- at Euclidean distance≤β from them then satisfy

\[
n\cdot s_+-a\ge\gamma-\beta>0,\qquad
a-n\cdot s_-\ge\gamma-\beta>0. \tag{8}
\]

Thus S has points in both open halfspaces of every plane in A. A facet F of P with diameter≥η would lie in a supporting plane H(n,a) of P. Since F⊂C, its two diameter witnesses put (n,a) in A. Equation(8) contradicts that plane being supporting. If A=∅, such a facet would itself contradict(4). In either case every facet has diameter<η. Together with(7) this proves(1). ∎

The proof treats all planes, not sampled normals, and every facet, including equality at the forbidden threshold η. It gives an existence construction with a positive compactness margin; it does not give an optimized facet count, a numerical value of γ for an unspecified body, or an efficient mesh algorithm.

## 5. Exact counterexamples and the literal source correction

### Fine sampling alone does not make arbitrary facets small

Take K=[−1,1]² and, for each integer m≥1,

\[
S_m=\{(-1+2j/m,-1+2k/m):0\le j,k\le m\}.
\]

This finite set is origin-symmetric, contains the four corners, and is a Euclidean √2/m-net of K. Yet convS_m=K for every m. Its facets have diameter2, even as the mesh tends to0, and d_H(K,convS_m)=0. **FALSIFIED:** arbitrarily fine point nets or Hausdorff approximation alone force small facets for every convex body. Triangulating a square edge does not change its facet. The source's strict-convexification step is essential to this proof route, not an optional visual refinement.

### A local side-label assertion in v2 is false as printed

Physical9, visually checked against the PDF, says that the point s1 chosen close to b1 must be on the same side as b2, after declaring b1 and b2 on opposite sides. The valid inequality shows instead that s1 stays on **b1's** side, and s2 stays on **b2's** side.

An exact local witness to the printed assertion uses the strictly convex Euclidean unit disk, H={x1=0}, b1=(−1,0), b2=(1,0), s1=b1 and s2=b2. The approximation errors are0, so they satisfy any of the source's positive proximity tolerances; these endpoints can be included in any required finite symmetric net. But s1 and b2 lie on opposite sides. Thus the literal side assertion is **FALSIFIED**. Correcting the one label gives the intended opposite-side net conclusion, as proved quantitatively in(8). This is a local label slip, not a disproof of Lemma3.4, and the source file is not altered.

The source's minimum-depth presentation also leaves the empty exceptional-family case implicit. Section3–4 supplies that branch. The reconstruction proves compactness through witness pairs and continuity of the support function, so it does not rely on an unproved moving-section continuity assertion. Norms in all proximity inequalities are explicitly Euclidean here. These changes preserve the source theorem's statement while making the necessary reasoning explicit.

### Boundary and degeneration controls

Dimension1, arbitrary ε/η ratios, flat initial K, small positive τ, redundant points in S, changing facet combinatorics and the empty family A are covered above. Full dimensionality and0∈intK are retained; lower-dimensional sets are outside B_d. Strict inequalities in the conclusion have a margin in(7)–(8). No conclusion is inferred from a finite grid or failure to find a bad plane.

## 6. Dependency adjudication and remaining gap

| Claim | Outcome | Exact scope |
|---|---|---|
|M10-SMALL-FACET-APPROX-C097|PROVED|Theorem(1), equivalent to sourceLemma3.4, with all stated dimensions and tolerances.|
|M10-STRICT-CONVEXIFICATION-C097|PROVED|Norm p+τ||·||₂, strict convexity, interior and radial error(3).|
|M10-CUTTING-DEPTH-C097|PROVED|Compact witness-pair plane family and positive uniform cutting depth for nonempty A; explicit empty branch.|
|M10-DENSE-NET-SHORTCUT-C097|FALSIFIED|Fine nets/Hausdorff approximation imply small facets for arbitrary bodies; square grids refute this.|
|M10-SOURCE-SIDE-LABEL-C097|FALSIFIED|Only the literal same-side-b2 assertion; corrected local inference and source theorem survive.|
|M10-GEOMETRY-SOURCE-C097|CERTIFIED_RANGE|Actual read source definitions/lemmas and visual source correction at recorded extents.|
|M10-FULL-GEOMETRIC-ASSEMBLY-C097|NOT_TESTED|Boundary transfer, facet-offset stability, angular assignment, remaining m>0 dependence, full nowhere-denseness and infinite graph compactness are not adjudicated here.|

The source-matched norm regularization is shared with the published proof. The radial estimate, compact witness-family/support-depth derivation and explicit exact controls were reconstructed within one exposed internal audit. This is not blind reproduction, independent human review or formalization. No executable mathematical instrument, numerical certificate, empirical data or measured speed comparison was used.

The fresh2026 primary owner/version and its pinned introduction were checked for M10 status; the author describes the Euclidean problem as open with the familiar5-to7 bracket. That is **OPEN_AS_REPORTED** with bounded source coverage, not exhaustive current literature or new sharp bounds. The generic typical-norm theorem, the named Euclidean norm and this geometric lemma remain distinct. Proving(1) gives no new Euclidean colouring.

The next discriminating action is M10 facet-offset stability (historical local record; not distributed here), SELECTED_NOT_TESTED: verify whether strict small-facet bounds persist for all nearby support offsets, allowing redundant constraints and changing combinatorics, with a Hausdorff control. This is a separate missing input in the093 geometry list. SourceLemma3.5's adjacent proof was read but is not promoted by this run; the full geometric assembly remains held.

# Audited historical reading edition

**Current audited claim:** PROVED: The displayed rational all-subset capacity holds on a comeager class containing a dense G-delta subset of norm bodies.

**Claim ceiling:** Q-rank and distinct unoriented lines; no probability, all-norms assertion or conclusion that the whole class is G-delta.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Generic rational-span capacity: countability and topology

2026-10-30 UTC, cycle101. **PROVED internally: the known generic rational-span capacity application previously conditional in092.** The fixed-family100 result supplies nowhere-denseness; exact membership/countability and the required Baire topology are established below. No infinite-graph colouring theorem, full2026paper reproduction or new Euclidean chromatic bound is claimed.

The submitted packet (historical local record; not distributed here), fresh freeze (historical local record; not distributed here) and dependency custody (historical local record; not distributed here) preserve the exact object and exposed expected result. Ordinary classical mathematics(ZFC), Euclidean compactness, finite-dimensional convexity and elementary linear algebra are the foundations. No unproved hyperspace-completeness or Baire assertion is substituted for the topology checks.

## 1. Precise statement and claim ceiling

For fixed d≥2 let B_d be compact convex origin-symmetric bodies B⊂R^d with0∈intB, with Euclidean Hausdorff metric. All ranks and spans in the capacity statement are over Q. Set

\[
 G_d=\left\{B\in\mathcal B_d:
 |S|\leq d\,\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}S
 \text{ for every finite }S\subseteq\partial B
 \text{ on distinct unoriented lines}\right\}.
\]

“Distinct unoriented lines” means no two members are parallel as real vectors; for norm-unit vectors it is equivalent to forbidding both u and −u as separate representatives. Zero is never on ∂B. The empty set has rank0.

For every ℓ≥1, A∈Q^((dℓ+1)×ℓ) and rational0<η<π/2, let E_(A,η) be the exact100 family: B admits N=dℓ+1 boundary vectors u_j with all relations u_j=Σ_(i=1)^ℓ a_ji u_i and every pair of acute unoriented line angles>η. Closures below are relative to B_d. Define

\[
 R_d=\mathcal B_d\setminus\bigcup_{\ell,A,\eta}
 \overline{E_{A,\eta}}.
\]

**Theorem.** G_d is comeager, and R_d is a dense G_delta subset of B_d contained in G_d. The same one class G_d works simultaneously for every finite configuration. Equivalently, for every finite distinct-line U⊂∂B and every T⊂U,

\[
 |U\cap\operatorname{span}_{\mathbb Q}T|\leq d|T|. \tag{1}
\]

For d=1 the capacity holds for every norm body directly. We do not infer that G_d itself is G_delta merely from containing R_d; no such additional classification is needed or asserted here. A generic statement does not include every named norm, and is not a probability statement.

**Claim ceiling:** internal reconstruction of this known countable rational-capacity/topology result, including explicit density and a G_delta subset. The100 proof is an internally proved dependency with current identity/contract checks, not matching external human/formal review. Infinite colouring, m>0 rational functions and new open-problem resolution remain outside scope.

## 2. Complete ambient Hausdorff space

Let X_d consist of all nonempty compact convex origin-symmetric subsets of R^d, allowing degenerate sets. Each contains0 by convexity and symmetry. We prove X_d is complete.

Let K_n be Hausdorff-Cauchy. All K_n lie in a common closed Euclidean ball of some finite radius R: compare a sufficiently late tail with one fixed compact K_N within distance1, then include the finitely many earlier bounded sets. Put f_n(x)=dist(x,K_n). Closest-point comparisons give

\[
 |f_n(x)-f_m(x)|\leq d_H(K_n,K_m)\quad\text{for every }x.
\]

Thus the pointwise finite limit f exists with uniform error sup_x|f_n(x)−f(x)|→0; boundedness of the functions on all R^d is not assumed. The limit is nonnegative and1-Lipschitz, f(0)=0 and f(x)≥||x||_2−R. Hence

\[
 K=\{x:f(x)=0\}
\]

is nonempty, closed, bounded and compact. For x∈K, dist(x,K_n)=f_n(x) is uniformly at most the preceding uniform error. For the other directed distance, suppose some subsequence has y_k∈K_(n_k) with dist(y_k,K)≥ε>0. A further subsequence converges to y in the common compact ball. Since f_(n_k)(y_k)=0 and the convergence to f is uniform, f(y_k)→0, so f(y)=0. Then dist(y_k,K)≤||y_k−y||_2→0, a contradiction. Therefore d_H(K_n,K)→0.

For x,y∈K choose x_n,y_n∈K_n tending to them. For every λ∈[0,1], λx_n+(1−λ)y_n∈K_n; uniform distance convergence implies λx+(1−λ)y∈K. Similarly −x_n∈K_n implies −x∈K. Thus K is convex and origin-symmetric and belongs to X_d. This proves completeness without invoking an uninspected hyperspace theorem.

## 3. Norm bodies are an open subspace

Fix B∈B_d and choose r>0 with rD_2⊆B. For L∈X_d with d_H(B,L)<r/2, support-function comparison gives, for every Euclidean unit vector v,

\[
 h_L(v)\geq h_B(v)-d_H(B,L)>r/2.
\]

We verify this forces (r/2)D_2⊆L. Otherwise let x in that ball lie outside L, choose a nearest y∈L, and set n=(x−y)/||x−y||_2. Minimality on segments in L yields n·(z−y)≤0 for all z∈L, hence h_L(n)=n·y<n·x≤||x||_2≤r/2, contradicting the support bound. The nearest-point inequality follows by expanding the squared distance at y+t(z−y) and letting t decrease to0.

Consequently L has0 in its interior, so B_d is open in X_d. We do not claim B_d is closed or complete in its raw Hausdorff metric.

## 4. The needed Baire conclusion, proved by nested balls

Let O_1,O_2,… be open dense subsets of B_d and let W⊂B_d be nonempty open. Because B_d is open in X_d, these are open relative to the ambient complete space as well. Choose C_1∈W∩O_1 and a positive radius r_1<1/2 such that the closed ambient ball F_1=closedBall_X(C_1,r_1) is contained in W∩O_1⊂B_d.

Inductively choose

\[
 C_{k+1}\in\mathbb B_X(C_k,r_k/2)\cap O_{k+1},
\]

which is possible by density within the nonempty open norm-body ball. Choose0<r_(k+1)<min{r_k/4,2^(−k−1)} small enough that the closed ambient ball F_(k+1) lies inside that open intersection. The F_k are nested, nonempty and closed in X_d, with radii tending to0. The centres are Cauchy; completeness gives a limit C∈X_d in every F_k. Crucially F_1 is wholly inside B_d, so C is a norm body, not a degenerate limit. Also C∈W and C∈O_k for all k.

Thus every countable intersection of open dense subsets of B_d is dense. This is the precise Baire form used below. No unsupported inference from raw norm-body completeness is needed.

## 5. Exact countable cover of all finite violations

Let F_d=B_d\G_d. For each fixed finite size, rational matrices form a countable set, and rational positive separators form a countable set. Taking the countable union over integers ℓ preserves countability. This enumerates relation data, not uncountably many real point configurations.

We prove

\[
 F_d=\bigcup_{\ell,A,\eta}E_{A,\eta}.              \tag{2}
\]

If B∈F_d, some finite distinct-line S⊂∂B satisfies |S|>d r, where r=dim_Q span_Q S. Here r≥1 because S is a nonempty set of nonzero vectors. Choose a Q-basis b_1,…,b_r from S. Since |S|≥dr+1 and dr+1≥r, select exactly dr+1 members of S containing that basis, and relabel the basis first. Rational coordinates give a rational(dr+1)×r matrix A with all required relations, including the first r rows. The finite distinct-line list has a positive minimum acute angle; choose rational0<η smaller than it and than π/2. Then B∈E_(A,η).

Conversely B∈E_(A,η) supplies a set S of exactly N=dℓ+1 distinct-line vectors. Its Q-rank is at most ℓ, so |S|=dℓ+1>d rank_Q S. Thus B∈F_d. Rank-deficient A and non-identity first rows do not invalidate this implication.

The [100 theorem](m10-rational-family-hole-c100.md) proves every E_(A,η) nowhere dense. Therefore(2) is meagre and G_d is comeager. Each O_(A,η)=B_d\closure(E_(A,η)) is open dense. Section4 makes their countable intersection R_d dense; by definition it is G_delta. Since each E lies in its closure, R_d⊆G_d. This also proves the good class is nonempty and dense; a purely formal comeager label in an unverified non-Baire space is not being used.

No uniform angle lower bound across all configurations is assumed. The rational η is selected separately for each bad finite witness and absorbed into the one countable index set, so the conclusion holds for all finite configurations simultaneously.

## 6. Inclusive spans and dimension1

Suppose B∈G_d and U⊂∂B is finite on distinct lines. For T⊂U put C=U∩span_Q T. The set C is also a finite distinct-line unit set and rank_Q C≤|T|. Hence |C|≤d rank_Q C≤d|T|. If T=∅ then C=∅, because0 is not a unit vector.

Conversely suppose(1) holds for every such U,T. For any finite distinct-line S take U=S and T a Q-basis of S. Then U∩span_Q T=S, so |S|≤d|T|=d rank_Q S. This proves the exact equivalence. For a fixed finite U the same reasoning applied to its subsets proves the old092(C)/(I) crosswalk.

When d=1 a norm body is[−a,a], a>0, whose boundary has one unoriented line. Every admissible S has size0 or1 and satisfies the capacity with d=1. Thus G_1=B_1 directly; no d≥2 fixed-family lemma is applied to it.

## 7. Exact adversarial controls

**FALSIFIED — raw B_d is complete in the Hausdorff metric.** The norm bodies B_n=(1/n)D_2 satisfy d_H(B_n,B_m)=|1/n−1/m| and converge in X_d to{0}, which is not a norm body. In d=2 the thin rectangles[−1,1]×[−1/n,1/n] likewise converge to a segment. Uniqueness of metric limits rules out a different limit inside B_d. The corrected complete ambient space/open-subspace proof establishes Baire, not completeness of B_d. The primary source asserts Baire and is not refuted by this control.

**FALSIFIED — substitute real rank in the generic capacity statement.** For any B∈B_d,d≥2, choose d²+1 distinct unoriented rays and take one boundary point on each. This is always possible by radial intersection of a norm body with rays. Their real rank is at most d, so their number exceeds d times real rank. The real-rank-substituted good class is empty for every d≥2. Rational rank is a different quantity and is not bounded by the physical dimension.

**FALSIFIED — allow both antipodal representatives and retain the same generic bound.** For every two-dimensional norm, choose a unit u and continuously move a unit v from u to−u on the norm-unit circle. The function ||v−u|| runs from0 to2, so some v satisfies ||v−u||=1. Here v≠±u, hence u,v are real-linearly independent. With w=v−u, the six distinct vectors ±u,±v,±w are unit vectors and have Q-rank2. They violate6≤2·2. This holds for every B∈B_2, making the altered good class empty. The continuous unit-circle path exists by radially normalizing a Euclidean semicircle; norm continuity follows from the triangle inequality and a positive Euclidean inner ball. This is not merely one exceptional-norm example.

**FALSIFIED — arbitrary uncountable unions of nowhere-dense sets remain meagre.** Every singleton{B} in B_d is closed and has empty interior: (1+t)B gives distinct norm bodies approaching B as t decreases to0. In fact d_H((1+t)B,B)=t max_(x∈B)||x||_2, using radial comparison for the upper bound and a maximum-radius point for the lower bound. But the union of all those singletons is the entire nonempty Baire space B_d. Countability of the rational relation data cannot be discarded. This refutes a general union inference, not the actual rational-index proof.

Healthy cases include empty sets/T, repeated matrix descriptions, empty E-families and d=1. The explicit five rational unit vectors of100 show the Euclidean disk is outside G_2; generic membership is not inferred for that named body. No chromatic lower bound follows from its capacity failure. We do not claim G_d itself is G_delta from its containment of R_d.

## 8. Source increment and mathematical trust boundary

The [primary original source](https://arxiv.org/abs/2302.09058v2), revised2024-11-07, is33pages/484598bytes, SHA-25687801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960. Physical6 explicitly asserts the Hausdorff norm-body space is Baire; its cited external theorem is not claimed independently retrieved. Sections2–4 above give the needed topology directly. Physical17–19 and the [092 dossier](m10-vector-partition-c092.md) supply the exact rational-family/countability conventions. These and text10 were reread without new text credit; current092/100 inputs match their original manifests. The previous092 conditional capacity conclusion is now internally established at this scope.

New full-text reading covers physical11–12, and new full visual reading covers6 and12. The exact register (historical local record; not distributed here) records lineage, hashes and page/line extents. Combined full text is physical1–12,17–26:22 selected pages of33, with prior partial extents retained. The source increment exposes the entropy/coordinate-partition proof of Lemma4.3: independence is over its specified field F and each single-direction edge subgraph must be a forest. This is a different combinatorial consumer; its complete proof chain is not promoted as a consequence of our capacity theorem.

A useful exact source-scope control drops only that forest hypothesis: take V=Q,u_1=1,p_1=0,p_2=1,p_3=2 and G=K_3. Every edge difference lies in span_Q(1), but3>(3/2)log_2 3 because log_2 3<2. Thus the forest-free span-edge bound is false. This is an abstract graph satisfying the other stated span conditions, not a Euclidean unit-distance triangle on collinear points and not a refutation of the source lemma. The base2 convention was checked on physical6 and12.

Fresh [2026 owner metadata](https://arxiv.org/abs/2609.36220) still lists v1. Its cached exact matching-v1 introduction was reread: Euclidean open/5-to7 statements remain AS_REPORTED under a bounded2026-10-30 owner/version/body check, not new bound proofs or exhaustive current absence/novelty coverage. No fresh PDF body was downloaded. Same-work representations and repeated reads are not independent sources or reviewers.

All construction and review is by the same exposed internal actor. The100 fixed-family proof is inherited internal mathematical evidence, with artifact identity and exact contract rechecked; the countability reduction is rederived and the topology proof supplied here. No external human/model review, formal verification, mathematical executable, numerical certificate or measured performance gain occurred. Finite-dimensional compactness, basic convexity and standard classical set theory remain named foundations.

## 9. Verdict and next obstruction

| Object | Outcome | Exact ceiling |
|---|---|---|
| Countable generic Q-capacity and inclusive spans | PROVED | Every finite distinct-line configuration, common comeager class |
| Ambient completeness/open norm-body space/nested-ball Baire | PROVED | Raw norm-body completeness explicitly excluded |
| Explicit dense G_delta subset R_d | PROVED | No stronger classification of G_d itself asserted |
| Raw completeness, real rank, antipodal duplication, uncountable-union variants | FALSIFIED | Only the exact altered statements above |
| Forest-free source span-edge bound | FALSIFIED | Abstract graph control, not unit-distance or source-theorem disproof |
| Infinite graph colouring/new Euclidean bound/m>0 branch | NOT_TESTED | Separate applications and source obligations |

This closes the old conditional generic-capacity application. The next discriminating action is a separately specified finite-to-infinite colouring bridge: match the092/093 finite colour constructions and compactness theorem, including uncountable vertex sets and endpoint conventions. A generic capacity result by itself is not a global colouring, and no automatic extension is made in this cycle.

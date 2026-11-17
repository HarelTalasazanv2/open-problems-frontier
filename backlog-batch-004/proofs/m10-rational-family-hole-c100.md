# Audited historical reading edition

**Current audited claim:** PROVED: Every specified m=0 rational dependence family with separated boundary directions is nowhere dense in norm-body Hausdorff space.

**Claim ceiling:** Fixed family only; the body center may move and no closedness of the existential bad family is assumed.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Robust exclusion of a fixed rational-dependence family

2026-10-30 UTC, cycle100. **PROVED internally: the m=0 case of the known sourceLemma5.3.** The finite parameter exclusion093 and geometry097–099 compose into a robust Hausdorff hole for every fixed rational family. This is not a new Euclidean chromatic bound, a countable generic-capacity application, or the m>0 rational-function case.

The submitted packet (historical local record; not distributed here), fresh freeze (historical local record; not distributed here) and dependency custody (historical local record; not distributed here) preserve the exact claim, expected-result exposure, time limit and named inputs. Artifact identity was checked separately from mathematical scope.

## 1. Exact statement and claim ceiling

Let d≥2, ℓ≥1, N=dℓ+1, A=(a_ji)∈Q^(N×ℓ), and rational0<η<π/2 be fixed. Let B_d denote the compact convex origin-symmetric bodies in R^d with0 in their interior. Distances, radii and diameters are Euclidean; offset-space distances use the maximum norm.

Let E_(A,η)⊂B_d consist of B admitting u_1,…,u_N∈∂B with

\[
 u_j=\sum_{i=1}^{\ell}a_{ji}u_i\quad(1\leq j\leq N),
 \qquad\vartheta(u_j,u_k)>\eta\quad(j\ne k),       \tag{1}
\]

where θ is the acute angle between unoriented lines. This is the source's A_(A,η) for m=0. No rank assumption or assumption that the first ℓ rows of A form an identity matrix is imposed.

**Theorem.** For every B_0∈B_d and ε>0 there are B∈B_d and ρ>0 such that

\[
 d_H(B,B_0)<\varepsilon,
 \qquad \mathbb B_H(B,\rho)\subseteq
 \mathbb B_H(B_0,\varepsilon)\setminus E_{A,\eta}. \tag{2}
\]

Here the balls are relative to B_d. Consequently E_(A,η) is nowhere dense in B_d. Its closedness is not assumed or established. The radius depends on the fixed family and the local data; no uniform or optimized numerical radius is claimed.

**Claim ceiling:** a complete internal reconstruction of one known fixed-family nowhere-denseness argument under named internally proved geometric inputs. Countable generic-capacity/Baire application, all graph colourings, m>0 algebraic dependence, novelty, external human review and formal verification remain outside this result.

## 2. Inputs and the order of choices

The exact contracts of the following local inputs were reread and their files matched to their original immutable manifests:

| Input | Scope used here | Evidence limitation |
|---|---|---|
| 093 finite parameter proof (historical local record; not distributed here) | Finite proper-hyperplane cover for all injective index/sign choices; empty case h<N | Internally proved; no external review |
| [097 small-facet theorem](m10-small-facet-approx-c097.md) | Independent positive Hausdorff and whole-facet tolerances for arbitrary norm bodies | Known lemma internally reconstructed |
| [098 offset theorem](m10-facet-offset-stability-c098.md) | Strict facet bound persists under nearby fixed-normal offsets; d_H≤RΔ/s_min | Full facet-diameter continuity is not needed |
| [099 boundary/facet theorem](m10-boundary-facet-transport-c099.md) | Boundary transfer, angular exclusion, distinct active rows and support errors with unit normals | Same exposed internal actor and source |

The finite parameter step is reconstructed again in Section4, so its dimension/properness logic is visible in the composition. Earlier proofs are not silently upgraded into external assurance.

The choice order is

\[
 (B_0,\varepsilon,A,\eta)\to r,\alpha,P_0,o,s,R,D_*
 \to\tau,a\to H\to t,\kappa\to B,\beta,\rho.
\]

In particular the offset window is fixed before the generic parameter tuple, and the final body radius is chosen after the positive parameter margin. Nothing requires a later radius to determine an earlier object.

## 3. Small facets, a preserved inner ball, and an offset window

Fix B_0 and ε. Choose r>0 with2rD_2⊆B_0, possible because0 is interior. Set

\[
 \alpha=\min\{\varepsilon/4,r/2\},\qquad
 D_0=r\sin(\eta/3),\qquad D_*=r\sin(\eta/2).
\]

By097 choose a symmetric full-dimensional polytope P_0 with0 interior, d_H(P_0,B_0)<α, and every whole facet of diameter<D_0. Since0<η<π/2,

\[
 D_0<D_*<r\sin\eta.                              \tag{3}
\]

The099 boundary lemma sends each b∈∂P_0 to a point of ∂B_0 within distance<α. Every point of ∂B_0 has norm≥2r. Hence ||b||_2>2r−α≥3r/2>r, and rD_2⊆P_0. To justify this last implication explicitly, if a point of rD_2 were outside P_0, the segment from0 to it would first leave P_0 at a boundary point of norm≤r, a contradiction. This uses convexity, closedness and0 interior.

Choose a finite symmetric support description

\[
 P_0=\{x:|o_i\cdot x|\leq s_i, 1\leq i\leq h\},
 \quad\|o_i\|_2=1,
 \qquad s_i\geq r.
\]

Such a description is obtained from its antipodal facet pairs and rescaling normals. Redundant or duplicate rows are harmless. Put R=max_(P_0)||x||_2>0 and s_min=min_i s_i≥r.

By098 there is τ>0 such that all positive offsets w with ||w−s||∞<τ give P(w) whose whole facets have diameter<D_*. Fix

\[
 a=\min\{\tau/2,\varepsilon r/(8R),r/2\}>0,
 \qquad U=\prod_{i=1}^{h}(s_i,s_i+a).              \tag{4}
\]

For every w∈U the offsets are outward, so P_0⊆P(w) and rD_2⊆P(w). Also Δ=||w−s||∞<a≤r/2<s_min and Δ<τ. The098 estimate gives

\[
 d_H(P(w),P_0)\leq R\Delta/s_{\min}
 <Ra/r\leq\varepsilon/8.                         \tag{5}
\]

Thus all such P(w) are valid norm bodies with facet diameter<D_*, and

\[
 d_H(P(w),B_0)<\varepsilon/4+\varepsilon/8
 =3\varepsilon/8.                                \tag{6}
\]

The use of min in α handles every ε>0 without a hidden small-ε restriction. Outward offsets preserve the inner radius, while strict facet slack is supplied by(3); a fixed combinatorial type is never assumed.

## 4. All achievable parameters lie in a finite closed proper union

For these fixed normals, call w∈R^h achievable when there are vectors u_1,…,u_N∈R^d satisfying all relations in(1), and an injection φ:{1,…,N}→{1,…,h}, with

\[
 |o_{\phi(j)}\cdot u_j|=w_{\phi(j)}\quad(1\leq j\leq N).
\]

Boundary/angle conditions are deliberately omitted from this parameter definition; it is a superset of the parameters the final bad-body assumption can produce.

If h<N there are no injections, hence no achievable tuples; set H=∅. If h≥N, fix an injection φ and a sign vector σ∈{−1,1}^N. The N expressions

\[
 L_j(v_1,\ldots,v_\ell)
 =\sigma_j o_{\phi(j)}\cdot\sum_{i=1}^{\ell}a_{ji}v_i
\]

are linear forms on a space of dimension dℓ=N−1. There is a nonzero c∈R^N with Σ_j c_jL_j=0. Every tuple achievable with those signs belongs to

\[
 H_{\phi,\sigma}
 =\{w:\sum_{j=1}^{N}c_j w_{\phi(j)}=0\}.
\]

This is a proper hyperplane of R^h: φ is injective, so the nonzero coefficients cannot cancel by being assigned to the same parameter coordinate. Additional relations on v_1,…,v_ℓ from the first ℓ rows of A merely restrict their admissible values; allowing them to range freely is a valid enlargement. No full rank or identity-row assumption is used.

Take H to be the union over every injection and every sign vector. There are at most h!/(h−N)! times2^N members when h≥N. This is a finite analytic cover, not an enumeration performed by a program. A zero signed dot product may take either sign, so no missing boundary sign case occurs. Duplicate hyperplanes cause no difficulty. All achievable parameters lie in H.

The finite union H is closed and has empty interior. One elementary proof of the latter successively removes each proper hyperplane from a nonempty open set, retaining a smaller nonempty open ball at every finite step. No Baire theorem is needed for finitely many hyperplanes.

Choose t∈U\H. Since U\H is open, choose κ>0 with

\[
 \overline{\mathbb B}_\infty(t,\kappa)\subseteq U\setminus H. \tag{7}
\]

The same choice is possible when H=∅. Define B=P(t). Equations(3)–(6) give every geometric condition needed below.

## 5. A parameter margin becomes a whole-body exclusion ball

Set

\[
 \beta=\frac{r\sin\eta-D_*}{2+\sin\eta}>0,
 \qquad
 \rho=\min\{\kappa/2,\beta/2,\varepsilon/8,r/4\}>0. \tag{8}
\]

Then ρ<r and (D_*+2ρ)/(r−ρ)≤sinη. Suppose B′∈B_d has d_H(B′,B)<ρ and belongs to E_(A,η). Retain the original boundary vectors u_j and their exact A-relations. Apply099 to P=B, inner radius r, facet bound D_* and error ρ. It yields distinct indices φ(j) and a positive support tuple t′ with

\[
 t'_{\phi(j)}=|o_{\phi(j)}\cdot u_j|,
 \quad t'_i=t_i\text{ on unused coordinates},
 \qquad\|t'-t\|_\infty<\rho<\kappa.              \tag{9}
\]

If h<N the distinct indices are already impossible, which settles that branch. Otherwise the unchanged u_j and the injection make t′ achievable, so t′∈H. But(7) and(9) give t′∉H, a contradiction.

Only the support parameters were changed. Substituting approximating points b_j for the original u_j in their rational relations would not preserve those relations and is not done here. The b_j are used solely to obtain distinct active indices and the error bound.

Thus B_H(B,ρ) is disjoint from E_(A,η). For any B′ in that ball, (6) and ρ≤ε/8 give

\[
 d_H(B',B_0)<\rho+3\varepsilon/8\leq\varepsilon/2<\varepsilon.
\]

This proves(2), with positive spare margin and no circular radius choice. Neither high precision nor finite sampling stands in for the neighbourhood statement.

## 6. Nowhere-denseness without closedness of the bad family

Every nonempty relatively open W⊂B_d contains some B_H(B_0,ε). Equation(2) produces a nonempty open ball V⊂W disjoint from E_(A,η). An open set disjoint from a set is also disjoint from its closure: each point has a smaller neighbourhood within that open set. Hence V∩closure(E_(A,η))=∅. No nonempty W can be contained in that closure, so its interior is empty. This is precisely nowhere-denseness.

The proof never asserts that E_(A,η) itself is closed. It also does not invoke completeness of B_d, Baire category, countability over all matrices or an infinite-graph compactness theorem. Those belong to later applications.

## 7. Exact adversarial findings

**FALSIFIED — the stronger unperturbed-centre assertion.** In d=2 take ℓ=2,N=5,η=1/10 and

\[
 A=\begin{pmatrix}
 1&0\\0&1\\3/5&4/5\\-3/5&4/5\\5/13&12/13
 \end{pmatrix}.
\]

For B_0=D_2, let u_j be these rows, interpreted as vectors. All have Euclidean norm1 and satisfy the A-relations with u_1=e_1,u_2=e_2. The ten absolute pair determinants, in lexicographic pair order, are

\[
 1,\ 4/5,\ 4/5,\ 12/13,\ 3/5,\ 3/5,\ 5/13,
 \ 24/25,\ 16/65,\ 56/65.
\]

Their minimum16/65 exceeds1/10≥sin(1/10). Since all vectors are unit and their line angles are acute, every pair has angle>η. Thus D_2∈E_(A,η), and no exclusion ball centred at this B_0 can be disjoint from the family. The literal theorem permits a nearby centre B, so it survives. This also blocks promotion from a generic norm result to the named Euclidean norm; no chromatic lower bound follows from this witness.

**FALSIFIED — omitting angular separation.** Let ℓ=1,N=d+1 and take every entry of A to be1. With no separation condition, every B∈B_d belongs to the resulting family: choose any u∈∂B and repeat it N times. That family equals the entire nonempty B_d and is not nowhere dense. The positive line-separation assumption is substantive.

**FALSIFIED — point nonmembership alone implies a disjoint neighbourhood.** In the same norm-body metric consider S={qD_2:q>0 rational}. The body √2D_2 is outside S, yet every Hausdorff neighbourhood meets S because d_H(qD_2,√2D_2)=|q−√2|. This is a counterexample to the general point-only inference, not an assertion that S is our fixed A-family. Our proof instead uses the closed parameter union(7) and the transport bound(9).

Healthy degeneracies are also explicit. A=0 makes E empty because its relations force all u_j=0, excluded from norm-body boundaries. Rank-deficient A and non-identity first rows only restrict a linear image further. For h<N no injection exists; it is not an empty collection silently treated as a nonzero hyperplane. Sign zeros, repeated descriptions, every ε>0, and all remaining body-neighbourhood inputs are covered analytically. No mathematical executable or numerical certificate is used.

## 8. Source increment and evidence limits

The [primary source](https://arxiv.org/abs/2302.09058v2), revised2024-11-07, is33pages/484598bytes, SHA-25687801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960. Its physical17 definition and19–20/22–23 m=0 argument were fully reread, with no new text credit. The m>0 algebraic branch is not adopted. The inspection register (historical local record; not distributed here) records exact extents and lineage.

New full-text reading covers physical1–2 and full visual reading covers2. Theorem1.1 there has a generic upper unit-edge count with a single exceptional set followed by every n and every n-point set; Theorem1.2 has a lower-edge construction for every norm and large n. These opposite quantifier patterns and edge-count conclusions are distinct from a chromatic value of a named norm. Their full global proofs are not reproduced here. The2024 introductory Euclidean bounds are historical statements, not a current-status attestation. Combined full text is physical1–10 and17–26:20 selected pages of33, not the whole paper; prior partial extents remain preserved.

Fresh [2026 owner metadata](https://arxiv.org/abs/2609.36220) still lists v1. The cached exact matching-v1 introduction was reread; its Euclidean open/5-to7 statements remain AS_REPORTED under a bounded2026-10-30 owner/version/body check. No new bound proof, fresh PDF body download, exhaustive recent-literature absence check or novelty claim occurred. Same-work representations are not independent sources or reviewers.

The proof is an exposed internal reconstruction using previously internally proved inputs; current artifact hashes and exact contracts were checked, not a fresh external audit of every predecessor. The fixed-matrix parameter argument actually needs only real coefficients, but no uncountable-union genericity claim is inferred. Publication, matching human/formal review and global claim-promotion gates remain separate. Performance is NOT_MEASURED.

## 9. Verdict and next obstruction

| Object | Outcome | Ceiling |
|---|---|---|
| Robust fixed rational-family hole and nowhere-denseness | PROVED | Known m=0Lemma5.3 internally reproduced under the named local inputs |
| Complete finite hyperplane parameter cover and radius order | PROVED | All injections/signs, h<N, degeneracies and strict margins explicit |
| Unperturbed-centre, separation-free, and point-only variants | FALSIFIED | Only those exact stronger/weakened inferences |
| Countable generic capacity/Baire and infinite colouring | NOT_TESTED | Fixed-family success does not automatically promote applications |
| m>0 rational-function family | NOT_TESTED | Separate algebraic-dependence obligation |

The changed uncertainty is whether the finite lemmas compose: they do, with a genuine excluded body neighbourhood and unchanged rational relations. What should not be repeated is another local radius or matrix grid after this assembly is closed. The immediate application requiring a fresh specification is countable generic rational-span capacity, including the topology/Baire scope and distinct-line membership; infinite graph colouring remains a separate bridge. No new Euclidean chromatic value or open-problem resolution is claimed.

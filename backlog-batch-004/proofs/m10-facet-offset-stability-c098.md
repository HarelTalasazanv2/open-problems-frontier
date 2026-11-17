# Audited historical reading edition

**Current audited claim:** PROVED: Positive fixed-normal offset perturbations obey the displayed radial Hausdorff bound and upper semicontinuity of maximum whole-facet diameter.

**Claim ceiling:** No adoption of the source's stronger individual-face continuity assertion.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M10: fixed-normal offset stability of whole-facet diameters

2026-10-29 UTC, cycle098. **PROVED internally at the stated finite-dimensional scope.** This closes a known geometric prerequisite used in Alon–Bucić–Sauermann, arXiv2302.09058v2, Lemma5.3, physical21–22. It does not prove that lemma's full nowhere-denseness assertion, a new Euclidean chromatic bound, or novelty. The submitted next packet (historical local record; not distributed here) and fresh frozen attempt (historical local record; not distributed here) are preserved.

## Exact statement and ceiling

Let d,h be positive integers. Fix nonzero vectors o_1,…,o_h in R^d, positive offsets s_1,…,s_h, and

\[
 P(t)=\{x\in\mathbb R^d: |o_i\cdot x|\leq t_i\quad(1\leq i\leq h)\}.
\]

Assume P(s) is bounded. All norms, diameters and Hausdorff distances below are Euclidean, except the explicitly specified maximum norm on offset space. A facet is an entire (d−1)-dimensional face, not a triangle in a subdivision. Define

\[
 s_{\min}=\min_i s_i>0,\qquad R=\max_{x\in P(s)}\|x\|_2,
 \qquad D(s)=\max_{F\text{ facet of }P(s)}\operatorname{diam}_2(F).
\]

For every positive offset vector t, P(t) is a compact full-dimensional origin-symmetric polytope with 0 in its interior. If

\[
 \Delta=\|t-s\|_\infty<s_{\min},\qquad \theta=\Delta/s_{\min},
\]

then

\[
 (1-\theta)P(s)\subseteq P(t)\subseteq(1+\theta)P(s),\qquad
 d_H(P(t),P(s))\leq R\Delta/s_{\min}.                 \tag{1}
\]

The maximum whole-facet diameter is upper semicontinuous at s:

\[
 \limsup_{t\to s,\ t_i>0}D(t)\leq D(s).              \tag{2}
\]

Consequently, for every ρ>D(s), there exists δ_*>0 such that all t with ||t−s||∞<δ_* have positive offsets and D(t)<ρ. Redundant and duplicate inequalities, inactive constraints, lower-dimensional supporting faces becoming facets, mixed inward/outward moves, and changes of combinatorial type are admitted. We prove existence, not an optimized or computed numerical δ_*.

**Claim ceiling:** an exact internal analytic stability lemma for fixed finite normal lists, with a Hausdorff bound and exact controls; no full genericity, angular-assignment assembly, m>0 dependence, infinite graph compactness, numerical certification, formalization, or external review.

## 1. Bodies, normalization, and radial containment

The Euclidean ball of radius r=min_i s_i/||o_i||_2>0 is contained in P(s). Thus P(s) is closed, bounded, full-dimensional and has positive finite R. Its symmetry follows from the absolute-value inequalities. For any positive t, put

\[
 a=\min_i t_i/s_i>0,\qquad b=\max_i t_i/s_i<\infty.
\]

Direct substitution gives aP(s)⊆P(t)⊆bP(s). In particular, boundedness, full dimension, symmetry and interior persist for every positive t; these assertions do not require a smallness condition. The intersection of finitely many closed halfspaces is a polyhedron, and its boundedness makes it a polytope. These elementary finite-dimensional polytope facts are the named foundations; no genericity theorem is imported.

For Δ<s_min, θ<1. For x∈P(s),

\[
 |o_i\cdot(1-\theta)x|\leq(1-\theta)s_i
 =s_i-\theta s_i\leq s_i-\Delta\leq t_i.
\]

For z∈P(t), |o_i·z|≤t_i≤s_i+Δ≤(1+θ)s_i, so z/(1+θ)∈P(s). This proves both containments in (1). Their directions are essential, particularly when some offsets increase and others decrease.

For x∈P(s), the comparison point (1−θ)x∈P(t) is within θR. For z∈P(t), let x=z/(1+θ)∈P(s); then ||z−x||_2=θ||x||_2≤θR. Taking both suprema in the definition of Hausdorff distance proves (1), including Δ=0. Using the radius of P(s), rather than an unproved bound R for P(t), is what makes the second estimate valid.

Normals are not assumed unit. Therefore Δ is an offset-coordinate error, not automatically a geometric distance between planes. Rescaling any constraint must rescale its offset too. The proof uses the invariant relative ratios t_i/s_i before the conservative common bound Δ/s_min.

## 2. Two elementary facet facts, including redundancies

Write an arbitrary full-dimensional bounded polytope P with nonempty interior as a finite system a_j·x≤b_j, with nonzero a_j. Every facet F is the equality face of at least one row. Indeed, at a point in the relative interior of F at least one inequality is active. If an active row were not constant on aff(F), the relative interior would contain a nearby point of F violating that row. Thus its hyperplane contains aff(F), and its equality face is exactly F. For our system such a row is σo_i·x≤t_i, where σ∈{−1,1}. Duplicate rows may give several labels for the same facet; choose any one.

Every boundary point belongs to an actual facet. For completeness, delete redundant inequalities until an irredundant representation remains. Each retained row cuts out a facet: since it cannot be deleted, a point y satisfies every other row but violates this row. The segment from a strictly interior point z to y meets the retained row at a point with all other inequalities strict. A relative open ball in that hyperplane is therefore feasible, proving facet dimension d−1. Every boundary point has an active retained row, since otherwise all retained inequalities would be strict.

We need only the following consequence, which also handles lower-dimensional supporting faces. If x,y∈P lie in the same supporting hyperplane, their midpoint m lies on the boundary. Choose an actual facet G containing m. Its supporting linear functional is at most its support value on both x and y; equality at their midpoint forces equality on each. Hence x,y∈G and

\[
 \|x-y\|_2\leq D(P).                               \tag{3}
\]

This does not assume the original constraint's equality face itself is a facet.

## 3. Upper semicontinuity, with all possible new facets

Suppose (2) fails. Then some ε_0>0 and positive t^(k)→s satisfy D(t^(k))≥D(s)+ε_0. Pick a facet F_k attaining that finite maximum, and points x_k,y_k∈F_k attaining its diameter. Facets are compact, so these choices exist. By the first facet fact, F_k is an equality face of σ_k o_(i_k)·x≤t^(k)_(i_k). There are only 2h labels. After a subsequence, (i_k,σ_k)=(i,σ) is fixed.

For all large k, (1) bounds P(t^(k)) within 2P(s). Compactness gives a further subsequence with x_k→x and y_k→y. Passing to every defining inequality yields x,y∈P(s), and passing to the selected equality yields

\[
 \sigma o_i\cdot x=\sigma o_i\cdot y=s_i.
\]

This is a proper supporting hyperplane: o_i≠0 and s_i>0, while 0 is interior. Equation(3) gives ||x−y||_2≤D(s). On the other hand, continuity of Euclidean distance gives ||x−y||_2≥D(s)+ε_0, a contradiction.

An originally strictly inactive row cannot occur along such a sequence: the same limiting equality would contradict its strict inactivity on P(s). An originally tight but lower-dimensional face causes no problem because (3) embeds the limiting pair in an actual facet. No facet identity, vertex enumeration, simplicity or fixed combinatorial type was assumed.

There are finitely many original facets, so the hypothesis that every one has diameter<ρ gives D(s)<ρ. Failure of a uniform neighbourhood would supply t^(k)→s with D(t^(k))≥ρ, contradicting (2). Intersect the resulting neighbourhood with ||t−s||∞<s_min/2 to make all offsets positive. This proves the literal frozen target. For d=1 the two facets are endpoints, each of diameter0; the same arguments apply.

## 4. Different derivation of the pivotal limiting step

As a check that the conclusion is not an artifact of constraint labels, use outward Euclidean unit normals n_k to the hypothetical facets F_k instead. Compactness of the unit sphere gives n_k→n along a subsequence. For any compact sets K,L, their support functions obey |h_K(v)−h_L(v)|≤||v||_2 d_H(K,L): compare each point with a closest point of the other compact set and then reverse the roles. Also |h_P(v)−h_P(w)|≤R||v−w||_2.

By (1), P(t^(k))→P(s). Thus

\[
 n\cdot x=n\cdot y=h_{P(s)}(n).
\]

Since ||n||_2=1 and P(s) has interior, this is again a proper supporting hyperplane. Equation(3) gives the same contradiction. This independently re-derives the key limiting support assertion within the same exposed internal audit. It is not a second actor, blind reproduction, external review or formal proof.

## 5. Exact adversarial controls

1. **Non-strict margin is insufficient — FALSIFIED weaker assertion.** For P(s)=[−1,1]^2, the whole-facet diameter is2. Set ρ=2 and t=(1+ε,1+ε), with unchanged coordinate normals and any ε>0. Then every facet of P(t) has diameter2+2ε>ρ, even though ||t−s||∞=ε→0. This refutes stability from D(s)≤ρ without slack. It does not refute the strict theorem or the source, whose two sine thresholds have positive slack.
2. **A former vertex becomes a facet.** Describe the square additionally by |x_1+x_2|≤2. Replacing only the last offset by2−ε, 0<ε<1, creates diagonal facets with endpoints(1,1−ε),(1−ε,1), and their negatives. Each new facet has diameter√2 ε. The limiting equality face is a vertex, not an old facet. The proof permits this.
3. **Strict inactivity.** In that example replace the last initial offset by2+γ, γ>0. It cannot become active before its offset has moved downward by at least γ if the coordinate offsets remain fixed. This explains why strictly inactive labels have no spurious limiting equality.
4. **Duplicate labels and mixed moves.** Two copies of |x_1|≤1 changed to offsets1+ε and1−ε leave the effective bound1−ε. With |x_2|≤1+ε the resulting rectangle has vertical facets2(1+ε) and horizontal facets2(1−ε). This checks mixed directions, redundant labels and the need for a positive strict margin, without assuming one facet per row.
5. **Boundedness and positivity are substantive.** The strip |x_1|≤1 in R^2 is unbounded and has no finite R. A zero coordinate offset collapses a square to a segment; a negative offset makes its symmetric inequality infeasible. These inputs are outside the theorem, not hidden tolerance cases.
6. **No numerical sampling.** All examples and bounds above are exact analytic calculations. No finite grid, numerical residual, decimal sign, executable certificate or software test is used as a universal proof.

## 6. Source consumer, read coverage and limitations

The primary source is [Alon–Bucić–Sauermann,2302.09058v2](https://arxiv.org/abs/2302.09058v2), revised2024-11-07. Its pinned33-page PDF is484598bytes with SHA-25687801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960. The inspection register (historical local record; not distributed here) separates new physical3–5 full-text reading and physical4 full visual review from reread19,21,22. The latter pages were already fully read092/093/097 and receive no new page credit. Current2026 owner metadata and the pinned matching-v1 introduction were also reread; their status statements remain AS_REPORTED, not reproduced bound proofs or an exhaustive current-literature search.

The overview physical4–5 explicitly connects small facets with translations of their hyperplanes and warns that the overview omits details. Physical21 claims full continuity of maximum facet diameter and individual exposed-face diameters. **We do not adopt or refute those stronger continuity assertions.** Upper semicontinuity, proved here, is sufficient for its actual consumer: original facets have diameter≤r sin(η/3), while the allowed new bound is r sin(η/2), with r>0 and0<η<π/2. The strict inequality sin(η/3)<sin(η/2) supplies exactly our ρ>D(s). Choose ε′ smaller than δ_* and the separate Hausdorff budget εr/(2c), where c bounds the original body's radius. The source uses only outward offsets s_i≤t_i≤s_i+ε′; our argument also covers mixed changes. Normalization ||o_i||_2=1 is present in the source but unnecessary for our stated offset-coordinate bound.

This supplies the local perturbation-radius dependency previously asserted without a locally replayed argument. It does not close the source's boundary transfer, distinct facet-pair assignment, algebraic dependence for m>0, exclusion neighbourhood, full nowhere-denseness or infinite graph compactness. The old2^d versus new2d bounds are not interchangeable; physical4 rendering confirms the old exponent that the text parser collapses.

## 7. Verdict, dependencies and learning

| Object | Outcome | Evidence and limit |
|---|---|---|
| Fixed-normal offset theorem and (1) | PROVED | Exact analytic proof for every stated finite d,h; normals need not be irredundant or unit |
| Maximum whole-facet upper semicontinuity(2) | PROVED | Label-subsequence proof and support-normal re-derivation |
| Non-strict robustness shortcut | FALSIFIED | Exact expanding-square family |
| Source's stronger full continuity/individual-face assertion | NOT_TESTED | Not required and not silently imported |
| SourceLemma5.3/full genericity/Euclidean bound | NOT_TESTED | This cycle closes one necessary geometric link only |

The uncertainty changed from an assumed perturbation radius to a proved existence statement with explicit Hausdorff control. Fixed facet identities and full continuity are unnecessary for this consumer. The strict threshold is essential; positive offsets and original boundedness keep degeneracies explicit. These arguments transfer to finite support descriptions under changing offsets, not to an automatic solution of the named Euclidean colouring problem.

Foundations are finite-dimensional compactness, support functions and the elementary facet facts proved above. The source and previous packet exposed the expected result and proposed compactness mechanism before construction. All derivation/review is by the same internal actor; no independent human, blind, external model or formal assurance is claimed. There is no mathematical executable or consequential pipeline change, and performance is NOT_MEASURED.

The next discriminating action is a separately frozen boundary-to-facet transport obligation: transport boundary points between Hausdorff-close convex bodies, then use the strict angular margin to assign separated lines to distinct antipodal facet pairs and control their support-coordinate errors. It tests a new interaction needed by physical22, rather than repeating offset stability. It remains NOT_TESTED in this cycle.

# Audited historical reading edition

**Current audited claim:** PROVED: For each fixed d>=2 a dense G-delta set of norm bodies has m_B(n)/n tending to one for positive distinct distances.

**Claim ceiling:** Known generic theorem; the all-norms version fails for the displayed sup-norm grids.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Generic norm distances: integration of the fixed-tolerance and Baire arguments

**PROVED internally, at known-result integration scope:** for each fixed integer d>=2, there exists a dense G_delta subset G_d of the space B_d of real norm unit balls, with the relative Euclidean Hausdorff metric, such that

    m_B(n)/n -> 1  for every B in G_d,

where m_B(n) is the minimum number of positive distinct norm distances among all sets of n distinct points in R^d. The full class with this limit is comeagre and contains G_d; it is not asserted to be itself G_delta. The universal version claiming this limit for every norm is **FALSIFIED** by an exact sup-norm grid family below.

This discharges the particular H(d) assumed in Cycle131, using the exact internally proved Cycle141 fixed-tolerance result. It is a known generic-norm theorem reproduced within the project's named internal proof chain, not a new theorem, a Euclidean chromatic result, a current worldwide status check, a measure-one assertion, independent human review, or formal verification. No complete literal printed-paper proof or blanket Theorem1.3 adoption is claimed.

Attempt frozen before source-body inspection (historical local record; not distributed here):35minutes/70combinedtoolcalls with8minutecloseout reserve,<=400native scientific lines,0publicrequests/0PDFpages. New141meagreness is the substantive continuation input; the closed Ungar search and all other paused routes remain closed.

## 1. Exact premise match, not a similar-looking theorem

Fix d>=2 and let B_d consist of compact convex origin-symmetric bodies in R^d with0interior. No radius, volume, smoothness or strict-convexity normalisation is imposed. Delta_B(S) counts positive distinct norm distances, without ordered-pair multiplicities.

[Cycle141](m10-fixed-mu-meagre-c141.md), exact-statement lines1–37, proves for each real0<mu<1 that

    A*_mu={B in B_d: exists integer n>=n0(d,mu), exists distinct n-point S,
                       Delta_B(S)<=(1-mu)n}

is meagre in this same B_d. The threshold is

    n0(d,mu)=max(N125(d,mu),floor(1/mu)+1,2),

with exactly the explicit N125 audited141. This result has no remaining D_n or selected-bad-witness assumption; its named internal inputs are109/110/115and primary-backed140.

Cycle131 (historical local record; not distributed here), lines1–132, defines its A*_r by taking precisely the126threshold n0(d,r), the same existential integer n and distinct S, the same weak inequality, positive-distance convention and relative Hausdorff space. Its H(d) asks for meagreness of each such set for rational0<r<1. Specialising141to mu=r proves every required instance. Neither the threshold nor domain is changed. No tolerance nesting or monotonicity is assumed. Dimension is fixed before constructing G_d; no single set across different norm spaces is asserted.

Thus H(d) is now discharged at the inherited internal-proof ceiling. The historical conditional131proof remains unchanged. This run checks its remaining topology, quantifiers and limit transfer; it does not rerun125/126, Ungar or the geometry foundations.

## 2. Integer minimum and the upper bound

For every B and n>=2, some n-point set exists and every positive-distance count is an integer in the finite set1,...,binom(n,2). The nonempty set of achieved counts has a smallest achieved member. No configuration-space compactness or minimising-sequence argument is needed.

For a nonzero u, the equally spaced collinear set0,u,...,(n-1)u has exactly the n-1positive distances k||u||_B,1<=k<=n-1. Hence

    1 <= m_B(n) <= n-1,   m_B(n)/n <= 1-1/n < 1.

This upper bound is universal over norms. The lower bounds below apply only on the chosen generic set. Zero distances and repeated point labels cannot be introduced into either count.

## 3. Baire property with the correct complete ambient space

Let C_d be the nonempty compact convex origin-symmetric subsets of R^d, allowing degenerate ones. The Hausdorff metric on C_d is complete. The131proof is valid: a Hausdorff-Cauchy sequence is uniformly bounded, and the nested compact closures of its tails have a nonempty compact intersection K. For arbitrarily small epsilon, the Cauchy bounds put every late K_j within epsilon of K and every K-point within epsilon of K_j. Thus d_H(K_j,K)->0. Symmetry and convexity pass to this limit by pointwise approximations in the same late sets;0 is retained. Degeneracy of K is permitted in C_d.

B_d is open in C_d. If rD_2 is contained in K and d_H(K,L)<r/2, then for every unit direction v,

    h_L(v) >= h_K(v)-d_H(K,L) > r/2.

The support estimate follows by approximating a maximiser in K by a point of L. If z in(r/2)D_2 were outside L, a nearest point y of the compact convex L gives the supporting unit vector v=(z-y)/||z-y||. The one-sided squared-distance derivative along segments in L shows h_L(v)<=v.y<v.z<=r/2, a contradiction. Therefore(r/2)D_2 is contained in L and L remains a norm body. B_d is nonempty, since it contains the Euclidean unit ball.

For completeness of the category argument, start in any nonempty relatively open U subset B_d. It is open in C_d. For closed nowhere-dense F_j subset B_d, choose nested closed ambient balls with positive radii tending to0, each lying in the preceding open interior and outside F_j. Keep the first ball inside U. The centers are Cauchy in the complete C_d; their limit lies in every closed ball, hence inside U and outside every F_j. Consequently the intersection of the open complements is dense G_delta in B_d. No compactness of Hausdorff balls is needed.

**The given metric on B_d is not complete.** The norm balls K_j=(1/j)D_2 are Hausdorff-Cauchy with unique ambient limit{0}, outside B_d. This earlier131counterexample remains valid and is explicitly inherited; it does not defeat the open-subspace Baire proof. The first closed ambient ball keeps the nested construction away from degeneration.

## 4. Countability and full convergence

For each rational r in(0,1), choose a countable nowhere-dense cover of A*_r and take the relative closures of the covering sets. These closures are closed nowhere dense. The pairs(r,k) are countable, and the Baire argument gives

    G_d = intersection_(r rational in(0,1),k>=1) (B_d minus F_(r,k)),

a dense G_delta avoiding every A*_r. Taking closures of a nowhere-dense cover is legitimate; claiming that an existentially projected family is itself closed would not be.

For every B in this one G_d, every rational0<r<1, every n>=n0(d,r), and every distinct n-point S,

    Delta_B(S)>(1-r)n,   m_B(n)/n>1-r.                      (1)

The minimum is achieved, so the strict inequality survives minimisation. For arbitrary epsilon>0, choose rational0<r<min(epsilon,1). Combining(1)with the collinear upper bound gives, for every n>=n0(d,r),

    1-epsilon < m_B(n)/n <= 1-1/n < 1.

This proves full convergence, not merely a liminf statement or convergence along a favourable subsequence. The threshold n0(d,r) is the same for every B in G_d at fixed d,r, inherited explicitly from141. No sharp or measured numerical rate, efficiency improvement or uniformity across d is asserted.

For a separate quantifier check, if liminf m_B(n)/n<1, choose rationalr strictly below the deficit. Infinitely many n have m_B(n)/n<1-r, so some exceed the actual finite n0(d,r), irrespective of monotonicity. Their attained minima give B in A*_r. Thus the exceptional set is a subset of the countable union of these meagre sets. By the universal upper bound, its complement is exactly the class with limit1. That class is comeagre and contains G_d. The audit does not infer that this entire class is itself G_delta, open, closed or of full measure.

## 5. Exact adversarial boundaries

**FALSIFIED — the all-norms strengthening.** Let B be the sup-norm cube and let S_L={0,...,L-1}^d. Here n=L^d and the positive sup-norm distances are exactly1,...,L-1: no coordinate difference exceeds L-1 and every value occurs on a coordinate axis. Therefore

    m_B(L^d)/L^d <= (L-1)/L^d -> 0  for d>=2.

This already refutes convergence to1 for every norm. In fact, with L=ceil(n^(1/d)), any n-point subset of the L-grid has at most L-1distances, so m_B(n)/n->0. This exact family is a counterexample only to the all-norms statement; it is consistent with the generic theorem. The sup-norm ball is an admissible compact convex symmetric norm body, so no forbidden domain was used.

**FALSIFIED — replacing all sufficiently large n by infinitely many favourable n.** The integer sequence c_n=n-1for evenn and floor(n/2)for oddn has1<=c_n<=n-1and infinitely many ratios arbitrarily close to1. Its even ratios tend to1 and odd ratios to1/2. This is a logical quantifier control, not a claimed norm-realisation of that sequence. The actual proof uses all n beyond the threshold for each r.

Confirmation contract (historical local record; not distributed here), exact controls (historical local record; not distributed here). Five finite sup-norm grids check integer distances and positive-distance convention. Wrong L1 substitution and admission of zero are detected. A finite parity-sequence/radius prefix illustrates the analytic arguments but cannot establish an infinite limit. The general grid formula, incomplete-space counterexample and limit transfer above are analytic proofs, not inferences from samples. No floating-point or interval certificate is claimed.

## 6. Adjudication, custody and retirement

**PASS AT CLAIM CEILING / PROVED internally:** exact141-to131premise match, dense G_delta norm-ball subset and the stated positive distinct-distance asymptotic, with the uniform fixed-tolerance threshold above. Inputs retain the named inherited141/109/110/115/140internal assurance; those foundations were not independently re-audited142. Review is the same exposed actor/model, not human/blind/formal review. This is known-result project dependency closure, not a new discovery or global-open-problem resolution.

The generic-norm assembly family is now CLOSED at this internal claim ceiling. Do not repeat the assembly, its source contract or the Ungar lookup to generate activity. All other paused routes remain paused. A future stronger claim would need genuinely independent mathematical/formal assurance and any separately specified source-statement adoption; none was obtained or contacted here. Euclidean chi status,5–7bounds and global source-check dates are unchanged. Literal failed source steps and all older conditional records remain preserved.

Next research selection should rotate through the scientific frontier and require materially new proof/source/data input. No ready continuation is automatically selected. CurrentP02still requires an actually matched joint w0,wa observational product and M07a material source/certificate input; unchanged metadata polling does not meet their pause conditions. This is a native readiness boundary, not a claim that no scientific work is possible.

Adjudication (historical local record; not distributed here), source register (historical local record; not distributed here), report (historical local record; not distributed here). Directly inspected2native mathematical paths/2hashes:131FULL1–132and141PARTIAL1–37of118,169lines. Same inherited scientific lineage,0newprimarysources/independentreviews/PDFpages/publicrequests. Cumulative scientific path/content/source counts and denominators remain UNKNOWN; historical mixed-volume numbers are not scientific coverage. No excluded original/copy, source execution/mutation, external action, agent, app/schedule/notification, other-project/shared-skill change or unmanaged process occurred.

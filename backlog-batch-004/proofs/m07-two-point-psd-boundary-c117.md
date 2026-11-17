# Audited historical reading edition

**Current audited claim:** PROVED: The finite two-point comparison extends to every complex PSD pair with the stated support-sensitive extended production.

**Claim ceiling:** Unequal supports give infinite production; equal-support finiteness relies on finite dimension here.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Two-point inequality on all finite positive semidefinite matrix states

**PROVED internally at the stated finite-matrix scope.** Cycle116's two-point inequality extends to every positive semidefinite complex matrix pair, with the explicit extended entropy production below. The regularized entropy converges and the production has the exact finite/infinite classification. The scalar and all-finite-matrix infima coincide, including singular states. This is a restricted two-point result, not universal classical MLSI=CMLSI, arbitrary finite von Neumann auxiliaries, products, novelty or external human/formal acceptance.

The frozen attempt (historical local record; not distributed here) precedes the three selected mathematical text readings. The expected mechanism and earlier review verdict were exposed. This is same-actor/model analytic reconstruction, not blind or independent human review. No numerical certificate, tolerance, supplied code or TeX execution is used.

## Statement, definitions and admitted dependency

Fix0<p<1, q=1−p, m≥1, τ_m=Tr/m and positive semidefinite complex Hermitian A,B∈M_m(C). Put φ(x)=x ln x for x>0 and φ(0)=0, M=pA+qB, and

\[
 H_p(A,B)=p\tau_m\varphi(A)+q\tau_m\varphi(B)-\tau_m\varphi(M).
\]

Let s(A) be the orthogonal projection onto the range of A. Define the extended generalized relative entropy

\[
 D_\tau(A\Vert B)=
 \begin{cases}
 \tau(A\ln A-A\ln B)-\tau A+\tau B,&s(A)\le s(B),\\
 +\infty,&s(A)\not\le s(B).
 \end{cases}
\]

Here A ln A uses φ(0)=0. If supports are included, the mixed logarithm is evaluated on s(B), where B has a positive inverse in finite dimension; A vanishes on its orthogonal complement. D_τ(0||B)=τB and D_τ(0||0)=0. Set

\[
 J_{p,\mathrm{ext}}(A,B)=pq[D_\tau(A\Vert B)+D_\tau(B\Vert A)].
\]

Use exactly116's scalar positive-pair infimum a_p and its proved inequality for all finite positive-definite pairs, with a_p nonnegative and finite. No numerical value, sharp-minimizer proof or17/20 certificate is required. The theorem is

\[
 J_{p,\mathrm{ext}}(A,B)\ge2a_pH_p(A,B),\qquad
 \inf_{m\ge1,\ A,B\ge0,\ H_p>0}\frac{J_{p,\mathrm{ext}}(A,B)}{2H_p(A,B)}=a_p. \tag{T}
\]

The quotient can be+∞. No quotient is assigned when H_p=0. For A_ε=A+εI and B_ε=B+εI, prove additionally

\[
 H_p(A_\epsilon,B_\epsilon)\to H_p(A,B),\qquad
 J_p(A_\epsilon,B_\epsilon)\to J_{p,\mathrm{ext}}(A,B)
 \quad(\epsilon\downarrow0). \tag{R}
\]

These are assertions for each fixed finite pair, not a uniform limit over changing supports or matrix sizes.

## Extended relative entropy is well defined

For completeness one can check nonnegativity without importing joint convexity. Choose orthonormal eigenbases of A and B, with eigenvalues a_i,b_j≥0, and weights w_ij=|⟨e_i,f_j⟩|². The weights are nonnegative with each row and column sum1. If s(A)≤s(B), b_j=0 and a_i>0 imply w_ij=0. Direct expansion of the trace gives

\[
 D_\tau(A\Vert B)=\frac1m\sum_{i,j}w_{ij}
 [a_i\ln(a_i/b_j)-a_i+b_j]. \tag{1}
\]

For b_j>0 the bracket is b_j[t ln t−t+1], t=a_i/b_j≥0, with0ln0=0. It is nonnegative and vanishes exactly at t=1. When a_i=b_j=0 the bracket is0; impossible positive-a/zero-b terms have zero overlap and are omitted. Thus the finite-support expression is a finite nonnegative number. If support inclusion fails, some positive-a/zero-b overlap has positive weight, precisely the case assigned+∞. There are no−∞ summands.

The same scalar equality characterization shows D_τ(A||B)=0 exactly when A=B: zero forces a_i=b_j whenever w_ij>0, so every B-eigenvector lies in the matching A-eigenspace. This also covers zero eigenvalues. Conversely A=B gives zero directly.

Because p,q>0, kerM=kerA∩kerB: a zero quadratic form for M forces both nonnegative summands to vanish. Thus s(A),s(B)≤s(M), both relative entropies with M are finite, and trace expansion gives

\[
 H_p(A,B)=pD_\tau(A\Vert M)+qD_\tau(B\Vert M)\ge0. \tag{2}
\]

The linear terms cancel since M=pA+qB. Equality in(2) occurs exactly when A=M=B. Hence H_p>0 for every unequal pair, including singular ones. In particular all-zero pairs cause no denominator exception hidden by a tolerance.

## Same support: the finite positive corner and its trace

If s(A)=s(B)=E and r=rankE>0, the restrictions A_E,B_E are positive definite on the r-dimensional space E C^m. All zero-complement contributions to φ(A),φ(B),φ(M) vanish. The inherited trace is **not** normalized there:

\[
 \tau_m\big|_{E M_m E}=(r/m)\tau_r.
\]

Consequently H_m=(r/m)H_r. The linear terms in the symmetric D sum cancel, so

\[
 J_{p,\mathrm{ext}}(A,B)=(r/m)\,pq\tau_r[(A_E-B_E)(\ln A_E-\ln B_E)].
\]

Both quantities scale by the same positive factor. Applying116 in this corner proves(T)'s inequality for this case. The quotient is unchanged, not multiplied by r/m. If r=0, then A=B=0 and H_p=J_ext=0 directly.

The positive inverse in the corner follows from the finitely many strictly positive eigenvalues. This step does **not** assert that a bounded positive operator with full support in an infinite-dimensional algebra has a bounded inverse.

## Unequal support and the exact regularization expansion

Let P_A be the projection onto kerA and define

\[
 \ell(A)=\sum_{\lambda>0}(\ln\lambda)E^A_\lambda,
\]

zero on kerA. For ε>0, finite spectral calculus gives the exact decomposition

\[
 \ln(A+\epsilon I)=(\ln\epsilon)P_A+\ell(A)+R_A(\epsilon),\quad
 R_A(\epsilon)=\sum_{\lambda>0}\ln(1+\epsilon/\lambda)E^A_\lambda.
\]

If A≠0 and δ_A is its least positive eigenvalue,0≤R_A≤(ε/δ_A)I by ln(1+x)≤x. If A=0, both ℓ(A) and R_A are zero; no nonexistent δ_A is used. Define the corresponding objects for B. Since A_ε−B_ε=X=A−B,

\[
 J_p(A_\epsilon,B_\epsilon)=-\kappa\ln\epsilon+C+\eta_\epsilon, \tag{3}
\]

where

\[
 \kappa=pq[\tau_m(BP_A)+\tau_m(AP_B)],\quad
 C=pq\tau_m[X(\ell(A)-\ell(B))].
\]

The remainder satisfies

\[
 |\eta_\epsilon|\le pq\|X\|\epsilon
 \left(\frac{\mathbf1_{A\ne0}}{\delta_A}
 +\frac{\mathbf1_{B\ne0}}{\delta_B}\right), \tag{4}
\]

where absent terms are omitted. This follows from |τ_m(Y)|≤‖Y‖ and the spectral remainder bounds. The sign in(3) follows from

τ_m[X(P_A−P_B)]=−τ_m(BP_A)−τ_m(AP_B),

using AP_A=BP_B=0. In particular it is not permissible to discard a small positive kernel-overlap coefficient.

Both terms in κ are nonnegative. More precisely, τ_m(BP_A)=‖B^(1/2)P_A‖²_2 and is zero exactly when RanP_A⊆kerB, or P_A≤P_B. Similarly τ_m(AP_B)=0 exactly when P_B≤P_A. Faithfulness of the finite trace therefore proves

\[
 \kappa=0\iff P_A=P_B\iff s(A)=s(B). \tag{5}
\]

No commutation of the two support projections is needed. If supports differ, κ>0 and(3)–(4) give J_ε→+∞. At least one of s(A)≤s(B) and s(B)≤s(A) fails, so at least one D term is+∞. The other is a finite nonnegative number or+∞, never−∞. Therefore J_ext=+∞ and(R) holds for production in this case. Its inequality in(T) is immediate since H_p and a_p are finite.

If supports agree, κ=0 and C is exactly the corner production computed above, including C=0 for the zero corner. Equations(3)–(4) give J_ε→C=J_ext. Thus the production limit is established in every support case with a controlled per-pair remainder, not an appeal to an unchecked boundary continuity rule.

## Entropy limit and a separate resolvent check

Since M_ε=pA_ε+qB_ε=M+εI, each term of H_ε is a finite sum of(λ+ε)ln(λ+ε). The function extends continuously to0 with value0, so these finite sums converge to H_p. This proves the entropy part of(R), including common kernels and zero blocks.

A different formulation checks the sign, limit direction and absence of cancellation. The logarithm resolvent identity for ε>0 gives

\[
 \frac{J_p(A_\epsilon,B_\epsilon)}{pq}
 =\int_\epsilon^\infty
 \|(B+sI)^{-1/2}X(A+sI)^{-1/2}\|_{2,\tau_m}^2\,ds. \tag{6}
\]

Indeed log(A+εI)−log(B+εI) is the integral of(B+sI)^(−1)−(A+sI)^(−1) from ε to∞. The inverse difference equals(B+sI)^(−1)X(A+sI)^(−1), in that order. Multiplying by X and taking the trace produces the squared norm displayed. Onε,∞) the integrand is bounded by a constant times s^(−2), so these operations are justified for every ε>0. Its nonnegativity shows J_ε increases as ε↓0. The separate finite spectral expansion identifies its limit with the stipulated J_ext rather than assuming that identification from monotonicity alone.

One may therefore also pass the116inequality J_ε≥2a_pH_ε to the limit to obtain(T). This corroborates the direct corner/unequal-support proof. The two arguments share the model, actor, inputs and trace conventions; they are not independent external review.

## Sharp matrix constant, generator and normalization

The inequality gives every positive-entropy quotient at least a_p, including the+∞ quotients. Scalar positive-definite pairs are still admitted, so their variational infimum supplies the reverse bound. Thus the allfinitePSDmatrix infimum is exactly a_p, whether or not a scalar minimizer is attained.

For the native generator L=c(I−E_π), c>0, the ε-regularized production is cJ_ε and hence its extended limit is cJ_ext. The fixed-point relative entropy remains H_p by(2), or direct trace expansion on suppM. Thus the native inequality is2αH_p≤cJ_ext and the allfinite-matrix constant is ca_p. This is a matrix amplification constant; it is not yet an assertion about all auxiliary finite von Neumann algebras in the broader definition of α_c.

For any s>0, supports are unchanged and J_ext(sA,sB)=sJ_ext(A,B), allowing the usual positive-scalar multiplication of+∞. The logarithmic scale terms cancel on a common support; unequal supports remain infinite. The same homogeneity holds for H_p. If A,B are not both zero, T=τ_mM>0, so dividing both blocks by T imposes the single weighted density normalization. Separate trace-one blocks are not required. A=B=0 satisfies the inequality but is not normalized or assigned a quotient. Endpoint weights and c=0 remain outside the claim.

## Exact adversarial controls and false changed boundary models

| Case | Exact evidence | Conclusion |
|---|---|---|
| A=B, including a common singular matrix and A=B=0 | H_p=J_ext=0 and J_ε=0 identically. | No0/0 quotient or false divergence. |
| Scalar A=0,B=1 | κ=pq, H_p=−q lnq>0, J_ε=pq ln((1+ε)/ε)→∞. | One zero block is covered; unequal support does not have finite production. |
| Nested unequal supports, A=diag(1,0), B=I₂ | κ=pq/2>0, although s(A)≤s(B). The opposite inclusion fails. | One included support is insufficient for finite **symmetric** production. |
| Common proper complex noncommuting support | In M₃ use the2×2blocks A_E=((2,i),(−i,2)), B_E=diag(1,2), and a common zero complement. Both quantities are2/3times their normalized corner values. | All complex directions and the inherited trace factor are retained. |
| Noncommuting, arbitrarily close supports | Let A be the projection onto e₁ in C² and B onto(cosθ,sinθ),0<θ<π/2. Then κ=pq sin²θ>0 and J_ε=pq sin²θ ln((1+ε)/ε). | Infinite production for every fixed nonzero θ, with no uniform positive lower bound on κ as θ→0. |

Two isolated changed models are **FALSIFIED**, not the theorem:

1. **Replace ln0 by0 in the production formula.** At p=q=1/2,m=1,A=0,B=1, the resulting pseudolog production is0, whereas H_p=(1/2)ln2 and a_(1/2)=1 by116's scalar proof. The claimed inequality would require0≥ln2>0. The stipulated extended production is instead+∞. Assigning zero to xlnx at x=0 is legitimate; doing so to the unweighted logarithm in production loses the divergence.
2. **Mix original trace for production and normalized corner trace for entropy.** At p=q=1/2,m=2,A=diag(4,0),B=diag(1,0), the mixed ratio is one half of the actual scalar ratio. The116exact control gives the latter<2 because4H_scalar−J_scalar=(1/2)ln(2⁴⁹/5²⁰)>0. Thus the mixed ratio is<1=a_(1/2), a spurious separation. The correctly computed original-trace ratio equals the scalar ratio and satisfies the proved lower bound.

The near-support projection family also rejects any assertion that unequal supports have a universal positive divergence coefficient, even after total-density normalization (common scaling by2 makes τ_mM=1). This is a separate false uniformity claim; no uniform rate was assumed in(T) or(R). The limit fixes A,B. Simultaneously changing θ with ε is not that limit and licenses no zero-tolerance boundary shortcut.

These checks cover nested, nonnested, zero, common proper, complex noncommuting and near-coincident supports without a finite grid. There is no failed original-theorem control requiring its conclusion to be withheld. No global counterexample or numerical certificate is claimed.

## Claim ledger and continuation boundary

| ID/object | Verdict | Scope and ceiling |
|---|---|---|
| M07-TWO-POINT-PSD-BOUNDARY-C117 | PROVED internally / PASS AT CLAIM CEILING | Every finite complex PSDpair/all0<p<1, explicit extended J, regularization and scalar reverse infimum; c>0native scaling. |
| M07-KERNEL-LOG-EXPANSION-C117 | PROVED internally | Exact κclassification and per-fixed-pair O(ε)remainder; no uniformity over supports or dimension. |
| M07-BOUNDARY-MODEL-GUARDS-C117 | FALSIFIED changed assertions only | Pseudologfinite-production and mixed-trace variants, plus universal positive κclaim, have the exact controls above. |
| Arbitrary finite von Neumann auxiliaries, products, general reset/classical chains | NOT_TESTED117 / held | Finite spectral support-corner inversion is not an infinite-dimensional argument. |
| Novelty/current worldwide status/external human/formal acceptance/performance | NOT_ESTABLISHED / NOT_TESTED / NOT_MEASURED | No source survey, contact, proof assistant or controlled benchmark. |

The changed uncertainty is the complete finite-matrix domain: zero eigenvalues now have a proved support classification and extended-generator meaning. Strict two-point separation is excluded for all finite PSDmatrix states under this normalization, not just positive-definite inputs. The old biased interpolation and α₁=1 shortcuts remain false; this result does not use them or the old scalar numeric certificates. General classical chains involve more than two operator values and remain a different target.

The next proposed bridge is uniformly invertible bounded pairs over arbitrary finite tracial von Neumann algebras. It must replace the finite matrix-unit step in116 by genuine joint functional calculus of bounded left/right multiplication operators and justify the finite positive spectral measure/integrations without matrix approximation. Singular operators in such algebras remain another issue: full support does not imply a bounded inverse there. No such extension is adopted117.

## Source extent, provenance and custody

[Exact source inspections (historical local record; not distributed here) and the reading ledger (historical local record; not distributed here) bind whole-file hashes, selected captures and exact line/UTF-8 byte ranges. Three local mathematical text records were directly inspected:116's full211-line native proof; the existing review's normalization30–53 and boundary151–166; the frozen manuscript's169–197. The latter two files remain partial. Visible product/VN assertions are not proof adoptions. The source's finite corner/subadditivity route and review's resolvent route are checked here only at the stated finite-matrix boundary scope; no external joint-convexity or tensorization theorem is imported.

One new guaranteed review body interval151–166 complements116's exact1–150; the known union is1–166/333, still partial. The manuscript's interval is a reread inside116's1–197/266, still partial. One full native record plus two partial source records does not add volume-estate paths or independent underlying works. The draft and exposed review share an argument. Memory supplied only a packet-specific provenance/scope reminder, checked against current records, not proof evidence or a current-status fact.

Estatepass047 remains155paths=145full+10partial,146recorded hashes and113/428327candidate paths, with underlying-source/content denominators UNKNOWN. All PDF extents remain unchanged, including M10original26/33text/21/33visual and Cook10/12. No fresh primary-owner/status/novelty search occurred. Only local project records are written; no mathematical/supplied-code/TeX execution, agent, external request/message/upload/publication, foreign-estate mutation, installation, account/purchase, app/schedule/notification change or unmanaged continuation occurred. The run report (historical local record; not distributed here) records decision, integration and checked closeout.

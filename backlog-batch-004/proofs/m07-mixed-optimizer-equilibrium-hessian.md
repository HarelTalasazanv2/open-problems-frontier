# Audited historical reading edition

**Current audited claim:** PROVED: At the stated scalar minimizer and mixed 2x2 base, the full complex Hermitian-pair Hessian has the displayed rank-four positive normal part and four-dimensional kernel; beta lies in (23/2500,6/625).

**Claim ceiling:** Fixed reset generator and base; no global comparison or dimension-uniform neighbourhood.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Full mixed optimizer/equilibrium Hessian — fixed biased reset chain

**Verdict: `PROVED` internally at the stated second-order scope.** At p=1/10, q=9/10, A0=diag(r*,1), B0=I, the complete two-input complex Hermitian Hessian of Q is nonnegative, of real rank four, with exactly the four-dimensional kernel stated below. The positive off-diagonal coefficient has an exact rational enclosure. No finite-neighborhood inequality, global biased MLSI/CMLSI equality, novelty, human review or formal verification is claimed.

## 1. Definitions, dependencies and claim ceiling

L=I-E_pi with invariant weights (p,q); natural logarithms and unnormalized matrix trace. For A,B>0 let M=pA+qB,

`D=p tr(A log A)+q tr(B log B)-tr(M log M)`,

`I=pq tr[(A-B)(log A-log B)]`, `Q=I/(2D)` for D>0.

The normalization is 2 alpha D<=I. Common positive scaling leaves Q invariant, so normalized states can be obtained after perturbation without changing its value.

Let a=pr+q, d=pr log r-a log a, i=pq(r-1)log r, k=i/(2d). The cycle035 analytic proof (historical local record; not distributed here) establishes that the fixed biased chain has a unique interior scalar minimizer r=r*>1 with k'(r)=0, k''(r)>0 and 0<k(r)<1. Those analytic implications were rechecked here. Its previous numerical optimizer/value certificates are **not** imported as trusted numeric dependencies. The new certificate below establishes root membership directly.

Set C=i/d=2k(r), h=log r/(r-1), ell=log a/(a-1). For arbitrary Hermitian inputs write

`X=[[x,z],[conj(z),u]]`, `Y=[[y,w],[conj(w),v]]`,

where x,u,y,v are real and z,w complex. Then the full second derivative is

`D²Q_(A0,B0)[X,Y]`

`= k''(r)(x-r y)^2 + pq(2-C)/(2d)(u-v)^2 + beta |w|^2`,       (1)

`beta=[pq(r+3)-2C(q-q^2 ell)]/(2d)`.

The new exact certificate proves

`23/2500 < beta < 6/625`.                                     (2)

Each coefficient in (1) is strictly positive. Consequently the Hessian is nonnegative and its kernel is **exactly**

`x=r y`, `u=v`, `w=0`, with arbitrary complex z.                (3)

The domain is the full eight-real-dimensional Hermitian pair space; it is not a real-symmetric slice or a one-input calculation. Kernel dimension is four and rank is four. This classification applies at this fixed chain/base only. A Hessian classification alone is not the finite-neighborhood or global inequality.

## 2. Ambient stationarity comes first

Put F=I-C D, treating C as a fixed scalar at the base. At the first diagonal coordinate the gradients are the scalar derivatives

`D_A=d'`, `D_B=d-rd'`, `I_A=i'`, `I_B=i-ri'`.

Here d'=p log(r/a) and i'=pq(log r+1-1/r). Since i=Cd and i'=Cd', both derivatives of F vanish. At the second coordinate A=B=1, both scalar entropy and production gradients vanish separately. Off-diagonal first variations vanish because the base matrices and their logarithms are diagonal. Thus F=DF=0 in the entire ambient pair space, not just the chosen slice, and D=d>0.

The quotient rule therefore gives `D²Q=D²F/(2d)`. Along a curved common-unitary path, the second derivative includes DQ applied to path acceleration; that term vanishes because the full gradient has just been proved zero. No symmetry shortcut was used to assume stationarity.

## 3. Diagonal directions and absence of missing cross terms

For diagonal inputs the trace splits into the two scalar coordinates. At the optimizing coordinate,

`D²F = (i''-C d'')(x-r y)^2 = 2d k''(r)(x-r y)^2`,

with d''=pq/(ra), i''=pq(r+1)/r^2. At the equilibrium coordinate,

`D²D=pq(u-v)^2`, `D²I=2pq(u-v)^2`,

so its F contribution is pq(2-C)(u-v)^2. The coefficient is positive since C=2k(r)<2.

There are no diagonal/off-diagonal cross terms: in the trace-resolvent second derivatives, a diagonal base pairs only equal matrix indices, and each ordered off-diagonal index is paired with its conjugate reverse index. Equivalently, simultaneous conjugation by diag(1,exp(i theta)) preserves Q, fixes all diagonal variables and rotates both off-diagonal entries by the same phase. An invariant quadratic form has no diagonal/off-diagonal bilinear term. The explicit derivation below also excludes an imaginary cross coefficient.

## 4. Complete off-diagonal block by trace differentiation

For log, T_H(Z)=integral_0^infinity (H+sI)^(-1)Z(H+sI)^(-1)ds. For trace f(H)=tr H log H, its Hessian is tr[Z T_H(Z)]. At a diagonal two-eigenvalue base, the off-diagonal contribution is 2h(b1,b2)|Z12|^2, where h(b1,b2)=(log b1-log b2)/(b1-b2), with continuous value 1/b1 at coincident eigenvalues. Hence, with X,Y purely off diagonal,

`D''=2[p h |z|^2+q |w|^2-ell |p z+q w|^2]`.                  (4)

The B eigenvalues coincide, so its coefficient is exactly1; no division by their difference is permitted.

Expand production as pq times `tr A log A+tr B log B-tr A log B-tr B log A`. The first two terms give 2h|z|^2 and 2|w|^2. At B=I, D²log_I[Y,Y]=-Y², so the second derivative of tr A log B is `-(r+1)|w|^2+4 Re(z conj(w))`. Finally, tr log(A0+epsilon X)=log det(A0+epsilon X) gives second derivative `-2|z|^2/r`; the mixed first-log pairing is `4h Re(z conj(w))`. Combining signs yields

`I''=pq[2(h+1/r)|z|^2+(r+3)|w|^2-4(1+h)Re(z conj(w))]`.        (5)

Complex conjugacy is essential: |z|^2 and Re(z conj(w)) cannot be replaced by Re(z^2) and Re(z w).

### A second spectral derivation

For purely off-diagonal X, the eigenvalues of A0+epsilon X are `r+epsilon²|z|²/(r-1)+O(epsilon⁴)` and `1-epsilon²|z|²/(r-1)+O(epsilon⁴)`. Thus the epsilon² coefficient of tr A log A is h|z|². The corresponding coefficient for M is ell|p z+q w|². For B=I+epsilon Y, log B=epsilon Y-epsilon²Y²/2+O(epsilon³), and tr B log B has coefficient |w|².

Also tr log A=log det A has coefficient -|z|²/r, while the off-diagonal first derivative of log A is h z. These give the cross-trace coefficients `2Re(z conj(w))-(r+1)|w|²/2` and `-|z|²/r+2h Re(z conj(w))`, respectively. They recover exactly one-half of (4)-(5), the Taylor coefficient rather than the second derivative. This route checks signs, the factor two, the repeated B eigenvalue, and the imaginary-entry treatment through explicit 2x2 spectra. It shares the mathematical model and reviewer with the first route and is not external or blind review.

## 5. Exact cancellation at the actual optimum

Both scalar value and stationarity are needed. From i=Cd and i'=Cd', divide by nonzero p(r-1) and use log a=p(r-1)ell to obtain

`q(r-1)h=C(r h-a ell)`,

`q(h+1/r)=C(h-p ell)`.

Subtract r times the second rearranged equation from the first rearranged equation. Since a-pr=q, it gives

`C ell=1+h`.                                                  (6)

Substituting back gives

`h(1-C)+p+q/r=0`.                                             (7)

Using (6), the z-w coefficient of I''-CD'' is exactly zero. Its |z|² coefficient equals `2p[h(1-C)+p+q/r]`, zero by (7). The sole remaining off-diagonal coefficient is

`G=pq(r+3)-2C(q-q²ell)` multiplying |w|².

Division by 2d gives beta in (1). Neither cancellation is justified at a nonstationary ratio. In particular, common-unitary X directions lie in the kernel precisely consistently with the zero ambient gradient; we did not round small residuals to zero.

## 6. New exact sign certificate and adversarial controls

The frozen attempt (historical local record; not distributed here) and discovery/confirmation contract (historical local record; not distributed here) preceded the deciding calculation. The new OPF checker (historical local record; not distributed here) uses Python's standard-library Fraction only. Reproduce:

`python3 artifacts/m07_mixed_hessian_cycle036/certify_mixed.py`

For x>=1 let z=(x-1)/(x+1). It encloses log x by the first80 positive terms of `2 sum z^(2j+1)/(2j+1)` and the upper remainder `2 z^161/[161(1-z²)]`. The lower bound omits a nonnegative tail; the upper follows by replacing every subsequent denominator by161 and summing a geometric series. Reciprocal inversion covers x<1. Monotonicity gives interval log endpoints. All interval additions, signed products and reciprocal divisions use exact rationals; denominators containing zero are rejected.

The stationary numerator S=i'd-id' is strictly negative at8 and positive at9. Since k'=S/(2d²) and the analytic scalar minimizer is unique, the root is between them. Eighteen strict-sign bisections yield

`2201889/262144 < r* < 1100945/131072`.

The lossless certificate (historical local record; not distributed here) records each midpoint/decision, positive entropy lower bound, C enclosure and interval beta over this **entire** retained ratio interval. Exact comparisons prove (2); displayed decimal beta approximately 0.00937342–0.00937658 is diagnostic only. No floating-point number enters the verdict.

Controls passed: one-term log2 bounds [2/3,25/36], independent integral bounds for log2/log4, reciprocal log signs, asymmetric signed interval arithmetic, rejection of zero-containing divisors and inadmissible r<=1, and negative B-only curvature at r=4. The latter is not the scalar optimizer and does not refute its nonnegative Hessian. Three selected wrong coefficient variants (wrong I2 sign, wrong D2 sign, missing r+1 production contribution) are rejected by the actual certified coefficient consumer and its coarse enclosure criterion. This is not exhaustive mutation coverage.

Twelve exact synthetic algebra canaries (historical local record; not distributed here), generated by a separate algebra check (historical local record; not distributed here), compare the raw D/I quadratic form to the reduced G|w|² form under explicit formal stationary relations. They include real/imaginary unitary tangents and coupled complex entries and detect a wrong Hermitian pairing. They do not evaluate actual logarithms or supply an all-input proof. There was no failed control, skipped case or optional-package failure in this run.

For X=0 and w=1, I''/2=pq(r+3)/2 and D''/2=q-q²ell. The epsilon² quotient coefficient is beta/2. This exactly recovers the cycle017 restricted-family formula without inheriting its old certificate. The new enclosure is intentionally coarse, not claimed a sharper curvature bound.

## 7. Positivity, denominator and exact null directions

For any fixed X,Y, choose |epsilon| below

`min(1/(2||X||op),1/(2||Y||op),(r-1)/(2||X-Y||F))`,

omitting any term with zero denominator. A0 and B0 have smallest eigenvalue1, so both perturbed matrices stay positive definite. Their difference remains nonzero by the last bound. Strict convexity of tr H log H, whose Hessian tr[Z T_H(Z)] is positive for nonzero Hermitian Z, gives D>0. Thus Q is genuinely defined along an admissible open perturbation segment; no entropy tolerance conceals an equilibrium exception.

All coefficients in (1) are strictly positive: k''>0 and C<2 are analytic scalar facts, d>0, and beta>0 is newly certified. Therefore (3) is necessary and sufficient for a zero quadratic form. Its two real diagonal degrees of freedom scale the optimal and equilibrium blocks separately. Its two real off-diagonal degrees of freedom arise from common-unitary rotations of A0 with B0=I. No additional hidden negative or zero off-diagonal direction remains.

These kernel directions are tangent to the commuting critical family `A=U diag(r b1,b2)U*`, `B=U diag(b1,b2)U*`, b1,b2>0. Q equals alpha1 there. This observation motivates a possible separate local-neighborhood argument, but this run does **not** claim such an argument or a quantitative remainder. Nonnegative Hessian alone does not license a finite separation exclusion.

## 8. Source status, learning and next action

The primary-source note (historical local record; not distributed here) rechecks Gao et al.'s normalization/Problem6.4 and substantively inspects its classical bounds, including Example3.11's known reset-chain complete lower bound1/2. The known reset lower bound can also be checked from the definitions: I=D+J with J=tr[M log M]-p tr[M log A]-q tr[M log B]. Convexity of tr H log H gives tr[M(log M-log A)]-tr M+tr A>=0, and the corresponding B inequality. Their weighted sum is J>=0 because pA+qB=M. Thus Q>=1/2 whenever D>0 in any finite dimension. This reproduces known prior art and does not identify the sharp biased complete constant. Zhao's current abstract remains a circle/tori special case. This bounded check neither establishes current universal openness nor novelty of the mixed-base calculation. It is internal, exposed to earlier project work and not human/formally reviewed.

Uncertainty reduced: the complete simultaneous-input mixed optimizer/equilibrium quadratic form is nonnegative; the earlier single B direction did not establish that. The proportional and this mixed-base infinitesimal families should now stay paused absent a distinct mechanism. A repeated grid at these bases has little decision value. The known global reset lower bound1/2 leaves the actual global comparison unresolved.

**Next prioritized research action:** take the ready M08 H1132 original-source reconstruction and compare its complete data to the pinned mirror under a declared equivalence, rather than repeat settled local Hessian searches. This changes a live source-dependency decision. Independent human review of M07 manuscript v3 remains a separate unsent claim-promotion gate; this new dossier is not silently included in that exact payload.

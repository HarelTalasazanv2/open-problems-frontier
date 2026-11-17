# Audited historical reading edition

**Current audited claim:** PROVED: For the specified complex 2x2 biased reset problem there is an open positive neighbourhood of the stated mixed critical family with the displayed residual coercivity bound (Q-alpha1)>=||residual||^2/8000.

**Claim ceiling:** Existential neighbourhood for this fixed chain and finite dimension only; no explicit radius, global inequality or M07 resolution.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Finite neighborhood at a mixed optimizer/equilibrium base

**Adjudication: PROVED internally at the stated restricted scope; PASS AT CLAIM CEILING.** Exact claim: for the fixed biased two-state reset chain and complex2x2 amplification, every sufficiently nearby pair around diag(r*,1),I satisfies Q>=alpha1, with equality exactly on the commuting optimal/equilibrium family. A numerical grid or nonnegative Hessian alone is not the proof. The argument below uses a full local chart, exact criticality and an integral Taylor remainder. No explicit radius, other weights/dimensions, singular boundary, global comparison, novelty or external review claim.

## 1. Exact statement and normalization

Fix p=1/10,q=9/10 and L=I-E_pi on the classical two-state algebra, E_pi(A,B)=(M,M), M=pA+qB. Matrices A,B are positive-definite Hermitian2x2 over C. All traces are unnormalized and logarithms natural. Put

D(A,B)=p tr(A log A)+q tr(B log B)-tr(M log M),
I(A,B)=pq tr[(A-B)(log A-log B)], Q=I/(2D), when D>0.

These are the entropy and production for this generator: L(A,B)=(q(A-B),p(B-A)); its invariant weighted trace is p tr A+q tr B, and the E_pi log term cancels in the production. The convention is2 alpha D<=I. Common positive scaling scales D,I equally, so Q is unchanged, but the local coercivity constant below is stated at this particular unnormalized base.

For scalar ratio r>0 set a=pr+q, d(r)=pr log r-a log a, i(r)=pq(r-1)log r, k=i/(2d) off r=1, with scalar continuous extension k(1)=1. Let r=r*>1 be the unique scalar minimizer and alpha1=k(r), C=2alpha1=i(r)/d(r). The scalar justification is rechecked in section2. Write d0=d(r)>0, A0=diag(r,1),B0=I.

**Theorem.** There exists epsilon>0 such that every complex Hermitian pair with ||A-A0||_F+||B-I||_F<epsilon is positive definite, D>0 and Q>=alpha1. In a specified smooth A-eigenframe, let b1,b2 be the diagonal entries of B and w its off-diagonal entry, and let lambda_plus>lambda_minus be the ordered eigenvalues of A. Then, after shrinking epsilon if necessary,

Q(A,B)>=alpha1 + [(lambda_plus-r*b1)^2+(lambda_minus-b2)^2+|w|^2]/8000.       (T)

Equality Q=alpha1 holds exactly when w=0,lambda_plus=r*b1,lambda_minus=b2, equivalently on the local family

A=U diag(r*b1,b2) U*, B=U diag(b1,b2) U*, b1,b2>0.

The residual in(T) is a Euclidean four-coordinate residual, **not** a claim with this constant for ambient Frobenius distance to the manifold. The radius is existential and is not supplied by the numerical coefficient certificate. The theorem excludes local separation in this neighborhood only.

## 2. Scalar dependency: actual minimum, not an arbitrary stationary ratio

For p=1/10, q=9/10, direct derivatives are d'=p log(r/a),d''=pq/(ra)>0, i'=pq(log r+1-1/r),i''=pq(r+1)/r². Functions and first derivatives vanish at1. The Taylor integral formula writes i/d as a positive weighted average of R=i''/d''=1+pr+q/r, using weights(r-t)d''(t) on1<t<r if r>1 and(t-r)d''(t) on r<t<1 if r<1. Thus d>0 off1. For r<1, R(t)>2 on the integration interval, so k>1. For1<r<=3=sqrt(q/p), R(t)<2 and k<1. The scalar removal has k(1)=1. The quotient tends to infinity as r tends to0 or infinity, since d->-q log q while i~-pq log r at0, and d~pr log(1/p),i~pq r log r at infinity. Hence a global minimum is attained strictly inside r>1.

On r>1, d'>0. Put H=i'/d', T=d'R-i', J=dH-i. Then T'=d'R', H'=d''T/(d')² and J'=dH'. R decreases on(1,3), increases on(3,infinity). T starts at0, is negative through3, then strictly increases to infinity: d' tends to p log(1/p)>0, R grows linearly, i' grows only logarithmically. Consequently T has exactly one zero c1>3; H' is negative before c1 and positive afterward. J starts at0, is negative through c1 and strictly increasing afterward. An interior minimizer exists, and k'=d'J/(2d²); therefore J has exactly one zero beyond c1, giving the unique global scalar minimizer. At that zero, J'>0 and k''=d'J'/(2d²)>0. Positivity of d,i and k<1 somewhere give0<alpha1<1.

This is the fixed-weight portion of the internally proved cycle035 scalar lemma (historical local record; not distributed here), audited here rather than importing its old rounded optimizer. It also identifies alpha1 as the scalar constant, since a scalar pair(x,y)>0 has D=y*d(x/y),I=y*i(x/y). The exact036 sign bracket was recomputed in040: r is in(2201889/262144,1100945/131072), the unique stationary root there. No older sharp-value bracket is needed.

## 3. A complete local chart despite B0 having a repeated eigenvalue

For eta in C define

U_eta=(1+|eta|²)^(-1/2) [[1,-eta],[conj(eta),1]].

This is unitary. Coordinates are s=(Re eta,Im eta,b1,b2) in R4 and v=(v1,v2,u,t) in R4, with w=u+it. Define the pair Phi(s,v) by

A=U_eta diag(r*b1+v1,b2+v2) U_eta*,
B=U_eta [[b1,w],[conj(w),b2]] U_eta*.

The reference coordinates are s0=(0,0,1,1),v0=0. Restrict to a neighborhood where b1,b2>0, r*b1+v1>b2+v2>0 and B>0. It contains the reference pair.

Here is an explicit smooth inverse covering **every** nearby Hermitian pair. Write A=[[a,z],[conj(z),e]], define

g=sqrt((a-e)^2+4|z|²), lambda_plus=(a+e+g)/2, lambda_minus=(a+e-g)/2,
tau=lambda_plus-e, eta=z/tau.

Near A0, a-e>0 and tau>0, bounded away from zero. The eigenvalues stay distinct because r>8. The normalized columns(tau,conj(z)) and(-z,tau) give precisely U_eta, and the characteristic equation verifies U_eta* A U_eta=diag(lambda_plus,lambda_minus). Set Btilde=U_eta* B U_eta, b1=Btilde11,b2=Btilde22,w=Btilde12, v1=lambda_plus-r*b1,v2=lambda_minus-b2. These recover all coordinates and reconstruct A,B. All operations are smooth real functions near the base, including the positive square root and division by tau>0. No B-eigenvector or division by the eigenvalue difference of B occurs, so B0=I is covered rather than excluded.

The forward map and this inverse give a genuine local diffeomorphism of eight-real-dimensional open sets. At the reference, its derivative is

X11=r*delta b1+delta v1, X22=delta b2+delta v2, X12=(r-1)*delta eta,
Y11=delta b1,Y22=delta b2,Y12=delta w.

It is invertible for r!=1. The critical-family tangent(v=0) has exactly x=r*y, u_diag=v_diag, w=0 with arbitrary complex X12, agreeing with the full four-dimensional kernel in036. This tangent check is useful, but the proof below needs the explicit full chart and positive transverse block; it does not assume a general named critical-manifold theorem.

## 4. Exact equality and ambient stationarity on the whole critical family

Let F(A,B)=I(A,B)-C D(A,B), C fixed at the scalar optimum. On v=0 in the chart, the matrices commute and

D=b1*d(r)>0, I=b1*i(r), F=0.

The second diagonal coordinate is an equilibrium pair(b2,b2) and contributes zero. The scalar deficit for a pair(a,b) is b*g(a/b), with g=i-Cd. Its derivatives are g'(a/b) and g(a/b)-(a/b)g'(a/b). At r, g=g'=0 by value and stationarity; at1, d=i=d'=i'=0. Hence all diagonal first derivatives vanish at every such pair, not only at b1=b2=1.

All off-diagonal first derivatives vanish too: at a commuting diagonal pair, the trace gradients of entropy are diagonal; differentiating cross terms tr A log B and tr B log A pairs diagonal matrices with the diagonal part of the log derivative. An off-diagonal variation has zero diagonal log derivative at a diagonal positive matrix. This remains true at a repeated eigenvalue, where Dlog_bI(Y)=Y/b. Equivalently it follows directly from the resolvent derivative. Thus DF=0 in **all** ambient Hermitian directions throughout the local v=0 family. Unitary invariance transports this conclusion for all eta.

Therefore f(s,v)=F(Phi(s,v)) satisfies f(s,0)=0 and partial_v f(s,0)=0 for every s near s0. This exact critical-family assertion, rather than the Hessian alone, removes all dangerous higher-order drift along tangent directions.

## 5. Direct transverse Hessian and its rigorous positive margin

At the reference, varying v keeps eta,b1,b2 fixed. Thus X=diag(v1,v2), Y=[[0,w],[conj(w),0]]. No curved-path acceleration term occurs in this affine v-slice. Alternatively DF=0 already makes such an acceleration term vanish.

The diagonal trace splitting gives coefficient h1=i''(r)-C*d''(r) on v1², and h2=pq(2-C) on v2². To derive the w coefficient directly, let B(epsilon)=I+epsilon Y with A=A0. Since Y²=|w|²I,

log B=epsilon Y-epsilon²Y²/2+O(epsilon³),
tr B log B has epsilon² coefficient |w|²,
tr A log B has epsilon² coefficient -(r+1)|w|²/2,
tr B log A has no epsilon² term.

Hence I''=pq(r+3)|w|². For M0=diag(a,1), a=pr+q, the entropy trace Hessian in an off-diagonal direction Z is2 ell|Z12|², ell=log(a)/(a-1). Therefore D''=2(q-q²ell)|w|². The transverse coefficient is

h3=pq(r+3)-2C(q-q²ell).

Mixed diagonal/w terms vanish by simultaneous conjugation by diag(1,exp(i theta)), which fixes the diagonals and rotates w; no nonzero real-linear w term times a diagonal variable is invariant. The same phase symmetry makes the real and imaginary w coefficients equal and excludes a cross term between them. The two diagonal coordinates have no cross term because the commuting trace splits. Thus the full real v-Hessian is exactly

H_vv f(s0,0)=diag(h1,h2,h3,h3).                              (H)

This is the Hessian in the Euclidean coordinate v specified above, not the list of nonzero eigenvalues in an ambient Frobenius-orthonormal basis. Formula(H) is independently obtained without the delicate full z,w cancellation in036, while sharing definitions, scalar optimum and mathematical reviewer.

The new exact consumer (historical local record; not distributed here) reuses the reviewed036 Fraction interval backend, recomputes all18 stored bisection signs and the lossless old beta receipt, and directly bounds h1,h2,h3 and d over the whole retained r interval. Its certificate (historical local record; not distributed here) proves

h1>1/1000, h2>1/1000, h3>1/1000, 0<d0<1.                   (C)

In the JSON, `normal_h3_twice` stores h3 once with multiplicity two in the four-coordinate Hessian, not the arithmetic value2*h3; the explicit eigenvalue-membership list removes that naming ambiguity. The displayed decimal lower diagnostics are about0.00139700448,0.0251778737,0.0154452070; d upper is about0.823883302. These decimals do not decide the inequalities. The old beta interval is exactly reproduced by its original expression; the direct h3/(2d) interval also lies strictly between23/2500 and6/625. The log bound is the exact positive80-term atanh series with explicit geometric tail, using Fraction arithmetic and zero-divisor guards. Reuse is a same-implementation numerical recomputation, not new independent arithmetic or blind review. The new h1/h2/h3 consumer rejects three selected wrong sign/omission variants and the nonstationary ratio4.

## 6. Uniform remainder and neighborhood coverage

On a sufficiently small ambient neighborhood, A,B and M have smallest eigenvalues at least1/2. One may first choose radius<1/4 in the sum Frobenius metric, which gives eigenvalues at least3/4 for A,B; shrink further for the chart. The matrix logarithm is smooth even at repeated positive eigenvalues: use

log H=integral_0^infinity [(1/(1+s))I-(H+sI)^(-1)] ds.

On matrices with eigenvalues bounded below, resolvent differentiation is uniformly integrable: first and higher derivatives have tails of order s^(-2) or faster, and no singularity at s=0. This proves the needed C² regularity of F and of f=F composed with Phi without a spectral-eigenvalue denominator for B. D is continuous and equals d0 in(0,1) at the reference.

Let lambda0=1/1000. By(H),(C) and continuity, choose a small product ball in(s,v), with its closure inside the chart/positive-cone domain, on which

||H_vv f(s,v)-H_vv f(s0,0)||_op<lambda0/2,
0<D(Phi(s,v))<1.

The second bound can be obtained by requiring |D-d0|<min(d0/2,(1-d0)/2). All constants are strictly positive; this is a local existential continuity argument, not an asserted numerical radius. The Hessian comparison implies H_vv f(s,v)>=(lambda0/2)I4. Shrink to a product ball convex in v so(s,tv) stays in it for every0<=t<=1.

For each fixed s, exact criticality from section4 and the integral Taylor formula give

f(s,v)=integral_0^1 (1-t) v^T H_vv f(s,tv) v dt
       >=lambda0*||v||²/4.

Since Q-alpha1=F/(2D) and0<D<1,

Q-alpha1>=lambda0*||v||²/8=||v||²/8000.

At v=0 equality holds exactly; at v!=0 the lower bound is positive. The explicit inverse chart maps this product neighborhood to an open ambient neighborhood containing(A0,I); therefore some epsilon-ball in the stated sum Frobenius metric lies inside it. This covers every nearby complex Hermitian pair, not merely pairs whose B has distinct eigenvalues or whose entries are real. It proves(T) with the stated existential epsilon. No compactness of a noncompact global family, finite-grid extrapolation or global Hessian sign is invoked.

## 7. Adversarial checks and limits

- **Hessian-only fallacy:** f(s,v)=v²-s⁴ has positive transverse Hessian2 at0, a null s-direction and negative values along v=0 arbitrarily near0. Its supposed equality/critical family fails: f(s,0)=-s⁴ and derivative -4s³ are nonzero. This exact counterexample rejects that shortcut but is not a counterexample to the M07 theorem, whose critical family was proved exactly.
- **Coordinates and complex coverage:** the explicit inverse is an analytic identity for all nearby inputs. Eight supplementary rational-complex canaries cover real/imaginary/mixed eta and w, nonzero residuals and different block scales. Their synthetic r=17/2 is not substituted for the actual optimum. An omitted imaginary coordinate drops Jacobian rank from8 to7; a wrong conjugation breaks unitarity. These finite checks supplement rather than prove the all-input chart.
- **Ratio/normalization:** ratio4 has a negative known normal coefficient and nonzero scalar stationary numerator; it cannot inherit the r* theorem. No small residual is rounded to zero. Natural logs, generator and2alpha convention are fixed.
- **Boundary/repeated eigenvalues:** B=I is included using the A-chart and resolvent log; singular matrices, repeated A eigenvalues and r=1 lie outside the neighborhood. No extension by numerical tolerance is made. D=0 points are excluded by an actual open continuity bound.
- **Kernel/higher orders:** the kernel agrees with the tangent of an exact critical family, and Taylor is applied at(s,0) for each nearby s, not merely at the single base point. This is what controls mixed higher-order terms and curved-unitary directions.
- **Certificates:** all old036 files remain unchanged. The new consumer is bound to code/input hashes, exact intervals and strict margins. Its three selected faults are detected by the actual coefficient acceptance rule; this is not exhaustive fault coverage. No numerical grid, randomized search or speed benchmark was run.

## 8. Sources, originality and independence

The owning [Gao et al.2025 primary paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7270B6BBA7891B612C00FAB066F1A380/S2050509424001178a.pdf/complete-positivity-order-and-relative-entropy-decay.pdf), normalization(1.1),Example3.11 and Problem6.4, was partially reinspected2026-10-20. Its known reset complete lower bound1/2 is distinct from this sharp-scalar local inequality. [Wirth–Zhang2021](https://link.springer.com/article/10.1007/s00220-021-04199-4), Remark2, Definition5/Corollary1 and Theorem6/proof, was substantively checked: the operator mean matters for gradient estimates, and the tree-group/uniform Z2 result uses a Haar trace, not an arbitrary biased two-point invariant distribution. Its CLSI(2) convention corresponds to alpha1 under the2alpha convention. [Zhao's current abstract](https://arxiv.org/abs/2608.23482) still concerns circle/tori heat semigroups. The bounded public search found no verified general closure; it is not exhaustive and establishes no novelty/priority or current universal-open theorem. Exact extents/access limitations are separately registered.

This is a new local development in this project, with a self-contained chart/remainder proof and reused exact arithmetic. Same-model internal mathematical review is not external human review; no formal proof assistant was run. No assertion that this theorem is new to mathematics, a solution of classical complete equality, or approved in a prior reviewer payload is made. The exact v3 manuscript/request remains unchanged and unsent;040 is not silently added to it.

## 9. Learning, remaining obstruction and reproduction

The uncertainty changed from a second-order nonnegative form to a genuine neighborhood, including its equality cases. Positive transverse curvature alone would have been insufficient. The useful mechanism is an explicit eigenframe chart around a repeated-B base plus an exact critical family; it can inform later local arguments but is not an all-dimension/all-weight result. Do not repeat grids near this base or merely recertify its positive normal coefficients without changed evidence.

The broader fixed-chain complete comparison still requires distant noncommuting states, other dimensions and singular-limit control. No amount of local coverage alone supplies that global step. The numeric epsilon is not computed here.

Reproduce numerical dependencies with `python3 -B artifacts/m07_mixed_neighborhood_cycle040/certify_normal.py` and supplementary chart checks with `python3 -B artifacts/m07_mixed_neighborhood_cycle040/check_chart.py`. Both use standard-library exact arithmetic, and only OPF-owned code executes. The analytic proof, not these finite canaries, supplies neighborhood coverage. Custody manifests, final report and chronological log provide the operational closeout separately.

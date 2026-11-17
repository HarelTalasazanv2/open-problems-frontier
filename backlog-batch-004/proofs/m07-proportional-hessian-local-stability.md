# Audited historical reading edition

**Current audited claim:** PROVED: At a scalar stationary ratio r!=1 the full two-input Hessian equals k_second(r)/tr(B) times the stated positive log-derivative form in X-rY; strict scalar curvature yields a local coercive neighbourhood.

**Claim ceiling:** Finite dimension and positive cone only; no uniform neighbourhood, global constant or novelty claim.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

**Explicit correction or qualification:** The original Section7 recovery formula had an extra factor2 on r i/a. Earlier Hessian equations were correct. The reading edition corrects that comparison explicitly; original source bytes and the failure record are retained locally. See [ERRATA.md](../ERRATA.md). Chronological originals remain unchanged.

# Proportional-base Hessian and local stability for two-point matrix entropy

**Adjudication:** `PROVED` internally at the exact finite-dimensional local scope below. Complete analytic proof; numerical diagnostics are supplementary. No external human review or formal verification. Novelty and priority are unestablished. The parameterized theorem does not assume OPF's earlier scalar uniqueness certificate. A separate self-contained calculus argument supplies the fixed p=1/10 corollary. No global complete-constant comparison follows.

The initial packet (historical local record; not distributed here) and staged extension packet (historical local record; not distributed here) distinguish original 2x2 scope, extension to finite n, extension to general weights, and local stability. The challenge record (historical local record; not distributed here) records auxiliary checks and their limits.

## 1. Exact statement

Fix p in (0,1), q=1-p, and the classical two-state reset generator L=I-E_pi, invariant weights (p,q), amplified entrywise to complex matrices. All logarithms are natural, and tr is the unnormalized matrix trace. For positive definite Hermitian A,B put

`M=pA+qB`,

`D(A,B)=p tr(A log A)+q tr(B log B)-tr(M log M)`,

`I(A,B)=pq tr[(A-B)(log A-log B)]`, `Q(A,B)=I(A,B)/(2D(A,B))` when D>0.

The two generator components are L(A)=q(A-B), L(B)=-p(A-B). Pairing them with the weighted trace and log gives the displayed I; the weighted log M term cancels. Thus these are the entropy/production convention `2 alpha D <= I`. They are homogeneous of degree one in (A,B), so Q is invariant under common positive scaling. Indeed the log-scaling terms in D cancel; those in log A-log B cancel as well. Normalized densities can therefore be obtained by common scaling; our theorem is stated on the open unnormalized cone.

For r>0 define `a=pr+q`, `d(r)=pr log r-a log a`, `i(r)=pq(r-1)log r`, and `k(r)=i(r)/(2d(r))` for r!=1. We have d>0 for r!=1 by strict scalar convexity of x log x, and k extends continuously to k(1)=1.

**Theorem 1 (full Hessian).** Let r>0, r!=1, satisfy k'(r)=0. For every finite n>=1, every positive definite B in M_n(C), and every Hermitian X,Y, the point (rB,B) is stationary for Q and

`D²Q_(rB,B)[(X,Y),(X,Y)] = k''(r)/tr(B) * E_B(X-rY)`,

where `E_B(Z)=tr[Z T_B(Z)]` and `T_B=Dlog_B` is the Fréchet derivative of log. In an eigenbasis of B with eigenvalues b_j>0,

`E_B(Z)=sum_j Z_jj²/b_j + 2 sum_(j<l) |Z_jl|² h(b_j,b_l)`,

`h(x,y)=(log x-log y)/(x-y)` for x!=y, and `h(x,x)=1/x`.

Thus E_B is strictly positive for Z!=0. If k''(r)>0, the Hessian is positive semidefinite and its kernel is **exactly** X=rY. If k''(r)=0 the entire Hessian vanishes; no stability conclusion follows from that case. If k''(r)<0 every transverse nonzero direction has negative quadratic variation. The factor above is the second derivative, not the coefficient of epsilon² (which is half of it).

**Theorem 2 (finite local stability).** Under k'(r)=0 and k''(r)>0, for each fixed finite n and B0>0 there exist an open neighborhood U of (rB0,B0) and c>0 such that every (A,B) in U is positive definite, has D>0, and satisfies

`Q(A,B) >= k(r)+c ||A-rB||_F²`.

Equality holds exactly on A=rB within U. This is an existential finite neighborhood, with no explicit radius, no neighborhood uniform in n or in a vanishing eigenvalue, and no assertion for arbitrary distant states. It is a local stability theorem, not a global MLSI/CMLSI equality theorem.

## 2. Matrix logarithm identities, including repeated eigenvalues

For B>0, the scalar logarithm integral, applied by spectral calculus, gives

`T_B(Z)=integral_0^infinity (B+tI)^(-1) Z (B+tI)^(-1) dt`.

On a neighborhood with eigenvalues bounded below, differentiating under the integral is justified: resolvent derivatives have integrable bounds at infinity and bounded denominators near zero. This also gives smoothness of log on the positive cone. T_B is self-adjoint for the real trace pairing on Hermitian matrices, `T_(cB)=T_B/c`, and `T_B(B)=I`. Consequently `tr[B T_B(Z)]=tr Z`.

Differentiating this last identity in the base B in direction Z, with Z fixed, gives the pivotal second-log identity

`tr[B D²log_B[Z,Z]]=-tr[Z T_B(Z)]`.                 (1)

An independent derivation of (1) comes from differentiating the scalar identity `tr[(B+tZ)Dlog_(B+tZ)(Z)]=tr Z`, itself obtained directly by diagonalizing the base at each t. Neither derivation assumes B and Z commute.

Resolvent integration in an eigenbasis gives h(x,y) above. When x=y the integral is `integral_0^infinity (x+t)^(-2)dt=1/x`, so repeated eigenvalues require no singular division. Hermitian conjugacy gives Z_lj=conj(Z_jl); both ordered off-diagonal terms sum to `2|Z_jl|²`, not `2 Re(Z_jl²)`. All coefficients h are strictly positive and at least `1/max(x,y)`, hence

`E_B(Z) >= ||Z||_F²/lambda_max(B)`.                 (2)

The derivative of `tr C log C` in direction V is `tr V(log C+I)`; its second derivative is `tr[V T_C(V)]`. These follow from T_C(C)=I and trace self-adjointness, so no external matrix entropy theorem is needed for the calculation.

## 3. First variations: stationarity is proved before removing directions

At A=rB, `D=d tr B` and `I=i tr B`. Straight differentiation yields

`D'=d' tr X+(d-rd')tr Y`,

`I'=i' tr X+(i-ri')tr Y`,

where `d'=p log(r/a)` and `i'=pq(log r+1-1/r)`.

Let C=i/d=2k(r). Scalar stationarity is exactly `i'-C d'=0`, while `i-Cd=0` holds by definition. Subtracting C D' from I' gives zero for **every** X,Y. Hence DQ=0 at every (rB,B). This establishes ambient stationarity, rather than inferring it from symmetry.

For a smooth curved path with tangent V and acceleration W, the second derivative is `D²Q[V,V]+DQ[W]`. The acceleration term now vanishes because the entire gradient is zero. A common unitary path has X=rY, as do common scaling and any proportional-manifold tangent. They are Hessian kernel vectors by the formula proved below. Conversely, all kernel vectors are proportional-manifold tangents when k''>0, including arbitrary spectral changes of B, not just rotations/scalings.

## 4. Second variations and the factorization

Write `Z=X-rY` and `S=pX+qY`. The entropy second variation is

`D''=(p/r)E_B(X)+q E_B(Y)-(1/a)E_B(S)`

`    =pq/(r a) E_B(Z)`.                           (3)

For production, differentiate the defining trace directly. The result before simplification is

`I''/(pq)=2 tr[(X-Y)(T_B(X)/r-T_B(Y))]`

`          +(r-1)tr[B(D²log_B[X,X]/r²-D²log_B[Y,Y])]`.

Use (1) and self-adjointness. The coefficients of E_B(X), the mixed pairing, and E_B(Y) are respectively `(r+1)/r²`, `-2(r+1)/r`, and `r+1`. Thus

`I''=pq(r+1)/r² E_B(Z)`.                          (4)

A second route checks (4): expand `I/(pq)=tr A log A+tr B log B-tr A log B-tr B log A`. The cross terms contribute first-log mixed pairings and the same second-log traces in (1). This independently matches all three coefficients; no commutativity of the perturbations is used.

As the quotient numerator `F=I-C D` has F=F'=0 at the base, the quotient second derivative is simply `F''/(2D)`. Equations (3)-(4) give

`Q''=pq/[2d tr B] * [(r+1)/r²-C/(r a)] E_B(Z)`.   (5)

For the scalar quotient, `d''=pq/(r a)` and `i''=pq(r+1)/r²`. At k'=0,

`k''=(i''-C d'')/(2d)`.

Substituting this into (5) proves Theorem 1. Neither the matrix dimension nor a special value of p entered the proof. This justifies the separately frozen dimension and weight extensions.

## 5. A complete neighborhood argument along the degenerate manifold

Fix B0>0. At the stationary point (rB0,B0), Theorem 1 with Y=0 and (2) give

`D²_A Q[X,X] >= m0 ||X||_F²`,

`m0=k''(r)/(tr B0 * lambda_max(B0))>0`.

Q is C² wherever A,B>0 and D>0. D(rB0,B0)=d tr B0>0; continuity supplies an open ball where all these conditions hold. Shrink it until `D²_A Q[X,X] >= (m0/2)||X||_F²` for every X throughout that ball. This follows from continuity of the finite-dimensional Hessian in operator norm; it is not a numerical tolerance.

Use coordinates (Z,B) with A=rB+Z. Choose B near B0 and ||Z|| small enough that the entire segment (rB+tZ,B), 0<=t<=1, stays in that ball. Along the entire proportional manifold, Q(rB,B)=k(r) and `D_AQ(rB,B)=0` by section 3. Integral Taylor expansion in Z therefore gives

`Q(rB+Z,B)-k(r)`

`=integral_0^1 (1-t) D²_AQ_(rB+tZ,B)[Z,Z]dt`

`>=m0 ||Z||_F²/4`.

Take c=m0/4 and such a coordinate neighborhood. Flat manifold directions are handled exactly by Q(rB,B)=k(r), not by an uncontrolled higher-order expansion. This proves Theorem 2. For any fixed perturbation, positivity also follows explicitly from `|epsilon| ||X||<r lambda_min(B0)` and `|epsilon| ||Y||<lambda_min(B0)`; a possibly smaller neighborhood enforces D>0.

## 6. Fixed biased chain: a self-contained nondegeneracy argument

Here p=1/10,q=9/10. This argument is exposed to the earlier cycle-015 proof; it is not blind or independent human review. It supplies its own complete scalar reasoning, without assuming an old certificate or the numerical optimizer bracket.

We have d(1)=i(1)=d'(1)=i'(1)=0, d''>0, and

`R=i''/d''=1+pr+q/r`, `R'=p-q/r²`.

For 0<r<1, integral Taylor remainders express i/d as the positive weighted mean of R on (r,1). There `R(t)-2=(1-t)(q/t-p)>0`, so k(r)>1. Just to the right of 1, R is strictly decreasing below R(1)=2, and the analogous integral remainder gives k(r)<1. Also k(r)->infinity as r->infinity, because `d~pr log(1/p)` and `i~pq r log r`. Toward zero, d tends to `-q log q>0` and i tends to infinity. Thus a global minimum exists at an interior r*>1, with k'(r*)=0.

For r>1, d'>0. Define `H=i'/d'` and `A=d'R-i'`. Then `A'=d'R'`; A(1)=0; A is negative through r=3, strictly increasing after 3, and eventually positive. The last claim follows from `R~pr`, `d'->p log(1/p)>0`, `i'=O(log r)`. Hence exactly one c1>3 has A(c1)=0, and `H'=d''A/(d')²` is negative before c1 and positive afterward.

Define `Btilde=dH-i`. Its limit at 1+ is zero and `Btilde'=dH'`. Therefore Btilde<0 through c1 and strictly increases afterward. The existing interior minimizer must satisfy Btilde(r*)=0 because `k'=d' Btilde/(2d²)`. There can be only one such zero, it lies beyond c1, and at it

`k''(r*)=d' Btilde'(r*)/(2d²)>0`.

This proves uniqueness and nondegeneracy internally. Thus Theorems 1-2 apply to the actual fixed-chain scalar optimum alpha1=k(r*) in every **fixed finite** matrix dimension and at every strictly positive proportional base. The earlier sharp numerical interval is not needed for this conclusion and is not re-certified here. External scrutiny of both this scalar argument and the matrix theorem is still pending.

## 7. Recovery checks, failed extension and exact limits

- **Scalar/diagonal directions:** n=1,B=b gives `Q''=k''(r)(x-ry)²/b²`, exactly the chain rule for k(A/B) at k'=0. For diagonal n>1, summing scalar entropy contributions gives the same weighted sum of `(X_jj-rY_jj)²/b_j` divided by tr B.
- **Cycle 018 rotation:** B=diag(s,1), A(theta)=r U(theta)B U(theta)*. At theta=0, Y=0 and off-diagonal |X12|=r|s-1|. Theorem 1 yields `Q_theta theta=2r² k''(r)(s-1)log(s)/(s+1)`. This equals twice the old coefficient with u=sin²(theta), since its `H_old=(r+1)d-r i/a` and stationarity imply `r² k''=pq H_old/(2d²)`. The acceleration contributes zero by the proved stationarity. For s=1 the exact rotation path is constant, and the formula has its continuous zero limit.
- **Cycle 017 is not a special case:** its base A=diag(r,1),B=I has one optimizer block and one equilibrium block; it is not proportional. Its positive restricted coefficient cannot be substituted for this full calculation or inferred back from it. That mixed base remains the best next distinct obligation.
- **Nonstationary stronger formula fails:** for any homogeneous degree-zero Q and radial V=(A,B), differentiating DQ[V]=0 in a direction W gives `D²Q[W,V]=-DQ[W]`. At a nonstationary proportional base DQ[W] can be nonzero. Thus invariance does not make V a Hessian kernel vector. For this chain, k'<0 on (1,3), so r=2 and a ratio-changing scalar W supply an actual counterexample to the unconditional kernel assertion. This rejects the stronger interpretation, not Theorem 1.
- **Degeneracy:** r=1 is excluded because D=0 at the base. Singular B is excluded; h(b,b)=1/b diverges toward zero. No dimension-uniform or boundary-uniform neighborhood is claimed. A scalar stationary inflection/flat minimum with k''=0 is covered by the zero Hessian identity only; it does not inherit Theorem 2.

## 8. Contribution, novelty and review

Known ingredients: matrix logarithm resolvent/divided differences, entropy trace differentiation, scalar quotient calculus and finite-dimensional continuity/Taylor expansion. The project contribution developed here is their explicit cancellation into the full two-input Hessian factorization and the local stability argument along the entire proportional manifold. This is a new OPF derivation, not an established original literature result.

Primary sources and bounded search are in the source note (historical local record; not distributed here). No earlier equivalent theorem was identified in the inspected portions of those sources, but that limited check does not establish novelty, absolute priority, or present universal openness. Gao et al.'s 2025 Problem 6.4 remains the source of the global question; Zhao's 2026 tori theorem concerns a different generator. No manuscript was sent and no matching external review response exists for this version. Targeted review questions are in the local referee packet (historical local record; not distributed here).

**Next:** derive the full complex two-input Hessian at the mixed base A=diag(r*,1),B=I. It changes the base-state geometry and tests coupling between a scalar optimizer and an equilibrium block. Do not repeat proportional-base small-rotation grids after the present local stability result. The global complete constant still requires a global inequality or a separately certified finite separation witness with the same scalar normalization.

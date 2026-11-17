# Audited historical reading edition

**Current audited claim:** PROVED: Every biased 0<p<1 has exactly one nondegenerate scalar minimizer in the stated side of sqrt(q/p), with 0<alpha1(p)<1; the proportional local theorem applies.

**Claim ceiling:** No sharp numerical optimum, p/dimension-uniform matrix neighbourhood or new global-generator result.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# General two-state weights — scalar minimizer and matrix local corollary

**Verdict:** `PROVED` internally. The scalar extension survives for every biased p in (0,1), p!=1/2. This is a complete analytic argument, with supplementary exact algebra canaries. No human review, formal verification, priority claim or global biased MLSI/CMLSI equality is established. The supplied Gemini assessment is recorded as AI-assisted review of the named **v2** material, not review of the new v3 extension.

## Definitions and exact claim

Use q=1-p, a=pr+q,

`d_p(r)=pr log r-a log a`, `i_p(r)=pq(r-1)log r`, `k_p(r)=i_p(r)/(2d_p(r))`.

r>0,r!=1; logs are natural. The classical generator is L=I-E_pi with weights (p,q), and the convention is 2 alpha D<=I. Extend the scalar quotient continuously at r=1 only. p=0 and p=1 remain excluded.

For every 0<p<1, p!=1/2, there is exactly one global scalar minimizer r_p. If p<1/2 then r_p>sqrt(q/p)>1; if p>1/2 then r_p<sqrt(q/p)<1. It satisfies k_p''(r_p)>0 and 0<alpha1(p)=k_p(r_p)<1. For p=1/2 the scalar extension has unique minimum k(1)=1, with k''(1)=1/12; the unextended quotient attains no minimum off 1.

## Scalar derivatives and orientation

Differentiation gives

`d'=p log(r/a)`, `d''=pq/(r a)>0`,

`i'=pq(log r+1-1/r)`, `i''=pq(r+1)/r²`.

d,i and their first derivatives vanish at 1. For f=d or i, Taylor's integral remainder is

`f(r)=integral_1^r (r-t) f''(t)dt`.

For r<1, reversing bounds gives **positive** weights:

`f(r)=integral_r^1 (t-r) f''(t)dt`.

Equivalently, on either side,

`f(r)=(r-1)² integral_0^1 (1-u) f''(1+u(r-1))du`.

Thus i/d is a positive weighted mean of R=i''/d'', not a mean with negative weights below 1. Since d''>0, d(r)>0 off 1. The last representation cancels the common quadratic zero and proves joint real-analytic scalar removal near (p,r) with p in (0,1), r=1. It gives

`k_p(1)=1`, `k_p'(1)=(2p-1)/6`.

One can check the latter directly: for h=r-1,

`d=pq h²/2-pq(1+p)h³/6+O(h⁴)`,

`i=pq h²-pq h³/2+O(h⁴)`.

For each fixed p in (0,1), as r tends to zero, `d->-q log q>0` and `i~-pq log r`, so k->infinity. As r tends to infinity, `d~pr log(1/p)` and `i~pq r log r`, so k->infinity. These are fixed-weight limits, not uniform estimates as p approaches an endpoint.

## Every 0<p<1/2: existence, uniqueness and nondegeneracy

Here q>p. Set

`R(r)=1+pr+q/r`, `R'=p-q/r²`, `tau=sqrt(q/p)>1`.

R strictly decreases up to tau and increases afterward. For 0<t<1,

`R(t)-2=(1-t)(q/t-p)>0`.

The positively oriented integral mean therefore gives k(r)>1 for 0<r<1. For 1<r<=tau, R(t)<2 throughout 1<t<r, giving k(r)<1. Together with k(1)=1, both divergent endpoint limits and continuity, this proves existence of an interior global minimum r_p>1. To be explicit, choose one point with k<1; divergent endpoint tails and the value at 1 confine a minimizing sequence to a compact interval away from 0,1 and infinity.

For r>1, d>0 and d'>0. Define

`H=i'/d'`, `A=d'R-i'`.

Using d''R=i'',

`A'=d'R'`, `H'=d''A/(d')²`.

A tends to 0 at 1+. It is strictly negative on (1,tau], strictly increasing on (tau,infinity), and tends to infinity. For the last assertion, d' tends to p log(1/p)>0, R~pr and i'=O(log r). Hence exactly one c1>tau has A(c1)=0. H' is negative on (1,c1) and positive on (c1,infinity).

Now let `J=dH-i`. Since H tends to R(1)=2 at 1+, J tends to 0, and

`J'=dH'`, `k'=d'J/(2d²)`.

J is strictly negative through c1 and strictly increasing thereafter. An interior minimizer already exists and must have J=0, so there is exactly one such root, it lies beyond c1, and no other r>1 is critical. No r<1 can minimize because its k exceeds 1. Thus this is the unique global minimizer.

At the root, J=0 and J'=dH'>0. Differentiating the exact formula for k' yields

`k_p''(r_p)=d'(r_p)J'(r_p)/(2d(r_p)²)>0`.

This proves strict nondegeneracy, not merely uniqueness. Positivity of i,d and the attained interior minimum gives alpha1>0; the earlier point k<1 gives alpha1<1. Nothing in this proof requires a rational optimizer bracket or a numerical solve.

## Every 1/2<p<1: explicit state swapping

Write q=1-p<1/2. Direct substitution, retaining the scaling of entropy/production, gives

`d_p(r)=r d_q(1/r)`, `i_p(r)=r i_q(1/r)`,

and therefore `k_p(r)=k_q(1/r)`.

Differentiating **before** setting a critical point gives

`k_p'(r)=-r^(-2) k_q'(1/r)`,

`k_p''(r)=2r^(-3) k_q'(1/r)+r^(-4) k_q''(1/r)`.

The reciprocal map is a bijection of positive ratios, so the unique minimum is r_p=1/r_q, alpha1(p)=alpha1(q), and

`k_p''(r_p)=r_p^(-4) k_q''(r_q)=r_q^4 k_q''(r_q)>0`.

The first derivative term vanishes at this point only because stationarity has been established. Since r_q>sqrt(p/q), r_p<sqrt(q/p)<1. Using r² instead of r⁴ would be an incorrect nondegeneracy transfer formula even though its sign might accidentally remain positive.

## Symmetric weight p=1/2 and the limit of biased weights

For p=q=1/2, `R(r)=1+(r+1/r)/2>=2`, with equality only at r=1. On each nontrivial positively oriented remainder interval, the mean is strictly greater than 2. Thus k(r)>1 off 1 and the smooth scalar extension has unique minimum 1 at r=1. Expansion gives

`k_(1/2)(1+h)=1+h²/24+O(h³)`, so `k_(1/2)''(1)=1/12`.

**This does not admit r=1 into the proportional-base matrix theorem:** at A=B, D=I=0 and Q is undefined.

For completeness, the known uniform two-state matrix inequality can be proved separately with the correct normalization. Let M=(A+B)/2, W=(A-B)/2 and f(C)=tr C log C. Put `g(t)=(f(M+tW)+f(M-tW))/2-f(M)`, 0<=t<=1. Then D=g(1), I=g'(1), g(0)=g'(0)=0. For each s>=0 let K_s=(M+sI)^(-1/2) W (M+sI)^(-1/2). Positivity of A,B implies the eigenvalues kappa of K_s have absolute value <1. Resolvent differentiation gives

`g''(t)=integral_0^infinity sum_kappa [kappa²/2*((1+t kappa)^(-2)+(1-t kappa)^(-2))] ds`.

Each summand is nondecreasing in t in [0,1]. The expression is integrable because the original positive matrices stay uniformly positive on this compact segment and the resolvents decay at infinity. Hence g'' is nondecreasing. Pair t with 1-t to get

`I-2D=integral_0^1 (2t-1)g''(t)dt>=0`.

Consequently Q>=1 whenever D>0, uniformly over finite matrix dimensions. Scalar ratios tending to 1 show sharpness, so alpha1=alpha_c=1 for **L=I-E_uniform**. At A=B the inequality holds as 0>=0 while Q remains undefined. This is known prior art, not a new biased global result. Wirth–Zhang's CLSI(2) convention uses lambda D<=I, corresponding to alpha=lambda/2=1; the nonconstant character of Z2 decays at rate 1, matching this reset generator. Multiplying the generator by 2 multiplies both constants by 2.

The scalar limit is also controlled without claiming matrix uniformity. Joint scalar analyticity near (p,r)=(1/2,1), together with k_r=0, k_rr=1/12 and k_rp=1/3 there, permits the implicit function theorem. Its stationary branch obeys `r_p=1-4(p-1/2)+O((p-1/2)²)`; uniqueness for biased weights identifies it with r_p. Thus r_p->1, alpha1(p)->1 and k_p''(r_p)->1/12. Nonetheless `d_p(r_p)->0`: the matrix base approaches a zero-entropy point. The previous local-neighborhood theorem cannot be extended through that point or assigned a uniform radius by this limit argument.

## Exact strongest matrix corollary

For **each** p in (0,1) excluding 1/2, let r_p be the unique minimizer just proved, and alpha1(p)=k_p(r_p). For **each** integer n>=1 and **each** positive definite B0 in M_n(C), there are c=c(p,n,B0)>0 and an open neighborhood U of (r_p B0,B0) such that every Hermitian pair (A,B) in U is positive definite, has D_p(A,B)>0, and

`Q_p(A,B)>=alpha1(p)+c||A-r_p B||_F²`.

Choose c strictly below the Taylor lower-bound coefficient (for example m0/8 when the proof guarantees m0/4); the displayed inequality is then strict unless A=r_p B. Equality holds exactly on that proportional manifold. At every proportional base B>0 its full Hermitian Hessian is

`D²Q_p[X,Y]=k_p''(r_p)/tr B * tr[(X-r_pY)Dlog_B(X-r_pY)]`.

All scalar assumptions of the earlier parameterized theorem are now proved for the actual scalar optimum for every biased weight. Complex conjugacy, repeated eigenvalues and proportional null directions remain covered by that theorem. Swapping states also checks the matrix expression: Q_p(A,B)=Q_q(B,A), E_(rB)(Z/r)=r^(-3)E_B(Z), and tr(rB)=r tr B, recovering the r^(-4) scalar factor.

This is still a **local** result. No neighborhoods uniform in p, n or distance from the positive-cone boundary, no singular-state extension and no global biased MLSI/CMLSI equality have been proved. The symmetric known global inequality above is a distinct argument.

## Review and evidence limits

The Gemini review record (historical local record; not distributed here) pins the supplied AI assessment and local named-v2 hash. Its main completed derivations agree with the manuscript; unfinished antiderivatives with ellipses are not full proofs. A completed auxiliary integral identity is given in manuscript v3. The claim “error-free” is not adopted as a guarantee. No human review, blind reproduction, formal verification or novelty proof results from that assessment. New v3 swapping/symmetric/general-biased claims are outside its reviewed version.

The exact canaries (historical local record; not distributed here) check nine rational weights, six reciprocal derivative cases, orientation and domain controls. They are supplementary finite algebra checks, not the all-p proof. A first orientation fixture merely returned its expected closed form; its test-oracle weakness was preserved and repaired to evaluate the actual antiderivative at ordered bounds before confirmation.

Primary comparison and limitations are in the cycle035 source note (historical local record; not distributed here). This is a new project derivation; novelty/priority remain unestablished. Mixed-base investigation was not resumed during this task.

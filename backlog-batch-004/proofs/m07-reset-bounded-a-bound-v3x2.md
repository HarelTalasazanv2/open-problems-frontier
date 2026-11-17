# Audited historical reading edition

**Current audited claim:** PROVED: The same A(p) lower bound and displayed exponential entropy decay hold for bounded positive families under the explicit nonnegative resolvent production convention.

**Claim ceiling:** No unbounded L1 extension, sharpness, all-classical-generator equality or fresh external-definition equivalence.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M07 bounded positive reset extension — internal proof V3x2

Root accepted this proof under the fresh fixed convention after all six roles and root dependency review. It uses the accepted V3 positive-invertible theorem, standard bounded-operator functional calculus and elementary nonnegative integral convergence. It does not assume the old source's singular-extension verdict or import joint convexity, sharp constants, tensorization or a fresh external definition match.

## 1. Exact bounded class and extended production

Fix k>=2, pi_i>0, sum pi_i=1, p=min pi_i, and a finite von Neumann algebra(Q,tau) with faithful normal tracial state. Let f_i be arbitrary bounded positive elements, including zero and non-invertible ones. Choose finite M>=1 with 0<=f_i<=M1 and set m=sum pi_i f_i. Define phi(0)=0 and phi(x)=x log x for x>0, and

\[
H(f)=\sum_i\pi_i\tau(\phi(f_i))-\tau(\phi(m)).
\]

This is finite because phi is continuous on[0,M]. Positivity follows by the regularization argument below.

For bounded A,B>=0 put X=A-B and define, in the extended nonnegative reals,

\[
J(A,B)=\int_0^\infty
 \|(B+s1)^{-1/2}X(A+s1)^{-1/2}\|_2^2\,ds,
\qquad
I_{\rm ext}(f)=\frac12\sum_{i,j}\pi_i\pi_jJ(f_i,f_j).
\]

For every s>0 all resolvents are bounded, the squared norm is nonnegative and continuous in s, and its scalar integral is well-defined in[0,infinity]. The finite ordered-pair sum has no subtraction of infinities. The factor1/2 is part of the fixed convention. For c(I-E_pi), c>0, production is cI_ext, with c*infinity=infinity.

The main claim is

\[
I_{\rm ext}(f)\ge2A(p)H(f),\qquad
A(p)=\frac{(1-p)\log(1/p)}{2(\log(1/p)-1+p)}.
\]

## 2. Exact regularization and monotone production

For epsilon>0 write A_e=A+epsilon1, B_e=B+epsilon1 and

\[
J_\epsilon(A,B)=\tau[(A-B)(\log A_e-\log B_e)].
\]

The log resolvent difference is norm-integrable for fixed epsilon>0 and gives

\[
\log A_e-\log B_e
=\int_\epsilon^\infty[(B+s1)^{-1}-(A+s1)^{-1}]\,ds
=\int_\epsilon^\infty(B+s1)^{-1}X(A+s1)^{-1}\,ds.
\]

The tail is norm-bounded by ||X||/s^2, and the finite lower cutoff removes the0singularity. Pairing with X and cyclicity of tau show

\[
J_\epsilon(A,B)
=\int_\epsilon^\infty\tau[X(B+s1)^{-1}X(A+s1)^{-1}]\,ds
=\int_\epsilon^\infty
\|(B+s1)^{-1/2}X(A+s1)^{-1/2}\|_2^2\,ds.
\]

The last identity follows from ||Y||_2^2=tau(Y*Y). Thus J_epsilon>=0 and increases to J as epsilon decreases to0. Symmetry follows either from its trace-log expression and passage to the limit or by interchanging A,B there; it need not be guessed from the displayed norm ordering.

Set f_i^epsilon=f_i+epsilon1 and m^epsilon=m+epsilon1. Direct finite-sum expansion gives

\[
I(f^\epsilon)
=\sum_i\pi_i\tau[(f_i-m)\log(f_i+\epsilon1)]
=\frac12\sum_{i,j}\pi_i\pi_jJ_\epsilon(f_i,f_j).
\]

Therefore I(f^epsilon) increases to I_ext(f). In the uniformly positive case the same formula at epsilon0 agrees with the V3production, including its coefficient and generator sign. Nothing is defined by discarding zero eigenvalues or clipping a logarithm.

## 3. Relative-entropy convention and its extended values

For A,B bounded positive, define

\[
\mathfrak D_\tau(A\|B)
=\tau(\phi(A))-\tau(A)+\tau(B)
 -\lim_{\epsilon\downarrow0}\tau[A\log(B+\epsilon1)].
\]

This formula is meaningful: log(B+epsilon1) decreases as epsilon decreases, by scalar functional calculus of B. The positive pairing tau[A^(1/2)(.)A^(1/2)] preserves the order. For epsilon<=1, log(B+epsilon1)<=C1, where C=log(M+1) and M bounds A,B. Thus the trace limit lies in[-infinity,C tau(A)]; equivalently define it using the increasing positive trace of A^(1/2)[C1-log(B+epsilon1)]A^(1/2). Only a finite constant is subtracted from that positive extended limit.

For epsilon>0 the mass-corrected tracial Bregman quantity

\[
\mathfrak D_\tau(A_e\|B_e)
=\tau(\phi(A_e))-\tau(A_e\log B_e)-\tau(A_e)+\tau(B_e)
\]

is nonnegative. Indeed it is the Taylor remainder of F(t)=tau(phi(B_e+t(A-B))), whose Hessian is nonnegative by the V3resolvent derivation.

As epsilon decreases to0, tau(phi(A_e))->tau(phi(A)) by uniform continuity of phi on a common compact spectral interval. Also

\[
|\epsilon\tau\log(B+\epsilon1)|
\le\epsilon\max\{|\log\epsilon|,|\log(M+1)|\}\longrightarrow0.
\]

The mass correction is exactly -tau(A)+tau(B). Expanding the regularized expression therefore shows

\[
\mathfrak D_\tau(A_e\|B_e)\longrightarrow\mathfrak D_\tau(A\|B)\in[0,\infty].
\]

Here nonnegativity follows from the limit of the positive remainders, rather than an unproved support criterion. Since both directional limits are nonnegative extended numbers, their sum is defined and

\[
J(A,B)=\mathfrak D_\tau(A\|B)+\mathfrak D_\tau(B\|A).
\]

In particular D(0||B)=tau(B), D(A||0)=infinity for A!=0, and J(0,0)=0. Equal support is not a finiteness guarantee in a general finite von Neumann algebra.

### Entropy is relative entropy to the fixed-point expectation

On N=ell-infinity({1,...,k}) tensor Q with trace tau_pi=sum_i pi_i tau, regard f=(f_i) and E_pi f=(m,...,m). Applying the same declared D convention in N gives

\[
\mathfrak D_{\tau_\pi}(f\|E_\pi f)=H(f).
\]

Indeed the linear masses agree, and for every epsilon>0,

\[
\sum_i\pi_i\tau[f_i\log(m+\epsilon1)]
=\tau[m\log(m+\epsilon1)]\longrightarrow\tau(\phi(m)).
\]

The last convergence is uniform functional calculus, since0<=x log(x+epsilon)-phi(x)<=epsilon for0<=x<=M (value0 atx=0). Thus the product-algebra relative entropy is finite and exactly H. Equivalently each D_tau(f_i||m) is finite and their pi-weighted sum is H; finiteness follows because the individual decreasing cross-logarithms have uniform finite upper bounds while their finite positive-weighted sum has a finite limit. This identifies the entropy in the complete bounded-density convention without assuming log(m) is bounded.

## 4. Passing the accepted V3bound to the boundary

For each epsilon>0 the family f^epsilon is bounded uniformly invertible, so the exact accepted V3theorem yields

\[
I(f^\epsilon)\ge2A(p)H(f^\epsilon).
\]

Uniform continuity of phi gives operator-norm convergence phi(f_i+epsilon1)->phi(f_i) and phi(m+epsilon1)->phi(m). Thus H(f^epsilon)->H(f), and H(f)>=0 as a limit of nonnegative entropies. Section2 gives I(f^epsilon) increasing to I_ext(f). Passing to these two scalar limits proves I_ext>=2A(p)H, whether the production limit is finite or infinite. No V3lower spectral bound, Hessian domination uniform in epsilon, or singular pencil spectral measure has been assumed.

The conclusion is at the entire bounded-positive class of all stated finite tracial auxiliaries, not merely finite matrices or inputs invertible in a support corner.

## 5. Boundary cases and meaningful contrary controls

**Zero and equilibrium.** If all f_i=a, every pairwise difference is0, so J=I_ext=H=0, even if a is singular or zero. No entropy quotient or0times infinity occurs.

**Common kernel.** Let e=s(m). The order pi_i f_i<=m implies s(f_i)<=e. Every difference vanishes on1-e; for positive cutoff the logarithms on1-e are the same scalar log epsilon. The common zero block therefore contributes neither production nor entropy. One may restrict to eQe, but this proof does not require a spectral gap there. For e!=0, a restricted unnormalized trace multiplies both sides by its mass; renormalizing it cannot change the inequality. If e=0, use the allzero case without normalizing.

**Unequal supports.** If s(A) is not<=s(B), set r=1-s(B). Faithfulness gives tau(Ar)>0. For epsilon<=1,

\[
\tau[A\log(B+\epsilon1)]
\le(\log\epsilon)\tau(Ar)+C\tau(A(1-r))\longrightarrow-\infty.
\]

Thus D(A||B)=infinity. If the two supports differ, at least one directional inclusion fails, so J(A,B)=infinity. A positive weighted occurrence makes I_ext=infinity. This explains a case; the general proof does not require case splitting.

**Equal faithful support, infinite production.** In Q=L-infinity(0,1), tau(g)=integral_0^1g(t)dt, let A(t)=1 and B(t)=exp(-1/t). Both supports are1 and both inputs are bounded, but neither support equality nor faithfulness gives a uniform gap for B. Scalar substitution/monotone convergence gives

\[
J(A,B)=\int_0^1\frac{1-e^{-1/t}}{t}\,dt=\infty,
\]

because e^{-1/t}<=e^{-1}<1/2 on(0,1].

**Equal faithful support, finite production without a gap.** For A(t)=t and B(t)=2t on the same algebra,

\[
J(A,B)=\int_0^1t\log2\,dt=\tfrac12\log2<\infty.
\]

These two cases refute any proposed rule that decides finiteness from support equality or absence of a uniform gap alone. They are analytic cases, not a finite grid purporting to resolve infinite behavior.

**Scaling.** H(rf)=rH(f) for r>0 by cancellation of the mean log(r) terms. J_epsilon(rA,rB)=rJ_(epsilon/r)(A,B); hence I_ext(rf)=rI_ext(f), including infinity. Scaling the generator by c>0 gives cI_ext and coefficient cA(p). Trace rescaling multiplies both sides. c=0, negative weights and an unbounded L1class are outside the convention.

## 6. Entropy decay for the same complete bounded class

For c>0 define explicitly

\[
(T_t f)_i=e^{-ct}f_i+(1-e^{-ct})m.
\]

The mean is invariant. For fixed epsilon>0, T_t(f+epsilon1)=T_tf+epsilon1 stays uniformly positive, so ordinary differentiation under the finite trace gives

\[
\frac{d}{dt}H(T_t(f+\epsilon1))
=-cI(T_t(f+\epsilon1))
\le-2cA(p)H(T_t(f+\epsilon1)).
\]

The shifted family generally has total trace tau(m)+epsilon rather than1; the accepted V3theorem is unnormalized and homogeneous, so it applies directly. The added derivative-of-xlogx linear term cancels by the mean identity. Multiplying by exp(2cA(p)t) and integrating proves the regularized entropy bound. Passing epsilon to0 at each fixed t by the entropy continuity above yields

\[
H(T_t f)\le e^{-2cA(p)t}H(f),\qquad t\ge0.
\]

This does not differentiate a singular initial entropy or require finite initial production. It quantifies every finite tracial auxiliary and every bounded positive normalized density tau(m)=1 (indeed every unnormalized bounded positive family). It is a complete bounded-reset entropy-decay/lower-bound statement under the fixed displayed convention. The matching of an uncaptured external article's definition is not newly authenticated by this proof.

## Claim ceiling and stopping point

The bounded non-invertible completion and its explicitly defined production/relative-entropy identification are established internally, with the corresponding bounded-class entropy decay. Sharpness, equality to the scalar optimum, general classical generators, an unrestricted-state converse, unbounded L1input extension, current-world status, novelty, human/external review and formal verification remain outside this result. The six-role agreement is correlated source-exposed internal review, not six independent scientific confirmations or a measured factor-of-two improvement.


## Concurrent C165 reconciliation — supplemental reviewed proof

# Concurrent C165 production reconciliation

C165completed while this explicitly user-selected bounded-extension task was running. Its current production is I0(f)=sum_i pi_i J0(f_i,m), whereas this task fixed I_ext=(1/2)sum_(i,j)pi_i pi_j J(fi,fj). Both J0andJ are the identical positive resolvent norm-square integral: cyclicity changes no value. No convention is silently swapped.

For every epsilon>0, all logarithms below are bounded and the same mean m+epsilonI applies. The finite mean identity gives

    sum_i pi_i J_epsilon(f_i,m)
      =sum_i pi_i tau[(fi-m)(log(fi+epsilonI)-log(m+epsilonI))]
      =sum_i pi_i tau[(fi-m)log(fi+epsilonI)]
      =I(f+epsilonI)
      =(1/2)sum_(i,j)pi_i pi_j J_epsilon(fi,fj).

Each summand on both outer expressions is nonnegative and increases to its corresponding resolvent integral as epsilon decreases. Finiteness of the index set therefore permits both limits in[0,infinity], proving

    I0(f)=I_ext(f), including infinite values.

Together with the reviewed convention theorem this also gives

    I0(f)=sum_i pi_i [D_tau(fi||m)+D_tau(m||fi)]
          =H(f)+sum_i pi_i D_tau(m||fi).

Every D here is nonnegative extended and H is finite, as proved in the main candidate; there is no infinity subtraction. This identifies C165's production with the explicitly defined mass-corrected tracialD convention and permits the same bounded-positive inequality and entropy-decay consequence.

It doesNOT freshly authenticate that this explicit definition is the exact externally published primary definition desired by C165's prepared packet. That primary-body alignment remains held offline. Thus the current C165bridge may be marked partially discharged(explicit-definition identity proved) with external-primary alignment stillINCONCLUSIVE, not blanketPROVED. The C165lemma, conditional theorem, counter-shortcut and its evidence remain unchanged as historical source records; only a precisely scoped bridge annotation is warranted.

This is reconciliation of a concurrent actual native-state change within the already user-authorized fresh bounded task. It is not automatic selection of an unrelated/new research family. The stale staged plan was not applied; all C165records must be retained and a postC165baseline guards integration.

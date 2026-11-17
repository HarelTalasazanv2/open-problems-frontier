# Audited historical reading edition

**Current audited claim:** PROVED: The specified pointwise positive-form limit gives a quotient contraction semigroup; condition R is exactly strong continuity, and the stated connected-correlation hypotheses yield a unique vacuum and gap.

**Claim ceiling:** Nontrivial excited sector needs a positive limiting connected variance. No gauge-field or reconstruction theorem is asserted.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M06: positive-form limits, continuity, vacuum and gap

Cycle096,2026-10-29UTC. **PROVED internally at the abstract scope below.** Pointwise convergence of positive forms is enough for the limiting quotient and bounded semigroup; a separate time-zero continuity condition is exactly what yields a self-adjoint Hamiltonian. A fixed normalized vacuum label survives. A unique vacuum and gap follow from the stated connected-correlation bounds, while survival of an excited sector requires nonzero limiting connected variance.

Claim ceiling: analytic statements about specified forms and semigroup maps, not construction of actual Yang–Mills functionals, fields, continuum limits, empirical masses, novelty, external human review or formal verification. The frozen attempt (historical local record; not distributed here) and 095 packet (historical local record; not distributed here) fix the scope. Standard spectral calculus and the positive square-root theorem for C*-algebras are imported foundations, not formalized here. No numerical or executable mathematical instrument was used.

## 1. Exact data and quotient construction

Let V be a complex vector space, Ω∈V, and T(t):V→V linear for every real t≥0, with

\[
T(0)=I,\quad T(s+t)=T(s)T(t),\quad T(t)\Omega=\Omega.
\]

For each n≥1 let B_n be a finite-valued Hermitian positive semidefinite sesquilinear form, conjugate-linear in its first argument, such that B_n(Ω,Ω)=1. Assume pointwise convergence B_n(u,v)→B(u,v) for all u,v∈V, and for all n,t,u,v assume

\[
B_n(u,T(t)v)=B_n(T(t)u,v),\quad
B_n(v,T(t)v)\ge0,\quad
B_n(T(t)v,T(t)v)\le B_n(v,v). \tag{1}
\]

No fixed null space or common pre-existing Hilbert space is assumed. Individual cutoff semigroups need not yet be strongly continuous. All limits in this section are fixed-label limits, not suprema over changing spaces.

The limiting B is Hermitian, sesquilinear and positive semidefinite, and B(Ω,Ω)=1, by passing the corresponding finite identities/inequalities to the limit. Every positive semidefinite form obeys Cauchy–Schwarz: positivity of B(u+zv,u+zv) for complex z gives |B(u,v)|²≤B(u,u)B(v,v) (the zero-diagonal case follows by varying the linear term). Thus

\[
N=\{v:B(v,v)=0\}
\]

is a subspace and every vector in N pairs to zero with every vector. The form defines a genuine inner product on V/N. Complete this pre-Hilbert space to ℋ and write [v] for a quotient vector. Its image is norm dense by construction. Equation(1) passes to B, so T(t) preserves N. Consequently

\[
S(t)[v]=[T(t)v]
\]

is well defined and contractive on V/N, extends uniquely to a contraction on ℋ, and retains the semigroup laws. Symmetry in(1), initially on a dense subspace, makes each bounded S(t) self-adjoint; its quadratic forms are nonnegative, so S(t)≥0. The vector ω=[Ω] has norm1 and S(t)ω=ω. A fixed normalized label therefore does not suffer the moving-vector vacuum escape seen in094.

## 2. Exact regularity condition and the Hamiltonian

Consider

\[
\lim_{t\downarrow0}B(v,T(t)v)=B(v,v)\quad(v\in V). \tag{R}
\]

This is **necessary and sufficient** for strong continuity of S at0, and hence on all t≥0. Indeed

\[
\|S(t)[v]-[v]\|^2
\le2\bigl(B(v,v)-\operatorname{Re}B(v,T(t)v)\bigr)\to0.
\]

Contractions extend this convergence from dense quotient vectors to every w∈ℋ: approximate w by [v] and bound the remaining two errors by2||w−[v]||. Conversely strong continuity makes the displayed inner products converge. The semigroup law and contractivity give continuity at other times, from either side within [0,∞).

For completeness, the existence of a nonnegative self-adjoint generator can be obtained directly from spectral calculus. Let K=S(1), a positive self-adjoint contraction. If Ku=0, positivity and S(1)=S(1/2)² imply S(1/2)u=0; iterating gives S(2^{-j})u=0, and continuity at0 forces u=0. Thus K is injective and its spectral projection at0 is zero. Define

\[
H=-\log K
\]

by unbounded Borel spectral calculus on (0,1]. It is nonnegative and self-adjoint with dense domain: the spectral subspaces [1/m,1] lie in its domain and increase strongly to ℋ. Since S(1/m)^m=K and S(1/m)≥0, uniqueness of the positive spectral mth root gives S(1/m)=K^{1/m}. The semigroup law gives S(q)=K^q for nonnegative rational q. Strong continuity of S and dominated spectral convergence of K^q as q→t imply

\[
S(t)=e^{-tH}\quad(t\ge0). \tag{2}
\]

There is no hidden bounded-energy assumption. The zero spectral point of K may belong to continuous spectrum; injectivity is exactly what prevents an infinite-energy eigenvector from being smuggled into (2). Since S(t)ω=ω, spectral calculus gives Hω=0.

A sufficient stronger-looking condition is

\[
\lim_{t\downarrow0}\sup_n d_{n,v}(t)=0,
\qquad d_{n,v}(t)=B_n(v,v)-\operatorname{Re}B_n(v,T(t)v). \tag{U}
\]

Each d_{n,v}≥0 by contractivity and Cauchy–Schwarz. Since its pointwise limit is B(v,v)−ReB(v,T(t)v), (U) implies(R). Without individual-cutoff continuity, (U) need not be necessary: Section5C gives an exact finite-exception counterexample. No equivalence of(R) and(U) is assumed merely from pointwise form convergence.

## 3. Connected correlations give a unique vacuum and gap

Assume(R) and fix a single physical rate δ>0. Suppose that for every v∈V there are finite A_v,T_v≥0, independent of n, such that

\[
C_{n,v}(t):=B_n(v,T(t)v)-|B_n(\Omega,v)|^2
\le A_v e^{-\delta t}\quad(n\ge1,\ t\ge T_v). \tag{3}
\]

The modulus is essential. Set c_n=B_n(Ω,v), w_n=v−c_nΩ. Symmetry and T(t)Ω=Ω give B_n(Ω,T(t)v)=c_n. Expanding the sesquilinear form shows

\[
C_{n,v}(t)=B_n(w_n,T(t)w_n)\ge0. \tag{4}
\]

Thus these are genuine positive connected self-correlations, even though centering vectors vary with n. For each fixed v,t, form convergence gives

\[
C_{n,v}(t)\to C_v(t)=B(v,T(t)v)-|B(\Omega,v)|^2.
\]

Pass(3) to this limit at each fixed t≥T_v. Write W=|ω⟩⟨ω| and w=(I−W)[v]. Then C_v(t)=⟨w,e^{-tH}w⟩, and the family of such w is norm dense in ω-perpendicular. We do not yet identify W with the full zero-energy projection.

For 0≤a<δ, any positive scalar spectral mass c on [0,a] for one such w would give C_v(t)≥c e^{-at}, contradicting its eventual δ bound. Consequently E_H([0,δ)) annihilates every w in that dense family, and by bounded projection/density annihilates all ω-perpendicular. The inclusion of0 in this argument matters: it excludes additional zero-energy vectors. Since ω is a unit zero-energy vector,

\[
E_H(\{0\})=W,\quad
\operatorname{spec}(H)\cap(0,\delta)=\varnothing,\quad
\|e^{-tH}(I-W)\|\le e^{-\delta t}. \tag{5}
\]

The bound now has the optimal connected amplitude

\[
C_v(t)\le \bigl(B(v,v)-|B(\Omega,v)|^2\bigr)e^{-\delta t}
\quad(t\ge0). \tag{6}
\]

This is a quantified all-label/all-eventual-time implication. It does not turn a finite set of measured correlations into a dense family or a finite time window into an asymptotic statement. Spectrum at δ is permitted.

## 4. Nontriviality and the finite mass edge

The limiting excited space is nonzero if and only if some v∈V has

\[
\sigma_B(v):=B(v,v)-|B(\Omega,v)|^2>0. \tag{7}
\]

This equals ||(I−W)[v]||²; density proves the converse. Under(5) and(7), a nonzero excited spectral measure has positive mass in [δ,M] for some finite M. Its spectral subspace is nonzero and therefore

\[
\delta\le\inf\operatorname{spec}(H|_{\omega^\perp})\le M<\infty.
\]

This supplies finiteness of the abstract spectral edge, not an actual physical mass value, particle pole, or gauge field. Without(7), ℋ may equal ℂω and H=0; the supremum of admissible positive gaps is then infinite. Every cutoff being nontrivial does not ensure(7).

## 5. Exact adversarial models

### A. All cutoff gaps can survive while time continuity fails

Let V consist of finite sums aΩ+Σ_s c_s x_s, where s ranges over nonnegative real labels. Define T(t)Ω=Ω and T(t)x_s=x_{s+t}. Put ℓ_n(v)=Σ_s c_s e^{-ns} and

\[
B_n(v,w)=\overline a b+\overline{\ell_n(v)}\ell_n(w).
\]

The map q_n(v)=(a,ℓ_n(v)) is onto ℂ² and identifies the quotient with its ordinary inner product. It intertwines T(t) with diag(1,e^{-nt}). Thus every hypothesis(1) holds, each cutoff is strongly continuous with Hamiltonian diag(0,n), and each has a unique vacuum and gap n≥1. Null spaces vary with n. All labels satisfy

\[
C_{n,v}(t)=|\ell_n(v)|^2e^{-nt}
\le \left(\sum_s|c_s|\right)^2e^{-t}. \tag{8}
\]

The rate1, amplitudes and starting times are genuinely uniform in n. However ℓ_n(v)→c_0, so the limiting quotient is ℂ² with q(v)=(a,c_0). For t>0, q(T(t)v)=(a,0). Hence S(0)=I while S(t)=diag(1,0) for every t>0. The vector [x0] has norm1 and is immediately killed. This semigroup is not strongly continuous and cannot equal e^{-tH} for a densely defined self-adjoint H, whose finite-time exponential is injective. Here d_{n,x0}(t)=1−e^{-nt}, with supremum1 for every t>0; both(R) and(U) fail. **FALSIFIED:** pointwise forms, individually regular cutoffs and uniform connected gap bounds alone give a continuous limiting Hamiltonian. This is a continuity failure, not a numerical error or a counterexample to the theorem with(R).

### B. Nontrivial cutoffs can converge to only a vacuum

Take V=ℂ², Ω=(1,0), T(t)=diag(1,e^{-t}) and B_n(u,v)=overline(u0)v0+n^{-1}overline(u1)v1. Every cutoff is a two-dimensional Hilbert space with unique vacuum and gap1, and C_{n,v}(t)=|v1|²e^{-t}/n. The limiting form is B(u,v)=overline(u0)v0; its null space contains the entire second coordinate. Both(R) and(U) hold, but the completed limit is ℂω and no excited state remains. **FALSIFIED:** nontriviality of every cutoff plus uniform gap/regularity ensures nontriviality of the limit. Exactly the limiting variance witness(7) is absent.

### C. Uniform cutoff regularity is not necessary without individual regularity

Use the labels and T(t) from A. Let B_1(v,w)=overline a b+overline(c0)d0, the discontinuous quotient form from its limit. For every n≥2 take B_n(v,w)=overline a b+overline(Σ_s c_s e^{-s})(Σ_s d_s e^{-s}). The limiting form is this latter, continuous two-dimensional form, with S(t)=diag(1,e^{-t}); hence(R) holds. But d_{1,x0}(t)=1 for t>0, so(U) fails. Every algebraic/positive/contractive premise holds. **FALSIFIED at the stated base scope:**(U) is necessary for limiting continuity without assuming every individual cutoff is continuous. The only bad cutoff here is a finite exception; it cannot be discarded when taking sup over all n. SectionC does not address the stronger hypotheses with individual continuity at every n.

### D. Normalization and complex controls

For the ordinary inner product on ℂ², Ω=(1,0), v=(i,1), the correct connected variance is2−|i|²=1. Replacing the modulus square by i² would give3 and change under a phase, so it is not an orthogonal projection formula. If the vacuum norm were2 instead of1, even v=Ω in a trivial fixed sector would give the incorrect subtraction2−4=−2. Unit normalization or the correct normalized projection is indispensable. These are admissibility controls, not actual QFT counterexamples. A proposed negative one-time transfer cannot be part of an everywhere self-adjoint semigroup with a self-adjoint half-time square; the full semigroup contract rejects that input.

## 6. New source increment and a bounded representation lemma

[Schlingemann's author-deposited hep-th/9802035v1](https://arxiv.org/abs/hep-th/9802035v1) was already pinned095, PDF SHA-25640f33c2ce7b4b7bf12d43e485037ceb5ca3a36e0ed1fb188323efad4fa843af4. New full text18–21 and full visuals18,19,20 were inspected096; these were unread095. Same bytes and publication, not an independent source. Exact records are in the 096 inspection register (historical local record; not distributed here).

Physical18 Proposition3.5 represents the time-zero C*-algebra by π(b)[a]=[ba]. Here is an explicit norm check at that restricted contract. Assume the source's reflection-positive form B(a,d)=η(θ(a*)d) on A+, and a unital C*-subalgebra B0⊂A+ fixed pointwise by θ. For b∈B0 put c=(||b||²1−b*b)^{1/2}∈B0. Reflection positivity of ca gives

\[
0\le\eta(\theta(a^*)c^2a)
=\|b\|^2B(a,a)-B(ba,ba).
\]

Thus π(b) preserves the null space and extends boundedly with ||π(b)||≤||b||. Also B(ba,d)=B(a,b*d), proving π(b)*=π(b*), and multiplication/unitality follow directly. This is a complete local proof under the declared RP/C*-subalgebra hypotheses; no positivity of η on the whole Euclidean algebra is silently assumed. The positive C*-square-root theorem is imported. Faithfulness or nontriviality of π is not proved: for B0=ℂ² and η evaluation on one coordinate, a nontrivial input algebra can have a one-dimensional quotient representation.

The rest of source18–21 concerns observable-net locality via complex domains and a holomorphy lemma delegated to the unread appendix. In the literal v1 page20 display defining I, X2 is repeated in places where the preceding two-generator notation involves X1,X2. This is a source-index ambiguity to resolve against the intended definition or another version, **not an adjudicated refutation** of its locality theorem. The full analytic domains, appendix and version correspondence were not checked. OriginalOS1973/1975 full proofs and equivalence to every official Yang–Mills requirement remain held. A pure vacuum state, uniqueness, a gap and actual gauge fields are not supplied by the bounded representation lemma.

## 7. Adjudication ceiling and continuation control

The positive-form theorem, exact regularity criterion, canonical vacuum, conditional unique-vacuum/gap result and limiting-variance condition are internally proved. The named continuity shortcut, automatic nontriviality shortcut and base-scope necessity of(U) are false by the models above. The bounded time-zero representation estimate is locally proved at its own source contract. Full QFT reconstruction and actual Yang–Mills inputs remain NOT_TESTED. Source-index ambiguity remains INCONCLUSIVE.

This is one exposed analytic derivation and adversarial review sharing standard spectral foundations, not blind reproduction, an independent implementation, external expert review or formalization. Exact formula controls are not finite numerical evidence. Record hashes support local custody only; performance is NOT_MEASURED. A separately frozen extension may test cutoff-dependent amplitudes under individual continuity; it is not licensed by silently swapping n and t limits. After this third substantive M06 result, rerank the whole frontier before another adjacent extension.

## 8. Separately frozen extension: cutoff-dependent constants

The extension freeze (historical local record; not distributed here) was saved after the sufficient theorem and controls above passed their core internal review (historical local record; not distributed here). This section appends to the unchanged core byte prefix recorded there. **PROVED under the additional individual-continuity hypotheses below.** It does not retract the base-scope distinction in Section2 or its finite-exception model.

Assume now that, for every n, the quotient/completion induced by B_n has a strongly continuous semigroup S_n(t). The construction in Section2 gives S_n(t)=e^{-tH_n}, H_n≥0, and ω_n=[Ω]_n has norm1. Replace(3) by the weaker condition

\[
\forall n,v\ \exists A_{n,v},T_{n,v}<\infty:
\quad C_{n,v}(t)\le A_{n,v}e^{-\delta t}\quad(t\ge T_{n,v}), \tag{9}
\]

with nonnegative constants and the **same δ>0** for all n and v. The time parameter is common to the cutoff family; changing lattice time units is not an allowed implicit rescaling.

Fix n first. The centered quotient vectors [v]_n−B_n(Ω,v)ω_n are dense in ω_n-perpendicular. The positive spectral-measure argument of Section3, including zero in [0,a] for a<δ, excludes all spectral mass below δ on that complement. Hence ker H_n=ℂω_n, and for all labels v and all t≥0,

\[
0\le C_{n,v}(t)
\le \sigma_n(v)e^{-\delta t},\qquad
\sigma_n(v)=B_n(v,v)-|B_n(\Omega,v)|^2. \tag{10}
\]

Thus the unknown cutoff-specific amplitudes and starting times have been eliminated **before** taking the cutoff limit. Since σ_n(v)→σ_B(v), pointwise form convergence passes(10) at each fixed t to(6). Under(R), the limiting Hamiltonian consequently has the unique normalized vacuum and gap(5). Nontriviality still requires(7). There is no exchange of n→∞ and t→∞: the infinite-time implication was proved separately at each fixed n, yielding an all-time estimate with a convergent amplitude. This relaxation would not cover finite-time samples, only finitely many labels, cutoff-dependent rates with no common positive lower bound, or noncontinuous individual semigroups.

### Under individual continuity, (R) and (U) are equivalent

For each fixed v, the spectral theorem for H_n shows

\[
d_{n,v}(t)=\langle[v]_n,(I-e^{-tH_n})[v]_n\rangle
\]

is nonnegative and nondecreasing in t, and tends to0 as t↓0. For each fixed t, it converges to d_v(t)=B(v,v)−ReB(v,T(t)v). If(R) holds, given ε>0 choose a>0 with d_v(a)<ε. Pointwise convergence gives an N such that d_{n,v}(a)<2ε for all n≥N. Monotonicity then gives the same bound for every 0≤t≤a and all those n. For the finitely many n<N, their individual continuity supplies 0<b≤a with d_{n,v}(t)<ε whenever 0≤t≤b. Therefore sup_n d_{n,v}(t)≤2ε for 0≤t≤b, proving(U). The converse was already established in Section2.

The equivalence is labelwise, not uniform over all v. It uses every individual cutoff's continuity and positivity/monotonicity; the discontinuous n=1 example in Section5C fails that new hypothesis, so there is no contradiction. The pointwise limit need not be continuous merely because every cutoff is: Section5A remains the exact control. This resolves the comparison of continuity conditions and the cutoff-dependent-constant question within the declared extension, while actual field/functional inputs remain absent.

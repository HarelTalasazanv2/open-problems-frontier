# Audited historical reading edition

**Current audited claim:** PROVED: Under the specified strong convergence of fixed-time self-adjoint semigroups and uniform excited operator-norm bound, the limit retains the stated spectral exclusion and vacuum projections converge strongly.

**Claim ceiling:** Abstract operators on one Hilbert space; no actual Yang-Mills construction, vacuum-survival or empirical mass assertion.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M06: one-time spectral-gap transfer, surviving vacua, and physical units

Cycle094, 2026-10-29 UTC. **Verdict: PROVED at the abstract operator scope below.** Two weaker implications are **FALSIFIED** by exact examples. The Yang–Mills construction is **NOT_TESTED** by these arguments and remains open as reported by Clay.

Claim ceiling: this is an internal analytic proof for specified nonnegative self-adjoint operators on one Hilbert space. It neither constructs a quantum field theory nor establishes any actual Yang–Mills approximation, physical mass, empirical result, novelty, external expert review, or formal verification.

## 1. Custody, scope, and the source contract

The original attempt (historical local record; not distributed here) and captures survived an interrupted epoch. No proof/report/event/closeout had been saved. The recovery freeze (historical local record; not distributed here) retains that interruption and starts a new finite epoch; it does not retroactively satisfy the original elapsed-time cap. The present document is the saved proof, not a reconstruction of a previously saved proof.

[Clay's owning page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/), checked 2026-10-29 including during recovery, labels the problem Unsolved. This is a bounded owning-source check, not exhaustive literature or novelty coverage. The [official Jaffe–Witten description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), physical pages5–12, was read as text; pages5,6,11,12 were visually checked. Its14-page PDF SHA-256 is `3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09`. Full inspection records are here (historical local record; not distributed here).

Source crosswalk (source reports, not locally proved QFT axioms):

| Pages | Required distinction |
|---|---|
|5–6|A nontrivial theory for every compact simple gauge group on R4 must satisfy suitable axioms, with positive energy, a vacuum, local gauge-invariant fields, and the stated ultraviolet behaviour.|
|6|The spectral condition excludes (0,Δ). The supremum m of admissible Δ must also be finite. Adding this finite-mass qualification clarifies the previous brief catalog statement.|
|6|The displayed clustering statement concerns spatially separated local fields. It is not itself a full temporal semigroup operator bound.|
|11–12|Lattice limits must supply the fields, Hilbert space and required properties. Compactness alone is expressly insufficient; volume and cutoff limits require control.|

The source's historical progress and speculative mechanisms are not adopted as a current literature survey. Its cited axiom systems and reflection-positivity theorem are not reproduced here. An isolated one-particle state, confinement, and an identified particle mass are not consequences proved below.

## 2. Precise theorem: one physical time suffices

Let ℋ be a fixed complex Hilbert space. For every n≥1 let H_n, and also H, be densely defined nonnegative self-adjoint operators on ℋ. Fix a **single physical time** t0>0 and a constant δ>0 independent of n. Write

\[
K_n=e^{-t_0H_n},\quad K=e^{-t_0H},\quad
P_n=E_{H_n}(\{0\}),\quad Q_n=I-P_n,\quad r=e^{-\delta t_0}<1.
\]

Assume

\[
K_n\longrightarrow K\quad\text{strongly},\qquad
\|K_nQ_n\|\le r\quad\text{for every }n. \tag{A}
\]

Then P_n converges strongly to P=E_H({0}),

\[
\operatorname{spec}(H)\cap(0,\delta)=\varnothing,
\qquad
\|e^{-tH}(I-P)\|\le e^{-\delta t}\quad(t\ge0). \tag{B}
\]

The endpoint δ is allowed in the spectrum. Neither P≠0 nor I−P≠0 is asserted. Assumption(A) is a full operator norm bound, quantified over all vectors; it is not a finite sample of matrix elements. A common Hilbert space, identification of the limiting operator as e^{-t0H}, and nonnegative self-adjointness are actual hypotheses, not products of this theorem.

### Proof

The spectral theorem gives positive self-adjoint contractions K_n,K, with K_nP_n=P_n=P_nK_n. For every integer j≥1,

\[
K_n^j=P_n+(K_nQ_n)^j,\qquad
\|K_n^j-P_n\|\le r^j. \tag{1}
\]

For fixed j, strong convergence K_n→K and the uniform bound1 imply K_n^j→K^j strongly: induct on j using

\[
(A_nB_n-AB)v=A_n(B_n-B)v+(A_n-A)Bv
\]

for uniformly bounded A_n converging strongly and B_n converging strongly. Hence for each v∈ℋ and any n,l,

\[
\|(P_n-P_l)v\|
\le 2r^j\|v\|+\|(K_n^j-K_l^j)v\|. \tag{2}
\]

Choose j first so that the first term is arbitrarily small; then choose n,l large. Thus P_nv is Cauchy for every v. Define its limit Pv. Linearity and ||P||≤1 follow from those of P_n. Passing to inner products shows P=P*, and the bounded-product argument shows P_n²→P² strongly. Since P_n²=P_n, P²=P; therefore P is an orthogonal projection. Similarly K_nP_n=P_n=P_nK_n passes to KP=P=PK. Finally the strong limit of K_n−P_n yields

\[
\|K-P\|\le r. \tag{3}
\]

The complement Q=I−P reduces K and ||KQ||≤r. The eigenspace ker(K−I) equals ranP: inclusion of ranP follows from KP=P; a vector fixed by K has Q component fixed by KQ, and its norm would be at most r times itself, forcing that component to vanish. By spectral calculus e^{-t0λ}=1 on λ≥0 exactly when λ=0. Consequently P=E_H({0}).

If 0<a<δ and E_H((0,a])≠0, choose a unit v in that spectral subspace. Then Qv=v and

\[
\|Kv\|^2=\int_{(0,a]}e^{-2t_0\lambda}\,d\langle v,E_H(\lambda)v\rangle
\ge e^{-2t_0a}>r^2,
\]

contrary to(3). Taking an increasing sequence a↑δ gives E_H((0,δ))=0. The spectral theorem then gives the spectral exclusion in(B) and the norm bound for all t≥0. At t=0 the bound is ||Q||≤1; Q=0 is included. This covers continuous as well as point spectrum. ∎

### Quantitative projection approximation

Equations(1)–(3) also give ||K^j−P||≤r^j and

\[
\|(P_n-P)v\|\le 2r^j\|v\|+\|(K_n^j-K^j)v\|. \tag{4}
\]

If ε_n=||K_n−K|| is available, telescoping a difference of powers of contractions gives ||K_n^j−K^j||≤jε_n. Therefore

\[
\|P_n-P\|\le 2r^j+j\varepsilon_n\quad(j\ge1). \tag{5}
\]

In particular operator-norm convergence of K_n implies operator-norm convergence of P_n. This refinement has no asserted numerical rate when only strong convergence is given. The proof uses a uniform approximation by powers, rather than assuming convergence of discontinuous spectral projections.

## 3. Nonzero vacuum and nontrivial excitations are separate

If unit vectors Ω_n∈ranP_n converge **in norm** to Ω, then ||Ω||=1 and PΩ=Ω. Indeed

\[
\|(P_n-P)\Omega_n\|
\le2\|\Omega_n-\Omega\|+\|(P_n-P)\Omega\|\to0,
\]

and P_nΩ_n=Ω_n. Thus this additional condition ensures P≠0. More generally, a fixed v with liminf_n||P_nv||>0 suffices, by strong convergence. Weak convergence of normalized vacua need not suffice.

If every P_n has rank1 and P≠0, P has rank1. Otherwise take orthonormal u,v∈ranP. Their images P_nu,P_nv lie in a one-dimensional subspace, so their2-by-2 Gram determinant vanishes; strong convergence makes it tend to the Gram determinant of u,v, namely1, a contradiction. This rank conclusion uses the rank hypothesis. Identifying a Poincaré-invariant vacuum in a QFT with the full zero-energy subspace is a separate axiom/representation issue.

Survival of an excitation requires Q=I−P≠0. For example, a fixed w with liminf_n||Q_nw||>0 ensures it. If Q≠0, choose a nonzero v∈D(H)∩ranQ (dense there because Q is spectral). With

\[
m_Q=\inf\operatorname{spec}(H|_{Q\mathcal H}),
\qquad \delta\le m_Q\le\langle v,Hv\rangle/\|v\|^2<\infty, \tag{6}
\]

the limiting excited spectrum has a finite positive lower edge. This is an abstract energy statement, not construction of gauge-invariant local fields or a particle pole. If H=0 and P=I, (B) holds for every δ but the supremum of admissible gaps is infinite; this fails the official finite-mass/nontriviality requirement.

## 4. Exact counterexample: positive individual gaps do not transfer

On ℓ²({0,1,2,…}), with its orthonormal basis e_k, define bounded nonnegative self-adjoint operators by

\[
H_ne_0=He_0=0,\qquad
H_ne_k=\max\{1/n,1/k\}e_k,\qquad He_k=k^{-1}e_k\quad(k\ge1).
\]

All kernels equal span{e0}. For each n the spectral gap is exactly1/n (attained at every k≥n). Moreover

\[
\|H_n-H\|=\sup_{k\ge1}(1/n-1/k)_+=1/n\to0.
\]

The supremum here need not be attained. The limiting spectrum is {0}∪{1/k:k≥1}; positive spectrum accumulates at0. For Q=I−|e0⟩⟨e0| and every t>0,

\[
\|e^{-tH}Q\|=\sup_{k\ge1}e^{-t/k}=1.
\]

Thus **FALSIFIED:** operator-norm convergence of H_n, a fixed unique vacuum, and merely positive individual gaps imply a positive limiting gap. The missing uniformity is decisive. This is not a counterexample to Section2. It does not say that a vanishing *reported lower bound* proves the true gap vanishes, or that no other method could prove a gap.

## 5. Exact counterexample: a uniform gap does not retain a vacuum

On the same Hilbert space let P_n=|e_n⟩⟨e_n| for n≥1 and H_n=I−P_n. Each H_n has the unique unit vacuum e_n and gap1. For any v∈ℓ², its nth coordinate tends to0, hence P_nv→0. Consequently

\[
H_n\to I\text{ strongly},\qquad
e^{-tH_n}=e^{-t}I+(1-e^{-t})P_n\to e^{-t}I\text{ strongly}.
\]

The uniform bound ||e^{-tH_n}(I−P_n)||=e^{-t} holds exactly. The limiting H=I has no zero-energy vacuum: E_H({0})=0. The normalized e_n converge weakly to0 and have no norm-convergent subsequence. Thus **FALSIFIED:** uniform gap plus strong semigroup convergence alone preserves a nonzero normalized vacuum. Section2 correctly gives P=0 in this example. No actual Yang–Mills model is represented.

## 6. Transfer operators and physical units

Declare a>0 to be a physical Euclidean-time step. Assume a positive, injective, self-adjoint contraction S_a is already represented as e^{-aH_a}, with H_a≥0 self-adjoint, P_a=E_Ha({0}), and Q_a=I−P_a≠0. Set r_a=||S_aQ_a||. Injectivity and Q_a≠0 imply r_a>0; r_a≤1. Spectral calculus gives

\[
\delta_{\rm lat}(a)=-\log r_a,\qquad
\delta_{\rm phys}(a)=\inf\operatorname{spec}(H_a|_{Q_a\mathcal H})
=-\frac{\log r_a}{a}. \tag{7}
\]

For integers j≥1, positivity and the spectral theorem give

\[
\|S_a^jQ_a\|=r_a^j=e^{-ja\,\delta_{\rm phys}(a)}.
\]

A uniform physical lower gap δ therefore means r_a≤e^{-aδ}, equivalently δ_lat(a)≥aδ, throughout all relevant volume/cutoff parameters. Merely δ_lat(a)>0 for each a does not give a positive uniform physical lower bound. For Section4 with a_n=1/n and S_n=e^{-a_nH_n}, one has exactly r_n=e^{-1/n²}, δ_lat=1/n² and δ_phys=1/n→0, with the explicit gapless limiting H.

The vacuum eigenvalue is normalized to1. For another normalization it is the excited/vacuum eigenvalue ratio whose logarithm enters; a raw eigenvalue difference has neither the same normalization nor the required physical units. The assumptions exclude a transfer operator with negative spectrum or an unhandled kernel. No empirical transfer spectrum or lattice-spacing calibration was supplied or computed.

## 7. Adversarial adjudication and next obstruction

| ID | Result | Object and ceiling |
|---|---|---|
|M06-SOURCE-CONTRACT-C094|CERTIFIED_RANGE|The stated inspection extents establish the formal source contract, including finite mass; not full cited axiom proofs or current literature completeness.|
|M06-GAP-TRANSFER-C094|PROVED|Section2 under the exact common-space, self-adjoint, fixed-time, uniform operator hypotheses.|
|M06-PROJECTION-CONVERGENCE-C094|PROVED|Derived strong vacuum-projection convergence and equations(4)–(5).|
|M06-NONUNIFORM-GAPS-C094|FALSIFIED|The precise weaker inference in Section4, by its full exact diagonal family.|
|M06-VACUUM-PERSISTENCE-SHORTCUT-C094|FALSIFIED|The precise nonzero-vacuum shortcut in Section5.|
|M06-TRANSFER-UNITS-C094|PROVED|Equation(7) under its declared positive injective normalized-transfer assumptions.|
|M06-ACTUAL-QFT-BRIDGE-C094|NOT_TESTED|No construction of continuum fields, Hilbert spaces, gauge symmetry, positivity, covariance/locality, ultraviolet behaviour, uniform physical gap or nontriviality for actual Yang–Mills.|

Attacks addressed strong versus norm convergence, moving physical time, nonuniform lower bounds, disappearing vacuum, vanishing excited complement, continuous spectrum, the included δ endpoint, and normalized logarithmic units. H=0 covers the vacuous-gap degeneracy; H=I covers vacuum loss. All examples are exact analytic objects, not sampled finite matrices. No numerical error or completeness-of-grid assertion is involved.

The pivotal reduction has also been checked directly: if P_n already converged strongly, passing K_n−P_n gives(3); spectral measures then give(B). The power argument supplies precisely that previously unnecessary extra hypothesis. These are two derivations within one exposed internal review, sharing the spectral theorem and definitions, not blind reproduction or independent human review. The standard spectral theorem and its bounded functional calculus are imported foundations, not formalized here. No research executable, test suite, interval arithmetic, simulation, or claimed speed improvement was used.

The next discriminating action is M06-CORRELATION-CRITERION-NEXT-C094 (historical local record; not distributed here): determine the precise dense-family positive **temporal** correlation criterion that can replace a full operator norm hypothesis, and expose single-probe or nonuniform-rate failures. It is SELECTED_NOT_TESTED. The source's **spatial** local-field clustering requires its own domain, covariance and density bridge; no converse is inferred here. This changes the missing mechanism rather than repeating gap grids.

Useful transfer: the abstract theorem and both failure modes apply to other nonnegative self-adjoint approximation schemes on identified spaces. Do not repeat the false shortcuts without a new hypothesis. Actual varying-space lattice reconstruction remains a distinct unresolved dependency.

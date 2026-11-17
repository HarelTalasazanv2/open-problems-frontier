# Audited historical reading edition

**Current audited claim:** PROVED: Every ordinary canonical parity minimizer lies in D(A squared) with the displayed uniform bound. The abstract bounded-leakage implication to the full-line second domain is false.

**Claim ceiling:** One compressed iteration only; abstract counterexample remains separate from actual logarithmic regularity.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M01: one justified iteration of the canonical operator domain

Cycle155, 2026-11-09 UTC / 2026-11-08 America/Los_Angeles. Internal analytic result; no claim of novelty, external human review, formal verification, RH positivity, or resolution of RH.

**PROVED (restricted):** for the actual fixed-interval canonical form identified in [080](m01-complete-form-consumer-c080.md), every ordinary complex even or odd unit minimizer belongs to D(A²), with the explicit uniform bound in (12) below. This licenses applying the compressed eigenvalue equation twice. It does not license replacing A² by the compression of M².

**FALSIFIED (abstract inference only):** bounded exterior leakage, a bounded projection commutator, and u∈D(A²) do not in general imply Eu∈D(M²). Section6 gives an exact counterexample. Whether the actual logarithmic operator supplies the missing exterior-domain estimate remains **NOT_TESTED** in this attempt.

## 1. Exact objects and inherited premises

I=(-1,1), H=L²(I;ℂ), and 𝓗=L²(ℝ;ℂ). E is zero extension, R=E* restriction, P=ER, Q=1-P. Norms are unnormalized Lebesgue L² norms; inner products are linear in the first argument. The Fourier convention is f̂(ξ)=∫exp(-ixξ)f(x)dx, with Plancherel factor1/(2π). Let M be the self-adjoint maximal Fourier multiplier m(ξ)=log|ξ|+γ, where γ is Euler's constant. Its domain is {f:m f̂∈L²}.

The nonnegative closed form and its represented self-adjoint operator are

    ell(u)=1/4 ∫∫_(I²) |u(x)-u(y)|²/|x-y| dxdy
            -1/2 ∫_I log(1-x²)|u(x)|² dx,       A=A_ell.

The form domain V is the supported first-log Fourier space. The 084 domain proof (historical local record; not distributed here), lines30–146 directly re-audited here, gives

    D(A)={u∈H:Eu∈D(M)},
    MEu=EAu+K u,     Au=RMEu,                       (1)

where K:H→Q𝓗 is the bounded exterior map

    (Ku)(x)=-1/2 ∫_I u(y)/|x-y| dy, x outside [-1,1],
    ||K||≤κ:=π/2.                                   (2)

No endpoint point values are asserted in (2). The Hilbert transform identity K=-(π/2)sign(x)QHE proves the norm bound. The proof of (1) uses a form core only: test the global finite-part identity against Schwartz functions, pass by form convergence and bounded K, and obtain MEu=EAu+Ku as an L² distribution. The converse follows by the form representation. Thus it does not assume C_c∞(I) is an operator core. We use only the bound in (2), not the later sharpness results of084.

The identities and constants of080 used below are explicit inherited analytic premises, re-read and checked against the primary definitions and named dossier bytes; this is not an external audit of every historical descendant. The two relevant dossier members match their dated manifests; see identity evidence (historical local record; not distributed here).

## 2. H¹(I) embeds in the logarithmic operator domain

For w∈H¹(I), with its ordinary endpoint traces, integration by parts gives

    f̂(ξ)=[w(-1)e^(iξ)-w(1)e^(-iξ)+widehat(Ew')(ξ)]/(iξ),
    f=Ew, ξ≠0.                                      (3)

This follows first for smooth w and then for H¹ by continuous traces, H¹ approximation and L² Fourier convergence. At |ξ|<1, |f̂|≤√2||w|| and

    ∫_(|ξ|<1)(log|ξ|+γ)²dξ=2(2-2γ+γ²)≤4.

The low-frequency contribution to ||Mf||² is at most (4/π)||w||²; the logarithmic singularity at zero is integrable. At |ξ|≥1 use 0<γ<1, |a+b+c|²≤3(|a|²+|b|²+|c|²),

    ∫_1^∞ (1+log r)²/r² dr=5,
    sup_(r≥1)(1+log r)²/r²=1.

The high-frequency contribution is at most

    (15/π)(|w(-1)|²+|w(1)|²)+3||w'||².

Writing w(±1)=w(x)+∫_x^(±1)w', applying Cauchy–Schwarz, and averaging x over I gives

    |w(-1)|²+|w(1)|²≤2||w||²+8||w'||².

Consequently

    ||MEw||²≤(34/π)||w||²+(120/π+3)||w'||²
             ≤12||w||²+43||w'||².                  (4)

The first inequality also proves Ew∈D(M), rather than presupposing it. By (1), w∈D(A) and ||Aw||² satisfies (4). This covers nonzero endpoint traces; imposing H¹_0 would improperly strengthen the claim's hypotheses. All inequalities hold for complex w.

## 3. Projection and compressed translations preserve domains

Schwartz functions are a graph core of M. Indeed smooth compact Fourier data supported away from zero are dense in L²((1+m²)dξ), by truncation away from zero and infinity and smooth approximation on compact annuli. Their inverse transforms are Schwartz. This is a full-line multiplier graph core, not an interval operator-core assertion.

For a Schwartz f, Pf is the zero extension of f|I∈H¹(I), so (4) proves Pf∈D(M) and Qf=f-Pf∈D(M). Formula (1) and self-adjoint duality yield

    [M,P]f=K Rf-EK*Qf=:Jf.                          (5)

For the dual step, test R M Qf against u∈D(A), use (1), and get R M Qf=K*Qf. This dense test domain identifies the vector. In the orthogonal splitting P𝓗⊕Q𝓗, J has blocks [[0,-K*],[K,0]], and therefore ||J||=||K||≤κ. Approximate any f∈D(M) by the full-line graph core. Since P and J are bounded and M is closed, (5) passes to the limit and proves

    P D(M)⊂D(M),    MPf=PMf+Jf.                    (6)

Let τ_hf(x)=f(x+h), for every real h, and T_h=Rτ_hE. Translation is unitary, commutes with M as a Fourier multiplier, and preserves D(M). By (1) and (6), T_h preserves D(A). For u∈D(A), splitting MEu into (1) and applying the dual step gives the exact commutator identity

    [A,T_h]u=Rτ_hKu-K*Qτ_hEu,
    ||[A,T_h]u||≤2κ||u||=π||u||.                   (7)

All operations here are on D(M) or explicitly bounded extensions. There is no translation of an undefined boundary trace. T_h*=T_-h. T_h+T_-h is self-adjoint and commutes with parity, while the individual T_h need not preserve parity. The pair commutator has norm≤2π. For h=0, T_h=1 and the commutator is zero. For |h|≥2, T_h=0 almost everywhere, including equality: endpoints have measure zero. Thus the activation boundary of a prime term is covered exactly.

## 4. The actual canonical perturbation preserves D(A)

Fix any compact parameter interval Kpar=[b,c]⊂(0,∞), allowing b=c. To avoid overloading the exterior map K, denote the remainder integral operator by 𝒦_a. Use exactly080's constants

    R0=2c, κ0=log(2π)+γ,
    M_R=2cosh(R0/2)+1,
    L_R=sinh(R0/2)+(19/48)e^(2R0)+(3/4)e^(4R0),
    S_K=Σ_(2≤n≤exp(2c)) Λ(n)/√n,
    T_K=max(|log b|,|log c|)+|κ0|,
    M_K=T_K+2S_K+2cM_R.

The sum is over integers; Λ is von Mangoldt's function, so non-prime-powers contribute zero. An empty pool has sum zero. The actual real even remainder is

    r''(t)=-2cosh(t/2)+e^(-t/2)/(1-e^(-2t))-1/(2t), t>0,
    r''(0)=-7/4,
    |r''|≤M_R,  Lip(r'' on [-R0,R0])≤L_R.

Its even extension has a cusp at zero. Only Lipschitz regularity is used, never a nonexistent classical derivative there. The operator and perturbation are

    (𝒦_a u)(x)=∫_I a r''(a(x-y))u(y)dy,
    B(a)=-(log a+κ0)1
         -Σ_(2≤n≤exp(2c)) (Λ(n)/√n)(T_(log n/a)+T_(-log n/a))
         -𝒦_a,       q_a ↔ Q_a=A+B(a).              (8)

The exact closed form identity and ||B(a)||≤M_K are080's identified canonical form. Because T_h vanishes for |h|≥2, the fixed prime pool agrees with the moving source pool, including its boundary. No term is differentiated with respect to pool membership.

The Lipschitz kernel has weak x-derivative bounded by c²L_R almost everywhere. Fubini, weak differentiation against compact test functions, and Schur's estimate on the interval of length2 give, for all u∈H,

    ||𝒦_a u||≤2cM_R||u||,
    ||(𝒦_a u)'||≤2c²L_R||u||.

Thus 𝒦_a maps H into H¹(I)⊂D(A), and by (4)

    ||A𝒦_a||≤𝒥_K:=2c sqrt(12M_R²+43c²L_R²).        (9)

Since 𝒦_a is bounded self-adjoint, 𝒦_a A on D(A) is the restriction of (A𝒦_a)*, of norm≤𝒥_K. This follows by pairing against D(A), so is not an unjustified interchange of unbounded factors. Hence ||[A,𝒦_a]||≤2𝒥_K. Equations (7)–(9) now prove

    B(a)D(A)⊂D(A),
    ||[A,B(a)]||≤𝒞_K:=2πS_K+2𝒥_K, uniformly a∈[b,c]. (10)

The scalar term commutes with A. No derivative of the singular multiplier or smoothness of the prime-shift cutoffs was assumed.

## 5. One iteration of the minimizer equation

An ordinary parity minimizer means minimization over the full unit sphere in the even or odd complex parity sector of the common form domain V. It does not impose moment constraints.080 establishes attainment, D(A) membership, and, for every such minimizer,

    Au=(λσ(a)-B(a))u,     -M_K≤λσ(a)≤21/2+M_K.      (11)

Parity invariance of A and B ensures the sector eigen-equation is the full equation; no simplicity, spectral gap, selected eigenvector branch, or real-valued restriction is needed. The even/odd test vectors supply080's same21/2 upper constant. We do not reopen its numerical optimization.

By (10), the right side of (11) belongs to D(A). Therefore u∈D(A²). Applying A on its now-justified domain gives

    A²u=(λσ(a)-B(a))Au-[A,B(a)]u.

For ||u||=1,

    ||A²u||≤(|λσ(a)|+M_K)²+𝒞_K
             ≤(21/2+2M_K)²+𝒞_K.                    (12)

This is a coarse explicit uniform bound on every positive compact parameter interval. More generally any eigenvector of A+B(a) with eigenvalue λ satisfies ||A²u||≤[(|λ|+M_K)²+𝒞_K]||u||. No further iteration is asserted.

## 6. A bounded-leakage shortcut fails in an exact abstract model

Take H0=ℂ and G=ℓ²(ℕ). Let C on G be multiplication by n, with D(C)={x:Σn²|x_n|²<∞}. It is self-adjoint. The vector v=(1/n) belongs to G, since Σ1/n²≤2, but not D(C), because Cv=(1,1,...) is not square summable. Let K0z=zv, a bounded map H0→G. On H0⊕G define

    𝕄=[[0,K0*],[K0,C]],    D(𝕄)=ℂ⊕D(C).

This is self-adjoint by bounded self-adjoint perturbation of diag(0,C). Let E0z=(z,0), and P0 project to H0. Then P0 preserves D(𝕄), [𝕄,P0] is bounded with the same off-diagonal form as (5), and the compression A0=E0*𝕄E0 is zero on all ℂ. In particular 1∈D(A0²). But

    𝕄 E0(1)=(0,v)∉D(𝕄),

so E0(1)∉D(𝕄²). All stated abstract premises hold exactly; no finite approximation, random search, or floating-point summation is involved. This falsifies only the generic implication. The counterexample is not the actual logarithmic multiplier, nor a counterexample to its eigenfunction regularity or to RH.

For the actual objects, (1) makes the remaining gap precise. If u∈D(A²), then EAu∈D(M). Therefore

    Eu∈D(M²)  iff  Ku∈D(M).                         (13)

The right side is additional exterior-domain control; boundedness K:H→Q𝓗 alone does not give it. Equivalently it is membership in the exterior block domain for QMQ. We did not establish that property for the actual minimizers. Thus no fourth Fourier-log moment, inverse-log-fourth tail/modulus, or practical eigenvalue mesh follows from this run.

## 7. Challenges, evidence and review ceiling

| Obligation | Deciding check | Result | Limit |
|---|---|---|---|
| Low-frequency logarithmic singularity | Exact integral preceding (4) | PROVED finite | No uniform multiplier bound near zero asserted |
| Nonzero endpoints | Trace-retaining Fourier integration by parts | PROVED H¹ graph embedding | H¹ is sufficient, not necessary |
| Projection domain | Full-line multiplier graph core and closedness | PROVED (6) | No interval operator core claimed |
| Complex inputs, prime shifts and boundary | Duality, pair adjoint, |h|≥2 case | PROVED (7),(10) | No eigenvalue-branch differentiability |
| Actual remainder cusp | Weak Lipschitz derivative, Schur and (4) | PROVED (9) | No C³ assumption |
| All ordinary parity minimizers | Full represented eigen-equation | PROVED (12) | No constrained/moment minimizers substituted |
| Higher global moment shortcut | Exact self-adjoint block example | FALSIFIED abstract inference | Actual (13) NOT_TESTED |
| Current RH status | Clay owning page says Unsolved | Owner-listed status only | No exhaustive recent-literature or novelty review |

This is one actor/model's analytic derivation and self-challenge, exposed to080/084 and the anticipated outcome. Shared model, mathematical inputs, libraries and expected bounds are explicit. It is neither blind reproduction nor external human review. No numerical scientific instrument ran; native hashes and record validation check custody/consistency, not theorem truth. Numerical precision, simulation and performance comparison are NOT_TESTED / NOT_MEASURED.

The [EMS primary paper](https://ems.press/content/serial-article-files/44477?nt=1), DOI10.4171/LEM/1049, was reacquired byte-identically and physical pages10–13 read in text and images for normalization, prime pairs and closed-form identification. It is a source for the canonical form, not a published proof of (12). The [Clay RH page](https://www.claymath.org/millennium/riemann-hypothesis/) was read only for its current owner-listed status. Exact extents, hashes, parser limits and source lineages are in the inspection register (historical local record; not distributed here).

## 8. Decision and next action

The uncertainty changed from an unjustified second application to a proved compressed-domain iteration. The H¹-to-log graph bound and the bounded-commutator argument transfer to other bounded symmetric Lipschitz kernels and finite paired shifts on this interval. The abstract counterexample prevents promoting bounded leakage into higher global moments without another lemma.

Stop this attempt at D(A²). Next proposal, **unselected pending a fresh comparative contract**: test the actual exterior term Ku∈D(M) for ordinary canonical minimizers, starting from the endpoint kernel and (11), with an explicit norm bound or actual counterexample criterion. This targets the exact missing step in (13); repeating a grid or merely tightening (12) would not decide it. M02's152–154 and M05's149–151 sequences remain closed; other pauses remain. No operational repair was needed.

Detailed run receipt: Cycle155 report (historical local record; not distributed here). Deliverable artifact folder: m01_domain_iteration_cycle155 (historical local record; not distributed here).

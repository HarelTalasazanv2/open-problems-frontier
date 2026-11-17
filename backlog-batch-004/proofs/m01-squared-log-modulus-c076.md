# Audited historical reading edition

**Current audited claim:** PROVED: Every specified compact positive parameter interval has the displayed inverse-log-squared bound for both ordinary complex parity minima.

**Claim ceiling:** Upper modulus only; no sharpness, numerical mesh, positivity or RH.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle 076 — squared-log modulus for actual canonical parity minima

## Verdict and supported statement

**PROVED internally:** for every fixed K=[b,c]⊂(0,∞), both ordinary complex-linear parity lowest canonical eigenvalues satisfy

|λ_σ(a)−λ_σ(a′)|≤C_{K,2}/log²(e/δ), δ=|a−a′|,

for σ∈{+1,−1}, a,a′∈K and0<δ≤min(1/2,b/2). The difference is0atδ=0. The exact constant is

H_K=2(21/2+2M_K)²+π²+2,

C_{K,2}=2G_K+2S_K(4D_K+72)H_K.

All constants below are finite explicit functions of the compact interval. This proves the selected075candidate for the **actual minima**, using their operator equation, rather than only for an arbitrary bounded-energy family. No numerical eigenvalues were computed. The rate is not claimed sharp, Holder, Lipschitz, differentiable, practical for width1/100, novel, externally reviewed or formally verified. No RH or historical Bombieri2003 conclusion follows.

Frozen attempt (historical local record; not distributed here), state/custody reconstruction (historical local record; not distributed here).

## 1. Actual form, constants and inherited inputs

Work on H=L²(I;ℂ),I=(−1,1), with ordinary reflection Ju(x)=u(−x), sectors S_σ=ker(J−σI), zero extension f=Eu and Fourier F(ξ)=∫exp(−iξx)f(x)dx. N=||u||²=(2π)⁻¹∫|F|². Let V and the nonnegative closed form ell be exactly050's fixed-support logarithmic form; A_ell is its associated self-adjoint operator.

The [052 actual canonical decomposition](m01-continuity-modulus-c052.md), using051's identification, is

q_a(u)=ell(u)−(log a+κ)N

−Σ₂≤n≤exp(2c) c_n{C_u(τ_n/a)+C_u(−τ_n/a)}−〈K_a u,u〉,

C_u(h)=∫f(x+h)conj(f(x))dx,

c_n=Λ(n)/√n, τ_n=log n, κ=log(2π)+γ,

K_a(x,y)=a r″(a(x−y)).

Write q_a=ell+〈B(a)u,u〉. The finite pool includes non-prime powers with coefficient0. C_u(h)=0 for|h|≥2, **including equality**, so this fixed-pool formula equals the actual moving cutoff n≤exp(2a). No infinite or changing pool is differentiated.

For R=2c,052 supplies

M_R=2cosh(R/2)+1,

L_R=sinh(R/2)+(19/48)exp(2R)+(3/4)exp(4R),

|r″|≤M_R and |r″(s)−r″(t)|≤L_R|s−t| on[−R,R].

Define

S_K=Σ₂≤n≤exp(2c)Λ(n)/√n,

T_K=max(|log b|,|log c|)+|κ|,

M_K=T_K+2S_K+2cM_R,

D_K=2c/b², G_K=1/b+2(M_R+2cL_R).

The bounds are ||B(a)||≤M_K and

−M_K≤λ_σ(a)≤21/2+M_K.                            (1)

The upper bound uses normalized even/odd polynomial trials with ell≤21/2; nonnegative ell gives the lower bound. Attainment in each nonzero sector follows from the inherited common closed form domain and compact V→L²embedding. The source's [§4.1,4.3–4.5](https://arxiv.org/html/2606.09096v3) was directly reread for compact embedding, attained minimizers, bounded perturbations and parity. Its inspected passage establishes qualitative continuity, not this explicit rate or novelty.

052matches its historical manifest;075's [actual operator-domain theorem](m01-operator-graph-norm-c075.md) matches the preceding COMPLETE manifest. These are inherited internal proof inputs, not a new full independent re-audit. Source scaling/cutoff defects noted in earlier cycles are not reinstated; the actual051/052normalization above governs.

## 2. All sector minimizers satisfy the full operator equation

Reflection preserves V and ell. The scalar term commutes with J; J interchanges the two signed compressed translations, and the real-even r″kernel makes K_a commute with J. Hence B(a) is bounded self-adjoint and commutes with J, and q_a(Ju,Jv)=q_a(u,v).

Take any normalized minimizer u∈V∩S_σ. Differentiating its Rayleigh quotient in the real directions v and iv, for v∈V∩S_σ, gives

q_a(u,v)=λ_σ(a)〈u,v〉.

For v in the opposite sector, reflection invariance gives q_a(u,v)=−q_a(u,v)=0, and also〈u,v〉=0. Every v∈V decomposes into its two parity components because the parity projections preserve V. Therefore the displayed identity holds for **all** v∈V, not just sector test vectors.

Consequently ell(u,v)=〈λ_σ(a)u−B(a)u,v〉 for all v∈V. The closed-form representation theorem implies u∈D(A_ell) and

A_ell u=(λ_σ(a)−B(a))u.                           (2)

This argument neither assumes a simple eigenvalue nor chooses a continuous eigenvector. From(1), |λ_σ(a)|≤21/2+M_K, so every normalized sector minimizer satisfies

||A_ell u||≤21/2+2M_K.

Applying075's W₂(u)≤2||A_ell u||²+(π²+2)||u||² yields

W₂(u):=(2π)⁻¹∫(1+log⁺|ξ|)²|F(ξ)|²dξ≤H_K.        (3)

The uniform bound covers every minimizer choice and both parities. Form energy alone would not license it; the full equation(2) is essential.

## 3. Exact complex autocorrelation estimate on a W₂ball

For any u with finite W₂, Fourier inversion of its autocorrelation gives

C_u(h)=(2π)⁻¹∫exp(iξh)|F(ξ)|²dξ.

The integral is absolutely convergent by Plancherel. Let |h−k|≤Dδ, D≥0,0<δ≤1/2, t=log(1/δ)>0 and U=δ⁻¹/². On|ξ|≤U, use |exp(iξh)−exp(iξk)|≤|ξ||h−k|. On|ξ|>U use the bound2and the squared-log weight. This proves

|C_u(h)−C_u(k)|≤D√δ N+2W₂(u)/(1+t/2)²

≤D√δ N+8W₂(u)/t².                                (4)

There is no operator-norm continuity claim for full-L²translations.

Set L=log(e/δ)=1+t. For every t≥log2 the following exact inequalities hold:

√δ L²≤4, δL²≤2, L/t≤3.                           (5)

For the first, the maximum of (1+t)²exp(−t/2) over t≥0 occurs at t=3 and equals16exp(−3/2)<4: the positive exponential series gives exp3>131/8>16. For the second, (1+t)²exp(−t) has maximum4/e<2 at t=1, since e>2. For the third, log2=∫₁²dx/x≥1/2, hence1+1/t≤3. These bounds include δ=1/2, not only an asymptotic regime.

Since N≤W₂(u), multiplying(4) by L² and using(5) gives

|C_u(h)−C_u(k)|≤(4D+72)W₂(u)/log²(e/δ).            (6)

This works for complex u, arbitrary real h,k of the specified separation, both signed shifts and correlations crossing the support boundary. No low-frequency singularity is introduced: the target moment weight is1nearξ=0.

## 4. Prime thresholds, remainder and both Rayleigh directions

For every member of the fixed finite prime pool,

|τ_n/a−τ_n/a′|=τ_nδ/(aa′)≤(2c/b²)δ=D_Kδ.

The same holds for the negative shifts. Because C vanishes at and beyond|h|=2, (6) controls the activated, inactive and equality cases without an omitted threshold or membership jump. Each pair contributes at most2c_n(4D_K+72)W₂/L².

The scalar term changes by at mostδ/b. For z=x−y∈[−2,2],

|a r″(az)−a′r″(a′z)|≤δ(M_R+2cL_R).

Retaining the row/column length2in Schur's bound gives

||K_a−K_a′||≤2δ(M_R+2cL_R).

Thus for any unit vector u with W₂(u)≤H_K,

|q_a(u)−q_a′(u)|≤G_Kδ+2S_K(4D_K+72)H_K/L²

≤[2G_K+2S_K(4D_K+72)H_K]/L²=C_{K,2}/L²,           (7)

using δL²≤2from(5).

For any normalized minimizer u of q_a in sectorσ, (3) makes it eligible for(7), and it belongs to the common V. Therefore

λ_σ(a′)≤q_a′(u)≤λ_σ(a)+C_{K,2}/L².

Interchange a,a′ and choose any minimizer there to obtain the opposite inequality. This proves the stated absolute bound. Atδ=0the difference is0; its bound extends continuously to0. No uniform assertion at b=0or c=∞is licensed. If b=c, the positive-δrange is empty and the zero case still holds. The unrestricted canonical minimum min(λ_+,λ_−) inherits the same estimate by the elementary minimum inequality; no historical-form identification is added.

## 5. Adversarial checks and claim limits

1. **Sector-only stationarity:** opposite-parity tests vanish by explicit reflection invariance, so the full operator equation is actually obtained. No stronger domain assumption is silently inserted.
2. **Multiplicity:** (2)–(3)apply to every minimizing unit vector, without spectral gap, simple eigenvalue or continuous eigenvector selection.
3. **Complex phases:** modulus bounds handle complex correlations; both signed terms remain. No replacement by one real correlation or an antilinear parity sector.
4. **Prime interfaces:** the fixed pool and C(±2)=0cover both sides and equality of every threshold; no numerical tolerance is used.
5. **Parameter interfaces:** δ=0handled separately, δ=1/2covered by(5), a=b,cand b=cvalid; b>0prevents reciprocal singularities.
6. **Translation shortcut:** on unrestricted L²the norm of T_h−Iis2for h≠0, by its Fourier multiplier's essential supremum. The moment expectation in(6), not that false norm-continuity shortcut, supplies the estimate.
7. **Energy-versus-graph scope:**053's bounded-energy lower family cannot refute(3), which uses the eigen-equation and bounded operator graph norm. No actual-eigenvalue sharpness claim follows from that generic family.
8. **Constants and tail:** the tail is controlled over the entire|ξ|>δ⁻¹/²region by W₂; exact scalar maxima justify4,72and2without sampled checks. Infinite frequencies and low frequencies are both covered.

No failed mathematical control or repair to the proposed constants was needed. This is a complete analytic argument composed with named inherited internal proofs, not numerical certificate execution, blind reproduction, external human review or formal verification. Shared actor/model, source, prior results and expected constants remain exposure limits. Efficiency NOT_MEASURED.

## 6. Usefulness, feasibility and next decision

Uncertainty changed:075operator-domain information now controls the **actual** canonical minima's modulus. The previous inverse-log estimate remains true; this sharper asymptotic upper-rate bound does not identify a sharp rate, Holder/Lipschitz behavior, a derivative, sign or spectral value. No percentage of RH progress is meaningful here.

The constants are deliberately loose. To make this bound alone≤ε, a sufficient spacing is δ≤exp(1−√(C_{K,2}/ε)), within the theorem's parameter range. At K=[1,2], R=4and L_R≥(3/4)exp16, so G_K>6exp16and C_{K,2}>12exp16. Merely meeting the printed criterion C_{K,2}/log²(e/δ)≤1/100 therefore requires δ<exp(1−20√3 exp8). This concerns that sufficient bound, not necessary spacing for the actual eigenvalues. A practical mesh or width1/100certificate is not established, and no implemented speedup is claimed. No grid/head computation is allocated.

Do not automatically iterate higher-log-moment proofs. The next prioritized action is a bounded exact covering-family source gate (historical local record; not distributed here), prompted by the new corpus inspection. It must identify actual family membership and forest witness dependencies before independent finite verification. The corpus note's PROVED_LOCAL label and arithmetic consistency are not its certificate. The general Erdős203statement/current status remains unverified after two failed owning-site access routes; no new globally open catalog entry is promoted.

## Authority

Public read-only primary inspection, one inert donor Markdown read and local OPF writes only. No donor program/data certificate executed, donor mutation, agents/threads, messages/uploads/publication/reviewer contact, installs, accounts or application/schedule/notification changes. No unmanaged continuation.

# Audited historical reading edition

**Current audited claim:** PROVED: The explicitly defined even remainder r is globally C2, has r_second(0)=-7/4 and the displayed smooth punctured second derivative; its compact rescaled kernels are norm continuous.

**Claim ceiling:** For the exact displayed g/prime decomposition and named digamma identity; no historical form or positivity result.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle048 — exact global remainder and compact kernel bounds

**Verdict: PROVED internally at the stated source-defined scope; PASS AT CLAIM CEILING.** For the exact real function g in Suzuki arXiv:2606.09096v3(1.3), subtract its identical prime term and the specified logarithmic/linear singular part. The resulting r is real, even and C² on all of R, with r(0)=r′(0)=0 and r″(0)=−7/4. We derive its global second derivative, an explicit bound on every compact interval, and operator-norm continuity of the scaled remainder kernels on complex L²(−1,1). This is a dependency derivation of a formula already displayed in the source, not a claim of a new special-function theorem, canonical/historical form identification, RH, novelty or external review.

Attempt frozen before the derivation (historical local record; not distributed here), 2026-10-22T01:38:28.621097 UTC. The 047 conditional parity argument (historical local record; not distributed here) remains conditional on the other named source inputs. Its historical report is unchanged.

## 1. Definitions and source inputs

All logs are real natural logs. Write γ for Euler's constant, β=1/4, and A=(log(2π)+γ−1)/2. For every t∈R set

- P(t)=−4(exp(t/2)+exp(−t/2)−2).
- g₀(t)=Σ_{2≤n≤exp|t|} Λ(n)n^(−1/2)(|t|−log n), with Λ the von Mangoldt function. The sum is locally finite and empty near zero.
- F(t)=exp(−|t|/2) Φ(exp(−2|t|),2,β), including F(0)=Σ_{k≥0}(k+β)^(−2).
- g(t)=P(t)+g₀(t)−(|t|/2)(ψ(β)−log π)−(F(0)−F(t))/4.
- r(t)=g(t)−g₀(t)−|t|log|t|/2−A|t|, with |t|log|t|=0 at zero.

The definition is [Suzuki v3(1.3)](https://arxiv.org/html/2606.09096v3#S1.E3); §§2.2/2.4 contain the near-zero series and the candidate derivative. The current [arXiv record](https://arxiv.org/abs/2606.09096) still lists v3 dated September23,2026, checked October22 UTC. We do not use a local zeta power series outside its convergence range. The exact global Lerch series comes from [NIST DLMF25.14.1](https://dlmf.nist.gov/25.14.E1), valid for our positive β and |z|<1 (and z=1,s=2). The only non-elementary constant identity used below is [DLMF5.9.16](https://dlmf.nist.gov/5.9.E16), for Re z>0:

ψ(z)+γ=∫₀∞ (exp(−u)−exp(−zu))/(1−exp(−u)) du.

These source definitions/standard identities are named analytic inputs, not automatically audited external papers. The derivation of r and all interchanges/bounds used here are checked below. Capture receipts (historical local record; not distributed here) bind the exact inert HTML bytes. Only selected formula/status extents were read. Source and DLMF HTML were inspected directly; this cycle makes no new PDF-layout claim.

## 2. Global differentiation away from zero

For t>0 the exact series is

F(t)=Σ_{k=0}∞ exp(−2t(k+β))/(k+β)².

On any ε≤t≤R with ε>0 and R<∞, the series and its first two derivative series converge uniformly: derivative terms have absolute bounds, respectively, exp(−2ε(k+β))/(k+β)², 2exp(−2ε(k+β))/(k+β), and 4exp(−2ε(k+β)). Each bound is summable (the last is geometric). Thus termwise twice differentiation is valid on every such interval; their union is (0,∞). Summing the geometric series gives

F″(t)/4=exp(−t/2)/(1−exp(−2t)).

Cancel g₀ exactly in the definition before differentiating. Since P″(t)=−exp(t/2)−exp(−t/2), the resulting r on (0,∞) satisfies

R(t):=r″(t)=−exp(t/2)−exp(−t/2)+H(t),

H(t)=exp(−t/2)/(1−exp(−2t))−1/(2t).

Everything remaining is real and depends on |t| except the already even P, so the same formula with |t| in H holds for t<0. No theorem about a Bernoulli generating series at large t is invoked. The second derivative alone does not establish C² across zero: a hidden multiple of |t| would have the same punctured second derivative. We resolve that constant next.

## 3. Matching the first derivative at zero

For s>0 let

Sβ(s)=Σ_{k≥0} exp(−s(k+β))/(k+β)=∫_s∞ exp(−βu)/(1−exp(−u))du.

The integral identity follows term by term by Tonelli, as every summand is nonnegative. Also S₁(s)=−log(1−exp(−s)), obtained by elementary integration. DLMF5.9.16 yields

Sβ(s)−S₁(s)=−γ−ψ(β)−∫₀ˢ Dβ(u)du,

Dβ(u)=(exp(−βu)−exp(−u))/(1−exp(−u)).

Dβ has a finite right limit 1−β at zero. Its integrability at infinity follows from β>0. These facts justify subtracting the convergent improper integrals; no difference of divergent integrals is taken. In particular

Sβ(s)=−log s−γ−ψ(β)+E(s),

E(s)=−log((1−exp(−s))/s)−∫₀ˢ Dβ(u)du.

A controlled bound makes the limiting step explicit. For 0<s≤1, exp(−s)≤(1−exp(−s))/s≤1, hence the absolute value of the first term of E is ≤s. By the mean value theorem in the exponent, 0≤exp(−βu)−exp(−u)≤(1−β)u, whereas 1−exp(−u)≥u exp(−1) for 0<u≤1. Consequently |E(s)|≤[1+e(1−β)]s. This proves E(s)→0 without relying on a numerical asymptotic.

From the already justified derivative series F′(t)=−2Sβ(2t). For t>0,

r′(t)=P′(t)−(ψ(β)−log π)/2−Sβ(2t)/2−(log t+1)/2−A
      =P′(t)−E(2t)/2.

The constants cancel because A=(log(2π)+γ−1)/2. Since P′(0)=0, r′(t)→0 as t↓0, with an O(t) bound for 0<t≤1/2. At zero, dominated convergence in the defining F series gives F(t)→F(0), because Σ(k+β)^(−2)<∞. Thus r(t)→0=r(0). This directly checks both integration constants. Reality and evenness follow from the exact definition, not from a choice of integration constants after the fact.

## 4. Controlled second-derivative limit and the even extension

For t>0 put h(t)=(1−exp(−2t))/(2t)=∫₀¹exp(−2tu)du. Then

H(t)=[exp(−t/2)−h(t)]/[2t h(t)].

For 0<t≤1/2, Taylor's theorem with the exponential derivative bounded on nonnegative arguments gives

h(t)=1−t+E_h(t), |E_h(t)|≤(2/3)t²,
exp(−t/2)=1−t/2+E_e(t), |E_e(t)|≤t²/8.

Moreover h(t)≥e^(−1) and |1−h(t)|≤t. Therefore

|H(t)−1/4|≤e t/4+(19e/48)t=(31e/48)t.

In particular H extends continuously with H(0)=1/4. Also

|P″(t)+2|=2(cosh(t/2)−1)≤e^(1/4)t²/4,

so |R(t)+7/4|≤(31e/48)t+e^(1/4)t²/4 on 0<t≤1/2. This is a controlled remainder with explicit domain and constants, not high-precision evidence. Define R(0)=−7/4 and R(−t)=R(t). The positive-axis formula now defines a continuous even R on R.

Since r′(t)→0 and R is bounded near zero, integrate r″=R from δ to t and let δ↓0. Then r′(t)=∫₀ᵗR(s)ds for t>0. Similarly r(t)=∫₀ᵗ(t−s)R(s)ds. Evenness extends these identities to the negative side in the usual oriented-integral sense. They give r′(0)=0 and r″(0)=lim_{t→0}r′(t)/t=R(0). Thus r∈C²(R), including zero. In particular r(t)=−(7/8)t²+O(|t|³) locally, as a consequence, not a substitute for matching r′.

## 5. All prime-power interfaces

The exact g₀ term is subtracted identically at every real t. Near any t₀=log n>0 with n a prime power, its kth relevant summand is c_n(t−t₀)_+, c_n=Λ(n)/sqrt(n). The source g contains precisely that summand, so the derivative jump c_n cancels in g−g₀. At −t₀ both functions again contain the identical even kink. Non-prime-powers have zero coefficient; n=1 contributes zero and creates no origin term. Local finiteness prevents an accumulation on any finite interval. The remaining closed expression is smooth on either open half-line and C² through zero by §§3–4. Thus no threshold was excluded by a tolerance. Distributionally the same prime delta masses cancel as well, although no full distributional formula for g″ at zero is claimed in this cycle.

## 6. Explicit compact bounds and kernels

For x>0, elementary strict inequalities 1−exp(−x)<x and exp(x)−1>x imply

0<1/(1−exp(−x))−1/x<1.

Decompose H(t), for t>0, as

exp(−t/2)[1/(1−exp(−2t))−1/(2t)] + [exp(−t/2)−1]/(2t).

The first term is between0 and1. The second is between−1/4 and0 by 0≤1−exp(−t/2)≤t/2. Hence −1/4≤H(t)≤1 and |H(t)|≤1 globally, including its continuous value at0. For every R₀≥0,

sup_{|t|≤R₀}|r″(t)|≤2cosh(R₀/2)+1.

This is a valid, deliberately loose bound, not an optimal estimate or a bound independent of R₀.

Let Hspace=L²((−1,1);C), Jw(x)=w(−x), and for a>0 define

(K_aw)(x)=∫_{−1}¹ k_a(x,y)w(y)dy,
k_a(x,y)=a r″(a(x−y)).

For every [b,c]⊂(0,∞), |k_a(x,y)|≤c[2cosh(c)+1] on the full closed square and all a∈[b,c]. Each row and column absolute integral is at most2c[2cosh(c)+1]. Schur's test therefore gives

sup_{a∈[b,c]}||K_a||≤2c[2cosh(c)+1].

The kernel is real symmetric because r″ is real even, so K_a is self-adjoint on the complex Hilbert space; simultaneous reflection of x,y leaves it unchanged, so it commutes with J. Continuity of (a,x,y)↦a r″(a(x−y)) on the compact product implies uniform kernel continuity. Accordingly

||K_a−K_d||≤2 sup_{|z|≤2}|a r″(az)−d r″(dz)|→0 as a→d>0.

This is operator-norm continuity for the smooth remainder kernels only. It does not assert operator-norm continuity of the prime-translation terms (which use strong continuity in047). The coefficient a and interval length2 are both retained.

## 7. Adversarial assessment

| Obligation/attack | Exact check | Adjudication and limit |
|---|---|---|
| Global versus local convergence | M-test on every [ε,R] for the exact exponential Lerch series and two derivatives | PASS; no zeta-series continuation assumed |
| Hidden \|t\| cusp | Replace A by A+δ, δ≠0; punctured r″ is unchanged but new remainder r−δ\|t\| has right derivative −δ and left derivative +δ | Bad normalization is detected; punctured formula alone is insufficient |
| Wrong singular subtraction | Replace the coefficient1/2 of \|t\|log\|t\| by d≠1/2; residual (1/2−d)/t occurs in r″ on t>0 | No continuous origin extension; exact coefficient required |
| Prime membership/coefficient | Remove c_m(\|t\|−log m)_+ for one prime power from the subtraction while retaining source g | Derivative jump c_m survives; cancellation covers all locally finite terms, not just sampled primes |
| Zero and both sides | Derivative constant via digamma integral, explicit H Taylor bound, even extension | r(0)=r′(0)=0, r″(0)=−7/4; full real domain covered |
| Polar sign and large t | P″ exactly −2cosh(t/2); H bounded, so r″(t)→−∞ | Omitting polar term cannot reproduce exact source remainder; compact bound cannot become whole-line uniform bound |
| Kernel normalization | Keep prefactor a and both row/column lengths2; evaluate diagonal k_a(x,x)=−7a/4 | Rescaling without a is a different operator; bound proof uses actual convention |
| Claim boundary | Remainder alone supplies neither finite-part quadratic identity nor canonical/historical domain matching | Parent canonical parity remains CONDITIONALLY_PROVED; historical bridge HOLD and RH OPEN |

These are eight analytic attack items, not a software pass count or experimental sampling. No failed mathematical control or repaired deciding instrument occurred. Same agent/model/platform and exposure to source/expected expression are shared; this is an independent derivation from the globally convergent defining series versus the source's local generating-series route, not blind reproduction, human review or formal verification. Numerical instrument NOT_USED; efficiency NOT_MEASURED.

## 8. Dependency ledger and next obstruction

| Claim | Outcome | Evidence / remaining input |
|---|---|---|
| Exact source-defined global remainder and compact scaled kernels | PROVED internally | §§1–6, named standard Lerch/digamma inputs; no external review |
|047 abstract parity compactness implication | PROVED internally, inherited ARTIFACT_VERIFIED | Old proof unchanged; not rerun or strengthened |
|047 canonical application | CONDITIONALLY_PROVED | Global remainder regularity now discharged; full quadratic decomposition, logarithmic closure/core estimate and canonical/Friedrichs identification remain named |
| Historical Bombieri2003 form values/sector infima | INCONCLUSIVE/HOLD; source gate BLOCKED | No original text obtained or new retrieval attempted048 |
| RH | OPEN | [Clay owning-status page](https://www.claymath.org/millennium/riemann-hypothesis/) Unsolved checked October22 UTC; bounded source check |

The next exact obligation is to derive the localized quadratic decomposition corresponding to source(2.5) directly from D*G_aD, using this now-global r, with the zero singularity, delta terms at prime thresholds, constants and complex conjugation fixed. This differs from020's multiplicative/additive smooth-core change of variables and023's finite-value domain comparison. Do not repeat those proved steps or infer that023 identified every historical extension. A finite-part/distributional integration-by-parts proof or a precise mismatch would decide a still-named canonical input. The source's printed scaling defect from047 remains preserved and is not silently repaired here. Next packet (historical local record; not distributed here).

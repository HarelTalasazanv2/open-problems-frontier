# Audited historical reading edition

**Current audited claim:** PROVED: The stated nonnegative interval form is closed on supported first-log Fourier space, has smooth interior form core, and equals the supported pure-log Fourier expression.

**Claim ceiling:** No zero boundary traces on the completed domain; pure-log identity relies on interval support.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle050 — logarithmic form completion, smooth core and exact normalization

**PROVED internally; PASS AT CLAIM CEILING.** On I=(−1,1), the explicit nonnegative logarithmic form ell₀=L₁ initially on complex H₀¹(I) is closable. Its closure has exactly the zero-extension logarithmic Fourier domain V defined below. Both C_c^∞(I) and H₀¹(I) are form cores. We prove the exact shifted positive-weight identity, norm equivalence, support-preserving form-density argument, reflection invariance and the source's pure-log formula(4.6) on this closure. This reproduces known functional-analytic ingredients at the exact project normalization; it is not claimed novel.

The attempt (historical local record; not distributed here) was frozen2026-10-22T09:37:15.271721UTC before deciding the proof. The [049 quadratic identity](m01-quadratic-decomposition-c049.md) and 047 abstract parity lemma (historical local record; not distributed here) are inherited ARTIFACT_VERIFIED, not rerun. The canonical/Friedrichs identification remains a named separate input; canonical parity stays CONDITIONALLY_PROVED. No historical Bombieri2003 identification, RH, novelty, outside human/formal review or measured efficiency claim.

## 1. Definitions and strongest supported statement

For a complex v∈L²(I), write f for its zero extension and

F(ξ)=∫_R exp(−iξx)f(x)dx, N=||v||₂²=(2π)^(−1)∫|F|².

Compact support implies f∈L¹ and |F(ξ)|≤sqrt(2)||v||₂. Set w(ξ)=1+log⁺|ξ| and

V={v∈L²(I): W(v):=(2π)^(−1)∫w(ξ)|F(ξ)|²dξ<∞}.

Define the nonnegative physical quantities, possibly infinite,

R(v)=∬_{I²}|v(x)−v(y)|²/|x−y| dxdy,
B(v)=−∫_I log(1−x²)|v(x)|²dx,
ell(v)=R(v)/4+B(v)/2.

The last expression is ell₀ on H₀¹(I). Our theorem identifies its closed extension and completion; a finite-value set equality alone would not establish a core or an injective completion map. There is no imposed boundary trace in V. The Fourier convention and prefactor1/(2π) are fixed throughout.

For r≥0 define J(r)=∫₀ʳ(1−cos u)du/u, J(0)=0. The exact positive norm identity to prove is

E(v):=ell(v)+(1+log2)N
     =(2π)^(−1)∫[1+J(2|ξ|)]|F(ξ)|²dξ.                  (E)

For every v∈V we also prove

ell(v)=(2π)^(−1)∫(log|ξ|+γ)|F(ξ)|²dξ,                 (L)

where γ is Euler's constant. The negative part at zero is integrable because F is bounded; the positive-frequency part is integrable by V. Formula(L) is an equality of quadratic forms on a fixed-support space. The multipliers in(E) and(L) are not equal pointwise.

## 2. Exact translation energy and a positive norm

Let T_hf(x)=f(x+h) and

T₂(v)=∫_{|h|<2}||T_hf−f||₂² dh/|h|.

Tonelli applies to its nonnegative integrand. Splitting ordered pairs into both points inside I and crossings from I to its complement gives, for every complex L² vector in the extended-value sense,

T₂=R+2∫_I|v(x)|²[log(2/(1+x))+log(2/(1−x))]dx
  =R+4log2 N+2B.

Each crossing direction is counted twice; missing that orientation factor would give the wrong shift. All logarithms in the crossing expression are nonnegative, so this argument does not subtract two infinite quantities. Consequently

ell+log2 N=T₂/4, and E=N+T₂/4.                        (T)

For each h, Plancherel gives ||T_hf−f||²=(2π)^(−1)∫2(1−cos(hξ))|F|². Tonelli again yields T₂=(2π)^(−1)∫4J(2|ξ|)|F|², proving(E), including infinity cases.

Here is an explicit, nonoptimal equivalence bound valid for all real ξ:

(1/7)w(ξ)≤1+J(2|ξ|)≤6w(ξ).                          (W)

Indeed J≥0; for0≤r≤1, J(r)≤r²/4. For r≥1,

J(r)=J(1)+log r−∫₁ʳ cos u du/u,

and integration by parts bounds the last integral in absolute value by3. Thus J(r)≤1/4+log r+3. Substitution r=2|ξ| and log2<1 proves the upper bound6w. For r≤e⁶, w(ξ)≤7 and 1+J≥1. For r>e⁶, J(r)≥log r−3≥(1/2)log r, while w(ξ)≤1+log r≤(7/6)log r; this gives the lower bound1/7. No numerical fitting or asymptotic-only estimate is used.

It follows that the finite ell domain is exactly V. Moreover

ell+N≤E≤(1+log2)(ell+N),

because ell≥0. Together with(W), this proves equivalence of the original shifted form norm, E^(1/2), and the stated logarithmic Fourier norm.

## 3. Closedness and the completion map

The full-line space of Fourier transforms with ∫w|F|²<∞ is Hilbert, by weighted L² completeness and Plancherel. The condition that its inverse transform vanish a.e. outside [−1,1] defines a closed subspace: convergence in that norm implies L² convergence since w≥1, and fixed support is an L²-closed condition. Thus V is complete in W^(1/2), hence in E^(1/2), hence in (ell+N)^(1/2).

Therefore ell is a nonnegative closed form on its domain V. The continuous embedding into L² is injective: its norm controls ||v||₂, so the completion cannot acquire an extra vector mapping to zero. To show that this is the closure of the restriction ell₀ to H₀¹ rather than merely a closed extension, we must prove form density. That is a separate step, not a consequence of L² density.

## 4. Form-core density with support retained

For ρ>0 define the unitary physical dilation

(U_ρf)(x)=ρ^(−1/2)f(x/ρ), with Fourier transform sqrt(ρ)F(ρξ).

For1/2≤ρ≤2, change variables ζ=ρξ to obtain

∫w(ξ)|sqrt(ρ)F(ρξ)|²dξ=∫w(ζ/ρ)|F(ζ)|²dζ
 ≤(1+log2)∫w(ζ)|F(ζ)|²dζ.

The dilation operators are therefore uniformly bounded nearρ=1 in the full-line logarithmic norm. They are strongly continuous there: smooth compactly supported functions in the **frequency** variable are dense in weighted L², and on these functions the scaled amplitudes converge uniformly on a common compact set. This density uses only a locally bounded positive weight, not the physical support/core statement we are proving. The uniform operator bound then extends continuity to all weighted L² transforms.

For v∈V and0<ρ<1, f_ρ=U_ρf is supported in [−ρ,ρ] and f_ρ→f in logarithmic norm asρ↑1. Take a nonnegative even η∈C_c^∞(−1,1) with integral1 and let η_δ(x)=δ^(−1)η(x/δ). Then

f_{ρ,δ}=η_δ*f_ρ∈C_c^∞(I) whenever0<δ<1−ρ.

Its support is contained in [−ρ−δ,ρ+δ]. For fixedρ, its Fourier transform is ηhat(δξ)sqrt(ρ)F(ρξ); |ηhat|≤1 and ηhat(δξ)→1. Dominated convergence against w(ξ)|sqrt(ρ)F(ρξ)|² gives f_{ρ,δ}→f_ρ in logarithmic norm asδ↓0.

Chooseρ_n↑1, then chooseδ_n< (1−ρ_n)/2 sufficiently small that the mollification error in that norm is<1/n. The triangle inequality gives f_{ρ_n,δ_n}→f in logarithmic norm and therefore in the ell form norm by(W). This sequential choice avoids an unjustified uniform dominated-convergence assertion for a coupledρ,δ limit.

Thus C_c^∞(I) is a form core for ell. H₀¹(I)⊂V by the explicit H¹ bounds in049, and C_c^∞⊂H₀¹, so H₀¹ is also a form core. Its restriction ell₀ is closable and its closure is exactly ell with domain V. The theorem is about completion/density, beyond merely identifying a finite-value set.

Reflection Jv(x)=v(−x) is complex-linear and preserves physical support and both energies. It is an involutive isometry of L² and of the form norm. Dilation and the even mollifier commute with it, so the above approximation preserves even or odd parity whenever the input has that parity. Equivalently P_±=(I±J)/2 are continuous form-norm projections and their images of the smooth core are dense in their respective closed sectors. No antilinear star is substituted.

## 5. Exact pure-log formula: a support-specific tail cancellation

Norm equivalence does not by itself prove(L). Use the standard positive-real identities from [NIST DLMF6.2.11–6.2.13](https://dlmf.nist.gov/6.2):

Ci(r)=−∫ᵣ∞cos u du/u=γ+log r−J(r), r>0.

Integration by parts gives |Ci(r)|≤2/r. For0<r≤1, the displayed identity and J(r)≤1/4 give |Ci(r)|≤|γ|+|log r|+1/4. These bounds justify all subsequent integrals.

Write C(h)=∫f(x+h)conjugate(f(x))dx. For every L² vector supported in I, C(h)=0 for h≥2. Also (2π)^(−1)∫cos(hξ)|F(ξ)|²dξ=Re C(h), by Plancherel. For finite R≥2, Fubini is valid on the finite h interval because |F|²∈L¹ and ∫₂ᴿdh/h<∞. Therefore

(2π)^(−1)∫[Ci(R|ξ|)−Ci(2|ξ|)]|F(ξ)|²dξ
 =∫₂ᴿ Re C(h)dh/h=0.                              (C)

Each Ci integral is absolutely integrable separately: bounded F controls its logarithmic origin singularity, and |Ci(r)|≤2/r controls its tail. To pass R→∞, let M=||F||∞²≤2N. On |ξ|<1/R the absolute integral of Ci(R|ξ|)|F|² is at most 2M(|γ|+5/4)/R. On1/R≤|ξ|≤1 it is at most4M log R/R; on |ξ|>1 it is at most (2/R)∫|F|². All tend to zero. Hence(C) yields

∫Ci(2|ξ|)|F(ξ)|²dξ=0                              (S)

for every L² vector with this fixed support, without requiring pointwise cancellation of Ci. On V, the J and log weighted integrals are finite, and (T),(E),(S) give

ell=(2π)^(−1)∫[J(2|ξ|)−log2]|F|²
   =(2π)^(−1)∫(log|ξ|+γ)|F|²,

which is precisely(L), the source(4.6), now justified on the full closure. This proof does not exchange a conditionally convergent infinite h integral with a frequency integral: it truncates first and provides an explicit limit bound. The support restriction is essential. The multipliers J(2|ξ|)−log2 and log|ξ|+γ remain different pointwise.

## 6. Controls, exclusion and scope

| Attack | Exact check | Result/limit |
|---|---|---|
| Missing translation factor or shift | For v=1 on I,N=2,R=0,B=4−4log2,ell=2−2log2,T₂=8,E=4 | Exact constants match;the constant has nonzero boundary values yet belongs to V |
| False all-L² domain | Let d=1−x near the right endpoint and v=d^(−1/2)/log(e/d),with support in0<d<1/4 | N finite but B infinite,so v∉V by(T)/(W) |
| L² density confused with form density | Weighted dilation continuity and dominated mollification convergence are proved explicitly | Completion is identified by an actual core construction |
| Support leak | Naively mollifying1_I leaks outside I;contract first and requireδ<1−ρ | Every final approximant has strict interior compact support |
| Wrong dilation normalization | Fourier amplitude sqrt(ρ),notρ or1;the weighted change of variables above fixes it | Uniform norm bound supports the density proof |
| Pointwise multiplier shortcut | Ci(2|ξ|) is not identically zero;only its quadratic integral cancels by support | Norm equivalence and exact(L) are separate obligations,each proved |
| Complex parity | Linear reflection and even mollifiers commute with dilation;phases preserve modulus squares | Both complex parity sectors have form cores;no antilinear identification |
| Canonical/historical promotion | Closure of this explicit form does not alone identify the externally defined Weil closed form or2003extension | Canonical application conditional on its final identification;historical bridge HOLD |

For the exclusion control, ∫₀^(1/4)dd/[d log²(e/d)]<∞. Since −log(1−x²)=−log(d(2−d)) grows like log(1/d), its B integral dominates a positive multiple of ∫₀^δdd/[d log(e/d)]=∞. The interval cutoff only adds a possible interior jump and cannot remove this nonnegative endpoint divergence. This is an exact L² witness, not a guessed Fourier tail.

There are eight analytic attack items; no deciding numerical instrument, floating-point tolerance or failed primary mathematical control. The two equivalent positive-energy formulas and the separate Ci cancellation cross-check constants by different reductions. The same agent/model/platform, source target and prior-record exposure are shared; this is not blind reproduction, human review or formal verification. Efficiency NOT_MEASURED.

## 7. Primary-source context and what changed

[Suzuki v3(4.6)](https://arxiv.org/html/2606.09096v3) states the log multiplier and norm equivalence;the source passage describes the completion as a subspace of Hlog. The present derivation verifies the full exact completion/core map at the project's normalization. Latest arXiv version remains v3September23,checked2026-10-22. [Clay](https://www.claymath.org/millennium/riemann-hypothesis/) still labels RHUnsolved on a bounded owning-status check.

This is known functional analysis. [Chen–Weth v6, Proposition4.2 and Remark4.3](https://arxiv.org/pdf/1710.03416v6) already provide smooth density in the regional space on bounded Lipschitz domains and its zero-extension isomorphism with the full truncated-energy space. Their functions are real; our complex argument uses modulus squares throughout,or splits real/imaginary parts. The prior024record already identified this prior art. Current direct text and visual inspection locates Proposition4.2 on physical/printed page19 and Remark4.3 on page20 in the pinned34-page v6PDF. The earlier024pointer18–19 does not locate both in this pinned file;locator clarification (historical local record; not distributed here) appends the exact current coordinates without rewriting the historical dossier or its claimed read extent. No novelty inference is made from repackaging these ingredients.

## 8. Dependency disposition and next

| Claim | Outcome | Remaining boundary |
|---|---|---|
| Explicit ell completion/core,positive norm equivalence and exact4.6 | PROVED internally | V with fixed zero-extension support;not arbitrary whole-line functions |
|048global remainder/049H₀¹quadratic identity | PROVED internally,inherited ARTIFACT_VERIFIED | Not recomputed050 |
|047canonical parity application | CONDITIONALLY_PROVED | Only canonical/Friedrichs identification remains named after the remainder,quadratic and actual closure/core inputs are discharged |
| Historical Bombieri2003form values/sector infima | INCONCLUSIVE/HOLD | Original source BLOCKED,retrieval paused pending concrete new lawful pointer |
| RH | OPEN | No global positivity/eigenvalue/zero conclusion |

By bounded perturbation,the source-defined correctly scaled q_a forms from049/047 now have the common closed domain V;on each compact positive parameter interval their shifted form norms are equivalent. Reflection invariance and compactness can therefore use047's established abstract argument with the now-verified norm input. This observation does not silently replace the final identification with the canonical Weil form.

**Next:** compare the actual canonical Weil closed form with the Friedrichs closure of source-defined B_a,at exact normalization. Verify both smooth-core values and canonical-core/domain facts from primary definitions,then use uniqueness of closed forms with a common form core;otherwise identify the first mismatched coefficient or missing core theorem. Do not re-prove this density lemma or reopen generic blocked2003retrieval. Next packet (historical local record; not distributed here).

# Audited historical reading edition

**Current audited claim:** PROVED: The interval operator domain equals supported squared-log Fourier space, with W2 <= 2||Au||^2+(pi^2+2)||u||^2.

**Claim ceiling:** Exact interval logarithmic operator; no H1 trace requirement or eigenvalue value.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle 075 — boundary leakage and the actual logarithmic operator domain

## Verdict and exact supported claim

**PROVED internally, at the stated operator scope:** for the self-adjoint operator A_ell associated with the actual closed form ell on complex L²(I), I=(−1,1), zero extension E satisfies

W₂(u):=(2π)⁻¹∫ℝ(1+log⁺|ξ|)²|F_Eu(ξ)|²dξ

≤2||A_ell u||₂²+(π²+2)||u||₂²

≤(π²+2){||A_ell u||₂²+||u||₂²}, for every u∈D(A_ell).

There is no H¹trace hypothesis. In fact D(A_ell) equals the space of u whose displayed W₂ is finite. The new domain bridge is proved below using **form-core** convergence and global test functions, without assuming operator-core convergence or assuming the desired full-line multiplier domain in advance.

This is an explicit functional-analytic input for the project. It is not an actual eigenvalue enclosure, improved eigenvalue continuity rate, proof of rate sharpness, novelty, historical Bombieri2003 identification, RH, external human review or formal verification. Known ingredients and inherited internal review debt are identified below.

Frozen attempt (historical local record; not distributed here), reconstructed state (historical local record; not distributed here), inherited custody (historical local record; not distributed here).

## 1. Definitions and exact dependencies

All Hilbert inner products are linear in the first entry. For u∈L²(I;ℂ), f=Eu and F_f(ξ)=∫exp(−iξx)f(x)dx. Plancherel is ||f||²=(2π)⁻¹∫|F_f|². Since I has length2, ||F_f||∞≤√2||u||₂.

The inherited [050 proof](m01-log-form-closure-c050.md) establishes the closed nonnegative form

ell(u)=¼∬I² |u(x)−u(y)|²/|x−y| dxdy −½∫I log(1−x²)|u(x)|²dx,

with domain V={u:∫(1+log⁺|ξ|)|F_Eu|²<∞}, and smooth form core C_c^∞(I). On V its polarized form is

ell(u,v)=(2π)⁻¹∫(log|ξ|+γ)F_Eu(ξ)conj(F_Ev(ξ))dξ.

The positive-frequency part is integrable by weighted Cauchy–Schwarz, the negative part by compact support and the bounded Fourier transforms. A_ell is defined by the closed-form representation theorem: u∈D(A_ell) precisely when u∈V and ell(u,v)=〈g,v〉 for some g∈L²(I) and every v∈V; then A_ell u=g. Thus no unproved strong kernel formula is used to define its domain.

The050and [054 dossier](m01-polynomial-complement-c054.md) match their historical immutable manifests. They remain inherited PROVED_INTERNAL inputs, not a full independent re-audit or human review075. Standard ingredients are Plancherel, Cauchy–Schwarz, Tonelli and the closed-form representation theorem. The Carleman bound and the domain extension are derived here.

Let M denote the full-line Fourier multiplier m(ξ)=log|ξ|+γ, initially interpreted on compact-support L² vectors as a tempered distribution. The value at ξ=0 is irrelevant. The logarithmic singularity is not bounded there: local integrability follows from ||F_f||∞ and ∫₀¹|log r|dr<∞. At infinity log times an L² Fourier transform defines a tempered distribution by testing against Schwartz functions.

## 2. Primary-source normalization, on the smooth core only

[Chen–Weth v6, Theorem1.1 and Remark1.2, physical/printed page2](https://arxiv.org/pdf/1710.03416v6) give symbol2log|ξ| and

L_Δf(x)=c₁∫{f(x)1_{|x−y|<1}−f(y)}/|x−y|dy+ρ₁f(x),

with c₁=1 and ρ₁=−2γ in dimension1. Consequently M=L_Δ/2+γI. For f∈C_c^∞(I) and x∉[−1,1], f(x)=0, so

(Mf)(x)=K u(x):=−½∫I u(y)/|x−y|dy.                 (1)

The primary theorem gives L_Δf∈L²(ℝ) and the Fourier identity for smooth compact functions. Real formulas extend by complex linearity. It does not supply the arbitrary D(A_ell) extension needed here.

The whole relevant page was visually read from the hash-verified captured PDF and cross-checked with the live web text. Exact source register (historical local record; not distributed here). A web screenshot cache miss and absent pdftotext command did not produce accepted content; local Poppler rendering worked. No extracted TXT or full34-page read is claimed. This is the same known paper as earlier passes, not another independent source. There is no novelty inference.

## 3. Two full half-lines, including the singular endpoint and infinite tail

For g∈L²(0,∞), consider the Carleman kernel H g(t)=∫₀∞g(s)/(t+s)ds, t>0. With weight w(s)=s⁻¹/², the substitution s=t r² gives

∫₀∞ w(s)/(t+s)ds=2t⁻¹/²∫₀∞dr/(1+r²)=πw(t).

The same identity holds with s,t exchanged. For compactly supported g away from0, weighted Cauchy–Schwarz gives

|Hg(t)|²≤πw(t)∫₀∞ |g(s)|²/{w(s)(t+s)}ds.

Integrate in t and use Tonelli on the nonnegative majorant. The second weight identity yields ||Hg||₂²≤π²||g||₂². Density extends H as a bounded map on all complex L². Absolute values cover arbitrary complex phases, not just positive g. No finite t cutoff or assertion of pointwise endpoint boundedness is made.

For the right half-line write x=1+t,y=1−s,0<s<2. Extending g_+(s)=u(1−s) by zero for s≥2 gives K u(1+t)=−Hg_+(t)/2. The left half-line uses x=−1−t,y=−1+s and g_−(s)=u(−1+s). Each g has norm||u||₂. Hence

||K u||²_{L²(ℝ\I)}≤(π²/2)||u||₂².                (2)

The two output supports are disjoint, so their squared norms add; a missing half cannot be silently discarded. For every fixed t>0 the finite-interval kernel is in L²(0,2), so its integral against arbitrary u∈L²(I) is defined. Density and this pointwise continuity identify that integral with the bounded extension in(2). The endpoints x=±1 have measure zero; the Schur bound controls neighborhoods of them and the entire infinite tails.

## 4. Global-test extension: the domain step

For u∈D(A_ell), choose u_n∈C_c^∞(I) with u_n→u in the **form norm** from050. This implies L² convergence; it does not assert A_ell u_n→A_ell u in L².

First, for each smooth u_n, M E u_n∈L²(ℝ) by the primary theorem (or its smooth Fourier decay). For every v∈V, the polarized pure-log identity equals 〈M E u_n,E v〉. Thus the closed-form representation gives u_n∈D(A_ell) and (M E u_n)|I=A_ell u_n.

Now fix an arbitrary global Schwartz test function φ. Its restriction v=φ|I belongs to V: bounded derivatives control the regional difference quotient, and bounded values make the logarithmic boundary potential integrable. In particular no zero boundary trace is imposed on φ|I. Combining the smooth interior identity with(1) gives the global equality

〈M E u_n,φ〉=ell(u_n,φ|I)+〈K u_n,φ|ℝ\I〉.       (3)

Every term has a justified limit. The form term tends to ell(u,φ|I) by form-norm convergence and Cauchy–Schwarz for ell. The outside term tends to 〈K u,φ|ℝ\I〉 by(2) and L² convergence. For the left side, M E u_n→M E u as tempered distributions: on |ξ|≤1 use ||F_E(u_n−u)||∞≤√2||u_n−u||₂ and integrability of |log|ξ|| times the bounded Schwartz transform; on |ξ|>1 use ordinary L² Cauchy–Schwarz with m·F_φ∈L². No high-frequency graph-norm convergence was assumed.

Since u∈D(A_ell), ell(u,φ|I)=〈A_ell u,φ|I〉. Passing to the limit in(3), for **every global** φ, proves

M E u=E(A_ell u)+1_{ℝ\I}K u ∈L²(ℝ).             (4)

This global test identity rules out any additional endpoint-supported distribution. Separate identifications only inside I and outside its closure would not suffice for that purpose. We did not promote a form core to an operator core.

Disjoint supports in(4) and Plancherel yield the exact norm identity and upper bound

(2π)⁻¹∫m(ξ)²|F_Eu(ξ)|²dξ

=||A_ell u||²+||K u||²≤||A_ell u||²+(π²/2)||u||². (5)

Thus membership of the full-line multiplier domain is a conclusion, not a premise.

## 5. Squared-log graph estimate and converse domain equality

Elementary harmonic-integral bounds give0<γ<1. For |ξ|≥1, 1+log|ξ|=m(ξ)+(1−γ), so (1+log|ξ|)²≤2m(ξ)²+2. For |ξ|<1 the target weight is1, which also satisfies1≤2m(ξ)²+2. Integrating and using(5) proves

W₂(u)≤2||A_ell u||²+(π²+2)||u||².                 (6)

The simpler single graph-norm constant π²+2 follows because π²+2≥2. These are exact nonoptimal constants, not numerical fits. The logarithmic origin singularity was handled explicitly, not replaced by an alleged bounded multiplier.

Conversely suppose u∈L²(I) and W₂(u)<∞. Since the weight is≥1, the first-log moment is finite, so u∈V. For |ξ|≥1, |m(ξ)|≤1+log⁺|ξ|. On |ξ|<1 compact support gives |F_Eu|²≤2||u||² and

∫₀¹(log r+γ)²dr=2−2γ+γ²<∞.

Therefore mF_Eu∈L²(ℝ). For every v∈V, the polarized formula gives ell(u,v)=〈M E u,E v〉=〈(M E u)|I,v〉. The representation theorem now gives u∈D(A_ell). Combined with(6), this proves the exact domain equality with the squared-log moment space. No converse H¹regularity is asserted.

## 6. Adversarial controls and failure distinctions

1. **Nonzero trace:** u=1 on I is in D(A_ell), independently given by054's polynomial action. A_ell1=−½log(1−x²) is square-integrable. On the right K1(1+t)=−½log((t+2)/t), and the left expression is identical. Both logarithmic singularities near t=0 and1/t tails at infinity are square-integrable. Thus the proof admits this discontinuous zero extension; it cannot hide an H₀¹assumption.
2. **Normalization canary:** at x=3, K1=−(log2)/2. Omitting the half in(1) would instead give−log2, a different nonzero value. This falsifies that shortcut, not the proved estimate.
3. **Both sides:** for the same even state, a nonnegative smooth test supported on the left exterior pairs nontrivially with K1. A global identity retaining only the right output would give zero there and is false. Squared norms of the correct two outputs add.
4. **Complex and parity:** all estimates use absolute values or sesquilinear pairings. Multiplication by a complex phase preserves norms; reflection interchanges the two half-lines. No real-state or antilinear-parity restriction is imported.
5. **Boundary distributions:** local interior/exterior agreement alone would leave a potential endpoint distribution. Equation(3) for all global tests closes this gap; no assumption about endpoint traces is needed.
6. **Wrong core:** only form convergence is used in the right side of(3). No convergence of A_ell u_n, no operator-core assertion and no circular full-line graph norm enters the limit.
7. **Origin and infinity:** the compact-support Fourier L∞ bound controls log at zero; weighted Cauchy–Schwarz controls distributional high frequencies before(4). Carleman integrates all t>0. No cutoff leaves a missing range.
8. **Scope:** a bounded form-energy ball need not have bounded operator graph norm. This result does not contradict053's generic inverse-log energy-ball obstruction or prove a rate for actual eigenvalues. Zero state and complex scalar multiples satisfy(2),(4),(6) exactly at their respective scaling.

These are analytic checks, not executed numerical tests or an exhaustive code mutation campaign. No scientific executable, deciding numeric certificate, floating tolerance, failed mathematical control or pipeline change was introduced. Source-reader failures are recorded separately. The same actor/model and inherited definitions/expected answers are shared; this is not blind reproduction, independent human review or formal verification. Efficiency NOT_MEASURED.

## 7. What changed, remaining debt and next consumer

The exact outside coefficient, bounded leakage and actual operator-domain extension now support the squared-log graph estimate. The omitted-half, omitted-side and form-core/graph-core shortcuts are excluded. The mechanism can transfer to other interval normalizations only after their coefficients and form cores are checked. It is not claimed novel.

The next discriminating action is to test the **actual eigenfunction/eigenvalue-rate consumer**, not repeat this Carleman estimate. One proposed compact-parameter squared-log modulus (historical local record; not distributed here) must establish uniform operator graph bounds for all parity minimizers, then redo052's Fourier split, prime thresholds and variational comparison. The proposed rate/constants remain NOT_TESTED075. No practical width1/100head/coupling certificate, improved actual interpolation rate, historical2003identification, RH or new external review is inferred here.

## Authority

Only local OPF writes and public read-only source inspection. No donor file body or donor code read/executed075; no other-estate mutation, agents/threads, messages/uploads/publication/reviewer contact, installs, accounts, application/schedule/notification change or unmanaged continuation.

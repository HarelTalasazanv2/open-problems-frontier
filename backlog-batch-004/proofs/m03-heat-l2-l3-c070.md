# Audited historical reading edition

**Current audited claim:** PROVED: For every nu,t>0 and vector f in L2(R3), ||exp(nu t Delta)f||3 <= (4pi)^(-1/4)(5/6)^(5/4)(nu t)^(-1/4)||f||2.

**Claim ceiling:** The forced/mild transfer is conditional on its stated forcing norm; no nonlinear Navier-Stokes conclusion.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M03 — an explicit positive-time linear bound and the nonlinear input it leaves unpaid

Cycle070; internal analytic verification under the frozen attempt (historical local record; not distributed here). Outcome **PROVED**, restricted linear claim below; **CONDITIONALLY_PROVED**, the stated mild-solution transfer. These are standard analytic ingredients reproduced locally, not claimed novel. No numerical instrument, human review, blind reproduction or formal verification occurred.

## 1. Exact domain, normalization and claim

All spatial integrals use Lebesgue measure on R³. For real vector fields, |f(x)| is the Euclidean norm and ||f||p=(∫|f|^p)^(1/p). For a=νt with ν>0 and t>0 define

G_a(x)=(4πa)^(-3/2) exp(-|x|²/(4a)),  H_a f=G_a*f.

**Claim M03-HEAT-L2-L3-C070:** for every f∈L²(R³;R³),

||H_(νt) f||3 ≤ C_H (νt)^(-1/4) ||f||2,

where C_H=(4π)^(-1/4)(5/6)^(5/4). This is an admissible constant; sharpness is not asserted. In particular the bound holds for compactly supported smooth divergence-free f, where H_(νt)f is an unforced linear Stokes evolution. It is not asserted to be the nonlinear Navier–Stokes evolution.

## 2. Gaussian normalization and its exact L^(6/5) norm

The positive integral I=∫R exp(-z²) dz is finite by comparison of its tails with exp(-|z|). Tonelli and polar coordinates give I²=2π∫₀∞ exp(-r²)r dr=π, hence I=√π. Applying this in each coordinate after dilation gives ∫G_a=1. More generally, for r≥1,

∫G_a^r=(4πa)^(-3r/2)(4πa/r)^(3/2),

so ||G_a||r=(4πa)^(-3/2+3/(2r)) r^(-3/(2r)). Substitution r=6/5 gives

||G_a||_(6/5)=(4πa)^(-1/4)(5/6)^(5/4).

Every integral is finite because a>0. No logarithms, singular denominator or numerical tolerance enter this calculation.

## 3. The needed convolution inequality, including vector fields

Let k=G_a and g=|f|. For each x, ∫k(y)g(x-y)dy is finite by Cauchy–Schwarz since k∈L² and g∈L². The vector integral triangle inequality yields |k*f(x)|≤(k*g)(x), without a dimension-dependent component factor.

Write g_x(y)=g(x-y) and factor the integrand as

k g_x = (k^(6/5)g_x²)^(1/3) k^(3/5) g_x^(1/3).

Hölder in y with exponents 3,2,6 (1/3+1/2+1/6=1) gives

(k*g)(x) ≤ [∫k^(6/5)g_x²]^(1/3) [∫k^(6/5)]^(1/2) [∫g_x²]^(1/6).

The first integral is finite here because k is bounded. Cube this inequality and integrate x. Tonelli, translation invariance and ∫g_x²=||g||2² show

||k*g||3³ ≤ (∫k^(6/5))^(3/2) ||g||2 (∫k^(6/5)) ||g||2²
             = ||k||_(6/5)³ ||g||2³.

Taking cube roots and substituting section2 proves claim1 for every vector L² input. The reciprocal-exponent check is 1+1/3=1/2+5/6. The constant and exponent came from exact integrals, not a fitted grid.

## 4. Why this is the heat/Stokes baseline

For smooth compact f, differentiation under the Gaussian integral gives ∂t H_(νt)f=νΔH_(νt)f. It is justified on any compact positive-time interval by integrable Gaussian derivative bounds and bounded f. If div f=0, integration by parts against compact f gives div H_(νt)f=G_(νt)*(div f)=0. Taking pressure zero therefore solves the unforced linear Stokes equation with this velocity.

The mass-one kernels form an approximate identity: split the integral into |y|<ε and its complement, use uniform continuity of each compact smooth derivative on the first part and the Gaussian tail on the second. Thus the initial datum and its derivatives are recovered as t↓0. Completing the square in G_a*G_b gives G_(a+b), the heat semigroup identity. Jensen with ∫G_a=1, followed by Tonelli, gives ||H_a f||2≤||f||2. Density of compact smooth inputs and this contraction extend the initial-value semigroup in L²; the convolution formula already exists pointwise by Cauchy–Schwarz. These observations fix the meaning of exp(νtΔ) used here.

## 5. An explicit conditional transfer, not an energy closure

Fix ν>0, t>0, u0∈L², and a strongly measurable F:(0,t)→L²(R³;R³). Assume

J_t(F)=∫₀ᵗ (t-s)^(-1/4)||F(s)||2 ds <∞.

Then F is integrable in L² time because (t-s)^(-1/4)≥t^(-1/4). Define

u_t=H_(νt)u0 + ∫₀ᵗ H_(ν(t-s))F(s) ds.

The integral exists in L² by contraction and in L³ because section3 bounds the integrand norm by C_H ν^(-1/4)(t-s)^(-1/4)||F(s)||2. Strong measurability in L³ follows by approximation of F by simple L²-valued functions and the continuity of G_a in L^(6/5) for a>0; that continuity follows by dominated convergence on compact a-intervals. The Banach integral triangle inequality therefore proves

||u_t||3 ≤ C_H (νt)^(-1/4)||u0||2 + C_H ν^(-1/4) J_t(F).

**Conditional nonlinear corollary:** if a whole-space velocity u has the displayed mild identity (in L² or distributions) with F(s)=-P div(u(s)⊗u(s)), and this F satisfies the stated L² measurability/integrability assumptions, the same L³ estimate applies to u(t). Its right-hand side then supplies an L³ representative. This is a sufficient input for this particular estimate, not a claim that this forcing norm is necessary for regularity.

Here (div(u⊗u))_i=Σ_j ∂_j(u_j u_i). On L², P is the Fourier multiplier I−ξξᵀ/|ξ|² for ξ≠0, with arbitrary value at the measure-zero point ξ=0. Each matrix is an orthogonal projection, so P is an L² contraction by Plancherel. It kills gradient multipliers and commutes with heat multipliers. With Fourier convention exp(-2πiξ·x), heat has multiplier exp(-4π²νt|ξ|²). For sufficiently regular decaying projected fields, integrating the forced Fourier ODE gives the same mild formula. No L³ boundedness theorem for P is needed because F itself is assumed in L². We do not establish the required mild identity and forcing estimate for every velocity/pressure in a prize formulation.

Neither finite initial kinetic energy nor the usual energy-class norms have been shown here to bound J_t(-P div(u⊗u)). Dropping this term would discard the nonlinear equation. No local or global nonlinear continuation theorem, singular solution or global resolution follows.

## 6. Source comparison and dependency limits

The [author's exposition](https://terrytao.wordpress.com/2018/09/16/254a-notes-1-local-well-posedness-of-the-navier-stokes-equations/) was partially read: heat multipliers and the fundamental-solution exercise, whole-space forced heat, and the periodic projected Navier–Stokes identity. Its Fourier normalization agrees with section5. The nonlinear passage is explicitly periodic; its local existence theory is not imported as a whole-space result. The heat-kernel exercise is a statement, not proof established by reading it. Sections2–4 supply the calculation needed here. Exact capture and inspection extents (historical local record; not distributed here) distinguish one underlying work from three selected passages.

No fresh global-open status or novelty claim is made. Cycle069's literal Clay Active label and unresolved interpretation remain unchanged; this historical teaching source is not a current global-status authority.

## 7. Adversarial challenge and adjudication

- **Constant/sign/normalization:** the positive Gaussian has mass1; the general-r integral independently tracks amplitude a^(-3/2) and volume a^(3/(2r)). This yields a^(-1/4), matching Hölder reciprocity. Using a kernel L² or L³ norm in the same convolution step would give the wrong exponents.
- **Vector cancellation:** applying the integral triangle inequality to the Euclidean norm handles all components and signs together. A scalar-only proof with an unrecorded component constant was avoided.
- **Boundary controls:** zero input gives zero. ν=0 and t=0 are excluded; the factor diverges in either limit with the other parameter fixed. This bound supplies no uniform initial-time or zero-viscosity estimate.
- **Concentration check:** cycle069's fixed-energy family can have arbitrarily large initial L³. For each fixed positive νt this theorem bounds its heat evolution uniformly by the common L² norm. No contradiction: its estimate deteriorates as t↓0. No datum at infinite concentration is asserted admissible.
- **Nonlinear/domain control:** the forcing term is retained with its exact sign and norm. A periodic mild theorem and smoothness without decay are not silently substituted for a whole-space mild identity. The conditional statement stays valid without proving that all target nonlinear fields meet its hypotheses.
- **Independence:** Gaussian integration, Hölder accounting and amplitude/volume checking are same-actor analytic checks sharing the stated definitions. They are not independent human/external/formal review. No computational canary suite was run or required for an unexecuted research instrument.

Adjudication: **PROVED_INTERNAL** for claim1; **CONDITIONALLY_PROVED** for section5 under its explicit assumptions. Nonlinear energy closure **INCONCLUSIVE / NOT_ESTABLISHED_HERE**; all-time/global Navier–Stokes and novelty **NOT_TESTED**. No failed mathematical control was detected. Inherited outside-review requirements remain outstanding for global promotion.

## 8. What changes next

Viscosity closes the linear positive-time question with an explicit finite constant. The remaining uncertainty is now the projected nonlinear input, not a nearby heat constant. A next test should ask whether the full standard energy-class bounds alone control this specific weighted forcing norm, using a smooth divergence-free space-time concentration family with a nonzero projected convection term. That would challenge an actual nonlinear functional implication without pretending the test fields solve Navier–Stokes. The proposed successor remains NOT_TESTED until its own frozen audit; another heat-kernel bound or initial Lp grid is not selected.

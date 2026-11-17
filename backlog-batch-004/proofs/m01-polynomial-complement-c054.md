# Audited historical reading edition

**Current audited claim:** PROVED: For moment-orthogonal interval vectors the displayed b_N(R) and logN-1 complement lower bounds hold; polynomial heads belong to the represented operator domain. The stated Schur lower enclosure follows when actual head/coupling bounds are supplied.

**Claim ceiling:** Analytic complement theorem and conditional interface only. No actual eigenvalue enclosure, sign result or practical millions-degree computation.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle054 — a polynomial complement bound for a pointwise certificate

**PROVED internally, at the following restricted scope.** For the closed form ell of050 on complex L²(−1,1), its restriction to vectors orthogonal to polynomials of degree<N has an explicit lower bound tending to infinity with N. This supplies one analytic input to a pointwise canonical eigenvalue certificate. It is not a computed eigenvalue enclosure, a practical positivity certificate, novelty, independent expert review, historical2003 identification or RH.

## 1. Contract, normalization and dependencies

The frozen attempt (historical local record; not distributed here) redirects the former selected operator-regularity lemma toward an actual certificate dependency after reviewing successful-route drift in047–053. The consumer is a certified interval for lambda_sigma(1) of width at most1/100, before any interpolation on K=[1,2]. Neither that interval nor its feasibility is established here.

H=L²(I;C), I=(−1,1), f=zero extension of u,
F(ξ)=∫_I exp(−iξx)u(x)dx, ||u||²=(2π)^−1∫|F|².
V={u:∫(1+log⁺|ξ|)|F|²<∞}. Inherited050 gives

    ell(u)=(2π)^−1∫(log|ξ|+γ)|F(ξ)|²dξ,
    ell(u)=¼∬|u(x)−u(y)|²/|x−y| dxdy
           −½∫log(1−x²)|u(x)|²dx ≥0.                 (1)

These exact identities, domain and smooth form core are **PROVED_INTERNAL** dependencies, custody checked but not independently fully re-audited054. Plancherel, Taylor's integral remainder, elementary integral inequalities and finite-dimensional square completion are **STANDARD_THEOREM** ingredients; their uses and constants are derived below. The canonical identification051 and bounded perturbation052 are likewise inherited PROVED_INTERNAL; the historical2003 extension remains UNVERIFIED/HOLD. No source label or hash supplies a missing mathematical argument.

Let P_N be the L² orthogonal projection onto complex polynomials of degree<N, Q_N=I−P_N. N is an integer at least1. No H¹ zero-boundary assumption is made.

## 2. Exact low-frequency loss and complement coercivity

If u∈V and P_Nu=0 then ∫x^k u(x)dx=0 for k=0,…,N−1. For real t, Taylor's integral remainder for exp(−it) has modulus at most |t|^N/N!: every derivative on the real segment has modulus1. Subtracting that polynomial inside F gives

    |F(ξ)| ≤ |ξ|^N/N! ∫|x|^N|u(x)|dx
           ≤ sqrt(2)||u|| |ξ|^N/N!.                  (2)

The coarser sqrt(2) deliberately avoids optimizing constants. This argument covers arbitrary complex u; moment cancellation does not require u real. The negative logarithm near ξ=0 is integrable even without cancellation because |F|≤sqrt(2)||u||. All integrals below therefore have defined negative parts; positive parts are finite on V.

For every real R>0, subtract logR+γ from (1), discard the nonnegative integral over |ξ|≥R, and use(2) on the rest:

    ell(u) ≥ b_N(R)||u||²,
    b_N(R)=logR+γ−2 R^(2N+1)/[π(2N+1)²(N!)²].       (3)

Indeed ∫₀ᴿ ξ^(2N)log(R/ξ)dξ=R^(2N+1)/(2N+1)², by scaling and integration by parts. The factor2/π includes both frequency half-lines and the project's1/(2π), as well as the factor2 in(2). No finite grid, tail truncation or asymptotic remainder is hidden in(3).

Since log(N!)≥∫₁ᴺlogt dt≥NlogN−N, choose R=N/e to obtain

    ell(u) ≥ [logN−1+γ−1/(2πeN)]||u||²
            ≥ (logN−1)||u||².                       (4)

For the last inequality, H_n−log(n+1) increases to γ, so γ≥1−log2>1/4. The strict inequality log2<3/4 follows from exp(3/4)>1+3/4+9/32=65/32>2. Also π>3,e>2 imply1/(2πeN)<1/12. This verifies the sign in(4), including N=1. Nonnegativity in(1) can improve any negative printed bound to0. The best displayed lower bound is max(0,b_N(R)), not necessarily the simplified logN−1. Optimizing R or using the exact moment norm could improve constants but is not needed for this claim.

The subspace statement is essential. For the constant function1, ell(1)=2−2log2, ||1||²=2, so its quotient is1−log2. A claim that(4) holds for every u and all N is false, since logN−1 tends to infinity. This is an exact control against silently dropping moment orthogonality. V is larger than H₀¹; boundary values were not set to zero in the proof.

## 3. Polynomial heads have legitimate strong residuals

Finite polynomial heads must belong to the operator domain before writing a residual A_a p. This does not follow just from being a form-domain trial.

Every polynomial p lies in V by the physical expression(1): it is bounded and Lipschitz on the closed interval, its regional difference quotient is integrable, and −log(1−x²) is integrable. In fact

    A_ell p(x)=½∫_I [p(x)−p(y)]/|x−y|dy
              −½log(1−x²)p(x)                      (5)

belongs to L²(I). The first term is bounded by the Lipschitz constant times the interval length/2; the second is square-integrable because log² of the distance to each endpoint is integrable. Symmetrizing the polarized regional form gives ell(p,v)=<A_ell p,v> for smooth compactly supported v, with the factor1/2 in(5). By050's form-core density and continuity of both sides this identity extends to every v∈V. The representation theorem for a closed nonnegative form then gives p∈D(A_ell). This establishes precisely the finite-head domain input; it does not prove the deferred graph-norm/squared-log theorem for arbitrary operator-domain vectors.

For the canonical fixed-a form q_a=ell+<B(a)u,u>, with B(a) bounded self-adjoint, A_a=A_ell+B(a), D(A_a)=D(A_ell). Thus polynomial residuals are valid L² vectors. Projection P_N is bounded in the form norm because it has finite rank in V, so Q_NV=V∩Q_NH is a legitimate closed form subspace. No inverse of an unbounded far operator has been assumed.

## 4. Exact pointwise certificate interface, conditional on actual inputs

An allowed scalar perturbation bound is

    ||B(a)||≤M(a):=|log a+κ|+2 S(a)+2a[2cosh(a)+1],
    κ=log(2π)+γ,
    S(a)=Σ_{2≤n≤exp(2a)} Λ(n)/sqrt(n).               (6)

This is the052 correlation bound and Schur kernel-size bound at one point, with zero correlations at and beyond displacement2. Hence on Q_NV

    q_a(u) ≥ β||u||²,
    β=max(0,b_N(R))−M(a),                           (7)

or the simpler β=logN−1−M(a). Both are sufficient lower bounds; neither is the actual complement minimum.

Take an orthonormal polynomial basis p_j (normalized Legendre polynomials are one choice) for P_NH. Define the finite Hermitian head H_N=(<A_a p_j,p_i>) and the bounded map G_N=Q_N A_a P_N from that head into its orthogonal complement. The domain assertion in§3 makes these actual L² quantities. For any t<β, a certified Hermitian inequality

    H_N−t I−G_N*G_N/(β−t) ≥0                       (8)

implies q_a(u)≥t||u||² for every u∈V. To prove it, write u=h+v and complete the square in

    <(H_N−t)h,h>+2Re<G_Nh,v>+(β−t)||v||².

No far inverse is needed. If only H_N≥hI and ||G_N||≤η are available, the minimum eigenvalue of the scalar2×2 matrix [[h,−η],[−η,β]] gives the rigorous lower bound

    L=[h+β−sqrt((β−h)²+4η²)]/2.                    (9)

A certified upper bound U for the lowest head eigenvalue gives lambda(a)≤U by variational restriction. Therefore [L,U] is a full-form enclosure **only when** all head, coupling, complement and numerical enclosures are valid in the same normalization. When η=0, (9) is min(h,β); it must not be replaced by h if β<h. With h=β=1,η=2, the full2×2 eigenvalue is−1 despite a positive head. The vector(1,−1) demonstrates the missing-coupling shortcut directly.

For ordinary parity sigma=±1, use only polynomial degrees j<N of that parity. A sector vector orthogonal to that head is automatically orthogonal to all opposite-parity polynomials, hence the same (3)–(7) apply with the full degree parameter N. Reflection commutes with A_a under051; use sector residuals, not an antilinear star. The head dimensions are ceil(N/2) and floor(N/2); the odd head is empty at N=1, so an upper head eigenvalue there is undefined. Use N≥2 for both sectors. These endpoint conventions avoid treating an empty trial space as a certificate.

## 5. Usefulness audit: finite does not imply affordable

The first desired observable is lambda_sigma(1), with a width1/100 target. No actual H_N, G_N, outward quadrature, certified matrix eigenvalues or total error budget has been evaluated054. Thus a numeric enclosure of that width is **NOT_TESTED**, and no sign conclusion follows.

The coarse route can already be shown costly. At a=1, M(1)>14. Here are elementary sufficient lower estimates, used only to diagnose the printed bound. exp(2)>7 by its positive series, so the pool contains2,3,4,5,7. Using log2>2/3 (the first positive term of its atanh series), log3>1, log5>4/3, log7>3/2, sqrt2<3/2, sqrt3<2, sqrt5<5/2, sqrt7<3 gives S(1)>104/45. The log5 bound follows from e<3 and3⁴<5³; log7>3/2 follows from e<3 and27<49. Also κ>7/4 because log(2π)>log6>3/2 and γ>1/4, and2[2cosh1+1]>8. Hence M(1)>7/4+208/45+8=2587/180>14.

Consequently merely making the **simplified** β=logN−1−M(1) positive requires N>exp(15), already millions of polynomial degrees (the exact exp(15) threshold, not an outward decimal, is the recorded conclusion). This concerns this sufficient bound only. It is neither a lower bound on the true necessary head size nor evidence of actual negative complement spectrum. The sharper b_N(R) or a directional/middle-window treatment can improve the route. No large head is allocated or computed.

For052's interpolation bound on K=[1,2], nonnegative terms give C_K≥4cL_R≥3c exp(8c)=6exp16. To make its sufficient printed interpolation error≤1/100 requires log(e/δ)≥600exp16, hence δ≤exp(1−600exp16). This independently verifies the assessment's usefulness diagnosis. It is not a necessary spacing for the actual eigenvalues or a falsification of052. Improve pointwise/complement estimates before spending on a mesh.

## 6. Governor source review and exact scope crosswalk

The latest donor pointer observed054 is RH-GOV-20261023T004745Z, completed00:54:28UTC. Its immutable manifest still binds the earlier C214–C216 sources; these are read through that live lineage rather than treating the prepared packet's old run as CURRENT. Selected hashes and pointer stability are recorded separately. No donor code is executed or donor records changed.

C214's three-block Schur/Woodbury criterion and C215's residual identity were read fully. The abstract linear algebra is normalization independent, but an application is not: split OPF's fixed-a, fixed-parity polynomial head, polynomial window and Q_N far space orthogonally. The exact OPF A_a, target shift t, matrices H,B,T, maps C,D, and far lower μ must be supplied. Then the common form domain and bounded finite-head coupling hypotheses follow as in§3. T>0 and A=μT−C*C>0 remain actual input inequalities; they are not consequences of a positive head. C214's square completion gives S=H−B*T^-1B, Z=D−CT^-1B, and the sufficient head condition S−[Z*Z+(C*Z)*(μT−C*C)^−1(C*Z)]/μ>0. This is an abstract admissible interface, not an identification with Governor's source-specific Liu/Weil object or a verified production cross-Gram.

Independently expanding R=V−AX for arbitrary complex rectangular X,V and finite A=A*>0 gives

    V*A^-1V = X*V+V*X−X*AX+R*A^-1R.

If A≥αI>0 then the last term lies between0 and R*R/α in PSD order. This reproduces C215's exact algebra, including adjoints; same actor/model and source exposure are shared, so it is not blind or external review. Omitting that term fails at A=V=1,X=11/10,S=199/200: Q=99/100 gives a false positive margin1/200, while the exact complement margin is−1/200. Bounds on actual inputs and residuals remain mandatory.

C216 is a **SOURCE_REPORTED** missing elementary-function error premise in its printed donor model. Its logical distinction is preserved: absence of a log/exp contract is not a demonstrated library error or false production certificate. No source production numerical path was replayed here. OPF has no computed interval certificate to which that model can silently be attached.

## 7. Verdict, review debt and next obstruction

**PROVED_INTERNAL:** (3)–(5), the explicit complex polynomial complement bound and polynomial operator-domain formula, within050's exact form normalization. **CONDITIONALLY_PROVED interface:** (7)–(9) and the three-block application only after actual inputs/enclosures meet all hypotheses. **FALSIFIED shortcuts:** removing orthogonality, ignoring complement/coupling, and omitting the inverse residual square. **NOT_TESTED:** actual width1/100, global positivity, operator squared-log regularity, historical form identification, novelty, prompt superiority or speedup.

The uncertainty changed from no explicit polynomial complement bound to a proved but coarse bound with a quantified cost obstruction. This transfers to other fixed-support logarithmic forms plus bounded perturbations; no transfer to a different source normalization is presumed. Do not repeat coarse mesh or huge-head work without an improved far estimate, directional/window mechanism, or actual enclosed inputs.

Review debt persists in047–051. Their custody and source correspondence do not constitute a complete independent proof audit. Before a high-value numeric canonical certificate, review050's support-specific pure-log identity/core and051's shared-cutoff/canonical identification. The next prioritized action is a compact source-bound review of this high-leverage interface and the first tighter complement/coupling mechanism; a fresh adjacent regularity lemma is deferred pending that decision. The exact next packet specifies the stop rule. RH remains unresolved per [Clay's current owning page](https://www.claymath.org/millennium/riemann-hypothesis/), observed054; this is a status poll, not new mathematics.

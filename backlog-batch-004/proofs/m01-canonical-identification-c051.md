# Audited historical reading edition

**Current audited claim:** PROVED: For the explicitly specified Connes-Consani canonical multiplier and pole/prime terms, its closed form equals the Friedrichs closure of the displayed D-star-G-D form, with common supported log domain; ordinary parity infima are attained and continuous.

**Claim ceiling:** Canonical formulas and named special-function identities only; no unavailable historical 2003 extension, positivity or RH.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle051 — canonical Weil form equals the source-defined Friedrichs form

**PROVED internally, at this restricted scope:** for every a>0 the Connes–Consani2023 Proposition2.1 localized closed Weil form, transported by v(t)=F(e^t), is exactly the closure of the quadratic form of Suzuki v3's source-defined B_a=D*G_aD on complex H₀¹(−a,a). Both have the same zero-extension logarithmic form domain V_a and smooth interior form core. Consequently the correctly formulated canonical even and odd unit Rayleigh infima are finite, attained and continuous on (0,∞), by the internally proved047 compactness argument with048–050 dependencies now discharged.

This verifies a known canonical interpretation, not a novel theorem, the unavailable historical Bombieri2003 extension, the false imported antilinear parity identification, positivity, eigenvalue simplicity or RH. It is an internal analytic audit, not outside human review or formal verification. The historical identification remains INCONCLUSIVE/HOLD and its original-source retrieval remains BLOCKED/paused.

## 1. Frozen object and evidence

The051 attempt (historical local record; not distributed here) fixes all a>0, complex functions, the Fourier/coordinate convention, acceptance and falsifier lanes before the deciding derivation. No numerical deciding instrument is used. The primary [Connes–Consani paper](https://ems.press/content/serial-article-files/44477?nt=1), *Spectral triples and ζ-cycles*, Enseign. Math.69(2023), defines the canonical object in equations(2.7)–(2.12) and Proposition2.1. Physical PDFpages9–13 (printed101–105) were read as extracted text, with physical10–11 also visually inspected in the pinned56-page PDF. In particular the minus sign defining W_infinity=−W_R, the pole cross-product, n^−1/2 and Haar measure were checked visually. Lemma2.2 and its multiplier asymptotic are on physical12–13. Only these extents are claimed, not a complete-paper audit.

The [current Suzuki v3 source](https://arxiv.org/html/2606.09096v3) supplies the exact g and B_a definitions and introductory W. The arXiv owning record still lists v3 dated September23,2026 on today's bounded check. We do **not** assume its target identification Theorem1.1. The [Clay owning page](https://www.claymath.org/millennium/riemann-hypothesis/) still labels RH Unsolved. These are bounded primary checks, not exhaustive current-literature or novelty searches.

Known inputs are the exact global r048, distributional/core/H₀¹identity049, and actual logarithmic completion/core050. Their mathematical statements are inherited internally; verifying artifact custody does not re-prove them. Standard Plancherel, bounded perturbations and uniqueness of a closed form with a form core are used explicitly. The Connes–Consani distribution-to-multiplier identity(2.9) and asymptotic in Lemma2.2 are named primary analytic inputs, not independently audited special-function theorems. Neither is the target Friedrichs identification.

## 2. Exact conventions and canonical definition

Let I_a=(−a,a), λ=e^a, H_a=L²(I_a;C), zero extension f, and

F_v(ξ)=∫_R e^(−iξt)f(t)dt,  ||f||²=(2π)^−1∫|F_v|².

The unitary logarithmic map from L²([λ^−1,λ],du/u) is F↦v, v(t)=F(e^t); there is **no** extra e^(t/2) here. That factor belongs instead to the older L²(dx) map already checked020. The multiplicative involution is F*(u)=conjugate(F(u^−1)). Its convolution satisfies

(F* * F)(e^t)=∫conjugate(f(x−t))f(x)dx=C_v(t),
C_v(t)=∫f(x+t)conjugate(f(x))dx.

Thus C_v(−t)=conjugate(C_v(t)), C_v(0)=N=||v||² and C_v(t)=0 for |t|≥2a. Source sesquilinear conventions are antilinear first, while049 uses linear first; their diagonal values agree. Equality of diagonals determines the corresponding Hermitian polarizations after aligning conventions, not by identifying unlike ordered sesquilinear arguments.

On smooth compactly supported v, equations(2.6)–(2.9) of the primary source become

Q_can(v)=P(C_v)−Σ_{2≤n≤e^(2a)} c_n[C_v(τ_n)+C_v(−τ_n)]−W_R(C_v),
P(C)=∫_R C(t)(e^(t/2)+e^(−t/2))dt,
c_n=Λ(n)/sqrt(n), τ_n=log n,
k(t)=e^(−t/2)/(1−e^(−2t))=e^(t/2)/(e^t−e^(−t)), t>0,
W_R(C)=(log(4π)+γ)C(0)+∫₀∞[C(t)+C(−t)−2e^(−t/2)C(0)]k(t)dt.       (1)

The cancellation in the square brackets makes the integral locally integrable: C(t)+C(−t)−2C(0)=O(t²), and 2(1−e^(−t/2))C(0)=O(t). At infinity C is compactly supported and e^(−t/2)k(t) decays. Hence this is an ordinary convergent improper integral, not a difference of divergent values.

The pole expression is exactly

P(C_v)=2 Re[(∫e^(t/2)f(t)dt) conjugate(∫e^(−t/2)f(t)dt)]
      =2 Re[F_v(i/2) conjugate(F_v(−i/2))].             (2)

Both integrals are bounded linear functionals on fixed H_a by Cauchy–Schwarz. It is a rank-two **cross** term, not a sum of positive squares. Prime correlations are bounded by N, giving exactly the bounded self-adjoint operators of(2.12); the endpoint overlap is null. No unverified positivity/RH is used.

## 3. Decisive archimedean finite-part constant

Use the fixed distribution from049:

<P₀,C>=lim_{ε↓0}[∫_ε∞(C(t)+C(−t))/(2t)dt+log ε C(0)].

For t>0 the proved048 remainder identity is

r″(t)=−p(t)+k(t)−1/(2t), p(t)=e^(t/2)+e^(−t/2).

Also g″=P₀+(2A+1)δ₀+Σc_n(δ_{τ_n}+δ_{−τ_n})+r″,
2A+1=log(2π)+γ. This fixes the origin delta, not just a punctured derivative.

The only new constant calculation needed is elementary:

2∫_ε∞ e^(−t/2)k(t)dt
 =∫_ε∞ dt/sinh t
 =−log tanh(ε/2)
 =−log ε+log2+o(1).                                  (3)

The antiderivative follows by differentiating log tanh(t/2); tanh(ε/2)/(ε/2)→1. Thus from(1)

−W_R(C)=−lim_{ε↓0}[∫_ε∞(C(t)+C(−t))k(t)dt+log ε C(0)]
          −[log(2π)+γ]C(0).                         (4)

This checks the change from log(4π) to log(2π); omitting the log2 in(3) gives a nonzero error log2*N. The manipulation uses one shared cutoff throughout. It never subtracts two unevaluated divergent integrals.

Combining P₀ with the r″ integral, first at that same ε, gives

−<P₀,C>−∫_R r″(t)C(t)dt
 =P(C)−lim_{ε↓0}[∫_ε∞(C(t)+C(−t))k(t)dt+log ε C(0)]. (5)

Indeed the 1/(2t) terms cancel outside ε. The omitted ∫₀^ε(C(t)+C(−t))r″(t)dt tends0 because r″ is continuous/bounded near0 and C bounded. The p integral on(0,ε) also tends0. All remaining tails pair with compactly supported C, so the growth of p at infinity causes no issue. This justifies the limit rather than manipulating singular kernels pointwise at zero.

For smooth v,049 already proves Q_B(v)=−<g″,C_v>. Substituting(5), the exact delta coefficient and paired primes now yields precisely(1):

**Q_B(v)=Q_can(v), every complex v∈C_c^∞(I_a).**         (6)

The source Theorem1.1 was not used. This is an exact coefficient comparison, not a grid or agreement of decimal evaluations.

## 4. Closed domains, common core and Friedrichs conclusion

The actual primary closed definition(2.11), transported to H_a, is

Q_can(v)=(2π)^−1∫_R m(ξ)|F_v(ξ)|²dξ + P(C_v)−Σ c_n[C_v(τ_n)+C_v(−τ_n)],
m(ξ)=2θ′(ξ)=Re ψ(1/4+iξ/2)−logπ.                   (7)

The primary formula(2.9) identifies the archimedean term in(1) with this multiplier on the smooth core. The paper's Lemma2.2 gives m(ξ)=log|ξ|−log(2π)+O(|ξ|^−2) at infinity. It is real, continuous and bounded below on R (ψ has no pole on this vertical line). Thus there are constants C,b,B>0 with

b[1+log⁺|ξ|]≤m(ξ)+C≤B[1+log⁺|ξ|].                 (8)

To see this, use the leading log growth outside a sufficiently large compact set, then choose C to make the continuous multiplier strictly positive on that compact set and bound its extrema there. There is no negative log singularity in m at ξ=0, nor any infinite-minus-infinite cancellation.

The pole operator and finite prime sum in(7) are bounded self-adjoint on H_a. A sufficiently large L² shift therefore makes its form norm equivalent to the weighted Fourier norm in(8), with exact finite domain

V_a={v∈H_a:(2π)^−1∫[1+log⁺|ξ|]|F_v(ξ)|²dξ<∞}.       (9)

This is a closed fixed-support subspace of weighted Fourier L², hence complete. By050, with unitary rescaling w(x)=sqrt(a)v(ax), C_c^∞(I_a) and H₀¹(I_a) are form cores of V_a. Fixed a only changes the logarithmic weights by comparable constants: F_v(ξ)=sqrt(a)F_w(aξ), and 1+log⁺|η/a| is comparable to 1+log⁺|η|. Thus050's support contraction followed by compact mollification applies in this norm too. We do not infer form density merely from L² density or from set equality.

Independently049–050 give the closure of Q_B on H₀¹ as L_a plus bounded perturbations on this same V_a. Specifically L_a(v)=ell(w)−log a*N, with the r″ integral bounded by2a sup_{|t|≤2a}|r″(t)|N, and the finite prime terms bounded by2Σc_n*N. Hence this closure is lower bounded and closed, with the same smooth core. Both closed forms extend (6). Completing that common core in either shifted form norm gives identical limits and L² representatives; therefore the closed forms are equal on all V_a, with +∞ off V_a. Polarization gives the aligned sesquilinear equality. The form closure of the semibounded symmetric B_a on its dense H₀¹ operator domain is exactly its Friedrichs form. The associated self-adjoint operators consequently agree; their **operator** domain is not asserted to equal the form domain V_a.

## 5. Adversarial controls and falsifier lanes

| Attack | Exact check and disposition |
|---|---|
| Haar/half-density | du/u=dt; adding e^(t/2) here changes norm and prime/pole terms. Older L²(dx) map remains a different object. |
| Complex phase and orientation | F* *F maps exactly to C_v; replacing v by iv preserves every quadratic term. For v(t)=e^(iωt)u(t), real u, C_v(t)=e^(iωt)C_u(t), so paired primes are2cos(ωτ)C_u(τ), not2C_v(τ). Covers genuinely complex correlations. |
| Pole sign | For real nonzero odd u(t)=t(1−t²/a²), ∫e^(t/2)u>0 and ∫e^(−t/2)u<0, so(2) is negative. A sum-of-squares replacement fails this admissible H₀¹ control. |
| Origin/delta constant | Shared-cutoff identity(3) fixes log2; changing g by b|t| changes Q_B by−2bN while leaving the punctured second derivative unchanged. Such a normalization change cannot inherit this identification. |
| Prime interfaces | C_v(τ)=0 at |τ|≥2a exactly; on strict overlap a positive H₀¹ polynomial has C>0. Both signs and n^−1/2 remain. No threshold tolerance or infinite prime limit. |
| Form domain boundary | The constant indicator on I_a has Fourier decay O(1/|ξ|) and belongs to V_a despite nonzero traces. Its finite energy is inherited050. Do not impose H₀¹ traces on V_a or call all L² finite energy. |
| Closure uniqueness | Equality on a merely L²-dense set would be insufficient;050 supplies actual common form-norm cores and(8) transfers that core to the primary definition. Operator-domain equality with V_a is not claimed. |
| Parity and parameter limits | Ordinary complex-linear reflection Jv(t)=v(−t), not conjugate reflection. Results below hold at every fixed a>0 and on compact positive parameter sets; no a↓0 or a→∞ statement. |

All eight analytic attacks preserve the restricted result. No new failed mathematical control or source discrepancy was found051. Existing047/049 restricted display counterexamples remain visible and unchanged; neither is silently repaired in source bytes. Same agent/model/platform and expected-answer exposure are shared: this source/distribution/common-core audit is not blind reproduction, independent-person review or formal verification. No method speedup benchmark was performed.

## 6. Discharge of canonical parity dependency and remaining boundary

Under unitary scaling to H=L²(−1,1), the now-identified canonical form is exactly

q_a(w)=ell(w)−[log a+(2A+1)]||w||²
 −Σ c_n <(S_{τ_n/a}+S_{−τ_n/a})w,w>−<K_a w,w>,
K_a(x,y)=a r″(a(x−y)), domain V=V_1.

On each compact a∈[b,c]⊂(0,∞), only finitely many n≤e^(2c) are needed. The compressed translations are contractions, strongly continuous and zero at |h|≥2; the remainder kernels are norm continuous by048. These statements include every prime threshold. Reflection commutes with the paired shifts, even kernel and scalar shift.050 makes ell closed/nonnegative/reflection invariant, and047's Fourier-tail/tightness proof gives compact form embedding. All hypotheses of047's fixed-sector lemma are therefore satisfied without the formerly outstanding identification assumption.

For σ=±1, with ordinary linear parity,

λ_σ(a)=inf{Q_can(v):v∈V_a,v(−t)=σv(t),||v||₂=1}

is finite, attained and continuous for a>0. This is now **PROVED internally** for the canonical forms, as a consequence of the linked chain, rather than CONDITIONALLY_PROVED on an unidentified canonical object. No positivity, simplicity, endpoint limit, historical2003-value equality or RH follows. The historical report047 remains unedited; this dossier is the dated dependency-discharge continuation.

What changed: exact archimedean normalization and common-core uniqueness remove the final canonical identification gap. The elementary shared-cutoff calculation transfers to other logarithmic-kernel comparisons. Do not repeat the settled canonical identity, confuse it with the missing historical extension, or resume paused historical endpoints without a new lawful pointer. For the next discriminating mathematical step, a quantitative local continuity modulus can test how much the strong-translation/compactness proof actually controls, including prime thresholds; that proposed refinement is not proved here.

# Audited historical reading edition

**Current audited claim:** PROVED: On complex H01, the displayed source-defined quadratic form has the exact regional/boundary, scalar, paired-prime and remainder decomposition.

**Claim ceiling:** Exact specified form and normalization; no historical extension, positivity, numeric enclosure or new source-layout audit.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle049 — exact localized quadratic decomposition

**PROVED internally, PASS AT CLAIM CEILING:** for every a>0 and every complex v∈H₀¹(−a,a), the quadratic form of the exact source-defined operator B_a=D*G_aD equals the intended Suzuki v3(2.5), with the precise finite-part constant, both prime correlations and the global remainder kernel. This proves a source-defined H₀¹ identity, not the canonical closed-form/Friedrichs identification or a historical Bombieri identification. Canonical parity remains CONDITIONALLY_PROVED on the remaining closure/core and identification inputs. No RH, novelty, independent human or formal-verification claim.

**FALSIFIED at a separate restricted scope:** the literal unqualified cutoff row-integral identity printed on Suzuki v3 PDF page9 fails in the endpoint strip. The interior-qualified version is correct. An explicit vanishing boundary correction below proves that this failure does not invalidate the limiting quadratic identity.

Attempt frozen (historical local record; not distributed here) at2026-10-22T05:34:00.736514UTC, after reading the exact source definitions and before deciding the derivation or the proposed endpoint counterexample. No numerical deciding instrument or imported program executes. The [048 global r lemma](m01-global-remainder-c048.md) is inherited ARTIFACT_VERIFIED rather than re-proved.

## 1. Exact objects, conventions and statement

Fix I=(−a,a), a>0. L² is complex with ⟨u,v⟩=∫u conjugate(v), linear in the first variable. Let f be the zero extension of v∈H₀¹(I), so f∈H¹(R), and define

C_v(t)=∫_R f(x+t) conjugate(f(x))dx, N=||v||².

Then C_v(−t)=conjugate(C_v(t)), C_v(0)=N and C_v(t)=0 for |t|≥2a. There is no trace ambiguity at |t|=2a, since the overlap has measure zero. Define

L_a(v)=¼∬_{I²}|v(x)−v(y)|²/|x−y| dxdy −½∫_I log(a²−x²)|v(x)|²dx.

Use the exact g from [Suzuki arXiv2606.09096v3(1.3)](https://arxiv.org/html/2606.09096v3#S1.E3), A=(log(2π)+γ−1)/2, c_n=Λ(n)/sqrt(n), τ_n=log n, and the exact global decomposition established048:

g(t)=h(t)+A|t|+g₀(t)+r(t),
h(t)=½|t|log|t|,
g₀(t)=Σ_{n≥2}c_n(|t|−τ_n)_+.

The sum is locally finite, r is real even C²(R), and r″ is bounded on each compact interval. The convention is h(0)=0. Source [definitions(1.5),(1.6),(2.1)](https://arxiv.org/html/2606.09096v3) give D=i d/dx on H₀¹(I), G_a=P_aGP_a on the mean-zero space, and B_a=D*G_aD. P_a removes the mean on I; G uses kernel g(x−y). These are source definitions, not a new theorem. The precise result is

Q_g(v):=⟨B_av,v⟩
 =L_a(v)−(2A+1)N
  −Σ_{2≤n≤exp(2a)}c_n[C_v(τ_n)+C_v(−τ_n)]
  −∬_{I²}r″(x−y)v(y)conjugate(v(x))dxdy.                 (Q)

Each term is finite for v∈H₀¹(I). No positivity assumption is imposed. The finite cutoff includes equality, whose correlation is zero. Both sides are real; the paired prime term is 2Re C_v(τ_n), not 2C_v(τ_n) for an arbitrary complex v.

## 2. Operator domain and mean projection

On [−2a,2a], g is continuous and g′ is locally integrable. Indeed h′(t)=½sgn(t)(log|t|+1) for t≠0 is L¹ near zero, (A|t|)′ is bounded, g₀′ is a finite step function locally, and r′ is continuous. A bounded derivative or a finite one-sided derivative limit at zero is not needed and is false for h′.

Multiply g by a smooth compact cutoff equal1 on a neighborhood of [−2a,2a]. This yields a W¹,¹(R) convolution kernel. Young's inequality shows that convolution with any zero-extended u∈L²(I) has an L² weak first derivative on I. Thus G_a u∈H¹(I)=D(D*); subtracting its mean only subtracts a constant. B_a is well-defined on all H₀¹(I) with the source conventions.

For v∈H₀¹(I), ∫_I Dv=i(v(a)−v(−a))=0 by the zero traces, so P_aDv=Dv. Since P_a is orthogonal,

⟨B_av,v⟩=⟨G_aDv,Dv⟩=⟨GDv,Dv⟩
 =∬_{I²}g(x−y)v′(y)conjugate(v′(x))dxdy.             (G)

The factors i and conjugate(i)=−i multiply to1. In particular the projection has been removed by a mean-zero identity, not by dropping an unexplained rank term. This integral is absolutely convergent and bounded by 2a sup_{|t|≤2a}|g(t)| ||v′||². It is a continuous quadratic form in the H₀¹ norm for fixed a.

## 3. Distributional second derivative and its constant

Define the exact origin-regularized distribution P₀ by

⟨P₀,φ⟩=lim_{ε↓0}[½∫_{|t|>ε}φ(t)/|t|dt + log ε φ(0)], φ∈C_c^∞(R).

The limit exists: combine the two sides of zero, write φ(t)+φ(−t)−2φ(0)=O(t²), and integrate that divided by t on0<t<1; the rest is ordinary integration. The reference scale in this definition is fixed. A different reference scale changes the delta coefficient and must not be silently used with the same A.

Direct integration by parts twice on (ε,∞), applied to φ(t)+φ(−t), yields

⟨h″,φ⟩=lim_{ε↓0}{½∫_{|t|>ε}φ(t)/|t|dt +(log ε+1)φ(0)}
       =⟨P₀,φ⟩+φ(0).

To justify the boundary replacement explicitly, h(ε)=½ε log ε multiplies φ′(ε)−φ′(−ε)=O(ε); and h′(ε)=½(log ε+1) multiplies φ(ε)+φ(−ε)=2φ(0)+O(ε²). Both discarded terms are O(ε²|log ε|). Thus

h″=P₀+δ₀, (A|t|)″=2Aδ₀,
[g₀]″=Σ_{n≥2}c_n(δ_{τ_n}+δ_{−τ_n}).

The last identity follows directly from the slopes of (|t|−τ)_+, τ>0: the derivative jumps by1 at both signed thresholds. There is no delta at zero because this term is identically zero near zero. On every compact interval the sum has finitely many nonzero terms. Finally r″ is the ordinary continuous derivative, so globally as distributions

g″=P₀+(2A+1)δ₀+Σc_n(δ_{τ_n}+δ_{−τ_n})+r″.          (D)

The +1 in (D) is essential; differentiating only at nonzero t would miss it.

## 4. Smooth interior functions and correlation

Initially take v∈C_c^∞(I), so its zero extension is smooth and C_v∈C_c^∞(R). A direct integration by parts gives

∫ f′(y)conjugate(f′(y+t))dy=−C_v″(−t).

Putting t=x−y in (G), using the evenness of g and changing t→−t, gives Q_g(v)=−⟨g″,C_v⟩. Distributional pairing is complex-linear in C_v with no extra conjugation; its value is real because g″ is real/even and C_v has Hermitian symmetry. Substitution of (D) gives the prime terms and the smooth r″ term of(Q), as well as −(2A+1)N. It remains to show that −⟨P₀,C_v⟩ is exactly L_a(v), including endpoint effects.

For ε>0 set

J_ε(v)=−log ε N−½∬_{I²,|x−y|>ε}v(y)conjugate(v(x))/|x−y| dxdy.

By changing variables this is −log ε N−½∫_{|t|>ε}C_v(t)/|t|dt. Hence lim J_ε=−⟨P₀,C_v⟩. The following calculation both identifies its limit and controls the boundary strip for general H₀¹ functions.

## 5. Correct cutoff identity, source counterexample and boundary estimate

For x∈I and ε>0 the exact row integral is

m_ε(x)=∫_{y∈I,|x−y|>ε}dy/|x−y|
      =[log((a+x)/ε)]_+ + [log((a−x)/ε)]_+,

where [u]_+=max(u,0). The source's unnumbered PDFpage9 display writes m_ε(x)=log(a²−x²)−2log ε without an interior restriction. That formula is valid when ε≤min(a+x,a−x); it is not valid on all I at fixed ε.

**Exact literal-display counterexample:** a=1, ε=1/2, x=3/4. Only y∈(−1,1/4) contributes, so m_ε(x)=log(7/2). The printed right side is log(7/4). Correct minus displayed equals **log2>0**. This falsifies the unqualified finite-ε identity only. The PDF page9 image and identity receipt (historical local record; not distributed here) confirm the display is present in the PDF, not only a reader transformation. Source bytes remain unchanged; an interior reading is correct. No public correction or contact was sent.

For 0<ε<a put d(x)=min(a−x,a+x),

D_ε(v)=¼∬_{I²,|x−y|>ε}|v(x)−v(y)|²/|x−y| dxdy.

Symmetry cancels the imaginary part of the product integral. Expanding the square gives exactly

J_ε(v)=D_ε(v)−½∫_I log(a²−x²)|v(x)|²dx−E_ε(v),
E_ε(v)=½∫_{d(x)<ε}|v(x)|² log(ε/d(x))dx ≥0.       (B)

Thus the false unqualified row formula omits E_ε, rather than proving an error in the limit. The zero-trace estimate |v(a−d)|²≤d∫_{a−d}^a|v′|² and its reflected version imply the safe explicit bound

0≤E_ε(v)≤(ε²/4)||v′||²,

using ∫₀^ε d log(ε/d)dd=ε²/4 and bounding each endpoint derivative integral by ||v′||². No tolerance substitutes for the missing strip.

Also the zero extension f∈H¹(R) satisfies ||f(·+h)−f||₂≤|h| ||v′||₂ (fundamental theorem for H¹ functions and Cauchy–Schwarz, or density). Therefore

0≤D(v)−D_ε(v)≤¼∫_{|h|≤ε}||f(·+h)−f||²/|h|dh≤(ε²/4)||v′||²,

where D(v) is the full difference integral with prefactor1/4. Combining with(B) proves

0≤L_a(v)−J_ε(v)≤(ε²/2)||v′||², 0<ε<a.        (E)

In particular −⟨P₀,C_v⟩=L_a(v) on the smooth core. Formula(Q) follows there with exactly the intended coefficients.

An independent correlation check gives a stronger bound. Since C_v(t)+C_v(−t)−2N=−||f(·+t)−f||²,

L_a(v)−J_ε(v)=½∫₀^ε ||f(·+t)−f||² dt/t≤(ε²/4)||v′||².  (E′)

Here the equality follows by writing J_ε at two positive cutoffs, subtracting, and taking the limit just proved by(E). This cross-check validates the direction/sign and improves the bound without using the invalid pointwise row formula. It applies to H₀¹ after §6; no formal pairing of a general nonsmooth correlation with an arbitrary distribution is needed.

## 6. H₀¹ extension and domain coverage

The standard definition H₀¹(I)=closure of C_c^∞(I) in H¹ gives v_j→v in H¹ and zero extensions f_j→f in H¹(R). The latter follows first for compactly supported smooth functions and then by completion; no boundary jump delta occurs because traces are zero.

All terms of(Q) are continuous in this topology:

1. The derivative-kernel integral(G) has bounded g on I−I, as shown in §2. Its polarized form is bounded by2a sup|g| ||u′|| ||v′||.
2. D(v)≤a²||v′||² by integrating the translation estimate for |h|≤2a. Its polarized Cauchy–Schwarz estimate gives continuity under H¹ convergence.
3. W_a=∫_I|log(a²−x²)|dx is finite (log singularities at the endpoints are integrable). The bound ||v||_∞≤sqrt(2a)||v′||₂ implies ∫|log(a²−x²)||v|²≤2a W_a||v′||². Uniform convergence of v_j gives continuity of this weighted term, including both endpoint strips.
4. Each correlation is a bounded L² quadratic form: |C_v(τ)|≤||v||², and |C_u(τ)−C_v(τ)|≤(||u||+||v||)||u−v||. Only finitely many n satisfy τ_n≤2a.
5. With M_a=sup_{|t|≤2a}|r″(t)|<∞ from048, the r″ integral has absolute value≤2a M_a||v||² and is a continuous L² quadratic form.

Taking j→∞ proves(Q) for every complex H₀¹ vector. The cutoff relations(B),(E),(E′) follow directly for H₀¹ by the same finite integrals and translation estimate, or by this convergence. This is not an extension to the full logarithmic closed-form domain by L² density. Such a closure/core comparison remains a named separate input.

## 7. Analytic controls and falsification attempts

| Attack | Exact control / result | Scope |
|---|---|---|
| Delta constant at zero | h″=P₀+δ₀ from two integrations by parts, with O(ε² abs(log ε)) discarded terms;A abs(t) contributes2Aδ₀ | Missing +1 changes the form by N for every nonzero v |
| Sign and conjugation | At a=1,u(x)=1−x², ∫∫ abs(x−y)u′(y)u′(x)=−32/15 while ||u||²=16/15. Direct inner integral is2x−(2/3)x³. Replacing u by i u preserves this value with the conjugate;omitting it flips the sign | Exact nonzero control,not numerical agreement |
| Mean projection | ∫Dv=0 by both zero traces,so P_aDv=Dv;adjoint moves the orthogonal projection to Dv | No discarded rank term;requires H₀¹ |
| Boundary cutoff | Literal PDFpage9 display fails by log2 at(1,1/2,3/4);max-log formula and E_ε restore exact finite cutoff | Restricted source-display FALSIFIED;limiting(Q) survives |
| Cutoff error direction | Positive E_ε and positive D−D_ε give(E);correlation gives sharper(E′) | Error tends0 with explicit H¹ bound,not a finite grid |
| Prime sign/membership | Distributional slope jumps yield one delta at each ±τ;for2a≤τ overlap is zero,for2a>τ a nonnegative H₀¹ polynomial has positive overlap | Paired coefficient−c_n and exact threshold included;all locally finite terms covered |
| Hidden regularity | g′ has an integrable log singularity;Young with W¹,¹ cutoff gives G_a L²⊂H¹ | Does not assume bounded g′ or its finite origin limit |
| Extension | Every term bounded in H¹ norm,not just L² density;zero extension preserves H¹ via zero traces | Covers H₀¹ and complex phases,not arbitrary L² or historical extensions |

The polynomial prime control is v(x)=1−x²/a² on I, positive throughout I. If0<τ<2a, the overlap interval(−a,a−τ) has positive length and both factors are positive almost everywhere there, so C_v(τ)>0. At equality the interval is null. This distinguishes a real paired negative contribution from the wrong sign or a missing member. Scaling c_n by n^−1/2 is fixed in the source definition, not inferred from a target value.

There are eight analytic attack items. No mathematical acceptance control failed for(Q);one different literal finite-cutoff source statement was decisively falsified and replaced only in this new derivation,with its old source bytes preserved. No software certificate, high-precision arithmetic or sign grid is used. Same agent/model/platform and target exposure are shared;this is a different derivation using distributions,correct boundary rows and H¹ estimates,not blind reproduction or external expert/formal review. Efficiency NOT_MEASURED.

## 8. Dependency disposition and next obstruction

| Claim | Outcome | Exact limit |
|---|---|---|
| Global r regularity and kernel bounds048 | PROVED internally,inherited ARTIFACT_VERIFIED | No rerun or promotion |
| Source-defined quadratic identity(Q) on H₀¹ | PROVED internally | Complete conditional only on exact g definition and048 lemma; no unknown analytic step retained within this scope |
| Unqualified finite-cutoff row identity on whole I | FALSIFIED | Exact log2 endpoint-strip counterexample;interior-qualified identity valid |
|047 canonical parity application | CONDITIONALLY_PROVED | Global remainder and H₀¹ decomposition now discharged;logarithmic norm/core/closure and canonical/Friedrichs identification remain |
| Historical Bombieri2003 form values/sector infima | INCONCLUSIVE/HOLD | Original source access BLOCKED;retrieval remains paused |
| RH | OPEN | Clay owning page Unsolved checked2026-10-22;bounded status check |

Next select a precise closure/core bridge for the explicit L_a form,with a common form-norm domain under scaling. Existing023 already proves the literal regional/Hlog finite-value set comparison and024 finds relevant prior art;do not repeat those set equalities. The new task must establish the actual completion/density/norm identity needed in047,including cutoff/mollification control,or locate the precise missing canonical identification input. It must not infer a historical extended form from a canonical completion. Next packet (historical local record; not distributed here).

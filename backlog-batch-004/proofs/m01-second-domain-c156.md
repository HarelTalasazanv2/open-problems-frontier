# Audited historical reading edition

**Current audited claim:** PROVED: For the actual interval logarithmic operator, D(A squared) equals supported D(M squared), with the displayed fourth-log moment and tail bounds for canonical parity minimizers.

**Claim ceiling:** Actual kernel structure essential; no all-powers, eigenvalue-modulus improvement, useful mesh or RH.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M01: the actual exterior operator supplies the second global domain

Cycle156, 2026-11-09 UTC / America/Los_Angeles. **PROVED, internal restricted analytic result:** for the actual logarithmic interval operator, not an arbitrary block compression,

    D(A²)={u∈L²(-1,1;ℂ):Eu∈D(M²)}.                 (1)

All ordinary complex even/odd minimizers of the canonical form therefore have the uniform fourth Fourier-log moment in (16). This resolves the specific actual exterior-domain gap recorded in [155](m01-compressed-iteration-c155.md). Its abstract counterexample remains valid. The added actual Hilbert/cutoff structure is essential to this proof.

**Claim ceiling:** one second-domain identification, its quantitative graph bound and fourth-moment/tail consequences. This is an internal derivation and self-challenge under the named inherited analytic inputs. It is not a new RH positivity theorem, a practical eigenvalue mesh, an eigenvalue-modulus improvement, a novelty claim, blind reproduction, external human review or formal verification.

## 1. Objects, conventions and inherited evidence

I=(-1,1), H=L²(I;ℂ), 𝓗=L²(ℝ;ℂ), E:H→𝓗 zero extension, R=E* restriction, P=ER, Q=1-P. Inner products are linear in their first argument; all norms use Lebesgue measure. Fourier convention:

    f̂(ξ)=∫ exp(-ixξ)f(x)dx,   ||f||²=(2π)^(-1)∫|f̂|².

M is the maximal self-adjoint multiplier m(ξ)=log|ξ|+γ, with domain {f:m f̂∈L²}. The value at ξ=0 is irrelevant as a measure-zero convention. A is the nonnegative self-adjoint operator represented by

    ell(u)=1/4∫∫_(I²)|u(x)-u(y)|²/|x-y| dxdy
           -1/2∫_I log(1-x²)|u(x)|²dx.

The 084 proof (historical local record; not distributed here), selected lines30–146, gives the full operator identity, not merely a smooth-core formula:

    D(A)={u:Eu∈D(M)},   MEu=EAu+Ku,
    ||MEu||²=||Au||²+||Ku||².                       (2)

Here K:H→Q𝓗 is the bounded exterior map

    Ku(x)=-1/2∫_I u(y)/|x-y|dy, x outside [-1,1],
    ||K||≤κ:=π/2.                                   (3)

Endpoint values are not required. Let ℋ be the full-line Hilbert transform, Fourier multiplier -i sign(ξ), and S the physical-space multiplication sign(x). Distinguishing these two signs is crucial. The same actual-kernel derivation gives on all H

    K=-κ S Q ℋ E.                                  (4)

Also [155, section3](m01-compressed-iteration-c155.md) proves

    P D(M)⊂D(M),  ||[M,P]||≤κ.                     (5)

These are explicitly inherited internal analytic premises, with relevant source/dossier identity checks in inherited identity evidence (historical local record; not distributed here). The domain and kernel arguments were directly re-read. Hashes establish identity, not mathematical truth or independent review.155's actual canonical minimizer theorem will be used only in section6; the general domain proof below does not assume an eigen-equation.

## 2. Source normalization and the off-diagonal kernel

The primary [NIST DLMF6.2.11–13](https://dlmf.nist.gov/6.2#E11) states the cosine-integral definition and the relation Ci(z)=γ+log z-Cin(z), with Cin(z)=∫₀ᶻ(1-cos t)dt/t. We use positive real z only, so no branch crossing is involved. These formulas support the normalization, rather than a theorem about the new domain lift.

For a compact smooth f the finite-part expression is

    M_εf(x)=log(1/ε)f(x)
            -1/2∫_(|x-y|>ε)f(y)/|x-y|dy,
    Fourier symbol m_ε(ξ)=log(1/ε)+Ci(ε|ξ|).         (6)

The nonintegrable spatial tail is interpreted as a tempered convolution / oscillatory Fourier transform. Testing first against compact smooth functions justifies the displayed expression. The cosine integral gives

    m_ε(ξ)=m(ξ)-Cin(ε|ξ|) → m(ξ) for ξ≠0.

For0<ε≤1, Cin(ε|ξ|) is bounded by C+2log⁺|ξ|: split its integral at1, use (1-cos t)≤t²/2 near0 and ≤2 afterwards. This bound, Schwartz Fourier decay and local integrability of |log|ξ||² show M_εf→Mf in L². In particular the off-diagonal distribution kernel of M is -1/(2|x-y|); local identity terms in (6) vanish between disjoint supports. This re-derives the normalization used in084 rather than applying a formula for a different factor2 logarithmic Laplacian.

For the Hilbert transform convention, the regularized kernel x/[π(x²+ε²)] has Fourier multiplier -i sign(ξ)e^(-ε|ξ|), as obtained from ∫₀∞e^(-εt)sin(xt)dt=x/(x²+ε²). Plancherel and dominated convergence give the unitary L² limit ℋ. Thus

    ℋ D(M)=D(M),   Mℋf=ℋMf,   ||ℋf||=||f||.         (7)

The sign multiplier has modulus1 almost everywhere, including both low and high frequencies. This covers the logarithmic singularity at zero; no uniform boundedness of m near zero is presumed.

## 3. A half-line cutoff preserves the actual multiplier domain

Let P₊ be multiplication by1_(0,∞), P₋=1-P₊. Start with a Schwartz f. Both g₊=P₊f and g₋=P₋f lie in D(M), even when f(0)≠0. Indeed |ĝ₊|≤||f||_(L¹(0,∞)) near zero. For |ξ|≥1, integration by parts on the half-line gives

    ĝ₊(ξ)=[f(0)+∫₀∞f'(x)e^(-ixξ)dx]/(iξ),
    |ĝ₊(ξ)|≤(|f(0)|+||f'||_(L¹(0,∞)))/|ξ|.         (8)

The boundary term at infinity vanishes by Schwartz decay. Since log² is integrable at zero and log²r/r² is integrable at infinity, (8) proves domain membership. The negative half-line is identical after reflection. We do not silently impose a zero trace at the jump.

The cross action on x<0 is

    (P₋MP₊f)(x)=-1/2∫₀∞f(y)/(y-x)dy
                =κ(P₋ℋP₊f)(x).                    (9)

Here is a domain-safe derivation that never assumes (6) can simply be applied to a discontinuous g₊. Test against φ∈C_c∞(-∞,0). Its support has positive distance from the positive half-line. Self-adjointness gives ⟨MP₊f,φ⟩=⟨P₊f,Mφ⟩. Formula (6) applies to the smooth compact φ and has no singularity on y>0; Fubini is absolute because of the separation and Schwartz integrability of f. The result is (9) as a distribution on the open negative half-line. Both sides are L², so the identity holds almost everywhere there. A single excluded point cannot conceal an extra L² vector or a delta distribution.

Let B₊=κP₋ℋP₊, a bounded map P₊𝓗→P₋𝓗 with norm≤κ. Since ℋ*=-ℋ, its adjoint is B₊*=-κP₊ℋP₋. The reflected version of (9) is precisely P₊MP₋f=B₊*f. Therefore on Schwartz f

    [M,P₊]f=B₊f-B₊*f=:J₊f,
    ||J₊||≤κ.                                      (10)

The bound is κ, not an unjustified addition of two overlapping blocks: in P₊𝓗⊕P₋𝓗 the matrix is [[0,-B₊*],[B₊,0]], with orthogonal outputs. No sharpness is needed.

Schwartz functions form a true graph core of M. In Fourier variables, compact smooth functions supported on annuli away from zero are dense in L²((1+m²)dξ), by truncation followed by smooth approximation on each annulus. Their inverse transforms are Schwartz. For f_n→f in this graph norm, the identity MP₊f_n=P₊Mf_n+J₊f_n has convergent right side; P₊f_n→P₊f in L². Closedness of M yields

    P₊D(M)⊂D(M),   [M,P₊]=J₊ on D(M).              (11)

Since S=2P₊-1 almost everywhere, it follows that

    S D(M)=D(M),   ||[M,S]||≤2κ.                    (12)

Equality of the domains follows by S²=1. The value of sign at0 is immaterial. Similarly (5) gives QD(M)⊂D(M), ||[M,Q]||≤κ. This proof uses a full-line graph core and never asserts that the interval's C_c∞ form core is an operator core.

## 4. The actual exterior graph map

For u∈D(A), set f=Eu∈D(M). By (7), (11)–(12) and (5), each composition in S Q ℋ f belongs to D(M). Thus (4) proves Ku∈D(M). More explicitly, on these established domains,

    M S Q ℋ f = S Q ℋ Mf + S[M,Q]ℋf + [M,S]Qℋf.

Using ||S||=||ℋ||=1, ||Q||≤1, ||[M,Q]||≤κ and ||[M,S]||≤2κ yields

    ||MKu||≤κ||MEu||+3κ²||u||,   u∈D(A).           (13)

This is the additional actual-operator structure missing from a generic bounded exterior block. Every unbounded composition has been licensed before expansion; no assertion that bounded operators automatically preserve graph domains is made.

## 5. Both directions of the second-domain identification

If u∈D(A²), then u,Au∈D(A). Formula (2) shows EAu∈D(M), while (13) shows Ku∈D(M). Consequently MEu=EAu+Ku∈D(M), so Eu∈D(M²).

Conversely, if Eu∈D(M²), then Eu∈D(M) and (2) implies u∈D(A). By (13), Ku∈D(M). Also MEu∈D(M), so EAu=MEu-Ku∈D(M). Applying the exact first-domain characterization in (2) to Au gives Au∈D(A), hence u∈D(A²). This proves (1). The reverse direction was recorded as a bounded analytic amendment (historical local record; not distributed here) before the deciding completed proof was saved.

The same argument gives, for every u∈D(A²),

    ||M²Eu|| ≤ sqrt(||A²u||²+κ²||Au||²)
                +κ sqrt(||Au||²+κ²||u||²)+3κ²||u||. (14)

To see the first square root, apply the exact orthogonal-support identity (2) to Au. Apply (13) and (2) to bound MKu. Then use M²Eu=MEAu+MKu and the triangle inequality. No orthogonality between these last two global terms is asserted.

Equivalently, (1) identifies D(A²) with the supported fourth logarithmic Fourier-moment space. At high frequencies t=log|ξ|≥0 and0<γ<1, so

    (1+t)^4≤γ^(-4)(t+γ)^4,  (t+γ)^4≤(1+t)^4.

At |ξ|<1, |widehat(Eu)|≤√2||u||, and ∫₀¹(log r+γ)^4dr=24-24γ+12γ²-4γ³+γ⁴ is finite. These facts prove both directions, despite the low-frequency singularity and the zero of m on a finite-frequency sphere. In particular, with

    W4(u)=(2π)^(-1)∫(1+log⁺|ξ|)^4|widehat(Eu)|²dξ,

one has W4(u)≤||u||²+γ^(-4)||M²Eu||². Positivity0<γ<1 can be obtained without decimals from the usual increasing H_n-log(n+1) and decreasing H_n-log n bounds, with strict bounds after n≥2. No numerical enclosure for γ is needed.

## 6. Uniform bound for the actual canonical minimizers

Fix any positive compact interval Kpar=[b,c]⊂(0,∞), allowing b=c. Take precisely155/080's constants M_K,S_K,M_R,L_R with R0=2c, and

    J_K=2c sqrt(12M_R²+43c²L_R²),
    C_K=2πS_K+2J_K,
    H_K=21/2+2M_K,     D_K=H_K²+C_K.

For avoidance of ambiguity, M_R=2cosh(c)+1,
L_R=sinh(c)+(19/48)e^(4c)+(3/4)e^(8c),
S_K=Σ_(2≤n≤e^(2c))Λ(n)/√n, and
M_K=max(|log b|,|log c|)+|log(2π)+γ|+2S_K+2cM_R.
An empty prime pool has S_K=0. No pool membership is differentiated.

155 proves for every ordinary complex even or odd unit minimizer of the actual canonical q_a=A+B(a), a∈Kpar,

    ||Au||≤H_K,  ||A²u||≤D_K.

There is no eigenvalue simplicity, spectral-gap, real-valued or chosen-branch hypothesis. Substitute these upper bounds in (14), whose right side is increasing in each nonnegative norm. Define

    G_K=sqrt(D_K²+κ²H_K²)+κsqrt(H_K²+κ²)+3κ².         (15)

Then uniformly over a∈Kpar and all these minimizers,

    ||M²Eu||≤G_K,
    W4(u)≤1+γ^(-4)G_K²=:F_K.                       (16)

This is an explicit coarse analytic bound; no claim of numerical practicality or constant optimality is made. A direct, exactly scoped tail corollary is

    (2π)^(-1)∫_(|ξ|>ρ)|widehat(Eu)(ξ)|²dξ
         ≤F_K/(1+log ρ)^4,    ρ≥1.                 (17)

It follows just by the lower bound on the weight in the integration region. It is a Fourier L² tail inequality, not an eigenvalue continuity theorem or proof that a finite grid decides positivity. This run does not derive or test such a mesh/modulus.

## 7. Adversarial adjudication

| Obligation/attack | Evidence | Result | Limitation |
|---|---|---|---|
| Nonzero half-line trace and spatial infinity | Equation(8), including f(0) and Schwartz tail | PROVED graph-core membership | No assertion for arbitrary H¹ on an infinite interval without decay |
| Low-frequency log singularity | L¹ cutoff bound, integrable log²/log⁴ | PROVED | No bounded-symbol shortcut |
| Cross-block sign/factor | Domain-safe dual testing(9), ℋ*=-ℋ | PROVED(10) | The physical and Fourier signs remain distinct |
| Extend beyond smooth inputs | Full-line graph core and closed M | PROVED(11) | No interval operator-core promotion |
| Actual exterior kernel | K=-κSQℋE from084 plus composition domains | PROVED(13) | Generic bounded K would not suffice |
| Reverse domain inclusion | EAu=MEu-Ku after(13) | PROVED(1) | Exactly second domains, not all powers |
| Complex parity/all minimizers |155exact actual-form theorem and monotone substitution | PROVED(16) | Inherited internal analytic input, not independent human review |
| Generic counterexample from155 | C=diag(n),K0z=z(1/n) lacks proved(13) | Remains valid | No contradiction with the actual logarithmic theorem |
| Stronger global target | No positivity/mesh/novelty proof attempted | NOT_TESTED | RH remains owner-listed Unsolved |

Known-good structural controls are K=0 / u=0, a smooth trace-zero function and a smooth nonzero-trace function in(8). Explicitly f(x)=e^(-x²) has f(0)=1 and ∫₀∞|f'|=1, giving the high-frequency bound2/|ξ|; f(x)=x e^(-x²) has zero trace, positive-half-line L¹ norm1/2 and derivative variation√2e^(-1/2). Multiplication by i tests the same inequalities for complex inputs. These exact calculations do not hide a discarded boundary term.

A separate actual-kernel sign control takes u=1 on I, admissible in D(A) by155. For |x|>1,

    K1(x)=-1/2 log((|x|+1)/(|x|-1))<0.

It is real, even and nonzero. Since QℋE1 is real, replacing the physical sign S in(4) by the Fourier sign multiplier would give a nonzero purely imaginary vector. Thus this concrete input rejects that normalization mistake. Likewise a nonnegative Schwartz f on the positive half-line, tested against nonnegative φ supported strictly on the negative half-line, makes(9) strictly negative; reversing the sign of its cross block fails this control.

The negative generic block control from155fails the added property(13), exactly where it should: its exterior vector(1/n) is not in D(diag(n)). All these are analytic challenges, not executable mutation scores or independent reproductions.

The primary source increment reads the selected DLMF cosine-integral equations, context and branch convention, and the Clay status/heading region. Exact byte/line/entity extents, whole-file hashes, source lineage and parser limits are in the inspection register (historical local record; not distributed here). The DLMF formulas were compared as mathematical content with084's transcription; Clay is a bounded owner-status check only, not an exhaustive current literature or novelty search. No new PDF was read or scientific source program executed.

One actor/model constructed and challenged this proof, with exposure to155,084and the favored result. This is internal analytic review, not blind reproduction or outside expert review. Standard L² Fourier theory, self-adjoint multiplier theory and Hilbert-transform normalization are stated or derived at the steps used. All numerical certificate, simulation, model-comparison and speedup lanes are NOT_TESTED / NOT_MEASURED. Native code checks only custody and current-state consistency.

## 8. Outcome, usefulness and stopping point

The exact unresolved dependency changed: the actual exterior map does preserve the first graph domain, and the compressed second domain is exactly the supported global second multiplier domain. Thus fourth-log moments and the tail corollary can now be used locally under the written premises. The half-line cutoff mechanism transfers to this multiplier's translated cutoffs and the same Hilbert factorization; it does not transfer to arbitrary abstract block operators.

Stop here. Do not repeat155's abstract counterexample search, another unchanged regularity argument, a matrix grid, or a precision increase. Next proposal, **unselected pending a fresh comparative contract**: specify one actual canonical eigenvalue-continuity/certificate consumer, compact parameter interval and tolerance, then test whether(16)–(17)make that target feasible. This decides utility of the new moment bound rather than adding another operator-power lemma. Compare against other ready scientific obligations first; all other route pauses and the closed M02/M05sequences remain unchanged.

Run details and authority: Cycle156 report (historical local record; not distributed here). Artifact folder: m01_exterior_lift_cycle156 (historical local record; not distributed here).

## 9. Separate analytic check of the cross-block norm

After reflecting x=-s<0, the kernel in(9) is -1/[2(s+t)], s,t>0. Its norm bound can also be derived without the Hilbert Fourier multiplier. With weight w(t)=t^(-1/2),

    ∫₀∞ w(t)/(s+t)dt=πw(s),

by t=s r² and2∫₀∞dr/(1+r²)=π. Weighted Cauchy–Schwarz gives for T with positive kernel1/(s+t),

    |Tf(s)|²≤πw(s)∫₀∞|f(t)|²/[(s+t)w(t)]dt.

Integrating and using the same identity in s yields ||Tf||²≤π²||f||², first for compact supported functions and then by density. Therefore the cross block with its factor-1/2 has norm≤π/2=κ, in agreement with(10). Nonnegative integrands justify Tonelli; this does not require the non-square-integrable weight itself to be a vector in the Hilbert space. This different analytic estimate checks a possible factor2 error, while sharing the derived cross kernel and the same actor/model. It is not independent external review.

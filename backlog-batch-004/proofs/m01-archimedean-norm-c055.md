# Audited historical reading edition

**Current audited claim:** PROVED: For every real frequency, w <= m+C0 <= 6w with the displayed m and C0. The stated support-specific archimedean and closed-form identities follow under the named standard identities.

**Claim ceiling:** Named digamma/Fourier identities; no novel theorem, numeric eigenvalue or historical 2003 result.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle055 — audit of the canonical logarithmic form interface

**PASS AT CLAIM CEILING, internal exposed review.** The selected050/051 interface survives the checks below. We rederive the archimedean distribution/multiplier correspondence directly from the digamma integral, without assuming the target source identification, and replace unspecified growth-comparison constants by an explicit global bound:

    w(ξ) ≤ m(ξ)+C₀ ≤ 6w(ξ),  ξ∈R,
    w(ξ)=1+log⁺|ξ|,
    m(ξ)=Re ψ(1/4+iξ/2)−logπ,
    C₀=1−m(0)=1+γ+π/2+3log2+logπ.                 (A)

This is **PROVED internally** from named standard special-function identities. It is not claimed novel. The support-specific pure-log identity, smooth form core, shared cutoff constant and canonical closed-form equality are rechecked. No specific invalid necessary step was found in050/051. This is a review of those stated dependencies, not independent expert approval of the entire047–054 chain, a historical2003 identification, a numeric eigenvalue enclosure or RH.

## 1. Frozen object, sources and trust boundary

Frozen055 attempt (historical local record; not distributed here),01:41:22UTC, selects one linked interface audit after the054 readiness result. Consumer: an eventual ordinary-parity lambda_sigma(1) interval of width1/100. Current head/complement/residual/error inputs remain uncomputed. The competing ready EBRAINS source/units audit is deferred because this interface is the immediate high-leverage input to that numerical consumer. The M07 distant-state route has no new motivated certificate ready. No adjacent regularity lemma is automatically resumed.

Primary Connes–Consani, *Spectral triples and ζ-cycles* (2023), pinned PDF SHA256 `6e2e2611014d24a4951de04779f297fa7f609141929aea3dde18de69e92841b7`: physical10–11/printed102–103, equations2.7–2.12 and Proposition2.1, were fully reinspected visually and as the source defining object. These are known-source reinspections, not a new paper or independent source. Extraction has corrupted mathematical glyphs; the page images fix the minus sign W_infinity=−W_R,1/(2π),paired pole term,n^−1/2,Haar measure and the antilinear-first source convention.

New decision-relevant handbook extents are [DLMF5.7.6](https://dlmf.nist.gov/5.7.E6) and [5.5.4/5.5.5](https://dlmf.nist.gov/5.5); [5.9.16](https://dlmf.nist.gov/5.9.E16),already used048,is reinspected with its Re z>0 hypothesis. These are standard identities from an already known handbook, not new independent works. The exact source/capture kinds and extents are in the055inspection register. The positive-real Ci convention from050/DLMF6.2.11–13 is retained at its exact pinned source version.

048global r and049source-defined core identity are inherited PROVED_INTERNAL inputs at their recorded versions, not fully re-audited here. We recheck the specific origin delta and coefficient use needed below.050's closure/domain argument is reviewed explicitly. Standard Fourier/Plancherel, weighted-L² density, bounded perturbations and closed-form representation results are named STANDARD_THEOREM ingredients. DLMF identities are not formally verified from first axioms. Shared actor/model/platform, source selection and expected-answer exposure prohibit describing this as blind or external review.

## 2. Global multiplier comparison, without an asymptotic-only argument

The partial-fraction identity for ψ is valid away from its nonpositive-integer poles. Subtract its values at b+iy and b, with b=1/4,y=ξ/2, and take real parts:

    Re ψ(b+iy)−ψ(b)
       = Σ_{n=0}∞ y²/[(n+b)((n+b)²+y²)].            (1)

Every term is nonnegative. The series converges uniformly for y in a bounded interval by a constant times(n+b)^−3 beyond a finite index; thus the subtraction, real parts and continuity are justified. At y=0 it is exactly0. For y≠0, put f_y(t)=y²/[t(t²+y²)]. This is positive and decreasing for t>0, because

    f_y'(t)=−y²(3t²+y²)/[t²(t²+y²)²]<0.

Integral comparison therefore gives

    ∫_b∞ f_y(t)dt ≤ Σ_{n=0}∞ f_y(n+b)
                     ≤ f_y(b)+∫_b∞ f_y(t)dt.

The integral is(1/2)log(1+y²/b²), and f_y(b)≤1/b=4. Hence for all real ξ,

    ½log(1+4ξ²) ≤ m(ξ)−m(0)
                    ≤ 4+½log(1+4ξ²).              (2)

For |ξ|≤1, the right side plus1 is≤5+(log5)/2<6, while the lower side plus1 is≥1. For |ξ|≥1, the lower side plus1 is≥1+log|ξ|; the upper is≤5+(log5)/2+log|ξ|≤6(1+log|ξ|). These inequalities establish(A), including ξ=0 and |ξ|=1. They are global exact inequalities, not a finite frequency sample, a numerical evaluation of ψ, or an unchecked asymptotic.

For completeness the constant is explicit in elementary constants. The series at z=1 gives ψ(1)=−γ. Logarithmic differentiation of the gamma duplication formula at positive real z yields ψ(z)+ψ(z+1/2)=2ψ(2z)−2log2. At z=1/2 this gives ψ(1/2)=−γ−2log2; at z=1/4 it gives ψ(1/4)+ψ(3/4)=−2γ−6log2. Reflection gives ψ(1/4)−ψ(3/4)=−π. Thus ψ(1/4)=−γ−3log2−π/2, proving the displayed C₀. There are no branch or pole crossings on these positive real arguments.

## 3. Rederive the archimedean correspondence directly

For Re z>0, the absolutely convergent digamma integral is

    ψ(z)+γ=∫₀∞[e^−t−e^(−zt)]/(1−e^−t)dt.

At z=1/4+iξ/2, take real parts and substitute t=2s. Near0 its numerator is O(t) for fixed ξ; at infinity its real part decays exponentially. With

    k(s)=e^(−s/2)/(1−e^(−2s)), s>0,

we obtain

    m(ξ)=−γ−logπ
          +2∫₀∞[e^(−2s)−e^(−s/2)cos(ξs)]/(1−e^(−2s))ds.

The difference between replacing e^(−2s) by e^−s in this integral is

    2∫₀∞(e^−s−e^(−2s))/(1−e^(−2s))ds
       =2∫₀∞ ds/(e^s+1)=2log2.

Consequently the exact identity is

    m(ξ)=−[log(4π)+γ]
          +2∫₀∞[e^(−s/2)−cos(ξs)]k(s)ds.           (3)

The factor2log2 is indispensable. This is an independent derivation of the pivotal multiplier convention used in051, from a standard ψ identity rather than assuming the paper's distribution-to-multiplier conclusion(2.9).

Let v∈V_a, I_a=(−a,a), f its zero extension,
F(ξ)=∫exp(−iξt)f(t)dt, N=||v||²,
C_v(s)=∫f(x+s)conjugate(f(x))dx.
Then (2π)^−1∫cos(ξs)|F|²=Re C_v(s).

We justify Fubini even for the full form domain. For0<s≤1,

    k(s)≤e²/(2s),
    |e^(−s/2)−cos(ξs)|≤s/2+min(2,ξ²s²/2).

Split the second integral at s=1/max(1,|ξ|). Its ds/s integral is≤1/4+2log⁺|ξ|. The first contributes1/2. For s≥1, k(s)≤e^(−s/2)/(1−e^−2) and the numerator is≤2. Thus

    ∫₀∞ |e^(−s/2)−cos(ξs)|k(s)ds
        ≤(e²/2)[3/4+2log⁺|ξ|]
          +4e^(−1/2)/(1−e^−2).                    (4)

The right side is integrable against |F|² for v∈V_a. Absolute Fubini is therefore valid; no O(s²) smooth-correlation assumption is imported for arbitrary V_a states. Integrating(3) gives

    (2π)^−1∫m(ξ)|F|²dξ
      =−[log(4π)+γ]N
        −∫₀∞[C_v(s)+C_v(−s)−2e^(−s/2)N]k(s)ds
      =−W_R(C_v).                                 (5)

This ordinary integral is absolutely convergent on V_a by(4), not merely defined by a formal difference of infinities. It extends the smooth-core correspondence to the finite logarithmic form domain directly.

## 4. Audit the support-specific pure-log identity and core

For a=1,050's crossing-count identity is

    T₂=∫_{|h|<2}||T_hf−f||²dh/|h|
       =R(v)+4log2*N+2B(v),
    ell+log2*N=T₂/4.

Both crossing orientations are necessary. Tonelli and Plancherel give T₂=(2π)^−1∫4J(2|ξ|)|F|², where J(r)=∫₀ʳ(1−cos t)dt/t. The constants and positivity match the interval indicator exactly: N=2,ell=2−2log2,T₂=8. No zero trace is imposed on the final domain.

The questionable-looking step is not a pointwise multiplier equality. With Ci(r)=γ+logr−J(r), truncate at T≥2:

    (2π)^−1∫[Ci(T|ξ|)−Ci(2|ξ|)]|F|²dξ
       =∫₂ᵀ Re C_v(h)dh/h=0.                     (6)

Finite-interval Fubini is valid because |F|²∈L¹. Fixed support implies C_v(h)=0 for h≥2. Each Ci integral is absolutely integrable: compact support gives |F|²≤M=2N, Ci has a logarithmic origin singularity and |Ci(r)|≤2/r at infinity. To take T→∞, split at1/T and1. The three absolute bounds are

    2M(|γ|+5/4)/T,
    4M logT/T,
    (2/T)∫|F|²,

respectively. All vanish. Thus ∫Ci(2|ξ|)|F|²=0 and

    ell(v)=(2π)^−1∫(log|ξ|+γ)|F|²dξ.              (7)

This audit found no invalid infinite interchange in050. The support assumption, however, cannot be dropped; Ci(2|ξ|) is not pointwise zero. For general a the identical argument starts at2a and proves ∫Ci(2a|ξ|)|F|²=0. Crossing counts give L_a=T_{2a}/4−log(2a)N, leading to the same pure-log formula in physical coordinates. Unitary rescaling w(x)=sqrt(a)v(ax) yields L_a(v)=ell(w)−log a*N. This checks the scale and shift independently of the source's previously rejected intermediate display.

The form-core passage also survives. Weighted Fourier L² with weight w is complete; fixed physical support is an L²-closed subspace. The near-identity unitary contraction U_ρf=ρ^−1/2 f(·/ρ) has Fourier transform sqrt(ρ)F(ρξ), is uniformly bounded in that weighted norm for1/2≤ρ≤2, and is strongly continuous by frequency-compact dense approximation. Contract physical support first, then mollify with radius smaller than its distance to the boundary. Dominated convergence proves the fixed-contraction mollifier limit. Choose contraction and mollifier radii sequentially, rather than assume one uniform domination for an arbitrary joint limit. Every approximant lies in C_c^∞(I_a). This establishes a genuine form core. An even mollifier and the contraction commute with ordinary linear reflection, so it applies to both complex parity sectors.

The equivalence of050's positive translation energy and w gives closedness of ell and D(ell)=V, as in its complete argument. It is not inferred from L² density alone. The interval indicator belongs to V although it is outside H₀¹; the known d^−1/2/log(e/d) endpoint control has finite L² norm but infinite logarithmic boundary energy, so not all L² states are admitted. Operator-domain and form-domain membership remain distinct.

## 5. Source conventions and shared cutoff

The primary multiplicative Haar measure is du/u. The unitary map is v(t)=F_source(e^t), without e^(t/2); that extra factor belongs to a different L²(dx) convention. The multiplicative convolution F_source* * F_source maps to C_v(t), with negative-exponent Fourier transform |F(ξ)|². Source sesquilinear forms are antilinear first; project049 uses linear first. Compare diagonal values and align polarization, rather than equate unlike ordered arguments.

The source pole is

    P(C_v)=2Re[F(i/2)conjugate(F(−i/2))],             (8)

not a sum of two positive squares. It is bounded on fixed H_a since the two exponential moments have L² representers. A real odd nonzero state gives opposite real moments and a strictly negative value; an even real state gives a positive value. The source prime contribution is exactly −Σ c_n[C_v(logn)+C_v(−logn)], c_n=Λ(n)/sqrt(n), with n≤exp(2a). Both directions and the weight survive the map. At equality the overlap is null; no boundary tolerance is used. For complex modulations C_v(s)=e^(iωs)C_u(s), the pair is2cos(ωs)C_u(s), not2C_v(s).

The exact048 remainder obeys r″(s)=−p(s)+k(s)−1/(2s) for s>0, p(s)=e^(s/2)+e^(−s/2). The origin distribution049 is fixed by

    <P₀,C>=lim_{ε↓0}[∫_ε∞(C(s)+C(−s))/(2s)ds+logε*C(0)].

Direct boundary terms in differentiating |s|logs/2 give h″=P₀+δ₀; the linear cusp A|s| adds2Aδ₀, hence κ=2A+1=log(2π)+γ. A punctured second derivative alone would miss this delta. This is the specific049 constant rechecked here; the rest of048/049 is inherited, not claimed fully independently audited.

At one shared cutoff,

    2∫_ε∞e^(−s/2)k(s)ds=−log tanh(ε/2)
        =−logε+log2+o(1).

Therefore W_R(C)=lim_{ε↓0}[∫_ε∞(C(s)+C(−s))k(s)ds+logε*C(0)]+κC(0). Combining P₀ with r″ at that same cutoff gives P(C) minus this limit; the omitted near-zero r″ term tends0 by its boundedness. The pole's exponential growth is harmless because C has fixed compact support. Together with the correctly paired prime atoms this reproduces Q_B=Q_can on complex C_c^∞(I_a). A missing log2 would change the form by log2*N and is rejected.

## 6. Closed domain and uniqueness: complete the audited bridge

By(A), Q_infinity+C₀N has norm equivalent to W on the fixed-support space, with explicit factors1 and6. Its closed finite domain is exactly V_a. Pole and finitely many prime terms are bounded self-adjoint forms; for example their joint norm is at most4sinh a+2Σc_n. Adding that finite bound to the shift preserves the equivalent norm and closed domain. Thus the canonical form in the primary Proposition2.1 has D(Q_can)=V_a and a smooth interior form core. No appeal to an unquantified large-frequency asymptotic or to Suzuki's target identification theorem is necessary for this step.

Independently050and049 give the closed source-defined form on the same V_a with that same smooth core. Their diagonal values agree there by§5. Choose one sufficiently large L² shift for both forms. The shifted norms coincide on the common core, so its Cauchy completions and L² limits coincide. Consequently the closed forms agree on all V_a, and their aligned Hermitian polarizations agree. The associated self-adjoint operators agree by closed-form representation, without identifying their operator domains with V_a. For every a>0 this confirms the exact canonical interface used by052/054. No conclusion at a=0 or infinity is added.

## 7. Adversarial disposition and remaining work

| Obligation/attack | Audit result | Boundary |
|---|---|---|
| m near0 versus pure log | m is finite and minimized at0 by(1); pure log's singularity is integrable for compact support | They are not pointwise equal multipliers |
| Global m comparison | Exact positive-series integral bounds prove(A), all real frequencies | No numerical ψ enclosure or sharp constant |
| Digamma/kernel Fubini | Absolute bound(4) covers full V_a | Not all arbitrary L² Fourier tails |
| Ci cancellation | Finite truncation plus three vanishing bounds proves support-specific identity | No unrestricted whole-line statement |
| Core versus L² density | Support contraction then mollification gives actual form-norm density | No boundary trace imposed on V_a |
| Haar,phase,pole,primes | Exact maps and complex/parity bad variants checked | Older L²(dx)/antilinear-star objects remain distinct |
| Shared cutoff/delta | Both log2 and +1delta retained | A changed normalization needs a new crosswalk |
| Closed equality | Same smooth core and shifted completion used | Smooth equality alone would be insufficient |

No failing mathematical control was found for this interface. The rederived statements are PROVED_INTERNAL under the named standard identities and048/049inputs. The new explicit comparison and full-V_a archimedean integral justify the previously source-reported multiplier step at local derivation scope. This decreases specific internal review debt; it does not create external/human/formal review or prove the whole prior chain anew.

**Usefulness:** the object/domain normalization needed for a future width1/100 lambda_sigma(1) certificate is better founded. The certificate itself remains NOT_TESTED: actual enclosed head/residual/complement data and a practical total error budget are absent.054's coarse N>exp15 and052's impractical printed mesh have not been improved or executed. Historical2003source/value matching remainsHOLD, donor source-specific Q compatibilityUNVERIFIED, receiver/admission unchanged, RHOPEN. Novelty and efficiency NOT_CLAIMED/NOT_MEASURED.

**Do not repeat** this same unchanged interface audit in the next cycle. It is completed internally. Next selection must name a concrete useful certificate mechanism with predicted dimensions and paid errors, or advance the neglected source/units dependency if no such mechanism is ready. The current next packet records that portfolio decision and finite recovery rule. No external message, donor mutation, source-estate execution or automation change occurred.

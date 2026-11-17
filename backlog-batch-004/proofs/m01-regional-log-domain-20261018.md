# Audited historical reading edition

**Current audited claim:** PROVED: On every bounded interval, finite literal regional 1/|x-y| energy is exactly supported first-log Fourier energy, with equivalent shifted norms. The displayed canonical multiplier plus bounded terms has that domain.

**Claim ceiling:** Defined literal integral and specified canonical multiplier; no historical-extension identification or fresh attribution of a source error.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle 023 — canonical and literal regional logarithmic-energy domains

**Verdict:** `PROVED` internally for the restricted functional-analytic statement that the *literal* regional `1/|x-y|` finite-energy space on a bounded interval equals the zero-extension `H^log` space, and for identifying the canonical Connes–Consani/Suzuki domain with `H^log`. This is a source-level discrepancy with one sentence in Suzuki §3.1, not a claimed novel theorem, a verdict on Bombieri's entire 2003 theorem, sector continuity, or RH. The historical extended-form comparison remains `HOLD` pending direct original-text and independent expert review.

## Fixed object and primary evidence

Fix `a>0`, `I=(-a,a)`, and `lambda=e^a`. Connes–Consani use a multiplicative half-density `F in L²([lambda^-1,lambda],du/u)`; the unitary logarithmic coordinate map on **that** space is `v(t)=F(e^t)`. For Bombieri's older `f in L²(dx)`, the corresponding map is `Uf(t)=e^{t/2}f(e^t)`, as established separately in the [cycle-020 core bridge](m01-bombieri-suzuki-core-20261017.md). We use Suzuki's additive `v` and its unnormalized Fourier transform `vhat(z)=integral_I e^{-izt}v(t)dt`; Fourier sign has no effect on the norm. Distinguishing `F` from `f` is essential to the normalization.

[Connes–Consani, *Spectral triples and ζ-cycles* (2023)](https://ems.press/content/serial-article-files/44477?nt=1), PDF pp. 10–13, was read directly on 2026-10-18. Proposition 2.1, equation (2.11), defines a lower-bounded lower-semicontinuous localized form as an archimedean Fourier multiplier `2 theta'(z)/(2 pi)` plus a rank-two term and a **finite** sum of bounded self-adjoint prime operators. Its proof explicitly shows those corrections are bounded on the fixed interval and `theta'` is lower bounded with logarithmic growth. Lemma 2.2 proves Laurent polynomials in `U(u)=u^{i pi/log lambda}` are a form core; Proposition 2.3 gives the lower-semicontinuous core infimum formula. This corrects the earlier informal citation that attributed the core statement itself to Proposition 2.3; the proof is Lemma 2.2.

[Suzuki arXiv:2606.09096v3](https://arxiv.org/html/2606.09096), equations (2.3), (2.6), (2.8) and §3.1, was checked on 2026-10-18. Its `(2.8)` expresses the same form as `(2 pi)^-1 integral (log|z|-log(2 pi))|vhat(z)|² dz` plus an `a`-dependent bounded L² correction. The negative `log|z|` singularity near zero is integrable for compactly supported L² vectors because their Fourier transforms are bounded. These are source formulas, not a new Weil result.

## Exact restricted derivation and adversarial checks

Let `H^log(I)={v in L²(I): integral_R (1+log⁺|z|)|vhat(z)|² dz<infinity}`. In Connes–Consani's (2.11), write the form `Q=Q_infty+B_a`, where `B_a` is bounded self-adjoint on L² for each fixed `a`. A bounded perturbation has the same finite-value domain as `Q_infty`. The real multiplier `m(z)=2 theta'(z)` is bounded below and, from the standard gamma/digamma asymptotic used in Suzuki (2.8), satisfies `m(z)=log|z|+O(1)` as `|z|→infinity`. Consequently for a sufficiently large constant `C_a`, `m(z)+C_a` is comparable above and below to `1+log⁺|z|` for all real `z`. Plancherel gives the exact set equality

`D(Q_W^a)=H^log(-a,a)`

under the Connes–Consani/Suzuki canonical *closed-form* convention, for each fixed `a>0`. The graph norms are equivalent. This conclusion is already implicit in their formulas and is **not claimed novel**. It strengthens the one-sided inclusion recorded from Suzuki §3.1 in cycle 022, but does not retroactively identify a different historical extension.

Controls: (1) on bounded frequencies `m+C_a` is positive after shifting, so no `+infinity-infinity` cancellation is used; (2) the finite prime sum and rank-two term cannot enlarge the form domain; (3) the constant/interval indicator belongs to `H^log`, consistent with Connes–Consani's Laurent-polynomial core and Suzuki's operator-domain statement; (4) `H^log` is still a proper subset of all L² by the cycle-022 modulated-bump proof.

## Independent direct check of the literal regional condition

This is an adaptation of the frozen packet, documented before the confirmatory check (historical local record; not distributed here). Scale any bounded interval to `(0,1)`; the regional double integral changes by a positive constant and its finite-value space is unchanged. For `v in L²(0,1)` set

`R(v)=integral_(0,1)^2 |v(s)-v(t)|²/|s-t| ds dt`,

`B(v)=integral_0^1 |v(s)|²[log(1/s)+log(1/(1-s))]ds`.

**Boundary Hardy estimate.** For `0<s<1/16`, integrate `|v(s)|² <= 2|v(s)-v(t)|²+2|v(t)|²` over `sqrt(s)<t<1/2` against `dt/t`. Here `t>s`, `1/t <=1/(t-s)`, and `integral_(sqrt(s))^(1/2) dt/t = (1/2)log(1/s)-log 2 >= (1/4)log(1/s)`. Tonelli then gives

`(1/4) integral_0^(1/16) |v(s)|² log(1/s) ds <= 2R(v)+2 integral_0^(1/2) |v(t)|² min(t²,1/16)/t dt <= 2R(v)+||v||²`.

Reflect `s↦1-s` for the other endpoint; on the middle interval the logarithms are bounded. Therefore `B(v) <= C[R(v)+||v||²]` for an absolute finite `C`. This argument uses only nonnegative integrands and applies to arbitrary complex L² representatives, without traces or smooth approximation. It specifically rejects the attempted near-boundary-spike attack: any spike that makes the boundary-log term infinite must also make `R` infinite.

**Separate Fourier check.** Extend `v` by zero to the line and set `T(v)=integral_|h|<1 ||v(·+h)-v(·)||²_{L²(R)} dh/|h|`. Tonelli and splitting pairs inside `(0,1)` from crossing each endpoint give the exact identity `T(v)=R(v)+2B(v)`. The boundary-crossing integral at `s` is `integral_s^1 dr/r=log(1/s)` on the left and `log(1/(1-s))` on the right; both ordered directions account for the factor 2. Plancherel gives

`T(v)=(1/2pi) integral_R 4 J(|z|)|vhat(z)|² dz`, where `J(r)=integral_0^r (1-cos u)du/u`.

For `r>=1`, `J(r)=log r+O(1)` because `integral_1^r cos(u)/u du` is uniformly bounded by integration by parts. For `0<=r<=1`, `J` is finite and nonnegative. Thus `1+J(|z|)` is comparable to `1+log⁺|z|`; by Plancherel, `T(v)<infinity` iff `v in H^log(0,1)`. Since `R<=T=R+2B<=C'(R+||v||²)`, we obtain the exact set equality and equivalent graph norms

`{v in L²(I): R_I(v)<infinity}=H^log(I)=D(Q_W^a)`

for the literal bounded-interval regional integral printed in Suzuki §3.1 and the canonical closed form, after affine scaling. The equality of **finite-value sets** does not itself establish equality of two different quadratic-form *values* or historical extension rules.

The factors also match Suzuki's displayed (2.3): for `x=a(2s-1)`, `a²-x²=4a²s(1-s)`. Writing `R_phys`, `B_phys`, and `T_phys=R_phys+2B_phys` with the physical `dx` measure gives `L_a(v)=(1/4)T_phys(v) - (1/2)log(4a²)||v||²`. This is an identity between the **explicit local expression** and the truncated translation energy, not an identification of Bombieri's historical extension.

Adversarial canaries: a constant has `R=0` but `B<infinity`, so no false zero-trace condition entered; the interval indicator has finite Fourier log energy; a high-frequency compactly supported bump has both energies growing logarithmically and does not imply all-L² finiteness. A more severe attempted boundary witness, `v(s)=1/(sqrt(s)log(e/s))` near zero with a bounded cutoff, is L² but has divergent `B` (`integral ds/[s log(e/s)]`), so the Hardy estimate forces its `R` to diverge too. The proof is analytic; there is no numerical tolerance or finite-grid extrapolation. The two routes share the same mathematical model, so they are a cross-check of algebra, not independent human review.

## What remains held

Suzuki §3.1 says a regional-only domain implicit in Bombieri's 2003 Theorem 5.1 is “slightly larger” than the canonical domain. The exact Hardy/Fourier check above contradicts that **literal strict set inclusion** for the printed integral on a bounded interval. It may expose a missing qualification, a different extension convention, or a source error; we do not silently correct Suzuki or infer what Bombieri intended. Wiley's [publisher record](https://onlinelibrary.wiley.com/doi/10.1002/cpa.10089) confirms the 2003 paper and DOI, but its PDF redirected to the abstract in this run. The frozen volume candidate register had no filename/text-title hit for that 2003 original. The exact wording of Bombieri's theorem, his historical extended-value convention, equality of full quadratic-form values and parity sector infima, and sector continuity remain `HOLD`. **Next:** obtain the 2003 original and seek independent mathematical scrutiny of the displayed Hardy estimate and any differing domain definition before promoting a historical correction. No source estate was edited or executed; no external contact occurred.

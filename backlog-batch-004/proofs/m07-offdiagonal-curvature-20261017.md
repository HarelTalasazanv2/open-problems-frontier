# Audited historical reading edition

**Current audited claim:** CERTIFIED_RANGE: For p=1/10 and q=9/10 on the stated scalar-minimizer bracket, the defined off-diagonal coefficient C lies strictly between 4685/10^6 and 4690/10^6.

**Claim ceiling:** Local specified real family only; no universal matrix inequality or separation.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M07: positive off-diagonal curvature at a biased scalar optimizer bracket

**Verdict:** `CERTIFIED_RANGE` internally for one restricted second-order coefficient: for `p=1/10`, `q=9/10`, `L=I−E_π`, and every `r ∈ [68809/8192, 1100945/131072]`,

`4685/10^6 < C(r) < 4690/10^6`, where `Q(r,t)=Q(r,0)+C(r)t²+O_r(t⁴)` for `A=diag(r,1)`, `B(t)=[[1,t],[t,1]]` and `Q=I/(2D)`.

The exact rational interval output is approximately `[0.00468588703170165617, 0.00468908656896080000]`. This is an inwardly simplified *statement* from outward exact bounds, not a decimal certificate. The frozen packet (historical local record; not distributed here) fixes the inputs, decision rule and limits. The claim is internal and unreviewed by a human; no novelty assertion is made. Its application **at the unique scalar minimizer** is conditional on the cycle-015 internal global-uniqueness proof and cycle-016 optimizer bracket, both pending human review. It does not determine the complete constant or settle [Gao et al. 2025, Problem 6.4](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/complete-positivity-order-and-relative-entropy-decay/7270B6BBA7891B612C00FAB066F1A380).

## Exact derivation and domain

For `r>1`, `|t|<1`, both inputs are positive definite. Put `a=pr+q`, `λ±=(a+1±√((a−1)²+4q²t²))/2` and `F_B=(1+t)log(1+t)+(1−t)log(1−t)`. With an unnormalized matrix trace (whose common scaling cancels in `Q`),

`D=pr log r+qF_B−λ+log λ+−λ−log λ−` and

`I=pq[(r−1)log r+F_B−(r+1)log(1−t²)/2]`.

The second formula follows independently from `I=pq tr[(A−B)(log A−log B)]`: `tr(A log B)=(r+1)log(1−t²)/2` and `tr(B log A)=log r`. At `t=0`, `B=I` and `D₀=pr log r−a log a`, `I₀=pq(r−1)log r`, exactly the prior scalar quotient. Since `a>1`, eigenvalues are distinct and positive at zero; matrix logarithms and the quotient are even analytic in a neighborhood of zero. Direct perturbation gives `F_B=t²+O(t⁴)`, `λ+=a+q²t²/(a−1)+O(t⁴)`, `λ−=1−q²t²/(a−1)+O(t⁴)`. Thus `I₂=pq(r+3)/2`, `D₂=q−q² log(a)/(a−1)`, and `C=(I₂D₀−I₀D₂)/(2D₀²)`.

## Certificate and adversarial checks

The new OPF-owned checker (historical local record; not distributed here), SHA-256 `5d9b64dbbdc286bc80104e4866f597f3815745cb9ee5df93ee2967bbfb7965f3`, uses exact `Fraction` interval operations; 80 positive atanh-series terms bound logs at the rational `r,a` endpoints, with upper tail `2z^(2N+1)/((2N+1)(1−z²))`. It proves `D₀>0`, strict numerator positivity and the displayed coarse rational enclosure. The lossless rational result (historical local record; not distributed here), SHA-256 `39e5dc834694b9ed0b1df837ce2beb77c425999e7166aee7b1344078cbfd2d0b`, records each interval. Reproduce with `python3 artifacts/m07_offdiagonal_curvature_2026-10-17/certify_curvature.py > /tmp/opf_curvature_replay.json` and byte-compare to the saved result under ordinary Python 3.9.6. No source-estate code was executed.

Controls in the actual checker cover a hand-derived one-term `log 2` bound, asymmetric signed subtraction/product and positive division, rejection of `r=1`, a certified **negative** curvature interval near `r=4`, and two isolated wrong-formula probes (wrong `I₂` sign and wrong `D₂` sign), both rejected by the positive-curvature verdict. A 70-digit Decimal finite difference at `r=42/5`, `t=10^-4` gives about `0.0046905024`; it is diagnostic only, not an outward bound. These checks do not constitute an independent derivation or human review.

The positive coefficient and analytic evenness imply an **existential** small `|t|` neighborhood in this particular family where `Q(r*,t)>Q(r*,0)` if `r*` is in the certified bracket. No explicit `δ`, uniform fourth-order remainder, or finite-`t` exclusion was certified. This local direction cannot exclude other perturbations, noncommuting matrices, complex Hermitian states, higher ancillas or a matrix witness below the scalar lower bound. The strict separation test remains `upper(Q_matrix)<lower(alpha_1)` for the same chain and normalization; no such witness exists in this cycle.

**Prior art/status:** On 2026-10-17 the official Gao et al. page surfaced Problem 6.4 in search, but the direct page-open exceeded the web fetch limit; its previously read official PDF controls the exact normalization. [Zhao's August 2026 primary paper](https://arxiv.org/abs/2608.23482) proves sharp CMLSI for circle and torus heat semigroups, not a general two-state answer. A bounded search did not verify a universal closure or the novelty of this elementary local coefficient. Current universal status remains `RECHECK_INCONCLUSIVE`.

**Next discriminating action:** derive a quantitative fourth-order remainder on a small explicit `t` domain if this family remains valuable. Since the curvature is positive at the scalar optimizer, prioritize a mechanism that varies the matrix spectrum or a different noncommuting direction before another finite grid. No 2× method improvement was measured.

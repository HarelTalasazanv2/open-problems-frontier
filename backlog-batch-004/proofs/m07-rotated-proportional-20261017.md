# Audited historical reading edition

**Current audited claim:** CERTIFIED_RANGE: For the stated biased two-point bracket, the exact coefficient H=(r+1)d-(r/a)i lies strictly between 9/10 and 91/100, hence the specified local rotation direction is positive.

**Claim ceiling:** Specified local family; historical C034 recovery factor error is recorded in ERRATA, not adopted.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M07: infinitesimal rotation of proportional non-flat two-state matrices

**Verdict:** `CERTIFIED_RANGE` internally for a restricted sign: with `p=1/10`, `q=9/10`, `L=I−E_π`, every `r∈[68809/8192,1100945/131072]` satisfies `9/10 < H(r) < 91/100`, where

`a=pr+q`, `d=pr log r−a log a`, `i=pq(r−1)log r`, `H=(r+1)d−(r/a)i`.

Consequently, for every fixed `s>1`, the first-order coefficient of `u=sin²θ` in the quotient `Q(u)=I(u)/(2D(u))` is strictly positive when `B=diag(s,1)` and `A(u)=rR(θ)BR(θ)^T`. This is an internally checked local fact, not a finite-rotation inequality, a complete-constant comparison, universal M07 solution, or novelty claim. Applying it at the scalar optimizer is conditional on the cycle-015 internally proved, externally unreviewed uniqueness theorem and cycle-016 optimizer bracket. Frozen packet (historical local record; not distributed here).

## Exact convention and derivation

Use unnormalized trace, with `E=pA+qB`, `D=p tr(A log A)+q tr(B log B)−tr(E log E)` and `I=pq tr[(A−B)(log A−log B)]`. The quotient is invariant under common positive scaling, so a global density normalization can be imposed. At `u=0`, `A=rB`, and both channels contribute the same scalar ratio: `D(0)=(s+1)d`, `I(0)=(s+1)i`. All matrices are positive definite for `r,s>0`; on this bracket `r>1`, `d>0`.

For `u=sin²θ`, direct trace expansion gives exactly

`I(u)=pq[(r−1)(s+1)log r+(r+1)(s−1)u log s]`, so `I_u(0)=pq(r+1)(s−1)log s`.

Independently, `tr E=a(s+1)` and `det E=a²s+prq(s−1)²u`. Because the two eigenvalues at zero are `as` and `a`, their derivatives are `−prq(s−1)/a` and `+prq(s−1)/a`. Differentiating `tr(E log E)` yields `D_u(0)=prq(s−1)log s/a`. Thus

`Q_u(0)=pq(s−1)log(s) H(r)/[2(s+1)d(r)²]`.

For every `s>1`, the prefactor outside `H` is positive. Matrix eigenvalues and the quotient are analytic in `u` near zero for each fixed `r>1,s>1`, since the zero eigenvalues of `E` are distinct and positive and `D(0)>0`. Therefore positive `Q_u(0)` gives an existential small positive-u rise for each fixed pair. No explicit neighborhood or uniform remainder in `s` has been certified.

## Exact certificate and hostile checks

The new OPF-owned checker (historical local record; not distributed here), SHA-256 `889522e8da77a37563d9c19b9cf891bf89f77a3117a742daade24b6c42d78e75`, uses only Python `Fraction` for the decisive bounds. Each log on the narrow rational `r,a` interval is enclosed by 80 positive atanh-series terms and the explicit upper tail `2z^(2N+1)/[(2N+1)(1−z²)]`. The lossless result (historical local record; not distributed here), SHA-256 `c5d3b8beab423600b3743f7a40c08721357c1151a61e9954223cf7687e35beb4`, records full exact rational intervals; display only: `H≈[0.9022467060014253,0.9023057569312694]` and `d≈[0.8238803222891860,0.8238838943988734]`. Reproduce in OPF with ordinary `python3 artifacts/m07_rotated_proportional_2026-10-17/certify_rotation.py > /tmp/opf_rotation_replay.json`, then byte-compare with the saved JSON. Do not run under `python -O`, because assertions enforce the controls.

Adversarial checks exercised a hand-derived one-term `log 2` interval, signed subtraction/product, positive interval division, invalid `r` boundaries, and an omitted-leading-term fault that returns strictly negative `H`. The algebraically equivalent expression `H=(pr/a)[pr(r+1)+2q]log r−(r+1)a log a` was cross-checked at rational probes. A separately coded 80-digit Decimal spectral calculation at `r=42/5,s=2,u=10^-6` gave a finite-difference coefficient about `0.01382219655`, versus the predicted local coefficient about `0.01382219609`; this is a diagnostic, not a rigorous remainder or independent mathematical review. The first run failed before output because it passed a `Fraction` to `Decimal`; after explicit rational conversion, the complete checker replay passed. The failure was an implementation issue in the diagnostic path, not evidence against the sign, and it is preserved in cycle 018 report (historical local record; not distributed here).

**Source/status gate:** On 2026-10-17, [Gao et al.'s official 2025 article](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/complete-positivity-order-and-relative-entropy-decay/7270B6BBA7891B612C00FAB066F1A380) still displays Problem 6.4 in a bounded search. [Zhao's August 2026 primary paper](https://arxiv.org/abs/2608.23482) was opened; it proves a sharp circle/tori special case. This search neither establishes current universal openness exhaustively nor screens originality of the local rotation lemma.

**Next obstruction:** A matrix separation requires a certified finite state with `upper(Q_matrix)<lower(α₁)` under the same normalization. Two successive positive local-curvature directions now reduce the case for further small-rotation work without a new mechanism. A general Hessian or an unequal-spectra finite witness would require a fresh analytic sign criterion, explicit admissibility and outward quotient bounds. Human review of the scalar uniqueness and local calculations remains outstanding. No 2× method gain was measured.

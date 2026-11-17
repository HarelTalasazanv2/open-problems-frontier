# Audited historical reading edition

**Current audited claim:** PROVED: The displayed L2(dx) logarithmic unitary sends linear inversion to reflection and the displayed dagger convolution to the additive autocorrelation; the two explicitly written core functionals then agree term by term.

**Claim ceiling:** Exact displayed conventions and smooth core only; no historical 2003 closed extension, current source availability, parity continuity or RH.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle 020: Bombieri–Suzuki core bridge, with the two starred operations separated

**Verdict:** `PROVED` internally for the exact identity on complex smooth compactly supported test functions stated below. This is a change of variables between source-defined forms, **not a novelty claim** or a proof of sector continuity or RH. The closed-form-domain bridge remains `INCONCLUSIVE`. Frozen attempt (historical local record; not distributed here).

## Primary definitions and provenance

Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I* (2000), [archival PDF](https://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0), printed pp. 186, 191, 193, 194–196, inspected as extracted text and, for pp. 191 and 193, rendered page images on 2026-10-17. The local read-only PDF is 53 pages with SHA-256 `20bd544fc5297766966630092aba4c1e10c6a7e663d14be89bbe1d0c8220b7fd`, previously matched to the archive download in cycle 019. The local file is an archival copy; source-estate contents were not executed or changed. Suzuki, [*Weil's quadratic form via the screw function*, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096), §§1.1 and 4.5, rechecked 2026-10-17. Suzuki's `W`, convolution, and tilde are displayed in introductory equations; the unrestricted continuity result is Theorem 1.3, not a published sector theorem in that paper.

The source uses **different operations**:

1. Bombieri's parity involution is linear: `S f(x)=x^{-1} f(1/x)` (p. 186).
2. The Hermitian quadratic test uses the conjugate of that involution: `f†(x)=overline{S f(x)}=x^{-1} overline{f(1/x)}` and multiplicative convolution `F=f *_m f†` (p. 191, rendered image; p. 193, rendered image). Its displayed integral is `F(x)=∫_0^∞ f(xy) overline{f(y)} dy`. The PDF text extractor drops some overbars, so the page image is essential to this distinction.
3. Suzuki uses `H=G *_a tilde G`, `tilde G(t)=overline{G(-t)}` and `Q_W(G)=W(H)` (v3 introductory equations).

The imported corrected A242 manuscript mistakenly made operation 1 antilinear. Cycle 019 falsified that manuscript's printed ordinary-parity identification; it did **not** falsify operation 2 or the repaired source-level bridge here.

## Exact core statement and proof

Let `f∈C_c^∞((0,∞); C)` and define `G(t)=U f(t)=e^{t/2} f(e^t)`. Let `T` be Bombieri's p. 186/p. 193 explicit-formula functional and `W` Suzuki's v3 introductory explicit-formula functional, with Euler's constant `γ=C₀`. Then

`U(f *_m f†)=G *_a tilde G`, hence `T[f *_m f†]=W[G *_a tilde G]`, and `||f||²_{L²(dx)}=||G||²_{L²(dt)}`.

Moreover `U(S f)(t)=G(-t)`. Thus the *linear* Bombieri `S f=±f` core sectors are exactly Suzuki's ordinary even/odd core sectors. Support in `[e^{-a},e^a]` maps to `[-a,a]`; compactly supported smooth functions strictly inside those intervals map both ways.

Proof of the convolution identity: directly `U(f†)(t)=overline{G(-t)}=tilde G(t)`. Set `x=e^r`, `y=e^s` in Bombieri's p. 191 integral. Since `f(e^u)=e^{-u/2}G(u)`,

`F(e^r)=∫ f(e^{r+s}) overline{f(e^s)} e^s ds=e^{-r/2}∫G(r+s)overline{G(s)}ds=e^{-r/2}(G*_a tilde G)(r)`.

To check `T[F]=W[H]` without assuming it from a label, put `F(e^t)=e^{-t/2}H(t)` in each term of Bombieri's displayed explicit formula:

| Term | Exact transformed term |
|---|---|
| Two pole integrals | `∫_{R}H(t)(e^{t/2}+e^{-t/2})dt` |
| Prime symmetrization | `-Σ_{n≥1} Λ(n)n^{-1/2}[H(log n)+H(-log n)]` |
| Constant | `-(log(4π)+γ)H(0)` |
| Archimedean integral | `-∫_0^∞ [e^{t/2}(H(t)+H(-t))-2H(0)]/(e^t-e^{-t})dt` |

The last row equals Suzuki's displayed `-∫_0^∞[H(t)+H(-t)-2e^{-t/2}H(0)]e^{t/2}/(e^t-e^{-t})dt`. All changes of variables are legitimate for these smooth compact supports. The norm and parity identities follow directly from `dx=e^t dt` and `S f(e^t)=e^{-t}f(e^{-t})`.

## Adversarial checks and claim ceiling

- **Conjugation canary:** for nonzero real even `h∈C_c^∞`, `G=i h` gives `(G*_a tilde G)(0)=∫|G|²>0`; omitting the conjugate would give a negative value. The p. 191 and p. 193 page images visibly carry the overbar despite OCR loss.
- **Parity canary:** `G=i t h(t)` is odd under the *linear* `S` mapping, but fixed by the imported antilinear operation, reproducing cycle 019's exact counterexample. The repair is a new statement, not a retroactive validation of that packet.
- **Normalization canaries:** the prime coefficient is `Λ(n)/√n`; the archimedean subtraction is `2e^{-t/2}H(0)` inside Suzuki's bracket; `γ` and `C₀` denote the same Euler constant. No decimal approximation or finite search is used.

This proof establishes **core identity, core sector mapping, support, and L² normalization only**. It does not establish that Bombieri's full `L²([M^{-1},M])` form domain equals Suzuki's closed form domain, that the parity projections preserve both closures, or that the infima have identical admissible classes. Those are the first unresolved dependencies for using Suzuki v3's fixed-domain argument to repair A242. The two newly read local audit/proof files are leads, not primary sources or human review; the latter's final identification cites the faulty notation ledger and cannot be adopted unchanged. The source-level core identity is an algebraic restatement of published formulations; novelty is not asserted. No 2× method improvement was measured.

**Next discriminating test:** compare the closures/core density and exact localized admissible classes under `U`, then restrict Suzuki v3's lower and upper semicontinuity arguments to both parity sectors if the domains match. If either closure fails, exhibit a boundary or form-norm counterexample. A fresh packet is required for this next step.

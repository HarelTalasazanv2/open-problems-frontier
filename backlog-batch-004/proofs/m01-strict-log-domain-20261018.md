# Audited historical reading edition

**Current audited claim:** PROVED: For every bounded nonempty interval, supported first-log Fourier energy defines a Hilbert space properly contained in L2; the interval indicator has finite energy.

**Claim ceiling:** No historical Weil-form identification or RH conclusion.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle 022 — finite logarithmic energy is a proper localized domain

**Verdict:** `PROVED` internally for the narrow functional-analysis statements below; `HOLD / INCONCLUSIVE` for the proposed equality of Bombieri's entire L² variational interpretation and Suzuki's canonical closed form. This is a source-level domain audit, not a novel result, sector-continuity theorem, positivity result, or RH proof. No external human review or formal verification occurred.

## Frozen question and sources

The packet (historical local record; not distributed here) fixes `a>0`, `I=(-a,a)`, zero extension outside `I`, the complex L² norm, and `Uf(t)=e^{t/2}f(e^t)`. Bombieri, *Remarks on Weil's quadratic functional I*, [archive PDF](https://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0), printed pp. 193–198, was checked on the read-only archived PDF of SHA-256 `20bd544fc5297766966630092aba4c1e10c6a7e663d14be89bbe1d0c8220b7fd` on 2026-10-18. Its Problem 2 says minimize on the unit sphere of compactly supported `L²(E)`; Lemma 3 writes the digamma-weight Fourier formula for compact-support `L²`, and Theorem 3's minimizing sequence has bounded `1+log⁺|v|` Fourier energy. The passage does not explicitly say that every `L²` vector has a *finite* quadratic value.

[Suzuki arXiv:2606.09096v3](https://arxiv.org/html/2606.09096), dated 2026-09-23 and checked 2026-10-18, §§1.1, 2.3–2.4, 3.1–3.2, defines a lower-bounded closed localized form `Q_W^a` with finite-value domain `D(Q_W^a)⊂L²(I)`; §3.1 states `D(Q_W^a)⊂H^log(I)` for the logarithmic Fourier space below. Its (2.8) gives the leading log Fourier integral plus an `a`-dependent bounded L² remainder. Suzuki also says that an implicit regional-difference-quotient domain in Bombieri's 2003 Theorem 5.1 is *slightly larger* than the canonical closed domain; that comparison is source-reported here, because the 2003 original and a strict witness were not checked. Suzuki's Theorem 1.1 and §3.2 give a compactly supported smooth form core, subject to its cited Connes–Consani core input. [Clay](https://www.claymath.org/millennium/riemann-hypothesis/) still labels RH unsolved on 2026-10-18, a bounded status check.

## Exact restricted proof and controls

Set `H^log(I)={v∈L²(I): ∫(1+log⁺|z|)|v̂(z)|² dz<∞}`, with `v̂(z)=∫_I e^{-izt}v(t)dt`. By Plancherel, this weighted Fourier norm makes `H^log(I)` a Hilbert space: a Cauchy sequence converges in weighted Fourier L² and ordinary L², and its L² limit retains support in `[-a,a]` (the a.e. endpoint convention is immaterial).

**Strict inclusion:** Suppose `H^log(I)=L²(I)` as sets. The identity from the weighted Hilbert space to L² is continuous and bijective, so the bounded inverse theorem would give `||v||_{H^log}≤C||v||₂`. Fix nonzero `φ∈C_c^∞(I)` and put `v_N(t)=e^{iNt}φ(t)`. Its L² norm is fixed. Choose `R>0` with `c=∫_{|ξ|≤R}|φ̂(ξ)|²dξ>0`. Since `v̂_N(z)=φ̂(z-N)`, its weighted norm squared is at least `c[1+log(N-R)]` for `N>R+1`; this contradicts the inverse bound. Thus `H^log(I)` is a **proper** subset of compact-support L². This proves existence of L² vectors with infinite logarithmic energy, not an explicit named vector. The argument uses no zero hypothesis or numerical approximation. It also catches the false shortcut that Bombieri's phrase “over L²” means every vector has finite energy.

**Boundary canary:** `v=1_I` has `v̂(z)=2sin(az)/z` (with the continuous value `2a` at zero). Its `log⁺`-weighted energy converges because the tail is bounded by a constant times `∫_1^∞log z/z² dz`; the near-zero Fourier transform is bounded. Suzuki §1.2 explicitly states constants belong even to `D(A_a)`. Under `U^{-1}`, this is `f(x)=x^{-1/2}1_{[e^{-a},e^a]}(x)`, an L² function with nonzero endpoint traces. Hence a blanket `H_0^1` boundary condition would discard an admissible closed-form vector. This is a check of the domain, not a minimizer or eigenvalue claim.

**Low-frequency canary:** every compact-support L² function is L¹, so `v̂` is bounded. The negative part of `log|z|` on `|z|<1` is integrable against `|v̂|²`; no cancellation of `+∞` and `-∞` is needed. The prime/pole terms on fixed compact support are bounded quadratic corrections per Bombieri Lemma 3 and Suzuki (2.8), so the obstruction is the high-frequency positive log energy. A finite grid or smooth-only approximation could miss it.

## Adversarial result and exact remaining bridge

The previous smooth-core identity and Suzuki parity core do **not** alone specify Bombieri's historical extension on every L² input. Bombieri's Lemma 3 and Theorem 3 strongly suggest the finite-energy convention, but the text viewed does not explicitly identify its full extended-value domain and sector Rayleigh infima with Suzuki's canonical closed form. Suzuki's 2003-domain caution is a further reason to require an explicit extension theorem instead of inferring equality from notation. The `H^log⊊L²` proof rules out literal all-finite L² but does not prove or disprove `D(Q_W^a)=H^log(I)`, and does not provide a strict witness for the source-reported 2003 regional-domain gap. The attempted full-domain identification is therefore **HOLD**, not a falsification of sector continuity.

**Next discriminating action:** inspect Bombieri's 2003 Theorem 5.1 and Connes–Consani's canonical form-domain/core proposition from primary originals. Freeze a proposed equality as an extended lower-semicontinuous form, including the boundary logarithm in Suzuki (2.3); either prove uniqueness of the closure under `U` or exhibit a precise finite-energy-domain mismatch. Only then identify parity sector infima and address continuity.

## Reproducibility and independence

The strictness proof uses only Plancherel, the bounded inverse theorem and an explicit modulated smooth bump; the boundary check is the elementary Fourier integral above. No code, data, random seed, error bound, 2× comparison, external contact or publication was used. Bombieri pages were read from the previously hashed PDF; this was a reread for source verification, not new corpus-path coverage. The local pass-025 register (historical local record; not distributed here) covers a separate previously unread packet text, which is not independent primary authority. The two primary formulas and OPF derivation share the Weil quadratic model; agreement is not an external review.

# Audited historical reading edition

**Current audited claim:** PROVED: A common eventual exponential rate for positive self-correlations on a norm-dense excited family is equivalent to the stated spectral gap.

**Claim ceiling:** Full vacuum projection, positivity, common rate and infinite-time control are essential; no finite-observation inference.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M06: dense positive temporal correlations and the spectral gap

Cycle095, 2026-10-29 UTC. **PROVED internally at the stated abstract operator scope.** The common rate is essential; common amplitudes and common starting times are unnecessary. Exact counterexamples refute removing density, removing the common rate, or replacing the infinite-time assertion by a finite observation window.

Claim ceiling: a criterion for one already specified nonnegative self-adjoint operator, with positive temporal self-correlations on a dense excited family. No Yang–Mills construction, continuum limit, empirical mass estimate, novelty, external expert review or formal verification is established.

The frozen attempt (historical local record; not distributed here) follows the 094 packet (historical local record; not distributed here). It does not assume the conclusion of the094 gap-transfer theorem. The standard spectral theorem, including its scalar positive measures and bounded functional calculus, is an imported foundation. All deductions below are analytic; no numerical certificate, grid or research executable was used.

## 1. Exact theorem and conventions

Let H be a densely defined nonnegative self-adjoint operator on a complex Hilbert space ℋ. Write E for its spectral resolution, P=E({0}), Q=I−P, and fix δ>0. Let D⊂Qℋ be norm dense in Qℋ. It need not have a common operator domain: e^{-tH} is bounded on ℋ for t≥0. For v∈ℋ put

\[
\mu_v(B)=\langle v,E(B)v\rangle,\qquad
C_v(t)=\langle v,e^{-tH}v\rangle
=\int_{[0,\infty)} e^{-t\lambda}\,d\mu_v(\lambda). \tag{1}
\]

The inner product is conjugate-linear in its first argument. The measure μ_v is finite and nonnegative, of total mass ||v||². In particular C_v(t) is a nonnegative real number, not a general signed or non-adjoint field correlation.

The following three conditions are equivalent:

1. spec(H)∩(0,δ)=∅.
2. For all t≥0, ||e^{-tH}Q||≤e^{-δt}.
3. For every v∈D there exist finite A_v≥0 and T_v≥0 such that, for every real t≥T_v,
   \[
   C_v(t)\le A_v e^{-\delta t}. \tag{2}
   \]

The rate δ is the same for the entire family. Neither A_v nor T_v has to be bounded uniformly over D. The interval (0,δ) is open; spectrum at δ is permitted, including continuous spectrum. P and Q may be zero. No nonzero vacuum, unique vacuum or nontrivial excitation is a conclusion of this criterion alone.

### Proof

Conditions1 and2 are equivalent by spectral calculus on Qℋ: the vacuum spectral atom has been removed, and the remaining support is in [δ,∞) exactly when the positive exponential has the stated norm bound. In the reverse direction, positive spectral mass in (0,a] for any 0<a<δ would violate that norm bound. For Q=0 the norm is0 and both assertions hold.

Condition2 implies3 with A_v=||v||² and T_v=0. To prove3⇒1 without introducing any uniform-prefactor assumption, fix v∈D and 0<a<δ. If c=μ_v((0,a])>0, positivity in(1) gives

\[
C_v(t)\ge c e^{-at}\quad(t\ge0).
\]

Combining with(2) would give c e^{(δ−a)t}≤A_v for every t≥T_v. The left side tends to infinity and A_v is finite, a contradiction. Thus μ_v((0,a])=0. Letting a increase to δ yields

\[
E((0,\delta))v=0\quad\text{for every }v\in D, \tag{3}
\]

because ||E(B)v||²=μ_v(B). The spectral projection E((0,δ)) is bounded. It therefore annihilates the closure Qℋ of D. It also annihilates Pℋ because its spectral set excludes0. Hence E((0,δ))=0 on ℋ, which is condition1 for a self-adjoint operator. This is the full-domain argument; no finite vector list is substituted for density. ∎

There is no interchange of a vector-dependent threshold with a supremum over vectors. Each v is treated first, then a bounded projection extends its vanishing to the closure. A_v=0 for a nonzero v would itself be impossible, since C_v(t)>0 at every finite t for a nonzero positive spectral measure. For v=0 the condition is automatic. If Q=0 the theorem is vacuous about excited states, as it should be.

## 2. Independent formulation: the exact asymptotic spectral edge

For any nonzero v∈ℋ define β_v=inf supp μ_v. This is a finite number in [0,∞): a nonzero finite measure on [0,∞) has a nonempty support and some bounded interval with positive mass. Then

\[
\lim_{t\to\infty}-\frac1t\log C_v(t)=\beta_v. \tag{4}
\]

Indeed support above β_v gives C_v(t)≤||v||²e^{-β_vt}. For every ε>0 the definition of the support edge gives c_ε=μ_v([β_v,β_v+ε])>0, even if there is no atom at β_v. Thus

\[
c_\varepsilon e^{-(\beta_v+\varepsilon)t}
\le C_v(t)\le\|v\|^2e^{-\beta_vt}.
\]

After taking −log and dividing by t>0,

\[
\beta_v-\frac{\log\|v\|^2}{t}
\le -\frac{\log C_v(t)}{t}
\le\beta_v+\varepsilon-\frac{\log c_\varepsilon}{t}.
\]

First t→∞ and then ε↓0 proves(4). Consequently condition3 can equivalently be replaced by β_v≥δ for every nonzero v∈D. Conversely β_v≥δ supplies(2) with ||v||² and0. Formula(4) is an exact infinite-time statement, not a justification for extracting a gap from a finite fitted slope.

This support-edge derivation cross-checks the positive-low-mass contradiction by a second formulation. Both use the same spectral theorem and were constructed within one exposed internal review. They are not blind reproduction, an independent implementation, a separate human review or formalization.

## 3. Exact negative controls and endpoint coverage

### A. A positive rate for every vector can coexist with no gap

On ℓ²({0,1,2,…}), define H e0=0 and H e_k=k^{-1}e_k for k≥1. The operator is bounded, nonnegative and self-adjoint, P=|e0⟩⟨e0|, and positive spectrum accumulates at0. Let D be all finite-support vectors in Qℋ; it is norm dense there. For nonzero v∈D set

\[
\delta_v=\min\{1/k:v_k\ne0\}>0.
\]

Then C_v(t)=Σ_k|v_k|²e^{-t/k}≤||v||²e^{-δ_vt} for every t≥0. Every vector in this dense family has a positive rate, but no common positive lower rate exists and the full operator has no positive gap. **FALSIFIED:** replacing the common δ in the theorem by arbitrary δ_v>0 preserves its conclusion. Complex coefficients cause no cancellation in this self-correlation.

### B. A complete test of one finite sector can miss lower spectrum

For the same H and any fixed N≥1, let M_N=span{e1,…,eN}. For every v∈M_N, C_v(t)≤||v||²e^{-t/N}. Yet the global excited gap is0. In particular a single v=e1 has the exact correlation e^{-t}. **FALSIFIED:** the common-rate conclusion on one probe, or even all vectors of a fixed finite sector, certifies the full-space gap without density. This is an exact hidden-sector example, not failure of a numerical search.

### C. Every finite observation window is insufficient

Let ℋ=ℂe0⊕ℂe1⊕ℂe2 and H=diag(0,1,1/2). For any fixed finite T≥0 and all v∈Qℋ,

\[
C_v(t)\le\|v\|^2e^{-t/2}
\le \bigl(\|v\|^2e^{T/2}\bigr)e^{-t}
\quad(0\le t\le T). \tag{5}
\]

Thus even the full dense excited family admits a common apparent rate1 on the finite window with finite amplitudes; the true gap is1/2. A small hidden component also masks the slower tail with a fixed amplitude: let w=(1/2)e^{-T/2} and v=√(1−w)e1+√w e2. Then

\[
e^tC_v(t)=1-w+we^{t/2}\le3/2<2\quad(0\le t\le T),
\]

whereas e^tC_v(t)→∞ as t→∞. **FALSIFIED:** a finite-time bound alone establishes the corresponding asymptotic gap. No finite precision was involved; insufficient temporal coverage is the failure mode.

### D. Admissibility checks: adjoints and vacuum subtraction

In the preceding finite-dimensional example change the two excited energies to1/2 and put O=|e1⟩⟨e0|+|e0⟩⟨e2|. Then ⟨e0,Oe0⟩=0 and

\[
\langle e_0,Oe^{-tH}Oe_0\rangle=0,
\qquad
\langle Oe_0,e^{-tH}Oe_0\rangle=e^{-t/2}.
\]

A non-adjoint correlation need not be the positive self-correlation in(1). Its vanishing cannot license the self-correlation theorem. No statement about the source's spatial clustering is refuted by this temporal toy example.

If H=diag(0,0,1), Ω=e0 and O=|e1⟩⟨e0|+|e0⟩⟨e1|, then ⟨Ω,OΩ⟩=0 but OΩ=e1 lies in the full zero-energy subspace. Scalar centering against one chosen Ω does not ensure membership in Qℋ when the vacuum is degenerate. The theorem explicitly uses P=E_H({0}); unique-vacuum or full-projection matching is an additional input in any field application.

### E. Continuous spectrum and the included endpoint

Take ℋ=ℂΩ⊕L²([δ,δ+1],dλ), HΩ=0 and H acting by multiplication by λ on the second summand. For its unit constant vector v,

\[
C_v(t)=e^{-\delta t}\frac{1-e^{-t}}{t}\quad(t>0),\qquad C_v(0)=1.
\]

The gap edge δ is in continuous spectrum, not an eigenvalue, and the exact logarithmic decay rate is δ. The upper bound e^{-δt} and the theorem include this case. H=0 gives Q=0 and no nontrivial excited mass; all conclusions remain correctly vacuous.

## 4. Reconstruction source crosswalk and unresolved physical bridge

Exact source/version/read records (historical local record; not distributed here) distinguish the original cited papers, author overview, and the author-deposited algebraic paper. The source-route amendment (historical local record; not distributed here) preserves unsuccessful full-text routes; it does not replace missing original proofs with an overview.

The1975 publisher abstract confirms a correction of the earlier reconstruction work, but its checked route is subscription-preview only; the original1973 Euclid response was non-PDF. Their full proofs remain unaudited. The inspected Schlingemann v1 paper, [hep-th/9802035v1](https://arxiv.org/abs/hep-th/9802035v1), supplies a different algebraic framework: regularity and reflection positivity, a quotient by null vectors followed by Hilbert completion, a positive-energy semigroup, and a separate time-zero condition for its observable-net construction. Its cone-density/Poincaré results are source-reported here, not fully reproved. No claim that its Haag–Kastler formulation supplies every official Yang–Mills field/ultraviolet requirement is made.

In that framework the full quotient image is dense by construction; this does not make an arbitrary list of measured observables dense. Projecting a dense image by the correctly identified Q gives a dense excited family. Applying the theorem still requires actual positive temporal self-correlations with a single physical rate, correct adjoints, vacuum subtraction, and all-time asymptotic control. Neither reflection positivity nor regularity alone supplies a positive mass gap. Actual Yang–Mills functionals, reconstructed fields, cutoff/volume estimates, limiting nontriviality and full axioms remain **NOT_TESTED** by this run. The current [Clay owner](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) was checked2026-10-29 and labels Unsolved; this is bounded status reporting, not exhaustive literature coverage.

## 5. Adjudication, trust boundary and next test

| Claim | Outcome | Exact ceiling |
|---|---|---|
|M06-TEMPORAL-CRITERION-C095|PROVED|Equivalence1–3 for the specified H, full vacuum projection, common δ and norm-dense D.|
|M06-SPECTRAL-RATE-EDGE-C095|PROVED|Equation(4) for every nonzero finite positive scalar spectral measure of such H.|
|M06-VECTOR-RATE-SHORTCUT-C095|FALSIFIED|Replacing the common rate by arbitrary positive vectorwise rates, Section3A.|
|M06-NONDENSE-PROBE-SHORTCUT-C095|FALSIFIED|Promoting one finite sector's common rate to the full Hilbert space, Section3B.|
|M06-FINITE-WINDOW-SHORTCUT-C095|FALSIFIED|Replacing all-time asymptotics by a finite time window, Section3C.|
|M06-RECONSTRUCTION-SOURCE-C095|CERTIFIED_RANGE|Only the actual read contracts and source-route/correction distinctions; not full reconstruction or official-model equivalence.|
|M06-ACTUAL-CORRELATION-INPUT-C095|NOT_TESTED|No actual Yang–Mills dense observable family or common-rate continuum/cutoff/volume estimate is supplied.|

The uncertainty changed: uniform amplitudes and thresholds are unnecessary for the fixed-operator criterion, but a common rate, positivity, dense coverage and unbounded time are essential to this argument. The controls distinguish an actually false weakened hypothesis from finite temporal coverage and from applying the wrong correlator or projection. The criterion transfers to other nonnegative self-adjoint settings; it gives no percentage of progress toward Yang–Mills.

This is exposed internal analytic verification, sharing the spectral theorem and hypotheses between formulations. No independent external reviewer, blind reproduction, formal proof assistant or computational instrument was used. Custody/hash checks are separate record checks, not mathematical proof. Efficiency is NOT_MEASURED.

The single proposed continuation is the varying-quotient limit gate (historical local record; not distributed here), SELECTED_NOT_TESTED: formulate when converging positive forms on a common label space reconstruct a continuous limiting semigroup, retain a normalized vacuum, and carry uniform connected-correlation bounds despite changing Hilbert spaces. This addresses the actual missing varying-space mechanism left explicit in094 and the source construction; it must retain a time-regularity control and a nontriviality witness. It does not presume any actual gauge-field input.

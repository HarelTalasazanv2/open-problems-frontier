# Audited historical reading edition

**Current audited claim:** PROVED: A stationary full-rank positive-weight least-squares pair satisfying every reoptimized signed coordinate comparison gives modular margins at least half its leverage scores.

**Claim ceiling:** Sufficient certificate theorem; no universal certificate-generation or generic-norm assertion.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Hadwiger–Nelson scope audit and an exact matrix-avoidance certificate

**Source scope verified; full source theorem reproduction NOT_TESTED.** The2026 paper concerns a comeager set of norms, not every norm or the specified Euclidean norm. Its sharpness theorem gives a nonempty open family with a lower bound, not a lower bound for every typical norm throughout the norm space. The Euclidean plane problem remains **OPEN AS REPORTED** in its2026-09-28 introduction, with5≤χ≤7. A bounded primary-source search on2026-10-28 found no resolution; this is not an exhaustive literature search or a new proof of those bounds.

**PROVED internally:** a supplied stationary weighted least-squares pair satisfying all reoptimized one-coordinate comparisons gives a rigorous modular-avoidance certificate. The proof below requires neither a claim of global minimization nor an algorithm that finds such a pair. **FALSIFIED:** stationarity plus nearest-integer rounding alone implies the desired margin; two exact counterexamples include one with unique nearest integers. The paper itself uses stronger hypotheses, so these counterexamples do not refute its lemma.

**CERTIFIED_RANGE:** four specified positive rational certificates, a complete norm-specific K4 colouring, all22 main CLI dispositions and one separately frozen strict-rounding counterexample. No new Euclidean or generic-norm chromatic bound, universal certificate-generation method, novelty, external human review or formal verification is claimed.

## 1. Primary source, version and exact quantifiers

Noga Alon, Matija Bucić and James Davies, [*Hadwiger–Nelson Problem for Typical Norms*, arXiv2609.36220v1](https://arxiv.org/abs/2609.36220), submitted2026-09-28. The accepted [PDF](https://arxiv.org/pdf/2609.36220) has21 pages,583970 bytes, SHA-256 `c93b095812a73f0490107bf17d2a09b74d8718a1ca05736ee7b6bad2e7ccb547`. The owner abstract matches090 exactly; PDF/HTML/abstract are one publication, not independent mathematical corroboration. Exact extents (historical local record; not distributed here) distinguish full selected pages, partial reference lookups, parser limitations and full visual checks.

For a norm ν on R^d the unit-distance graph Gν has vertices R^d and edges {u,v} precisely when ν(u−v)=1. The chromatic number here permits arbitrary colourings; no measurable-colouring restriction is built into this graph definition or the paper's compactness argument. The Euclidean problem fixes d=2 and ν=||·||₂.

The paper identifies a norm with its compact convex origin-symmetric unit ball, with nonempty interior, and uses the Hausdorff metric. “Typical” means that the exceptional norms form a meagre set in this Baire space. It is not an unspecified probability distribution or a claim about every named norm.

The source states:

* Theorem1: for each positive integer d, a comeager set of norms satisfies χ(Gν)≤2d.
* Theorem2: for each d, there is a nonempty open set of norms satisfying χ(Gν)≥2d.

Their intersection gives norms with equality, and makes the generic upper bound unimprovable uniformly to a smaller integer. It does **not follow from those two quantifiers alone** that χ=2d is comeager in the whole norm space. As a logical countermodel, on the Baire space R let f=1 for x<0 and f=2 for x≥0. The universal upper bound f≤2 and a nonempty open set with f≥2 hold, but {f=2} is not comeager. This is a countermodel to an inference, not a counterexample norm to either source theorem. In the planar case, the additional source-reported lower bound4 for every norm yields typicalχ=4; the Euclidean lower bound5 explains why that specified norm is exceptional.

The old generic bound is2^d, while the new one is2d. pypdf flattens superscripts in places; full-page visual inspection of physical2 distinguishes them. A parser rendering both as “2d” cannot establish that there was no improvement.

Theorem3 is a full-spark real-matrix supremum bound, with attainment asserted for rational coefficients. Theorem4 is a lattice-zonotope covering-radius result under linear general position. These are source-reported statements, not newly proved here or automatically identical to every lonely-runner formulation. Their reported resolution of view-obstruction/covering-radius conjectures is not a reason to list those exact statements as unqualified open targets.

## 2. The exact missing links to the generic-norm conclusion

The source upper-bound route is:

1. A typical-norm structural statement from Alon–Bucić–Sauermann controls rational spans of finite non-antipodal unit directions.
2. Edmonds' matroid-partition criterion over **Q** partitions those directions into d rationally independent sets. The condition needed is |S|≤d·rank_Q(S) for every subset S.
3. Complete those sets to bases of their rational span, clear coordinate denominators, and apply the integer matrix-avoidance lemma.
4. Use half-open phase bins for each finite graph, then de Bruijn–Erdős compactness for the entire unit-distance graph.

The paper's N is the rational rank of the direction span and can exceed the ambient real dimension d; q=d is the number of basis families. Replacing rank_Q by an ordinary real-rank calculation in R^d would change the claim.

Its Proposition5 wording about “other” spanned vectors needs to be matched to the exact **total** cardinality bound in the original source before treating step1 as a locally audited dependency. If selected vectors were excluded from the count, the weaker bound would not immediately give the required d-partition. No mathematical error in that source has been demonstrated: this is a precise unresolved statement/crosswalk question. Reference[3] identifies the2025 journal paper *Unit and distinct distances in typical norms*; [arXiv2302.09058v2](https://arxiv.org/abs/2302.09058), revised2024-11-07, has matching authors/title but its body and equivalence to the journal statement were not read here. The next source gate (historical local record; not distributed here) resolves that exact input.

The new positive-certificate lemma below does not rely on genericity, matroid partition, balanced-weight existence, the full integer-avoidance induction, or graph compactness. Those are separate existence/coverage obligations. Reading a proof is not the same as independently reproducing every step of the21-page theorem.

## 3. A finite sufficient certificate, with complete analytic proof

Let A∈R^(m×N) have full column rank, with row vectors a_i^T. Let w_i>0, W=diag(w_i), β∈R^m, k∈Z^m, and x∈R^N. Define
\[
t=\beta+\tfrac12\mathbf1+k,\quad r=Ax-t,
\quad M=A^TWA,\quad
\lambda_i=w_i a_i^TM^{-1}a_i,
\]
\[
\Phi(x,k)=\sum_iw_i(a_i^Tx-\beta_i-\tfrac12-k_i)^2.
\tag{1}
\]
Assume stationarity A^TWr=0. For each i and σ∈{−1,+1}, put
\[
h_i=w_iM^{-1}a_i,\quad
x_{i,\sigma}=x+\sigma h_i,\quad k_{i,\sigma}=k+\sigma e_i.
\]
The certificate condition is the finite family of **all2m** inequalities
\[
\Phi(x_{i,\sigma},k_{i,\sigma})-\Phi(x,k)\ge0.
\tag{2}
\]
Then
\[
|r_i|\le\frac{1-\lambda_i}{2},\qquad
\operatorname{dist}(a_i^Tx-\beta_i,\mathbb Z)\ge\frac{\lambda_i}{2}
\quad\text{for every }i.
\tag{3}
\]

**Proof.** Full column rank and positive weights give v^TMv=Σ_iw_i(a_i^Tv)²>0 for v≠0, so M is invertible. The matrix
\[
P=W^{1/2}AM^{-1}A^TW^{1/2}
\]
is symmetric and satisfies P²=P. Its diagonal entries are λ_i, so0≤λ_i≤1. Nonzero rows give λ_i>0; zero rows simply give the trivial lower bound0.

For fixed k, the normal equations are Mx=A^TWt. Replacing k by k+σe_i changes the right side by σw_i a_i. Hence x+σh_i is the **exact** unique least-squares minimizer for that changed integer target. This justifies the reoptimization interpretation of(2); rounding at a fixed x alone is a different operation.

Expanding the difference in(2), using stationarity, yields
\[
\Delta_{i,\sigma}
=-2\sigma w_ir_i+h_i^TMh_i-2w_i a_i^Th_i+w_i
=w_i(1-\lambda_i-2\sigma r_i).
\tag{4}
\]
Both signs in(2), with w_i>0, imply −(1−λ_i)/2≤r_i≤(1−λ_i)/2. Since a_i^Tx−β_i=k_i+1/2+r_i, it lies in
\[
[k_i+\lambda_i/2,\;k_i+1-\lambda_i/2].
\]
Its distance to the nearest integer is therefore at least λ_i/2, including the boundary cases λ_i=0 or1. This proves(3). No global minimum of Φ over all k was asserted or needed. □

When m=qN and λ_i=1/q for every i, (3) gives the source-normalized margin δ=1/(2q). The trace identity Σ_iλ_i=N explains that normalization; no missing factor of N is absorbed into q. Positive rational balanced weights and a suitable pair need not be supplied by an arbitrary input matrix. This checker verifies a sufficient certificate when presented, and is not a complete implementation of the paper's existence proof or its tight-subset induction.

## 4. Exact failures of stationarity plus rounding

First take q=2,N=1,A=(1,1)^T,w=(1,1),β=0,k=(0,1),x=1. The targets are(1/2,3/2), r=(1/2,−1/2), M=2 and λ=(1/2,1/2). Stationarity holds, and each k_i is a nearest integer (ties allowed). Nevertheless both modular distances are0, below1/4. The + flip at i=0, reoptimized to x=3/2, lowers Φ by1/2. Thus(2) fails; neither the source lemma nor our sufficient condition accepts this pair.

The stronger counterexample has **unique** nearest integers:
\[
q=3,N=1,A=(1,1,1)^T,w=(1,1,1),
\quad\beta=(-9/10,-3/10,-3/10),\quad k=0,\quad x=0.
\]
Here r=(2/5,−1/5,−1/5), so its sum is0 and every |r_i|<1/2. All nearest choices are unique, M=3 and λ_i=1/3. Yet the actual modular margins are(1/10,3/10,3/10), whose minimum is less than the required1/6. Replacing k_0 by1 and reoptimizing x to1/3 changes Φ from6/25 to8/75, a decrease of2/15. Thus even unique rounding plus stationarity is insufficient.

This is a verified failure of a proposed **weakened verification rule**, not an implementation defect or a criticism of the paper, which uses stronger minimality to obtain(2). The separately frozen refinement (historical local record; not distributed here) and actual execution (historical local record; not distributed here) preserve the distinction from the first, tied example.

## 5. Phase bins, shifts and a norm-specific finite canary

Under all hypotheses of Section3, suppose additionally β=0 and λ_i=1/q. For a finite graph with vertices v∈Z^N and edge differences in {±a_i}, assign
\[
c(v)=\left\lfloor2q\{v^Tx\}\right\rfloor\in\{0,\ldots,2q-1\}.
\tag{5}
\]
If two phases occupy the same half-open bin of width δ=1/(2q), their difference has distance **strictly less** than δ from an integer. An edge has modular distance at least δ by(3), a contradiction. Thus(5) is a proper colouring. Equality in the avoidance bound is allowed; half-open bins assign every boundary point exactly once. This proves a finite conditional colouring statement, not a whole-plane colouring or a new generic-norm theorem.

Nonzero β is not innocuous here. For q=N=1,A=1,w=1,β=1/2,k=−1,x=0, the avoidance certificate is valid with shifted margin1/2. But the vertices0and1 of an ordinary zero-phase unit-step graph both receive colour0 from(5). The shift must be zero for that application, or a different edge-consistency argument must be supplied.

The mixed example uses q=2,N=2,
\[
A=\begin{pmatrix}1&0\\0&1\\1&1\\1&-1\end{pmatrix},\quad
w=(2,2,1,1),\quad\beta=0,\quad k=(0,0,0,-1),\quad x=(1/4,1/2).
\]
Here M=4I, λ_i=1/2, r=(−1/4,0,1/4,1/4), and the modular margins are(1/4,1/2,1/4,1/4). The pairs(Δ_minus,Δ_plus) are respectively(0,2),(1,1),(1,0),(1,0), all nonnegative. The four vertices(0,0),(1,0),(0,1),(1,1) have colours0,1,2,3. Every pair has distance1 in the **ℓ∞ norm**, so the graph is K4 and the finite colouring is sharp. Both diagonals have squared Euclidean length2, so these same data are not a Euclidean unit-distance K4. Neither this canary nor its four colours prove a four-colouring of the Euclidean plane.

## 6. Instrument verification, independence and reproduction

Producer (historical local record; not distributed here) uses exact Gaussian normal-equation solves and the closed expression(4). Consumer (historical local record; not distributed here) imports no producer code: it uses determinant/adjugate inversion and explicitly reoptimizes and evaluates Φ for every changed integer target. It checks every row index, both signed flips, balanced λ, dimensions and positive weights. Its optional graph consumer checks all supplied vertices, the entire unit-edge set in the declared norm, direction coverage and exact half-open bins.

The finite code contract is integer A partitioned into q invertible N×N blocks, N≤4,m=qN≤12, with rational positive weights, phases and witnesses. These resource limits describe the checker scope, not the analytic theorem's dimension range. No universal witness search, global minimization, floating log-determinant optimizer, SAT solver or donor-estate program was run.

Main22 CLI records (historical local record; not distributed here) bind code/input hashes, environment, stdout, exit and rejection stage. Four declared positive cases and a row permutation accept. The tied counterexample rejects as a mathematical negative finding. Sixteen planted defects reject: omitted/duplicate constraints, missing signed flip, forged residual/flip, nonstationary witness, wrong margin, nonpositive/unbalanced weights, singular basis, missing colour assignment, boundary-bin error, wrong metric, missing edge, shift misuse and malformed dimensions. The strict-nearest refinement adds one further expected rejection. **All23 expected dispositions matched**; no timeout/import crash is scored as a detected defect. The scientific counterexamples are not failed necessary controls.

Reproduce, from the project root, `python3 artifacts/hn_norm_scope_cycle091/check_certificate.py artifacts/hn_norm_scope_cycle091/inputs/mixed_basis_k4.json`, and separately the strict counterexample input with expected exit2. All arithmetic uses arbitrary integers and Fraction rationals; there are no outward rounding or precision assumptions hidden behind decimals. The source gap is mathematical coverage/existence, not numerical precision.

Producer/consumer share Python/Fraction, source, specification, actor/model and expected fixtures. Linear solves and flip evaluations differ in formulation. This targets concrete sign, coverage and arithmetic errors, not a common mistaken norm or theorem model. It is not blind reproduction, external human review, formal verification or a controlled performance gain.

## 7. Learning and the next unresolved bridge

The source gate resolved norm/topology/quantifier ambiguity and supplied a concrete sufficient certificate. The analytic contribution replaces unnecessary global-minimum verification **for a supplied pair** by finitely checkable coupled comparisons. It does not prove that a rational balanced certificate exists for every source input or reproduce the whole generic-norm theorem. The independent exact checks and strict-rounding counterexample show precisely which weaker rule must not be used.

The next source obligation is the original typical-norm rational-span statement needed before applying Edmonds' criterion. Resolve its inclusive counting, field, non-antipodal convention, version and quantifier scope. Do not replace it by a float rank calculation, repeat the same small matrices as discovery, transfer a shifted certificate to an unshifted colouring, or infer a new Euclidean bound from ℓ∞ examples. The global M10 problem, the full2026 existence theorem and genericity are separate unclosed research/reproduction obligations.

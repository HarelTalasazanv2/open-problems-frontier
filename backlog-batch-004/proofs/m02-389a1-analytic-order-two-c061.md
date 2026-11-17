# Audited historical reading edition

**Current audited claim:** CERTIFIED_RANGE: For the same fixed curve, the displayed outward raw L_second interval is positive and ord_(s=1)L(E,s)=2.

**Claim ceiling:** Known fixed curve under standard modularity and Mellin/functional-equation theory. Decimal correctness is an explicit implementation contract; no general BSD or independent human/formal review.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M02 cycle061 — certified second derivative and analytic order two for 389.a1

## Verdict and ceiling

**CERTIFIED_RANGE / PROVED internally.** For the fixed rational elliptic curve

\[
E:y^2+y=x^3+x^2-2x,\qquad [a_1,a_2,a_3,a_4,a_6]=[0,1,1,-2,0],
\]

with arithmetic normalization and center1, the corrected local interval instrument gives

\[
1.51125652187901730520937837991\le L''(E,1)
\le1.52599032062642969672811322048.
\]

Together with the exact central zero proved in [060](m02-389a1-central-zero-c060.md), the checked functional equation implies **ord\(_{s=1}L(E,s)=2\)**. This is a reproduction of a source-known finite example, not a new BSD case. Standard modularity, the newform/Euler identification and Fricke theory are imported mathematical theorems. Internal exposed review, source inspection and computation are not human review or formal verification. Algebraic rank2, independence, saturation, actual Sha order and the BSD leading coefficient formula remain unreproduced locally. General BSD is unproved by this project; its owning status was last checked060 on2026-10-23.

The raw second derivative is **not** the Taylor coefficient L''/2!. Its certified half lies in [0.755628260939508652604689189955,0.762995160313214848364056610240]. The previously seen table decimal0.75931650028842677023019260790 is AS_REPORTED expected-answer exposure, not an error estimate, oracle or input.

## Selection, assumptions and custody

This third prospective M02selection was explicitly reranked before execution. It outranked M01's unprepared practical head/error budget and M07's absent distant-state witness because an exact zero was now available and a nonzero derivative could decide a complete known-example analytic obligation. A neglected relevant corpus sample was the fallback. No new matrix grid or status-wrapper loop ran.

Reconstruction (historical local record; not distributed here) verifies all56immutable060members, the176-event hash chain and eight native-view hashes. No061artifact/lock was observed initially; a bounded lsof check returned no listed holder. These are overlap observations, not a guarantee of exclusive ownership. The frozen contract and later explicit amendments precede their deciding checks:

- Frozen attempt (historical local record; not distributed here).
- Precision amendment (historical local record; not distributed here).
- Different-kernel confirmation freeze (historical local record; not distributed here).

The complete060raw-coordinate consumer was rerun successfully: all390coordinates and780relations,58nonzero Hecke-witness entries and312relation coefficients. Its imported standard-theorem/model bridge remains explicit rather than being recreated from a decimal zero.

## 1. Root sign, newform convention and completion

Cycle060checked minimal discriminant389, multiplicative reduction only at389, conductor389, and the completed-square local equation after x=299+h:

\[
Y^2=4h^3+91h^2\pmod{389},\qquad Y=2y+1.
\]

Here93²≡91 mod389, so the two tangent lines Y=±93h are distinct and rational. Reduction is split multiplicative. As a second exact arithmetic observation, exhaustive counting on the singular projective cubic gives389points including its one singular point; the nonsingular locus has388points. Thus its bad Euler coefficient is a389=389−388=1, consistent with split multiplicative reduction.

[Sutherland2023lecture24, physical14/17](https://math.mit.edu/classes/18.783/2023/LectureSlides24.pdf) fixes the bad Euler factor1−T for split multiplication. [Cremona chapterII, printed25/physical19,2.6.1](https://johncremona.github.io/book/fulltext/chapter2.pdf) gives the Fricke eigenvalue ε389=−a389=−1 because389 divides the conductor exactly once. Since N=389, W389 is the full Fricke operator. Cremona2.8.5–2.8.6 then gives

\[
g(s)=389^{s/2}(2\pi)^{-s}\Gamma(s),\quad
\Lambda(s)=g(s)L(E,s),\quad
\Lambda(2-s)=-\varepsilon_{389}\Lambda(s)=\Lambda(s).
\]

The root number is +1; the Fricke eigenvalue is −1. Interchanging those signs is an invalid convention change. The modularity/newform identification uses the standard theorem for the actual curve and its conductor, not an assumption that a2 uniquely specifies a form.

Since L(E,1)=0 exactly and g is holomorphic and nonzero near1, Λ(1)=0. Evenness gives Λ'(1)=0. From Λ'=g'L+gL' we obtain L'(1)=0. Only now may the cross terms in Λ''=g''L+2g'L'+gL'' be discarded, giving L''(1)=cΛ''(1), c=2π/√389>0.

## 2. Integral formula, convergence and exact coefficient membership

The Mellin split at y=1 in Cremona printed42/physical36 gives

\[
\Lambda(s)=\int_1^\infty f(iy/\sqrt{389})
 (y^{s-1}-\varepsilon_{389}y^{1-s})\,dy.
\]

Consequently, with ε389=−1,

\[
\Lambda''(1)=2\int_1^\infty
 \left(\sum_{n\ge1}a_ne^{-cny}\right)(\log y)^2\,dy.
\]

This identity does not assume in advance that the order is exactly2. The derivative integral on physical36 supplies it for every k; physical37's proposition also states its order-at-least-r qualification explicitly. All quantities are real here.

For every good prime p≤100 the producer counts all affine (x,y)∈F_p² and adds infinity. It sets ap=p+1−#E(Fp). The complete25-prime membership is generated by integer trial division; every integer n=1..100 is generated once by the prime-power recurrence and multiplicativity. a1=1. All these primes are good because the sole bad prime is389. A separately written oracle counts using the quadratic discriminant/Legendre symbol (with the direct p2case) and expands the Euler factors by convolution. It agrees at every100indices, not merely at a summary count. The certificate records the indices, coefficients and prime counts. The recurrence and multiplicativity are fixed by Cremona2.6.2 and by the Euler product; the two implementations share that mathematical model.

A coarse global coefficient bound avoids an unverified numerical Hasse estimate. For a good prime p, there are at most2solutions y for each x and at least the point at infinity, so |ap|≤p. Inductively,

\[
|a_{p^{k+1}}|\le p\,p^{2k}+p\,p^{2k-2}
\le p^{2k+2}\quad(k\ge1),
\]

because 1/p+1/p³≤5/8<1. The base k=0,1 is immediate. At389, a389^k=1 from the bad Euler factor. Multiplicativity therefore proves |an|≤n² for all n≥1. The resulting exponential majorants justify termwise integration and differentiation near s=1 by dominated convergence. They also cover all omitted coefficients, not just the sampled prime range.

## 3. Outward arithmetic and all error budgets

The corrected producer is certify.py (historical local record; not distributed here). Its deciding parameters were frozen: K100, Y80,7900cells of exact width1/100 partitioning[1,80], precision30decimal digits. No binary floating-point values enter the mathematical bound.

Machin's identity π=16atan(1/5)−4atan(1/239), with finite rational alternating-series remainders after25and8terms respectively, supplies an interval for π. The identity follows by tangent addition and the first-quadrant angle choice; it is elementary and not a fitted decimal. Integer square-root inequalities at scale10³⁵ bound √389. Conversion of rational endpoints uses floor/ceiling division. All interval sums/products/divisions use explicit directed contexts, checking denominators away from0; negation uses context-independent sign copies.

The [official Python3.9 Decimal documentation](https://docs.python.org/3.9/library/decimal.html) specifies correctly rounded exp/ln with round-half-even. Each monotone endpoint evaluation is expanded by one representable number in each direction. Exact Fraction Taylor/atanh canaries independently bound representative exponentials/logarithms and signed arithmetic. This relies on the documented Decimal implementation contract and the local Python runtime; it is not a proof of libmpdec.

On each cell, interval evaluation bounds q=e^(−cy), evaluates the complete100-term polynomial by Horner's rule and multiplies by the interval(log y)². The integral lies within width times that interval. Summation of all7900cell enclosures bounds the entire finite integral; there is no unquantified quadrature discretization error. Dependency overestimation only enlarges the result.

### Omitted coefficient tail on[1,80]

c>3/10. Since exp(3/10)>1+3/10+9/200>4/3, q<3/4 throughout y≥1. Also log80<5, for exp5 already exceeds80 in its first six nonnegative Taylor terms. With r=3/4,K100,

\[
\sum_{n>K}n^2r^n=r^{K+1}\left[
 \frac{(K+1)^2}{1-r}+\frac{2(K+1)r}{(1-r)^2}
 +\frac{r(1+r)}{(1-r)^3}\right].
\]

Thus the absolute omitted integral on[1,80] is at most79·25times this sum, enclosed above by **0.0000205760942685117220540849045688**.

### Entire integration tail y≥80

Here q≤e^(−0.3y)<1/4. The exact geometric identity gives

\[
\sum_{n\ge1}n^2q^n=\frac{q(1+q)}{(1-q)^3}\le3q.
\]

Using (log y)²≤y²,

\[
\left|\int_{80}^\infty f(iy/\sqrt{389})(\log y)^2dy\right|
\le3e^{-24}\left(\frac{80^2}{0.3}+\frac{160}{0.3^2}+\frac2{0.3^3}\right),
\]

whose outward upper endpoint is **0.00000262581580524301688058861215196**. It covers every Fourier index, with no double-counting issue since the preceding omitted-coefficient estimate applies only below80.

The finite integral interval is

[2.37196006531619975781215936174,2.39503855120275961007436458730].

Both tail bounds are added symmetrically with outward arithmetic; multiplication by2 gives

Λ''(1)∈[4.74387372681225200614644937644,4.79012350622566672962659852164].

Multiplying by positive c supplies the raw derivative bound in the verdict. Input, rounding, finite-cell integration, coefficient truncation, infinite integration and completion conversion are all covered. Serialized endpoints are lossless decimal strings.

## 4. Failure, repair and adversarial review

**A first-version arithmetic contract failed.** Although its displayed final interval is positive, the expression I(−err,err) applied ambient28-digit rounding when negating a30-digit Decimal error. The intended exact negative−0.0000232019100737547389346735167208 became−0.00002320191007375473893467351672, an inward change. This is an implementation defect in the intended enclosure path; it is not a counterexample to analytic rank2, nor proof that the final displayed endpoints necessarily excluded the truth.

The first source and result are preserved as `certify_v1_rejected.py` and `certificate_v1_rejected.json`; failure record (historical local record; not distributed here). V1was withheld. The amended instrument uses `copy_negate`, reruns the full integral and passes the exact sign regression. No failed artifact was replaced or resealed. The displayed final endpoints happen to be unchanged because the final output rounding is coarser than the internal defect; that coincidence is not the reason for accepting the repair.

The separate Fraction consumer (historical local record; not distributed here) recomputes constants/tail formulas/conversions from exact rational endpoint values, checks all100coefficient indices and the different coefficient oracle, and verifies outward containment through completed/raw/factorial conversion. It is not merely checking that a result matches its own copied field. It does not independently reintegrate the finite integral; its validity also uses the explicit audited producer and interval argument above.

Twelve selected arithmetic/coverage canaries pass, including the known-bad unaryminus baseline and repaired path. Fourteen isolated bad-certificate mutations are rejected: wrongcenter,wrongsign,wrongfactoriallabel,actualfactor2,missingcoefficienttail,zerocoeftail,missingYtail,zeroYtail,inwardendpoint,missingcoefficient,duplicatecoefficient,alteredap2,omittedcell,wrongcompletion. Their denominator is14selected/executed/rejected, not all possible defects. The actual CLI separately accepts one healthy serialized certificate and rejects five representative bad files with the expected nonzero exits; CLI evidence (historical local record; not distributed here). The earlier060exact-image consumer also passes again.

## 5. Different-kernel challenge and adjudication

After separately freezing the challenge, integration by parts gives the genuinely different formula

\[
L''(1)=4\int_1^\infty
 \left(\sum_{n\ge1}\frac{a_n}{n}e^{-cny}\right)\frac{\log y}{y}\,dy.
\]

The boundary terms vanish at1and infinity. The polynomial here has coefficients an/n and a different logarithmic kernel. Its tail bounds use |an/n|≤n, log y/y≤1,79Σ(n>K)n(3/4)^n, and2e^(−24)/0.3 beyond80, followed by multiplication by4. Confirmation (historical local record; not distributed here) independently gives a positive interval

[1.50949329226612962700703351721,1.52784904645614565246210495137].

It overlaps the first enclosure. This checks a plausible formula/factor common-mode error, but shares coefficients, arithmetic engine, actor, platform, sources and expected-answer exposure. It is a different reduction/kernel, not blind reproduction, independent arithmetic, external review or formal verification. Agreement alone is not the certification; each interval has its stated error argument.

The second derivative is nonzero, so the exact order cannot exceed2. The exact central zero and even completion exclude orders0and1; equivalently the059Taylor lemma now has all its curve-specific analytic premises. **Analytic order exactly2 is PROVED internally at this fixed known curve.** None of this supplies a rank upper bound or independent rational points. The source's algebraic rank2 and rounded analytic Sha1 retain their059evidence status.

## 6. Outcome learning, coverage and next decision

The uncertainty changed from an unverified derivative decimal to an explicit outward nonzero enclosure and a complete fixed-curve analytic-order reproduction. The finite Mellin route is supported for this example. The detected failure mode is ambient-context unary arithmetic escaping a directed interval design; the exact-sign regression transfers to future certificate instruments. Do not repeat this numerical integral to gain digits without a named consumer; the positive margin already resolves its selected question. No speed or research-productivity gain is claimed.

Source inspection register (historical local record; not distributed here) records a new substantive book coefficient/Fricke passage and the completion passage in the primary lecture, with exact reinspection extents and Decimal documentation. It does not count the Wiley access failure as read content. Public-source captures and OPFcustody copies add0direct volume paths. Pass036 remains141paths,131full/10partial,132recorded whole-file hashes;105/428327frozen candidates,33noncandidates,3post-census/unclassified. Underlying-source count and whole-volume content-hash denominator remainUNKNOWN. Metadata census2,330,261non-directory entries/308,425directories is historical, not a content review. Estate sampling73/75candidate-bearing and5/60accessiblezero-candidate;five duplicate groups/14paths,fourinaccessible system directories,opaque symlink/archive interiors unchanged.

The third M02selection now completes its analytic certificate. Prefer the bounded volume-root heuristic relevance audit (historical local record; not distributed here), not another unchanged M02decimal or speculative point-rank proof. First identify scientifically relevant noncandidate content by minimal metadata; if there is none, record that negative sample instead of reading personal/commercial files. Algebraic-rank reproduction may be reconsidered when a concrete descent/saturation instrument is ready.

## Reproducibility

From OPFroot, standard-library Python3.9.6, no installs:

```
python3 artifacts/m02_second_derivative_cycle061/certify.py
python3 artifacts/m02_second_derivative_cycle061/verify.py
python3 artifacts/m02_second_derivative_cycle061/cli_controls.py
python3 artifacts/m02_second_derivative_cycle061/confirm.py
python3 artifacts/m02_central_zero_cycle060/verify.py artifacts/m02_central_zero_cycle060/certificate_389_discovery.json 389
```

Reruns write only061result files; preserve the sealed artifacts before rerunning. The immutable manifest and final closeout bind this actual run. No source-estate code ran; no messages, publications, uploads, purchases, installs, app/schedule/notification changes or other-estate writes occurred.

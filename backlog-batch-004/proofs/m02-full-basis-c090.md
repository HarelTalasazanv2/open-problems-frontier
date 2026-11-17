# Audited historical reading edition

**Current audited claim:** PROVED: For this fixed curve E(Q)=Z(0,0) direct-sum Z(1,0).

**Claim ceiling:** Known full basis under named canonical-height/difference theorems and the complete descent input. No full Sha or general BSD.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# The full rational-point group of the fixed 389.a1 curve

**PROVED internally, known-result reproduction under named standard height theorems.** On
\[
E/\mathbb Q:\quad y^2+y=x^3+x^2-2x,
\]
the points \(P=(0,0)\) and \(Q=(1,0)\) form a basis of the **entire** group:
\[
\boxed{E(\mathbb Q)=\mathbb ZP\oplus\mathbb ZQ.}
\]
In particular the torsion subgroup is trivial and the subgroup already proved 2-saturated in086 has index one. This is stronger than rank two or testing a list of odd primes. It does not establish general BSD, the full leading-coefficient formula, finiteness/order of Sha, a regulator value, novelty, or external human/formal verification.

The analytic argument reduces the full generation question to a complete bounded rational-point set. **CERTIFIED_RANGE:** that set has60 affine points plus O, and every point has an exact expression mP+nQ with |m|,|n|≤4. A separately written consumer checks every member and witness; no cutoff in the witness-discovery search is used as a nonexistence claim.

## 1. Dependencies and normalization

The prior [086 proof](m02-point-independence-c086.md) proves independence, absence of rational2-torsion, and that P,Q,R=P+Q are all outside2E(Q). The [089 complete quartic envelope](m02-389a1-rank-two-c089.md) proves |E(Q)/2E(Q)|≤4 under the named published general-descent/reduction/equivalence theorems. Thus
\[
O,P,Q,R=(-2,-1)
\tag{1}
\]
give a complete set of representatives for E(Q)/2E(Q). This completeness is a necessary inherited proof dependency; a source-reported rank or a small point search could not replace it. The prior immutable artifacts were verified before use. The existing independence proof is needed at the final direct-sum step.

The new primary ingredient is Cremona's corrected online second edition of *Algorithms for Modular Elliptic Curves*, [Chapter3](https://johncremona.github.io/book/fulltext/chapter3.pdf), physical10–11 and16–17, printed71–72 and77–78. The [owner index](https://johncremona.github.io/book/fulltext/index.html) was checked again; its bytes agree with089. The pinned42-page PDF remains SHA-256 `c4843b80ae1b6b91795b9952d782912542dd8d6b17c1940cd1a881fa6fdd9c26`. Exact source records (historical local record; not distributed here) distinguish the new selected pages, reread pages and metadata from a full-chapter reading.

Use the **larger** normalization
\[
H(T)=\widehat h(T)=\lim_{n\to\infty}4^{-n}h(2^nT),\qquad
h(T)=\log\max\{|a|,c^2\}
\tag{2}
\]
when x(T)=a/c² is reduced, c>0; put h(O)=H(O)=0. All logarithms are natural. This H is twice the smaller height in Silverman's paper, exactly as the source warns on printed72. We import its standard nonnegative quadratic-height properties, including H(2T)=4H(T) and the parallelogram identity. We also import the published explicit height-difference bound, Proposition3.5.1, in this normalization. Its underlying height-theory proof is not re-proved here. The short generation lemma will be proved below, rather than treated as a numerical heuristic.

For an integral standard Weierstrass model, that proposition gives
\[
-C\le H(T)-h(T)\le U,
\]
\[
U=\mu+2.14,\quad C=\tfrac1{12}h(j)+\mu+1.922,
\quad\mu=\tfrac16(\log|\Delta|+\log^+|j|)
+\log^+|b_2/12|+\log(2^*),
\tag{3}
\]
where 2*=2 when b₂≠0 and1 otherwise. The printed decimal constants are used as the stated rational bounds107/50 and961/500. No floating-point evaluation of a canonical height or a truncation algorithm is a proof premise.

## 2. Exact coarse bounds for this curve

The checked invariants are b₂=4,c₄=112,c₆=−856,Δ=389. Set N=112³=1404928. Here j=N/389>1, log⁺|b₂/12|=0, 2*=2, and hence
\[
\mu=\tfrac16\log N+\log2,\qquad h(j)\le\log N.
\]
An upper bound for h(j) suffices; reduction of this rational number cannot increase numerator or denominator height.

We need only elementary rational logarithm bounds. The positive exponential series gives
\[
e^{7/10}>1+\tfrac7{10}+\tfrac{(7/10)^2}{2}+\tfrac{(7/10)^3}{6}
=\tfrac{12013}{6000}>2,
\]
so log2<7/10. Conversely, the convergent positive series2atanh(1/3) gives
\[
\log2>2\left(\tfrac13+\tfrac1{81}\right)=\tfrac{56}{81}.
\tag{4}
\]
Since N<2²¹, (3) implies
\[
U<\frac{21(7/10)}6+\frac7{10}+\frac{107}{50}
=\frac{529}{100}<\frac{53}{10},
\]
\[
C<\frac{21(7/10)}4+\frac7{10}+\frac{961}{500}
=\frac{6297}{1000}<\frac{63}{10}.
\tag{5}
\]
The upper direction in each substitution is deliberate. In particular h(T)≤H(T)+C uses the **lower** side of the height-difference inequality, while H(T)≤h(T)+U uses its upper side.

Twice doubling the three affine representatives gives the following **exact** points:

| T | 4T |
|---|---|
| P | (114/121, −267/1331) |
| Q | (1431/961, −64665/29791) |
| R=P+Q | (2319450/243049, 3616419800/119823157) |

Both the original-model discovery law and an independently written law on a short model verify these coordinates. Each reduced x-coordinate has max(|numerator|,denominator)<2²². Therefore, using the factor **16**, not4, for two doublings,
\[
H(T)=\frac{H(4T)}{16}
\le\frac{h(4T)+U}{16}
<\frac{22(7/10)+53/10}{16}
=\frac{207}{160}<\frac{13}{10}.
\tag{6}
\]
The representative O has height0. Thus the full canonical-height ball
\[
S=\{T\in E(\mathbb Q):H(T)\le B\},\qquad B=13/10,
\tag{7}
\]
contains a complete set of representatives (1). It is important that S means **all** points satisfying the height bound, not just the four listed points.

## 3. A complete proof of the height-ball generation lemma

We prove the source's Lemma3.5.2 in the form needed here, with properness explicit. Let G=E(Q), let H be a nonnegative quadratic canonical height, and assume a uniform bound h≤H+C. Suppose B≥0 and S={H≤B} contains a representative for every coset of2G. Then S generates the entire group G.

For each finite K, {H≤K} has finitely many elements: its x-heights are at most K+C, which bounds the numerator and denominator of the reduced rational x-coordinate. Only finitely many x occur, each has at most two y-values, and O adds one point. Thus the properness needed to choose a minimum does not require an unsupported assertion that arbitrary real height values form a discrete subset of R.

Let A be the subgroup generated by S and suppose A≠G. Choose W outside A of least H. Such a minimum exists by applying the preceding finiteness argument to all outside points of height at most that of any one initial outside point. Since every point with H≤B belongs to S⊂A, H(W)>B.

Choose V∈S representing W modulo2G and write W=V+2Z. If Z∈A then W∈A, so Z is outside A and H(Z)≥H(W). The parallelogram identity and nonnegativity give
\[
H(V)=\tfrac12\{H(W+V)+H(W-V)\}-H(W)
\ge\tfrac12H(2Z)-H(W)
=2H(Z)-H(W)\ge H(W)>B.
\]
This contradicts V∈S. Consequently A=G. The argument works in the actual group, not only modulo torsion. In particular every torsion point lies in S because H=0 there; it is not a missing exceptional coset.

This lemma explains why a list of coset representatives alone is insufficient: one must establish membership in the claimed subgroup for **every** point of the height ball.

## 4. Reduction to a complete finite rational-point census

For T∈S, (5) and (7) give
\[
h(T)\le H(T)+C<\frac{13}{10}+\frac{63}{10}=\frac{38}{5}.
\]
The lower bound in (4) gives
\[
\frac{38}{5}<11\frac{56}{81}<11\log2=\log2048.
\tag{8}
\]
The rational margin in the first comparison is2/405. Thus every affine T∈S satisfies max(|a|,c²)<2048. We deliberately enumerate the slightly larger **closed** region max(|a|,c²)≤2048; no boundary point is lost.

Here is an elementary denominator justification, covering primes2 and3 as well. If vₚ(x)=−m<0, the term x³ has uniquely smallest valuation −3m on the right of y²+y=x³+x²−2x. The left must have vₚ(y)=−n<0, with uniquely smallest valuation −2n. Hence2n=3m, so m is even and n=3m/2. Conversely, if x is p-integral then the right side is p-integral, and a negative valuation of y would make the left side nonintegral, a contradiction. Across all primes this proves x=a/c²,y=b/c³ for integers a,b,c, c>0 and gcd(a,c)=1. No point with a nonsquare reduced x-denominator can have been excluded incorrectly.

Since45²≤2048<46², the census is
\[
1\le c\le45,\quad -2048\le a\le2048,\quad\gcd(a,c)=1.
\tag{9}
\]
Substitution gives the exact criterion
\[
(2b+c^3)^2=D(a,c):=4a^3+4a^2c^2-8ac^4+c^6.
\tag{10}
\]
For each pair, discard negative D; otherwise test for an exact integer square z²=D. Include both signs of z, zero only once, and put
\[
x=a/c^2,\qquad y=\frac{\pm z-c^3}{2c^3}.
\]
Parity is consistent: D≡c⁶ mod4 forces z≡c³ mod2, so the displayed numerator is even. Direct substitution independently checks every emitted point. The case a=0 is included with c=1, negative coordinates and both inverse y-values are retained, and O is handled separately.

There are184365 raw pairs in (9) before the coprimality filter,113201 afterward. The exact census gives **60 affine points**. These counts describe the stated finite region, not all rational points on E.

## 5. Independent exact membership verification

The discovery instrument (historical local record; not distributed here) uses Fraction arithmetic and the chord-tangent formula derived for the original model. A bounded |m|,|n|≤16 dictionary is used solely to find **positive** membership witnesses for the60 points. All are found; the largest absolute coefficient actually used is4. The failure to find a witness would have been INCONCLUSIVE, not a proof of nonmembership or a reason to shrink the census.

The independent consumer (historical local record; not distributed here) imports no discovery code. It regenerates the finite set by looping over reduced x-denominators v≤2048, requiring v to be a square, and checking the reduced rational discriminant4x³+4x²−8x+1 for square numerator and denominator. It verifies exact member sets and multiplicities rather than counts alone.

For each submitted expression mP+nQ it uses binary multiplication and the independent short model
\[
U=x+1/3,\quad V=y+1/2,\qquad V^2=U^3-\tfrac73U+\tfrac{107}{108}.
\]
Its addition formula has no x² or linear y term. This targets a plausible shared-model sign/offset mistake. Both models check point admissibility, inverse/identity cases and exact coordinate equality. Known small canaries verify P+Q=R,2P=(3,5),2Q=(6,−16), the vertical-line inverse and O. A declared separate curve V²=U³−U with (0,0) supplies a genuine order-two boundary canary for the short-law doubling branch; it is not misrepresented as rational2-torsion on our fixed curve.

The full point table below and machine-readable certificate (historical local record; not distributed here) show that all60 points in the closed naive-height region belong to L=ZP+ZQ. O belongs to L as well. By (8), S⊂L; by Section3, S generates E(Q). Therefore E(Q)⊂L. The reverse inclusion is immediate, proving E(Q)=L. The086 independence theorem then makes this an isomorphism Z²→E(Q), so there is no nonzero torsion and no residual odd index. No additional torsion or prime-saturation oracle is required for this implication.

## 6. Adversarial findings, limits and reproducibility

The initial source contract (historical local record; not distributed here), bounded finite attempt (historical local record; not distributed here) and confirmation freeze (historical local record; not distributed here) precede their deciding executions. The source gate identified this route in4.41 minutes; the finite attempt completed in3.31 minutes, sharing the original45-minute/100-call budget. Times are descriptive, not a controlled performance comparison.

Thirteen actual CLI cases (historical local record; not distributed here) record input/code hashes, Python version, raw stdout, exits and stages. The healthy and reordered complete certificate pass. Eleven planted defects reject: missing point, duplicate, omission of the inverse of P, same-count replacement by the genuine but out-of-region4R, forged combination, wrong model, wrong cutoff, wrong height normalization, noncanonical fraction, missing O and substituting2P for4P. Every expected exit/stage matches. No invalid/import crash is scored as a detected defect. These cases challenge the consumer; the analytic height/coverage argument supplies the proof beyond them.

Reproduce the confirming check from the project root with `python3 artifacts/m02_odd_index_readiness_cycle090/check_basis.py artifacts/m02_odd_index_readiness_cycle090/discovery.json`. It uses standard-library arbitrary integers, Fraction and isqrt only. No floating-point rounding, numerical canonical-height computation, asymptotic tail, downloaded executable, source-estate code execution or installation occurs. Discovery writes its output exclusively; rerun it only in an isolated local copy to preserve this dated record.

The two implementations share Python/Fraction, the fixed curve, input certificate, source theorems, actor/model and exposure to the expected known basis. They differ in point-census coordinates, discriminant-square formulation, group model and scalar method. This is an independent implementation in those dimensions, not blind reproduction, external human review or formal verification. Inherited086/089 proof debt and the imported explicit height theorem remain visible. Withholding a required imported theorem makes the full-group conclusion conditional on it; it does not erase the exact finite point identities.

**Learning:** an explicit height-ball argument closed the odd-index gap without a regulator estimate or an arbitrary prime scan. The regulator route was unnecessary, not false. The conclusion transfers to another curve only after new coset-completeness and explicit height-bound audits. Do not repeat the60-point census, the089 quartics or086 half obstructions. After the independence/rank/basis successes, pause this known-curve family and rotate the frontier. Actual Sha-order/leading-coefficient work is a separate unprepared obligation; rank equality or a full basis cannot substitute for it.

## Appendix: complete closed-region point certificate

Coordinates are reduced fractions. Each row is the exact identity T=mP+nQ; O has witness(0,0) separately. The finite table is not a second independent source.

| # | x(T) | y(T) | m | n |
|---:|---:|---:|---:|---:|
|1|-51/25|-68/125|-3|2|
|2|-51/25|-57/125|3|-2|
|3|-2|-1|1|1|
|4|-2|0|-1|-1|
|5|-1364/729|-28952/19683|-1|4|
|6|-1364/729|9269/19683|1|-4|
|7|-95/64|-1007/512|-1|-3|
|8|-95/64|495/512|1|3|
|9|-11/9|-55/27|-3|0|
|10|-11/9|28/27|3|0|
|11|-1|-2|1|-1|
|12|-1|1|-1|1|
|13|-3/4|-15/8|-1|2|
|14|-3/4|7/8|1|-2|
|15|-14/25|-216/125|3|1|
|16|-14/25|91/125|-3|-1|
|17|-36/169|-2952/2197|-3|-2|
|18|-36/169|755/2197|3|2|
|19|-5/49|-405/343|1|-3|
|20|-5/49|62/343|-1|3|
|21|0|-1|-1|0|
|22|0|0|1|0|
|23|1/16|-55/64|3|-1|
|24|1/16|-9/64|-3|1|
|25|26/361|-5720/6859|-3|3|
|26|26/361|-1139/6859|3|-3|
|27|1/9|-19/27|1|2|
|28|1/9|-8/27|-1|-2|
|29|328/361|-4059/6859|-2|-3|
|30|328/361|-2800/6859|2|3|
|31|1809/1936|-65151/85184|2|-4|
|32|1809/1936|-20033/85184|-2|4|
|33|114/121|-1064/1331|-4|0|
|34|114/121|-267/1331|4|0|
|35|1|-1|0|-1|
|36|1|0|0|1|
|37|315/289|-6110/4913|4|-2|
|38|315/289|1197/4913|-4|2|
|39|10/9|-35/27|-2|2|
|40|10/9|8/27|2|-2|
|41|5/4|-13/8|2|1|
|42|5/4|5/8|-2|-1|
|43|1431/961|-64665/29791|0|4|
|44|1431/961|34874/29791|0|-4|
|45|56/25|-496/125|0|-3|
|46|56/25|371/125|0|3|
|47|3|-6|-2|0|
|48|3|5|2|0|
|49|4|-9|2|-1|
|50|4|8|-2|1|
|51|6|-16|0|2|
|52|6|15|0|-2|
|53|445/49|-9955/343|4|1|
|54|445/49|9612/343|-4|-1|
|55|39|-247|-2|-2|
|56|39|246|2|2|
|57|133|-1540|2|-3|
|58|133|1539|-2|3|
|59|188|-2585|-4|1|
|60|188|2584|4|-1|

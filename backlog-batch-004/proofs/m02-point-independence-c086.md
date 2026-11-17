# Audited historical reading edition

**Current audited claim:** PROVED: The points P=(0,0),Q=(1,0) are Z-independent and their subgroup is2-saturated.

**Claim ceiling:** Named nonsingular Weierstrass group law; no upper rank or odd/full saturation from this record alone.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Fixed389.a1 curve: point independence and a 2-saturation corollary

**PROVED_INTERNAL, restricted analytic theorem.** On

\[
E/\mathbb Q:\quad y^2+y=x^3+x^2-2x,
\]

the points P=(0,0), Q=(1,0) are ℤ-linearly independent. Their subgroup L=ℤP+ℤQ is 2-saturated in E(ℚ): if 2S∈L, then S∈L. In particular E(ℚ) contains a subgroup isomorphic to ℤ², and its Mordell–Weil rank is at least2.

This reproduces a component of a source-known example. It proves neither an upper rank bound nor odd-prime/full saturation, Sha, the BSD leading coefficient formula or general BSD. The earlier native analytic-order2 result is a separate theorem; combining it with this lower bound does not by itself prove algebraic rank exactly2.

Frozen scope (historical local record; not distributed here), halving adaptation (historical local record; not distributed here), separately frozen corollary (historical local record; not distributed here), exact checks and controls (historical local record; not distributed here).

## 1. Model, group law and source role

This is exactly the native coefficient vector[0,1,1,−2,0] from059–061. The discriminant is389. Directly, b₂=4,b₄=−4,b₆=1,b₈=−3, and

\[
\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6
=48+512-27-144=389\ne0.
\]

Thus its projective completion is nonsingular, with identity O at infinity. We use the standard theorem that a nonsingular Weierstrass cubic with its rational identity carries the chord-tangent abelian group law. Associativity is an imported standard theorem, not proved by our finite arithmetic or a database status. [Sutherland's MIT lecture2](https://math.mit.edu/classes/18.783/2021/LectureNotes2.pdf), physical1 and3, reviews this law and the coefficient comparison giving point addition. Explicitly U=x+1/3, V=y+1/2 carries our curve over ℚ to V²=U³−(7/3)U+107/108, so the standard short-model theorem applies. The formulas used below are derived directly for our equation, rather than copied from a short model without adjusting its x² and y terms.

The web retrieval tool initially returned an LMFDB browser-check page. An ordinary public HTTP retrieval subsequently returned the actual owner page, with the matching label/equation and source-reported rank2, trivial torsion and generators(0,0),(1,0). Its relevant text was inspected after the proof's certificate had been frozen and run; no page-supplied programs executed. This resolves current model/source association, not an independent upper-rank or full saturation certificate. The proof works for the displayed nonsingular curve independently of the label389.a1 or a database's claimed rank. Both the initial route failure and the successful content-bearing alternative are retained.

For affine points the inverse is

\[
-(x,y)=(x,-y-1).
\]

Both P and Q lie on E. The line y=0 has intersections at x=0,1,−2; reflecting the third point (−2,0) gives

\[
R:=P+Q=(-2,-1).
\tag{1}
\]

These three points are nonidentity points.

## 2. A necessary quartic for a rational half

Put

\[
F(u)=4u^3+4u^2-8u+1.
\]

If T=(u,v) is affine, its curve equation gives (2v+1)²=F(u). If 2T is a nonidentity affine point, then 2v+1≠0: equality would make T=−T, hence2T=O. The tangent slope is therefore defined and equals

\[
m=\frac{3u^2+2u-2}{2v+1}.
\]

Substitute its line in the cubic. Comparing the coefficient of x² for the double intersection at u gives

\[
x(2T)=m^2-1-2u
=\frac{(3u^2+2u-2)^2-(1+2u)F(u)}{F(u)}
=\frac{u^4+4u^2-2u+3}{F(u)}.
\tag{2}
\]

This is an identity over ℚ, with its nonzero-denominator condition explicitly checked. If S is a nonidentity rational point with x(S)=s and S=2T, then u is a rational root of the **monic integral** polynomial

\[
h_s(u)=u^4-4su^3+(4-4s)u^2+(-2+8s)u+(3-s).
\tag{3}
\]

For the integer coordinates s used here, the rational-root theorem makes u an integer. For completeness, if a/b in lowest terms solves a monic integral polynomial, multiplying by b⁴ shows b divides a⁴. Coprimality forces b=1. This is why reduction of the polynomial modulo3 is legitimate even though a general rational elliptic-curve point could have denominators divisible by3.

The modular calculations below concern integer polynomials. They do **not** apply a characteristic-not3 group-law formula to an elliptic curve over F₃.

## 3. P, Q and P+Q are not rational doubles

For P, s=0 and

\[
h_0(u)=u^4+4u^2-2u+3
=u^4+(2u-\tfrac12)^2+\tfrac{11}{4}>0
\]

for every real u. Consequently P is not a double even in E(ℝ), hence not in E(ℚ).

For Q and R, equations(1)–(3) give

\[
h_1(u)=u^4-4u^3+6u+2,\qquad
h_{-2}(u)=u^4+8u^3+12u^2-18u+5.
\]

Modulo3 both are u⁴+2u³+2. The complete residue table is

| u mod3 |0|1|2|
|---|---:|---:|---:|
| h₁(u) mod3 |2|2|1|
| h₋₂(u) mod3 |2|2|1|

Neither has an integer root, so neither has a rational root. By the necessary condition(3), Q and R=P+Q are not in2E(ℚ).

This is a complete obstruction, not a search for small rational halves. Monicity handles every possible rational denominator and the residue tables cover every integer class.

## 4. There is no rational 2-torsion

If a nonidentity T=(x,y) has2T=O, then T=−T gives y=−1/2. Its curve equation becomes F(x)=0. Setting z=4x and multiplying by16 gives

\[
z^3+4z^2-32z+16=0.
\tag{4}
\]

It is monic integral, so rational z would be an integer. Its complete mod5 values are

| z mod5 |0|1|2|3|4|
|---|---:|---:|---:|---:|---:|
| z³+4z²−32z+16 mod5 |1|4|1|3|1|

There is no root, so E(ℚ)[2]={O}. O is already accounted for; no affine endpoint, denominator or projective point is omitted.

## 5. Infinite descent proves independence

Suppose aP+bQ=O with integers a,b not both0. Divide their coefficients by their largest common power of2. This preserves a relation: if2(a′P+b′Q)=O, the absence of rational2-torsion forces a′P+b′Q=O.

We obtain a relation with at least one odd coefficient. Modulo2E(ℚ), its left side is one of P,Q,P+Q according to the three nonzero parity classes of(a,b). Section3 proved none lies in2E(ℚ), while O does. Contradiction.

Hence no nonzero integer relation exists. The map ℤ²→E(ℚ), (a,b)↦aP+bQ, is injective. Interpreting this as rank≥2 uses only the usual Mordell–Weil rank terminology; the injectivity theorem itself needs no computation of a basis or an upper bound.

## 6. Separately stated 2-saturation corollary

Assume 2S=aP+bQ. If either coefficient is odd, the same parity argument contradicts Section3. Both are even, so

\[
2\bigl(S-\tfrac a2P-\tfrac b2Q\bigr)=O.
\]

Section4 gives S=(a/2)P+(b/2)Q∈L. Thus L is2-saturated. Iteration gives the corresponding statement for powers of2.

The quotient E(ℚ)/L has no nonzero2-torsion. This says nothing here about odd torsion in that quotient, its rank, the full finite index of L, or whether L is all of E(ℚ). It is not a full saturation or rank-exactly2 certificate.

## 7. Adversarial verification and trust boundary

The analytic proof is Sections1–6 under the named standard group-law theorem. The owned exact checker (historical local record; not distributed here) confirms coefficient identities, admissible points, discriminant, the positive-square identity and every mod3/mod5 residue. The certificate was frozen before execution; integer and Fraction arithmetic supply exact results, not floating approximations.

Seven actual CLI executions covered the valid certificate and six bad cases, checking both exit status and expected failure stage. Missing parity classes, sign errors, missing or duplicate residue membership and forged values were rejected. A known true half controls the logical direction: tangent arithmetic gives2P=(3,5), whose polynomial h₃(u)=u⁴−12u³−8u²+22u has rootu=0. A purported root-free certificate for it is rejected at ZERO_ROOT. Thus the checker does not merely accept every monic quartic as a no-half proof.

The confirming arithmetic shares the model, expected answers and actor/model with the derivation. It is not blind reproduction, external human review or formal verification. No point-height algorithm, finite-group implementation, full descent, rank oracle, modular-symbol replay, L-function computation or source-estate program was executed.

**Uncertainty changed:** a previously unproved local algebraic lower-bound component is now proved, with a narrow2-saturation corollary. The larger planned finite-group search was unnecessary. The prior analytic order2 and database rank2 remain distinct evidence, with the algebraic upper bound and odd-prime/full saturation still open within this project.

**Do not repeat:** finite-prime or small-coordinate searches for these same halves, or treat this as a new mathematical example. Any further upper-rank/descent work needs an explicitly prepared certificate and its own source/hypothesis audit. The full frontier is reranked at closeout.

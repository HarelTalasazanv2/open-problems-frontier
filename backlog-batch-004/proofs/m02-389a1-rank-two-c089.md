# Audited historical reading edition

**Current audited claim:** PROVED: The exact conservative10205-triple envelope has64quartics, each with a positive equivalence witness to one of four soluble targets. Under the specified published complete descent/reduction theorems the fixed curve has rank2.

**Claim ceiling:** Finite exact computation and fixed-curve deduction under named published completeness/equivalence and Mordell-Weil theorems; no source-theorem reproof, novelty or general BSD.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Fixed 389.a1 curve: a complete quartic envelope and algebraic rank two

**PROVED internally, restricted known-result reproduction.** For
\[
E/\mathbb Q:\quad y^2+y=x^3+x^2-2x,
\]
the Mordell–Weil rank is exactly two. The upper bound is a complete finite quartic-cover certificate under the explicitly imported general two-descent and reduction theorems below. The lower bound is the native [086 analytic halving proof](m02-point-independence-c086.md), restated at its decisive steps below. No database rank integer is used as a proof premise. This is a known example, not a new BSD case, proof of general BSD, full saturation, determination of the order of Sha, or an externally/formally reviewed result.

**CERTIFIED_RANGE:** all integral quartics with invariants (112,−1712) in the conservative box (3) are enumerated exactly: 64 forms from 10,205 coefficient triples. Every form has an exact positive equivalence witness to one of four specified rationally soluble targets. Two algebraically different enumerators agree on exact membership. This finite statement becomes a rank upper bound only through the source reduction/completeness theorems; the computer does not prove those theorems.

## 1. Imported theorems, source custody and the logical bridge

The source is John Cremona, *Algorithms for Modular Elliptic Curves*, corrected online second edition, [Chapter 3](https://johncremona.github.io/book/fulltext/chapter3.pdf), §3.6, printed pp.89–96 (physical pp.28–35). Owner provenance is the [online index](https://johncremona.github.io/book/fulltext/index.html). The pinned PDF is 335297 bytes, SHA-256 `c4843b80ae1b6b91795b9952d782912542dd8d6b17c1940cd1a881fa6fdd9c26`. Its actual coefficient bounds and equivalence proposition were visually checked, as were the invariant-pair selection rules. Exact extents are in the inspection register (historical local record; not distributed here). Extracting all 42 pages is not a full reading of the chapter.

The following published mathematical results are **imported**, rather than claimed to be re-proved invariant theory:

1. A quartic model \(z^2=ax^4+bx^3+cx^2+dx+e\), up to the rational equivalence in §3.6 p.89, describes a two-covering. Rationally soluble classes identify with \(E(\mathbb Q)/2E(\mathbb Q)\); everywhere locally soluble classes form its two-Selmer envelope (p.90). The trivial class consists of quartics with a rational root.
2. For a minimal integral Weierstrass model, p.92 specifies either one or two integral invariant pairs sufficient to represent all locally soluble classes. The coefficient reduction on pp.93–94 gives a bounded representative for every nontrivial real-soluble class at each required pair. Rational-root classes, including zero leading coefficient, are accounted for separately by the trivial class.
3. Proposition 3.6.3, p.96, gives the exact rational-equivalence criterion (5) below. Only its positive direction is needed here.
4. Mordell–Weil finite generation gives \(|E(\mathbb Q)/2E(\mathbb Q)|=2^r|E(\mathbb Q)[2]|\). The group law and the rational coordinate change are standard for this nonsingular Weierstrass model.

These are standard theorem applications with source/hypothesis checks, not blind reproduction, a proof-assistant replay, a full audit of the cited reference [20]/[52] proofs, or human mathematical review. If any imported completeness or equivalence theorem is withheld, the certified finite calculation survives, while the rank conclusion is conditional on that theorem. No borrowed executable or donor-estate program was executed.

## 2. Normalization, minimality and one invariant pair

Direct Weierstrass arithmetic gives
\[
(b_2,b_4,b_6,b_8)=(4,-4,1,-3),\quad c_4=112,\quad c_6=-856,\quad\Delta_E=389.
\]
The integral discriminant is squarefree, hence the model is minimal: a nonminimal integral scaling at a prime would require a factor of the twelfth power of that prime in its discriminant. Nonsingularity follows from \(\Delta_E\ne0\).

For a binary quartic put
\[
I=12ae-3bd+c^2,\qquad
J=72ace+9bcd-27ad^2-27eb^2-2c^3.
\tag{1}
\]
The source choice is \(I=c_4=112,J=2c_6=-1712\). The basic pair is not divided by (16,64), since \(64\nmid1712\). The extra larger pair is unnecessary by the source's p.92 criterion: \(4\mid112\), \(8\mid-1712\), and \(16\mid(2\cdot112-1712)=-1488\). This checks the often important second-pair omission explicitly.

The quartic Jacobian model is
\[
E_{I,J}:Y^2=X^3-27IX-27J=X^3-3024X+46224.
\]
The rational isomorphism is \(X=36x+12,Y=216y+108\). Indeed its two sides differ by \(46656(y^2+y-x^3-x^2+2x)\). The quartic invariant discriminant is \(4I^3-J^2=2688768=6912\cdot389>0\); the ordinary quartic discriminant is this divided by 27, namely \(99584\). Do not confuse either with \(\Delta_E\).

## 3. A conservative complete coefficient box

The source resolvent is
\[
R(t)=t^3-3It+J=t^3-336t-1712.
\]
Its signs at −15,−14,−6,−5,20,21 are respectively −47,248,88,−157,−432,493. The intermediate value theorem and degree three give exactly one root in each disjoint interval
\[
t_-\in(-15,-14),\quad t_0\in(-6,-5),\quad t_+\in(20,21).
\tag{2}
\]
No numerical approximation to a root is a proof input. Positive discriminant leaves source types 1 (no real roots) and 2 (four real roots), not type 3. Negative-leading type 1 is real-insoluble and may be discarded.

For type 1 the source orders the roots decreasingly. Put \(K=(4I-t_+^2)/3\). Then \(7/3<K<16\) and \(3/2<\sqrt K<4\). Its positive-a bound is
\[
a\le\frac{K+\sqrt Kt_+}{3\sqrt K+t_++2t_0}<\frac{100}{25/2}=8.
\]
The denominator is strictly positive by (2). With \(-2a<b\le2a\), the source bounds on c read \(t_0/2+3b^2/(8a)\le c\le t_+/2+3b^2/(8a)\). Therefore \(-3<c<45/2\) even after conservatively including a=8.

For type 2 with a>0,
\[
a\le\frac{I-t_0^2}{3(t_0-t_-)}<\frac{87}{24}<4,
\]
so a≤3. The lower bound on c is \(t_0/2-(I-t_0^2)/(6a)+3b^2/(8a)>-35/2\); its upper bound \(t_-/2+3b^2/(8a)\) is less than −5/2. These lie well inside [−32,32].

For type 2 with a<0 the source explicitly reverses the root ordering. Its bound gives
\[
|a|\le\frac{I-t_0^2}{3(t_+-t_0)}<\frac{87}{75}<2,
\]
so a=−1. The c bounds are \(t_+/2-3b^2/8\le c\le t_0/2+(I-t_0^2)/6-3b^2/8\); they are strictly between 17/2 and 12 after allowing \(|b|\le2\). Again [−32,32] contains the full range.

Thus every nontrivial locally soluble class has a representative in
\[
\boxed{a\in\{-1,1,2,3,4,5,6,7,8\},\quad -2|a|\le b\le2|a|,\quad -32\le c\le32.}
\tag{3}
\]
The extra b endpoint and a=8 intentionally enlarge the region. An enlarged region can only add forms to check; it cannot lose a required representative. It has \(65(5+\sum_{a=1}^8(4a+1))=65\cdot157=10205\) triples. This is a complete **representative envelope**, not a claim that every integral quartic with these invariants has small coefficients.

## 4. Exact enumeration and its completeness

The discovery instrument uses the seminvariants
\[
p=3b^2-8ac,\qquad r=b^3+8a^2d-4abc,
\]
and the source identity \(27r^2=p^3-48Ia^2p-64Ja^3\). For each triple (3), an integer square test determines both possible signs of r, including zero once; then
\[
d=\frac{r-b^3+4abc}{8a^2},\qquad e=\frac{I+3bd-c^2}{12a}.
\]
Nonintegral choices are discarded and (1) is checked directly.

The confirming checker does **not import that enumerator**. Eliminate e using (1). The equation for d is
\[
Ad^2+Bd+C=0,\quad A=108a^2,\quad B=27b^3-108abc,
\]
\[
C=4aJ-24acI+32ac^3+9b^2I-9b^2c^2.
\tag{4}
\]
It obtains both roots by an exact discriminant-square test and divisibility by 2A, then checks e and both original invariants. Since a≠0, A≠0; no linear/degenerate case is silently omitted. Conversely every integral solution of (1) must satisfy (4), so this procedure enumerates every required d,e. It independently visits every triple and compares the exact submitted member set, rejects multiplicities, and verifies the declared counts.

Both procedures obtain precisely 64 forms. This is integer arithmetic, not floating-point agreement or a bounded d/e search. Python arbitrary integers and `isqrt` use no numerical error model or precision tolerance. The published mathematical reduction, not the fact that two programs agree, supplies the infinite-to-finite completeness argument.

## 5. Four targets and 64 positive equivalence witnesses

Use the following quartics, with coefficients in descending order:

| Target | (a,b,c,d,e) | Image on E from a rational point at infinity |
|---|---|---|
| T | (1,0,−20,44,−24) | 2P=(3,5) |
| P | (1,0,−2,4,9) | P=(0,0) |
| Q | (1,0,−8,4,4) | Q=(1,0) |
| R | (1,0,10,−4,1) | P+Q=(−2,−1) |

Every target has (I,J)=(112,−1712). Because a=1, the smooth projective model has rational points at infinity (in the chart x=1/t,z=w/t², w²=1+bt+ct²+dt³+et⁴ at t=0). The source map sends these points to \((3p/4,\pm27r/8)\) on E_IJ, giving the stated images via the inverse isomorphism. T also has rational root x=2, so it accounts for the trivial class directly.

For two forms g,h with leading coefficients a,A and seminvariants p,r and q,s, Proposition 3.6.3 defines
\[
P_e=(32aAI+pq)/3,\quad R_e=rs,
\]
\[
S_e=\{64I(a^2q^2+A^2p^2+aApq)-256aAJ(aq+Ap)-p^2q^2\}/27.
\]
An exact rational root of
\[
u^4-2P_eu^2-8R_eu+S_e=0
\tag{5}
\]
certifies equivalence. The discovery search tries integer u with |u|≤4096 only to **find positive witnesses**. No root-absence or inequivalence conclusion is drawn from that cutoff. The independent checker evaluates 27 times (5) directly with exact integers. All 64 witnesses pass: 8 assigned to T, 14 to P, 20 to Q, 22 to R. The complete coefficient/root table follows in the appendix; the machine-readable certificate (historical local record; not distributed here) contains the same members.

Every member is therefore rationally soluble. The proposed real/modular obstruction branches in the discovery script are unused and earn no verification credit. No finite positive local test or unverified lifting routine is needed; a rational point also gives points at every completion. The reduction may discard real-insoluble classes, but nothing in the deciding 64-member certificate is discarded by a numerical real-root classification.

## 6. Rank conclusion and lower-bound audit

The source completeness theorem and (3)–(5), with T for the trivial class, prove that the two-Selmer envelope, and hence E(Q)/2E(Q), has at most four classes. No assertion of four distinct classes is needed for this upper bound.

For completeness, the earlier lower proof covers all rational denominators. If a rational point with x-coordinate s is twice another rational point, the half's x-coordinate u satisfies the monic polynomial
\[
h_s(u)=u^4-4su^3+(4-4s)u^2+(-2+8s)u+3-s.
\]
For P, s=0 and \(h_0=u^4+(2u-1/2)^2+11/4>0\). For Q and R=P+Q, s=1 and −2, and their polynomials have respective full mod3 value lists (2,2,1). Monicity makes any rational root integral, so neither has a rational root. Thus P,Q,P+Q are all outside 2E(Q). They give three distinct nonidentity cosets, so the quotient has at least four elements.

There is no rational two-torsion: a nonidentity order-two point would give a rational root z of \(z^3+4z^2-32z+16\), whose complete mod5 values are (1,4,1,3,1). Monicity again excludes every rational denominator. The detailed derivation, nonzero tangent denominator and O case are in086, not inferred by sampling halves.

Consequently \(|E(Q)/2E(Q)|=4\). Mordell–Weil finite generation and E(Q)[2]=0 give \(2^r=4\), hence **r=2**. The native061 analytic-order-two theorem remains separate evidence; together they reproduce rank equality at this fixed known example. The proof does not certify that P,Q generate the whole free group: their already proved 2-saturation still allows an odd finite index. No full leading-coefficient formula or order/finiteness of Sha is established here.

## 7. Challenge, reproducibility and learning

The source freeze (historical local record; not distributed here), finite attempt (historical local record; not distributed here) and confirmatory freeze (historical local record; not distributed here) distinguish source review, discovery and verification. Exact CLI records (historical local record; not distributed here) bind tested code/input hashes, commands, exits and stages. Two cases accept (original and reordered complete certificate); eight planted defects reject: omitted member, duplicate, forged root, wrong coefficient, altered target, wrong invariant pair, same-count wrong membership and a Boolean presented as an integer root. All ten expected dispositions matched. No invalid/import-crash case is scored as a detected defect.

Run `python3 artifacts/m02_rank_readiness_cycle089/check_certificate.py artifacts/m02_rank_readiness_cycle089/discovery.json` from the project root. The confirming consumer has no third-party dependency or import from discovery. Discovery is retained unchanged; to reproduce it without overwriting its exclusive-create output, use an isolated local copy. The finite attempt finished in 6.54 minutes including the derivation/checker work, sharing the original 45-minute/100-call run budget. The subsecond enumeration is only an observation, not a controlled performance comparison.

The main uncertainty changed: an upper bound formerly missing locally is now supplied by an exhaustive representative envelope and positive equivalence certificates. The successful mechanism is general quartic descent, not rational two-isogeny, a database integer, the analytic rank, or another small-point search. Do not repeat this census, the086 halving obstructions or the061 derivative just to accrue activity. The next useful obligation is a finite odd-index/full-saturation certificate route using explicit height bounds and a valid torsion prerequisite. Its source readiness and cost must be checked before doing a potentially enormous height search. Imported reduction theorem review debt, shared actor/model and exposure to the known rank remain explicit; no novelty, external human/formal verification or measured improvement is claimed.

## Appendix: exact complete certificate

The generated table below is part of this dated proof record, not an additional independent source.

| # | (a,b,c,d,e) | Target | Integer root u in (5) |
|---:|---|---|---:|
| 1 | (-1, -2, 16, -16, 4) | Q | 48 |
| 2 | (-1, -2, 16, 50, 37) | Q | -48 |
| 3 | (-1, 2, 16, -50, 37) | Q | 48 |
| 4 | (-1, 2, 16, 16, 4) | Q | -48 |
| 5 | (1, -2, -8, 0, 4) | Q | -32 |
| 6 | (1, -2, -8, 18, -5) | Q | 32 |
| 7 | (1, -2, 4, -14, 15) | P | 40 |
| 8 | (1, -2, 4, 8, 4) | P | -40 |
| 9 | (1, -1, -2, 4, 8) | R | -36 |
| 10 | (1, 0, -26, -68, -47) | Q | 48 |
| 11 | (1, 0, -26, 68, -47) | Q | -48 |
| 12 | (1, 0, -20, -44, -24) | T | -160 |
| 13 | (1, 0, -20, 44, -24) | T | 160 |
| 14 | (1, 0, -8, -4, 4) | Q | -64 |
| 15 | (1, 0, -8, 4, 4) | Q | 64 |
| 16 | (1, 0, -2, -4, 9) | P | -16 |
| 17 | (1, 0, -2, 4, 9) | P | 16 |
| 18 | (1, 0, 4, -12, 8) | R | -16 |
| 19 | (1, 0, 4, 12, 8) | R | 16 |
| 20 | (1, 0, 10, -4, 1) | R | -80 |
| 21 | (1, 0, 10, 4, 1) | R | 80 |
| 22 | (1, 1, -2, -4, 8) | R | 36 |
| 23 | (1, 2, -8, -18, -5) | Q | -32 |
| 24 | (1, 2, -8, 0, 4) | Q | 32 |
| 25 | (1, 2, 4, -8, 4) | P | 40 |
| 26 | (1, 2, 4, 14, 15) | P | -40 |
| 27 | (2, -2, -2, 2, 4) | R | -24 |
| 28 | (2, 2, -2, -2, 4) | R | 24 |
| 29 | (3, -2, 4, -8, 4) | P | -88 |
| 30 | (3, 2, 4, 8, 4) | P | 88 |
| 31 | (4, -8, -32, -26, -6) | T | 32 |
| 32 | (4, -8, -32, 98, -68) | T | -32 |
| 33 | (4, -8, -20, -10, -1) | Q | 96 |
| 34 | (4, -8, -20, 58, -35) | Q | -96 |
| 35 | (4, -8, 4, -2, 3) | P | -32 |
| 36 | (4, -8, 4, 2, 1) | P | 32 |
| 37 | (4, -8, 16, -14, 4) | R | -160 |
| 38 | (4, -8, 16, -10, 2) | R | 160 |
| 39 | (4, -4, -8, 0, 1) | Q | -64 |
| 40 | (4, -4, 4, 4, 1) | P | -80 |
| 41 | (4, -2, -2, 2, 2) | R | -72 |
| 42 | (4, -1, 7, 5, 1) | R | -20 |
| 43 | (4, 0, -20, -22, -6) | T | -320 |
| 44 | (4, 0, -20, 22, -6) | T | 320 |
| 45 | (4, 0, -8, -2, 1) | Q | -128 |
| 46 | (4, 0, -8, 2, 1) | Q | 128 |
| 47 | (4, 0, 4, -6, 2) | R | -32 |
| 48 | (4, 0, 4, 6, 2) | R | 32 |
| 49 | (4, 1, 7, -5, 1) | R | 20 |
| 50 | (4, 2, -2, -2, 2) | R | 72 |
| 51 | (4, 4, -8, 0, 1) | Q | 64 |
| 52 | (4, 4, 4, -4, 1) | P | 80 |
| 53 | (4, 8, -32, -98, -68) | T | 32 |
| 54 | (4, 8, -32, 26, -6) | T | -32 |
| 55 | (4, 8, -20, -58, -35) | Q | 96 |
| 56 | (4, 8, -20, 10, -1) | Q | -96 |
| 57 | (4, 8, 4, -2, 1) | P | -32 |
| 58 | (4, 8, 4, 2, 3) | P | 32 |
| 59 | (4, 8, 16, 10, 2) | R | -160 |
| 60 | (4, 8, 16, 14, 4) | R | 160 |
| 61 | (8, -12, 4, 0, 1) | R | 48 |
| 62 | (8, -4, -2, 1, 1) | R | -48 |
| 63 | (8, 4, -2, -1, 1) | R | 48 |
| 64 | (8, 12, 4, 0, 1) | R | -48 |

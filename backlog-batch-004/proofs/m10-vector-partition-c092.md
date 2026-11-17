# Audited historical reading edition

**Current audited claim:** PROVED: For finite represented configurations, a partition into q represented-independent families exists exactly when every subset cardinality is at most the sum of its q ranks.

**Claim ceiling:** Generic norm capacity remains a separate claim; real and rational ranks are distinguished.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M10: inclusive rational spans, finite vector partition, and integer coordinates

**Cycle092; internal analytic audit, 2026-10-28.** The original structural source supplies the inclusive count needed in the later paper. The finite vector-partition criterion and the conversion to integer matrix inputs are proved below. Two weaker count criteria are false, with exact unit-vector counterexamples. The nowhere-denseness lemma remains an explicitly imported published result; its full proof, universal matrix avoidance and a new Euclidean chromatic bound are not established by this audit. No novelty, external human review or formal verification is claimed.

## 1. Objects, source identity and claim ceiling

Fix a positive integer d. Let B_d be the closed, bounded, origin-symmetric convex bodies in R^d with 0 in their interior, with Hausdorff distance computed using Euclidean distance. Each body determines one norm. A typical property holds off a meagre subset of this space; it is not a probability statement or a property of every named norm.

For one norm, U is a finite **set** of unit vectors with u != +/-v for distinct members. A real line contains exactly two unit vectors, so this convention is equivalent to using one signed representative of each distinct unoriented direction. Put

\[
r(S)=\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}S,
\qquad C_U(T)=U\cap\operatorname{span}_{\mathbb Q}T.
\]

The needed condition is

\[
\tag{C} |S|\le d\,r(S)\quad\hbox{for every }S\subseteq U.
\]

The inclusive span formulation is

\[
\tag{I} |C_U(T)|\le d|T|\quad\hbox{for every }T\subseteq U.
\]

Members of T count in C_U(T). Empty sets have rank and cardinality zero.

The original source is Noga Alon, Matija Bucić and Lisa Sauermann, [*Unit and distinct distances in typical norms*, arXiv2302.09058v2](https://arxiv.org/pdf/2302.09058v2), revised 2024-11-07. The accepted 33-page PDF has 484598 bytes, SHA-256 `87801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960`. Physical pages17–19 and23–24 identify the structural input. The later [Alon–Bucić–Davies paper2609.36220v1](https://arxiv.org/pdf/2609.36220v1), physical4–5, uses it for a d-family partition. That paper cites a 2025 journal version; this audit uses the explicitly pinned arXiv version and does not assume identical journal numbering or text.

**Claim ceiling:** the generic statement is conditional on the original nowhere-denseness lemma; all finite linear-algebra implications proved below are complete under their displayed hypotheses, independently of that imported lemma. These results do not reproduce the full generic-norm or Euclidean theorem.

## 2. What the original source actually counts

On original physical17, set m=0. For an integer ell>=1, a rational matrix A of size (d ell+1) by ell, and rational 0<eta<pi/2, the source defines a set A_{A,eta} of norm balls admitting unit vectors v_1,...,v_{d ell+1} in pairwise separated real-line directions such that

\[
v_j=\sum_{i=1}^{\ell}a_{ji}v_i\quad(1\le j\le d\ell+1).
\]

Original Lemma5.3, physical19, states that each such set is nowhere dense. We checked the actual definition and lemma statement, not its entire geometric proof. In the proof of Theorem6.1, physical23–24, the count ranges over j in the **entire** index set, including the spanning indices. Thus the original supplies (I), rather than an outside-only count. The later summary's word “other” does not establish a mathematical error in the original result or in the intended partition.

Here is a complete reduction of uniform capacity to this named source lemma. It also checks the order of quantifiers.

For fixed d>=2 form E_d as the union of A_{A,eta} over all ell, all such rational matrices and all rational eta. This is a countable union: for each finite size, rational matrices form a countable set, as do positive rational separators. **Assuming original Lemma5.3**, E_d is meagre, and the complement is one common comeager class of norm balls.

Suppose a norm violates (C) for some finite direction set and subset S. Its rank r is positive, since S contains nonzero unit vectors. Choose a Q-basis b_1,...,b_r from S. Since |S|>=dr+1, choose dr+1 members of S including that basis and relabel with the basis first. Every chosen member has rational coordinates in b_1,...,b_r. These coordinates give one (dr+1) by r rational A. Pairwise distinct real lines in this finite list have a strictly positive minimum angle; choose a positive rational eta smaller than both that minimum and pi/2. The norm ball then belongs to A_{A,eta}, hence to E_d.

Conversely, any norm in A_{A,eta} has d ell+1 distinct unit directions contained in the Q-span of ell of them. Their rank is at most ell, so their number exceeds d times their rank. Thus **E_d is exactly the set of norms having some finite violation of (C)** under these definitions. The argument ranges over rational relation data, not an unjustified countable enumeration of all real configurations. All finite U are handled simultaneously outside this one E_d.

For d=1 every norm on R has just one non-antipodal unit direction, so (C) holds directly without invoking a lemma stated in a d>=2 section.

Finally, (C) and (I) are equivalent. Given (I), take a basis T of S; then S is contained in C_U(T), so |S|<=d|T|=dr(S). Given (C), apply it to C_U(T). This closure has the same rank as T because it contains T and lies in its span. Hence |C_U(T)|<=dr(T)<=d|T|. This proves both directions, including T=empty.

**Verdict:** the original inclusive-count source dependency is identified and supported. The generic conclusion is `CONDITIONALLY_PROVED` on original Lemma5.3, rather than a claim that its full proof was independently reproduced here. The statement crosswalk is `CERTIFIED_RANGE` at the pinned passages.

## 3. A complete finite vector-partition proof

We prove a slightly more general theorem, so that the contraction step is explicit and no matroid theorem needs to be an unchecked local dependency.

Let E be finite, q>=1, K a field, and for each i=1,...,q let v_i:E->V_i be a vector representation, with

\[
r_i(T)=\dim_K\operatorname{span}\{v_i(e):e\in T\}.
\]

**Theorem.** There is a partition E=I_1 disjoint-union ... disjoint-union I_q with each family (v_i(e))_{e in I_i} independent if and only if

\[
\tag{P}|T|\le\sum_{i=1}^q r_i(T)\quad\text{for every }T\subseteq E.
\]

The theorem concerns vector representations, not a newly claimed proof for all abstract matroids. It is the standard vector-partition result, rederived here without a novelty claim. Repeated vectors and zero vectors are permitted as labeled inputs; (P) decides whether they can be accommodated.

Necessity is immediate: restriction of each independent I_i to T remains independent, so |T|=sum_i |T intersect I_i|<=sum_i r_i(T).

For sufficiency use induction on |E|, simultaneously for all choices of q and representations. The empty case holds. For nonempty E there are two cases.

**A proper nonempty tight set exists.** Let S be such that |S|=sum_i r_i(S), with empty!=S!=E. The restrictions to S satisfy (P), so induction partitions S into independent I_i. Because |I_i|<=r_i(S) and their sums are equal, |I_i|=r_i(S) for every i. Consequently I_i spans L_i=span(v_i(S)).

On E\S use the quotient representations v_i(e)+L_i in V_i/L_i. For any T contained in E\S their ranks are

\[
r_i'(T)=r_i(S\cup T)-r_i(S).
\]

Summing and applying (P) to S union T gives sum_i r_i'(T)>=|S|+|T|-|S|=|T|. Induction partitions E\S into families J_i independent in these quotients. Then I_i union J_i is independent in V_i: project any relation to V_i/L_i to force all J_i coefficients to vanish, and use independence of I_i for the rest. These unions give the required partition.

**No proper nonempty tight set exists.** Choose e in E. Applying (P) to {e} shows that v_j(e)!=0 for at least one j. Delete e from every ground set, and for representation j also quotient by the line K v_j(e). In the other representations only delete e. For every nonempty T contained in E\{e}, T is a proper subset of E and is not tight. Since all ranks are integers,

\[
\sum_i r_i(T)\ge |T|+1.
\]

Quotienting one representation by one line lowers its rank by at most one. Thus the new representations satisfy (P) on E\{e}; the empty T also satisfies it. Induction partitions the smaller set into independent J_i. Append e to J_j. Its image is nonzero, and the quotient independence of J_j ensures that J_j union {e} is independent before the quotient. The other J_i need no change. This completes the induction, including |E|=1.

Specialize to q=d and identical representations v_i(e)=u_e over Q. Condition (P) becomes (C), so U partitions into d Q-independent families. Necessity also proves that an actual violating subset blocks every proposed partition, not only a particular greedy algorithm.

**Verdict:** `PROVED` internally for every finite vector configuration under the displayed all-subset rank condition. There is no numerical approximation, sampling of subsets, or external genericity assumption in this theorem.

## 4. Exact attacks on weakened criteria

All examples below are analytic. No finite search or floating-point rank calculation is being presented as proof.

### 4.1 A whole-family count misses an obstructing subset

In the physical plane with the infinity norm, define

\[
S=\{(1,-1),(1,-1/2),(1,0),(1,1/2),(1,1)\},
\qquad w=(1,\sqrt2/2),\qquad U=S\cup\{w\}.
\]

All six vectors have norm1 and are pairwise non-antipodal. The five rational vectors have Q-rank2: they lie in Q^2, and (1,0) and (1,1) are independent. The irrational vector w is outside their Q-span, since its second coordinate is irrational. Therefore r(U)=3, and the whole-family count gives |U|=6=2r(U). Nevertheless |S|=5>4=2r(S). Each independent family can contain at most two members of S, so two independent families cannot cover U.

This refutes the implication “|U|<=d r(U) implies a d-family independent partition,” even for non-antipodal unit vectors. It does not refute the typical-norm theorem: the infinity norm is not assumed to belong to the good class.

### 4.2 An outside-only interpretation loses one family

Use just the five-vector S above and d=2. For T of size1, its Q-span contains no other member of S, because any two members have nonzero determinant. For |T|>=2, the number of members in S\T lying in span_Q(T) is at most 5-|T|<=3<=2|T|. The empty T has no such member. Thus the outside-only inequality holds for every T, although S cannot partition into two independent sets.

In general an outside-only bound |C_U(T)\T|<=d|T| yields only |C_U(T)|<=(d+1)|T|. The partition theorem then supplies at most d+1 independent families; d families do not follow. This explains why consulting the original inclusive statement was necessary. It is a counterexample to a weakened interpretation, not a counterexample to either published proof under the original input.

### 4.3 Rational rank is not physical dimension

The three Euclidean unit vectors (1,0), (0,1), and (1/sqrt2,1/sqrt2) have real rank2 and rational rank3. Indeed a rational relation forces both first coefficients to equal minus the third divided by sqrt2, which is rational only when the third is zero. The other two coefficients then vanish. Thus even a fixed physical plane can require an abstract rational coordinate space of dimension N>2.

The irrationality used here is exact: if sqrt2=a/b in lowest positive integer terms, a^2=2b^2 makes a even and then b even, a contradiction. No decimal approximation is used in these rank calculations.

### 4.4 The specified Euclidean norm actually fails this capacity condition

For rational t in [0,1], put

\[
u(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2},0,\ldots,0\right)\in\mathbb R^d.
\]

The denominator is positive and the sum of the first two squared coordinates is ((1-t^2)^2+4t^2)/(1+t^2)^2=1. The coordinates are rational. These vectors lie in the first quadrant, are pairwise non-antipodal, and are distinct: t equals the second coordinate divided by one plus the first. Choose any 2d+1 distinct rational parameters including 0 and1. The resulting unit family has Q-rank exactly2, since u(0)=e_1 and u(1)=e_2 and all its vectors lie in Qe_1+Qe_2. Its cardinality 2d+1 exceeds d times that rank.

For d=2 a fully displayed five-vector witness is (1,0), (0,1), (3/5,4/5), (4/5,3/5), (5/13,12/13). The last three squared-norm checks are (9+16)/25=1, (16+9)/25=1 and (25+144)/169=1. Thus for every d>=2 the Euclidean norm lies in the exceptional set E_d constructed in §2. This is a direct obstruction to transferring this particular capacity-based route to the specified Euclidean norm. It supplies no lower bound for its chromatic number: failure of a sufficient structural hypothesis does not imply failure of a colouring by another method.

**Verdicts:** the whole-family and outside-only shortcuts are `FALSIFIED` by explicit restricted counterexamples. Replacing rational rank by real rank is not a valid field change.

## 5. From the partition to integer matrix inputs

Let G be a finite connected graph with a placement p:V(G)->R^d such that every edge difference belongs to +/-U. Suppose U satisfies (C). Edgeless graphs are trivially colourable and are excluded from the following N>=1 construction. Partition U into d independent families as above.

Move any vector outside the span of the first family into that family, removing it from its previous family. Adding it preserves independence of the first family; removing it preserves independence of its old family. This finite process terminates with the first family B a basis of W=span_Q U. Put N=dim_Q W. For each other family, if its span is not W, some member of B lies outside that span; append a copy of such a member. Repeat until each family is a basis of W. The completed families can overlap, and are not a disjoint partition. There are q=d basis families, each with N rows; N is not d.

Take abstract Q-coordinates relative to B. Every member of U has rational coordinates. Choose a positive integer D clearing all their denominators, and replace the coordinate basis B by B/D, meaning each physical basis vector is divided by D. Every coordinate is thereby multiplied by D, and all original and added rows become integral. Each completed row matrix A_s is N by N, integral and invertible. Its determinant need not be +/-1; unimodularity is not required.

Translate a chosen graph vertex p_0 to the origin. Along a path from p_0, every increment is +/-u for u in U. Hence every translated vertex has integral coordinates in B/D. Connectedness justifies this assertion; disconnected graphs are treated component by component. These are coordinates of the abstract Q-space W. When N>d they are not a real coordinate basis of the physical R^d, and a later real phase vector need not define a continuous real-linear functional on the physical plane.

Thus (C) gives exactly the integer input contract of the 2026 matrix lemma, without using that lemma's conclusion. This is `PROVED` as a finite implication.

For clarity, if one additionally assumes the universal integer avoidance theorem

\[
\tag{A}
\forall A_1,\ldots,A_q\in\mathbb Z^{N\times N}\text{ invertible},\quad
\exists x\in\mathbb R^N:\quad
\operatorname{dist}((A_sx)_j,\mathbb Z)\ge1/(2q)\ \forall s,j,
\]

then colour a vertex with integer coordinate z by floor(2d {z dot x}). The bins are half-open. If two adjacent vertices occupied the same bin, the difference of their fractional phases would have absolute value strictly less than 1/(2d). The phase of their edge, however, is a signed matrix row dot x, of distance at least 1/(2d) from Z. This is a contradiction. Equality at the avoidance threshold is allowed. Component-wise constructions use the same palette of 2d labels.

This last finite colouring implication is `CONDITIONALLY_PROVED` on (A). Cycle091 checks supplied positive certificates; it does not prove that a certificate or balanced weights exist for every matrix input. General shifts are required by the published induction but the graph reduction uses zero shifts. Infinite-graph compactness and original genericity remain separately named dependencies, not hidden consequences of a finite computation.

## 6. Dependency and verification ledger

| Claim | Evidence and outcome | Limit |
|---|---|---|
| Original count is inclusive and uniform off one exceptional set | Pinned definitions/lemma statement/actual §6 count; `CERTIFIED_RANGE` | Journal-version text equivalence not asserted |
| Bad finite configurations equal the countable rational-relation union | Complete basis/angle/countability proof above; `PROVED` reduction | Nowhere-denseness itself imported |
| Generic inclusive capacity | `CONDITIONALLY_PROVED` on original Lemma5.3 | Its full geometric proof not independently replayed |
| All-subset vector-partition criterion | Complete induction above; `PROVED` | Finite represented configurations, not a new abstract-matroid claim |
| Whole-family and outside-only substitutes | Explicit infinity-norm counterexamples; `FALSIFIED` | Weaker rules, not the source result |
| Euclidean norm satisfies the capacity input | Rational unit-circle family refutes it for every d>=2; `FALSIFIED` | Obstructs this route, not a chromatic-number bound |
| Integer matrices/vertex coordinates | Basis extension and exact denominator argument; `PROVED` | No universal avoidance witness generated |
| Finite 2d colouring | Complete conditional bin argument | Universal (A) not reproduced in this cycle |
| New Euclidean bound, full generic theorem, novelty or outside/formal review | `NOT_TESTED` | No promotion from these local results |

The exact vector calculations and induction were performed analytically. Tools retrieved sources, extracted/rendered PDF pages, and checked record integrity; no mathematical search, numerical rank program, solver or finite-certificate campaign was run. Source passages and earlier results were visible throughout: this is internal review, not blind reproduction or independent human review. A second representation of the same PDF is not another mathematical source.

## 7. What changed and what should not be repeated

The inclusive-count uncertainty is resolved at the pinned source scope. The finite d-family partition and integer-coordinate obligations now have explicit local proofs, with empty/tight/quotient/field cases covered. The weak outside-only and whole-family routes are decisively invalid and should not be repeated without changing the claim.

The next discriminating obligation is universal integer avoidance: balanced positive weights and attainment in the strict-subset case, then the proper tight-subset induction with shifted targets. The exact source formulas on 2026 physical6–9 are already available and have been reread as a readiness check. This changes the mechanism from verifying supplied finite witnesses to proving existence for every admissible matrix input. It does not justify a matrix grid, an installation, or a new Euclidean claim.

The source/corpus extents and hashes are in the cycle092 inspection register (historical local record; not distributed here). Public/owned source review adds zero volume-estate paths; pass047 and its UNKNOWN content/source denominators remain unchanged.

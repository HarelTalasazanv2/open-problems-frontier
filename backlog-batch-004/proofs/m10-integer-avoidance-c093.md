# Audited historical reading edition

**Current audited claim:** PROVED: For q nonsingular integral N-by-N matrices and arbitrary real shifts, one x gives every row phase distance at least 1/(2q) from Z.

**Claim ceiling:** Known theorem reproduced analytically; rational extension and shifted sharpness are stated separately; no new Euclidean chromatic bound.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M10: universal integer avoidance, sharp shifted margin, and a balancing obstruction

**Cycle093, 2026-10-28; internal analytic reproduction of a known theorem.** `PROVED` below: simultaneous avoidance for any q nonsingular integer N by N matrices and arbitrary real shifts, with non-strict margin1/(2q). The proof covers proper tight subsets, strict subsets, attainment, ties, signs and endpoints. This closes the matrix-existence input of the locally proved finite colouring reduction. It is not a new Euclidean chromatic bound, a full reproduction of the original geometric genericity theorem, an algorithmic complexity result, or a claim of novelty, external human review or formal verification.

The submitted result is Lemma7 of Noga Alon, Matija Bucić and James Davies, [*Hadwiger–Nelson Problem for Typical Norms*,2609.36220v1](https://arxiv.org/pdf/2609.36220v1), physical6–9. The pinned21-page PDF is583970bytes, SHA-256 `c93b095812a73f0490107bf17d2a09b74d8718a1ca05736ee7b6bad2e7ccb547`. Its source and proof were visible throughout this audit; this is not blind reproduction. The proof is reconstructed with elementary finite-dimensional identities and explicit edge cases, not inferred from agreement of computer runs.

## 1. Exact statement and conventions

For a real number t, write dist(t,Z)=min_{k in Z}|t-k|. Equivalently dist(t,Z)>=delta, for 0<=delta<=1/2, means t belongs to [delta,1-delta]+Z.

**Theorem.** For every q,N>=1, every A_1,...,A_q in Z^{N by N} with nonzero determinant, and every b_1,...,b_q in R^N, there is x in R^N such that

\[
\tag{1} A_sx-b_s\in[1/(2q),1-1/(2q)]^N+\mathbb Z^N
\quad(1\le s\le q).
\]

All rows are labeled, including repeated rows in different matrices. The matrices are nonsingular, not assumed unimodular. Shifts are arbitrary real vectors. The conclusion permits equality at the two endpoints. Logarithms used in the proof are natural logarithms.

We prove (1) without invoking a general matrix-scaling theorem, the genericity of any norm, or a computational search. Cauchy–Binet, finite-dimensional orthogonal complements, continuity on a compact cube and elementary differentiation suffice. These standard identities are stated where used.

## 2. Rank facts and the dimension induction

Stack the rows as a_i^T, i=1,...,m, with m=qN, and stack the shifts as beta_i. Let r(J) be the real row rank of the rows labeled by J. Each of the q original bases contributes at most r(J) members to J, so

\[
\tag{2} |J|\le q r(J)\quad(J\subseteq[m]).
\]

A set is tight when equality holds. Every row is nonzero. A nonempty proper tight set therefore has rank r with 1<=r<N: rank0 would force emptiness, while rankN and tightness would give |J|=qN=m, contradicting properness.

For q=1 set x=A_1^{-1}(b_1+(1/2)1). This proves the theorem for all N in that case. For fixed q>=2 use strong induction on N. The strict-subset case below needs no smaller-dimensional theorem. When N=1 there is no nonempty proper tight subset, because every nonempty subset has rank1 and fewer than q members. Thus that case also supplies the induction base without a measure argument at an equality endpoint.

## 3. Proper tight subsets: the integral block reduction

Suppose a nonempty proper tight set J has rank r. Its qr rows meet each original basis in exactly r rows, since each intersection has size at most r and the total size is qr. Those r rows span L=span_R{a_i:i in J} in every basis.

Choose r integer columns spanning L, by selecting independent transposes of rows in J. The equations defining L-perpendicular have integer coefficients, so ordinary elimination over Q gives a rational basis of L-perpendicular. Clearing each basis vector's denominators gives N-r integer columns spanning it. Assemble these two column lists into P. Since L and L-perpendicular are complementary, P is nonsingular and integral. No assertion det(P)=+/-1 is needed.

Permute each original matrix's rows and its shift vector in the same way, putting the r rows from J first. Orthogonality gives

\[
A_sP=\begin{pmatrix}C_s&0\\D_s&F_s\end{pmatrix},
\qquad b_s=\binom{b_s'}{b_s''}.
\]

Every block is integral; C_s and F_s are nonsingular square matrices of sizes r and N-r. Indeed A_sP is nonsingular and the determinant of this block triangular matrix is det(C_s)det(F_s). Both sizes are strictly between0 and N.

Apply induction to C_1,...,C_q with shifts b_s', obtaining y with the required margin for all C_sy-b_s'. Fix this y. Apply induction to F_1,...,F_q with shifts **b_s''-D_sy**, obtaining z for all F_sz-(b_s''-D_sy). Set x=P(y,z)^T. The upper and lower blocks of A_sx-b_s are exactly the two expressions just controlled, so (1) follows. The induced shifts need not be rational, which is why the theorem quantifies arbitrary real shifts. This completes the tight branch.

## 4. Strict subsets: construct balanced positive weights

Assume now that no nonempty proper subset is tight. By (2) and integrality of ranks,

\[
\tag{3} q r(J)-|J|\ge1
\quad(\varnothing\ne J\subsetneq[m]).
\]

For t in R^m put

\[
M(t)=\sum_{i=1}^m e^{t_i}a_i a_i^T,
\qquad F(t)=\log\det M(t)-\frac1q\sum_i t_i.
\]

M(t) is positive definite: for any nonzero v, the spanning rows cannot all have a_i^T v=0, so v^TM(t)v=sum_i e^{t_i}(a_i^Tv)^2>0. Consequently F is smooth and finite. Because m=qN,

\[
F(t+c1)=F(t)+Nc-(m/q)c=F(t).
\]

It suffices to minimize F on H={t:sum_i t_i=0}.

Let B range over all N-element row bases. Cauchy–Binet applied to the matrix with rows e^{t_i/2}a_i^T gives

\[
\tag{4}\det M(t)=\sum_{B}(\det A_B)^2
 \exp\Big(\sum_{i\in B}t_i\Big).
\]

Every nonzero determinant here is an integer, so its square is at least1. Thus for any such B,

\[
\tag{5}F(t)\ge\sum_{i\in B}t_i-\frac1q\sum_i t_i.
\]

Relabel so t_1>=...>=t_m; the strict rank condition concerns every subset and is unaffected. Scan the rows in that order, retaining a row precisely when it increases the span. After k rows, the retained rows span the first k rows, and their number is r_k=r({1,...,k}). The final retained set B is an N-element basis, with |B intersect {1,...,k}|=r_k. Writing each t_i as t_m plus its successive gaps gives the exact telescoping identities

\[
\sum_{i\in B}t_i=Nt_m+\sum_{k=1}^{m-1}(t_k-t_{k+1})r_k,
\quad
\frac1q\sum_i t_i=Nt_m+\sum_{k=1}^{m-1}(t_k-t_{k+1})\frac{k}{q}.
\]

All gaps are nonnegative. Equations(3) and(5) therefore imply

\[
\tag{6}F(t)\ge\frac1q\sum_{k=1}^{m-1}(t_k-t_{k+1})
=\frac{t_1-t_m}{q}.
\]

On H, t_m<=0<=t_1, so t_1-t_m>=||t||_infinity. Hence F tends to infinity along every unbounded sequence in H. It attains a minimum there: a nonempty sublevel set F<=F(0) is closed and bounded in this finite-dimensional hyperplane, and thus compact. Translation invariance makes its minimizing point t* a global minimum on all R^m as well.

Define w_i=e^{t_i*}>0, M=sum_i w_i a_i a_i^T, and lambda_i=w_i a_i^TM^{-1}a_i. The rank-one determinant identity

\[
\det(M+uv^T)=\det M\,(1+v^TM^{-1}u)
\]

gives

\[
F(t*+s e_i)-F(t*)
=\log(1+(e^s-1)\lambda_i)-s/q.
\]

The derivative at s=0 vanishes, proving

\[
\tag{7}\lambda_i=1/q\quad(1\le i\le m).
\]

This construction requires strictness in(3). No uniqueness or effective computation of t* is asserted. Integrality supplied the convenient determinant lower bound1; for a fixed real full-rank row configuration one could replace it by the minimum positive squared basis determinant, obtaining an additional fixed logarithmic constant in(6). That observation concerns weights, not the later existence of a periodic distance minimum.

## 5. Attainment, ties and the exact signed comparison

With these positive weights define

\[
\Phi(x,k)=\sum_i w_i(a_i^Tx-\beta_i-1/2-k_i)^2,
\quad x\in\mathbb R^N,\ k\in\mathbb Z^m.
\]

For fixed x the minimum over k is

\[
g(x)=\sum_i w_i\operatorname{dist}(a_i^Tx-\beta_i-1/2,\mathbb Z)^2.
\]

Distance to a closed set is continuous, and every a_i is integral, so g is continuous and Z^N-periodic. It attains a minimum on [0,1]^N, which by periodicity is a global minimum on R^N. At a minimizing x, choose each k_i to be any nearest integer. The resulting pair (x,k) globally minimizes Phi. This choice is valid even at a tie; the minimized function g need not be differentiable.

Put r_i=a_i^Tx-beta_i-1/2-k_i. Holding k fixed, the smooth quadratic Phi has a minimum at x, so

\[
\tag{8}\sum_i w_i r_i a_i=0.
\]

For any index j let h=w_j M^{-1}a_j. For either sigma in {+1,-1}, compare with the admissible pair (x+sigma h,k+sigma e_j). Expanding exactly and using(8) gives

\[
\begin{aligned}
\Delta_{j,\sigma}
&=2\sigma\sum_i w_i r_i(a_i^Th-\mathbf1_{i=j})
  +h^TMh-2w_ja_j^Th+w_j\\
&=-2\sigma w_jr_j+w_j(1-\lambda_j)\\
&=w_j(1-\lambda_j-2\sigma r_j).
\end{aligned}
\]

Both differences are nonnegative by global minimality. In fact x+sigma h also solves the normal equations for its changed integer target, since Mh=w_ja_j, but only its admissibility is needed for the comparison. The two signs and w_j>0 imply

\[
|r_j|\le(1-\lambda_j)/2=(q-1)/(2q).
\]

Thus a_j^Tx-beta_j belongs to k_j+[1/(2q),1-1/(2q)], exactly(1). This proves the strict branch and completes the dimension induction. It does not replace global minimality by stationarity or nearest rounding; the earlier counterexamples to that weaker rule remain valid.

## 6. Why the tight branch cannot be replaced by global balancing

Here is a new exact obstruction to the stronger shortcut that **every** admissible union of q integer bases has positive weights with all lambda_i=1/q.

Take q=N=2 and labeled rows e_1,e_2,e_1,e_1+e_2, partitioned as

\[
A_1=I_2,\qquad A_2=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

Both determinants are1. For arbitrary positive w_1,...,w_4 put s=w_1+w_3. Then

\[
M=\begin{pmatrix}s+w_4&w_4\\w_4&w_2+w_4\end{pmatrix},
\quad\det M=s(w_2+w_4)+w_2w_4.
\]

The leverage sum of the two repeated e_1 rows is

\[
\lambda_1+\lambda_3
=\frac{s(w_2+w_4)}{s(w_2+w_4)+w_2w_4}<1.
\]

It therefore cannot equal the value1 forced by lambda_1=lambda_3=1/2. The two repeated rows form a proper tight rank1 set. This refutes unconditional positive balancing; it does **not** refute avoidance. For example, with zero shifts x=(1/3,1/3) gives phases1/3,1/3,1/3,2/3, all of distance1/3 from Z. The theorem's tight-subset induction remains valid for arbitrary shifts as well.

Zero rows would make an unrestricted singular-matrix version false: a zero row with zero shift has distance0 from Z. Such rows are excluded by nonsingularity. This is a simple assumption canary, not evidence about a source defect.

## 7. Sharpness and sufficient extensions

**The shifted uniform constant is sharp.** Fix any q,N>=1. Let all A_s=I_N and b_s=((s-1)/q)1. On the circle, the q equally spaced points (s-1)/q leave gaps of length1/q. Every real x_j is within1/(2q) of one of those points modulo Z. Thus no x can make every coordinate distance strictly larger than1/(2q). Conversely x=(1/(2q))1 has minimum distance exactly1/(2q), attaining the bound. This is a matching analytic upper example for the **arbitrary-shift matrix theorem**. It proves neither optimality of a zero-shift subproblem nor a chromatic lower bound for any norm.

**Rational matrices are also covered.** For nonsingular rational A_s choose one positive integer D such that D A_s is integral for every s. Apply(1) to these matrices, obtaining y, and put x=D y. Then A_sx-b_s=(D A_s)y-b_s. The shift vectors remain arbitrary real vectors. In this normalization periodicity may use D Z^N rather than Z^N. We do not claim that this proof establishes the same attainment assertion for arbitrary real matrices without a common rational lattice.

**A row-family sufficient condition.** Let rational rows a_i in Q^N span Q^N, with arbitrary real beta_i. If |J|<=q rank_Q{a_i:i in J} for every labeled subset J, the finite vector-partition theorem proved092 partitions the rows into q independent families. Extend each to a basis by copying rows from a fixed rational basis; retain all original shifts and assign arbitrary shifts to added copies. The completed bases are nonsingular rational matrices. The rational version of(1) supplies the desired margin for every original row. This is a sufficient condition, not a claimed necessary-and-sufficient classification of avoidance for fixed shifts.

## 8. The finite colouring bridge is now proved

The092 basis/denominator argument converts a finite graph whose non-antipodal unit-direction family U satisfies |S|<=d rank_Q(S) for all S into q=d nonsingular integer N by N row matrices and integer vertex coordinates. Apply the theorem just proved with zero shifts. Give coordinate z the colour floor(2d {z dot x}). If adjacent vertices had the same colour, their fractional phases would lie in the same half-open interval of length1/(2d), making the edge phase have distance **strictly less** than1/(2d) from Z. Its corresponding matrix row has distance at least1/(2d), a contradiction. Disconnected components use the same palette independently. Equality margins are safe because the bins are half-open.

Thus every such finite graph is2d-colourable, `PROVED` internally under its explicit structural hypothesis. Unlike the earlier conditional step, it no longer imports universal matrix existence. Applying it to a comeager class of norms still depends on the original geometric nowhere-denseness lemma; passing from all finite subgraphs to an infinite graph still requires a correctly stated graph compactness theorem. Those dependencies are not silently promoted here. The092 rational unit-circle family shows that the specified Euclidean norm fails this structural hypothesis for every d>=2, so this is not a new Euclidean bound.

## 9. Review ledger and reproducibility limits

| Obligation | Result | Decisive checks and limits |
|---|---|---|
| Universal integer avoidance with arbitrary real shifts | `PROVED` internally | Complete dimension induction and smooth finite-dimensional proof above |
| Strict-case positive balancing and attainment | `PROVED` internally | All subsets, integer slack, Cauchy–Binet signs, global minimizer, natural-log derivative |
| Proper tight sets | `PROVED` internally | 1<=r<N, every basis contributes r, integer nonsingular P, smaller blocks and shifted targets |
| Ties and signed comparison | `PROVED` internally | A global pair exists; differentiate with k fixed; both signs; no smoothness assumption on g |
| Positive balancing for every admissible input | `FALSIFIED` | Exact repeated-row example and strict leverage-sum inequality |
| Uniform arbitrary-shift margin exceeds1/(2q) | `FALSIFIED` | Equally spaced shifts, including equality attainment |
| Rational-matrix and rank-cap row-family sufficient extensions | `PROVED` internally | Explicit scaling; prior complete finite vector-partition proof |
| Finite2d colouring under all-subset capacity | `PROVED` internally | Integer coordinates, zero shifts and half-open-bin contradiction |
| Full original genericity, infinite compactness, full21-page theorem, new Euclidean value | Not established by this audit | Separate imported/unreproduced obligations remain |

All calculations here are exact analytic arguments. There were no new mathematical numerical runs, finite-grid claims, optimizations by software or solver certificates. Retrieval, PDF rendering and hash/ledger checks are record operations, not mathematical proof verification. The source/expected statement were visible, and the reviewer is the same actor/model; no blind, external expert or formal check occurred. No benchmark, gain ratio or novelty claim is made.

The inspection register (historical local record; not distributed here) distinguishes source rereads from the bounded new geometric-source increment. The dated report (historical local record; not distributed here) records that increment and the remaining exact dependencies. Prior091 and092 proof/counterexample artifacts are preserved. A failed stronger shortcut is not a defect in the source's two-branch proof.

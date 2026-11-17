# Audited historical reading edition

**Current audited claim:** PROVED: Every norm in the stated rational-capacity class admits a set-theoretic 2d-colouring of its full unit-distance graph.

**Claim ceiling:** Known generic upper theorem; no measurability, typical equality in every dimension or named Euclidean norm claim.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Finite-to-infinite colouring for the known generic norm class

2026-10-30 UTC, cycle102. **PROVED internally under the named prior internal proofs and classical ZFC:** for fixed d≥2, every norm body in the101 generic rational-capacity class has a unit-distance graph on all of R^d with a proper colouring in2d colours. This reconstructs the known upper theorem. It is not a new Euclidean bound, generic equality, a measurable colouring, or a full reproduction of the source paper. External/formal claim promotion remains held.

The submitted packet (historical local record; not distributed here), fresh freeze (historical local record; not distributed here) and dependency custody (historical local record; not distributed here) specify the exposed inputs. This is an internal consumer crosswalk and proof, not blind reproduction or independent human review.

## 1. Statement, conventions and dependencies

Fix d≥2 and a compact convex origin-symmetric norm body B⊂R^d, with0 in its interior. Write ||·||_B for its norm and let H_B have vertex set R^d and edges between distinct x,y with ||x−y||_B=1. Colours are arbitrary set-theoretic functions, without measurability, periodicity or an effective construction requirement.

Let G_d be the101 class for which every finite S⊂∂B on distinct unoriented real lines satisfies

\[
 |S|\le d\,\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}S.
\]

The101 proof establishes that G_d is comeager in the Hausdorff space of norm bodies and contains its explicit dense G_delta subset R_d. Rank here is rational rank, which can exceed the physical dimension. Opposite unit differences use one representative of their common unoriented line.

**Theorem.** If B∈G_d, then χ(H_B)≤2d. Consequently the set of norms with this upper bound is comeager and contains R_d. No assertion that the entire colouring class is itself G_delta is needed. The d1 upper bound2 holds directly for every one-dimensional norm.

Inputs are [092 finite vector partition and integer preparation](m10-vector-partition-c092.md), [093 universal integer avoidance](m10-integer-avoidance-c093.md) and [101 allfinite generic Q-capacity](m10-generic-q-capacity-c101.md). Their exact contracts and original manifest identities were checked102. They remain prior internal proofs, not newly supplied external review. The graph compactness argument needed below is proved here from the maximal principle of Zorn, explicitly used as a classical choice foundation; no imported de Bruijn–Erdős or Tychonoff theorem is used as an unexamined application premise.

## 2. Every finite subgraph: matching the consumer

Let H be any finite subgraph of H_B. An empty or edgeless graph has a constant proper colouring. Otherwise treat each nontrivial connected component separately, using the same palette of2d labels. It suffices to consider one finite connected graph with an edge.

Choose one signed representative from each unoriented unit direction appearing on its edges, obtaining finite U. Every subset of U satisfies the capacity inequality because the **same fixed** B belongs to G_d. The092 finite vector-partition theorem therefore partitions U into d Q-linearly independent families I_1,…,I_d. This is an all-subset criterion; a whole-family cardinality bound alone would not suffice.

If I_1 does not span W=span_Q(U), move a member outside its span from its present family into I_1. Adding it preserves independence of I_1, and deleting it preserves independence of its old family. Each move increases |I_1|, so the finite process stops with a basis B_1 of W. Set N=dim_Q(W)≥1. Each other independent family is extended to a basis of W by adjoining members of B_1 outside its current span. Those completed families may overlap: copied rows are allowed. Every original direction remains a row of at least one completed family.

Use rational coordinates in B_1. A positive integer D clears all denominators of these finitely many rows. Replace each basis vector b by b/D: coordinates are **multiplied by D**, not divided. The completed row matrices A_1,…,A_d are integral N×N matrices of nonzero determinant. They need not be unimodular. This is an abstract rational coordinate basis, not a real basis of the physical space when N>d.

Translate a chosen component vertex p_0 to zero. A path from p_0 expresses any translated vertex as an integral sum of signed unit directions, hence its coordinates z_v in B_1/D belong to Z^N. Path independence follows because two such paths have physically zero difference and the coordinate basis is Q-linearly independent. On each edge vw, z_v−z_w is the positive or negative of a row occurring in some A_s.

Apply the093 theorem with q=d and **all shifts zero**. There is x∈R^N with

\[
 \operatorname{dist}((A_sx)_j,\mathbb Z)\ge\frac1{2d}
 \quad\text{for all }s,j.
\]

Set k=2d, δ=1/k, and give v colour

\[
 c(v)=\lfloor k\{z_v\cdot x\}\rfloor\in\{0,\ldots,k-1\}.
\]

The bins [j/k,(j+1)/k) are half-open. If adjacent v,w have the same colour, their fractional phases r_v,r_w obey |r_v−r_w|<δ. Their edge phase differs from r_v−r_w by an integer, so its distance from Z is at most |r_v−r_w|<δ. But it is a signed matrix-row phase of distance at least δ. This is a contradiction. Equality at the avoidance threshold is safe because the same-bin bound is strict.

This proves the required finite colouring for every finite subgraph. Component translations, matrices, N and x can vary with the finite graph. This step does **not** produce compatible finite colourings or one finite-dimensional phase vector for the entire uncountable graph. The next section supplies the global colouring by a different mechanism.

## 3. Graph compactness for arbitrary vertex sets

We prove the precise form needed. Let H=(V,E) be any set-sized simple graph and let a **single fixed finite** k≥1 be given. If every finite induced subgraph has a proper colouring in K={0,…,k−1}, then H has one. The converse follows by restriction.

Let J consist of all pairs (F,a), where F is a finite subset of V and a:F→K is a proper colouring of H[F]. In particular the empty pair belongs to J. For each finite T⊂V define the tail

\[
 C_T=\{(F,a)\in J:T\subseteq F\}.
\]

Each C_T is nonempty by finite colourability, and C_T∩C_S=C_(T∪S). Thus supersets of these tails form a proper filter F_0 on J: they contain J, exclude the empty set, are upward closed and are closed under finite intersections. Using **all pairs** avoids silently choosing one colouring for every finite set.

Consider the proper filters on J containing F_0, ordered by inclusion. This is a nonempty set. A chain has a proper-filter union: finitely many members of that union lie together in one chain element, giving intersection closure, and the empty set occurs in none. The other filter axioms persist. Zorn's maximal principle supplies a maximal proper filter U containing F_0. This is the explicit use of classical choice, not a sequential compactness assertion.

For any A⊂J, either A∈U or J\A∈U. Indeed, if A∉U and every B∈U meets A, then

\[
 \{S\subseteq J:\exists B\in U,\ B\cap A\subseteq S\}
\]

is a proper filter strictly extending U and containing A, contrary to maximality. Hence some B∈U is disjoint from A; by upward closure J\A∈U. Both A and its complement cannot belong to a proper filter.

For v∈V and i∈K put

\[
 A_{v,i}=\{(F,a)\in J:v\in F,\ a(v)=i\}.
\]

These k sets are disjoint and their union is C_{\{v\}}∈U. At least one belongs to U: otherwise all their complements would belong to U, whose finite intersection with C_{\{v\}} is empty. At most one belongs to U by disjointness and properness. Define c(v) as the unique i with A_(v,i)∈U. Unique definability gives the whole function c without an additional selection of arbitrary colours.

If vw is an edge and c(v)=c(w)=i, then A_(v,i)∩A_(w,i) is empty, since every pair in that intersection would encode a proper finite colouring containing both endpoints with equal colours. Yet both sets belong to U, a contradiction. Thus c is proper. This works for uncountable V, disconnected graphs and V=∅. No enumeration or convergent subsequence of vertices/finite colourings is required.

The conclusion is under classical ZFC, with Zorn explicitly named. No computable ultrafilter, measurable colour classes, or constructive-choice-free theorem is asserted.

## 4. Application to the fixed norm and generic class

For B∈G_d, Section2 gives the Section3 hypothesis for H_B with the **one palette** K of size2d. Apply Section3 to V=R^d. Hence χ(H_B)≤2d for every B∈G_d. By101, G_d contains the dense G_delta class R_d and has meagre complement. The class of norms satisfying this chromatic upper bound contains G_d, so its complement is a subset of that meagre complement and is meagre too. This is the known comeager upper-colouring theorem, reconstructed internally.

For d=1 let B=[−a,a], a>0. Define c(t)=floor(t/a) modulo2, using the usual floor also for negative t. Unit-distance neighbours differ by ±a, so their floor values differ by ±1 and their colours differ. Thus the claimed upper bound2 also holds directly there.

Generic upper2d does not imply generic equality2d or reproduce the source's nonempty-open lower-bound theorem. The particular Euclidean norm fails the092/101 capacity input, so this route licenses no new conclusion about its chromatic value. Failure of that sufficient input is not a colouring lower bound.

## 5. Exact adversarial controls

**FALSIFIED — closed bins with the least containing index preserve the endpoint argument.** Take d=q=2,N=1,A_1=A_2=[1],x=1/4 and zero shifts. These admissible rows have distance exactly1/4 from Z. On any one unit edge with vertex coordinates0,1, the fractional phases are0,1/4. Closed bins [j/4,(j+1)/4] with the least available bin index give both endpoints colour0. The actual half-open rule gives0 and1. This is a counterexample to the altered rule, not to the literal theorem or source.

**FALSIFIED — arbitrary shifted avoidance can replace zero shifts in this graph consumer.** In the same matrix input choose x=0 and b_1=b_2=−1/4. Shifted phases are1/4, satisfying the matrix theorem, while the ordinary vertex phases on the unit edge are both0. It is the unshifted row phase that must avoid integers for the stated graph colouring. General shifts remain valid and necessary in the093 existence proof; the graph application correctly sets them to zero.

**Positive finite/scaling control.** In the plane with the infinity norm put b_1=(1,0),b_2=(1,1),u=(1,1/2),v=(0,1). They are four unit vectors on distinct lines, and every subset obeys |S|≤2rank_Q(S). Partition into the two independent pairs (b_1,b_2) and (u,v). Relative to (b_1,b_2), u has coordinates(1/2,1/2) and v has(−1,1). Dividing the basis vectors by D=2 gives

\[
 A_1=2I_2,\qquad A_2=\begin{pmatrix}1&1\\-2&2\end{pmatrix}.
\]

Both determinants are4. For x=(1/8,1/4), phases are(1/4,1/2) and(3/8,1/4), all at distance at least1/4 from Z. The points0,b_1,b_2,u have colours0,1,2,1; the unit edges are the three incident to0 and b_1b_2, and all are proper. Dividing the original coordinate row of u by2 instead would give(1/4,1/4), not an integer row. This is a finite consumer/scaling check; the infinity norm is not claimed in the generic class.

**FALSIFIED — a finite palette may depend on the finite subgraph.** The complete graph on N has every finite induced graph finitely colourable, but no one finite palette colours it: for each k it contains a (k+1)-clique. The actual theorem fixes k before quantifying over finite sets.

**FALSIFIED — the same abstract graph compactness conclusion holds for a fixed countably infinite palette.** Every finite induced subgraph of the complete graph on R colours in N. A global proper colouring in N would inject the uncountable R into N, impossible. Finite colour partitions, not merely a common palette symbol, are used in Section3. These are abstract graph controls, not unit-distance graph counterexamples.

**FALSIFIED — arbitrary products of finite colour spaces are sequentially compact.** Index coordinates by all subsets A⊂N and define x_n(A)=1 if n∈A,0 otherwise. For any infinite subsequence x_(n_j), choose A={n_(2j):j≥1}. Its A-coordinate alternates, so that subsequence is not coordinatewise convergent. Thus no subsequence converges in the product topology. This defeats a proposed uncountable sequential-diagonal argument; it neither disproves graph compactness nor supplies a geometric obstruction.

Empty inputs, isolated vertices, disconnected components, repeated/opposite edge differences, overlapping completed bases, N>d and exact endpoint margins were covered in the actual argument. No finite grid, floating-point rank, numerical proof or solver was used.

## 6. Source contract, review and remaining scopes

The2026 source's physical4–5, reread102, explicitly invokes de Bruijn–Erdős, uses the rational independent partition, enlarges basis families, clears denominators, applies zero shifts and uses half-open bins. The present proof supplies the required graph compactness directly and makes the abstract Q-coordinate and endpoint contracts explicit. These pages were already fully read091/092; rereading adds no new page, underlying-source or independent-review credit. Fresh owner metadata still lists2609.36220v1; the cached exact matching-v1 introduction/status is reread, without a fresh PDF body download or exhaustive literature/priority check.

The 102 exact inspection register (historical local record; not distributed here) separates that reread from the bounded new frontier status-source increment. Discovery of a source-status qualification elsewhere does not alter this mathematical object or authorize another proof attempt. The frozen source amendment preserves that change of corpus priority.

Verdict: **PASS AT CLAIM CEILING / PROVED internally** for the known all-R^d upper-colouring application under092/093/101 and classical ZFC. The pivotal new bridge is finite-colour graph compactness for arbitrary vertex sets, with the finite consumer matched exactly. Inherited inputs remain internal proofs; original identities and contracts are checked, not freshly externally audited. Same actor/model, exposed source and expected theorem; no blind, external human or formal verification, novelty claim, performance gain or global open-problem resolution.

The source's lower/open-set theorem, m>0 branch, remaining21-page paper and Euclidean chromatic value remain unreproduced/unresolved at their separate scopes. Arbitrary-colouring existence is not measurable, periodic or algorithmic colouring. The structural/upper-colouring route is retired at this known scope; the required whole-frontier rerank precedes the next selected obligation.

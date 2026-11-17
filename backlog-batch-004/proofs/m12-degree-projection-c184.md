# Audited historical reading edition

**Current audited claim:** PROVED: For every assignment to the136graph edges, the two saved compact formulas after existentially quantifying their disjoint auxiliaries equal the direct degree-seven graph predicate with unchanged clique/independent-set clauses.

**Claim ceiling:** Specified encoding equivalence and exact files only; no17vertex satisfying graph, nonexistence certificate, search performance or Ramsey bound.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Exact degree projection for the two literal compact formulas

**PROVED:** for every assignment x to the136graph-edge variables, the direct C183formula D(x), the functional-grid formula after existentially quantifying its2176auxiliary variables, and the sequential formula after existentially quantifying its1785auxiliary variables have the same truth value. This is a restricted encoding theorem and implementation audit. No17vertex model, nonexistence certificate, source-census reproduction or global Ramsey bound is supplied.

The analytic arguments below justify all graph assignments; the finite controls separately challenge the literal implementation. They must not be interchanged. Standard Boolean/counter methods are being reproduced for a specified project consumer, not claimed as novel or optimal.

## 1. Functional grid

Fix m>=1 and0<=k<m. For input bits x_1,...,x_m, let w=k+1 and introduce z_ij for1<=i<=m,1<=j<=w. Set z_i0=true, including z_00, and z_0j=false for j>0. For each cell impose

z_ij iff (z_(i-1,j) OR (x_i AND z_(i-1,j-1))).

For o iff (a OR (b AND c)), the CNF clauses are

(-o OR a OR b), (-o OR a OR c), (o OR -a), (o OR -b OR -c).

The first two clauses say o implies(a OR b)AND(a OR c), equivalently o implies a OR(b AND c). The other two say a implies o and b AND c implies o, equivalently a OR(b AND c)implies o. Thus the conjunction is exactly the stated equivalence. Substituting true/false constants and dropping true clauses or false literals preserves each clause's truth value. No implication is dropped merely as an optimization.

Write p_i=sum_{t=1}^i x_t. The boundary values equal the truth values of p_0>=j and p_i>=0. For each i,j,

p_i>=j iff (p_(i-1)>=j OR (x_i AND p_(i-1)>=j-1)).

Induction on i therefore gives z_ij=[p_i>=j]. Conversely these values satisfy every cell equation, so a unique assignment to the auxiliary cells exists for every input before the cap. This also proves that cells with j>i are false; unreachable cells are not omitted. Adding -z_m,k+1is equivalent to p_m<=k. Hence

sum x_i<=k iff there exists z satisfying the functional CNF and its cap.

The direction from an arbitrary satisfying auxiliary assignment is essential: it follows from the same induction and does not assume that the auxiliary assignment was produced canonically. The k=0and m=1boundaries are covered by the displayed base equations.

For the literal syntactic normalization in encodings184.py, row1has2wclauses; each later row has4w-1; the cap adds one. At m=16,w=8this gives482clauses per vertex. The corresponding literal counts are3w+1for the first row,11w-4for each later row and one for the cap, giving1286per vertex. No subsumption or unit-based elimination is assumed in these counts.

## 2. Optimized sequential counter

For k=0use the units -x_1,...,-x_m, which directly impose the predicate and use no auxiliaries. For0<k<m, use s_ij for1<=i<m,1<=j<=k. The exact clauses in the sequential implementation are:

- x_1 implies s_11; s_1j=false for j>1.
- For2<=i<m, x_i implies s_i1and s_(i-1),1implies s_i1.
- For2<=i<m and2<=j<=k, x_i AND s_(i-1),(j-1)implies s_ij, and s_(i-1),jimplies s_ij.
- For2<=i<=m, forbid x_i AND s_(i-1),k, including the explicit final i=moverflow clause.

If sum x_i<=k, the canonical values s_ij=[p_i>=j] satisfy every clause. This proves existence for all permitted inputs.

For the converse, suppose any auxiliary assignment satisfies the formula. Inductively, p_i>=j implies s_ij=true for1<=i<m,1<=j<=k. At i=1this follows from the initial clauses. At a later i, either the prior prefix already has jones, in which case the carry implication applies, or x_i=1and the prior prefix has at least j-1ones. For j=1use x_i implies s_i1; for j>1use the advancement implication. This proves a lower bound on the auxiliary thresholds, not their equality with the actual thresholds.

If the input contained at least k+1ones, let tbe the position of the first(k+1)thone. Then2<=t<=m, x_t=trueand p_(t-1)>=k. The lower-bound induction forces s_(t-1),k=true. The explicit overflow clause at t is therefore false, a contradiction. Every satisfying auxiliary assignment consequently projects to an input with sum x_i<=k. Together with the canonical extension, this proves the exact existential equivalence.

Auxiliary uniqueness is neither needed nor true here. For all-zero inputs, setting the first threshold column to true and all other columns to false is another valid model. A checker that requires every sequential auxiliary model to equal the canonical prefix counts would reject a correct encoding. The positive noncanonical control and exhaustive small joint-state enumeration explicitly protect this distinction.

For m>1,k>0the literal implementation has(m-1)kauxiliaries and2mk+m-3k-1clauses. At16/7these are105and218per vertex, with514literal occurrences. The separate k=0units avoid applying this size formula outside its stated domain.

## 3. Gluing to the named17vertex graph formula

Keep the136edge variables and all8568clique/independent-set clauses from the pinned direct C183formula. At each vertex, its16incident edge variables are ordered by neighbor index. The counter predicates above enforce that vertex's degree bound.

For the functional version allocate128IDs per vertex after136, with disjoint blocks137..264through2185..2312. For the sequential version allocate105per vertex, with disjoint blocks137..241through1817..1921. Shared incident edges retain their one original edge ID; only auxiliaries are local to each block.

For a fixed graph assignment, disjoint auxiliary blocks imply

exists(all auxiliary blocks) AND_v C_v(x,y_v) iff AND_v exists(y_v) C_v(x,y_v).

Applying the local equivalences proves that either complete compact formula projects exactly to the direct maximum-degree constraints. The unchanged clique and independent clauses then prove the claimed whole-graph projection for every one of the2^136graph assignments. This is an analytic argument, not an assertion that those graph assignments were computationally enumerated.

## 4. Actual formulas and confirmatory checks

The saved functional17.cnf has2312variables,16762clauses,98022literal occurrences and444354bytes; its SHA256is ed7c0772ee4e50df32df19f3021ea0a8e2b4f8e3da57ce1306d70c6edc328184. The saved sequential17.cnf has1921variables,12274clauses,84898literal occurrences and372971bytes; its SHA256is5432483ee5d247cee18e8e9d1f86bd1fc65b2832342dac3420bcb3295fdba8af. All predicted counts matched the saved-byte audits.

The reference implementation derives the four abstract prime clauses from the16-row truth relation rather than importing the generator's gate template. All432constant-substitution cases also agree. The whole-formula audit compares the complete clause multiset, exact base prefix and every auxiliary ID/block with a separately indexed specification; it rejects missing/duplicate clauses and aliasing. It reads the actual saved CNFbytes.

The finite tests enumerate67274joint input/auxiliary states over twelve small variant/parameter cohorts. They check existence for both variants and uniqueness only for the functional one. For each variant, all65536sixteen-bit inputs are checked using direct prefix popcounts, not the producer recurrence. Each accepts exactly26333inputs and rejects39203. The complete ordered input-IDstream has SHA2564a35a59aabf394adb1d83cda6d3c2e799553e35ba7e4ee55537c8add209532a7. These are reused inputs across two encodings, not independent trials or a17vertex graph enumeration.

Eleven targeted controls expose incorrect caps, missing initial/forward/overflow constraints, shifted thresholds, missing/duplicate clauses, auxiliary aliasing and malformed dimensions/literals. Where a projected predicate is wrong, the record includes an explicit violating input and satisfying auxiliary model, or a valid input wrongly rejected. A separate reverse-direction deletion loses the stronger functional uniqueness contract while preserving the tested small existential projection; it is correctly classified without calling it a projection counterexample. These controls do not establish universal software fault detection.

## 5. Source, independence and decision

Sinz's primary CP2005paper supplies the existential definition and the optimized sequential clause families. Its short version omits the proofs and points to an extended report, which was not inspected. The local arguments above independently establish the needed projection directions and boundary handling; the paper's optimality/performance discussions are not adopted as claims about this project. All five page texts and two critical images were inspected; source coverage is separate from proof verification of its bibliography.

Different gate derivations, indexing and direct-prefix oracles target plausible shared implementation errors. The actor, runtime, specification and exposed expected results are shared. No blind reproduction, human referee, formal proof assistant, search-runtime comparison or17vertex solver execution occurred. The old136variable proof checker remains ineligible for the1921variable formula without a separately reviewed extension.

The sequential formula is the preferred next candidate because its exact projection is established and its representation uses fewer clauses/auxiliaries than the functional comparison formula. This is a representation choice, not an observed solver-speed improvement or optimality claim. Retain both formulas and the original direct input. Stop this projection gate; the next distinct task is a bounded proof-producing adapter/control contract before any deciding search. Lemma5.1and the global Ramsey target remain unresolved by this run.

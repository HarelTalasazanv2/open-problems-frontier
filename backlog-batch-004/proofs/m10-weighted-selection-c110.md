# Audited historical reading edition

**Current audited claim:** PROVED: Under the full labelled closure bound |cl(I)|<=d|I|+m and weights in [0,M], an independent J has weight at least (total weight-mM)/d.

**Claim ceiling:** Known finite theorem; label multiplicity and coefficient field cannot be changed.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Weighted independent-set extraction: exact proof and source audit

2026-11-01 UTC, cycle110. **PROVED internally:** the known weighted-selection Lemma4.5 stated below, for an arbitrary field and a finite labelled vector list. A finite prefix-rank identity proves it without the printed proof's inconsistent index ranges or an external matroid-partition theorem. The literal Lemma4.2 contract remains on hold: its proof occurs in the inspected window, but its complete statement does not. This result does not establish full Lemma4.2, the distinct-distance theorem, the complete paper or a Euclidean colouring bound.

## 1. Source gate, adaptation and claim ceiling

Pinned primary: Alon-Bucic-Sauermann, https://arxiv.org/pdf/2302.09058v2 , owned33-page PDF (historical local record; not distributed here),484598bytes, SHA256 `87801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960`. Complete physical12-16 text and full-page renderings were inspected110. This is a version-specific audit, not a latest-status or novelty survey.

The initial freeze (historical local record; not distributed here) selected the bounded field-span source gate. Physical12 concludes a graph/forest proof;13 gives the complete statement and proof of Lemma4.5;14 begins the proof of4.2 and states an external direction theorem;15-16 continue and finish that proof. **The literal Lemma4.2 statement was not located in12-16.** Its full field/ambient/collinearity/n-threshold contract is not inferred from proof prose or its consumer. No absence outside the inspected window is asserted.

Instead of extending the lookup chain, the analytic amendment (historical local record; not distributed here) selected the complete actual Lemma4.5 as one ready nontrivial ingredient, with its named use on16. The source, expected greedy argument and candidate prefix proof were already exposed to the same actor/model before this amendment. The deciding exact proof follows; no blind, independent-agent, human or formal verification is claimed.

**Claim ceiling:** a known finite weighted independent-set extraction theorem and its explicit source/shortcut findings. Source16's application to forest weights is identified, but the validity of all those inputs, full4.2/5.2/countable/distinct-distance/global norm results, full paper, current global M10 status, novelty and external/formal acceptance remain unestablished by this run.

## 2. Exact theorem and labelled membership

Let F be any field, V a vector space over F, and u_1,...,u_k a finite **labelled** list of nonzero vectors, k>=0. Repeated vector values are allowed. For I subset[k], define the closure by indices

`cl(I)={ell in[k]: u_ell belongs to span_F(u_i : i in I)}`.

The empty span is{0}. Let d>=1,m>=0 be integers and suppose, for **every** I subset[k],

`|cl(I)| <= d |I| + m`.                                      (1)

Let M>0 be real and let the real weights satisfy0<=lambda_i<=M. Then there is J subset[k] whose vectors are F-linearly independent and

`sum_(j in J) lambda_j >= (sum_(i=1)^k lambda_i - m M)/d`.    (2)

For k>0 the argument supplies the more explicit bound

`sum_(j in J) lambda_j >= (sum_i lambda_i - m lambda_max)/d`, (3)

where lambda_max=max_i lambda_i. This is an elementary refinement within the known argument, not a novelty claim. The source proof already retains an even more detailed tail-weight estimate. We do not turn an index list into a set of distinct vector values when counting(1).

The coefficient field need not be ordered, real, characteristic0 or finite-dimensional. Ordering is applied only to real weights. The source's nonzero-vector hypothesis is retained; no unproved extension to zero vectors is promoted. If k=0 choose J empty, giving0>=-mM/d. In what follows assume k>0.

## 3. Greedy prefixes span exactly the needed inputs

Choose a permutation sorting weights in nonincreasing order and relabel the vectors with their corresponding weights, keeping the original labels for recovery of J. Ties may be ordered arbitrarily. Thus

`lambda_1 >= ... >= lambda_k >=0`, and put `lambda_(k+1)=0`.

Scan labels1,...,k. Accept q if and only if u_q is outside the span of previously accepted vectors. Let J be all accepted indices and B_q=J intersect{1,...,q}, with B_0 empty. Induction proves two invariants:

- The accepted vectors in every B_q are linearly independent: adjoining a vector outside the previous span preserves independence over any field.
- Their span equals span_F(u_1,...,u_q). An accepted vector is adjoined to both spans; a rejected vector is already in the prior accepted span. Thus no prefix member is omitted from the span.

In particular {1,...,q} subset cl(B_q). Applying the **full-list** closure bound(1) to I=B_q gives

`q <= |cl(B_q)| <= d |B_q| + m`,

and hence

`d |B_q| >= q-m` for every q=1,...,k.                        (4)

No assumption m<=k or m<=|J| was made. If q-m is negative, inequality(4) is still valid. The number of accepted vectors may be smaller than m; an index j_m is never needed. Extra vectors outside the current prefix can increase its closure, but that only strengthens the first inequality. We did not replace full-list membership by a prefix-only test without justification.

## 4. A finite weighted-rank identity proves the bound

Let Delta_q=lambda_q-lambda_(q+1)>=0. For each j,

`lambda_j = sum_(q=j)^k Delta_q`.

All sums are finite, so changing their order gives the exact identity

`sum_(j in J) lambda_j = sum_(q=1)^k Delta_q |B_q|`.         (5)

Similarly,

`sum_i lambda_i = sum_(q=1)^k q Delta_q`,

and `sum_(q=1)^k Delta_q=lambda_1=lambda_max`. Multiplying(5) by d, using(4) with nonnegative multipliers Delta_q, and collecting terms proves

`d sum_(j in J)lambda_j`

`>= sum_q Delta_q(q-m)`

`= sum_i lambda_i - m lambda_max`

`>= sum_i lambda_i - m M`.

Division by d>0 yields(3) and(2). This is finite summation by parts, not an asymptotic, numerical or integration argument. Nonnegative weights also make every selected weight nonnegative; ties and zero weights cause zero increments rather than gaps. The proof uses neither an external matroid partition theorem nor any assertion about the real dimension of V.

For m>=k, the displayed target is nonpositive because sum_i lambda_i<=kM<=mM; J empty is also a direct healthy witness. The greedy proof covers that same domain without this separate shortcut. Every empty/nonempty, zero-weight, tie and rank-deficient case in the statement is included.

## 5. Source index defects, preserved separately from the theorem

The full physical13 rendering confirms two inconsistent ranges in the printed greedy proof. After constructing a sequence of length r, an independence sentence refers to its entries through j_m; admissible m>r need not define those entries. The subsequent contradiction paragraph quantifies1<=s<=m while the asserted index bound ranges over1<=s<=r. With m=0 the printed contradiction range is empty although r may be positive.

For a concrete admissible range check, take k=1,d=1,m=2,u_1=e_1 and M=lambda_1=1. The closure bound holds for both subsets; the greedy sequence has r=1, so j_2 is undefined. This identifies an indexing defect, not a false Lemma4.5 statement. Conversely m=0,k=1,d=1 has r=1, and its literal s<=m contradiction range supplies no proof for s=1. The intended greedy argument can use r in both places, but it was not silently certified as written. Sections3-4 give a separately stated complete proof that avoids those ranges entirely.

These findings receive source-inspection scope. A notation defect does not refute the parent theorem, and no source bytes were edited. The optional external partition-theorem remark on13-14 was read but is not a necessary unchecked import in this proof.

## 6. Exact positive controls, sharpness and rejected shortcuts

### Sharp repeated-basis family

Over any field choose r>=1 independent vectors e_1,...,e_r. Use d copies of each e_a and m additional copies of e_1, all as distinct labels, so k=dr+m. For any label set I, let t be the number of basis directions it represents. Its closure contains dt indices, plus m if direction1 is represented. Since t<=|I|, inequality(1) holds for every I, including the empty set. An independent set contains at most one label per direction. With every weight M, its maximum weight is rM and(2) equals

`((dr+m)M-mM)/d = rM`.

Thus the stated multiplicative factor and the worst-case additive loss are sharp for this class. This supplies exact positive equality cases, not sampled evidence for universality. The cases m=0 and d=1 show respectively why a stronger uniform factor or a smaller worst-case loss cannot be inferred from the same hypotheses.

### Closure and input controls

| Proposed weakened rule | Exact witness | Verdict and scope |
|---|---|---|
| Count distinct vector values instead of closure indices | u_1=u_2=e_1,d=1,m=0,M=lambda_1=lambda_2=1 | The distinct-value test passes, but every independent set has weight<=1 whereas(2) would require2. **FALSIFIED weakened membership rule.** The actual indexed hypothesis fails at I={1}. |
| Check only I=[k] | u_1=u_2=e_1,u_3=e_2,d=1,m=0, all weights1 | Full-set count3<=3 passes, but independent weight<=2<3. **FALSIFIED incomplete-subset shortcut.** I={1} reveals the actual failed premise. |
| Remove the upper-weight bound while keeping fixed M | u_1=u_2=e_1,d=1,m=1,M=1,lambda_1=lambda_2=2 | Every actual closure inequality holds, but independent weight<=2<4-1=3. **FALSIFIED upper-bound-free variant.** The actual theorem excludes these weights. |
| Keep the Q-span premise but demand real independence | F=Q,V=R,u_1=1,u_2=sqrt(2),d=1,m=0,all weights1 | Q-closure satisfies(1), and the two vectors are Q-independent. Real-independent weight<=1<2. **FALSIFIED cross-field substitution**, not the F-normalized theorem. |

The Q example uses the elementary irrationality of sqrt(2); it does not identify the Q-dimension of R with its real dimension. The closure condition concerns every subset, not just those an implementation happens to present.

As a finite-field healthy case take F=F_2,V=F_2^2, u_1=e_1,u_2=e_2,u_3=e_1+e_2,d=2,m=0,all weights1. The empty closure has size0, each singleton closure has size1<=2, and any set of at least two labels spans all three, with3<=2|I|. Greedy selects two independent vectors, weight2>=3/2. No order or characteristic0 assumption on F is required. All-zero weights, m=0, k=0, repeated weights, m>r and m>=k were also handled exactly above.

No executable research instrument or floating arithmetic was used. These controls challenge the actual hypothesis boundaries; agreement of finite examples is not the proof. The proof is the universal prefix argument.

## 7. Actual consumer and unresolved parent obligations

Physical16 applies Lemma4.5 to directional-forest edge counts lambda_i and M=3d/mu under a contradiction hypothesis giving the closure bound. The conclusion needed there is precisely an F-independent J with retained total weight at least(sum_i lambda_i-mM)/d. The result above supplies that extraction **when those stated inputs are valid**.

This does not check the complete Lemma4.2 formulation, the legality of every preceding projection/forest construction, the external Ungar direction theorem stated on14, the graph bound's full application, the unspecified sufficiently-large-n thresholds, or the complete distinct-distance/countable reduction. The literal4.2 statement remains unlocated in this bounded window; no new global theorem is inferred by reading its printed proof conclusion. The known fixed-family geometry proved109 retains its prior scope.

## 8. Adjudication and useful changed uncertainty

Math-verification verdict: **PASS AT CLAIM CEILING**, internal and exposed, for Lemma4.5 and(3). **CERTIFIED_RANGE:** literal source statement/consumer and the two index inconsistencies on13 at the inspected extents. **FALSIFIED:** only the four explicitly weakened membership/subset/weight/field rules in the table. **INCONCLUSIVE/HOLD:** full Lemma4.2 contract and validation. Full4.2/5.2/countable/distinct-distance/global target, full paper, novelty, human review and formal verification remain **NOT_TESTED** as proof claims.

The changed uncertainty is a previously unverified weighted extraction input: it now has a complete finite proof covering arbitrary fields, labelled duplicates and m beyond the chosen rank. The source's index issues do not propagate into this proof. Label multiplicity, all-subset coverage and coefficient-field consistency are transferable failure checks. Do not repeat another greedy-weight grid or use this result as a substitute for validating the parent forest/field/n-threshold inputs.

This is the third material success in the resumed m-positive dependency sequence108-110. Reconsider the full dated frontier before another extension; no automatic lookup chain or global promotion follows. The source register (historical local record; not distributed here) and page review (historical local record; not distributed here) record exact extents and representation hashes. New full text/visual13-16,12 reread; one unchanged underlying paper, no new estate path or independent source. Local custody hashes are not external tamper resistance or mathematical assurance. No external action occurred.

> Public reading edition for the audited mathematical claim. Historical phase counts below are not current global status. The original proof is retained unchanged in the project. Local navigation was adapted for this package; credit is in [REFERENCES.md](../REFERENCES.md). CNF/SAT encodings, slide-coverage counts, novelty and external/formal review are outside this audit.

# Complete four-case binary support-cover audit

The claim ceiling is a complete finite test of all 64 zero-one vertex weights for each of the four remaining five-edge neighborhoods 659,662,692,920. A qualifying cover gives a restricted graph-class exclusion through the named support-cover lemma. Absence of a qualifying cover establishes only that this particular obstruction is absent in this finite family. It does not establish a nonnegative histogram, a fractional-cover optimum, a B-graph completion, or an original-target SAT result.

## Admitted graph reduction

The named C186 cumulative refinement and parity selector, C187 B-crossdegree bound, and C189 saturation argument concern a simple graph on 17 vertices with no K5, no independent four-set, and maximum degree at most seven. It admits a degree-six root. Its six neighbors A have local labels 0 through 5, corresponding to global labels 1 through 6; the global root is outside A. The other ten vertices form B.

B has no independent triple. For a vertex in B its B-nonneighbors form a clique of size at most four, so its B-degree is at least five and it has at most two A-neighbors. If A has five edges, summing the full minimum-degree bounds t[a]>=5-k[a] gives at least twenty cross incidences; ten B vertices give at most twenty. Thus all B vertices have exactly two A-neighbors, and t[a]=5-k[a].

Counts x[S] of the fifteen pair types are nonnegative integers with total ten and incidence degrees t[a]. If a pair avoids an independent triple in A, its count must vanish. These are necessary constraints, not sufficiency conditions for a graph. All pairs and all independent triples must be included before a support claim is made.

## Sufficient cover inequality and exact certificate

For nonnegative counts on a finite allowed-type family, totaling N, and vertex weights w[a]>=0 with sum_{a in S}w[a]>=1 for every allowed type, finite summation gives

sum_a w[a]t[a] = sum_S x[S]sum_{a in S}w[a] >= sum_S x[S] = N.

Consequently a complete cover of cost below ten excludes the necessary count model. An uncovered type cannot be silently omitted: it could carry all the mass. A cost of exactly ten gives no strict contradiction.

Let Mx=b consist of total count, six incidence rows, and one zero row per forbidden type. For a qualifying binary vector, combine minus the total row, plus w[a] times each degree row, plus (1-w(S)) times the zero row for each forbidden S. On every forbidden column the combined coefficient is zero; on every allowed column it is w(S)-1>=0. The right side is sum_a w[a]t[a]-10<0. Hence the exact row combination certifies nonnegative-model infeasibility. Equality-row multipliers are unrestricted in sign. A negative combined coefficient with negative right side is not sufficient; -x=-2 has the nonnegative solution x=2.

This is a direct sufficient implication, without a converse duality theorem, solver status, floating tolerance or rounding error. Reviewed C190 cone arithmetic and C191 cover checking may be reused with their hashes pinned; that reuse is not new arithmetic independence.

## Complete finite domains

The C191 residual has sixty classes. Selecting every representative with exactly five set edge bits must give exactly 659,662,692,920. Their original C188 orbit memberships supply the labeled weights; they are not four arbitrary submitted cases. Earlier excluded classes 684,617,632 remain historical evidence and are not retested as new research.

For six labeled vertices each binary weight vector has a unique mask m=sum_a 2^a*w[a], with 0<=m<64. Conversely extracting the six bits of such a mask gives its unique vector. Thus masks 0 through 63 cover the binary domain exactly once. The consumer uses product tuples and an independently constructed mask-to-vector map to check this association, not merely a count of 64. Four complete case domains contain exactly 256 case/mask pairs. A retained prefix with any pairs missing is incomplete even if all presented candidates pass.

For each candidate the consumer independently recomputes all allowed pair weights, cover flag, incidence cost, deficit and strict-obstruction flag. It verifies every reported qualifying mask, every boundary case, and every nonqualification. The least qualifying mask supplies a deterministic certificate. If none qualifies, only NO_BINARY_DEFICIT_IN_64_WEIGHTS is supported. A stronger feasibility statement would require a separate witness or theorem and is expressly rejected.

## Partial states, membership and residuals

A capped producer preserves the exact ordered remaining case/mask pairs and an INCONCLUSIVE status. The complete-result consumer must reject such a record. In particular, budget zero leaves all 256 pairs pending and cannot support a full-domain conclusion.

Only a case with a complete weight record and a valid strict-cover certificate is removed from the previous residual. Its exact C188 orbit members, and no others, are removed. If no cases qualify, the residual is unchanged. Dynamic counts are derived from actual exclusions, not anticipated here.

The full 17-vertex target and the published Ramsey census remain unresolved locally by this audit. Different graph representations and enumeration paths share actor, specification, inputs, Python runtime and exposed contract; generic certificate arithmetic is reused. No blind, external, formal, novelty or measured-performance claim is made.


[Batch verification](../verification_result.json) · [Extension verification](../extension_result.json) · [Exact exclusion chain](../chain_result.json).

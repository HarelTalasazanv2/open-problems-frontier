# Audited historical reading edition

**Current audited claim:** PROVED: At the displayed sufficient N(d,mu), the field-span conclusion and fixed-tolerance bad-norm meagreness follow under the precise real-field/norm definitions.

**Claim ceiling:** Known-result integration of the included restricted ingredients; no current Euclidean bound or novelty.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Exact M10 field-span and fixed-tolerance consumer integration — Cycle 141

**PROVED internally at the named inherited-proof scope:** the original-configuration D_n assumption can be removed from the exact Cycle125 field-span result and the Cycle126 pointwise consumer and fixed-tolerance meagreness result. The verified Cycle140 Ungar import supplies it at every actual invocation. This is known-result integration, not a new theorem or independent/external/formal review. The all-tolerance/Baire/topological assembly, complete printed Theorem1.3 and Euclidean colouring problem are outside this audit.

The contract was frozen first (historical local record; not distributed here): one explicitly user-authorized consumer integration,40minutes/80combinedtoolcalls,10minutecloseout reserve,0publicrequests/0PDFpages,<=1100directnative scientific lines. The change justifying this gate is the actual primary-backed140D_n result; other paused routes and completed source searches remain closed. No operational repair was needed.

## Exact established statements

For integers d>=1 and real 0<mu<1 define

    T = 3d/mu,
    R = max(2, 48dT^2/mu, (48d^2/(mu ln2))^2),
    N(d,mu) = ceil(max(9/mu,T R)).

For every integer n>=N, real subfield F, real vector space V, nonzero finite labelled list u_1,...,u_k (duplicates and unused labels allowed), and n distinct points p_x not on one real affine line, assume each nonzero pair difference lies on some F u_i. Then there is I subset[k] such that

    |{ell : u_ell in span_F(u_i:i in I)}| >= d|I|+(1-mu)n+1.    (FS)

No extra D_n hypothesis is required. The threshold is uniform in F,V,k, labels and points, and is a sufficient unoptimized witness, not a sharp or computationally measured bound.

For d>=2 let B_d be compact convex origin-symmetric norm balls with0 interior, with the relative Euclidean Hausdorff metric. Let Delta_B(S) count only positive distinct norm distances of distinct points. Put

    n0(d,mu)=max(N(d,mu),floor(1/mu)+1,2),
    A*_mu={B in B_d : some n>=n0 and distinct n-point S have
                         Delta_B(S)<=(1-mu)n}.

For every such B,S, with m=ceil((1-mu)n), there are ell>=1, L=dell+m+1, A over Q(X_1,...,X_m) of size L by ell, a positive rational eta<pi/2, legitimate common real evaluation z, and L actual boundary vectors v_j with all L relations

    v_j = sum_(i=1)^ell A_ji(z)v_i, 1<=j<=L,

whose pairwise unoriented real lines have acute Euclidean angles>eta. Consequently **A*_mu is meagre in B_d for each fixed 0<mu<1**. For mu>=1 and n>=2 the corresponding bad set is empty, a separate branch that invokes no positive-m family. Mu=0 is excluded.

These are the unconditional variants of the exact125/126 native statements, relative to the previously internally proved lemmas identified below. No all-mu intersection, dense/nonempty residual set, asymptotic distinct-distance statement or global Euclidean chromatic value is concluded here. Historical conditional proofs remain valid and unedited.

## Dependency ledger and assurance boundary

| Input | What was checked141 | Status and limit |
|---|---|---|
| [140D_n import](m10-d_n-import-c140.md) | Exact n>=3 real/noncollinear/unoriented statement, source identity header and frozen artifact hash; every125 invocation has n>=N>9 | Inherited primary-backed internal result; only lines1-17 reread, no Ungar proof/source retry |
| [110weighted extraction](m10-weighted-selection-c110.md) | Full proof: indexed closure, all subsets, greedy prefix ranks, nonnegative real weights, same coefficient field | Confirmed at use; no external matroid partition import or printed index ranges needed |
| [115forest bound](m10-forest-edge-c115.md) | Full corrected proof: independent F-directions, distinct original points, simple graph, full direction classes in G, corrected entropy inequality | Confirmed at use; printed false entropy step remains failed |
| [109fixed-family geometry](m10-mpositive-geometry-c109.md) | Full composition and exact d,ell,m,L,A,eta/evaluation/norm-boundary domain; no identity-row or rank restriction, robust holes for all legitimate z | Inherited internal theorem, interface and composition reread; its097/098/099/108 foundations are named inherited proofs, not independently re-audited141 |
| 125argument (historical local record; not distributed here) | All159lines, quotient/pruning/weights/graph membership and exact threshold | Complete at the frozen native statement after140substitution |
| 126consumer (historical local record; not distributed here) | All134lines, every witness and coefficient relation, variable-m countable cover and correct category implication | Complete at the fixed-tolerance scope after FS substitution |

All are exposed same-actor/model reviews of shared inputs. A matching hash establishes identity; it does not establish mathematical truth or reviewer independence. The mathematical argument and checked hypotheses supply the internal assurance. We did not claim to independently reproduce the entire foundational109chain, the primary paper's literal flawed steps, human review or formal verification.

## Field-span audit: the contradiction and its interfaces

Fix d,mu,n,F,V and the input. Let m=ceil((1-mu)n), an integer with1<=m<=n. Negating FS gives indexed closure<=d|I|+m for every I. Integer rounding is exact: ceil commutes with addition of the integer d|I|+1.

Prune precisely labels with no nonzero original point-pair witness. Every pair remains covered, the restricted closure bound persists, and any solution for retained labels is a solution for the original list. D_n holds for the original n distinct real-noncollinear points because n>=N>=9/mu>9. Since F is a subfield of R, one nonzero labelled F-line can cover only one real direction. Thus the retained label count k>=n-1, including duplicates. This is the only direction-count invocation.

Construct W_s as the F-span of previously selected directions and choose one original representative from each class of points modulo W_s. If some direction admits a forest with at least T edges on these representatives, adjoining that direction reduces the number of classes by at least T. The chosen direction is outside W_s; otherwise no eligible edge could join distinct representatives. Hence the selected directions are F-independent. The finite procedure stops with r selected directions and h original representatives, with

    1<=h<=n-rT,   r<=n/T.

No real direction theorem is applied to an F-quotient; the quotient may have no real vector-space structure. Every graph later uses the distinct ORIGINAL representatives and nonzero ORIGINAL directions.

If h<=n/T, connect one representative to each of the others by a covering label and adjoin the r selected directions. The resulting I has |I|<=r+h-1<=2n/T and spans every original pair difference. Every retained label has a witness with a nonzero F coefficient, so division shows that every retained u_i lies in this span. The original[n] point witnesses are used, rather than the printed[k] range. Consequently cl(I) has size k>=n-1. Since n>=9/mu and m<=(1-mu)n+1,

    n-1 >= (2mu/3)n+m+1 >= d|I|+m+1,

contradicting the closure bound. Therefore h>n/T.

For each retained label take a maximum forest G_i on the terminal representatives, lambda_i=|E(G_i)|. Termination gives0<=lambda_i<T. Every eligible pair is connected within this maximum forest, or its edge could be added between components. Hence both endpoints are non-isolated and there are at most(2lambda_i)^2 eligible ordered pairs. All h(h-1) ordered pairs are covered, so for h>=2,

    h^2/2 <= h(h-1) <= 4 sum_i lambda_i^2 <= 4T sum_i lambda_i,
    sum_i lambda_i >= mu h^2/(24d).

Apply110 with the full indexed closure bound, the same F and M=T. It gives F-independent J with

    sum_J lambda_j >= (sum_i lambda_i-mT)/d
                     >= (mu h^2/(24d)-nT)/d.

Since nT<T^2h and h>=48dT^2/mu, the right side is at least mu h^2/(48d^2). Independence makes the forests' edge sets disjoint, and their union G is simple. Crucially, the full direction-j edge class WITHIN G is exactly G_j; an edge from another independent F-direction cannot belong to it. Thus all of115's hypotheses hold and

    mu h^2/(48d^2) <= |E(G)| <= (h/2)log_2 h.                 (1)

The threshold is sufficient uniformly, with no decimal estimate. N>=TR and h>n/T imply h>R, providing h>=2 and loss absorption. Also h>(48d^2/(mu ln2))^2. For h>=1,

    ln h <= integral_1^h t^(-1/2)dt = 2(sqrt(h)-1)<2sqrt(h).

It follows strictly that log_2(h)/h < mu/(24d^2), contradicting(1). All denominators are positive in the stated domain. The dependence is only on d and mu, including when F and the distance list later vary with n and the configuration. This closes FS.

The110prefix-rank proof was checked rather than merely quoted: a greedy independent prefix B_q spans every prefix, so q<=d|B_q|+m. Multiply by nonnegative weight increments lambda_q-lambda_(q+1) and sum; this gives d*selectedweight>=totalweight-m*lambda_max>=totalweight-mT. Label multiplicity and zero weights are retained.

The115corrected entropy proof, not the failed printed intermediate inequality, supplies the graph bound. Its component proof partitions by the graph after removing one full direction forest; independence makes each removed-forest component meet each remaining component at most once. This yields the red-edge bound n-maxpart and the corrected partition-entropy inequality, including isolates/disconnected cases. No field order or real dimension bound enters.

## Consumer audit: no remaining direction assumption

A bad configuration at n>=n0 cannot be collinear. If ordered on a line, its n-1 distances from an extreme point are positive and strictly increasing, so Delta>=n-1>(1-mu)n because n>1/mu. This uses only norm homogeneity/distinctness and is not circular use of D_n. Hence140applies to EVERY actual bad witness; no extra witness-selection assumption remains.

Choose one norm-unit representative per real unoriented pair direction, with arbitrary sign. Every difference is plus or minus its positive norm distance times the chosen representative. Pad its finite positive distance list to m entries and put F=Q(z_1,...,z_m), a real subfield even for repeated or algebraically dependent values. FS applies with uniform N and supplies I, ell=|I|>=1 and at least L=dell+m+1 closure labels.

Select exactly L closure labels including I and relabel I first. The u_i are nonzero so I cannot be empty, and L>=ell. Distinct original real directions remain distinct in the selected list. No F-independence or ell<=d claim about I is needed. Choose coefficients in F for every one of the L relations, using the identity rows for j<=ell.

For the actual tuple z, values P(z)/Q(z) with rational polynomials and Q(z)!=0 form a field containing Q and z and contained in F, hence equal F. Thus each finitely many chosen coefficient has a legitimate rational-function presentation, and the product of their finitely many denominators is nonzero at this same z. This is a localization argument at the chosen evaluation, not an evaluation of the whole formal rational-function field. Algebraic dependence causes no gap; true poles remain inadmissible. In particular1/(X_1-X_2) cannot be evaluated at(1,1).

All selected vectors lie on the actual norm boundary, all L relations remain true (including the first ell self-relations), and finitely many pairwise distinct real lines have a strictly positive minimum acute Euclidean angle. A positive rational eta below that minimum and pi/2 supplies exactly109's E_(A,eta) witness. No relation is imposed on a perturbed approximation instead of the original vectors. No strict convexity, smoothness or fixed matrix rank is introduced.

For fixed d,mu, take the union over every integer n>=n0, every ell>=1, every formal matrix A with m=ceil((1-mu)n) variables and size(dell+m+1)byell, and rational eta. Rational polynomials and fractions in any fixed finite number of variables are countable, as are finite matrices and the outer integer indices. The value m is allowed to vary with n. Actual real parameters z and vectors are existential witnesses INSIDE E, not uncountable family indices. Every possible bad witness is covered. The109theorem matches each family and supplies nowhere-denseness, across all legitimate evaluations.

A*_mu is a subset of this countable union, so it is meagre: intersect A*_mu with each nowhere-dense family and use monotonicity of closure. The existential family itself need not be closed. No Baire-space, completeness, residual-set-density, asymptotic or all-tolerance-intersection argument is used or claimed. The separately empty mu>=1branch is valid before any positive-m construction.

## Decisive controls and outcome classification

Confirmation contract (historical local record; not distributed here), exact controls (historical local record; not distributed here). Three integer/rational threshold fixtures use the conservative envelope obtained from ln2>1/2. They check strict lower margins/loss absorption, not the optimality of N or a computed enclosure of its logarithm. Original N is justified analytically above.

The inherited109six-row Euclidean fixture has all six unit vectors and absolute pair determinants at least16/65>1/10>=sin(1/10). Every relation holds with identity first rows. Changing the first row to(2,0) makes its required first relation fail and would force that boundary vector to zero; checking only rows after the first ell incorrectly accepts the altered fixture. Missing rows and malformed coefficient dimensions are rejected. These controls target a real admission failure mode of the consumer. They are not samples establishing the general theorem.

Exact equality n=1/mu still allows collinear equally spaced points with n-1distances and cannot replace the strict threshold. At fixed mu=1/2, n20and21give m10and11, so a fixed-m outer union would omit cases. Field substitutions, label deduplication, omitted graph-direction edges and replacing full-field evaluation by arbitrary pole values remain invalid shortcuts; their exclusions are checked in the analytic chain. Old110index defects,115printed entropy failure and108/109source-restatement defects remain historical, not silently repaired or accepted.

**PASS AT CLAIM CEILING:** FS, every stated126pointwise witness, and fixed-tolerance meagreness are PROVED internally from the named internal lemmas and verified140import, with no D_n assumption remaining. No essential gap was found in this frozen chain. Original125/126conditional proof files and source evidence remain unchanged. The complete literal printed proof, independent human review, formal verification, novelty, all-mu/topological assembly and global M10problem are NOT TESTED as new claims.

The next possible action is a SEPARATE bounded contract matching the established fixed-tolerance sets/thresholds to Cycle131's conditional premise and auditing its all-tolerance/topological assembly. It is an unselected proposal, not automatic continuation. We did not read or rerun131, reopen any other paused route, or retry the closed Ungar search.

Adjudication (historical local record; not distributed here), exact inspection register (historical local record; not distributed here), report (historical local record; not distributed here). Six directly relevant native paths were inspected: five full and one partial(140lines1-17),761direct lines/six hashes,0PDFpages/0publicrequests/0new independent sources or reviews. Native derivatives share source lineage. Scientific cumulative content/source/path counts and denominators remain UNKNOWN; legacy mixed-volume counts are not scientific coverage. No excluded original/copy, source execution/mutation, external action, agents, application/schedule/notification, other-project/shared-skill change occurred.

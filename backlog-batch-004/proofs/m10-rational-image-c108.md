# Audited historical reading edition

**Current audited claim:** PROVED: The normalized L=d ell+m+1 rational-output achievable family is covered by a finite proper polynomial zero set, at every legitimate common evaluation.

**Claim ceiling:** Normalized full witness list; no arbitrary pole filling or certification of defective shorter source wording.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M10 rational-image dependency: exact internal reconstruction

2026-10-31 UTC, cycle108. **PROVED**, internally, for the algebraic primitive, normalized source Claim2, and its robust parameter-exclusion corollary stated below. Math-verification verdict: **PASS AT CLAIM CEILING**. These are known source ingredients, not novel theorems, a new Euclidean colouring bound, or validation of the full paper. Same exposed actor/model constructed and challenged this argument; there was no blind reproduction, external human review or formal verification.

## Source, frozen contract and literal defects

Pinned primary: Alon-Bucic-Sauermann, https://arxiv.org/pdf/2302.09058v2 , owned 33-page PDF (historical local record; not distributed here), 484598 bytes, SHA256 `87801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960`. Physical pages20-22 were read in full text and rendered form108. This is a version-specific source audit, not a latest-status or novelty survey. Initial attempt (historical local record; not distributed here) preceded source inspection. The analytic amendment (historical local record; not distributed here) followed source inspection and exploratory reasoning, and preceded the deciding proof. Its exposure statement is part of the contract.

The complete m-positive achievable definition in the middle of p20 supplies L=d*ell+m+1 witness vectors. The later phi-achievable definition on p20 and the first witness sentence of Claim2 on p21 instead list only d*ell+1 vectors while subsequently using all L. For m>0 that shorter list does not supply the variables the formulas require. We preserve that inconsistency and reconstruct the claim from the earlier complete definition. On p21 the union H is once labelled a subset of R^d, although its coordinates and polynomial zero sets lie in R^h. We explicitly use R^h. These are reported indexing/ambient-label defects, not counterexamples to Claim2. The literal defective sentences have not silently been certified as written.

Let d,ell,m be positive integers, h a nonnegative integer, N=d*ell+m and L=N+1. Fix vectors o_1,...,o_h in R^d and a matrix A in Q(z_1,...,z_m)^(L by ell). No rank, invertibility, genericity or nonzero-normal assumption is needed for the algebraic claim. A tuple t in R^h is achievable in the normalized definition if there are an injection phi:[L]->[h], a real parameter z where every entry of A is well-defined, and vectors u_1,...,u_L in R^d satisfying

`u_j = sum_(i=1)^ell A_ji(z) u_i`, and `|o_phi(j) dot u_j| = t_phi(j)` for every j=1,...,L.

The first ell relations may impose self-consistency conditions on the base vectors. They are not discarded as assertions about a witness; the parameter map below merely overcovers their allowed set. No source geometric hypotheses are inferred from this algebraic reconstruction.

## Lemma A: a nonzero polynomial relation with a finite degree bound

For F=Q or R, let n>=0 and r>n, and let f_1,...,f_r be elements of F(x_1,...,x_n). There is a **nonzero formal polynomial** H in F[Y_1,...,Y_r] with H(f_1,...,f_r)=0 in that field. If n>=1, a sufficient bound on the total degree of H is

`k = 1 + r! (E+n)^n`,

where E>=1 bounds the degrees of a common denominator and its corresponding numerators constructed as follows. This bound establishes finite existence; it is not an efficiency claim or a serialized certificate for an unspecified A.

Write f_i=P_i/Q_i, with Q_i a nonzero polynomial. In the polynomial ring over a field, the product D=product_i Q_i is nonzero. Put B_i=P_i product_(j!=i) Q_j. Then f_i=B_i/D. Choose an integer E>=1 at least the degrees of D and all nonzero B_i; a zero B_i creates no difficulty.

For every multi-index beta in N_0^r with |beta|<=k, form the polynomial

`C_beta = D^(k-|beta|) product_i B_i^beta_i`.

Its total degree is at most kE. There are binom(k+r,r) such beta, whereas the F-vector space of polynomials in n variables of total degree at most kE has dimension binom(kE+n,n). For k>=1 and n>=1,

`binom(k+r,r) >= k^r/r!`,

`binom(kE+n,n) <= (kE+n)^n/n! <= k^n (E+n)^n/n!`.

Because r-n>=1 and k=1+r!(E+n)^n, we have

`k^(r-n) >= k > r!(E+n)^n >= (r!/n!)(E+n)^n`.

Thus the number of C_beta is strictly larger than the dimension of their containing space. There are coefficients c_beta in F, not all zero, with sum_beta c_beta C_beta=0. The polynomial H(Y)=sum_beta c_beta Y^beta is nonzero: the beta label distinct formal monomials. In the fraction field, D^k H(f)=0, so H(f)=0, since D is nonzero and hence invertible there. This does not require any B_i to be nonzero or algebraically independent. For n=0 every f_i is a constant in F and H=Y_1-f_1 proves the assertion directly. This also handles the empty input space without an ambiguous dimension convention.

### Evaluation and poles

An identity in the fraction field must be connected to real inputs; writing decimal values or silently filling poles would not do that. For a point a in R^n, consider the subring of rational functions admitting some polynomial quotient presentation with denominator nonzero at a. Define evaluation by that quotient. If P/Q=P'/Q' and both denominators are nonzero at a, cross multiplication P Q'=P' Q proves that the values agree. Sums and products retain presentations with denominators nonzero at a, so evaluation is a ring homomorphism on this subring.

Whenever every f_i has such a legitimate evaluation, H(f)=0 may be evaluated through this homomorphism, giving H(f(a))=0. The identity therefore holds at all legitimate common evaluations, even where the initially chosen D vanishes but a removable presentation exists. If source evaluation uses only a fixed denominator-nonzero presentation, it is a subset of this domain and is covered as well. No true pole is admitted, and no arbitrary assigned value at an undefined point is licensed. For example, (t^2-1)/(t-1) has the local presentation t+1 at t=1; 1/t has no such presentation at t=0.

## Lemma B: the normalized source achievable set has a finite proper algebraic cover

Fix an injection phi and a sign vector sigma in {+1,-1}^L. Introduce N=m+d*ell independent real variables, consisting of z and coordinates v_(i,a) of ell base vectors. Define L rational functions

`F_j(z,v) = sigma_j sum_(a=1)^d o_(phi(j),a) sum_(i=1)^ell A_ji(z) v_(i,a)`.

Their coefficients belong to R, including possibly irrational coordinates of the fixed normals. At any actual achievable witness choose v_i=u_i and the signs sigma_j to make t_phi(j)=sigma_j(o_phi(j) dot u_j). Zero dot products allow either sign and cause harmless duplicate coverage. Relations (a) give t_phi(j)=F_j(z,v). Condition (o) makes every F_j legitimately evaluable there. The map is defined on a superset of any first-ell self-consistency constraints; proving a cover for this larger image covers all actual witnesses.

There are L=N+1 outputs, so Lemma A gives a nonzero H_(phi,sigma) in R[Y_1,...,Y_L] vanishing on this rational image. Define a polynomial in the full parameter tuple by

`G_(phi,sigma)(T_1,...,T_h) = H_(phi,sigma)(T_phi(1),...,T_phi(L))`.

Because phi is injective, different monomials in the Y variables remain different monomials in the selected T coordinates. This substitution is injective on polynomial rings, hence G_(phi,sigma) is nonzero. Every witness with this injection and sign choice lies in its zero set. With h>=L there are h!/(h-L)! injections and 2^L sign patterns, finitely many. The product G of all these nonzero G_(phi,sigma) is nonzero because R[T_1,...,T_h] is an integral domain. Its real zero set is exactly the finite union of their zero sets and contains every achievable tuple. Repeated or proportional factors do not create independent evidence or invalidate the cover.

If h<L, no required injection exists, so the achievable set is empty. The empty product G=1 supplies a valid nonzero covering polynomial with empty zero set. In particular h=0 is covered. No determinant has been divided out, so no rank-deficient stratum has been lost: zero matrices, changing ranks, zero rows and dependent relations are all included. No finite nonsingular chart family is assumed. Selected t coordinates must be nonnegative for an actual absolute-value witness; permitting a larger rational image only strengthens the cover argument.

## Lemma C: properness and robust exclusion

A nonzero real polynomial has a closed zero set by continuity. Its zero set has empty interior. To see the latter without importing algebraic geometry, suppose a nonzero polynomial in h>=1 variables vanishes on an open box. Express it as a polynomial in the last variable with polynomial coefficients in the other variables. For each point in the lower-dimensional box, that univariate polynomial vanishes on an interval, so all its coefficients vanish. A nonzero univariate polynomial cannot have infinitely many distinct roots: repeated factor theorem bounds roots by its degree. Induction in h therefore forces every coefficient polynomial to be zero, a contradiction. For h=1 the same root argument is the base; for h=0 a nonzero constant has empty zero set.

The finite product G above is nonzero, so its zero set Z(G) is closed with empty interior. The closure of the achievable set, being contained in the closed Z(G), also has empty interior. Every nonempty open parameter box contains a point t outside Z(G). Its intersection with the open complement of Z(G) contains a sufficiently small closed sup-norm ball about t. This ball is disjoint from all achievable tuples. When a prescribed closed box has nonempty interior, first choose t in its interior and then shrink the ball to stay in that box. The source's positive perturbation box may be treated this way once its positive width is supplied. This proves existence of a margin, not a computed numerical margin or the later geometric stability statement.

## Adversarial controls and their outcomes

| Challenge | Exact response and consequence |
|---|---|
| Constant outputs | H=Y_1-c is nonzero; zero maps do not defeat the argument. |
| Curve (t,t^2) | H=Y_2-Y_1^2 verifies a nonzero exact relation independently of the dimension count. |
| Remove r>n | Identity map R^n->R^n has image with nonempty interior; no nonzero polynomial vanishes on it. The weakened shortcut is **FALSIFIED**, not Lemma A. |
| Allow noninjective phi | H=Y_1-Y_2 becomes zero after substituting the same T coordinate twice. The proposed weakened embedding shortcut is **FALSIFIED**; source phi is injective. |
| Initial denominator vanishes removably | Local presentations and the evaluation homomorphism retain the identity at every legitimate value. Requiring the initially chosen D!=0 would have unnecessarily narrowed coverage. |
| True pole 1/t at0 | If it had a representation P/Q with Q(0)!=0, then tP=Q would give Q(0)=0, contradiction. Undefined inputs are excluded, not approximated. |
| Rank-zero A | All selected witness t coordinates are zero; the parameter map remains rational and the finite proper cover applies. |
| Changing-rank A(z) | Formula uses A directly without inversion; rank loci impose no omitted domain. Entry poles remain subject to (o). |
| Base self-consistency | Dropping those restrictions only for constructing a covering image enlarges it; all valid witnesses remain included. |
| h<L or h=0 | No injection, empty achievable set, product1; no nonexistent witness case is claimed to have been checked by sampling. |

No counterexample satisfying the actual reconstructed hypotheses was found by these exact structural attacks. This is not a finite-search nonexistence inference: the universal restricted conclusion is supported by the proofs above. The source notation defects remain visible, and their normalized interpretation is separately identified.

## Adjudication, usefulness and remaining obstruction

The uncertainty changed from an unreproduced algebraic citation/source bridge to a complete elementary argument with exact parameter count, nonzero relation, evaluation domain and all-rank coverage. Rank decomposition and denominator-zero blind spots were plausible failure modes; explicit parameterization and local evaluation eliminate them at this claim ceiling. The injection and strict dimension-excess controls show which weakened statements actually fail. These lessons transfer to other rational-image exclusion arguments. Do not repeat a numerical grid or assume an arbitrary pole filling supplies a certificate.

**PROVED, internal:** Lemmas A-C and normalized source Claim2 for the full p20 achievable definition. **CERTIFIED_RANGE, source inspection:** the stated indexing and ambient-dimension inconsistencies occur on the selected pages. **FALSIFIED:** only the two explicitly weakened generic shortcuts in the control table. **NOT_TESTED:** full m-positive Lemma5.3/geometric exclusion, Theorem1.3 distinct-distance application, countable/global assembly, lower bound, full paper, current global M10 status, novelty, formal verification and external mathematical acceptance. The later facet-diameter continuity sentence is not adopted as an unchecked necessary input; only the standalone parameter exclusion was proved here.

The next discriminating obligation is a fresh bounded audit of the m-positive geometric exclusion step linking a hypothetical nearby boundary configuration to the now verified achievable tuple, using the exact source proof continuation and the earlier strictly bounded geometric ingredients. It changes mechanism from algebraic dependence to boundary/facet assignment, preserves the source notation corrections, and must stop at its first unsupported geometric dependency. Success would close that particular finite-A robust-exclusion bridge; it would still not establish the final global theorem.

Reproduce by reading the frozen records, selected physical20-22 text/renderings, and these exact algebraic steps. No numerical executable, external theorem beyond elementary linear algebra/polynomial arithmetic, or claimed machine-checked certificate is needed. Required source hashes and inspection extents are recorded in the source register (historical local record; not distributed here). No external action occurred.

# Audited historical reading edition

**Current audited claim:** PROVED: Every finite distinct real-affine-noncollinear point set admits a planar real-linear projection preserving point distinctness, noncollinearity and its entire unoriented direction set bijectively.

**Claim ceiling:** The projection depends on the finite configuration; no infinite-set or one-map-for-all claim.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Finite real point configurations admit a planar projection preserving all directions

**PROVED internally - M10-FINITE-PROJECTION-C122.** For every finite set of distinct real affine-noncollinear points in an arbitrary real vector space, a real-linear map on the finite difference span gives a distinct noncollinear planar image with exactly the same real unoriented pair directions, in bijection. This elementary lemma uses no Ungar theorem. A planar lower-bound consequence is separately **CONDITIONALLY_PROVED**, with its planar premise explicit. No primary Ungar statement, full Lemma4.2, Euclidean chromatic value, novelty, external review or formal verification follows.

Frozen attempt (historical local record; not distributed here). The proof below includes finite avoidance, every pair-direction constraint, exceptional cases and exact controls; it is an analytic proof, not an inference from successful examples.

## 1. Exact statement and conventions

Let V be any real vector space and S={x_1,...,x_n} a set of n>=3 distinct points not contained in one real affine line. Put W=span_R{x_i-x_1:1<=i<=n}; its finite dimension r satisfies 2<=r<=n-1. Define the finite set of unoriented directions

    D(S) = {R(x_i-x_j): 1<=i<j<=n}.

Here Rv is the one-dimensional real subspace spanned by nonzero v; multiplying v by any nonzero real, including a negative one, leaves the direction unchanged. No metric, angle, normalization, topology, probability or field F is used.

There exists a real-linear T:W->R^2, allowed to depend on S, such that y_i=T(x_i-x_1) are distinct and noncollinear, and R(x_i-x_j) -> R(y_i-y_j) is a well-defined bijection D(S)->D({y_i}). It does not assert that T is injective on all of W, that one T works for all S, that every projection works, or that an infinite configuration can be treated this way. No map on all of an infinite-dimensional V is required.

## 2. Elementary finite-avoidance lemma, with a finite choice bound

For a finite labelled list a_1,...,a_m of nonzero vectors in an r-dimensional real space, r>=1, choose a basis and write a_i=(a_i1,...,a_ir). There is a linear functional ell with ell(a_i)!=0 for every label, including when vectors repeat.

For a real parameter t define

    ell_t(z)=z_1+z_2 t+...+z_r t^(r-1).

For each nonzero a_i, p_i(t)=ell_t(a_i) is a nonzero polynomial of degree at most r-1. A nonzero real polynomial of degree d has at most d distinct real roots: induction on d proves this, because after any root a, polynomial division gives p(t)=(t-a)q(t), with deg(q)=d-1, and every other root is a root of q. A nonzero constant has none. Thus at most m(r-1) real numbers are bad for at least one p_i. Among the m(r-1)+1 distinct integers 0,...,m(r-1), at least one avoids every root. Take ell=ell_t at such an integer. If m=0, t=0 is permitted and there are no constraints.

This proves existence without a probabilistic or numerical genericity assumption. The integer coefficient row is relative to the chosen basis, not an assertion of rational coordinates of S. The finite root bound is not a measured software cost or a claimed efficiency improvement.

## 3. First coordinate: keep all pair differences nonzero

List the N=binom(n,2) nonzero vectors

    v_(i,j)=x_i-x_j,  i<j.

Keep this list labelled: repeated or opposite vectors cause no problem. Each lies in W. Apply section2 to select a linear functional a:W->R with a(v)!=0 for every vector in this full list. One may take a=ell_t with 0<=t<=N(r-1).

In particular, a(x_i-x_j)!=0 for every distinct pair. The first coordinate alone will make the image points distinct. It will not by itself guarantee noncollinearity or preserve directions; the next step is essential.

## 4. Second coordinate: do not merge nonparallel directions

Let P be the finite set of unordered pairs of distinct labels u,v in the difference list for which u and v are real-linearly independent. Let M=|P|<=binom(N,2). Fix either order for each such pair and set

    w_(u,v)=a(u)v-a(v)u.

Every w_(u,v) is nonzero. Otherwise, as a(u)!=0, the equation would give v=(a(v)/a(u))u, contradicting independence. The list of w-vectors is finite; repetitions are allowed and zero vectors have just been excluded. Section2 supplies a linear functional b with b(w_(u,v))!=0 for all P. In the same chosen coordinate basis b can be ell_s with 0<=s<=M(r-1). Define

    T(z)=(a(z),b(z)).

For every independent difference pair,

    det(Tu,Tv)=a(u)b(v)-a(v)b(u)=b(a(u)v-a(v)u)!=0.    (1)

Thus their images remain independent. The identity uses only linearity of b; no transpose, conjugation, norm or approximate sign test occurs. The order chosen for u,v changes only the sign, so cannot change nonvanishing.

For an independent algebraic check of the pivotal zero condition, normalize the pair by their nonzero first coordinates: the vectors u/a(u) and v/a(v) are distinct, and

    det(Tu,Tv)=a(u)a(v) b(v/a(v)-u/a(u)).

Multiplying the normalized difference by a(u)a(v) recovers w_(u,v). This checks the nonzero divisor and determinant convention by another algebraic expression within the same exposed review, not by an independent reviewer.

## 5. Complete direction equivalence, cardinality and noncollinearity

Every listed v has nonzero image, since its first coordinate a(v) is nonzero. If u=cv for some nonzero real c, then Tu=cTv by real linearity, so parallel original differences remain parallel and the direction assignment is well-defined. Conversely, if u,v are not real multiples, they are independent, the corresponding labelled pair lies in P, and (1) shows Tu,Tv cannot be parallel. Hence

    Ru=Rv  if and only if  R(Tu)=R(Tv)

for all pair differences. This covers parallel/repeated/opposite vectors as well as all independent pairs; no untested pair has been removed. Every pair direction of the image is the image of its original pair direction, because y_i-y_j=T(x_i-x_j). The induced map on direction sets is therefore injective and surjective.

For i<j, a(x_i-x_j)!=0 ensures y_i!=y_j, so exactly n points remain. Noncollinearity of S implies that two vectors x_i-x_1 and x_j-x_1 are independent: otherwise all nonzero vectors from x_1 would be scalar multiples of any one, placing S on one affine line. Their negatives x_1-x_i and x_1-x_j occur in the labelled list and remain independent under T by (1). Consequently y_i-y_1 and y_j-y_1 are independent, so the image is noncollinear. In particular M>=1 here. This completes the theorem for every admissible n,r and S.

When r=2 the resulting T has rank2 and is an isomorphism on W. When r>2 a kernel is unavoidable, but the selected kernel avoids this finite list of pair differences and the relevant two-dimensional direction spans. The statement never needed global injectivity. Finite-dimensional W is available even if V has infinite dimension; translation to x_1+W and the affine map on that set require no extension of T to V or topological/compactness assumption.

## 6. Conditional planar-bound transfer and exact source consumer

Fix n and a real number f(n). Assume the explicit premise B(n): every set of n distinct noncollinear points in R^2 has at least f(n) real unoriented pair directions. Sections1-5 give a planar set Y of n such points and a bijection of directions. Therefore

    |D(S)|=|D(Y)|>=f(n).

**CONDITIONALLY_PROVED - M10-PLANAR-BOUND-TRANSFER-C122**, conditional precisely on B(n), for the same n; no parity or small-n convention is changed. If a planar theorem is available only for n in a subset A, the consequence is only for n in A. No odd-n conclusion is silently inferred from an even-n theorem. The exact original Ungar statement and its small-n/parity/domain conventions remain unverified from its primary body.

For the source4.2consumer, suppose also F is a subfield of R, u_1,...,u_k are nonzero vectors, and each pair difference belongs to F u_j for some label j. Every nonzero such difference then has real direction R u_j. Thus

    |D(S)| <= |{R u_j:1<=j<=k}| <= k.

Together with B(n), this gives k>=f(n). In particular k>=n-1 follows if B(n) with f(n)=n-1 is assumed, exactly as a conditional consequence. Repeated/unused direction labels only strengthen the final inequality. No preservation of F-span closure, rank, source label witnesses or quotient forests under T is asserted; T is used solely to count real directions before the separate source4.2argument. The full source argument, thresholds, its recorded index issue and application are not proved here.

## 7. Adversarial checks and exact false shortcuts

**Good triangle control.** For S={0,e_1,e_2} in R^2, T(x,y)=(x+2y,x) has determinant -2 and images (0,0),(1,1),(2,0). Three distinct directions remain. This checks r=2/n=3 without importing a primary direction theorem.

**Good higher-dimensional control.** For S={0,e_1,e_2,e_3}, T(x,y,z)=(x+2y+4z,x+3y+9z) has images (0,0),(1,1),(2,3),(4,9). The six pair slopes are exactly 1,3/2,9/4,2,8/3,3, all distinct; all first-coordinate differences are nonzero. The original simplex has six pair directions, so this is a concrete allowed witness. These two finite controls illustrate the proof; neither establishes its universal quantifiers.

**FALSIFIED - M10-PROJECTION-SHORTCUT-C122:** injectivity on S plus preservation of noncollinearity does not force preservation of all directions. On the same tetrahedron, P(x,y,z)=(x+z,y+z) gives four distinct noncollinear image points 0,(1,0),(0,1),(1,1). Yet e_1 and e_3-e_2 are independent in R^3 and both map to (1,0); their distinct real directions merge. This exact counterexample explains why section4 is necessary. It refutes this shortcut, not the existential theorem.

**Additional collapse controls.** P_0(x,y,z)=(x,y) collapses 0 and e_3 on the tetrahedron. For a triangle, Q(x,y)=(x+2y,0) retains three distinct points but makes them collinear. These directly challenge any reasoning that tests only one of the required properties.

**Quantifier reversal fails.** For any fixed linear T:R^3->R^2, the three images of the standard basis are linearly dependent, giving a nonzero v in ker(T). Choose w not in Rv. The admissible set {0,v,w} has a collapsed pair. Thus no fixed T works for every noncollinear set in R^3. The proved order is forall S exists T, with T depending on all its pair constraints. No conclusion about a countably infinite list follows from finite root avoidance.

**Domain coverage.** Duplicates are excluded because a zero pair difference cannot have a direction or satisfy a(v)!=0. A collinear set cannot have a noncollinear linear image; its exclusion is essential. Many collinear subsets, repeated/opposite differences and arbitrary real coordinates remain covered by sections2-5. Real one-dimensional spans are the declared convention; no identification of F-linear directions or oriented rays is used. No rounding, precision tolerance or small numerical denominator hides a boundary case.

## 8. Review, source status and stopping

The two full native contexts (historical local record; not distributed here) are the121source-dependency dossier and120import map. They name the real-affine direction consumer, distinguish F from R, retain the known14-16proof location and document the failed primary retrieval. They were reread in full; their source mathematics is not independently corroborated by this reread. The120dossier's then-unknown citation identity is historical and superseded by121; its unverified primary-statement ceiling still applies. No PDF, external source or public endpoint was newly read122.

The finite projection dependency is now internally proved and should not be repeated without a new mathematical obligation. The primary Ungar statement/parity/domain remains INCONCLUSIVE, worldwide availability UNKNOWN after121's two route failures. Full4.2 remains INCONCLUSIVE; its whole application remains NOT_TESTED. Existing110weighted/115forest proofs and the printed4.4failure retain their scopes; this lemma does not overwrite them. Novelty is NOT_ESTABLISHED; no current global open-status claim is made. The proof uses elementary algebra reconstructed above and not an unverified external theorem.

This is one exposed actor/model's complete analytic derivation and challenge. It is not blind reproduction, human expert review or formal verification; local hash checks concern custody, not mathematical truth. The adjudication (historical local record; not distributed here) and run report (historical local record; not distributed here) keep those dimensions separate. No automatic full4.2proof, primary retry, further source chain, publication or external contact follows. The required fourteen-row rerank determines one next discriminating action.

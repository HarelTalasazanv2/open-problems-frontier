# Audited historical reading edition

**Current audited claim:** PROVED: For the literal F17/F23double covers the normalized plane blowup is the minimal base-field resolution, and the named sixteen divisor classes are independent with geometric Frobenius pI on their untwisted span.

**Claim ceiling:** Exact two finite-field models under named published surface-resolution and etale cycle/trace results. No independently chosen integral-model comparison, full operator, Picard rank18, RM/Hodge result or novelty.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle181: the explicit double-plane resolution and its divisor subspace

**PROVED, restricted finite-field models:** for k=F_17 or F_23, the normalized cover of the plane blown up at the fifteen nodes is the minimal resolution of the literal normalized double-plane X_k. The morphism and the named Cartier divisors are defined over k. With the numerical and C/T imports already admitted179/180, H and the fifteen exceptional cycle classes span sixteen dimensions of H²_et(Y_kbar,Q_l), for every l!=char(k), and geometric point-count Frobenius acts on this span by pI (by I in H²(1)). This is a local analytic proof relative to the stated standard imports, not external human or formal verification, a full cohomological operator reconstruction, or a new global Hodge/rank/RM theorem.

Here 'the named minimal resolution over F_p' means the minimal resolution of the literal F_p-cover used in the retained counts. Identifying its special fibre with a separately chosen integral model of a characteristic-zero surface would require a further comparison; that is not silently included in this result.

## Inputs and imported results

The equation is

F=(-y²+8yz-8z²)(7x²+40xz+56z²)(2x²+3xy+y²), W²=F.

The original equation is isomorphic by W=8w, invertible at17/23. Cycle174 and the independent finite-membership consumer179 bind the exact six k-lines, fifteen transverse k-rational pair intersections and absence of triple intersections to this F. Their retained hashes/certificates are ARTIFACT_VERIFIED this run; no field counts, incidences, Gram determinant or quartic calculations are rerun. In particular their geometry describes all geometric singularities, since all six factors are k-lines. C179 provides the numerical degree/pullback/restriction ingredients; C180 imports the precise cycle-map/cup/trace and Frobenius/Tate statements at smooth projective geometrically connected Q_l scope. Their published-proof debt and raw-source custody limits remain.

Three freshly inspected Stacks statements are used, with their displayed proof blocks read: [0C5S](https://stacks.math.columbia.edu/tag/0C5S), common point-blowup refinement of proper regular integral surfaces birational over a Noetherian base; [0C5R](https://stacks.math.columbia.edu/tag/0C5R), factorization of proper birational maps between regular integral surfaces into closed-point blowups; [0C5J](https://stacks.math.columbia.edu/tag/0C5J), descent of a morphism constant on the exceptional curve through an existing contraction. Earlier dependencies and omitted details in these standard results are imports, not locally reproduced proofs. The unrelated genus-positive curve-model uniqueness theorem used as a link locator is not a surface-resolution theorem and is not adopted.

## The cover and its normality

Define X as the relative Spec over P²_k of O plus O(-3), with odd generator squaring to F. This is the finite double cover underlying the weighted equation, without any extraneous weighted-projective vertex. Each affine plane chart has ring R[W]/(W²-f), R a polynomial ring or its localization, f a reduced product of distinct linear factors up to a unit. The function f is not a square even over kbar: a branch-line valuation is odd. Thus the cover and its base change are integral quadratic covers.

For completeness normality can be checked without a smoothness inference. If a+bW in the quadratic function field is integral over R, its conjugate is integral, so its trace2a is integral. R is integrally closed and2 is a unit, whence a belongs to R. Then b²f is integral and lies in Frac(R), so lies in R. For every irreducible divisor, 2val(b)+val(f)>=0. Squarefreeness gives val(f) equal to0 or1, and therefore val(b)>=0. Unique factorization in R gives b in R. Hence R[W] is its integral closure. The argument applies over kbar too.

Away from a branch line the derivative2W is nonzero. At a point on exactly one branch line, a local equation W²=u*g with g a unit has nonzero u-derivative when W=u=0. At a two-line intersection choose the two line equations as local coordinates u,v. Then

W²=u*v*g(u,v), c=g(0,0)!=0.

These are the only singular points. We do not replace the nonconstant unit g by c in this local ring. Such a replacement would require an additional square-root or change-of-coordinates argument.

## Global construction and the two charts

Let pi:B->P² blow up the fifteen distinct rational nodes, with exceptional divisors F_i and h=pi*O(1). The six strict branch lines are smooth and disjoint, with total divisor D in |6h-2sum F_i|. Set L=O_B(3h-sum F_i). The transformed section of L² defines the finite flat cover f:Y=Spec_B(O_B plus L^(-1))->B. The natural inclusion pi*O(-3) into L^(-1) defines a global algebra homomorphism from the pulled-back X algebra to the Y algebra, and thus a k-morphism q:Y->X. Locally this is the W-rescaling below. This algebra inclusion also supplies global gluing, not just a collection of unrelated local smooth models.

Over a node the first plane-blowup chart is v=u*t. Its normalized cover has equation

r²=t*g(u,u*t), with q(u,t,r)=(u,u*t,u*r).

The second chart is u=v*s and

z²=s*g(v*s,v), with q(v,s,z)=(v*s,v,v*z).

On the overlap t is invertible and s=1/t, v=u*t, z=r/t. Substitution verifies both equations and both q formulas exactly, retaining the full g. The raw fibre-product equation W²=u²*t*g is not substituted for this normalization: its fibre u=0 has W²=0 and is nonreduced.

Each normalized chart is finite over that raw pullback (adjoin r or z, satisfying a monic quadratic), has the same fraction field, and is normal. For the latter, on u=0 the t-derivative of r²-t*g(u,u*t) is -c, never zero; the other chart has s-derivative -c on v=0. Away from the exceptional divisor it agrees with the already smooth complement of the old node. Thus Y is smooth on all charts, including the two exceptional branch endpoints. A finite birational normal extension is the full integral closure: every element integral over the smaller ring is integral over the larger ring and lies there by normality. This verifies the normalization description rather than assuming it.

Finite-over-projective makes Y projective over k. Its function field is that of X, and the construction remains integral over kbar, so it is geometrically connected. The map q is proper (Y is proper over k and X is separated), birational and an isomorphism away from the nodes. These properties and smoothness make q a resolution over k.

## The exceptional curves and the actual divisor bindings

Over one F_i the charts reduce to r²=c*t and z²=c*s with z=r/t. Thus the exceptional curve E_i is reduced and irreducible, even if c is a nonsquare. Coordinates a=r and a'=z/c satisfy a*a'=1 on the overlap; they exhibit E_i as P¹_k without extracting sqrt(c). Its map to F_i=P¹ has degree2, ramified at the two rational branch directions. This also covers the r=0 and z=0 endpoints, which cannot be discarded by working only on the overlap.

The Cartier inverse image f*F_i is exactly E_i, with multiplicity one, as seen from the prime local equation u=0 (or v=0). Therefore N_(E_i/Y) is the pullback of N_(F_i/B)=O_P1(-1) by the degree-two map. The admitted numerical degree formula gives E_i²=-2. The E_i are disjoint, and there are no other exceptional curves of q, since q is an isomorphism off the nodes. The commuting cover/blowup diagram binds H=f*h to the pullback of O(1) from the target double-plane. It binds each E_i to the node labelled by its exact line pair in the retained input. All maps, divisors and coordinate gluings are over k, not merely over kbar.

## Minimality and uniqueness over the base field

We prove a stronger mapping property instead of silently invoking a generic 'no minus-one curves' slogan. Let q':Y'->X be any proper regular integral resolution. Apply0C5S over the Noetherian base S=X to get a common regular refinement Z, with a:Z->Y and b:Z->Y' sequences of closed-point blowups. If b is not an isomorphism, take its last blowup beta:Z->Z_1, with exceptional curve C=P¹_(kappa(x)) and normal bundle O_C(-1). Its image in X is a point.

If a(C) were a curve, it would be one of the E_i, since those are all the curves contracted by q. The birational map a identifies C with the strict transform of E_i. Their function fields would agree. Because the algebraic constant field of k(E_i)=k(t) is k, whereas that of k(C)=kappa(x)(t) is kappa(x), this forces kappa(x)=k. Thus C²=-1 in this only possible noncontracted case; we do not incorrectly assign -1 over k to a blowup at a nonrational point.

On the other hand, under a sequence of point blowups the strict transform of the smooth curve E_i has square E_i² minus a sum of nonnegative residue-field degrees at centres on the successive strict transforms. This follows by writing total transform as strict transform plus the exceptional divisor and using its degree-minus-one normal bundle; the multiplicity is one because those strict transforms are smooth. Therefore C²<=-2, a contradiction. It follows that a contracts C to a point, including automatically the case kappa(x)!=k.

By0C5J, a descends through beta to a_1:Z_1->Y. This descended map is proper birational between regular integral surfaces: properness follows from properness of Z_1 over X and separatedness of Y over X, and birationality from the common dense open. By0C5R it again factors into point blowups. Induct on the length of b. The result is a morphism Y'->Y over X. It is unique, since any two such morphisms agree on the dense open above the regular locus of X and Y is separated.

Consequently Y is the terminal, minimal resolution over k. Equivalently, if Y' is another resolution without a contractible exceptional curve of the first kind, the proper birational morphism Y'->Y factors by0C5R; a nonempty factorization would exhibit just such a last exceptional curve on Y'. Hence it is an isomorphism. This proves the named minimal-resolution binding over F_p without an unsupported descent from an isomorphism over kbar.

## Cohomological consequence and attacks

G is now established for the two literal finite-field covers. C179's numerical pairing diag(2,-2,...,-2) becomes the actual cup/trace pairing by the source-admitted C180 imports. Its nonzero determinant gives sixteen independent Q_l classes, including l=2. Since the individual divisors descend to F_p, their H²(1) classes are fixed. The admitted geometric-Frobenius convention untwists this to pI on their untwisted span. This proves the restriction of the operator mathematically; it does not claim an observed or reconstructed full operator.

Adversarial review: both normalized charts, their inverse overlap and both exceptional endpoints were checked. Keeping g addresses the unsupported Zariski square-root shortcut: g=1+u need not have a square root in k(u,v), so a general unit cannot simply be absorbed. The nonsquare-c case is handled by the explicit P¹ coordinates. Characteristic2, nonreduced branch factors and triple intersections are excluded by the frozen inputs; the proof does not extend to them. Raw unnormalized base change fails the reduced exceptional-fibre test. Closed points with nontrivial residue field are handled explicitly in the minimality argument. A smooth resolution alone is insufficient; the mapping-property proof supplies minimality and uniqueness. A separately chosen integral model is not identified by assertion.

Verdicts: G and the sixteen-class finite-field statement PASS AT CLAIM CEILING/PROVED with named standard imports. Full degree22 operator, residual-degree-six reconstruction, degree-three counts, Picard upper bounds/rank18, RM/field action, tensor/Hodge conclusions, novelty, external expert review and formal verification remain NOT_TESTED or held at their earlier specific gaps. No global percentage or method gain is measured. Source/import proofs, selected input artifacts, expected scalar action and analyst are shared with earlier work; this is not a blind or external reproduction.

The numerical/divisor subspace family is now closed. After three constructive stages179-181, rerank rather than replay it. The prepared next obligation is to specify exactly which Lefschetz/K3 dimension and reciprocity hypotheses make the retained degree-one/two counts into constraints on a six-dimensional quotient, and identify the first missing independent trace before authorizing any expensive cubic count.

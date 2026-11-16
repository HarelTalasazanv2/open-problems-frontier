# Rational Hodge classes on a surface times projective space

## Exact statement and claim ceiling

Let S be a connected smooth complex projective surface. Let r be any integer at least zero and let 0 <= p <= r+2 be an integer. Set X=S x P^r. Every alpha in H^(2p)(X,Q) whose complexification is of type (p,p) is a rational linear combination of cohomology classes of algebraic codimension-p cycles on X.

This is an internal derivation of a known restricted case from standard cohomological ingredients, not a novel theorem or a proof of the general Hodge conjecture. It assumes the class is rational and of the stated Hodge type. It is an existence construction given divisor representatives; it is not an algorithm to recognize Hodge classes or compute arbitrary Picard groups. No integral analogue or effective-cycle assertion is included.

All cohomology below is Betti cohomology. Put h=c1(O_P^r(1)); the normalization is integral_(P^r) h^r=1. Use the same letter for its pullback to X. For r=0, h=0 and h^0=1, so the conventions still apply.

## Dependency map

1. The rational cycle-class formulation and the fact that an algebraic codimension-a cycle has type (a,a) are given in Deligne's official Clay description, physical/printed pages1-2.
2. The divisor theorem follows from the exponential sequence, as recalled on page2, Remark2(iii). A proof of the exact rational consequence is given below.
3. Rational Kunneth and the projective-space ring H*(P^r,Q)=Q[h]/(h^(r+1)) give the finite decomposition. The compatibility of the Hodge decomposition with Kunneth is explicit on page4, section4, Example1. Kunneth itself and Poincare duality are standard imported foundational theorems, not newly proved here.
4. The projective-space ring has one generator h^j in each even degree2j and no odd-degree cohomology. Its generator is the class of a codimension-j linear subspace. This fixes both degree and algebraic normalization.
5. Cycle classes commute with external products and pullbacks. Integration over the projective factor is rational, lowers bidegrees by (r,r), and satisfies the product/projection formula. These standard functorial properties are explicit dependencies; the coefficient identity is checked independently below.

Primary source: https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf . Owning current listing: https://www.claymath.org/millennium/hodge-conjecture/ . That listing was inspected historically; this audit makes no exhaustive current-status or novelty claim.

## 1. Divisor classes on S: rationality and algebraicity

Let u in H^2(S,Q) be of type (1,1). Since S is compact and has finite CW type, the image of H^2(S,Z) modulo torsion is a lattice in H^2(S,Q). Choose a positive integer n so that n*u is the rational image of an integral class c. The complex image of c has type (1,1); torsion vanishes on passage to C.

The cohomology sequence of

    0 -> Z -> O_S --exp(2*pi*i*.)--> O_S^* -> 0

gives exactness at H^2(S,Z): the kernel of its map to H^2(S,O_S) is the image of H^1(S,O_S^*) under the first Chern class. The natural map to H^2(S,O_S) is the (0,2) component under the Hodge/Dolbeault identification. Thus c is in that kernel and is c1(L) for an analytic line bundle L. Projectivity and GAGA make L algebraic. A nonzero rational section of L defines a Cartier divisor D (allowed to have positive and negative components), and cl(D)=c in integral cohomology. Hence u=cl(D)/n in rational cohomology.

No torsion obstruction or demand for effectiveness was hidden in this step. Clearing denominators is precisely why the rational input is sufficient. This proof is the known divisor theorem used as a dependency, not a new result.

## 2. Exact Kunneth decomposition and Hodge-type restriction

Define the finite index set

    J(p,r) = {j in Z : max(0,p-2) <= j <= min(r,p)}.

Kunneth over Q and the cohomology of projective space give a unique expression

    alpha = sum_(j in J(p,r)) pi_S^*(u_j) cup h^j,
    u_j in H^(2(p-j))(S,Q).

Indeed, the projective factor contributes only degree2j, and the surface has even cohomological degrees0,2,4 in this decomposition. Its odd cohomology cannot occur in total degree2p because projective space has no odd cohomology. Thus a=p-j is exactly0,1 or2; there are no omitted mixed odd-degree summands.

The decomposition is Hodge-compatible and h^j has type(j,j). Consequently a (p,p) class has u_j of type(p-j,p-j) for every j. Non-Hodge components cannot cancel between j's: the Kunneth summands form a direct sum of Hodge structures. The independent projection calculation in section4 proves this conclusion without relying on a cancellation assertion alone.

## 3. Algebraic representative for every summand

For each j in J(p,r), put a=p-j.

- If a=0, connectedness gives H^0(S,Q)=Q*1. Write u_j=q_j*1 and represent it by the rational codimension-zero cycle q_j*S.
- If a=1, section1 gives a rational divisor cycle Z_j with cl(Z_j)=u_j.
- If a=2, compact connected complex-oriented S has H^4(S,Q)=Q*[point]. The class of any complex point integrates to1, so a rational multiple of that point represents u_j.

Let L_j be a linear subspace of P^r of codimension j. It exists for exactly0<=j<=r and has class h^j. In each case the external product Z_j x L_j has codimension a+j=p and class pi_S^*(u_j) cup h^j. Their finite sum represents alpha. This proves the stated theorem.

## 4. Independent coefficient extraction and degree challenge

For every j with0<=j<=r, integration along the projective factor gives

    u_j = (pi_S)_*(alpha cup h^(r-j)),

where absent-degree coefficients are interpreted as zero. To check the formula, insert the Kunneth expansion. A term indexed by k contains h^(k+r-j). If k>j, that power exceeds r and is zero. If k<j, its projective degree is less than2r and its fibre integral is zero. For k=j, the fibre integral of h^r is1. Thus only the desired coefficient remains, with no sign or factorial factor.

This independently checks the exponents r-j and p-j, the coefficient normalization, and the endpoint j=r. It also proves u_j is rational. If alpha has type(p,p), the product has type(p+r-j,p+r-j), and fibre integration reduces that by(r,r), yielding type(p-j,p-j). This is the same necessary type condition derived by Kunneth compatibility.

This projection is a different check of the pivotal algebraic indexing step, not an independent human or blind reproduction. Both routes use the same standard cohomological model and source conventions.

## 5. Boundary and scope audit

- r=0: J contains only j=0 when a=p is0,1,2, so the argument is exactly the known surface case.
- p=0: the sole term is j=0,a=0; rational multiples of X represent all classes.
- p=r+2: the sole term is j=r,a=2; rational multiples of point x point represent all top classes, with integral1 normalization.
- For intermediate p, J is the intersection of0<=j<=r and0<=p-j<=2, so it covers every and only allowed Kunneth term. Empty/out-of-degree surface groups are never supplied a fictitious cycle.
- Disconnected S is not in the stated input domain. A finite componentwise extension is possible but was not required or promoted.
- Smooth projectivity is used for the Hodge package, algebraic line bundles via GAGA, and the intended cycle formulation. No conclusion for arbitrary compact Kahler manifolds is claimed.
- The argument uses rational cycle coefficients and permits differences. It does not construct an effective cycle for every Hodge class or assert the integral conjecture on arbitrary varieties.

## 6. Analytic attacks on two overbroad variants

### Dropping rationality: FALSIFIED only for that variant

Take S=P^2, r=0, p=1 and let h be its integral hyperplane class. The class alpha=sqrt(2)*h is of type(1,1) in complex (indeed real) cohomology. If it were the class of a rational divisor cycle, its intersection with h would be rational, because each integral divisor has integral intersection number and the coefficients are rational. But integral_(P^2) alpha cup h=sqrt(2), which is irrational. Thus the overbroad assertion for every complex (1,1) class is false. It is not a counterexample to the rational theorem.

### Dropping Hodge type: FALSIFIED only for that variant

Let E=C/(Z+iZ) be the square elliptic curve and S=E x E, a smooth projective surface. Write z_k=x_k+i*y_k with x_k,y_k of period1 and use the orientation volume form

    v=dx1 wedge dy1 wedge dx2 wedge dy2, integral_S v=1.

The class

    alpha=dx1 wedge dx2 - dy1 wedge dy2

is integral: the one-forms dx_k,dy_k represent the dual integral lattice basis. The holomorphic2-form is omega=dz1 wedge dz2. Expanding the wedge product gives

    alpha wedge omega = 2*v,
    integral_S alpha wedge omega = 2.

For detail, set A=dx1 wedge dx2 and B=dy1 wedge dy2. Then A wedge B=-v and (A-B)^2=-2*A wedge B=2*v; the cross-terms with the imaginary part of omega have repeated one-forms and vanish. Every class of type(1,1) pairs to zero with omega because their product would have type(3,1) on a surface. Thus alpha is rational but not of type(1,1), and cannot be the class of a rational divisor cycle. This refutes only the variant with the Hodge condition omitted.

Both attacks are exact analytic examples, not a numerical grid or experimental evidence. They establish that two domain hypotheses cannot simply be discarded. They do not assert that every hypothesis of the restricted theorem is logically necessary.

## 7. What the proof excludes, and the next genuine obstruction

A search for a rational-Hodge counterexample inside S x P^r cannot succeed under these hypotheses: every class has the explicit factorwise construction above. Increasing r adds only algebraic Tate-type projective classes, not new cohomological mechanisms. This is useful local exclusion of an untested catalog family, not a measured gain or a global-resolution claim.

For a product of two positive-dimensional non-Tate factors, such as two surfaces, middle cohomology can contain H^2(S1,Q) tensor H^2(S2,Q). A (2,2) tensor can involve (2,0) tensor (0,2) and its conjugate, so the factorwise-divisor argument does not cover it. The next obligation would have to identify an exact such rational tensor and a primary-source status for that chosen family, then construct an algebraic correspondence or prove an actual obstruction. No claim is made that a particular surface pair or K3 family is newly open; many special correspondence results are known. This run does not select that extension.

## Assurance

The proof is internal and exposed to the expected known result. Imported standard theorems, source retrieval, parser checks and mathematical derivation are distinct evidence dimensions. No external human, blind or formal verification occurred. No novelty, best-bound, least-unresolved-case or scientific performance ratio is claimed. No new mathematical/numerical instrument was used to infer the universal quantifiers.

## Audit batch002 adjudication

The complete analytic proof above was rechecked, including the exact coefficient extraction, all parameter endpoints, the divisor argument and both domain counterexamples. The general derivation uses the named standard cohomological imports; a finite index test does not prove its universal quantifiers. PASS_RESTRICTED: the stated known rational surface-times-projective-space theorem only. See [analytic audit](ANALYTIC_AUDIT.json) and [references](REFERENCES.md).

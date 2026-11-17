# Historical project dependency reading edition

The source import statuses below are historical. The current C181 audit supplies the separately reviewed geometric binding. Published standard theorems remain imports, not locally reproduced proofs.

# Cycle180: source-admitted cycle and Tate conventions

**CONDITIONALLY_PROVED under G:** for p=17 or 23 and every prime l different from p, the sixteen named classes H,E_1,...,E_15 on the target resolution span a 16-dimensional subspace of H²_et(S_Fbar,Q_l); point-count geometric Frobenius acts there by pI, and on its Tate(1) twist by I. G is the still-unadmitted identification of the Cycle179 double-cover construction, including its Cartier divisors, with the named minimal resolution. No actual full cohomological operator has been measured. This run removes the separate C/T source holds for the smooth projective geometrically connected construction; it does not remove G.

The imported theorems below are **SOURCE_STATEMENT_ADMITTED, NOT LOCALLY REPROVED**. The elementary consequences are proved here relative to them. This distinction is necessary: the inspected source omits the proof of its cycle-map comparison and explicitly warns about its Chern-character exposition and a flawed proof in its older book. Neither that exposition nor the older proof is adopted as a reproduced proof.

## Exact source and domain

J.S. Milne, *Lectures on Étale Cohomology*, v2.21, March 22, 2013, 202 physical pages, author-owned [PDF](https://www.jmilne.org/math/CourseNotes/LEC.pdf), [version page](https://www.jmilne.org/math/CourseNotes/lec.html), [errata](https://www.jmilne.org/math/CourseNotes/errata.html). Author/version identity is supported by the owning page. All PDF reads are provider-parsed text. Raw PDF bytes/hash, local pagination validation and visual completeness remain UNKNOWN after two raw timeouts and four failed screenshot requests. Physical page numbers below are provider page indices plus one; printed labels agree where displayed. See provider_extent_receipt.json for the larger actual returned ranges.

We use S/F_p smooth, projective and geometrically connected of dimension two, l!=p, V=H²_et(S_Fbar,Q_l). Write Q_l(1)=(lim_n mu_(l^n)(Fbar)) tensor_Z_l Q_l with its natural Galois action. Arithmetic Frobenius sigma sends x to x^p; geometric Frobenius gamma=sigma^(-1). A divisor means a Cartier divisor, with its associated invertible sheaf. Classes and products use rational l-adic coefficients, not reduction of a Gram matrix modulo l. Projectivity is retained because the inspected Chern-class construction is stated for projective varieties. We do not silently extend that source admission to every nonprojective proper surface.

## C: divisor classes and the intersection pairing

The opening of section23, physical138/providerL7011-7065, gives the divisor class as the connecting map for the Kummer sequence Pic(S_Fbar)->H²(S_Fbar,Lambda(1)). Section23 Theorem23.4 and its adjoining properties, physical142/providerL7270-7284, state compatibility of the cycle map with products and agreement with the direct Gysin definition. The rational Q_l statement there explicitly removes the temporary lower bound on l that appeared in the integral construction. It therefore covers l=2 as well as larger l, always with l!=p.

For a base-field automorphism, the induced equivalence of étale sites respects the Kummer sequence. Connecting homomorphisms are natural, so cl(sigma D)=sigma cl(D). The source's field-automorphism discussion, physical167/providerL8761-8779, and section23.7 physical143/providerL7318-7341 support the Galois interpretation. If D descends to F_p, O(D) and hence its class are fixed in V(1). This uses the line bundle/class, not a requirement that every point of D be rational.

Theorem24.1(a), physical144/providerL7389-7419, normalizes the trace H_c^4(S_Fbar,Lambda(2))->Lambda by sending the Gysin class of a geometric closed point to 1. Properness identifies compactly supported and ordinary cohomology. Compatibility as n varies and rationalization give tr:H^4(S_Fbar,Q_l(2))->Q_l. The adjacent text, physical145/providerL7421-7424, identifies the pairing with cup product in the quasi-projective case. Projective S is in that case.

Consequently, for divisors D,E on S_Fbar, cycle-map multiplicativity gives cl(D) cup cl(E)=cl(D.E) in H^4(2), and the point normalization gives

tr(cl(D) cup cl(E))=deg(D.E).

Both twists are essential. Zero-cycles and their degrees here are over Fbar, so geometric points have degree one. A closed point of degree d over F_p splits into d geometric points; applying the formula to that base change gives d, not one. Geometric connectedness avoids adopting the source's displayed single-copy trace isomorphism for a disconnected variety without modification. Intersection need not be represented by distinct transverse divisors: the cycle-map ring statement includes self-intersections in the Chow ring.

## T: Frobenius direction derived from the coefficients

Section16 definitions, physical108/providerL5464-5482, identify Lambda(1) with the sheaf of roots of unity. On each mu_(l^n), sigma(zeta)=zeta^p; in additive Z/l^n-module notation this is multiplication by p. Since l!=p, p is invertible at every level. Thus sigma acts on Q_l(1) by p and gamma by 1/p. This is an exact algebraic calculation; there is no numerical approximation or small-denominator tolerance.

For v tensor t in V(1), gamma(v tensor t)=gamma(v) tensor (t/p). A fixed twisted divisor class therefore corresponds to gamma(v)=p v in V. The zero class satisfies the identity too; independence, not a division by v, supplies the nonzero subspace below. On Q_l(r) the same convention gives p^(-r).

Milne Proposition29.10, physical167/providerL8773-8805, states that the variety/sheaf Frobenius action on cohomology is inverse to the arithmetic field-automorphism action. This is the needed binding to the point-count convention, not just a name attached to a matrix. Its general proof is omitted in the notes and is imported as a stated theorem. The nearby dual-action warning, physical167-168/providerL8806-8830, reinforces the distinction between Galois dual actions and ring endomorphism actions.

## Application and adversarial checks

Cycle179's already checked construction and exact numerical pairing are ARTIFACT_VERIFIED, not recomputed here. Under G the construction is smooth projective geometrically connected, its divisors descend to F_p, and its Gram matrix is diag(2,-2,...,-2), determinant -65536. The new C imports identify this numerical matrix with the cup/trace matrix. Pairing any linear relation against each basis class gives Ga=0, hence a=0 over Q_l, including Q_2. These are sixteen independent classes, not sixteen assumed dimensions. Their rationality and T give pI on the untwisted span and I after twisting. The conditional factor (T-p)^16 follows for this span only; it is not the full characteristic polynomial.

Decisive attacks: (1) reversing arithmetic/geometric Frobenius would predict 1/p rather than p on untwisted divisor classes; the root-of-unity calculation rejects that reversal. (2) Galois stability alone permits permutation of classes; actual descent of each named divisor supplies pointwise fixedness. (3) omitting the twists destroys the Galois-invariant pairing convention. (4) integral reduction modulo2 makes the displayed Gram singular, but the stated coefficient field is Q_2, where the determinant is nonzero. (5) the trace statement is used on a connected projective surface, not an unrestricted disconnected/nonproper object. (6) a rational divisor need not be pointwise rational. (7) the Tate conjecture converse is unnecessary: only algebraic classes imply fixed classes, never the reverse. (8) a source theorem with an omitted proof is an import, not a locally reproduced theorem.

Verdict: PASS AT CLAIM CEILING for this source-bound C/T admission and its conditional deduction; HOLD for G and any unconditional target-resolution conclusion. No new finite search, interval certificate, formal kernel, independent human review, blind reproduction, rank18/RM claim, full Frobenius polynomial, novelty or current-world open-status determination. Same analyst, prior expected result and source conventions were shared. The coefficient calculation is a second route for convention errors, not independent external review.

The next discriminating action is to prove or source-admit G using the actual node equation W²=uv*unit, its two normalized blowup charts, contraction map and divisor identifications over F_p. That can remove the last named condition on this 16-class subspace; another Gram calculation cannot. Full degree-six/residual reconstruction and the later rank/RM/tensor obligations remain separate.

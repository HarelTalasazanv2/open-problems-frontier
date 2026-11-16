# Four exact point counts for a literal double plane

**CERTIFIED_RANGE:** for the singular double cover Y of P² given by

W² = (-y²+8yz-8z²)(7x²+40xz+56z²)(2x²+3xy+y²),

the counts below hold in exactly the four fields shown. The cover uses the line bundle O(3), equivalently weights (1,1,1,3); it is not an ordinary degree-six hypersurface in P³.

| Field | Canonical base points | Singular Y | Minimal resolution X |
|---|---:|---:|---:|
| F17 | 307 | 313 | 568 |
| F23 | 553 | 547 | 892 |
| F17[u]/(u²-3) | 83,811 | 83,881 | 88,216 |
| F23[v]/(v²-5) | 280,371 | 280,729 | 288,664 |

The integer irreducibility checks for the two quadratic moduli are complete: 3 is not a square modulo17 and5 is not a square modulo23. Elements of an extension are represented by a+p*b for a+b*u. The extension count is not a count over the integers modulo p².

## Projective fibres and complete domains

Every base point has a unique representative in (1,y,z), (0,1,z), (0,0,1). Their disjoint domain sizes are q²,q,1. On changing a base representative by λ, F changes by λ⁶ and W by λ³; multiplication by λ³ bijects the roots, including at F=0. Thus each fibre has exactly the number of roots of W²=F in the field:1 at zero,2 at a nonzero square,0 at a nonsquare. There is no extra point above the zero base vector.

The producer enumerates all squares to obtain those root multiplicities and evaluates the three quadratic factors with exact field arithmetic. The consumer takes a different arithmetic path. Splitting the first two quadratics over F17/F23 gives six rational lines, and Vieta identities verify

F = -7 product(L_i),

with L_i=(y-r1*z),(y-r2*z),(x-s1*z),(x-s2*z),(x+y),(2x+y). For the quadratic extensions, the character identity χ_(p²)(a+b*u)=χ_p(a²-d*b²) follows by raising to (p²-1)/2 and using the field norm. Thus the consumer computes six prime-field norms and a Legendre character; it does not call the producer's field multiplication, sextic evaluator or square table. Base-field consumption uses the six linear values and the scalar-7 directly.

Each fibre is compared, not just its sum. Explicit chart indices must visit exactly0..q²+q, without duplicates. The number of branch fibres must also be6q-9 by inclusion-exclusion for six lines and15double intersections without triples. The two saved historical extension payloads are separately transported between their z-first charts and the new x-first charts, with every membership and byte checked. Hash matching is a custody check, not the mathematical reason for agreement.

The certificates and all per-fibre data are in [counts](counts/AUDIT_CERTIFICATE.json). The [checker](finite_count_audit.py) runs under Python3 using only its standard library. No floating-point mathematical operations or tolerances occur.36negative consumer controls pass across the four fields: wrong model/field/chart sizes, short/long payloads, invalid multiplicity with a new hash, a same-total zero/two-root swap with a new hash, incorrect resolution correction, and a reducible extension modulus. Complete zero/square/nonsquare model fixtures check branch and infinity contributions independently of the target answers.

## Resolution correction and its geometry

The [certificate](counts/AUDIT_CERTIFICATE.json) lists six distinct rational branch lines and every unordered pair intersection at each base prime. All15points are distinct and have exactly two incident lines. The remaining factors are units there. A line crossing is transverse because its two distinct linear equations are independent local coordinates. Away from the branch divisor the cover is étale; over a smooth branch point its equation has a nonzero base derivative. Therefore these15points are exactly its singularities, over the algebraic closure as well as the base field. They stay rational and distinct in the two extensions.

Locally at a crossing the equation is W²=u*v*g(u,v), with c=g(0,0) nonzero. Blowing up the point gives the u-chart v=u*s, W=u*r, whose strict-transform equation is r²=s*g(u,u*s). Along its exceptional locus the derivative in s is -c, so it is smooth. The v-chart is analogous. These two charts cover the exceptional conic because on W²=cUV neither U nor V can both vanish. Away from the exceptional locus the blowup is an isomorphism. The exceptional curve is the nonsingular conic W²=cUV, whose U=1 chart has q choices of W and uniquely determined V, plus its one U=0 point. This is q+1 rational points even when c is a nonsquare.

The double cover is normal: it is a hypersurface (hence satisfies the Cohen–Macaulay/S2 condition) with only isolated singularities (hence R1), so Serre's criterion applies. The blowup is proper and birational. Its exceptional conic has normal bundle O_P²(-1) restricted to a conic, namely O_P¹(-2). Consequently this resolution has no exceptional(-1)-curve and is the minimal resolution of the normal double plane. These standard algebraic-geometric facts about blowups, normality and minimal resolutions are declared imports, not kernel-verified foundations. The local equations above check their application, including nonsquare units and the missing infinity point.

Replacing each old singular point by q+1points adds q, not q+1. Thus #X=#Y+15q, as in the table.

## Source identity and claim ceiling

At t=1 the rational quadratic forms in Elsenhans–Jahnel's family have8*q1=-y²+8yz-8z²,8*q2=7x²+40xz+56z² and q3=(x+y)(2x+y). Hence W=8w gives the displayed model, invertibly at17and23. The primary formula and Theorem6.6 were checked through their [versioned source](https://arxiv.org/html/1402.4555v2#S6); bibliographic credit is in [references](REFERENCES.md). This source match is separate from the theorem's full rank/RM proof. Its Theorem6.3 requires2to be a nonsquare and cannot be substituted for these counts.

The arithmetic algorithms were newly written by the same actor with the model and expected answers exposed. Their agreement addresses some implementation errors, not shared-model error or all foundational dependencies. No blind reproduction, external mathematical review, formal proof, novelty, full Frobenius-polynomial identification, Picard-rank/RM reproduction, or global Hodge solution is claimed.

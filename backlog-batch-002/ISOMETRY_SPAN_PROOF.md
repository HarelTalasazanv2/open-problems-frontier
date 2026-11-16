# Exact isometry-span obstruction under a real-field adjoint

## Statement and assurance boundary

Let T be a nonzero finite-dimensional rational vector space carrying a Hodge structure and a nondegenerate symmetric bilinear form q. Suppose the algebra E=End_Hdg(T) is a field of characteristic zero and the q-adjoint involution restricts to the identity on E. Then the rational Hodge q-isometries of T are exactly +id and -id, and their Q-linear span is Q*id.

If moreover E is identified with Q(sqrt(2)), let psi denote the endomorphism represented by sqrt(2). Then psi is outside that span, satisfies q(psi*x,psi*y)=2*q(x,y), and has no rational scalar multiple which is a q-isometry.

This is an internal exact algebraic implication. It is not an assertion that a specified K3 surface realizes these hypotheses. In the geometric application below, the endomorphism field, adjoint and actual surface remain named assumptions. No nonalgebraicity conclusion follows from failure of this particular isometry-based route.

## 1. Isometry, adjoint and the field hypothesis

The adjoint u^dagger is defined by

    q(u*x,y)=q(x,u^dagger*y) for all x,y in T.

Nondegeneracy makes it unique. A Hodge endomorphism u is a q-isometry exactly when u^dagger*u=id: indeed q(u*x,u*y)=q(x,u^dagger*u*y), and nondegeneracy proves equivalence with q(x,y). Such a map is automatically invertible in finite dimension.

By the declared adjoint assumption, every u in E satisfies u^dagger=u. Thus an isometry satisfies u^2=1. In the field E,

    (u-1)(u+1)=0

forces u=1 or u=-1. Conversely these two maps are Hodge q-isometries. Characteristic zero distinguishes them and nonzero T makes id nonzero. Their Q-span, as well as the Q-algebra they generate, is Q*id. No assertion about the dimension, signature or period of an actual K3 realization was used.

## 2. The exact quadratic element and normalization failure

Because E=Q(sqrt(2)) and psi corresponds to sqrt(2), psi is not a rational scalar. Equivalently its minimal polynomial overQ is t^2-2, irreducible overQ. Therefore psi is not in Q*id, hence not a rational linear combination of Hodge isometries of T.

The adjoint identity and psi^2=2id give

    q(psi*x,psi*y)=q(x,psi^dagger*psi*y)=2*q(x,y).

Thus psi is a Hodge similitude of multiplier2, not a q-isometry. Nondegenerate q on nonzero T has at least one pair x,y with nonzero pairing, so multiplier2 cannot also be multiplier1.

For c in Q, c*psi is isometric if and only if 2*c^2=1. No rational c satisfies this: for nonzero rational c, the2-adic valuation of 2*c^2 is the odd integer1+2*v_2(c), whereas v_2(1)=0. c=0 is not an isometry. Real scalar multiplication of the underlying rational matrix by1/sqrt(2) is not an allowed rational scalar rescaling. In contrast, composition in E with psi/2 gives (psi/2) composed with psi=id; this uses another endomorphism and changes the target map. These are different operations. Neither expresses psi as a rational linear combination of the known isometries.

The last distinction matters: composing a hypothesized algebraic sqrt(2)-correspondence with another endomorphism would already assume the missing algebraicity input. It is not a use of an isometry theorem alone.

## 3. Exact conditional Hodge tensor

Suppose S is a projective K3 surface with

    T=NS(S)_Q^perp in H^2(S,Q),
    End_Hdg(T)=Q(sqrt(2)), dagger=id,

using its nondegenerate cup-product form restricted to T. These are the geometric application hypotheses, not a surface constructed or verified in this run.

For any rational basis e_i of T, let e^i be its q-dual basis: q(e^i,e_j)=delta_ij. Define

    tau_psi = sum_i e^i tensor psi(e_i)
        in T tensor T subset H^4(S x S,Q).

The correspondence convention is

    C_tau(x) = (pi_2)_*(tau cup pi_1^*x).

Then C_(tau_psi)(x)=sum_i q(e^i,x)*psi(e_i)=psi(x), so this is the unique tensor corresponding to psi under the nondegenerate pairing. Rational inverse-Gram coefficients make the class rational, and the formula is independent of basis because it represents a specified linear map.

The cup form pairs Hodge type(a,b) with type(2-a,2-b). Since psi preserves Hodge types, the associated tensor has total type(2,2). This proves tau_psi is a rational Hodge class under the stated geometric hypotheses. It does not exhibit an algebraic cycle for it, and no particular surface equation, verified endomorphism ring or numerical period is supplied here.

## 4. What the isometry route can and cannot license

For a projective K3 surface, the rational (1,1) classes in H^2 equal NS(S)_Q by the divisor theorem. Any Hodge isometry of full H^2 preserves this subspace and, by isometry, preserves its orthogonal complement T. Its restriction is a Hodge q-isometry of T, hence +id or -id under the field/adjoint assumptions.

Consequently every Q-linear combination of full H^2 Hodge-isometry correspondences restricts to a rational scalar on T. Products of divisor classes across S x S act as zero on T: the action involves the pairings q(x,D), which vanish by definition of T. Point/fundamental factor cycles also contribute zero to the H^2-to-H^2 action for degree reasons. The diagonal contributes id. Rational linear combinations and compositions of these named generators still act on T by a rational scalar.

Since psi is not such a scalar, tau_psi is not obtained by this declared fixed-surface generator route. Any isometry of full H^2 extending psi is impossible because its restriction would have to be a T-isometry. A chain consisting solely of Hodge isometries and returning to S likewise has isometric restriction; adding a genuinely new nonisometric algebraic correspondence is an additional input.

This is a no-go statement for a specifically named implication/generator family. It does not refute algebraicity of tau_psi, rule out other constructions or all consequences of a paper, or establish the global current status of the Hodge conjecture for K3 products. An algebraic similitude theorem or a different verified correspondence could bypass this route. The separate source audit must identify the precise theorem actually inspected; no theorem is adopted merely from its title.

## 5. Analytic controls that attack the hypotheses

### Known-good boundary: E=Q

If End_Hdg(T)=Q with identity adjoint, the isometry set is still {+1,-1}, but its Q-span equals the whole endomorphism field. Thus failure to span needs a proper field extension; the result is not a blanket obstruction for all K3 self-products.

### Nonidentity involution: Q(i)

In the field Q(i) with dagger given by conjugation, i^dagger*i=(-i)*i=1. Thus i is a unitary/isometric element outside {+1,-1}. For example multiplication by i on Q^2 is the matrix [[0,-1],[1,0]], whose transpose times itself is I for the standard rational form. This exact algebraic control shows that the identity-adjoint assumption cannot simply be omitted. It is not offered as a new geometric K3 realization.

### Zero divisors: Q x Q

In the product algebra Q x Q with identity involution, u=(1,-1) has u^2=1 but is neither (1,1) nor(-1,-1). The vectors (1,1) and(1,-1) span the whole two-dimensional algebra. Therefore the field/no-zero-divisor condition is essential to the factorization argument. Merely assuming a commutative algebra would be an invalid proof step.

All controls are exact analytic checks. No floating-point result, finite matrix grid or formal verification carries the universal claim.

## 6. Review and next obstruction

The last supported statement is the exact span/normalization implication and its conditional tensor/application crosswalk. The stronger geometric statement would assert algebraicity of tau_psi for an actual projective K3 with verified field/adjoint hypotheses. This run supplies neither that geometric instance nor a cycle proving or refuting the stronger statement.

Before further work, require either a precisely applicable primary theorem about the relevant nonisometric map, or an actual surface with verified endomorphism data and a cycle/construction obligation. A bounded source search failing to locate a newer theorem does not establish that the geometric problem is currently open. Do not repeat this closed field-factorization lemma, normalize by an irrational scalar, substitute a CM adjoint for the real one, or confuse the Hodge standard conjecture with the Hodge conjecture.

Internal same-actor review, standard imported Hodge/Kunneth/divisor facts, primary theorem-contract inspection and external proof assurance remain distinct. No new global theorem, novelty, general M05 solution/refutation, blind/external-human review, formal proof or performance gain is claimed.

## Audit batch002 adjudication

PASS_RESTRICTED for the abstract field/adjoint lemma; CONDITIONALLY_PROVED for the stated K3 tensor application under its explicit geometric hypotheses. A reading clarification separates real scalar multiplication from composition by the algebraic endomorphism psi/2. The sealed original is preserved locally. No actual K3 instance, nonalgebraicity, global theorem status or new Claude review is asserted. See [analytic audit](ANALYTIC_AUDIT.json) and [references](REFERENCES.md).

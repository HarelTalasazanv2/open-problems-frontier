# Exact algebra of two printed polynomials

**PROVED at restricted scope:** For p=17 and p=23, respectively, the following literal polynomials are irreducible over Q, and none of their complex roots equals pζ for any root of unity ζ:

f17(T)=T⁴+28T³+646T²+8092T+83521,

f23(T)=T⁴+52T³+1702T²+27508T+279841.

The coefficients were freshly transcribed from the complete published physical page18 image in interrupted Cycle177 and compared against the pinned Cycle176 transcription. Cycle178 rechecks those retained identities and executes the previously unrun instruments. This is not an on-time completion of Cycle177. The source's assertion that these are Frobenius factors is a separate, unreproduced dependency.

Both reductions modulo3 are

r(T)=T⁴+T³+T²+T+1.

A reducible monic quartic over a field has a monic factor of degree1 or2. The certificate tests all three monic linear polynomials and all nine monic quadratics over F3, with complete case membership and independently checked remainders. For the linear divisors T,T+1,T+2 the remainders are1,1,2. For quadratic divisors T²+bT+a they are:

| b | a=0 | a=1 | a=2 |
|---|---|---|---|
| 0 | T+1 | 1 | 2T |
| 1 | 1 | T+1 | 2T |
| 2 | T+1 | T+2 | T+2 |

Every remainder is nonzero, proving r irreducible over F3. A second check computes T^81−T≡0 modulo r and gcd(T⁹−T,r)=1. An alternative analytic explanation is (T−1)r=T⁵−1 and r(1)=2 in F3: any root has multiplicative order5, which cannot occur in a field of3 or9 elements. Thus an irreducible factor cannot have degree1 or2. This targets the enumeration mechanism by a different argument.

For completeness, the monic reduction-to-Q bridge is elementary. The product of primitive integer polynomials is primitive: reducing modulo any prime dividing every product coefficient would contradict the absence of zero divisors in the polynomial ring over that prime field. Consequently content is multiplicative. If a monic integer polynomial factors into monic rational polynomials G,H, write G=A/a and H=B/b with primitive integer A,B and their leading coefficients a,b. Then AB=abF; comparing contents gives |ab|=1. Therefore G,H have integer coefficients. Their reductions modulo3 preserve their positive degrees because they are monic. A rational factorization of either f_p would contradict the proved irreducibility of its reduction r. Both f_p are therefore irreducible over Q.

Normalize by

g_p(X)=p^(-4)f_p(pX).

Scaling the variable by the nonzero rational p preserves irreducibility. Exact coefficient calculations give

g17(X)=X⁴+(28/17)X³+(38/17)X²+(28/17)X+1,

g23(X)=X⁴+(52/23)X³+(74/23)X²+(52/23)X+1.

Suppose f_p(pζ)=0 and ζ has finite order m. Then g_p is the monic irreducible minimal polynomial of ζ over Q, so it divides X^m−1 in Q[X]. The same monic-factor argument above, applied to the monic integer polynomial X^m−1, forces g_p∈Z[X]. This contradicts its X³ coefficient, which is28/17 or52/23. Thus no such ζ exists. The argument covers every positive order m without enumerating any finite cutoff. It does not assume the polynomials are Weil polynomials or identify any cohomological operator.

The irreducibility hypothesis is essential to that shortcut. For example

h(T)=(T²+2T+4)(T²−5T+4)=T⁴−3T³−2T²−12T+16.

Its normalized polynomial 2^(-4)h(2X) has X³ coefficient−3/2, yet h has roots2ζ for primitive cubic roots of unity ζ. Thus the general inference from a nonintegral normalized coefficient alone is **FALSIFIED**. This counterexample is a control for an invalid shortcut, not a counterexample to the two claims proved above. Likewise, failure of a modulo3 irreducibility route does not prove reducibility over Q; the consumer preserves INCONCLUSIVE when that bridge is missing.

The actual consumer passes20 checks and rejects nine defective certificates, including a wrong nonzero remainder with a new checksum, missing/duplicate cases, wrong modulus, source-prime mismatch, wrong normalization and duplicated instance identity. Known reducible quartics without F3 roots challenge a root-only test. A correctly scaled cyclotomic quartic is not falsely excluded. These controls exercise the real parser and verdict path.

The producer uses ascending polynomial division and Fraction normalization. The checker uses separately written descending division, Frobenius/gcd calculations and integer-pair normalization. They share the same actor, source coefficients, anticipated mechanism and Python integer arithmetic. No blind, external human or formal verification is claimed. The executed code is copied unchanged from the frozen, unexecuted Cycle177 preparation; its C177 schema names are retained version identities.

**Claim ceiling:** exact algebra of these two supplied polynomials. Actual Frobenius-factor identification, cubic point counts, the16-class cohomological/Galois input, Tate/Artin–Tate, Picard rank, real multiplication, field action, tensor and global Hodge conclusions remain separate obligations. This reproduces a known source algebraic assertion; no novelty or performance gain is established.

## Audit batch002 reproduction

The [new exact checker](quartic_audit.py) freshly verifies the24divisor cases, both Fraction normalizations and the reducible shortcut canary; seven new malformed-certificate controls are rejected through its actual consumer. The new [certificate](QUARTIC_AUDIT.json) is separate from the historical20/nine checker tally above. Original source authors retain credit in [references](REFERENCES.md).

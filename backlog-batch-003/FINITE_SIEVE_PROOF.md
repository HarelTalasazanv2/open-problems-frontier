# Finite noncovering criterion: explicit kernel derivation

This is an internal derivation of the known finite noncovering part of the BBMST method, following its construction but making zero-mass and inactive branches explicit. Adjudication and computational-challenge results are separate. It is not a novel theorem, a formal proof or a reproduction of the paper's quantitative density theorem.

## Statement

Let U be any finite set of distinct integers greater than 1, and choose arbitrary integers a_d for d in U. The empty U case is immediate, so assume U is nonempty. Write Q=lcm(U)=product_i p_i^gamma_i, with distinct primes in increasing order, and fix real delta_i in [0,1/2]. Put Q_0=1 and Q_i=product_(j<=i) p_j^gamma_j, retaining the GLOBAL exponents gamma_j from Q. Let N_i be the moduli in U whose largest prime factor is p_i. For d in N_i write d=m_d p_i^j_d, with p_i not dividing m_d; then m_d divides Q_(i-1). Define

    nu(m)=product_(p_j divides m) 1/(1-delta_j), nu(1)=1;
    F_i=sum_(d in N_i) nu(m_d)/d;
    G_i=sum_((d,e) in N_i x N_i)
        nu(lcm(m_d,m_e))/(p_i^(j_d+j_e) lcm(m_d,m_e));
    b_i=F_i if delta_i=0, otherwise min(F_i,G_i/(4delta_i(1-delta_i)));
    beta=sum_i b_i.

The pair sum is ordered and includes diagonals. If beta<1, the residue classes a_d+dZ do not cover Z. All definitions and sums here are finite; there is no limiting or tail argument.

## 1. Conditional probability kernel, including empty events

Represent Z/Q_i by old residue x modulo Q_(i-1) and a new fibre of h=p_i^gamma_i points, using CRT. Let B_i be the union of the new residue classes with moduli in N_i. For EVERY old x, define alpha=k/h by counting the k new points that belong to B_i. Do not define alpha by dividing a mass by the prior mass of x. The count is meaningful even when that prior mass is zero.

For a prior probability distribution mu on the old residues, assign each point in this fibre mass mu(x) times the following conditional kernel K:

- If alpha<=delta_i, K=0 on covered points and K=1/[h(1-alpha)] on uncovered points.
- If alpha>delta_i, K=(alpha-delta_i)/[h alpha(1-delta_i)] on covered points and K=1/[h(1-delta_i)] on uncovered points.

In the first branch alpha<=delta_i<=1/2, so 1-alpha>0. In the second branch alpha>delta_i>=0, so alpha>0, and 1-delta_i>=1/2. An empty covered or uncovered part has no point at which an inappropriate expression is evaluated: alpha=0 uses the first branch, and alpha=1 uses the second branch with no uncovered point. Zero prior mass simply multiplies the well-defined kernel by zero. Thus there is no 0/0 case, including delta_i=0 or 1/2.

All weights are nonnegative. Summing the kernel in the first branch gives (1-alpha)/(1-alpha)=1. In the second it gives

    alpha*(alpha-delta_i)/(alpha*(1-delta_i))
      +(1-alpha)/(1-delta_i)=1.

Consequently the new distribution is a probability distribution and preserves every old-residue marginal. Iterating this construction from the single old residue modulo 1 defines P_i on Z/Q_i.

Relative to the uniform lift of the prior distribution, each point is multiplied by at most 1/(1-delta_i). For the first branch use 1/(1-alpha)<=1/(1-delta_i). For covered points in the second branch, the multiplier is also at most 1, because alpha-delta_i<=alpha*(1-delta_i). These assertions remain true at zero prior mass without taking a ratio there: they are direct inequalities between the constructed masses.

## 2. Congruence probability bound and distinct-prime weights

For every divisor m of Q_i and integer a,

    P_i(a modulo m)<=nu(m)/m.

Prove this by induction. At i=0 only m=1 occurs, and the claim is equality. If p_i does not divide m, the event depends only on the old residue, so marginal preservation gives the previous bound. Otherwise write m=f p_i^t, where f divides Q_(i-1) and 1<=t<=gamma_i. Under the uniform lift, the event has probability P_(i-1)(a modulo f)/p_i^t, since the new prime-power coordinate is uniform. The pointwise distortion inequality from section 1 therefore gives

    P_i(a modulo m)
      <=P_(i-1)(a modulo f)/[p_i^t(1-delta_i)]
      <=nu(f)/[f p_i^t(1-delta_i)]=nu(m)/m.

A prime contributes its distortion factor ONCE, independently of its exponent t. This explains nu's distinct-prime convention. The global exponents in Q_i are essential: Q_i need not equal the lcm of the moduli already exposed. For example U={2,12} has Q=12 and first prefix Q_1=4, although the first exposed modulus has lcm 2.

## 3. Actual moment bounds for arbitrary residues

For d=m_d p_i^j_d, the fraction of a fibre lying in a_d modulo d is p_i^(-j_d) when x equals a_d modulo m_d, and zero otherwise. This follows either from CRT or from invertibility of Q_(i-1) modulo p_i^j_d. A union bound on a fibre gives

    alpha_i(x)<=sum_(d in N_i) p_i^(-j_d) 1_[x=a_d modulo m_d].

Taking expectation under P_(i-1) and using section 2 yields M1_i=E[alpha_i]<=F_i. Squaring the nonnegative upper sum and expanding ALL ordered pairs yields a bound for M2_i=E[alpha_i^2]. Two cofactor congruences are either incompatible, giving an empty intersection, or specify one class modulo L=lcm(m_d,m_e). In the compatible case its prior probability is at most nu(L)/L by section 2. Hence M2_i<=G_i. The usual congruence fact follows because any two solutions differ by a multiple of both moduli, and compatibility is divisibility of the residue difference by their gcd; Bezout's identity supplies a solution when compatible.

The actual distributions can depend on the residue choices. No comparison of actual moments between different residue systems is used. The same upper sums nevertheless work for every choice of residues.

## 4. Bound the covered mass at each stage

The constructed covered mass in a fibre is

    mu(x)*max(alpha-delta_i,0)/(1-delta_i).

It is at most mu(x)*alpha, so P_i(B_i)<=M1_i<=F_i for every delta_i, including zero. For delta_i>0, the elementary inequality

    max(alpha-delta_i,0)<=alpha^2/(4delta_i)

follows from (alpha-2delta_i)^2>=0 when alpha>=delta_i, and is immediate otherwise. Thus P_i(B_i)<=M2_i/[4delta_i(1-delta_i)] as well. Combining gives P_i(B_i)<=b_i. The zero-delta branch uses only the first bound and never forms 0/0. At delta_i=1/2 the second denominator is exactly 1.

## 5. The final union cannot have full measure

Each B_i is determined by a residue modulo Q_i. Every later step preserves that marginal, so P_n(B_i)=P_i(B_i), viewing B_i as a lifted event modulo Q. Finite subadditivity gives

    P_n(union_i B_i)<=sum_i P_n(B_i)=sum_i P_i(B_i)<=beta<1.

The complement is nonempty in the finite cyclic group. Since every original modulus divides Q, any point in that complement represents an integer residue class missed by the progressions. Thus they do not cover Z. No uniform-density estimate or positivity of each individual P_n atom is required.

If every full-pool residue assignment fails to cover, every subset also fails: a covering subset could be extended by arbitrary classes for missing moduli and would produce a covering of the full pool. This is an independent logical alternative to sub-pool upper-sum monotonicity.

## Scope and assurance

The argument is algebraic and covers all finite U and all real delta_i in [0,1/2]. Small exact tests of a kernel implementation do not prove these quantifiers; the derivation above does. In the historical C147run the U877arithmetic was inherited. In this batch the vector and every F/G/stage/total are freshly recomputed by the separate exact checker; this does not retroactively change C147history. There is no claim of a full BBMST-paper/density-theorem replay, formal verification, external human review, blind reproduction, new cutoff, novelty or original global M09 resolution.

## Batch003audit

The complete kernel, marginal-preservation, congruence/moment and final-union derivations were rechecked. Zero prior mass, alpha0/1and delta0/half are explicit. The new [checker](sieve_check.py) tests216kernel cells/648prior vectors and the actual cross-term/distinct-prime/strict-threshold failure modes; these finite checks supplement the analytic argument. See [exact certificate](SIEVE_AUDIT.json) and [references](REFERENCES.md).

# Exact finite-period exclusions for shifted primes

**PROVED at restricted scope(C063):** no covering by pairwise distinct moduli p-1, primes p>=5, can have all moduli dividing360. **CERTIFIED_RANGE(C064/C065):** every finite such covering must have exact least common multiple L>=393120. These reproduce known partial claims and do not decide unrestricted existence or a current-best/least-unresolved bound.

For any finite class list a_m mod m, its common LCM period L covers all integers iff all residues0..L-1are covered. Each class occupies exactlyL/mpositions. Thus covering requires sum(1/m)>=1. For every L define D(L)={m>=4:m divides L and m+1is prime} and T(L)=sum_(m in D(L))L/m. Distinctness implies a cover with exact period L needs T(L)>=L. This is necessary only: overlaps may prevent covering even at larger capacity.

## The360boundary

The known reconstructed p>=3witness is

| a | m |
|---:|---:|
|0|2|
|1|4|
|1|6|
|7|10|
|11|12|
|9|18|
|21|30|
|15|36|
|3|40|
|15|60|
|39|72|
|39|180|

The [checker](period_bound_check_v2.py) verifies all360residues, exact LCM360, distinct shifted-prime moduli and canonical residues. Multiplicities are1..3. This is a reconstruction of the known boundary variant, not a p>=5answer or an assertion about Selfridge's exact original residues.

At p>=5the complete divisor pool is4,6,10,12,18,30,36,40,60,72,180. Its exact reciprocal sum is7/9and total capacity280out of360. Every subset/residue assignment therefore leaves at least80positions uncovered. Divisibility by360is the scope, not every numerical LCM<=360.

## Every period below393120

The new program generates prime flags by strided Eratosthenes and independently by a linear least-prime-factor sieve; they agree on every integer2..393120. It computes all T(L)by adding L/mat multiples of every admissible m, then recomputes each of393119positive capacities by complete divisor factorization. The sieve arguments are elementary: each composite has a prime factor at most its square root, and the linear sieve assigns its least prime factor. All comparisons use integers. L=1and odd L are included; equality T(L)=L is retained.

Exactly28periods survive density, first55440. Their complete identities, moduli and capacities are in the [certificate](period_certificate_v2.json). No target survivor count stops enumeration.

Fix a surviving L and surplus delta=T(L)/L-1. If1/m>delta, omission of m would leave total capacity below1, so m is forced. The exact inequality is strict: equality would not force it. All28survivors force4and6and have delta<1/12. If the selected4and6classes had the same parity, their intersection has density1/12, leaving total union at mostT(L)/L-1/12<1. Hence they have opposite parity and cover density5/12.

A remaining even modulus m contributes to the remaining holes at most the larger of A(m)and B(m), where A=1/mif4divides m, otherwise1/(2m), and B=1/mif6divides m, otherwise2/(3m). These follow from compatibility modulo gcd(m,4)or gcd(m,6)on the two parity sides. Independent maximization may overestimate jointly attainable coverage, which is safe for exclusion. Summing these bounds gives a capacity below7/12for23of the28periods, all listed in the certificate.

## Exhaustive forced-residue CRT step

For each remaining L, let F be its forced set and Q=lcm(F). Translate all residues by the selected modulus4residue, fixing a4=0without losing any system. Enumerate every canonical residue of every other forced modulus. Let U be the holes modulo Qand H=|U|. Their L-period holes number H*L/Q.

A remaining class modulo m is compatible with hole u exactly when u agrees with its residue modulo g=gcd(Q,m). Each compatible pair has L/lcm(Q,m)solutions modulo L. Thus its hole capacity is at most

(L/lcm(Q,m))*max_r #{u in U:u=r mod g}.

Summing per-modulus upper capacities remains safe even if their maximizing residues conflict. The program checks every Cartesian configuration, not just a maximum supplied by the certificate:

| L | F | Q | configurations | largest capacity-minus-holes |
|---:|---|---:|---:|---:|
|110880|4,6,10,12,16|240|11520|-5474|
|166320|4,6,10,12|60|720|-5943|
|221760|4,6,10,12|60|720|-7116|
|277200|4,6,10,12|60|720|-8793|
|332640|4,6,10,12|60|720|-6477|

All14400configurations have nonempty holes and strictly negative margins. Together with the complete density/parity partitions this proves L>=393120. Zero/nonnegative margins would be inconclusive, not existence witnesses. The exact program checks every saved case, identity, cardinality and arithmetic value.13targeted defects are rejected, including changed-cutoff p3promotion and missing/duplicate Cartesian cases. The analytic reductions supply the all-residues quantifier; finite primes/pools/configurations supply the finite certificate.

The new results match every historical CRTcase. Source credit is in [references](REFERENCES.md); the GitHub source was read inertly and not executed/copied. The original linked manuscript remains unread. No novelty, global solution, performance gain, blind/external review or formal verification follows.

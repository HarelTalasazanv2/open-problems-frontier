# Eight exact unit-fraction families

**PROVED at restricted scope(C158):** for every integer n>=2outside1and49mod120, the following fixed families give positive integers x,y,zwith4/n=1/x+1/y+1/z. Repetitions are allowed. The complement describes this method only; no global Erdős–Straus resolution or current-status claim is made.

| Condition | x | y | z |
|---|---|---|---|
|n=0mod2|n/2|n|n|
|n=0mod3|n/3|2n|2n|
|n=2mod3|(n+1)/3|n(n+1)/3|n|
|n=3mod4|(n+1)/4|n(n+1)/2|n(n+1)/2|
|n=5mod8|(n+3)/4|n(n+3)/8|n(n+3)/4|
|n=0mod5|2n/5|4n/5|4n|
|n=33mod40|(n+7)/4|n(n+7)/8|n(n+7)/20|
|n=17mod20|(n+3)/4|n(n+3)/10|n(n+3)/2|

Write n=mt+rfor each row, with t>=max(0,ceil((2-r)/m)). The [candidate](unit_fraction_candidate.json) gives the three integer polynomials in t. Every coefficient is a nonnegative integer, degree at most2, and each denominator is positive at that exact minimum. Monotonicity on t>=0therefore proves integrality/positivity for the full row, separately from the identity.

The [checker](unit_fraction_check.py) multiplies polynomial coefficients and verifies the zero polynomial

4XYZ-(mt+r)(XY+XZ+YZ)=0.

Its degree is at most6. This coefficient identity proves every t; three actual-domain rational evaluations per row are additional boundary controls, not the infinite proof. Historical seven-root-site checks remain a separate valid degree-bound argument. No reciprocal is evaluated at a zero denominator in residue-zero families.

All row moduli divide120. Every residue's full applicable-family set is checked, including overlaps, giving118covered classes and complement{1,49}. A separate hand deduction confirms it: after removing even n, multiples3and n=2mod3, only odd n=1mod3remain. Removing n=3mod4leaves n=1mod12; removing n=5mod8leaves n=1mod24, hence residues1,25,49,73,97mod120. The last three relevant families remove25,73,97. The classes1and49fail every displayed predicate, exactly as claimed.

They are not counterexamples. In particular4/49=1/14+1/196+1/196, checked exactly. More generally a solution at p scales to n=mpby multiplying all three denominators by m, so the eight direct classes need not exhaust all nsolved by these constructions.

16malformed-certificate controls are rejected through the actual consumer; an equivalent family/residue permutation passes. Missing/duplicate cases, wrong polynomial/domain/minimum, false global promotion and zero witness denominators cannot pass. [Exact audit](UNIT_FRACTION_AUDIT.json).

This is a known-style construction rechecked internally, not a new claimed solution. No2026solution preprint or withdrawn paper is adopted. Same exposed actor/model/Python backend, no blind/external human/formal review. See [references and credit](REFERENCES.md).

# Fixed U877noncovering certificate

**CERTIFIED_RANGE(C146):** for U877={p-1:5<=p<=877,p prime}, no choice of one residue per distinct modulus in any subset covers the integers. Hence any admissible unrestricted covering requires a prime exceeding877. No optimality, larger cutoff, current-best or unrestricted nonexistence claim is made.

The [exact candidate](sieve_candidate.json) has149moduli and47distinct prime keys. It uses delta2=delta3=0; delta5=40837/100000; delta7=3799/8000; delta11=241159/500000; delta13=59661/125000; delta17=2397/5000; every other key r>=19has delta_r=1/2. The prime keys are exactly the factors of lcm(U877), not all primes below877.

Apply the complete [finite criterion proof](FINITE_SIEVE_PROOF.md). Write d=m_d*p_i^jwithin its largest-prime group and nu(m)=product_(r divides m)1/(1-delta_r), over distinct primes. The checker evaluates

F_i=sum_d nu(m_d)/d,
G_i=sum_(d,e) nu(lcm(m_d,m_e))/(p_i^(j+k)*lcm(m_d,m_e)),

including every ordered pair/diagonal. Its alternative unordered-pair calculation uses multiplicity1on diagonals,2off diagonals and the equal term gcd(m_d,m_e)*nu(lcm(m_d,m_e))/(d*e). This equality follows from m_d*m_e=gcd*lcm. Each F/G/contribution agrees exactly, not just their total.

Set b_i=F_iwhen delta_i=0; otherwise min(F_i,G_i/[4delta_i(1-delta_i)]). All deltas lie in[0,1/2], so the finite proof handles every branch, including zero delta without0/0. The new exact result, all47rows and1187ordered terms are in [SIEVE_AUDIT.json](SIEVE_AUDIT.json). It proves

beta=sum_i b_i <199983/200000<1,
1-beta>17/200000.

There is no decimal rounding or approximate search in this proof path. The historical discovery floats were excluded from the released candidate. The complete analytic criterion then excludes every residue assignment for the full U877pool. If a subset covered, adding arbitrary residue classes for missing moduli would preserve covering and contradict that full-pool conclusion. Thus all subsets are excluded without comparing actual distorted distributions for different systems.

The [new checker](sieve_check.py) regenerates all149moduli by trial division and strided sieve, enforces47unique admissible rational keys, and recomputes all moment sums and the exact strict bound.12selected defects are rejected, including actual omitted cross terms and prime-exponent weighting. Exact beta=1is not certified; a genuine12period cover has beta185/144and is not falsely excluded. Kernel controls additionally preserve total prior mass and distortion at all selected endpoint/zero-prior cases.

The fresh rational outputs match every historical stage and the full beta/margin. Implementations share the actor, model, expected values and Python Fraction backend; notblind, external human or formal verification. Original BBMSTauthors and source contributors retain credit in [references](REFERENCES.md).

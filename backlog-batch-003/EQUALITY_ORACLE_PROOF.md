# One explicit equality oracle

**PROVED at the stated restricted/relative scope.** For the exact unary-clock/program oracle Adefined here, ordinaryEXP=P^A=NP^A. This single-oracle known theorem does not imply ordinaryP=NP, P!=NP, EXP^A=EXP, or a new barrier for a submitted proof.

## Exact coding and computational conventions

All strings are binary. Set `I(v)=1^v 0` for each nonnegative integer v. A valid deterministic one-tape program code d begins `I(s) I(g)`, with s>=3 states and g>=3 tape symbols. States are0,...,s-1; start0, accept1, reject2 are distinct. Symbols are0,...,g-1, with input symbols0/1 and blank2. For every pair (q,a), ordered lexicographically, with q not1 or2 and a any symbol, d contains exactly one row

`I(q_next) I(a_next) I(h)`, where q_next<s, a_next<g, h in{0,1}.

Here h=0 means one cell left, h=1 one cell right. No trailing bits are allowed. Thus transitions of nonhalting states are total and deterministic. The sets and rows are explicit, not succinctly described. Both header values are at most |d|; checking rows, ranges and absence of extra bits is polynomial in |d|. Any fixed machine of this model has a finite valid code. Relabelling its finite states/symbols is harmless; start/halting and input/blank conventions are fixed throughout this proof. The tape extends both ways, initially contains x with blanks elsewhere, and the head starts at its first symbol or a blank if x is empty.

An ordinary EXP language is decided by a fixed deterministic machine in at most `2^(c(n+1)^k)` steps for some fixed integers c,k>=1, for every input of length n. This is the union of deterministic `2^poly(n)` bounds. Multiplicative constants and finitely many exceptional input lengths can be absorbed by increasing c: a decider halts on every one of the finitely many exceptional inputs. Constants/exponents may depend on the language's one fixed machine, never on an individual input.

P^A and NP^A use one fixed finite oracle machine and one polynomial bound on every actual branch on inputs of length n. The query tape is initially blank, contains an explicitly written binary string at a query, and every ordinary write/move/choice costs a step. Only the membership answer costs one abstract step, regardless of the time an ordinary machine would spend deciding A. Nondeterministic branching is bounded by a fixed finite number. No advice, length-dependent program or free succinct expansion is permitted. Enlarging a valid polynomial clock to be at least n+1 changes none of these classes.

Fixed numbers of tapes do not change the ordinary P/EXP classes used here: a one-tape simulator can represent a fixed number of tracks with marked heads. At simulated time u its occupied span is O(n+u+1). A scan obtains the fixed tuple of head symbols, a return/update scan writes symbols and shifts head marks, and boundary extension adds only a constant number of cells. Thus U steps cost O((n+U+1)^2), up to constants of the fixed simulator. This supplies the polynomial overhead used below, rather than importing a black-box universal simulation bound. For a fixed machine's finite alphabet, track symbols are finite and hardcoded; the variable program inside A is separately decoded by the explicit universal routine below.

## Define A on every binary input

Parse an input z as

`enc(d,x,1^t) = 1^|d| 0 d 1^|x| 0 x 1^t`, with t>=0.

First count ones up to the first0, then read exactly that many d bits; next count ones up to the next delimiter0 and read exactly that many x bits. The remainder must consist entirely of ones and its length is t. Reject if a delimiter or required bit is missing, d is not a valid program, or the suffix contains a0. Length prefixes and the suffix therefore have unique meanings. For a valid encoding,

`N = |z| = 2|d| + 2|x| + t + 2`.

Let `T=2^t`. Put z in A exactly when the machine coded by d accepts x at time0 or within its first T transitions, including transition T. Reject on early rejecting halt or on expiration without accepting. In the selected coding the start state is distinct from both halting states, so initial acceptance never occurs for a valid d; the initial check remains an explicit harmless endpoint convention. When t=0, T=1, not0. Empty x and empty clock suffix are allowed. Malformed outer strings and malformed programs are rejected. This defines one total ordinary decidable language, the same A in every inclusion below.

## A has an ordinary `2^O(N)` decider

Syntax/program checks take polynomial time in N. To decide a valid query, keep the program, the current finite configuration, state/head marks, and a binary remaining-transition counter. Initializing the counter to `2^t` writes a1 followed by t zeros, requiring t+1 bits, not `2^t` bits. The algorithm then performs literal transitions until acceptance/rejection or counter exhaustion; no halting oracle or acceleration is used.

At most |x|+2T+1 cells need representation. State and symbol identifiers can be stored in padded blocks of O(N+1) bits because their descriptions occur in d. A complete configuration consequently uses O((N+T+1)(N+1)) bits. A constant number of work tapes suffice. For each transition, scan to its marked head, match the program row by finite scans/comparisons, and copy/update the configuration, extending by one blank cell if necessary. Program/header values, row matching and each comparison have polynomial cost in N; full configuration scans have polynomial cost in N+T. For example the direct scans can be bounded by a fixed multiple of `(N+T+2)^3` per transition. Parsing, T transitions and counter updates together are bounded by a fixed multiple of `(N+T+2)^4` on a fixed multitape machine. Its one-tape simulation is bounded by a fixed multiple of `(N+T+2)^8` by the preceding track argument. These are generous upper bounds, not a measured runtime improvement.

Since t<=N and T=2^t, `N+T+2 <= 2^(N+2)`. There is therefore one constant K, independent of d,x,t, such that the ordinary decider's time on every length-N input is at most `2^(K(N+1))`, enlarging K for finitely many small cases. Malformed inputs were already handled in polynomial time. In particular A is in ordinary EXP. The clock's unary length and the explicit program format are essential to this *particular bound*.

## Every ordinary EXP language is in P^A

Fix L in EXP and a deciding machine D with valid fixed code d and bound `2^(c(n+1)^k)` on every input, with c,k fixed integers as above. On input x of length n, compute `t(n)=c(n+1)^k`, write `enc(d,x,1^t(n))`, ask A, and return that bit.

The length `2|d|+2n+t(n)+2` is polynomial in n. Since c,k,d are fixed for L, the integer t and its unary representation are generated in polynomial time, including every output bit, for example by fixed nested loops or ordinary integer multiplication. This is one uniform many-one reduction, not an input-dependent exponent. Its A answer equals D's actual acceptance, because the clock covers all of D's computation, including acceptance at the last permitted step. Rejecting inputs halt and are not in A. For x empty, the same formula gives a finite valid clock and encoding.

Thus `EXP subseteq P^A`. The assertion does not say that the reduction is polynomial in the *bit length of c or k as additional input*: they are constants of the fixed language/program, as required by the EXP union definition. No unproved completeness theorem is needed; completeness at this reduction convention has just been established by construction.

## Every NP^A language is in ordinary EXP

Fix an NP^A decider M, a polynomial step bound p(n)>=n+1 for every actual branch, and finite branching bound b>=2. A binary choice block of fixed length `h=ceil(log_2 b)` can encode each possible choice at one step; out-of-range choices reject and unused blocks at deterministic steps are ignored. Enumerate every binary string of length `h p(n)`. This is at most `2^(h p(n))` choices. For each choice string simulate M from its initial configuration for at most p(n) original oracle-machine steps, stopping at halting. After early halt ignore the unused suffix.

Whenever a simulated branch actually issues a query y, compute its exact A answer using the ordinary decider already constructed, then resume that branch with that answer. Queries can depend on all earlier answers. They are not guessed, and answers from a different oracle are never substituted.

Query lengths are polynomially bounded because every bit must have been explicitly written from an initially blank query tape within p(n) steps. A safe bound is `|y| <= r(n)=2p(n)+n+2`; an ordinary one-bit-per-cell query model gives an even smaller bound. There are at most p(n) queries along any branch. The A-decider cost on each is at most `2^(K(r(n)+1))`. Copying/restoring configurations, maintaining the polynomial-length choice word and counters, and writing/reading these explicit queries incur polynomial overhead in the original work plus the A simulation. The fixed-tape/one-tape overhead is polynomial and can be absorbed into a larger constant K' and a fixed polynomial factor `(p(n)+n+2)^a`.

The complete deterministic simulation has an upper bound of the form

`C * 2^(h p(n)) * (p(n)+n+2)^a * 2^(K'(r(n)+1))`.

All constants and the polynomials p,r are fixed for M,A. The binary logarithm of this displayed expression is bounded by a fixed polynomial in n, so it is at most `2^(c'(n+1)^k')` for fixed integers c',k'>=1 after increasing them for small cases. The simulation is in ordinary EXP.

**Completeness of branch coverage:** for every actual accepting computation of M with oracle A, its finite nondeterministic choices extend to at least one enumerated length-hp(n) choice string. Recomputing each exact A answer inductively recreates the same configuration/query sequence, so that branch accepts in the simulation. Conversely, every simulated accepting path follows legal M transitions and the correct answers of A, so it is an actual accepting M^A path. Invalid choices are rejected. If none accepts, rejecting after the finite enumeration is correct. This is exhaustive coverage proved from the machine contract, not a finite sample of branches or oracle answers.

Hence `NP^A subseteq EXP`. A deterministic oracle machine is a special nondeterministic one, giving `P^A subseteq NP^A`. The inclusion cycle is now complete:

`EXP subseteq P^A subseteq NP^A subseteq EXP`.

Therefore `P^A = NP^A = EXP` for this one specified A.

## Restricted relativization consequence

The universal statement `for every binary oracle B, P^B != NP^B` is false, since substituting the constructed A contradicts its proved equality. Accordingly an ordinary separation argument cannot be correct *with a property guaranteeing that its separation conclusion persists for every oracle*, under these same oracle conventions. This is the precise scope of the obstruction established here. It does not classify any particular submitted proof as relativizing, ban every diagonal argument, establish a natural-proof barrier, or infer anything by removing A from a machine that uses it. No actual ordinary solver or separation candidate was supplied or adjudicated.

## Adversarial controls and verdicts

| Challenge | Decisive check and limit |
|---|---|
| Ambiguous encodings, missing delimiters, invalid rows or suffix0 | Exact parsing and total rejection rule, no implicit exponential state/table expansion. |
| Empty x, t=0, clock endpoint | Empty inputs parsed by zero length; t=0 allows one transition. A machine accepting precisely after two transitions is rejected at t=0 and accepted at t=1. A one-step accepting machine is accepted already at t=0. Literal transition tables with both nonhalting rows moving right supply these cases. |
| Unary clock replaced by binary t | For an m-bit t, t can be `2^(m-1)`, and the same literal simulation may require `2^(2^(m-1))` transitions. Thus the bound `2^O(m)` does not follow from this simulation. This invalidates that *unchanged cost argument*, not a proved classification of the changed oracle outside EXP. |
| Free exponentially long queries | Disallowed by the explicit-write model. The bound r(n) derives from charged query construction, not free input length. |
| Adaptive query dependence | The simulator recomputes the exact answer at each reached branch configuration; induction preserves all preceding answers. |
| Missed nondeterministic paths | Fixed h blocks and length-hp(n) enumeration cover every actual path, including early halts; invalid encodings reject. |
| Constants/exponents vary with x | Not permitted. d,c,k are fixed per EXP language; M,p,b are fixed per NP^A language. Their union is handled one fixed machine at a time. |
| Different A in the lower and upper inclusions | All steps use the same encoded language A with the same decider and endpoint rules. |
| EXP confused with EXP^A or P with P^A | The simulation/removal cost is charged to ordinary EXP; only the explicitly queried machine has unit-cost oracle answers. The proof makes no equality assertion after deleting the superscript. |
| Entire BGS/natural-proof source promoted | Only the equality-oracle existence component is independently derived; generic/separating-oracle and other imported theorems remain unverified here. |

**PASS AT CLAIM CEILING / PROVED:** explicit equality oracle, all inclusion/cost/membership obligations, and the exact all-oracle conclusion counterexample. **ARGUMENT_INVALID:** binary-clock substitution while keeping this unary-clock exponential simulation bound; no stronger changed-oracle theorem is refuted. **CERTIFIED_RANGE:** complete rereads8/10 and bounded fresh owner status. **INCONCLUSIVE/NOT_TESTED:** ordinary P-versus-NP, current complete barrier literature, natural proofs, generic/separating-oracle constructions, NP lower bounds, novelty and human/formal acceptance.


## Batch003adjudication

Complete analytic reconstruction checked for domain/quantifier/encoding alignment, endpoints, uniform fixed-program costs and every necessary implication. The concrete hand controls in the proof were re-derived; no finite experiment supplies its universal quantifiers. Shared exposed actor/expected argument, no independent human/formal review, novelty or ordinary PversusNPresult. Original context/source credit is in [references](REFERENCES.md).

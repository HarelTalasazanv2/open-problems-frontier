# Known circuit-uniformity qualification

**PROVED at the stated restricted/relative scope.** There exists a decidable binary language outside uniform Pwith constant functions/two noninput gates at every positive length. A uniform polynomial unary-length circuit generator would instead give a polynomial decider. No NPmembership or PversusNPseparation is claimed.

## Definitions

Inputs are finite strings over {0,1}; length is n. P means one ordinary deterministic finite-program Turing machine and one polynomial worst-case bound for all input lengths, with no oracle, advice or length-dependent program. We use polynomial bounds `c(n+1)^k`, with integer c>=1 and k>=0. This class of bounds covers every polynomial running-time bound, including small inputs, by increasing c or k.

For n>=1 a circuit has n labelled input nodes, one output, and an acyclic graph of gates from {AND, OR, NOT}; AND/OR have fan-in2. Size here counts non-input gates. Unused inputs are permitted. If input nodes and their labels are counted too, the two-gate circuits below have O(n) total nodes and a polynomial-length ordinary encoding. The empty input has its membership specified separately; it has no effect on P membership or the asymptotic circuit bound. No constant-input gates are assumed.

A family need not have any efficient generator unless that requirement is stated. Its existence quantifiers are: one sequence of finite circuits, each correct for every input of its own length. A polynomial-time generator below means one deterministic machine outputting an ordinary explicit circuit description on unary input `1^n`, within a fixed polynomial in n, not a binary succinct circuit, oracle or advice.

## Full construction and proof

Enumerate effectively all finite deterministic binary-input Turing-machine descriptions `D_0,D_1,...`. Such an enumeration can list finite strings in length/lexicographic order, parse each as a transition table, and replace an invalid description by a fixed rejecting machine. Every genuine finite machine occurs. Enumerate all triples `(i,c,k)` with i>=0, c>=1, k>=0 effectively, with each triple present at some positive index: for example order by i+c+k and then lexicographically. Each bounded-sum block is finite, every triple is reached after finitely many blocks, and the triple at any given positive index n is computable by finite enumeration. Denote it `(i_n,c_n,k_n)`.

Define the clocked Boolean function `F_n(w)` to be1 precisely when `D_(i_n)` accepts w within its first `c_n(|w|+1)^(k_n)` transitions, including acceptance at that final step. Otherwise it is0, whether the simulation rejected, halted without accepting, or exhausted its clock. Initial acceptance is checked before transitions. Each F_n is total and computable: compute a finite integer clock and iterate the finitely specified transition rule at most that many times. No halting oracle or claim of an efficient universal simulation is used. At each fixed n, its clocked computation is polynomial-time as a function of |w|; the enumeration as a whole has no fixed polynomial bound.

For n>=1 set `b_n = 1 - F_n(0^n)`. Let

`L = { w : |w|>=1 and b_(|w|)=1 }`, with the empty string rejected.

**Decidability.** On input w compute n, recover the nth triple, compute its finite integer clock, simulate that specified machine on `0^n` for the prescribed finite number of transitions, and flip its acceptance indicator. All stages terminate. Even if the enumerated machine happens to describe this decider, bounded step-by-step simulation is a finite computation; it does not recursively ask an unbounded acceptance question. This establishes ordinary decidability, with no asserted polynomial bound.

**Exclusion from P.** Suppose a polynomial-time machine D decides L. Choose its index i and integers c,k bounding D's actual running time on all inputs by `c(|w|+1)^k`. The triple (i,c,k) occurs at a positive index j. Because D halts within that clock, `F_j(0^j)` is exactly D's acceptance bit on `0^j`, which is exactly the membership bit of `0^j` in L. But that membership bit is `b_j = 1-F_j(0^j)` by construction. A bit cannot equal its complement. This contradiction covers every polynomial-time decider because every machine and every required integer clock pair is in the enumeration. It is not an enumeration of only the machines we happen to have tested.

**Circuit size.** At every positive length n, membership is the constant b_n across all `2^n` inputs. If b_n=0, output `x_1 AND (NOT x_1)`; if b_n=1, output `x_1 OR (NOT x_1)`. Each uses exactly two non-input gates and is correct on the entire length-n input domain, irrespective of the other n-1 input bits. The family is even computably generated from unary n by the terminating procedure for b_n, but not by any polynomial-time generator of correct polynomial-size circuits, as the next argument shows. Two possible diagrams do not tell a uniform algorithm which diagram belongs at each length.

## The sufficient uniformity condition, proved

Fix any language K and a deterministic generator G that, on `1^n`, outputs a correct explicit circuit C_n for K at length n in time at most a fixed polynomial g(n). Assume ordinary finite graph descriptions, legal labels and fan-in, and acyclicity, with size bounded by a fixed polynomial s(n). The generator's output length is itself at most its running time up to a fixed encoding constant; explicitly including labels and wires is therefore accounted for. No random access to an exponentially large succinct graph is assumed.

To decide K on w, compute n, write `1^n` in O(n) work, run G, label the n inputs by the bits of w, and evaluate the finite acyclic graph. One elementary evaluation procedure repeatedly scans the graph for a gate whose predecessors already have values and then stores its Boolean value. Acyclicity ensures that such a gate exists until all gates are evaluated: otherwise following an unevaluated predecessor forever in a finite graph would form a cycle. There are at most s(n) gate-evaluation rounds. Each round can use a polynomial amount of tape work in the full description length even with naive scans and binary wire labels. Thus total work is bounded by one fixed polynomial in n. The final output equals membership by correctness of C_n. The n=0 membership bit may be handled as a fixed finite exception, or by a generator convention allowing constant zero-input circuits.

Consequently K is in P. Applied to L, such a generator would contradict the preceding diagonal proof. The missing uniformity requirement is therefore essential even for a decidable language with only two gate choices per length. A binary-length generator is a different contract; we do not silently change the input-length scale.

## Adversarial adjudication

| Obligation/attack | Result and scope |
|---|---|
| Is L merely defined using undecidable halting? | No. Only finite clocked simulations occur; ordinary decidability is explicitly proved. |
| Does the enumeration omit a decider with a larger constant/exponent? | Every finite description and every positive integer c, nonnegative integer k is included. A chosen global polynomial bound occurs at some positive index. |
| Does rejecting or timing out spoil the diagonal? | F is a total acceptance indicator. At the selected decider/valid-clock index there is no timeout; the contradiction uses that index only. |
| Small n, empty input, initial/final-step acceptance? | n>=1 supplies x_1; epsilon rejected separately; bounded acceptance includes time0 and the clock endpoint. |
| Do two gates work on all inputs rather than samples? | Boolean identities prove constant output for both values of x_1 and every setting of unused inputs. |
| Are n input nodes hidden in the gate count? | Yes, explicitly excluded by the stated non-input-gate convention; including them gives O(n), still polynomial. |
| Is the family noncomputable? | No, a terminating generator exists. The obstruction is a *polynomial-time* generator of a correct polynomial-size family. |
| Could a different efficient family evade the negative result? | No. Any such generator would decide L by the generic DAG-evaluation argument. |
| Does the result give an NP language outside P? | No NP membership was established. This is a model/uniformity counterexample, not P-versus-NP separation. |
| Does this disprove circuit lower bounds or the source implication? | No. P=>small circuits survives. An unrestricted superpolynomial circuit lower bound for an NP language would still be sufficient, not supplied here. |
| Were oracle/natural-proof/derandomization barriers verified? | No. They remain named source imports, separate from this elementary construction. |

**PROVED:** the exact decidable-language/two-gate construction and uniform-generator converse. **FALSIFIED:** the universal shortcut that existence of polynomial-size circuits at every length implies membership in uniform P. **CERTIFIED_RANGE:** direct source inspection6–10 and model/import identification. **INCONCLUSIVE/NOT_TESTED:** actual NP-complete polynomial solver, NP circuit lower bound, full barrier theorems, current literature/novelty, formal or independent human verification, and global M04 resolution.


## Batch003adjudication

Complete analytic reconstruction checked for domain/quantifier/encoding alignment, endpoints, uniform fixed-program costs and every necessary implication. The concrete hand controls in the proof were re-derived; no finite experiment supplies its universal quantifiers. Shared exposed actor/expected argument, no independent human/formal review, novelty or ordinary PversusNPresult. Original context/source credit is in [references](REFERENCES.md).

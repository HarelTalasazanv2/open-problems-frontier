# Known decision-to-search reduction

**PROVED at the stated restricted/relative scope.** For each fixed polynomially bounded polynomial-time verifier relation, a correct decision oracle and a fixed polynomial prefix-language reduction give a uniform search algorithm with at most p(n)+1queries. Ordinary polynomial search remains conditional on an ordinary polynomial decider.

## 2. Exact interface, encodings and quantifiers

Work with binary strings. Fix a deterministic polynomial-time Boolean verifier R(x,y) and an explicit nonnegative integer-valued bound p(n), polynomially bounded and evaluable in polynomial time. For example, one may take a fixed nonnegative integer polynomial; more generally assume p(n)<=C(n+1)^b for fixed C,b. The task on input x is to output some y with |y|<=p(|x|) and R(x,y), or a distinct failure symbol bottom if no such y exists. Bottom is not the empty string or a bit string. Empty witnesses are permitted.

The verifier, bound and reduction algorithms are fixed once for this search problem. The resulting algorithm and polynomial bound are uniform over **all inputs x**. No single exponent or uniform compiler across all verifier descriptions is claimed. This explicit p formulation is self-contained; it does not infer conventions for the source's n^k notation at n=0.

Use the unambiguous pair encoding

`enc(x,s) = 1^|x| 0 x s`, with length `2|x|+1+|s|`.

Decode by finding the first0, counting the preceding1s as n, reading the next n bits as x and the remaining bits as s. Reject a string with no0 or too few subsequent bits. Define the prefix language

`E_R,p = {enc(x,s): exists y, |y|<=p(|x|), s is a prefix of y, R(x,y)}`.

Malformed encodings and prefixes longer than the bound are NO instances. The encoding of two empty strings is the one-bit string0; it is well-defined.

Let A be a fixed language with a **correct decision oracle**, and let f be a fixed total polynomial-time many-one reduction from E_R,p to A:

`z in E_R,p iff f(z) in A` for every binary z.                (1)

The theorem proves a polynomial-time A-oracle search algorithm from this interface. If A is NP-complete under the definition on source4, existence of such an f follows once E_R,p is shown to be in NP. No particular NP-completeness theorem or polynomial-time ordinary decider for A is thereby proved. In particular, applying the result to SAT using its NP-completeness requires that known theorem as an input; its full proof was not reproduced111.

## 3. Prefix existence is an NP language

A verifier for E_R,p first parses z as enc(x,s), computes p(|x|), rejects an overlong prefix, then uses y as its certificate. It accepts exactly when |y|<=p(|x|), s is a prefix of y, and R(x,y) holds. Every check is deterministic and polynomial in |z|+|y|. Also |x|<=|z| and the certificate length is at most C(|z|+1)^b. The relation is therefore polynomial-time with a polynomial certificate bound, proving E_R,p belongs to NP by definition.

The field of mathematical choice here is ordinary finite strings; no numerical approximation or infinite search is hidden. This proof does not use Cook-Levin, relativization, a SAT-solving algorithm or an external circuit theorem. NP-completeness of A is used only through its quantified definition to choose one fixed reduction f for this fixed prefix language.

## 4. Search algorithm and proof of correctness

Let n=|x| and P=p(n). A prefix-existence query is implemented by asking the A oracle about f(enc(x,s)).

1. Query the empty prefix. If the answer is NO, output bottom.
2. Otherwise set s to the empty string. At each iteration, first evaluate R(x,s). If it is true, output s.
3. If it is false, query the prefix s0. Choose s0 if that answer is YES; otherwise choose s1. Repeat, making at most P extensions.

The invariant after initialization and every extension is

`|s|<=P and some accepted bounded witness extends s`.         (2)

Initialization is precisely the empty-prefix oracle query. If R(x,s) is false, an accepted extending witness cannot equal s. It therefore has a next bit,0 or1. If some witness extends s0, choosing0 preserves(2). Otherwise, the existing witness must extend s1, so choosing1 preserves(2) without a second query. This reasoning uses both the correct oracle and the reduction equivalence(1).

Every extension increases length by1. If |s|=P, invariant(2) forces the extending witness to equal s, so R(x,s) must be true. Thus the false-verifier branch at length P is unreachable under the stated interface. The process returns a valid witness after at most P extensions. If there is no bounded witness, the first query correctly returns bottom. If P=0, the only possible witness is empty: the initial query and verifier test cover both outcomes. Empty input x is also allowed by the encoding and p(0).

The early verifier test is necessary for this general relation. Padding an accepted short witness to length P need not preserve R. The proof does not assume fixed-length certificates or require a special padding convention.

## 5. Query count, query length and ordinary running time

There is one initial oracle call and at most one per extension, hence **at most P+1 calls**. All queried prefixes have length<=P, so their encoded lengths are at most2n+1+P. Let q_f be a fixed nondecreasing polynomial upper bound on both the running time and output length of f. Such an output-length bound follows in the ordinary Turing model because output symbols must be written; enlarge the polynomial for constants if necessary. Every A-query length is at most

`q_f(2n+1+P)`.                                                (3)

Let q_R bound verifier time as a polynomial in combined pair size. Apart from polynomial-time evaluation of p, nonoracle work is bounded by a fixed polynomial of the form

`O((P+1)[q_R(c(n+P+1)) + q_f(2n+1+P) + n+P+1])`,             (4)

where c accounts for a fixed conventional verifier-pair encoding. This includes prefix/encoding construction, query writing and output, not just abstract unit-cost oracle replies. Since P is polynomially bounded in n, (3)-(4) are polynomial in n+1. No input-dependent exponent or bounded-length experiment substitutes for that uniform argument.

If an actual deterministic decider D for A has fixed polynomial running bound T_D, replacing oracle calls adds at most

`(P+1) T_D(q_f(2n+1+P))`.

That gives a conditional ordinary polynomial-time search algorithm. No such decider is supplied or certified here. Separately, if P=NP were assumed, E_R,p itself would belong to P, and the same construction with its decider would prove polynomial-time search for every fixed NP verifier relation. This establishes the **logical conditional**, not its unproved global premise.

## 6. Exact adversarial controls and their proper scope

| Challenge | Exact finding |
|---|---|
| Force every witness to length P | Let p=1 and R(x,y) hold only for empty y. The initial prefix is extendible and empty is valid; no length1 witness exists. Fixed-length padding/search is **FALSIFIED for this relation**. The actual algorithm returns empty. |
| Replace prefix membership by original input-language membership | Let p=1 and R(x,y) hold exactly when y=1. Its input decision language L is all binary strings, but E_R,p(enc(x,0)) is false. Simply querying L on an encoded prefix gives the wrong answer. That **specific predicate-identification shortcut is FALSIFIED**. |
| Infer impossibility of every search reduction to an arbitrary NP language from that example | Not established. R is also available to a search algorithm, and some verifiers have easy witnesses. No unconditional separation of arbitrary NP search from its own decision language is claimed. NP-completeness in the source supplies the justified reduction of the distinct prefix language. |
| No accepted witness | R always false makes the first query NO and returns bottom after one oracle call. |
| Zero witness bound, empty input, multiple witnesses | Covered by the invariant and explicit terminal tests; any valid witness suffices. No shortest/unique-witness property is claimed. |
| Malformed pair or overlong prefix | Rejected in E_R,p's verifier; the searcher's constructed encodings are always valid and within P. |
| Incorrect oracle or unverified reduction | Guarantees are withheld: (1) and correct membership are actual hypotheses, not inferred from examples or low residuals. An executable candidate would need a separate contract and verification. |

Uniformity has an additional exact control. For the **specific running-time function** T(n)=2^n, every finite interval0<=n<=N admits a polynomial upper bound with constant2^N. No one fixed C,k bounds T(n) by C(n+1)^k for all n. For integer k>=0 and n>=2(k+1),

`2^n >= binom(n,k+1) >= (n/2)^(k+1)/(k+1)!`.

Dividing by (n+1)^k<=(2n)^k gives a lower bound proportional to n, which is unbounded. This **falsifies finite-window-to-uniform-time inference for that machine/time function**. It is not a lower bound for SAT or a proof that no other algorithm is polynomial.

These are exact mathematical attacks, not numerical tests or finite samples offered as a universal proof. The proof is the explicit invariant, encoding and fixed-polynomial composition.


## Batch003adjudication

Complete analytic reconstruction checked for domain/quantifier/encoding alignment, endpoints, uniform fixed-program costs and every necessary implication. The concrete hand controls in the proof were re-derived; no finite experiment supplies its universal quantifiers. Shared exposed actor/expected argument, no independent human/formal review, novelty or ordinary PversusNPresult. Original context/source credit is in [references](REFERENCES.md).

# Audited historical reading edition

**Current audited claim:** PROVED: For E:y^2+y=x^3+x^2-2x, L(E,1)=0 in arithmetic normalization.

**Claim ceiling:** Known fixed curve under standard modularity/reduction/Hecke-Mellin theorems; no rank, Sha or general BSD result.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Exact central vanishing for the fixed curve 389.a1

**PROVED internally, known-result reproduction:** for

\[
 E/\mathbb Q:\quad y^2+y=x^3+x^2-2x,
 \qquad L(E,1)=0
\]

in arithmetic normalization. The new evidence is a rational Manin-symbol identity, checked in every free coordinate by a separate certificate consumer, followed by an explicit conductor/Frobenius/modularity/Mellin bridge. Standard modularity and reduction theorems are imported, not newly proved or formally verified here. The zero was already known from the database; there is no novelty, rank-two, Sha or general BSD claim. External human review remains outstanding.

## 1. Scope, readiness and changed mechanism

The frozen attempt (historical local record; not distributed here) follows the selected059central-zero obligation. System Python3.9.6 and the bundled runtime have no Sage, PARI or SymPy. A bounded standard-library Fraction implementation was therefore used; no installation or downloaded/source-estate code execution occurred. The chosen presentation has only390generators and780declared relations, so it fits the finite budget.

The old packet proposed identifying one rational newform component explicitly. The frozen060strategy instead proves central vanishing for **every** weight-two level389 cusp eigenform with T2 eigenvalue−2. The fixed curve is put inside this class by its conductor and its directly counted a2. Thus no claim that a2 uniquely identifies a newform, no all-zero eigenvector, no unverified database projection and no basis-isolation shortcut is needed. The label389.2.a.a is historical orientation, not an input to the deciding computation.

## 2. Exact finite object

Let F be the free rational vector space on P1(F389), in this exact order:

    x0=(0:1); x_(t+1)=(1:t), 0<=t<389.

There are390distinct classes: normalize a nonzero pair(c,d) by c if c!=0; if c=0 its class is(0:1). Trial division by every prime at most19 establishes389prime. No pair(0,0) is admitted.

For each x=(c:d), include both valid weight-two Manin relations

    R_S(x)=x+(d:-c),
    R_U(x)=x+(d:-c-d)+(-c-d:c).

The last summand is projectively(c+d:-c), giving exactly Cremona2.2.6–2.2.7. These are oriented edge-reversal and triangle relations; integrating a level389cusp differential annihilates them. Relation IDs are2j and2j+1 for symbolj, all780included. Only their validity is necessary for the witness implication. Gaussian relation rank325and quotient dimension65 are diagnostics; the proof does not infer a complete modular-form decomposition or a rank theorem from those counts. We use the full relative-symbol presentation, not a claim that the central symbol is zero in that full module.

Right action is(c,d)[a,b;c',d']=(ac+c'd,bc+d'd). With

    H2 = { [1,0;0,2], [2,0;0,1], [2,1;0,1], [1,0;1,2] },

let T act on each generator by the sum of its four normalized images. This is the weight-two Heilbronn–Cremona T2 action, with no extra factor1/2. The exact matrices and action convention are explicitly given in the [official Sage documentation](https://doc.sagemath.org/html/en/reference/modsym/sage/modular/modsym/heilbronn.html). None of Sage's source code is executed.

The generator x0 maps to the oriented cusp symbol{0,infinity}: the determinant-one identity matrix has bottom row(0,1). Put e=x0.

## 3. Decisive certificate and independent consumption

The discovery certificate (historical local record; not distributed here) contains58nonzero rational coefficients w and312nonzero relation coefficients r satisfying the exact identity in the **free**390-dimensional space

    e = (T+2I)w + sum_(j=0)^779 r_j R_j.                 (1)

All denominators divide290. The integer witness (historical local record; not distributed here) records equivalently

    290 e = (T+2I)W + sum V_j R_j,

with integer W=290w,V=290r. It is a lossless derivative of the same certificate, not independent evidence.

The OPF discovery program uses sparse Fraction Gaussian elimination. The separately written consumer (historical local record; not distributed here) imports neither the solver nor its row-reduction routines. It regenerates every projective symbol, every relation and every operator column, validates the exact ordered membership, and checks(1) with dense exact rational arithmetic at all390coordinates. It ignores the producer's rank and timing diagnostics. Zero/duplicate/malformed rational data are rejected. The discovery program uses extended-Euclidean inversion while the consumer uses Fermat inversion; actor, definitions, source convention, arithmetic library and expected result remain shared.

After discovery, the confirmatory contract (historical local record; not distributed here) froze the actual-CLI checks. The final control receipt (historical local record; not distributed here) contains2healthy and14isolated rejection cases. The wrong-eigenvalue and zero-target additions were made before the final confirmation; the earlier14-case successful receipt remains separately preserved. The healthy level389image and level11nonimage both pass. Wrong coefficient, all-zero w, wrong a2, zero/reversed target, wrong expected level, absent/duplicated/changed relation, changed Hecke matrix, zero denominator, a forged level11image, zero dual and duplicate w entry are rejected with nonzero process exits. These are selected failure classes, not exhaustive fault coverage.

For the level11control, the saved dual functional annihilates all24Manin relations and all12columns of(T2+2I), but pairs to−1/5with its central target. The consumer checks those equations directly. It therefore proves that this central target is **not** in the indicated image, without appealing to a numerical L-value or assuming that every central symbol vanishes. This is a negative finite-module control, not an imported rank assertion.

## 4. Hecke-convention challenge

The four raw right-action matrices and the three usual upper-triangular cusp transformations must not be confused. A separate OPF program lifts each symbol to a determinant-one matrix, acts on its two cusps with

    [2,0;0,1], [1,0;0,2], [1,1;0,2],

and independently decomposes the resulting rational cusp paths with continued fractions. Each edge is checked unimodular and oriented as g{0,infinity}. For **all390symbols**, the resulting operator column agrees with the four-matrix construction modulo valid Manin relations; receipt (historical local record; not distributed here). This targets a common-mode operator/convention error. It shares the exact relation reduction with discovery and is exposed internal reproduction, not blind, external or formal review.

The [primary Cremona chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf),2.2–2.4, supplies the pair/coset action, relation and cusp conversion definitions and the direct Hecke action. Physical pages10–15 were extended substantive reading; physical11and13were visually inspected because extraction corrupts some mathematical glyphs. Physical24was visually reinspected for2.8.7. Entire-chapter reading is not claimed.

## 5. All relevant eigenforms have exact central zero

Let f be any weight-two cusp form for Gamma0(389) with T2 f=−2f. Define the cusp-differential pairing

    ell_f({a,b})=2*pi*i*integral_a^b f(z) dz.

Cuspidality makes the integrals converge at the cusps. The edge/triangle and Gamma0relations imply ell_f(R_j)=0. Change of variables in the integral gives Hecke equivariance

    ell_f(Tv)=ell_(T2f)(v)=−2 ell_f(v).

This normalization is checked in Cremona2.4,physical13. Applying ell_f to(1) now gives ell_f(e)=0. Cremona2.8.7,physical24, gives exactly

    L(f,1)=−ell_f({0,infinity})=0.                    (2)

No approximate special value, root-number inference, derivative value, period estimate or eigenvector normalization decides the zero. The global sign in the Mellin identity is retained, although it cannot affect an exact zero.

## 6. Transfer to the actual curve without trusting a database rank

For a-invariants[0,1,1,−2,0], elementary Weierstrass arithmetic gives

    b2=4,b4=−4,b6=1,b8=−3,c4=112,Delta=389.

The curve is nonsingular. It has good reduction away from389 because Delta is a unit there. Discriminant valuations of isomorphic integral Weierstrass models differ by multiples of12; a valuation1cannot be reduced to a smaller nonnegative valuation. Hence this equation is locally minimal at389(and at every other prime, where its valuation is0).

For an explicit multiplicative-reduction check at389, put Y=2y+1. The equation becomes

    Y^2=4x^3+4x^2−8x+1.

The unique repeated root of the cubic modulo389is x=299. At x=299+h the constant and linear terms vanish and the equation is

    Y^2=4h^3+91h^2 (mod389).

Since91!=0this singularity is an ordinary node. Thus reduction at389is multiplicative. The standard conductor rule gives exponent1at a multiplicative prime and0at good primes; consequently N_E=389. These reduction and conductor facts are standard imported theory. The selected author lecture source explicitly records the nodal reduction model and conductor exponents; no local Tate-algorithm library is used.

Over F2the four affine points are(0,0),(0,1),(1,0),(1,1), with one point at infinity. Thus #E(F2)=5 and

    a2(E)=2+1−5=−2.

Exact arithmetic record (historical local record; not distributed here).

By the standard modularity theorem for elliptic curves over Q, there is a normalized weight-two cusp eigenform f_E of level N_E with L(f_E,s)=L(E,s) and T2f_E=a2(E)f_E. This is a named STANDARD_THEOREM, not a new project proof. [Sutherland's author lecture24](https://math.mit.edu/classes/18.783/2023/LectureSlides24.pdf),physical2and19,states the theorem and level convention; physical14–15/17–18supply the Frobenius/reduction/conductor conventions. These selected pages were read as text, not the entire23-page lecture. The unavailable original Annals endpoint is recorded as a retrieval failure, not a missing modularity theorem or evidence of global source unavailability.

The computed conductor and Frobenius coefficient put this nonzero normalized f_E inside the class covered by(2). Therefore **L(E,1)=0**. No matching of a database integer to zero, no claim that a2alone singles out the named newform, and no BSD assumption enters this inference.

## 7. Adjudication, usefulness and remaining dependencies

- Finite identity(1): exact computer-assisted **PROVED_INTERNAL**, with separately consumed rational witness and stated software/source trust boundary.
- Transfer to this fixed E: **PROVED_INTERNAL** under established modularity and reduction theory, with an explicit case-specific conductor/a2bridge. These standard theorems are imported; human review/formalization not performed.
- The genus/dimension and combined-rank diagnostics are not needed for the vanishing inference.
- L''(E,1) nonzero enclosure: **NOT_TESTED**. Analytic rank exactly2therefore remains unreproduced by this cycle.
- Algebraic rank/independence/descent/saturation: **NOT_TESTED**. Analytic Sha1retains the059approximate/rounded qualification.
- General BSD: **OPEN** on the bounded current Clay check. Novelty/priority not claimed.

The uncertainty removed is the first actual local certificate gap in059. The witness is small enough for exact ordinary-Python replay, so this avoids an installation dependency and a nominal green database assertion. No speed or research-productivity comparison was conducted. The level11dual makes a universal-zero bug detectable. The generic annihilator/image route can transfer to other finite modular-symbol certificates, but this example does not establish it for other levels/eigenvalues.

**Next:** freeze a rigorous nonzero second-derivative enclosure for this curve, after checking completion/root-sign conventions and a feasible complete tail/rounding model. This serves the059analytic-order criterion. Do not rerun the unchanged zero witness or infer rank2from its success. The source-known algebraic rank remains a separate later reproduction task.

## 8. Reproduction, corpus and authority

From the project root:

    python3 -B artifacts/m02_central_zero_cycle060/verify.py artifacts/m02_central_zero_cycle060/certificate_389_discovery.json 389
    python3 -B artifacts/m02_central_zero_cycle060/verify.py artifacts/m02_central_zero_cycle060/control_11_nonimage.json 11
    python3 -B artifacts/m02_central_zero_cycle060/confirm.py
    python3 -B artifacts/m02_central_zero_cycle060/direct_hecke_check.py

The consumer is read-only. The last two commands regenerate only their own OPF result records; discovery regeneration uses discover.py with an explicit new output path. Python3.9.6 ran the deciding exact arithmetic; Fraction, integer arithmetic and stdlibprocess controls are the only dependencies. Bundled Python3.12andpypdfwere used only for source extraction. No installed algebra system or external source program ran.

Six public source-inspection rows separate extended book reading, reinspection, two official documentation sections, a newly inspected author lecture and the routine Clay status poll. They are not six independent mathematical reviews. **Zero new volume paths**; pass036retains141paths131full/10partial132recorded hashes,105/428327frozen candidates+33noncandidates+3post-censusunclassified. Underlying-source and volume-content denominators stayUNKNOWN.

Preflight also read the newly integrated175th side-audit event. Its uploaded M07defects are distinguished from the correct native040coefficients. It does not change this main selection or authorize persistent skill installation or cross-project messages. No agents/threads,source-estate execution/writes,external messages/uploads/publication,installation/purchases/accounts/app/schedule/notification changes or Governor/Engine action occurred.

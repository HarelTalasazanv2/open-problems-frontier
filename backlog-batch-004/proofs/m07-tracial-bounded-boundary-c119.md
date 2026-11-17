# Audited historical reading edition

**Current audited claim:** PROVED: The same infimum identity holds for all bounded positive pairs with the explicit canonical trace-truncation relative entropy and extended production.

**Claim ceiling:** Bounded finite-tracial class and exact production convention; no unrestricted L1 or arbitrary-generator statement.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Bounded two-point tracial boundary and canonical extended entropy

**PROVED internally at the exact bounded-input scope below.** The positive-gap comparison from118 extends to every bounded positive pair in every finite von Neumann algebra with faithful normal tracial state, including unequal supports, diffuse spectrum reaching zero and infinite production. The canonical trace-truncation entropy is identified with a positive spectral-kernel integral before taking the regularization limit. No matrix-exhaustion or same-support finiteness assumption is used.

This closes the selected bounded two-point domain leaf. It does not prove a theorem for unbounded affiliated L1 inputs, semifinite/infinite traces, products, reset chains with three or more values, general classical chains, current worldwide status, novelty or external human/formal acceptance. The draft, prior internal review and expected strategy were exposed; this is same-actor/model/source verification, not blind reproduction or human/formal review.

## Exact statement and definitions

Let(Q,tau) be a finite von Neumann algebra with faithful normal tracial state tau(1)=1. Take bounded A,B in Q, A,B>=0; fix0<p<1,q=1-p and c>0. Set phi(0)=0,phi(x)=x ln x for x>0, M=pA+qB and

\[
 H_p(A,B)=p\tau\phi(A)+q\tau\phi(B)-\tau\phi(M).
\]

All three terms are finite because phi is continuous on bounded nonnegative intervals. Define log_+(b)=max(ln b,0) for b>0, log_+(0)=0 and log_-(b)=max(-ln b,0), log_-(0)=+infinity. For n>=1 put h_n(b)=min(log_-(b),n), including h_n(0)=n. Bounded Borel calculus in Q defines h_n(B). Set

\[
 N(A,B)=\lim_{n\to\infty}\tau[A^{1/2}h_n(B)A^{1/2}]\in[0,\infty],
\]
\[
 D_\tau(A\Vert B)=\tau\phi(A)-\tau[A^{1/2}\log_+(B)A^{1/2}]
                 +N(A,B)-\tau A+\tau B. \tag{1}
\]

The limit in N exists by monotonicity and positivity. Every other term in(1) is finite; log_+(B) is bounded. Thus(1) has no infinity-minus-infinity. Nonnegativity will be proved, not assumed. This is the specified generalized, unnormalized tracial relative entropy, with its unbounded negative logarithm interpreted by positive-form truncations. Products with an unbounded logarithm are never taken as an unspecified trace of an indefinite operator.

Define

\[
 J_{p,\mathrm{ext}}(A,B)=pq[D_\tau(A\Vert B)+D_\tau(B\Vert A)]\in[0,\infty]. \tag{2}
\]

Use exactly the scalar positive-pair infimum from116/118,

\[
 a_p=\inf_{r>0,r\ne1}\frac{J_p(r,1)}{2H_p(r,1)}.
\]

It is finite and nonnegative: positive scalar pairs have positive H and nonnegative finite J, and any one r!=1 gives a finite upper bound. No numerical scalar bracket enters. The theorem is

\[
 J_{p,\mathrm{ext}}(A,B)\ge2a_pH_p(A,B). \tag{3}
\]

The infimum of J_ext/(2H) over H>0 and this entire bounded finite-tracial auxiliary class equals a_p. For L=c(I-E_pi), E_pi(A,B)=(M,M), its optimal constant **on this specified bounded class with extended production(2)** is c a_p in the native2alphaD convention.

## Foundations and dependency ceiling

The [118 direct proof](m07-tracial-uniformly-invertible-c118.md) establishes(3) for bounded pairs with positive lower bounds, on every admitted Q. Its Hilbert-space left/right construction, compact joint calculus and coherent spectral-mixture comparison were reread here in full. It is the only problem-specific theorem input. No tensorization, numerical certificate, external Definition3.1 identification or global CMLSI theorem is imported from the review.

Standard mathematical foundations used here in their stated forms are: bounded self-adjoint spectral/Borel calculus; the joint spectral measure for a commuting bounded self-adjoint pair; positive vector measures; normal trace continuity on bounded increasing positive nets; and monotone/dominated convergence for finite positive scalar measures. These are foundational inputs, not newly formalized kernel proofs. The hypotheses and the exact trace/measure identification needed in this application are checked next. There is no separability or finite-spectrum assumption.

## A positive joint vector measure with noncommuting A,B

On H=L2(Q,tau), inner product <Y,Z>=tau(Y*Z), let e=1. Bounded left/right operators L_A Y=AY and R_B Y=YB are positive self-adjoint and commute, although A and B need not commute in Q. Indeed their norm bounds, positivity and self-adjointness follow on the dense subspace Q from trace cyclicity and extend by boundedness, as checked118. If U=max(||A||,||B||), both spectra lie in[0,U]. For U=0 the pair is zero and the conclusions below are immediate; otherwise the same construction works on that compact rectangle.

Their spectral projections are L_(E_A(S)) and R_(E_B(T)). To check the normal representation point explicitly, if projections E_i increase to E in Q, then for Y in Q,

\[
 \|(L_E-L_{E_i})Y\|_2^2=\tau[Y^*(E-E_i)Y]\longrightarrow0
\]

by normality; the right version follows in the same way or by cyclicity. Uniform norm bounds extend this strong convergence to all L2 vectors. The left and right representations therefore carry spectral projections to the indicated projections. Commuting bounded self-adjoint operators have commuting spectral projections, so the joint spectral theorem applies on arbitrary H.

Let mu_AB be the joint spectral **vector** measure at e, a positive Borel probability measure on[0,U]^2. On rectangles it satisfies

\[
 \mu_{AB}(S\times T)
 =\langle e,L_{E_A(S)}R_{E_B(T)}e\rangle
 =\tau[E_A(S)E_B(T)]. \tag{4}
\]

The last number is positive because the product of the two Hilbert-space projections is a projection; also trace cyclicity gives tau(E_A E_B)=tau(E_B E_A E_B)>=0. Thus(4) is not treating a noncommuting product in Q as a positive operator. It is a vector measure of the commuting left/right pair. Total mass is||e||2^2=1.

For bounded Borel u,v, simple-function approximation and bounded convergence, or the joint Borel calculus, give

\[
 \int u(a)v(b)d\mu_{AB}(a,b)=\tau[u(A)v(B)]. \tag{5}
\]

One first checks indicators by(4), extends to simple functions, and uses the bounded spectral theorem/normality for the limit. In particular the marginals are the trace spectral distributions of A and B, and

\[
 \int\phi(a)d\mu=\tau\phi(A),\quad
 \int a\log_+(b)d\mu=\tau[A^{1/2}\log_+(B)A^{1/2}],
\]
\[
 \int a h_n(b)d\mu=\tau[A^{1/2}h_n(B)A^{1/2}]. \tag{6}
\]

All equalities in(6) involve bounded functions. Scalar monotone convergence of a h_n(b)>=0 now identifies its limit integral with N(A,B), including +infinity. No unbounded operator product or indefinite trace interchange has been presumed.

## Canonical entropy equals a nonnegative Borel kernel integral

Define on the closed nonnegative quadrant

\[
 f(a,b)=a\ln(a/b)-a+b\quad(a,b>0),
\]
with f(0,b)=b for b>0, f(a,0)=+infinity for a>0 and f(0,0)=0. For b>0, f(a,b)=b[t ln t-t+1],t=a/b, with0ln0=0. The convex scalar function t ln t-t+1 has minimum0 at1. Hence f is nonnegative everywhere with these conventions.

Write f as the sum of the bounded signed function

c(a,b)=phi(a)-a log_+(b)-a+b

on the rectangle and the nonnegative extended function a log_-(b), taking0 times infinity to mean0. Equations(6) and monotone convergence for the latter function prove

\[
 D_\tau(A\Vert B)=\int f(a,b)d\mu_{AB}(a,b)\ge0. \tag{7}
\]

In particular it is legitimate to add the finite integral of c to the nonnegative extended integral. If applying monotone convergence to c+a h_n directly, add a fixed finite constant making c nonnegative first; no claim that every unshifted truncated kernel is nonnegative is needed. This proves the canonical identification rather than simply defining D as a regularization limit.

It also recovers the usual bounded invertible formula tau(A ln A-A ln B)-tau A+tau B: when B has a positive lower bound its logarithms are bounded and(1) is that ordinary trace formula. In a finite matrix algebra(7) is the familiar sum over spectral pairs with weights tau(P_i Q_j); singular kernels receive their actual extended values. It is not a pseudolog rule setting ln0 to0.

## Support and integrability are separate

Let P_0=E_B({0}). The mass weighted by a at b=0 equals

\[
 \int a\,1_{\{b=0\}}d\mu=\tau(AP_0)
 =\|A^{1/2}P_0\|_2^2. \tag{8}
\]

By faithfulness, this is zero exactly when A^(1/2)P_0=0, equivalently supp(A)<=supp(B). If this support inclusion fails, the positive quantity in(8) contributes n tau(AP_0) to the nth negative-log truncation, so D(A||B)=+infinity. This argument works for noncommuting support projections.

If inclusion holds, the b=0 contribution is zero, but the integral of a log_-(b) near b=0 may still diverge. Precisely, D(A||B) is finite if and only if N(A,B)<infinity. Equal supports do not guarantee this. If the two supports are unequal, at least one inclusion fails, so J_ext=+infinity. Equal-support pairs, including full-support pairs, still require the integrability criterion. This is the missing distinction in any attempt to use a finite common-corner argument for a diffuse algebra.

## Common-epsilon regularization, including infinite limits

For epsilon>0 define A_e=A+epsilon1 and B_e=B+epsilon1. On L2, left and right operators shift by epsilon I. Therefore the joint vector measure for the shifted pair is the pushforward of mu_AB under(a,b)->(a+epsilon,b+epsilon). Its ordinary finite entropy is

\[
 D_\tau(A_e\Vert B_e)=\int f(a+\epsilon,b+\epsilon)d\mu_{AB}. \tag{9}
\]

For every a,b>=0 the integrand is nonnegative. Its derivative with respect to epsilon is

\[
 \frac{d}{d\epsilon}f(a+\epsilon,b+\epsilon)
 =\ln r+1-r\le0,\qquad r=(a+\epsilon)/(b+\epsilon)>0. \tag{10}
\]

The inequality follows from ln r<=r-1. Thus decreasing epsilon increases the kernel. Its endpoint limit is exactly f(a,b): the interior is continuous; for a=0<b, epsilon ln(epsilon/(b+epsilon))->0 and the limit is b; for b=0<a the limit is +infinity; for a=b=0 it is identically0. Monotone convergence, first along any decreasing sequence epsilon_n->0 and then monotonicity for all epsilon, gives

\[
 D_\tau(A_e\Vert B_e)\uparrow D_\tau(A\Vert B)
 \quad(\epsilon\downarrow0). \tag{11}
\]

Apply the same argument to the reversed pair. Both entropies are nonnegative, so adding their limits is valid in[0,infinity] without subtraction:

\[
 J_p(A_e,B_e)\uparrow J_{p,\mathrm{ext}}(A,B). \tag{12}
\]

For positive-gap pairs, expanding the two ordinary relative entropies shows that their sum equals tau[(A-B)(ln A-ln B)]; linear trace terms cancel. This establishes the identification of(12) with the exact production used118. No finite-production assumption is hidden in(11) or(12).

For entropy H, let omega_eta be a modulus of uniform continuity of phi on[0,U+1]. When0<epsilon<=1, spectral calculus gives ||phi(C+epsilon1)-phi(C)||<=omega_eta(epsilon) for C=A,B,M. Because tau is a state, |H(A_e,B_e)-H(A,B)|<=2omega_eta(epsilon)->0; p+q=1 and M_e=M+epsilon1. In particular H>=0 follows from the positive-gap result or its convexity argument.

The118 inequality applies to every epsilon>0. Taking(12) and the finite H limit proves(3). If J_ext=+infinity the inequality is valid in the extended sense; if finite, both sides have ordinary limits. No point with zero denominator is used to take a quotient.

For completeness, H=0 occurs exactly at A=B. If U>0 and X=A-B, the118 Hessian formula on C_t+epsilon1 is an average of inverses of operators bounded above by(U+epsilon)I. Therefore F_e''(t)>=||X||2^2/(U+epsilon), and its Green integral gives

\[
 H_p(A_e,B_e)\ge\frac{pq}{2(U+\epsilon)}\|A-B\|_2^2.
\]

Letting epsilon down0 gives H>=pq||A-B||2^2/(2U). Faithfulness proves strict positivity if A!=B. The case U=0 is A=B=0. If A=B, the measure lies on the diagonal by(4), f vanishes there, and H=J_ext=0. This estimate is a domain check, not a sharp new constant claim.

## A second pivotal check: positive resolvent production

An alternate derivation checks the direction in(12), sharing the admitted A,B,tau but not the scalar-kernel monotonicity argument. Put X=A-B. For epsilon>0, the norm-resolvent identity for logarithms gives

\[
 \frac{J_p(A_e,B_e)}{pq}
 =\int_\epsilon^\infty\tau[X(B+s1)^{-1}X(A+s1)^{-1}]ds
 =\int_\epsilon^\infty\|(B+s1)^{-1/2}X(A+s1)^{-1/2}\|_2^2ds. \tag{13}
\]

Indeed R_B-R_A=R_B X R_A, and the Hilbert-Schmidt square is the trace expression after cyclicity. Its norm is bounded by||X||2^2/s^2, integrable on[epsilon,infinity]. Thus every manipulation at fixed epsilon is a bounded norm-integral/trace operation. The nonnegative integral increases as its lower endpoint decreases. Combining its limit with the independently established canonical identification(11) proves

J_ext/pq=integral from0toinfinity of the squared norm in(13), possibly infinity.

This confirms the reviewed resolvent formula while supplying the missing detailed identification with canonical trace truncations. Merely calling the integral the usual entropy would not have established(7). The expected formula was exposed in the source; this is an alternate analytic check, not blind or independent human review.

## Native entropy, generator, scaling and reverse infimum

The block state is rho=(A,B) in Q directsum Q with trace p tau directsum q tau, and E_pi rho=(M,M). Its canonical generalized relative entropy is pD(A||M)+qD(B||M). Both terms are finite. To check this even without a positive gap, bounded h_n(M)>=0 satisfy

\[
 p\tau[A^{1/2}h_n(M)A^{1/2}]
 +q\tau[B^{1/2}h_n(M)B^{1/2}]=\tau[Mh_n(M)].
\]

The right side increases to tau[M log_-(M)]<infinity because x log_-(x), extended by0 at0, is bounded on[0,U]. Positivity and p,q>0 bound each of the two limits. The bounded log-positive terms sum in the same way. The linear trace corrections cancel. Consequently

\[
 D_{p\tau\oplus q\tau}(\rho\Vert E_\pi\rho)=H_p(A,B). \tag{14}
\]

For invertible blocks, direct expansion of L=c(I-E_pi) gives production cJ_p. Its canonical extended production is cJ_ext in(2), also exactly the increasing regularized limit in(12). This is the production convention proved here; no additional assertion about every possible unbounded-generator/domain definition is inferred.

For s>0 the joint measure under simultaneous scaling is the pushforward(a,b)->(sa,sb), and f(sa,sb)=s f(a,b), including zero and infinite values. Hence D(sA||sB)=sD(A||B), J_ext scales by s, and H scales by s because the common log s contributions cancel. If T=tau M>0, dividing both blocks by T gives the single total density condition p tau A+q tau B=1. If T=0, faithfulness and positivity imply A=B=0, already handled. For normalized regularized inputs use A_e/(T+epsilon),B_e/(T+epsilon); the same limits and quotient follow by homogeneity. Two separate trace-one block conditions are never imposed.

Inequality(3) gives infimum>=a_p over all admitted auxiliaries and H>0, where infinite production yields infinite quotient. The scalar algebra C with positive unequal scalar pairs is contained in this class, and its infimum is exactly a_p. Thus the reverse bound holds without an attained minimizer or numerical approximation. Multiplying the production by c>0 gives optimal constant c a_p on the stated bounded class.

## Exact controls and false altered assertions

| Control | Exact result | Ceiling |
|---|---|---|
| A=B, including common diffuse zero spectrum | Joint vector measure is diagonal, f=0 there, H=J_ext=0. | No quotient0/0. |
| A=0, B nonzero | D(0||B)=tau B; D(B||0)=infinity; J_ext=infinity. The zero pair has both D=0. | Zero blocks and zero-pair conventions explicit. |
| Unequal noncommuting supports | For example in M2, P=diag(1,0) and Q=(1/2)[[1,1],[1,1]] have tau[P(I-Q)]=1/4 with tau=Tr/2. Hence the n-th negative-log truncation contributes at least n/4; each directed entropy is infinite. | No simultaneous diagonalization or finite pseudolog substitution. |
| Full-support diffuse A(x)=x,B=1 | D(A||B)=integral(x ln x-x+1)=1/4. D(B||A)=integral(-ln x-1+x)=1/2. Thus J_ext=3pq/4 is finite although A has no bounded inverse. | Covers full support with no gap, finite integrability. |
| Full-support A(x)=exp(-1/x),B=1 | D(B||A)=integral(1/x-1+exp(-1/x))=infinity; D(A||B) is finite since phi(A),A are bounded. Hence J_ext=infinity. | Equal supports do not imply finite entropy/production. |
| Monotonicity sign | A=0,B=1 gives D(A+1||B+1)=1-ln2 and D(A+2||B+2)=1-2ln(3/2), whose difference is ln(9/8)>0. | The changed assertion that D_e increases with increasing e is FALSIFIED. The actual direction is(11). |
| Normalization | H and J_ext both have degree one; normalized epsilon densities use T+epsilon, not T or two independent block traces. | Native factor2, c>0 and0<p<1 fixed. |
| Finite matrices/scalars | Borel integral reduces to spectral-pair sums and matches117; positive-gap pairs recover118. | Domain inclusion, not matrix exhaustion. |

The pseudolog shortcut also fails already at A=0,B=1: setting ln0=0 would give a finite or zero expression whereas the canonical reverse entropy is infinite. The source manuscript's same-support corner contains A+epsilon e with positive lower bound epsilon e, but original A in a diffuse full-support corner need not be boundedly invertible or have finite logarithmic production. No such original invertibility/finiteness is used here. All altered-assertion failures are separated from the original inequality, which survives the controls.

## Adjudication, transfer and next decision

| Claim | Outcome | Exact scope |
|---|---|---|
| M07-TRACIAL-BOUNDED-BOUNDARY-C119 | PROVED internally / PASS AT CLAIM CEILING | Every bounded positive pair, all finite faithful normal tracial auxiliaries, all0<p<1; canonical J_ext>=2a_pH and reverse infimum; native c>0 and weighted normalization. |
| M07-CANONICAL-ENTROPY-LIMIT-C119 | PROVED internally | Trace-truncation D equals positive Borel-kernel integral; D_e increases to D, H_e->H, J_e increases to J_ext, possibly infinity. |
| M07-BOUNDARY-ALTERED-GUARDS-C119 | FALSIFIED changed assertions only | Increasing-e monotonicity, finite pseudolog endpoint, and same-support finiteness; exact controls above. |
| Unbounded affiliated states, products/reset>=3/general classical equality | NOT_TESTED119 / held | No automatic promotion from bounded two-point inputs. |
| Novelty/current worldwide status/human or formal acceptance/performance | NOT_ESTABLISHED / NOT_TESTED / NOT_MEASURED | No primary-owner public survey, external review or controlled benchmark in this attempt. |

The uncertainty changed from an unidentified no-gap entropy convention to a complete bounded-domain canonical identification and limit. Positive Borel kernels and trace truncations transfer to other bounded tracial relative-entropy boundary checks, but not automatically to unbounded states, other generators or multi-value reset comparison. Do not repeat finite two-point separation grids, the positive-gap proof, or a finite-corner finiteness shortcut without a new consumer. This was the explicitly selected terminal gate after116–118; retire the bounded two-point leaf and rotate. The whole-frontier decision (historical local record; not distributed here) chooses the next separate ready obligation; none is implied by this theorem alone.

## Evidence and trust inventory

Exact inspections (historical local record; not distributed here) and the reading ledger (historical local record; not distributed here) bind three direct local mathematical records:118proof208/208full, internal review30–53 and151–190/333partial, frozen manuscript187–197/266partial. Review167–190 adds24guaranteed direct body lines; the guaranteed review union becomes1–190/333, while manuscript union remains1–197/266. This is one full plus two partial records/four intervals/three recorded whole-file hashes in the named set. Shared draft/review lineage is not independent evidence. All source text is literal UTF8 and inert; no supplied code or TeX execution, mathematical program, numerical approximation or new PDF read occurred.

The source review's product/tensorization and scalar-check claims visible in the new lines were not needed or adopted here. No external theorem cited by the review, its numerical computation, or its separate POVM/reset certificate serves as a dependency. Foundational spectral/measure inputs are stated and their application hypotheses checked above. Independence is limited by shared actor/model, source and expected mechanism; the resolvent cross-check targets monotonicity/sign/model errors, not those shared assumptions.

Estatepass047 is unchanged:155directpaths145full/10partial,146recorded hashes;113/428327candidatepaths107full/6partial, underlying-source count and volume content denominator UNKNOWN. M10original26/33text and21/33visual;Cook10/12; other estate/PDF extents unchanged. No fresh current-world-status or novelty claim is made. Memory was a packet-specific provenance/scope reminder only, checked against current records. No agent, public request, external message/upload/publication, foreign-estate write/source execution, install/purchase/account, app/schedule/notification change or unmanaged continuation occurred. See the run report (historical local record; not distributed here) for integration and checked operational closeout.

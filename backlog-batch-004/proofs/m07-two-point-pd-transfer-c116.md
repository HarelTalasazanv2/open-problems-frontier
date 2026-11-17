# Audited historical reading edition

**Current audited claim:** PROVED: For every 0<p<1 and finite positive-definite complex Hermitian pair, J_p>=2 a_p H_p and the all-finite-matrix infimum equals the scalar infimum a_p.

**Claim ceiling:** Exactly the stated reset generator, total density normalization and factor two; no numerical scalar bracket or general classical-generator equality.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Two-point scalar deficit transfers to every finite positive-definite matrix pair

**PROVED internally at the exact scope below.** For every0<p<1, every finite matrix size, and positive-definite complex Hermitian A,B, the two-point matrix entropy-production quotient is at least the scalar infimum. Scalar pairs give equality of the infima. This closes the project's positive-definite finite-matrix comparison, including the biased p=1/10 chain. It does not yet establish the singular-state extension, arbitrary finite von Neumann auxiliaries, products, arbitrary classical chains, novelty or human/formal acceptance.

This is an exposed reconstruction of the submitted source and existing internal review, by the same actor/model. The favored conclusion and mechanism were already known. It is not blind reproduction or independent human review. No numerical scalar certificate or supplied executable is used.

## Statement and native normalization

Fix p∈(0,1), q=1−p, m≥1 and τ=Tr/m on M_m(C). For positive-definite complex Hermitian A,B put X=A−B, M=pA+qB, φ(s)=s ln s, and

\[
 H_p(A,B)=p\tau\varphi(A)+q\tau\varphi(B)-\tau\varphi(M),\qquad
 J_p(A,B)=pq\tau[X(\ln A-\ln B)].
\]

For scalar positive inputs define the same quantities without τ, and set

\[
 a_p=\inf_{r>0,\ r\ne1}\frac{J_p(r,1)}{2H_p(r,1)}.
\]

The exact theorem is J_p(A,B)≥2a_pH_p(A,B), including A=B, and

\[
 \inf_{m\ge1,\ A,B>0,\ A\ne B}\frac{J_p(A,B)}{2H_p(A,B)}=a_p. \tag{T}
\]

All logarithms are natural. The scalar infimum is well defined, nonnegative and finite: strict scalar convexity gives H_p(r,1)>0 for r≠1, monotonicity of ln gives J_p(r,1)>0, and any fixed r≠1 gives a finite upper bound. No minimizer or closed formula is assumed.

Use the nonnegative generator L=c(I−E_π), c>0, with invariant weights π=(p,q), E_π(A,B)=(M,M), and semigroup e^(−tL). For the weighted trace pτ⊕qτ, direct substitution gives

\[
 D((A,B)\Vert(M,M))=H_p(A,B),\qquad
 (p\tau\oplus q\tau)[L(A,B)\ln(A,B)]=cJ_p(A,B).
\]

Indeed A−M=qX and B−M=−pX, and the two mixed logM terms add to τ[M lnM]. Thus the native convention is **2αD≤production**, and the constant in(T) scales to ca_p. This is exactly the native p=1/10, q=9/10, L=I−P normalization in the historical scalar dossier. Its17/20 bound or later numerical brackets are not assumed in this proof.

For s>0, φ(sC)=sφ(C)+s(ln s)C. The added entropy terms cancel, so H_p(sA,sB)=sH_p(A,B); log differences give J_p(sA,sB)=sJ_p(A,B). Dividing both matrices by τM>0 enforces the single total-density normalization pτA+qτB=1 without altering the quotient. Requiring τA=τB=1 separately would change the admitted class and is not used. The case c=0 and endpoint weights p=0,1 are outside this contract.

## Entropy curvature, with justified derivatives

Let C_t=(1−t)B+tA and F(t)=τφ(C_t), t∈[0,1]. Write a_−,a_+ and b_−,b_+ for the positive extreme eigenvalues of A,B. Set δ=min(a_−,b_−)>0. The segment has C_t≥δI, persisting on a slightly larger open interval with a smaller positive bound if X≠0; X=0 is constant.

The spectral theorem gives the norm-convergent improper identity

\[
 \ln C=\int_0^\infty\big[(1+s)^{-1}I-(C+sI)^{-1}\big]ds.
\]

Differentiating the inverse yields

\[
 \frac{d}{dt}\ln C_t=\int_0^\infty (C_t+sI)^{-1}X(C_t+sI)^{-1}ds. \tag{1}
\]

The derivative integrand norm is at most ‖X‖/(δ+s)², integrable in s and uniform on the segment. The corresponding bound on a slightly larger interval justifies differentiation under the integral, including at the original endpoints. Trace cyclicity and the scalar integral ∫₀∞c/(c+s)²ds=1 give

\[
 F'(t)=\tau[(\ln C_t+I)X],\quad
 F''(t)=\int_0^\infty\tau[X(C_t+sI)^{-1}X(C_t+sI)^{-1}]ds. \tag{2}
\]

For example, in differentiating τ[C_t lnC_t], the second product-rule term is τ[C_tDln(C_t)[X]]=τX by moving X to the end of the trace and applying that integral spectrally. This supplies F′ without importing an unproved holomorphic differentiation rule. The same domination supplies continuity of F″; C² is sufficient here, so no stronger analyticity claim is needed.

On the complex Hilbert space of matrices with inner product ⟨Y,Z⟩=τ(Y*Z), let L_CY=CY and R_CY=YC. These are positive self-adjoint operators when C>0, and L_C,R_C commute. For positive scalars x,y,

\[
 \int_0^\infty\frac{ds}{(x+s)(y+s)}
 =\int_0^1\frac{d\theta}{(1-\theta)x+\theta y}; \tag{3}
\]

both sides equal(lnx−lny)/(x−y) if x≠y, and1/x if x=y. In an eigenbasis of C, the matrix units simultaneously diagonalize L_C and R_C, with eigenvalues x,y. Thus(3) applied to each of the finitely many matrix units proves the required operator identity, including repeated eigenvalues.

Define positive operators on this **m²-dimensional matrix Hilbert space** by

\[
 P_\theta=(1-\theta)L_B+\theta R_B,\qquad
 Q_\theta=(1-\theta)L_A+\theta R_A.
\]

Combining(2)–(3) and the linearity of left/right multiplication gives

\[
 F''(t)=\int_0^1\langle X,[(1-t)P_\theta+tQ_\theta]^{-1}X\rangle d\theta. \tag{4}
\]

No commutation of A with B, or of P_θ with Q_θ, is assumed. In particular this is not simultaneous unitary diagonalization of A,B on the original m-dimensional space.

## Positive spectral pencil identity

For positive-definite operators P,Q on a finite-dimensional Hilbert space and a vector e, suppose X=(Q−P)e. Put K=P^(−1/2)QP^(−1/2) and v=P^(1/2)e. Direct multiplication proves

\[
 P^{-1/2}X=(K-I)v,\qquad
 [(1-t)P+tQ]^{-1}=P^{-1/2}[(1-t)I+tK]^{-1}P^{-1/2}.
\]

The finite-dimensional spectral theorem, with the positive measure ν(S)=⟨v,1_S(K)v⟩, now gives

\[
 \langle X,[(1-t)P+tQ]^{-1}X\rangle
 =\int\frac{(k-1)^2}{1-t+tk}\,d\nu(k). \tag{5}
\]

In(4) choose e=I. Then P_θe=B, Q_θe=A, so the essential relation X=(Q_θ−P_θ)e holds exactly. This proves

\[
 F''(t)=\int_0^1\int\frac{(k-1)^2}{1-t+tk}\,d\nu_\theta(k)d\theta. \tag{6}
\]

The measure has mass ‖v_θ‖²=⟨I,P_θI⟩=τB, not necessarily1. Its displacement moment is ∫(k−1)dν_θ(k)=⟨I,(Q_θ−P_θ)I⟩=τ(A−B), though that moment is not needed for the inequality.

The draft identifies v_θ=B^(1/2). This also holds in finite matrices: in an eigenbasis of B, I lies in the diagonal subspace, P_θ acts there by multiplying the j-th diagonal entry by b_j, and its square root sends I to B^(1/2). The proof above avoids needing this extra identification; it uses v_θ=P_θ^(1/2)I directly.

## Bounds and integral interchange

For every θ∈[0,1], b_−I≤P_θ≤b_+I and a_−I≤Q_θ≤a_+I. Congruence therefore gives

\[
 (a_-/b_+)I\le K_\theta\le(a_+/b_-)I.
\]

Let ℓ=a_−/b_+>0 and u=a_+/b_−<∞. All spectral measures in(6) are supported on[ℓ,u], with common finite mass τB. For t∈[0,1] and k in this interval, 1−t+tk≥min(1,ℓ)>0. Hence the absolute value of the kernel in(6) is bounded by max(|ℓ−1|,|u−1|)²/min(1,ℓ). These are per-pair bounds; no uniform spectral gap across all admitted pairs is claimed or needed.

The matrices P_θ,Q_θ, their positive square roots/inverses and K_θ vary continuously in θ. For continuous f on[ℓ,u], ∫f(k)dν_θ(k)=⟨v_θ,f(K_θ)v_θ⟩ is continuous. Eigenvalue crossings or repeated eigenvalues need no continuous choice of eigenvectors. To interchange t and θ one may use ordinary Fubini on the continuous bounded scalar inner products in(4); for fixed θ the spectral integral is a finite sum, which can be integrated in t term by term. This suffices for the iterated integral below without assuming a joint diagonalization or an unproved regularity of individual eigenvectors.

## Exact scalar-deficit transfer

Let G_p(t)=qt for0≤t≤p, and G_p(t)=p(1−t) for p≤t≤1. Splitting the integral at p and integrating by parts gives, for every C² function F,

\[
 \int_0^1G_pF''=pF(1)+qF(0)-F(p).
\]

The boundary derivative terms cancel because G_p(p)=pq; the remaining terms are−q(F(p)−F(0))+p(F(1)−F(p)). Since C_p=M, this is H_p(A,B). Also

\[
 pq\int_0^1F''(t)dt=pq[F'(1)-F'(0)]=J_p(A,B).
\]

For any real α, the signed kernel pq−2αG_p is bounded. The bounds above therefore justify all the following operations even when α is not positive. Applying the same Green identities to g_k(t)=φ(1−t+tk), with g_k″=(k−1)²/(1−t+tk), yields

\[
 \boxed{J_p(A,B)-2\alpha H_p(A,B)
 =\int_0^1\int[J_p(k,1)-2\alpha H_p(k,1)]\,d\nu_\theta(k)d\theta.} \tag{7}
\]

This scalar calculation is an elementary identity, not an assumed MLSI inequality. At α=a_p its inner integrand is nonnegative by the definition of the infimum for k≠1. At k=1 both scalar terms are zero; no undefined ratio is inserted. Positive measures now prove J_p(A,B)≥2a_pH_p(A,B).

If A≠B, then X≠0. For each fixed t,s, the integrand in(2) is τ[(R^(1/2)XR^(1/2))²]>0, R=(C_t+sI)^(−1); the congruence is invertible and the trace is faithful. Thus F″(t)>0, and G_p is strictly positive in(0,1), giving H_p(A,B)>0. If A=B, H_p=J_p=0 directly. There is no hidden small-denominator tolerance.

Common scalar scaling reduces every scalar pair(a,b) to(r,1). Taking m=1, or A=rI_m and B=I_m, realizes all those scalar quotients inside the matrix class. Their infimum is a_p, so the proved lower bound gives(T), regardless of whether any minimizing scalar r is attained. This completes the exact theorem.

The quotient for A≠B is more precisely a probability mixture of scalar quotients, weighted by H_p(k,1)dν_θ(k)dθ/H_p(A,B); atoms at k=1 receive zero weight. The original spectral measures with mass τB are not themselves asserted to be probability measures. This explains why noncommuting entries cannot lower this quotient beneath the scalar infimum.

## Analytic controls and rejected changed models

These are exact analytic checks, not numerical samples establishing a universal theorem.

| Control | Expected result and actual check | Scope |
|---|---|---|
| Scalars and commuting matrices | In a simultaneous eigenbasis with entries a_j,b_j, ν_θ=(1/m)Σb_jδ_(a_j/b_j) on the diagonal contribution, independent of θ. Formula(7) reduces to the coordinate scalar identities. | PASS; no assumption that a general pair commutes. |
| Complex noncommutation | A=((2,i),(−i,2)) has eigenvalues1,3; B=diag(1,2) is positive and [A,B]=((0,i),(i,0))≠0. The proof uses congruence, not joint diagonalization of these matrices. | Admissible exact input; this is a structural coverage check, not a computed quotient. |
| Zero deficit and atoms | A=B gives X=0,H=J=0; k=1 contributes zero on both sides of(7). | PASS; ratios excluded only at zero entropy. |
| Near scalar equilibrium | r=1+ε gives H_p(r,1)=pqε²/2+O(ε³), J_p(r,1)=pqε²+O(ε³), hence J/(2H)→1. These follow from φ's ordinary Taylor expansion near1. | Fixes the native factor2; not a claimed optimizer for biased p. |
| Asymmetric Green location | At p=1/3,A=4,B=1, H_p=(2/3)ln2. Replacing G_p by G_q would yield H_q=(16/3)ln2−3ln3. Their difference is(1/3)ln(2¹⁴/3⁹)<0 since16384<19683. | FALSIFIED changed identity; no source identity refuted. |
| Missing pencil coherence | P=Q=1,e=1,X=1 gives actual quadratic form1, while the putative right side of(5) is0 at k=1. Here X≠(Q−P)e. | FALSIFIED extension of(5) to arbitrary X. This is not the separately reported POVM certificate. |
| Scaling | H,J scale together; c multiplies production only; normalizing τM does not impose two separate block traces. | PASS exactly. |

For completeness the uniform scalar normalization can be checked without an imported constant. By common scaling let a=1+s,b=1−s, |s|<1. At p=q=1/2, H(s) is even, H′(s)=atanh s, H(0)=0, and J(s)=s atanh s. For0≤s<1 the convergent positive series gives

\[
 H(s)=\sum_{j\ge0}\frac{s^{2j+2}}{(2j+1)(2j+2)},\qquad
 J(s)=\sum_{j\ge0}\frac{s^{2j+2}}{2j+1}\ge2H(s).
\]

Termwise integration is justified by uniform convergence on each[0,s] with s<1. Evenness covers negative s; the near-equilibrium limit gives a_(1/2)=1. This is a known prior-art case, not a novelty assertion.

A concrete wrong-factor variant is then false: the altered inequality J≥4a_(1/2)H fails at scalar A=4,B=1. Here J=(3/2)ln2 and H=4ln2−(5/2)ln(5/2), so4H−J=(1/2)ln(2⁴⁹/5²⁰)>0. Positivity follows already from2⁷=128>125=5³, raising to the seventh power. The original factor2 passes the scalar bound above. This checks a meaningful rejected normalization rather than merely comparing matching notation.

Endpoint weights, singular matrices and infinite-dimensional auxiliary algebras are outside the theorem. Arbitrarily small **positive** eigenvalues remain covered individually by the per-pair bounds; no limit to zero is silently promoted. The supplied unrestricted POVM failure remains a separate AS_REPORTED internal-review outcome; its certificate was not executed or reaudited116.

## Claims, effect and remaining obstruction

| Claim | Verdict | Exact limitation |
|---|---|---|
| M07-TWO-POINT-PD-TRANSFER-C116 | PROVED internally / PASS AT CLAIM CEILING | Every finite m, all positive-definite complex Hermitian pairs, every0<p<1, native c>0 scaling. |
| M07-POSITIVE-PENCIL-C116 | PROVED internally | Coherent X=(Q−P)e, positive-definite finite-dimensional P,Q, t∈[0,1]. |
| M07-TRANSFER-MODEL-GUARDS-C116 | FALSIFIED changed assertions | G_q replacement, arbitrary-X extension, and factor4 variant each have the exact counterexample above; none refutes the source theorem. |
| Matrix comparison at p=1/10 on the PD domain | PROVED as a consequence | No numerical scalar value, sharp-minimizer or prior17/20 proof audit is imported. |
| Singular matrices/general finite von Neumann auxiliaries/products/reset chains/general classical equality | NOT_TESTED116 | Do not promote the full manual review from this finite-PD check. |
| Novelty/current worldwide status/external human or formal acceptance/performance | NOT_ESTABLISHED / NOT_TESTED / NOT_MEASURED | No public status query or reviewer contact. |

The uncertainty changed from an unadopted review assertion to a complete local finite-PD proof. A search for a strict biased two-point separation using positive-definite finite matrices is therefore retired under this normalization; old grids and local curvature results remain preserved history. The previous interpolation and α₁=1 shortcut failures still do not refute equality. This proof bypasses those routes rather than rehabilitating them.

The smallest next mathematical gap is the **finite singular-state extension**, with φ(0)=0 and an explicit extended entropy-production definition. Common support may permit restriction to a finite support corner; different supports require a proved infinite-production convention or regularization limit. This is a distinct boundary argument, not another matrix grid. No such boundary theorem is adopted116.

## Source custody, direct extents and independence

The frozen attempt (historical local record; not distributed here) precedes the six selected text readings. Exact inspections (historical local record; not distributed here) bind whole-file hashes, UTF-8 byte offsets, line extents and lineage:

- Existing internal REPORT.md, lines1–150/333, partial, finite-PD core only. Broader claims in its header/table were read as scope warnings, not accepted proofs.
- Submitted frozen manuscript.tex, lines1–197/266, partial, inert TeX. Its visible singular paragraph and broader statements were not checked or promoted. No compile, source script execution, later reset section or new PDF read.
- claim_ledger.json, all79lines; input_manifest.json, all41lines; native M07 definition dossier, all15lines; native biased scalar dossier, all45lines. These four complete local records supply claims/custody/normalization context; their other results are not new independent sources or newly reproduced certificates.

The frozen manuscript is byte-identical to the original submitted packet; that relationship does not turn two copies into two readings or independent sources. The review and manuscript share the underlying argument. The reviewed29manifest members and7original/snapshot input pairs are custody checks, not29source reads. Six local text records are4full+2partial, not a volume-estate increment. Underlying-source independence is not claimed. Estatepass047 remains155paths=145full+10partial,146recorded hashes and113/428327candidate paths, with source/content denominators UNKNOWN. M10original26/33text/21/33visual, Cook10/12 and other extents are unchanged.

Only this bounded proof object is rederived; no fresh public primary-source/status/priority survey was performed. Bibliographic claims in the input remain source-reported, and no external tensorization theorem is needed for(T). The method shares source, input selection, actor/model and platform with the exposed context. Alternative resolvent and finite spectral formulations target missing commutation, derivative, integration and normalization steps; they do not supply external review.

No mathematical executable, numerical optimization, interval certificate, proof assistant, agent, external message/upload/publication, foreign-estate write/execution, installation, account/purchase action, application/schedule/notification change or unmanaged continuation occurred. Detailed integration, decision and closeout are in the run report (historical local record; not distributed here).

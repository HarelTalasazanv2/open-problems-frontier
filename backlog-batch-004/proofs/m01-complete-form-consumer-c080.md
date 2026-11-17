# Audited historical reading edition

**Current audited claim:** PROVED: The same canonical minima obey the displayed inverse-log-squared bound with H_K=2(21/2+2M_K)^2+pi^2/2+1.

**Claim ceiling:** Smaller sufficient constant, not a new modulus order, runtime gain, practical certificate or positivity.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle080 — the improved graph bound has a complete canonical-form consumer

**PROVED internally, at the exact scope below.** For the closed Connes–Consani canonical Weil form, the lowest eigenvalue in either ordinary complex-linear parity sector has the inverse-log-squared modulus in §1, with the smaller sufficient constant furnished by079. The complete form, common domain, prime translations, actual remainder kernel, all minimizers and both variational directions are checked here. This preserves the order already proved076; it improves a sufficient constant and audits its consumer. It is not a new continuity theorem, an optimal rate, a practical numerical mesh, a historical Bombieri2003 identification, positivity or RH.

Frozen attempt (historical local record; not distributed here); reconstruction (historical local record; not distributed here). The canonical definition is read directly from [Connes–Consani2023, equations2.7–2.12, Proposition2.1 and Lemma2.2](https://ems.press/content/serial-article-files/44477?nt=1), independently of Suzuki's target continuity result. The exact public-source inspection extents (historical local record; not distributed here) distinguish text and visual readings from full-paper reading. Standard Fourier theory, the representation theorem for closed forms, and the standard digamma asymptotic specified below are named analytic inputs. No numerical deciding experiment, formal proof or external expert review occurred.

## 1. Exact statement and constants

Let I=(−1,1), H=L²(I;C), Eu the zero extension, Ju(x)=u(−x), Sσ=ker(J−σ), σ∈{+1,−1}. Fourier convention is Ff(ξ)=∫e^(−ixξ)f(x)dx, with Plancherel factor1/(2π). Set N=||u||² and

V={u∈H:∫(1+log⁺|ξ|)|F(Eu)(ξ)|²dξ<∞}.

The fixed closed nonnegative form and its associated operator are

ell(u)=¼∫∫I² |u(x)−u(y)|²/|x−y| dxdy −½∫I log(1−x²)|u(x)|²dx,

A=A_ell, D(A)={u∈V:ell(u,v)=〈g,v〉 for all v∈V, some g∈H}.

Inner products and polarized forms in this note are linear in the first variable. The source uses the opposite convention; diagonal real values agree and determine the same form by polarization. The subscript ell names the form, not an interval half-width or a first derivative.

Fix 0<b≤c<∞, K=[b,c], and define

κ=log(2π)+γ, R=2c,

M_R=2cosh(R/2)+1,

L_R=sinh(R/2)+(19/48)e^(2R)+(3/4)e^(4R),

S_K=Σ_{2≤n≤exp(2c)}Λ(n)/√n,

T_K=max(|log b|,|log c|)+|κ|,

M_K=T_K+2S_K+2cM_R,

D_K=2c/b², G_K=1/b+2(M_R+2cL_R),

H^H_K=2(21/2+2M_K)²+π²/2+1,

**C^H_{K,2}=2G_K+2S_K(4D_K+72)H^H_K.**                 (1)

All sums are finite over integers; Λ(n)=0 unless n is a prime power. Let q_a be the canonical form on functions supported in [e^(−a),e^a], carried unitarily to H by F(e^t)=a^(−1/2)u(t/a). Define λσ(a)=inf{q_a(u):u∈V∩Sσ,||u||=1}. Then

**|λσ(a)−λσ(a′)|≤C^H_{K,2}/log²(e/δ), δ=|a−a′|,**

for a,a′∈K and 0<δ≤min(1/2,b/2). At δ=0 the difference is0. If b=c the positive-δ range is empty. No uniform assertion at b=0 or c=∞ is intended. The unrestricted lowest value min(λ+,λ−) obeys the same estimate by the elementary minimum inequality.

**Claim ceiling:** an internal analytic estimate for these canonical minima on every fixed positive compact parameter interval, under standard named analytic inputs and the079 internally proved graph inequality; no global conjecture, novelty, optimality, practical enclosure or independent-person/formal verification claim.

## 2. Direct canonical normalization and closure

Write v(t)=F(e^t), where source Haar measure d*u=du/u becomes dt. There is no extra factor e^(t/2) in this unitary change of variables. Let C_v(t)=∫v(s+t)conj(v(s))ds. Multiplicative conjugate adjoint gives (F* *F)(e^t)=C_v(t); it is not ordinary parity. Also C_v(−t)=conj(C_v(t)), C_v(0)=||v||², and C_v(t)=0 at and beyond |t|=2a. Equality at the endpoint holds because the overlapping supports have measure zero.

The source's equations2.6–2.8 give, initially on compact smooth v,

Qcan(v)=P(C_v)−Σ_{2≤n≤e^(2a)}Λ(n)/√n [C_v(log n)+C_v(−log n)]−W_R(C_v),

P(C)=∫R (e^(t/2)+e^(−t/2))C(t)dt,

W_R(C)=(log(4π)+γ)C(0)+∫₀∞[C(t)+C(−t)−2e^(−t/2)C(0)]k(t)dt,

k(t)=e^(−t/2)/(1−e^(−2t)), t>0.                    (2)

For clarity P(C_v)=2Re(A_v conj(B_v)), A_v=∫e^(t/2)v(t)dt, B_v=∫e^(−t/2)v(t)dt. It is a cross product, not |A_v|²+|B_v|². This checks the pole sign and coefficient independently of the old decomposition.

Define the finite part

P₀(C)=lim_{ε↓0}{∫_ε∞[C(t)+C(−t)]/(2t)dt+log ε C(0)}.

With the same cutoff on every singular term,

2∫_ε∞e^(−t/2)k(t)dt=∫_ε∞dt/sinh t=−log tanh(ε/2)=−log ε+log2+o(1).

Consequently

−W_R(C)=−κC(0)−lim_{ε↓0}{∫_ε∞[C(t)+C(−t)]k(t)dt+log ε C(0)}.

Let the actual remainder be the real even function

r″(t)=−2cosh(t/2)+k(t)−1/(2t), t>0; r″(0)=−7/4.   (3)

The bounded continuation at0 and the bounds it needs are proved in §3. Substitution into (2) gives exactly

Qcan(v)=−P₀(C_v)−κ||v||²−Σ paired prime terms−∫R r″(t)C_v(t)dt. (4)

This is a direct source-defined identity; the notation r″ agrees with048/051 but no unverified Lerch-function differentiation is needed for this consumer. In particular the negative pole kernel is included in r″, rather than dropped.

On I, zero-extension translation energy satisfies

ell(u)+log2 N=¼∫_{|h|<2}||Eu(·+h)−Eu||² dh/|h|

=∫₀²[N−Re C_u(h)]dh/h.                              (5)

To verify the first equality, expand the double integral for zero extensions. Interior pairs give the regional term in ell; the two crossings at each boundary integrate to −½log(1−x²)+log2. The second equality uses ||T_hEu−Eu||²=2N−2Re C_u(h) and evenness. Since C_u vanishes outside [−2,2], (5) gives **ell(u)=−P₀(C_u)** on the smooth core. For v(t)=a^(−1/2)u(t/a), C_v(t)=C_u(t/a), and changing the cutoff to ε/a gives P₀(C_v)=P₀(C_u)+log a N. Moreover

∫R r″(t)C_v(t)dt=〈K_a u,u〉,

K_a(x,y)=a r″(a(x−y)), x,y∈I.

Evenness removes the harmless orientation reversal between a correlation and a convolution quadratic form. Thus the exact fixed-domain expression is

**q_a(u)=ell(u)−(log a+κ)N**

**−Σ_{2≤n≤exp(2c)} c_n[C_u(τ_n/a)+C_u(−τ_n/a)]−〈K_a u,u〉,** (6)

c_n=Λ(n)/√n, τ_n=log n. The fixed pool is identical to the source's moving pool: for n>exp(2a) the correlation vanishes, and it also vanishes at the boundary n=exp(2a). No discontinuous pool membership is differentiated.

Here is why (6) identifies the closed forms, not just smooth values. Source Proposition2.1 defines its closure with archimedean multiplier

m(ξ)=2θ′(ξ)=Re ψ(1/4+iξ/2)−logπ.

This is real continuous and bounded below. The standard digamma asymptotic ψ(z)=log z−1/(2z)+O(|z|^(−2)) in a closed sector away from the negative real axis gives m(ξ)=log|ξ|−log(2π)+o(1); the source's printed104 Lemma2.2 gives the stronger expansion. We use only this growth equivalence, not the expansion coefficient. On every fixed compact frequency interval m is bounded, and at infinity m+an appropriate constant is bounded above and below by positive multiples of 1+log⁺|ξ|. Therefore the source's finite-energy space is exactly the fixed-support first-log space V, with equivalent shifted form norm after scaling. Pole and finite prime terms are bounded, as also verified directly in §4.

C_c^∞(I) is a core for V: contract support first by f_r(x)=r^(−1/2)Eu(x/r), r↑1. Its Fourier transform is √r F(Eu)(rξ). The weighted dilation maps are uniformly bounded for r near1, by 1+log⁺(|η|/r)≤(1+|log r|)(1+log⁺|η|), and are strongly continuous first on continuous compactly supported Fourier data and then by density. Convolve f_r with smooth compact approximate identities of radius less than1−r. Their Fourier multipliers have modulus≤1 and converge to1, so dominated convergence in the weighted norm supplies the core. Thus both source and (6) closed forms agree on a common form core and have equivalent shifted norms; their closures are identical. This uses form-core convergence, not the stronger and unnecessary assertion of operator-core convergence.

The closedness/nonnegativity of ell and the graph estimate in §5 were re-established079. For completeness, closedness also follows from (5), Plancherel and J(s)=∫₀ˢ(1−cos t)dt/t: 1+J(2|ξ|) is comparable to 1+log⁺|ξ|, by integration by parts in the cosine integral outside1. The zero-support subspace is closed in L².

## 3. Actual kernel size and two-point Lipschitz control

Set H(t)=k(t)−1/(2t). For x>0,

0<1/(1−e^(−x))−1/x<1.

The lower inequality is 1−e^(−x)<x; the upper is x<e^x−1. Both follow by integrating strictly positive exponential derivatives, or their power series. Hence

H(t)=e^(−t/2)[1/(1−e^(−2t))−1/(2t)]+[e^(−t/2)−1]/(2t)

satisfies −1/4≤H(t)≤1, since 1−e^(−t/2)≤t/2. In particular |r″(t)|≤M_R on [−R,R].

For a genuine two-point estimate without singular subtraction, define on [0,R]

h(t)=∫₀¹e^(−2tu)du,

Z(t)=∫₀¹[−½e^(−st/2)+∫₀¹2u e^(−2stu)du]ds.

The fundamental theorem of calculus gives e^(−t/2)−h(t)=tZ(t), so H(t)=Z(t)/(2h(t)) for t>0. This representation extends smoothly from the right to0, where h(0)=1, Z(0)=1/2 and H(0)=1/4. It proves (3)'s continuation. Differentiation under these bounded compact integrals gives

h≥e^(−2R), |h′|≤1, |Z|≤3/2,

|Z′|≤∫₀¹s(1/4+∫₀¹4u²du)ds=1/8+2/3=19/24.

Thus |H′|≤(19/48)e^(2R)+(3/4)e^(4R), and the positive-side derivative of −2cosh(t/2) has modulus≤sinh(R/2). Even extension and ||s|−|t||≤|s−t| prove

**|r″(s)−r″(t)|≤L_R|s−t|, s,t∈[−R,R].**            (7)

This does not assume r∈C³. Indeed h′(0)=−1, Z′(0)=1/8−2/3=−13/24, so H′(0+)=−1/48. Evenness gives the left derivative +1/48. The cusp falsifies C³ but leaves the required Lipschitz statement intact.

For z∈[−2,2], a,a′∈K,

|a r″(az)−a′r″(a′z)|≤δ(M_R+2cL_R).

Each row and column of the kernel has interval length2. Schur's bound, with both row and column integrals bounded by twice the displayed quantity, therefore gives

**||K_a−K_a′||≤2δ(M_R+2cL_R), ||K_a||≤2cM_R.**       (8)

## 4. Bounded perturbations, attainment and all minimizers

Let S_hu=(Eu)(·+h)|I. It is a contraction, S_h*=S_(−h), and 〈S_hu,u〉=C_u(h). The paired prime term is self-adjoint; the kernel is real even and symmetric. Each pair, K_a and the scalar term commute with J. Writing q_a=ell+〈B(a)u,u〉, (6)–(8) prove

**B(a)=B(a)*, JB(a)=B(a)J, ||B(a)||≤M_K.**            (9)

There is no assumed operator-norm continuity for translations.

V embeds compactly into H. To see this, a bounded V-ball has Fourier tails bounded by a constant divided by 1+log R. The Fourier map L²(I)→L²([−R,R]) is Hilbert–Schmidt because its kernel e^(−ixξ) is square-integrable on this finite rectangle. After inverse transform, low-frequency parts are precompact in L²(R). Uniformly vanishing tails give precompactness of the whole zero extensions, hence of their restrictions to I. The parity projections (1±J)/2 preserve V.

The normalized trials

φ+=(√15/4)(1−x²), φ−=(√105/4)x(1−x²)

have norm1 and derivative norms squared5/2,21/2 by direct polynomial integration. They are in H₀¹(I) in their respective sectors. For u∈H₀¹(I), ||T_hEu−Eu||≤|h| ||u′||; integrating (5) gives ell(u)+log2 N≤||u′||², since ∫_(−2)^2|h|dh=4. Thus both trials have ell≤21/2, and

**−M_K≤λσ(a)≤21/2+M_K.**                            (10)

A normalized minimizing sequence has bounded ell by (9)–(10), hence a strongly L²-convergent subsequence. Its limit remains unit and in the closed parity sector; lower semicontinuity of ell and continuity of the bounded perturbation give attainment. This works separately for every a and both nonzero sectors.

Take **any** unit minimizer u. Real variations in v and iv in the same sector give q_a(u,v)=λσ(a)〈u,v〉. If v has opposite parity, invariance under J makes both sides zero. Since every v∈V splits into its two parity components, the equation holds for all v∈V. Closed-form representation then gives

u∈D(A), **Au=(λσ(a)−B(a))u**, ||Au||≤21/2+2M_K.     (11)

No spectral gap, simple eigenvalue or continuous choice of eigenvector has entered this proof.

## 5. Uniform squared-log moment and exact translations

The079 local analytic theorem, with its explicit actual-form/core proof, is

W₂(u)=(2π)^(−1)∫(1+log⁺|ξ|)²|F(Eu)|²dξ

≤2||Au||²+(π²/2+1)||u||², u∈D(A).                  (12)

Its mechanism is MEu=EAu+1_outside Ku, M=log|D|+γ, Ku=−(π/2)sign(x)H(Eu) outside I and the full-line Hilbert isometry ||Hf||=||f||. Orthogonality of interior/exterior gives ||MEu||²=||Au||²+||Ku||², with ||Ku||²≤π²N/4. The pointwise weight inequality (1+log⁺|ξ|)²≤2(log|ξ|+γ)²+1 follows for t=log|ξ|≥0 from t²+(4γ−2)t+2γ²≥0, using1/2<γ<1; for t<0 it is immediate. These are the precise previously proved inputs, not a new claim to optimality. The global domain and exclusion of endpoint distributions are proved in079§§1–4 and retained as internal review debt, not blind reproduction here.

Apply (12) to every minimizer in (11): **W₂(u)≤H^H_K**. Form energy alone would not supply this moment; the full equation is essential.

For any finite-W₂ vector, Plancherel gives the absolutely convergent correlation formula

C_u(h)=(2π)^(−1)∫e^(iξh)|F(Eu)(ξ)|²dξ.

If |h−k|≤Dδ, D≥0, 0<δ≤1/2, put t=log(1/δ), U=δ^(−1/2). Split at U; use |e^(iξh)−e^(iξk)|≤|ξ|Dδ at low frequencies and≤2 at high frequencies. Then

|C_u(h)−C_u(k)|≤D√δ N+2W₂(u)/(1+t/2)²

≤D√δ N+8W₂(u)/t².                                  (13)

Writing L=1+t=log(e/δ), elementary scalar bounds are

√δ L²≤4, δL²≤2, L/t≤3, t≥log2.

For the first, (1+t)²e^(−t/2) has maximum16e^(−3/2)<4 at t=3; e³>1+3+9/2+27/6+81/24=131/8>16. For the second, (1+t)²e^(−t) has maximum4/e<2. For the third log2=∫₁²dx/x≥1/2. Since N≤W₂(u), (13) proves

**|C_u(h)−C_u(k)|≤(4D+72)W₂(u)/log²(e/δ).**          (14)

This controls arbitrary real h,k, complex vectors, both signs and support crossings. It is an expectation estimate on a moment ball; on full L², ||T_h−I||=2 for h≠0, so an operator-norm shortcut would be false. No Fourier tail is discarded or numerically truncated.

## 6. Both Rayleigh directions and endpoint coverage

For every n in the finite pool, τ_n≤2c and

|τ_n/a−τ_n/a′|=τ_nδ/(aa′)≤D_Kδ.

The same holds for negative shifts. Equations(8),(14), the scalar bound |log a−log a′|≤δ/b and a unit vector with W₂≤H^H_K give

|q_a(u)−q_a′(u)|≤G_Kδ+2S_K(4D_K+72)H^H_K/L²

≤[2G_K+2S_K(4D_K+72)H^H_K]/L².                     (15)

Choose an actual minimizer at a as a competitor at a′; common V, same unit norm and same sector are established above. It satisfies the moment bound, hence λσ(a′)−λσ(a)≤C^H_{K,2}/L². Choose a minimizer at a′ to obtain the reverse inequality. This proves §1, including multiplicities and either parity. Zero δ is handled separately; a or a′ at b,c cause no issue. Empty prime pool S_K=0 is allowed. The proof even permits δ≤1/2 without the additional b/2 restriction, but the frozen smaller range is retained.

## 7. What is improved, and what remains unproved

For exactly the same definitions of M_K,D_K,G_K,S_K, the076 sufficient constant was

C^old_{K,2}=2G_K+2S_K(4D_K+72)[2(21/2+2M_K)²+π²+2].

Thus

C^old_{K,2}−C^H_{K,2}=2S_K(4D_K+72)(π²/2+1)≥0.

The difference is strictly positive if S_K>0 and zero if the prime pool is empty. The old theorem remains valid; no historical record is replaced. The inverse-log-squared order is unchanged, and this arithmetic comparison is not a speed/reliability benchmark or a2× claim.

The bound is extremely conservative. For example, on K=[1,2], R=4, L_R≥(3/4)e^16, G_K>6e^16 and C^H_{K,2}>12e^16. The sufficient printed inequality C^H_{K,2}/log²(e/δ)≤1/100 would consequently require δ<exp(1−20√3 e^8). This is a limitation of this sufficient certificate, not a necessary spacing of actual eigenvalues. No pointwise eigenvalue enclosure, truncation error, residual certificate or useful mesh has been constructed. A practical tolerance would require a separately frozen approximation and error budget. Nothing here proves H¹ regularity, forbids stronger eigenfunction estimates, or supplies a matching lower bound for sharpness.

No global-open or novelty status is refreshed by this bounded source check. Historical Bombieri2003 extended-form values/infima, complete Weil positivity, RH, and the missing historical COVER203 object retain their separate existing holds/ceilings. Human review and formal verification are outstanding.

## 8. Adversarial ledger, independence and next decision

| Object or attack | Result at exact scope |
|---|---|
|Canonical Haar/Fourier change, pole, primes and constant|PROVED by direct source cutoff calculation; no extra e^(t/2) and no sum-of-squares pole substitution.|
|Smooth identity promoted to closure without core|Rejected shortcut; actual multiplier growth and support contraction/mollification give common V and common core.|
|Assuming C³ at origin|FALSIFIED auxiliary statement by one-sided derivatives; required two-point Lipschitz bound PROVED.|
|Dropping prefactor or Schur factor|Both a dependence terms and row/column length2 retained in(8).|
|A trial alone used as minimizer regularity|Rejected shortcut; compactness, attainment, full stationarity and(11) are proved first.|
|Sector-only stationarity, multiplicity or complex phases|All-sector tests and both signed correlations covered without an eigenvector selection.|
|Prime threshold equality and δ interfaces|C(±2)=0, finite pool, δ=0,δ=1/2,b=c and empty pool explicitly covered.|
|One Rayleigh inequality mistaken for an absolute bound|Both minimizers separately inserted in(15).|
|New modulus order/practical mesh inferred from smaller moment constant|Not established; only the stated sufficient constant improves.|

The deciding evidence is analytic. Custody/record validators check artifacts and membership, not the theorem. The author/model has seen051/052/076/079, shares Fourier conventions and the079 proof input, and is not a blind or independent human reproducer. Direct canonical cutoff derivation provides a different route around the source-specific g/D*G chain; it does not remove shared standard analysis assumptions. No new scientific CLI certificate, numerical eigenvalue, outward-rounded interval or empirical dataset is represented as executed.

**Uncertainty changed:**079's stronger graph bound is now connected to the actual complete canonical form with checked translations, kernel and minimizer bridge. The pure-dilation-only shortcut is inadequate but unnecessary. **Do not repeat:** the same graph bound, higher moments or constant tightening absent a named useful tolerance/certificate mechanism. The printed bound does not presently ready a practical mesh. Rerank to a neglected substantive source/corpus gate, using an exact metadata-backed target and a frozen bounded read; any later numerical M01 program needs a new approximation/error contract first.

Usefulness: this closes the named remaining analytic consumer obligation and states why it does not yet enable practical computation. Authority: read-only primary source inspection and local OPF records only; no donor execution/mutation, agents, messages, upload, publication or automation change.

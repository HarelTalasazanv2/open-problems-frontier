# Audited historical reading edition

**Current audited claim:** PROVED: On each specified positive compact parameter interval, both ordinary complex parity minima obey the displayed explicit C_K/log(e/delta) bound.

**Claim ceiling:** Actual specified canonical minima; loose sufficient constants, not sharpness, useful numerical mesh or positivity.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Cycle052 — an explicit compact-parameter modulus for canonical parity minima

**PROVED internally, at the exact scope below:** on every compact K=[b,c]⊂(0,∞), both ordinary complex-linear parity lowest unit Rayleigh infima for the051 canonical Weil forms obey an explicit inverse-logarithmic continuity bound. All complex form-domain states needed in the variational comparison and every prime threshold are covered. This is a quantitative refinement of the internally reproduced qualitative theorem, not a claim of novelty, optimality for the actual minima, differentiability, positivity, historical Bombieri2003 identification or RH. Outside human review and formal verification remain outstanding.

**FALSIFIED, separate auxiliary scope:** the exact source remainder r is not C³ across0. Its even continuous second derivative has right derivative −1/48 and left derivative +1/48 there. A genuine two-point Lipschitz estimate survives; it does not require a continuous third derivative.

## 1. Freeze, sources and inherited objects

The frozen052 attempt (historical local record; not distributed here) fixes the inverse-log target, compact positive parameter interval, complex ordinary parity, uniform-energy/Fourier-split/remainder method, controls and finite budget before the deciding derivation. No numerical deciding instrument is used. The exact source-defined decomposition and canonical closure identification are inherited from047–051. Their custody is ARTIFACT_VERIFIED, not a claim that every predecessor proof was blindly re-proved this run.

The current [Suzuki v3 primary text](https://arxiv.org/html/2606.09096v3), selected§4.2–4.5, was directly reviewed for its qualitative continuity mechanism, uniform minimizer form-energy control and parity scope. It uses compactness and variational upper/lower semicontinuity;the inspected passage does not state the explicit rate proved here. That bounded source observation does not establish novelty elsewhere. The [arXiv record](https://arxiv.org/abs/2606.09096) still lists v3 dated September23,2026. [Clay](https://www.claymath.org/millennium/riemann-hypothesis/) still labels RHUnsolved today. Full captured files are not full-paper reads;exact extents/hash/lineage are in the052source register. No PDF-layout claim is made this run. The source's scaling and cutoff display defects identified047/049 remain preserved, and are not used here.

Let H=L²((−1,1);C), ordinary linear reflection Jw(x)=w(−x), sectors S_σ=ker(J−σI), σ∈{+1,−1}, and V the zero-extension logarithmic form domain from050. With f the zero extension,

F(ξ)=∫e^(−iξx)f(x)dx,  N=||w||²=(2π)^−1∫|F|²,
W(w)=(2π)^−1∫(1+log⁺|ξ|)|F(ξ)|²dξ.

Write ell for the nonnegative closed logarithmic form from050 and κ=2A+1=log(2π)+γ. The exact inherited estimates are

W(w)≤7[ell(w)+(1+log2)N],
ell(w)+log2*N=¼∫_{|h|<2}||f(·+h)−f||²dh/|h|.          (1)

The correctly scaled051canonical form is

q_a(w)=ell(w)−(log a+κ)N
 −Σ_{2≤n≤e^(2c)} c_n[C_w(τ_n/a)+C_w(−τ_n/a)]−<K_aw,w>,
C_w(h)=∫f(x+h)conjugate(f(x))dx,
c_n=Λ(n)/sqrt(n), τ_n=log n,
K_a(x,y)=a r″(a(x−y)),                                (2)

for a∈K and w∈V. The finite pool includes all integers up to e^(2c), with zero coefficients when not prime powers. C_w(h)=0 for |h|≥2, including equality, so(2) agrees exactly with each moving source cutoff. No growing/infinite prime pool is differentiated.

Define λ_σ(a)=inf{q_a(w):w∈V∩S_σ, N=1}.047–051 give attainment, common V and canonical identification. These are the actual canonical sector infima, not unidentified historical quantities.

## 2. Explicit constants and theorem

Fix 0<b≤c<∞. All constants below depend only on b,c and the stated normalization:

R=2c,
M_R=2cosh(R/2)+1,
L_R=sinh(R/2)+(19/48)e^(2R)+(3/4)e^(4R),
S_K=Σ_{2≤n≤e^(2c)}Λ(n)/sqrt(n),
T_K=max(|log b|,|log c|)+|κ|,
M_K=T_K+2S_K+2c M_R,
E_K=7[21/2+2M_K+1+log2],
D_K=2c/b²,
G_K=1/b+2(M_R+2c L_R),
**C_K=G_K+2S_K(2D_K+12)E_K.**                         (3)

Every sum is finite;the formula is explicit even when no prime lies in the pool. No evaluated decimal, floating-point enclosure or assumed numerical eigenvalue enters it. These constants are deliberately loose;their practical usefulness for any requested tolerance must be assessed separately.

For σ=±1 and a,a'∈K, set δ=|a−a'|. The theorem is

**|λ_σ(a)−λ_σ(a')|≤C_K/log(e/δ),**
          0<δ≤min(1/2,b/2).                           (4)

The proof in fact works for every0<δ≤1/2 with a,a'∈K;the smaller frozen interval is retained in(4). At δ=0 the difference is0 and the modulus has continuous extension0. No uniform statement at b=0 or c=∞ is licensed.

## 3. A real two-point remainder estimate, including0

For t>0 the exact048identity is

r″(t)=−2cosh(t/2)+H(t),
H(t)=e^(−t/2)/(1−e^(−2t))−1/(2t).

A one-point bound H(t)=1/4+O(t) would not by itself imply Lipschitz continuity between two nearby positive points. To obtain that property without singular subtraction, define for t≥0

h(t)=∫₀¹e^(−2tu)du,
j(t)=e^(−t/2)−h(t),
Z(t)=∫₀¹[−½e^(−st/2)+∫₀¹2u e^(−2stu)du]ds.

Since j(0)=0, the fundamental theorem of calculus gives j(t)=t Z(t). Hence for t>0,

H(t)=Z(t)/(2h(t)),                                   (5)

and the right side is a regular smooth function on [0,R]:h≥e^(−2R)>0. Derivatives under these finite integrals are valid by uniform boundedness of the exponential derivatives on the compact rectangle/cube. Direct integration bounds give

|Z|≤3/2,  |Z'|≤1/8+2/3=19/24,  |h'|≤1,
|H'|≤(19/48)e^(2R)+(3/4)e^(4R).

Indeed Z' has integrand s[¼e^(−st/2)−∫₀¹4u²e^(−2stu)du];absolute bounds integrate to the displayed19/24. Together with the derivative of −2cosh(t/2), this proves |(r″)'(t)|≤L_R on the positive side, up to its one-sided endpoint. Even extension and ||x|−|y||≤|x−y| yield

**|r″(x)−r″(y)|≤L_R|x−y| for x,y∈[−R,R].**           (6)

The inherited048bound |r″|≤M_R supplies the separate size control. Thus no hidden C³ regularity is assumed.

A useful exact negative control is available from the same representation:

h(0)=1, h'(0)=−1,
Z(0)=1/2, Z'(0)=1/8−2/3=−13/24,
H'(0+)=(−13/24)/2−(1/2)(−1)/2=−1/48.

The cosh derivative vanishes at0, so (r″)'(0+)=−1/48. Evenness gives (r″)'(0−)=+1/48. The two derivatives differ: **r is not C³ at0**. This falsifies only that tempting auxiliary strengthening;048claimed C², so there is no reversal of a prior result. Formula(6) remains valid across the cusp.

For z=x−y∈[−2,2], (6) now gives

|a r″(az)−a' r″(a'z)|≤δ[M_R+2c L_R].

Both row and column lengths are2;Schur's bound therefore yields

||K_a−K_a'||≤2δ(M_R+2c L_R).                          (7)

All scale factors and both parts of the product difference are retained.

## 4. Uniform energy of actual sector minimizers

Let B(a) be the bounded perturbation in(2). Correlations satisfy |C_w(h)|≤N by Cauchy–Schwarz, while ||K_a||≤2cM_R. Thus uniformly on K,

||B(a)||≤M_K, and −M_K≤q_a(w)−ell(w)≤M_K for N=1.    (8)

The fixed normalized sector trials are

φ_+(x)=sqrt(15)/4*(1−x²),
φ_−(x)=sqrt(105)/4*x(1−x²), x∈(−1,1).

They lie in the indicated H₀¹ sectors. Exact polynomial integration gives

||φ_+||²=||φ_−||²=1,
||φ_+'||²=5/2, ||φ_−'||²=21/2.

For every H₀¹vector, zero extension is H¹ and ||T_hf−f||≤|h| ||w'||. From(1), since ∫_{−2}²|h|dh=4,

ell(w)+log2*N≤||w'||²,

so each trial has ell≤21/2. Consequently both sector minima satisfy

−M_K≤λ_σ(a)≤21/2+M_K.                               (9)

For **any** normalized minimizer w_{a,σ}, (8)–(9) give

ell(w_{a,σ})≤λ_σ(a)+M_K≤21/2+2M_K,
**W(w_{a,σ})≤E_K.**                                 (10)

This is uniform over all a∈K, both parities and all minimizer choices. There is no simplicity assumption or selected continuous eigenvector. A bound for one fixed test vector alone would not prove(10);the bounded perturbation inequality is essential.

## 5. Quantitative translation control on the energy ball

For all w∈V, Fourier inversion of its autocorrelation gives

C_w(h)=(2π)^−1∫e^(iξh)|F(ξ)|²dξ.

This integral is absolutely convergent by Plancherel, including complex w. For h,k∈R with |h−k|≤Dδ and0<δ≤1/2, split at U=δ^(−1/2)>1. The low frequencies use |e^(iξh)−e^(iξk)|≤Dδ|ξ|;the tail uses the bound2 and the logarithmic weight. Therefore

|C_w(h)−C_w(k)|≤D sqrt(δ)N +4W(w)/log(1/δ).           (11)

No operator-norm continuity is asserted. This is an expectation estimate with a quantified form-energy bound.

Write t=log(1/δ)≥log2. Elementary inequalities give

sqrt(δ) log(e/δ)=(1+t)e^(−t/2)≤2,
[1/log(1/δ)] log(e/δ)=1+1/t≤1+1/log2≤3,
δ log(e/δ)≤1.

The first bound follows by differentiating (1+t)e^(−t/2), whose maximum for t≥0 is2/sqrt(e)<2. The second uses log2=∫₁²dx/x≥1/2. The last follows from the monotonicity of δ(1−logδ) for0<δ<1 and its value(1+log2)/2<1 atδ=1/2. Since N≤W(w), (11) implies

**|C_w(h)−C_w(k)|≤(2D+12)W(w)/log(e/δ).**             (12)

For every member of the fixed prime pool,

|τ_n/a−τ_n/a'|=τ_nδ/(aa')≤(2c/b²)δ=D_Kδ.

Thus(12) controls each of the two signed shifts, including thresholds at ±2. The same correlation is exactly zero beyond those thresholds;no membership jump or boundary tolerance is introduced. Constants remain independent of n within the fixed finite pool.

## 6. Two-sided variational comparison

For a unit vector w∈V with W(w)≤E_K, the logarithmic scalar shift has difference≤δ/b. Equations(7),(12) and the triangle inequality give

|q_a(w)−q_a'(w)|
 ≤δ[1/b+2(M_R+2cL_R)]
   +2S_K(2D_K+12)E_K/log(e/δ)
 ≤C_K/log(e/δ).                                     (13)

To bound λ_σ(a')−λ_σ(a), insert an actual unit minimizer of q_a in sectorσ into q_a';the common domain and unitary parity scaling justify this competitor. By(10) it is eligible for(13), so

λ_σ(a')≤q_a'(w_{a,σ})≤λ_σ(a)+C_K/log(e/δ).

Interchanging a,a' gives the other direction and proves(4). No sign of λ, gap between sectors, simple eigenvalue or differentiable selection is used. Since min of two real pairs changes by no more than the maximum component change, the unrestricted lowest canonical value inherits the same bound;this is a consequence, not a historical-form identification.

## 7. Adversarial checks and limits

| Failure mode | Decisive check |
|---|---|
| Strong translations promoted to operator-norm continuity | (11) is derived directly from Fourier expectation with W;on full L²(R),||T_h−I||=2 for h≠0,so an operator-norm shortcut is invalid. |
| Hidden regularity at the origin | Exact one-sided derivatives ±1/48 reject C³;regular finite-integral formula proves the two-point Lipschitz bound actually needed. |
| Uniform-energy circularity | Trial upper bounds and a separate operator bound yield(10) before any comparison of minimizers at two parameters. |
| Wrong parity trial or normalization | Exact norms and derivative norms are given for both sectors;nonzero odd sector is explicitly covered. |
| Crossing a prime threshold | One finite pool and C(h)=0 for |h|≥2 cover either side and equality;both signed shifts are retained. |
| Complex orientation or sign | Autocorrelation Fourier integral is absolutely convergent;complex values are bounded in modulus and paired in q;no replacement by a single real correlation. |
| Missing scaling/interval factors | τ/a has derivative magnitudeτ/a²;K_a has both prefactor and argument changes;Schur length2 retained. |
| Hidden endpoints/division by zero | δ=0 handled separately;δ≤1/2 makes all logarithms positive;0<b≤c<∞. No rate at0/infinity or norm1 assumption on an uncontrolled sequence. |

All eight controls preserve(4). No numerical search/certificate or failed acceptance control is hidden behind these analytic checks. The source048C²statement survives the new auxiliary C³falsifier. Known qualitative primary results are not claimed as discoveries. Sameagent/model/platform,definitions and prior expected answers are shared;the Fourier split and regular integral derivation are not blind reproduction or independent human review. Formal verification NOT_TESTED;efficiency NOT_MEASURED.

## 8. What changed and next obstruction

The uncertainty changed from mere continuity to an explicit compact-parameter error bound, conditional only on the internally established canonical chain and standard Fourier/variational identities stated here. The remainder is now quantitatively Lipschitz with its origin cusp accounted for. A finite parameter mesh could use(4) to bound interpolation error **if** its pointwise values had separately justified enclosures;none were computed here, and large constants may make the bound impractical.

A sharper rate for the actual minima is unresolved. The current argument controls all states in a bounded logarithmic-energy ball, which may be the limiting mechanism rather than the eigenvalue branches themselves. The next discriminating action is an exact high-frequency family testing sharpness of the **energy-ball autocorrelation** estimate. Prove a matching inverse-log lower example or identify a stronger universal estimate. Such an example would rule out improving this argument from energy control alone, not prove the actual minima have that sharp modulus. Do not repeat qualitative continuity,claim eigenvalue-rate optimality from generic states,or reopen stalled historical2003retrieval.

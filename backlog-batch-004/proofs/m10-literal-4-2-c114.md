# Audited historical reading edition

**Current audited claim:** CONDITIONALLY_PROVED: The pinned v2source states Lemma4.2 on physical10. Assuming that lemma at its uniform threshold, the displayed finite normed-space consumer satisfies its field, real-noncollinearity, coverage and integer-ceiling hypotheses.

**Claim ceiling:** Conditional interface plus fixed-version source contract. This source-location audit alone does not prove4.2 or a generic/Euclidean theorem.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M10 literal Lemma4.2 contract and conditional consumer interface

**CERTIFIED_RANGE:** the complete literal Lemma4.2 is on physical page10 of the pinned Alon–Bucic–Sauermann v2 source. **CONDITIONALLY_PROVED:** its finite normed-space application on18 meets the displayed field, noncollinearity, difference-span and rounding requirements, provided Lemma4.2 itself is valid and n is above its unspecified threshold. The complete lemma, full5.2, Theorem1.3 and new Euclidean bounds are not proved by this audit.

The result resolves a specific source dependency left by110's12–16 window. It does not turn a known source theorem into a new discovery. Same exposed actor/model performed construction and challenge; no blind, human, external or formal review occurred.

## Custody, locator and direct reading

Primary: owned33-page v2 PDF (historical local record; not distributed here), https://arxiv.org/pdf/2302.09058v2 ,484598bytes, SHA256 `87801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960`. No latest-version, current global-status or novelty assertion is made.

Frozen attempt (historical local record; not distributed here) preceded the bounded locator (historical local record; not distributed here). It verified exact source identity, page count33 and complete ordered locator membership1–16. Nine controls covered a genuine header, inline/proof references, a wrapped proof reference, whitespace, wrong identifiers, missing/duplicate page membership and altered identity. A healthy window/identity also passed. These checks support a source-location instrument, not theorem validity.

Locator result (historical local record; not distributed here) returned a header candidate on10 and references on14/15. Its sixteen extracted texts are machine scans, not sixteen direct full-page readings. Printed previews expose only their recorded character ranges. The selection (historical local record; not distributed here) then fixed10,11,18 before complete text/visual inspection. Page10 contains the full4.2 statement and4.3 statement;11 contains4.4 and the beginning of4.3's proof;18 contains the actual5.2 consumer and its continuation into rational coefficients. No full4.3 proof or additional imported-theorem page was read114. Exact source register (historical local record; not distributed here) separates full pages from locator previews.

## Normalized literal statement, source assertion only

The page10 assertion has this quantifier structure: for every integer d>=1 and real mu with0<mu<1, n is sufficiently large depending on d,mu. Equivalently for this audit, name an unspecified integer threshold `N42(d,mu)` and restrict n>=N42. This threshold is not numerically identified, bounded or proved here.

Let F be a **subfield of R** and V a **real vector space**. Let `u_1,...,u_k` be a finite indexed list of nonzero vectors in V, and let `p_1,...,p_n` be distinct points in V that are **not all on one affine line over R**. Assume that for each pair x,y there is an index i with

`p_x-p_y in span_F(u_i)`.

The source concludes that some index subset `I subseteq {1,...,k}` satisfies

`#{ell : u_ell in span_F(u_i : i in I)} >= d|I| + (1-mu)n + 1`.

The count is over labelled indices, not over all vectors of a span. The statement does not require the entire u-list to be linearly independent or pairwise distinct. d is a positive integer parameter, not a stated dimension of V; the consumer chooses that parameter to equal its ambient normed-space dimension. The noncollinearity test is over R, even though the conclusion uses F-span. This is not the arbitrary-field contract of the separately checked weighted Lemma4.5 or the arbitrary-field graph Lemma4.3.

| Contract item | Actual source4.2 | Page18 consumer |
|---|---|---|
| Field | F subseteq R | Q(z_1,...,z_m) subseteq R |
| Ambient space | Real vector space V | R^d with a real norm |
| Parameters | d>=1,0<mu<1,n sufficiently large(d,mu) | n>=n0(d,mu); validity of4.2 requires this threshold to cover N42 |
| u-list | Nonzero, indexed; no global independence premise | One norm-unit representative per real difference direction; distinct real lines |
| p-list | Distinct, not real-affinely collinear | Distinct; collinearity excluded using the original distance budget and mu*n>1 |
| Pair coverage | Every pair difference lies in some one-vector F-span | Each nonzero difference is plus/minus z_j*u_i; zero differences handled explicitly below |
| Conclusion | At least d|I|+(1-mu)n+1 indices | Integer count becomes d|I|+ceil((1-mu)n)+1 |

The source statement's formulation is now identified. Its analytic/combinatorial proof and the existence/size of a valid N42 are still unverified local dependencies. Reading the statement does not prove those assertions.

## Exact conditional finite interface

The consumer contract (historical local record; not distributed here) fixes the following claim. Assume4.2 is valid for n>=N42(d,mu). Fix d>=1,0<mu<1, n>=max(2,N42), with `mu*n>1`. Suppose a norm on R^d and n distinct points realize at most `r=(1-mu)n` distinct positive pairwise distances. Set `m=ceil(r)`. Choose positive reals z_1,...,z_m containing every actual distance; if fewer than m are needed, pad by repeated positive values. Distinctness or algebraic independence of the z-values is not required. Let F=Q(z_1,...,z_m), and choose one oriented norm-unit vector u_i for every real line direction realized by a nonzero point difference.

Then a **nonempty** I has at least `d|I|+m+1` direction indices in its F-span. This claim is conditional only at the invocation of4.2 and its valid threshold; the following mapping and integer steps are elementary and complete.

**Real field and pair coverage.** The generated field F is a subfield of R containing Q and each positive z_j. For distinct x,y, normalize the difference by its norm. With the chosen orientation, `p_x-p_y=+z_j*u_i` or `-z_j*u_i` for some i,j, hence lies in span_F(u_i). Since n>=2 and the points are distinct, there is at least one nonzero difference and k>=1. For x=y the zero vector lies in any of those one-vector spans. All directions are norm-unit and nonzero. V=R^d is a real vector space as required.

**Noncollinearity.** If all n points lie on an affine real line, write them as `a+t_i v` for one v!=0 with distinct real t_i. Order the t_i and choose the minimum. Distances from that endpoint to the other n-1 points are `(t_i-t_min)||v||`, all positive and distinct. Thus any such collinear configuration has at least n-1 distinct distances, without assuming a Euclidean or strictly convex norm. But `mu*n>1` is equivalent to `n-1>(1-mu)n=r`, contradicting the assumed distance budget. Hence the points are noncollinear over R. For d=1 these assumptions give no admissible large configuration; that is a vacuous boundary case, not an exception hidden by tolerance.

**Apply the explicitly assumed lemma.** Now all displayed4.2 premises hold, including n>=N42. Let the resulting integer count be M and a=d|I|. Its conclusion gives `M>=a+r+1`. Because M-a-1 is an integer, this implies `M-a-1>=ceil(r)=m`, hence `M>=d|I|+m+1`. No strict inequality or the additional1 is lost. If I were empty its F-span would be{0}; none of the nonzero u_i would be counted, while the lower bound is positive. Therefore I is nonempty.

Relabelling an index subset as the first |I| entries is a bijection, not a change of multiplicity. The selected u_i already belong to their own span, so they can be included among any chosen `d|I|+m+1` counted indices. Coefficients expressing these vectors in the selected span lie in F by the definition of span. This verifies the finite interface that18 uses before its rational-function/angle continuation. It does **not** independently validate every rational-function choice, the complete A_mu* definition, the rest of5.2, quantitative threshold choice, or Baire/countable/global theorem.

## Attacks and exact limits

- **Strict size guard is needed for this collinearity inference.** With n=2,mu=1/2, two collinear points have one distance, equal to r. Thus replacing `mu*n>1` by equality would not exclude collinearity. This attacks that isolated inference, not4.2: no claim that n meets an unknown sufficiently-large threshold is made.
- **The original distance budget cannot be rounded upward as a hypothesis.** With n=3,mu=1/2, the Euclidean points (0,0),(1,0),(2,0) have two distances. They satisfy `s<=ceil(1.5)=2` but not `s<=1.5`, and are collinear. This falsifies the replacement inference `s<=ceil(r) => s<=r` and its resulting collinearity shortcut only. It is not a counterexample to the source lemma or full5.2 at their stated hypotheses/unknown n-threshold.
- **No arbitrary-field promotion.** The fact that4.5 was proved for any field does not erase the subfield-of-R and real noncollinearity premises of4.2. An arbitrary-field extension is NOT_TESTED, not declared false without a counterexample.
- **n0 is still a dependency.** Page18 explicitly uses n0(d,mu)>1/mu. A full application must also choose n0 large enough for4.2. No numerical n0/N42 and no verification of all earlier definitions is manufactured from this page.
- **No independence or dimension assumption is added to4.2.** Those belong to different lemmas or to the particular finite R^d application. Labelled closure counts are preserved.
- **Locator hints are not mathematical assertions.** The proof-of and inline matches on14/15 did not become statement locations; all full-page counts remain bounded by3.

**Adjudication:** CERTIFIED_RANGE for the literal source contract and actual consumer mapping. CONDITIONALLY_PROVED for the displayed finite interface assuming4.2/N42. The two isolated guard/rounding shortcuts are FALSIFIED by the exact examples above. Full4.2/5.2/Theorem1.3/new Euclidean bounds, arbitrary-field extension, current global status/novelty, human and formal verification remain INCONCLUSIVE/NOT_TESTED.

## What changed and next obstruction

The missing literal contract is resolved; it is no longer UNKNOWN where4.2 is stated or whether it uses an arbitrary field. The finite consumer's real-field, real-collinearity and integer steps are checked at a conditional ceiling. The remaining obstacle is the theorem's proof/import chain and threshold, not another search for its header.

Page10 identifies actual graph Lemma4.3 as a necessary ingredient, page11 starts its proof and its entropy ingredient4.4, and110's earlier source record locates the continuation on12. That supplies a genuinely ready bounded proof obligation for later ranking; it is not proved merely by the current partial proof read. The next queue entry must name that complete contract and adversarial controls or rotate, rather than repeating4.5 or extending a blind locator chain.

## Coverage and trust

Three direct complete text/visual rereads10/11/18, with new full visual11 only. Cumulative original full text stays26/33; full visual becomes21/33. Locator previews14/15 are separate partial direct rereads at recorded character extents, while sixteen full extracted texts are indirect machine output. Remaining27–33 are not fully text-read; prior partial31 is preserved. The source, underlying paper and estate-path counts do not increase. Distinct source/content denominators remain UNKNOWN.

The PDF was read, not edited or executed; the locator is new owned code using the installed parser and is not an independent mathematical checker. Same actor/model, source, library/platform and expected target were shared. There is no numerical approximation, formal assistant or external review. Local hashes support custody only. Report (historical local record; not distributed here) records integration, prior113 delayed handoff and the actual next selection. No external action, foreign-estate mutation/execution, agent, install, publication or automation change occurred.

Source-year clarification: append-only metadata note (historical local record; not distributed here) explains that2023 in the locator contract/lineage comes from the arXiv identifier, not a verified v2 revision year. The fixed v2 hash/bytes govern this audit;114 did not refresh release metadata. The prior101 revision-date statement is AS_REPORTED only.

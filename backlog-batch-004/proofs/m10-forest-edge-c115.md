# Audited historical reading edition

**Current audited claim:** PROVED: For the stated finite simple graph over any field with independent directions and each full direction class a forest, edges <= (n/2) log2 n.

**Claim ceiling:** The historical printed entropy-step failure is not adopted; the separate corrected proof is used.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Finite direction-forest edge bound — cycle115

**PROVED internally, at the exact finite scope below.** The known Lemma4.3 bound holds over every field. The printed proof of its entropy ingredient has a false intermediate inequality; a corrected induction and a second entropy argument establish the ingredient. This is source-exposed analytic reconstruction by the same actor/model, not blind, human expert or formal verification. No novelty or global distinct-distance result is claimed.

The frozen attempt (historical local record; not distributed here) precedes the three complete source reads10–12. The separate frozen amendment (historical local record; not distributed here) preserves the discovered printed defect and specifies the corrected confirmation. The original PDF and prior conclusions were not edited.

## Exact statement and conventions

Let F be any field, V an F-vector space, and u1,…,uk a finite linearly independent list (k may be zero). Let n≥1 and let p1,…,pn be distinct points of V. Let G be a finite simple undirected graph on [n]. Assume:

1. Every edge xy has px−py in F ui for some i.
2. For each i, the graph on all n vertices whose edge set is **all** edges xy of G with px−py in F ui is a forest, including isolated vertices.

Then

\[
 |E(G)|\leq \tfrac12 n\log_2 n.
\]

Span of an empty list is {0}; no logarithm of zero is required. The graph is not a multigraph and has no loops. Neither a field order, real embedding, finite ambient dimension nor noncollinearity is assumed. This scope is different from Lemma4.2's real-field and affine-noncollinearity assumptions. The source uses the ordinary graph convention; the present contract makes simplicity and undirectedness explicit.

If an edge belonged to F ui and F uj for i≠j, its nonzero difference would lie in their intersection. Independence makes this intersection {0}, a contradiction. Thus every edge has a unique direction. Positive-length independent lists contain no zero vector. If k=0, the first assumption forces E(G) empty.

## Printed entropy error and its exact counterexample

Physical11 states Lemma4.4 for positive integers n1≥…≥nℓ≥1, n=Σni:

\[
 n_1-\tfrac12\sum_i n_i\log_2 n_i
 \ge n-\tfrac12 n\log_2 n. \tag{E}
\]

Its final displayed induction chain merges n1 and nℓ into n1′. In the intermediate expression, the remaining sum over i=2,…,ℓ−1 is printed **without** its necessary coefficient1/2. This is present in both the full text extraction and visual page. The following second inequality in that literal chain is false for the admissible partition (2,2,2):

\[
 \underbrace{4-\tfrac12(4\log_2 4)-2\log_2 2}_{-2}
 \not\ge 6-3\log_2 6.
\]

Indeed 6³=216<256=2⁸, so log₂6<8/3 and 6−3log₂6>−2. This is an exact comparison, with no decimal error model. **FALSIFIED** applies to the printed intermediate inequality; **ARGUMENT_INVALID** applies to this literal induction step. It does not refute (E), Lemma4.3 or Lemma4.2. No source was silently corrected.

## Corrected entropy proof

Define h(t)=−t log₂t−(1−t)log₂(1−t), with continuous endpoint values h(0)=h(1)=0. On (0,1),

\[
 h''(t)=-\frac{1}{\ln2}\left(\frac1t+\frac1{1-t}\right)<0.
\]

Thus h is concave on [0,1]. Since h(1/2)=1 and h(1)=0, its graph lies above their chord: h(t)≥2(1−t) for 1/2≤t≤1. Endpoint continuity follows from x ln x→0 as x↓0, so no omitted boundary is being inferred numerically.

Prove (E) by induction on ℓ. At ℓ=1 it is equality. For ℓ≥2, put a=n1, b=nℓ, c=a+b and t=a/c∈[1/2,1). Then

\[
 a-\tfrac12(a\log_2a+b\log_2b)
 =-\tfrac12c\log_2c+c\,[t+\tfrac12h(t)]
 \ge c-\tfrac12c\log_2c.
\]

**Subtract one half of the remaining sum on both sides.** Apply the induction hypothesis to the positive sorted list c,n2,…,nℓ−1, whose sum is n and whose largest element is c. This gives (E). The missing coefficient is restored in a separately stated valid argument, not in the source artifact. Ties, ℓ=2 and n=1 are included; the empty remaining sum is zero.

A second formulation checks both the constant and inequality direction. Put pi=ni/n, p*=max pi. Equation(E) is equivalent to

\[
 H(p):=-\sum_i p_i\log_2p_i\ge 2(1-p_*). \tag{H}
\]

For p*=1 this is equality. If 1/2≤p*<1, split off that atom. Entropy decomposes as h(p*)+(1−p*)H(rest normalized), and the second term is nonnegative. The chord bound proves(H). If p*≤1/2, for 0<x≤1/2 define f(x)=−log₂x−2(1−x). We have f(1/2)=0 and f′(x)=2−1/(x ln2)<0, since ln2=∫₁²dt/t<1. Hence f(x)≥0, giving

\[
 H(p)\ge2\sum_i p_i(1-p_i)
 =2(1-\sum_i p_i^2)\ge2(1-p_*).
\]

The final substitution uses Σpi²≤p*Σpi=p*. This is another analytic argument on the same exposed claim, not a new independent reviewer or a numerical certificate.

## Graph proof by nonred components

Use strong induction on n. At n=1 a simple graph has no edges. At any n, an empty edge set satisfies the bound. Otherwise choose a used direction, relabelled uk, and let R be its **entire** direction edge set. It is a nonempty forest by assumption. Write T=F uk and S=span_F(u1,…,uk−1); independence gives T∩S={0}.

Delete R from G and let W1,…,Wℓ be the vertex sets of the connected components of the resulting graph H. Every H-edge has direction i<k. Telescoping a path in H therefore puts the difference of its endpoint points in S. Telescoping a red path puts the endpoint difference in T. These assertions use only field addition and scalar multiplication, including characteristic2; reversing a path edge changes the scalar's sign and causes no exception.

Each red connected component meets each Wj in at most one vertex. Otherwise distinct x,y in both components would have px−py in S∩T={0}, contradicting distinctness. In particular no red edge has both endpoints in a Wj. Thus every edge of G[Wj] is nonred, and the H-components are exactly these induced subgraphs as edge sets. Since R contains an edge, its endpoints lie in different Wj. Therefore ℓ≥2 and 1≤|Wj|<n.

Each G[Wj], relabelled onto [|Wj|], satisfies the same theorem hypotheses with the original independent list. Edge coverage is inherited. For each direction its **all-eligible** edge class is a subgraph of that direction's original forest; it cannot acquire a cycle. The induction hypothesis applies to every Wj, not merely selected components.

Let n1=maxj|Wj| and reorder the other sizes decreasingly. The n1 vertices in a largest Wj occupy n1 distinct connected components of the red forest. If c_R counts all its components including isolates, c_R≥n1. A finite forest on n vertices has n−c_R edges: remove a leaf and its incident edge in a nontrivial tree, or remove an isolated vertex, and induct. A nontrivial finite tree has a leaf by taking an endpoint of a longest simple path. Thus |R|≤n−n1.

Every G-edge is either in R or in exactly one of the induced G[Wj], and these alternatives are disjoint. Consequently, using the proved entropy inequality(E),

\[
 \begin{aligned}
 |E(G)|
 &=|R|+\sum_j|E(G[W_j])|\\
 &\le n-n_1+\tfrac12\sum_j |W_j|\log_2|W_j|\\
 &\le\tfrac12n\log_2n.
 \end{aligned}
\]

This completes the induction for every finite simple G, connected or disconnected, over every field. No ordered-field or Euclidean argument occurs. When V={0}, distinctness admits only n=1, already covered. Infinite fields or infinite-dimensional V cause no infinite sum: there are at most n component sets.

## Match to the actual source proof

The complete4.3 statement is on10; its proof starts11 and ends12. The source handles disconnected graphs first using the induction hypothesis and monotonicity of log₂. In a connected graph, paths from a fixed base point place every point in its affine span of the independent directions. Independence makes each coordinate unique. Its partition Wa by the uk coefficient has finitely many nonempty parts. Nonred edges stay within a Wa; red edges cross parts. A red component meets a Wa at most once by the same T∩S argument. A used red edge ensures at least two parts, hence smaller induction cases. All-eligible direction forests restrict to induced subgraphs. The source's red-edge bound n−max|Wa| and its final substitution are valid **with the corrected entropy proof supplied above**.

This explicitly checks the coordinate argument and the component formulation's common pivotal intersection lemma. It is source-exposed reconstruction and a changed formulation, not blind reproduction. Page12's concluding hypercube remark continues on13; only the complete theorem proof preceding its square and the visible start of that remark were inspected115. No page13 read or inferred credit.

## Exact challenges and their meanings

| Test | Exact check | Outcome and limitation |
|---|---|---|
| Equality family | In F^d, take all 2^d vectors with coordinates0 or1 and cube edges changing one coordinate. Independent directions are the standard basis; each full direction class is a matching. There are d·2^(d−1)=(n/2)log₂n edges. For d=0 use the separate singleton case. | PASS for every field, including F₂. This checks sharpness and normalization, not a sampling proof. |
| Dependence removed only | In R² take (0,0),(1,0),(0,1),(1,1), G=K4, and directions (1,0),(0,1),(1,1),(1,−1). The full direction classes have2,2,1,1 edges respectively; the first two are matchings and the others singleton edges. All points are distinct and every edge covered. Directions are nonzero but dependent. | The weakened theorem is FALSIFIED:6>4=(4/2)log₂4. Independence is essential to this general assertion. This is not a counterexample to4.3. |
| Forest removed | Prior101's Q example u1=1, points0,1,2, G=K3 has all3 edges in one direction and a cycle.3>(3/2)log₂3 because3<4. | Inherited exact forest-free counterexample; re-explained for the contract, not a new discovery115. |
| Natural log substituted | F=Q, points0,1, one direction1 and G=K2 satisfy all graph hypotheses. One edge exceeds (2/2)ln2 since ln2<1. | FALSIFIED altered normalization only. Original base2 bound equals1. |
| Empty and shrinking cases | n=1, k=0, empty graph, isolated vertices, disconnected G, tied largest parts; nonempty R forces at least two smaller components. | Covered by the proof, without skipped membership or log0. |
| Field and dimension | S∩T argument uses independence over the stated F; characteristic2 changes no path identity. V={0} and infinite-dimensional V covered above. | No hidden real/complex-only restriction. |

No mathematical executable, random search, floating point, interval certificate or formal tool was used. Hand-derived controls do not replace the analytic universal proof. There is no failed control requiring the finite theorem to be withheld after the corrected argument; the literal printed step remains failed.

## Claim ledger, consequences and limits

| ID | Object and exact scope | Verdict |
|---|---|---|
| M10-FOREST-EDGE-C115 | Finite4.3 theorem with all specified field, direction, point and graph assumptions | PROVED internally / PASS AT CLAIM CEILING |
| M10-ENTROPY-BOUND-C115 | Inequality(E) for every positive sorted integer partition; also normalized(H) | PROVED internally by two exposed analytic formulations |
| M10-ENTROPY-PRINT-C115 | Literal printed second inequality with remaining-sum coefficient1 at physical11 | FALSIFIED by(2,2,2); source proof step ARGUMENT_INVALID |
| M10-DIRECTION-DEPENDENCE-C115 | Same graph conclusion after deleting only direction independence | FALSIFIED by the exact real K4 configuration |
| Full4.2/unknownN42, Ungar import, complete5.2/countable/global application | Stronger source chain | INCONCLUSIVE / remaining obligations NOT_TESTED115 |
| Current global status, priority, Euclidean value, efficiency | Broader claims | NOT_TESTED / performance NOT_MEASURED |

The changed uncertainty is substantive: the finite graph ingredient is now available with an explicit corrected entropy proof, and a real source error is localized. Repeating a graph grid or rechecking this component is unnecessary without new evidence. The T∩S method transfers to any admissible field, but does not generalize4.2's real-field statement or supply its large-n threshold. Only this named import closes; no downstream parent is automatically promoted.

The new intervening M07 manual review (historical local record; not distributed here) is retained as a separate existing input, not a115 theorem adoption. Its newly asserted biased two-point result and failed stronger extension warrant bounded normalization/custody reconciliation before another M07 search or catalog promotion. The next packet will be selected from the dated whole frontier; no implicit further M10 proof chain is authorized by this success.

## Reproducibility and custody

Source: owned fixedv2 PDF,484598bytes,33pages, SHA25687801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960. The identifier year is not a fresh revision-date attestation. Full text and full renderings of10,11,12 were directly read and cross-checked. Exact register (historical local record; not distributed here) and page ledger (historical local record; not distributed here) bind the source and derived representations. All are rereads: cumulative full text26/33 and full visual21/33 unchanged. Original27–33 remain not fully text-read; prior partial31 retained. Estatepass047 remains155paths=145full+10partial,146recorded hashes,113/428327candidate paths; underlying-source count and volume distinct-content denominator UNKNOWN. No new path, content hash or independent underlying source is claimed.

The reconstruction (historical local record; not distributed here) preserves114's57immutable members and intervening232nd ledger event. Only project-local records are written. No external messages, uploads, publication, foreign-estate writes/execution, agents, installs, purchases, application or automation changes occurred. Detailed run/decision/closeout records accompany the report (historical local record; not distributed here).

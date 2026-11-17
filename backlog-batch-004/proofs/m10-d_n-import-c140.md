# Audited historical reading edition

**Current audited claim:** PROVED: Every finite real-affine-noncollinear n-point set, n>=3, in an arbitrary real vector space has at least n-1 unoriented pair directions.

**Claim ceiling:** Known Ungar import with explicit interface; no direction theorem is applied to F-quotients.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# Ungar's primary proof and the exact M10 direction input — Cycle 140

**PROVED at internal known-result import scope:** for every finite set S of n >= 3 distinct real affine-noncollinear points in an arbitrary real vector space,

    D(S) = { R(x-y) : x,y in S, x != y },     |D(S)| >= n-1.

Directions are one-dimensional REAL linear subspaces: opposite vectors have the same direction. The proof below audits Ungar's original even-planar result, supplies the parity and ambient-space transfers, and verifies the exact M10 consumer interface. No new theorem/novelty, formalization, human review, full source Lemma 4.2/H(d)/Theorem 1.3, current open-status update or Euclidean chromatic result is claimed. Existing downstream conditional records are preserved and are not automatically promoted.

## Primary identity and access

Peter Ungar, *2N Noncollinear Points Determine at Least 2N Directions*, Journal of Combinatorial Theory, Series A 33 (1982), 343–347. The original five-page journal scan is accessible at [this public mirror](https://www.theoremoftheday.org/MathsStudyGroup/Lovegrove-Slope-Problem/ungarpaper.pdf). Local scientific capture (historical local record; not distributed here): 271800 bytes, SHA256 `6f945e7c1f0f8f560870d687e83413a0f47ecea3e0e77d3aed7f0d3eb490b8c0`. Author, journal, volume, pagination, title and embedded PII 0097-3165(82)90045-0 match the native citation. The prior DOI identifier matches that PII; no fresh publisher DOI response is claimed.

All physical pages 1–5 / printed 343–347 were read in text and as full-page images. This is the original article on a third-party host, not a later author's restatement. Its hosting does not constitute independent review, publisher-authenticated delivery, a reuse licence, or a second source. One exact-title search call (two queries) found this new endpoint; one new full-text route succeeded. Neither failed Cycle121 publisher/CiteSeer route was retried. The original source and prior failed records are unchanged. The search stopped after success; there was no wider source crawl.

The mathematical proof used here is Theorem 2, printed 344–346, with the geometric setup on 343–344. The unrelated greedy upper-bound Theorem 1 was read as part of the page extent but is not an imported dependency or separately certified result. References are bibliographic context: their results are not silently assumed to prove the rotating-projection construction below.

## 1. The even permutation lemma: checked central-barrier accounting

Let m >= 4 be even. Start with m distinct objects in increasing label order and end in reverse order. Each move reverses disjoint consecutive increasing blocks; singleton blocks are irrelevant. The entire ordering may not be reversed as one block. Ungar's Theorem 2 says the number q of moves is at least m.

Put a barrier between positions m/2 and m/2+1. In a crossing move exactly one reversed block straddles it. If its lengths to the left and right of the barrier are a and b, set d=min(a,b). Exactly 2d objects cross the barrier. Every object starts and ends on opposite sides, so, writing d_1,...,d_t for the crossing moves in one half-period,

    2 sum_i d_i >= m.                                      (1)

This is a non-strict inequality. The full-page image, unlike a web OCR rendering, shows >=, not >.

Two local facts suffice. An interior object of a decreasing consecutive block cannot be moved by an increasing-block reversal; thus a persistent decreasing block loses at most one position at each end per move. Conversely, an interior object of a newly increasing consecutive block cannot have moved in that move: a moved object has a neighbouring member of its reversed block in descending order. Thus stripping both ends from a new increasing block leaves an increasing block that was already in place before the move.

Immediately after crossing i there is a decreasing central block with at least d_i positions on each side. Immediately before crossing i+1 there is an increasing one with at least d_(i+1) on each side. If g intervening moves did not cross the barrier and g <= d_i+d_(i+1)-2, choose an integer s with 0<=s<=g, s<=d_i-1, and g-s<=d_(i+1)-1. Such s exists exactly because of this inequality. Propagating the decreasing block forward s moves and the increasing block backward g-s moves makes the same central adjacent pair simultaneously decreasing and increasing, a contradiction. Therefore

    g_i >= d_i+d_(i+1)-1.                                  (2)

The wraparound is essential; discarding it would not prove the claimed bound. Each object pair is reversed exactly once in the initial-to-reverse sequence: after an initially increasing pair is reversed it cannot be reversed again by an increasing block. Extend the sequence by reversing every ordering in the next q steps, periodically with period 2q. Each pair now changes order once every q moves. Starting at any cut and relabelling by that initial ordering, the next q moves again reverse increasing blocks. The block locations, crossing condition and d do not depend on the labels.

There are at least two crossing moves per q-step interval: otherwise (1) forces its only crossing block to contain all m positions, which is forbidden. Hence the last crossing and the first in the following interval both fit in some q-step window. Apply (2) in that window after relabelling. This supplies the same gap bound across the cut, with d_(t+1)=d_1. There are exactly q=t+sum_i g_i moves in a cyclic interval, so

    q >= t + sum_i(d_i+d_(i+1)-1) = 2 sum_i d_i >= m.

This verifies the pivotal cyclic step of the primary proof. No generic position, adjacent-transposition-only assumption, or suppression of simultaneous blocks is used.

## 2. Planar configurations: the geometric implication is explicit

For m distinct noncollinear planar points, choose a projection line whose direction is not perpendicular to any point-pair difference, and label points by their initial increasing projected coordinates. Rotate that line through a half-turn. Each pair's projected-coordinate difference has exactly one zero in this open half-turn. Its sign changes there. Thus the final ordering is the initial ordering reversed.

At an event, equal projected coordinates form consecutive blocks just before and after the event; each block reverses. Each pair inside a block has not previously changed its initial relative order, so it is an increasing block in the original labels. Different tie values produce disjoint blocks, including when several parallel lines of points generate the same event. Distinct point-pair directions correspond bijectively to these event angles modulo a half-turn. These are unoriented real lines, not rays, ordered pairs, or slopes with the vertical direction omitted.

A reversal of the entire ordering as one block would mean all points have the same coordinate at one angle, placing them on one affine line, excluded here. Therefore the preceding lemma applies when m is even and m>=4: there are at least m directions. Partial collinearities, multiple parallel ties and other nongeneric configurations are allowed.

## 3. Odd and small n: no hidden deletion assumption

If n>=5 is odd, retain a fixed noncollinear triple and delete a point outside it. The remaining n-1 points are even in number, distinct and still noncollinear, so they determine at least n-1 directions. Their directions are a subset of the original set's directions. Arbitrary deletion would be unjustified: in a nearly collinear configuration, deleting the unique off-line point can destroy noncollinearity.

If n=3, the noncollinear triangle has exactly three different unoriented pair directions; in particular three>=n-1. For even n>=4 the primary bound n is stronger than n-1. Thus every admissible n>=3 is covered, with no appeal to a nonexistent noncollinear two-point set. The claim 'at least n for every n' is false: the four vertices of a square together with its centre give five points but four directions.

## 4. Arbitrary real ambient spaces: direction surjectivity is enough

Translate x_1 to 0 and work in the finite-dimensional real span W of the finitely many differences, even when the original space V is infinite-dimensional. Choose independent differences u,v from a noncollinear triple. A real linear functional a can be chosen nonzero on every nonzero pair difference: in a basis of W, a_t(z)=z_1+t z_2+...+t^(r-1)z_r fails on each fixed nonzero difference at only finitely many t. Avoid the finite union of these root sets.

Then w=a(u)v-a(v)u is nonzero. Choose a real linear functional b with b(w)!=0 and put Tz=(a(z),b(z)). The a-coordinate makes all n image points distinct, while det(Tu,Tv)=b(w)!=0 makes a noncollinear triple survive. The planar image therefore has the same number n of distinct points and is noncollinear.

For every original pair direction Rz, Tz is nonzero. Real linearity makes Rz -> R(Tz) well-defined. Every image pair direction arises this way, so this map is SURJECTIVE. Consequently

    |D(original)| >= |D(planar image)| >= n-1.

Injectivity on directions is unnecessary for this lower-bound transfer. The stronger direction-preserving projection proved internally in122 remains valid; its counterexample to arbitrary direction preservation is also unchanged. For example, the four-point tetrahedron projected to a square merges six original directions into four, but the inequality needed here still has the correct direction. This simpler sufficient transfer is a fresh verification of the import interface, not a reproof or reopening of the retired122 route.

## 5. Exact M10 contract and witness linkage

The fixed cached M10 primary source (historical local record; not distributed here), SHA256 `87801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960`, was checked only at complete physical/printed pages10 and14. Page14's Theorem4.6 uses real one-dimensional subspaces generated by nonzero point differences in a finite-dimensional real space, and requests n-1 directions. Page10's Lemma4.2 allows an arbitrary real vector space V and F subset R, but requires distinct, real-affine-noncollinear points. The finite-span transfer above supplies exactly this extension.

The 125 internally conditional proof (historical local record; not distributed here) uses D_n only to infer k>=n-1 for the original configuration. If a nonzero pair difference z lies in F u_i, then z=c u_i for a nonzero c in F subset R, so it has the same REAL direction as u_i. One label cannot cover two different real directions. Covering all pair differences therefore needs at least n-1 labels. Duplicate or unused labels do not defeat this lower bound; retained labels still cover all differences. We do not apply a real direction theorem to later F-quotients, which need not be real vector spaces. We do not infer F-linear independence from real-direction distinctness.

For the 126 norm-distance consumer (historical local record; not distributed here), suppose S has n distinct points with at most (1-mu)n positive distinct norm distances, 0<mu<1 and n>1/mu. If S were collinear, order its affine parameters t_1<...<t_n. Distances from the first point are the n-1 distinct positive numbers (t_i-t_1)||v||. Thus Delta(S)>=n-1>(1-mu)n, a contradiction. Consequently S is noncollinear and D_n applies. The retained threshold n0=max(N125,floor(1/mu)+1,2) enforces the strict inequality. Equality n=1/mu is insufficient: equally spaced collinear points have n-1 distances.

Each normalized unoriented real direction has a chosen norm-unit representative. A nonzero difference is plus or minus its positive norm distance times that representative. With F generated over Q by these finitely many positive distances, F is a real subfield and every difference is on a labelled F-line. Hence the verified D_n fits the actual original-configuration consumer without a field, parity, normalisation, or noncollinearity mismatch. No new assumption of strict convexity, smoothness, no-three-collinear, or finite ambient dimension is introduced.

## 6. Adversarial result, limits and next decision

Exact convention fixtures (historical local record; not distributed here) check triangle3, square4, square-plus-centre4, tetrahedron6 and projected tetrahedron4 directions using only integers/gcd. They detect oriented-ray doubling, the false all-n stronger assertion, omission of noncollinearity, the unnecessary projection-bijection assertion, threshold equality, duplicates and malformed dimensions. Finite controls are illustrative/falsifying examples, not the universal proof. The general result rests on the analytic arguments above.

The OCR incorrectly rendered the primary >= signs as > at two consequential places; complete page images fixed those readings. Cached M10 text extraction reported missing fontTools for some fonts; no package was installed, and symbols were checked visually. The system interpreter lacked pypdf, so the configured bundled interpreter supplied extraction. No failed mathematical control or silently modified source/certificate was hidden.

**PASS AT CLAIM CEILING / PROVED internally:** Ungar's even-planar direction theorem, the stated n>=3 D_n transfer, and its applicability to M10's actual bad witnesses. The exact original-configuration D_n dependency is discharged. This is a known theorem imported after primary reading plus elementary interface verification, not a newly discovered result. Review is the same exposed actor/model; there was no external human/blind/formal review.

Historical120–139 missing-source/conditional conclusions remain in their original records. This new evidence supersedes the current D_n source hold, not their chronology. The source-search family is closed after this one successful exception. All unrelated paused mathematical routes and corrected scientific-scope controls remain in force. Global M10 status/date, 5–7 chromatic bounds, H(d) and downstream full-source-proof/adoption fields remain unchanged. Updating those would require a separately frozen, justified consumer integration audit of the inherited corrected proof chain. No automatic source/theorem chain or additional search follows this result.

Attempt and continuation justification (historical local record; not distributed here), confirmatory contract (historical local record; not distributed here), adjudication (historical local record; not distributed here), exact inspections (historical local record; not distributed here), report (historical local record; not distributed here). Scientific cumulative content/source/path counts and denominators remain UNKNOWN; legacy mixed-volume figures are not scientific coverage. No excluded source/copy was accessed, and no external write/contact, automation/schedule/notification, other-project/shared-skill change or agent occurred.

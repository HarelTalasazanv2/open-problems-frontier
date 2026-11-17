# Audited historical reading edition

**Current audited claim:** CERTIFIED_RANGE: The pinned v2Lemma4.2proof spans14-16and invokes Ungar4.6before its first k>=n-1step, then quotient forests, weighted selection and the direction-forest bound.

**Claim ceiling:** Dated source/import map only. Later separately reviewed C140/C141 proofs have their own stronger local ceilings.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M10 Lemma4.2: exact source map and first unsupported import

**CERTIFIED_RANGE — source contract and import map only.** The fixed cached v2 proof of Lemma4.2 begins on physical/printed14 and ends on16. All three pages were directly read in full text and full renderings. Its first necessary external input is the direction theorem attributed to Ungar as Theorem4.6/[47] on14. That primary theorem has not been checked in this run. **Full Lemma4.2 reproduction remains INCONCLUSIVE/NO_GO at that import; the full distinct-distance application remains NOT_TESTED.** No Euclidean chromatic bound, new open-problem solution, current-status refresh or novelty is claimed.

This also corrects a native readiness inconsistency: the cycle110 weighted-selection dossier already described proof14–16 in its first30lines, whereas119's current handoff called the span UNKNOWN. The older dossier was hash-pinned but not substantively reconciled during119selection.120 directly checks the PDF and restores the known span in current views; it does not claim to have discovered a previously unrecorded proof location.119's artifacts and all prior manifests remain unchanged.

## Fixed source and direct inspection

Raw source: cached v2 PDF (historical local record; not distributed here),484598bytes,33pages, SHA25687801fbd57539a8371009e8e181c773c51701396519809f2500c525fed331960. The native110context identifies it as arXiv2302.09058v2; this is a fixed-version identity, not a fresh latest-version assertion. No public retrieval occurred.

The frozen attempt (historical local record; not distributed here) allowed15primary minutes, a bounded locator1–18, at most3fulltext-and-visual PDFpages, and at most2native mathematical ingredient contexts. A default-runtime check found pdftotext/pypdf unavailable; the preparation failure (historical local record; not distributed here) was preserved before the attempt. The installed bundled Python/pypdf6.10.0 and Poppler renderer were available, so no installation was needed. No source investigation occurred before the actual method was frozen.

The locator (historical local record; not distributed here) scanned exactly physical1–18 and returned matching snippets, with knownphysical10Lemma4.2canary and missing/duplicate-page controls. Parsing a page is not full reading. Adaptive page selection (historical local record; not distributed here) fixed14,15,16 before full extraction/rendering. The partial statement at physical10lines28–33 and the existential consumer at17lines9–12 were also read; other locator snippets retain their limited extents. All selected PNGs were inspected; fractions, ceilings, subscripts, log terms and footers14–16 were checked against text. No OCR, source-code/TeX execution or mathematical numerical instrument was used.

## Exact source statement and quantifiers

The literal statement at physical10, read here as a partial text range and previously text/visually checked114, has this scope:

- Integer d>=1 and real0<mu<1. There is a sufficiently large n threshold depending on d,mu.
- F is a subfield of R; V is a real vector space. The proof uses F-linear spans inside this real ambient space.
- A finite labelled list u1,...,uk of nonzero vectors and n distinct points p1,...,pn in V. The points are not all on a common **real affine line**. The source does not impose independent directions at the initial stage.
- Every difference px-py belongs to F ui for some label i.
- There is I subset[k] such that the number of **labels** ell with u_ell in span_F(u_i:i in I) is at least d|I|+(1-mu)n+1.

Thus the source assertion is uniform over F,V and the labelled configuration once n is sufficiently large for the fixed pair(d,mu). It is not an assertion over arbitrary abstract fields, merely F-noncollinearity, or an individually normalized list. These domain distinctions must survive any local reproduction.

The proof uses the integer m=ceil((1-mu)n)<=n. Under the contrary assumption, every I has at most d|I|+m labels in its closure. Integer rounding is material: a count below d|I|+(1-mu)n+1 is at most d|I|+ceil((1-mu)n). The subsequent goal d|I|+m+1 is consistent with the literal source statement. This is a transcription/alignment check, not a new proof of the conclusion.

## Complete inspected proof span and dependency map

| Span | Source role | Evidence status120 |
|---|---|---|
|14, before the proof | Theorem4.6/[47]: a real affine-noncollinear finite point set in R^t determines at least n-1 real line directions. The source notes an even-n strengthening. | Literal statement directly text/visually checked. Primary Ungar statement/proof/publication identity not checked; AS_REPORTED, necessary HOLD. |
|14, proof start | Set m, negate the desired label-closure conclusion, discard unused direction labels. | Directly inspected source construction; no complete local theorem adoption. |
|15, beginning | Apply4.6 to obtain k>=n-1, then choose successive direction labels with a forest of at least3d/muedges after quotienting. | The first inequality depends on the unresolved direction theorem. |
|15, Claim1 | Each chosen forest collapses at least3d/mupoints in the quotient, so r<=mu n/(3d). | Directly inspected internal source step. |
|15–16, Claim2 | If the terminal quotient has too few points, a small label set spans all used direction labels; k>=n-1 then contradicts the negated closure bound for large n. | Depends again on the Ungar-derived k bound and on large-n rounding. |
|16 | Maximal direction forests on h=|H_r| representatives have weights0<=lambda_i<=3d/mu. Pair counting yields sum lambda_i>=mu h^2/(24d). | Directly inspected source construction/inequalities. |
|16 | Apply weighted Lemma4.5 with M=3d/mu and the negated closure assumption, obtaining an F-independent J and a quadratic lower edge bound after large-n absorption. | Matches the explicit native110statement at its pinned scope. |
|16, end | Union the forests for J. Independence separates their directions, so Lemma4.3 gives at most(1/2)h log_2 h edges, contradicting the quadratic lower bound for large h. | Matches native115forest statement. The source proof closes on16. |

No bibliography page outside the locator bound was inspected. The exact primary bibliographic identity of[47], its parity convention and its original ambient dimension remain unresolved here. In particular, seeing a precise theorem quoted in a later paper is not primary-source verification of that theorem.

The source uses Theorem4.6 in the finite real span of the points, which has dimension at most n even if V is infinite-dimensional. A future primary check must establish the needed arbitrary finite-dimensional statement or explicitly justify any passage from a planar statement. Neither step is silently imported in this source map.

## Existing local ingredients: statement matches, no reproof

Two native contexts were directly read at exact partial ranges:

1. 115forest-edge dossier (historical local record; not distributed here), lines1–25/140, pinned SHA256ddee7a63c18b929c1384b2f30e683bb89dd063b51a2bdc9fca359824ffbc107a. Its established contract is any field, an independent finite direction list, distinct points and a finite simple graph whose all-eligible edges in each direction form a forest; then |E|<=(n/2)log_2n. The inherited proof is ARTIFACT_VERIFIED, and its statement was reread; it was not independently reproved120. The old printed4.4failure and the separately corrected entropy proof remain distinct and unchanged.
2. 110weighted-selection dossier (historical local record; not distributed here), lines1–30/131, SHA25677fa46d8fb127b5004e5a09e553eebc207b11e142359a2ec7e4a45c2d98b0b61. Its contract retains labelled/repeated nonzero vectors, every-subset closure bound <=d|I|+m, and0<=lambda_i<=M. It gives an independent J with weight at least(sum lambda_i-mM)/d. These are the quantities used on source16. No external matroid-partition theorem or fresh reproduction is required merely to match that previously proved native ingredient.

These two known ingredients do not establish the missing geometric direction bound, all of the intervening4.2argument, or the final application. Matching an input contract is a readiness fact with a limited ceiling.

## Threshold and source-index findings

The source pages14–16 do not supply a numerical N42. They invoke sufficiently large n depending on d,mu at three kinds of steps:

- The Claim2contradiction uses n-1>=2mu n/3+ceil((1-mu)n)+1.
- Pair counting and absorption use h>mu n/(3d)>=2 and n(3d/mu)<=(3d/mu)^2h<=(mu/(48d))h^2.
- The final step requires (mu/(48d^2))h^2>(1/2)h log_2h for sufficiently large h, with h>mu n/(3d).

These identify the source's threshold obligations; this run does not optimize them or invent a numeric bound. The partial source consumer at17lines9–12 explicitly chooses n0(d,mu)>1/mu so Lemma4.2holds for all n>=n0(d,mu). At that displayed interface an existential uniform threshold in(d,mu) is used. A complete application still requires its own proof and parameters; the four lines are not a full Theorem1.3/5.2audit or a theorem for every positive mu.

There is a literal index inconsistency in Claim2on15: the earlier pruning on14takes witnesses x,y in[n], but the later sentence quantifies its p-index witnesses in[k]. Both the extracted text and full image show[k] on15. A full reproduction must explicitly return to the earlier[n]witness property or otherwise justify its range. This finding is recorded as an index/transcription obligation, not as a counterexample to Lemma4.2or a repaired proof silently adopted here. For h=h* the zero difference likewise needs an explicit harmless convention when choosing the auxiliary label; no full route is promoted on that basis.

## Readiness reconciliation and stopping decision

The reconciliation record (historical local record; not distributed here) records the operational defect, consequence and acceptance test. **Defect:**119's UNKNOWN proof-span field lost the explicit older110location evidence. **Consequence:**the next packet allocated a repeat locator despite a known native location. **Minimal repair:**preserve119 and110 unchanged, append this correction, and update the native current views with verified14–16plus its evidence anchor. **Acceptance:**the current queue, M10root, dependency node and next-readiness record must all retain14–16; a stale UNKNOWN or automatic full-theorem promotion must be rejected by the focused record checks.

The source/import gate now has a precise result:

| Object | Outcome | Ceiling / next gap |
|---|---|---|
| M10-FULL42-IMPORT-MAP-C120 | CERTIFIED_RANGE | Fixed cached source: statement/complete proof span14–16/import/threshold map, exact selected reading. |
| M10-PROOF-LOCATION-RECONCILIATION-C120 | CERTIFIED_RANGE | Prior110record and direct120PDF agree; current readiness restored, prior artifacts unedited. |
| M10-UNGAR-DEPENDENCY-C120 | INCONCLUSIVE / NO_GO | Quoted4.6not primary-verified; exact[47]identity/domain/parity and required ambient extension unclosed. |
| Full4.2 / field-span consumer | INCONCLUSIVE | Necessary external import unverified; source index/whole-proof checks also remain for reproduction. |
| Full5.2/countable distinct-distance application/global Euclidean value | NOT_TESTED | No promotion from source inspection or two known finite ingredients. |

The attempt stops at that essential import. No external retrieval or automatic source chain occurred. The whole-frontier reconsideration (historical local record; not distributed here) must decide any next gate from this actual outcome. A later Ungar check needs its own bounded primary-source identity/domain contract and stop rule; it is not execution authorized by this dossier alone.

## Corpus, custody and independence

Exact inspections (historical local record; not distributed here), the page ledger (historical local record; not distributed here) and reading ledger (historical local record; not distributed here) bind the raw PDF, three complete text/visual representations, partial snippets and two native context ranges. There are3direct local mathematical paths, all partial as whole documents, with3recorded whole-file hashes in that named set. Eighteen locator-parsed pages are not18full direct readings. The3fulltext/visual pages14–16are rereads, so no new PDFpage coverage is claimed. The current source-map/reconciliation information is useful despite zero path/page increment.

Estatepass047 remains155paths145full/10partial,146recorded hashes;113/428327candidatepaths107full/6partial, underlying-source count and volume distinct-content denominator UNKNOWN. M10original26/33fulltext/21/33fullvisual, Cook10/12and other extents are unchanged. The selected PDF and native lemmas share a primary lineage; no independent-source increment or independent human review is claimed. Same actor/model/expected inputs/platform were exposed. No mathematical performance comparison was measured.

Memory supplied only a packet-specific provenance/scope reminder and no M10fact; current conclusions use the pinned native evidence and inspected PDF. Source estates and installed skills were not modified. No agent, public request, external message/upload/publication, foreign-estate write/source execution, installation/account/purchase, app/schedule/notification change or unmanaged continuation occurred. The run report (historical local record; not distributed here) records integration and checked closeout separately from the held mathematical theorem.

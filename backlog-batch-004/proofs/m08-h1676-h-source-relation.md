# Audited historical reading edition

**Current audited claim:** CERTIFIED_RANGE: For the exact pinned payload records and the displayed mathematical translations, each reconstructed matrix at orders [1676] is Hadamard and matches its pinned mirror under the declared row/column sign map; raw equality is false.

**Claim ceiling:** Specified selected seed-derived mathematical translations, not execution of the downloaded program, general builder validity, author/account authentication, priority or independent-source corroboration.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# H1676: bordered h source relationship

**Outcome: CERTIFIED_RANGE.** One specified original-linked source-seed construction has signs ±1, satisfies HHᵀ=1676I, and matches the pinned mirror under the frozen row and column sign changes. Raw equality is false for these two representations. Finite existence at order 1676 was already certified in cycle029. This closes one data relationship; it establishes no new order, general h theorem, universal Hadamard result, authorship, priority, novelty, human review or formal verification.

## Frozen claim and source custody

The frozen contract (historical local record; not distributed here) precedes execution. It pins twelve inputs and fixes the selected record, border, indices, period requirement, arithmetic, controls, comparison and stopping rule. The pre-run derivation (historical local record; not distributed here) reviews the parameter-dependent assumptions of cycle039's h construction.

The reviewed OPF parser extracts saved headings as inert data, verifies all twelve ordered headers and consumes all 23,828 payload symbols. Only record7 is constructed: +++ dispatches to h without g's deletion argument; it consumes 1,672 signs at zero-based half-open payload interval [14044,15716), with no auxiliary segments. The 1,672 signs form a core seed, not the complete 1,676-square matrix.

The target is `artifacts/hadamard_august_ten/hadamard_1676.csv.gz`: 555,166 bytes, SHA256 `3bb48b0014d144c376a0c6a2ba15e59757067c7dc070d8ee886f33dabd1bb0f1`, Git blob `dba3130fa9dae9c2c58dab40bd13b8b30da23648`, hoa64 commit `d825201089123126ce792d4921cba4ae1b8977a3`. Size and blob match the previous batch manifest. Its old finite certificate is not evidence for this newly tested source relationship.

## Source derivation and period

Inert source1–32 and172–178 were reviewed. Source12's integer values are n/8=209 and n/4−1−n/8=208. Their sum417 plus the final character gives a 418-sign word. Both split lengths are positive; no empty-capture exception is used. Four words A,B,C,D give a 1,672-square core. Let their circulants have entry X[i,j]=word[(j−i) mod418], and let R reverse columns. The core is

[[A,BR,CR,DR],[-BR,A,DᵀR,-CᵀR],[-CR,-DᵀR,A,BᵀR],[-DR,CᵀR,-BᵀR,A]].

Lines13–16 generate the four corner rows and constant top blocks using all-plus/all-minus captures. Lines17–24 arrange held data A,rev(D),rev(C),rev(B),two line breaks,BCD. Lines25–28 give core prefixes and the four rotation directions. The rest-plus-first captures produce left shifts, giving the three core indices (j−i), (417−j−i), (i+j+1) modulo418. The frames fixed by those literal source signs are

P=[[-1,1,1,-1],[1,-1,1,-1],[1,1,-1,-1],[-1,-1,-1,-1]],
T=[[-1,-1,-1,1],[-1,-1,1,-1],[-1,1,-1,-1],[1,-1,-1,-1]],
C=[[1,1,1,-1],[-1,-1,1,-1],[-1,1,-1,-1],[1,-1,-1,-1]].

The complete matrix is [[P,T⊗ones(1,418)],[C⊗ones(418,1),core]]. In particular C and T differ in their first rows. Equating them is an invalid shortcut. Four border rows/columns give order4+4·418=1676. The four seed sums are exactly [2,0,0,0], as predicted from border orthogonality; that invariant alone does not prove validity.

The source loop stops when the entire current row returns to its duplicate initial row. A common rotation period must divide 418=2·11·19. All proper divisors—1,2,11,19,22,38,209—were checked and excluded as common periods. Each actual source word individually has period418. Reversal, shifts, signs and word permutations preserve the common period, so each core group emits exactly418 rows. This is a checked fact about this seed, not an arbitrary-input h theorem. Structure record (historical local record; not distributed here).

## Exact construction, certificate and map

The constructor (historical local record; not distributed here) adapts cycle039's NumPy circulant/block assembly to the new seed and order. The consumer (historical local record; not distributed here) adapts its separate scalar index rule without importing the constructor. Every one of 2,808,976 entries agrees: 2,795,584 core and 13,392 border entries. Strict row/sign membership is checked.

For all 1,403,650 unordered distinct-row pairs, the integer XOR/popcount distance is838. Their dot products are therefore1676−2·838=0. Signs and lengths give diagonal norms1676, proving HHᵀ=1676I for this matrix. A full signed-int64 Gram calculation agrees on all 2,808,976 cells; absolute dot products are at most1676, excluding overflow. There is no floating-point tolerance.

Candidate serialized SHA256: `8e919c2bdb4d30c34817eb5650d2dd3d82d7c6504feccd96c5ca22a2191cdb99`. Raw equality first fails at (0,0), candidate−1 versus target+1. The only permitted next comparison succeeds at every cell:

target[i,j]=H[i,0]·H[0,0]·H[i,j]·H[0,j].

The complete row and column signs are stored in the certificate (historical local record; not distributed here). Diagonal sign changes preserve the Hadamard identity. No permutation search or amended map was used. Reconstruction receipt (historical local record; not distributed here).

## Challenge and independence

Twenty-nine controls pass: known H4; missing/duplicate rows; bad signs; core-only dimensions; missing/changed seed; all seven proper common-period fixtures; incorrectly equal top/left frames; actual corner damage checked by both Gram and formula; final-core damage; omitted-final-row completeness; wrong/missing row and column signs; a valid row permutation rejected by formula and fixed map; wrong tail/full reversal and transpose-reverse offset; prior numeric-header inversion regression; seed sums and border membership.

A deliberately incomplete checker accepts the last-cell-damaged matrix after 1,401,975 pairs. The expected full count1,403,650 detects 1,675 omitted pairs. A row permutation can remain Hadamard while failing the declared source/map ordering. These controls address selected plausible faults, not all code behavior. No current mandatory control failed and no repair or interpretation amendment was needed. Earlier failures, including the cycle043 closeout oracle, remain in their sealed records.

This run adapts the existing039 algorithm families. It does not introduce newly independent mathematical methods. Both implementations share source, seed, mathematical model, platform, reviewer and target exposure;038 parsing/strict reader/bitset/map functions are reused. The block versus scalar/bitset paths check implementation mistakes but do not constitute blind reproduction, external human review or formal verification. No method speedup is measured.

## Source inspection and coverage

Exact extents (historical local record; not distributed here) record direct inspection of all1,672 selected signs as four418-sign words and inert source1–33/172–178 (g33 is orientation only). The full payload/header membership and both matrices are computationally checked, not visually read as millions of entries. Surrounding saved HTML remains partial. Downloaded code stays inert; only OPF-native code and installed dependencies execute.

Both current X URLs returned403. Saved capture hashes support local custody, not account authentication. Partial current [OEIS](https://oeis.org/A007299) inspection retains twelve named August former-gap orders and the original link. [Epoch](https://epoch.ai/frontiermath/open-problems/hadamard) retains solved668/global-open status alongside its stale smallest-unknown668 background sentence. This bounded check establishes no exhaustive current gap list, least unresolved order or priority.

There are zero new other-volume paths. Pass035 remains138 direct paths,128 full/10 partial,129 recorded whole-file hashes including partial reads;105/428,327 heuristic candidates,99 full/6 partial;33 noncandidate paths,29 full/4 partial,denominator UNKNOWN. Five duplicate groups span14 paths. Estates sampled:73/75 candidate-bearing and5/60 accessible zero-candidate. Underlying-source count and the volume distinct-content denominator remain UNKNOWN. The unchanged2026-10-14 metadata census counted2,330,261 non-directory entries across308,425 attempted directories;it is not a current content census. Four inaccessible system directories,archive interiors and symlink targets remain gaps. Verified equivalence adds no independent source or extra volume reading.

## Learning and next action

Current relationships (historical local record; not distributed here) preserve043 as predecessor. Nine/twelve are verified:668,716,892,1132,1244,1388,1436,1676,1916. Earlier eight are inherited artifact-verified,not recomputed044. Three remain1772,1948,1964. The ten-order batch is7/10 mapped,3/10 unresolved. The finite-order set is unchanged.

The new uncertainty resolved is the selected1676 seed's source/mirror relationship and its parameter-dependent h border/period assumptions. Raw equality,equal frames,wrong reversal/offsets and shorter loops are rejected for this contract. The reviewed model transfers after those checks; it does not automatically certify another record. Repeating1676 pair checks without changed evidence has little decision value.

**Next:** H1772's remaining h relationship (historical local record; not distributed here),SELECTED_NOT_TESTED. Record8 contains1,768 signs[15716,17484);check its442-sign words,221/220 split,borders and all proper common-period divisors before adapted construction and a newly frozen map. It can close the last h-family dependency. No1772 seed inspection or construction ran044. M07 local routes remain internal and nearby grids paused;no global promotion.

For later reproduction copy the entire044 artifact directory to a fresh sibling under OPF artifacts,then run reconstruct.py and verify.py with the bundled Python3.12.14/NumPy2.3.5 and-B. Preserve sealed originals. No downloaded/source-estate program,generic interpreter,agent,external message,upload,publication,mailbox draft,purchase,account,app,schedule or notification change occurred. Public read-only retrieval occurred.

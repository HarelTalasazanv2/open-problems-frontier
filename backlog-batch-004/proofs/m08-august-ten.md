# Audited historical reading edition

**Current audited claim:** CERTIFIED_RANGE: There exists a real sign Hadamard matrix at each of the exact orders [892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948, 1964].

**Claim ceiling:** Final objects only. Historical construction details remain context; no new order, priority, complete gap census or universal Hadamard theorem.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M08: ten exact finite witnesses from the August source-reported list

**Claim ceiling:** `CERTIFIED_RANGE` for the existence of a real Hadamard matrix at each order in `{892,1132,1244,1388,1436,1676,1772,1916,1948,1964}`. The universal Hadamard conjecture, least currently unresolved order, comprehensive internal coverage through 2000, original-author equivalence and priority remain unestablished.

## Source and frozen contract

[OEIS A007299](https://oeis.org/A007299) names the twelve formerly unconstructed admissible orders through 2000, and [Epoch's order-668 owner page](https://epoch.ai/frontiermath/open-problems/hadamard) reports their August 2026 construction; its old 668-smallest background sentence is stale. The frozen attempt contract (historical local record; not distributed here) set the exact ten-order membership before retrieval. A GitHub API listing of [`bbeartheancient/hoa64` at commit `d825201089123126ce792d4921cba4ae1b8977a3`](https://github.com/bbeartheancient/hoa64/tree/d825201089123126ce792d4921cba4ae1b8977a3/matrices) contained exactly the ten named fixtures, alongside 668, 716 and 1852. The pinned manifest (historical local record; not distributed here) records all names, sizes, Git blob IDs and immutable URLs; the received 4,703,752 compressed bytes matched every size and blob ID. Per-file SHA-256 and 62,205,516 expanded bytes appear in the batch certificate (historical local record; not distributed here). No upstream code was executed.

The mirror [README at that commit](https://github.com/bbeartheancient/hoa64/blob/d825201089123126ce792d4921cba4ae1b8977a3/README.md) calls these twelve Alpöge-order CSVs ingested on August 12, and separately says H(1212) and H(1940) exist but their construction data are inaccessible to that repository. Those are mirror-author statements, not independently verified author-to-mirror lineage or a complete current order census. Original announcement/release identity remains unresolved.

## Exact tests and adversarial controls

The OPF checker (historical local record; not distributed here) required exact batch membership, strict newline/CSV grammar, `n×n` shape and `±1` bytes. For each `n`, it checked every unordered pair of distinct rows has exact Hamming distance `n/2`; all row norms equal `n`. This is precisely `HHᵀ=nI`, hence an existence witness. Total distinct pairs checked: **12,434,956** across ten matrices. Individual counts and full hashes are in the batch certificate. Selected integer dots were zero for every order. Missing, duplicate, extra and misnamed membership controls; missing/short/nonsign row controls; corrupt/truncated gzip controls; and one-sign mutants for every order were rejected. An initial attempt under the system's Python 3.9.6 stopped before any certificate because `int.bit_count` was unavailable. The frozen instrument ran successfully with bundled Python 3.12.14; this environment failure is preserved as a failed execution, not mathematical evidence.

After the primary pass was known, a separate confirmatory contract (historical local record; not distributed here) specified a NumPy CSV parser and signed-int64 check (historical local record; not distributed here). Its receipt (historical local record; not distributed here) has four direct integer dots for each order, all zero, and the full **795,664-cell** Gram comparison at H(892), plus a rejected one-sign mutant. A dot's absolute value is at most 892 there, so int64 overflow is impossible. This second method shared the same source and model and was **not blind**; its complete Gram scope is H(892) only. No external mathematical review occurred.

## Decision update

These exact checks retire the ten named finite instances as project obligations. Together with prior internal H(668) and H(716) checks, OPF has checked the exact twelve-order set named by OEIS. It has **not** independently enumerated or reproduced all admissible orders through 2000; the mirror itself flags H(1212) and H(1940) as known without data available there. The next high-value action is to locate the primary construction evidence and checkable witnesses, or authoritative proof routes, for 1212 and 1940 while resolving the August author-release-to-mirror identity. Repeating the ten matrix tests would add little discrimination absent changed bytes or a specific checker defect.

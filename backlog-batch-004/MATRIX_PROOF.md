# Exact finite sign-matrix implication

For a real n-by-n matrix H whose entries are exactly +1 or −1, each row has squared norm n. If two distinct rows differ in h positions, their dot product is exactly n−2h. Thus checking all n(n−1)/2 unordered row pairs and requiring n−2h=0 proves HHᵀ=nI. Since H is square and n>0, H is invertible, so HᵀH=nI as well. No floating tolerance, sample, spectral residual or extrapolation is involved.

[MATRIX_AUDIT.json](MATRIX_AUDIT.json) checks the exact fifteen-witness membership and all 20,118,294 required pairs. Six historical existence records refer to that finite evidence; they are not six independent mathematical constructions. A known H4 and malformed-input, odd-order, duplicate-row and one-cell-damage controls challenge the actual checker.

For the ten specified seed-derived matrices, [relation_check.py](relation_check.py) implements the closed scalar index formulas of the linked proof reading editions, consumes all declared source segments, verifies the actual common periods, and checks every source/mirror cell under the single declared sign map. [RELATION_AUDIT.json](RELATION_AUDIT.json) covers all 24,602,272 source/map cells and 12,293,540 row pairs. Row and column sign multiplication preserves orthogonality; exact mapped equality is an additional data-relationship statement, not authenticated authorship or source-runtime equivalence.

The C166 CSV uses the same dot-product implication and separately checks all column pairs: [CSV668_AUDIT.json](CSV668_AUDIT.json).

All exact inputs are hash-bound and [supplied separately](EXTERNAL_INPUTS.md). Original constructors and data contributors retain credit in [REFERENCES.md](REFERENCES.md). No new order, priority, complete least-gap census or universal Hadamard theorem follows.

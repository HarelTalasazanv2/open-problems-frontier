# Automated verification

Run from a clean repository checkout with Python 3.12 and its standard library:

```sh
python -B -m unittest discover -s scripts -p test_verify_all.py -v
python -B scripts/verify_all.py
python -B -O scripts/verify_all.py
python -B -OO scripts/verify_all.py
```

GitHub Actions runs the same contract tests and all declared self-contained checks in normal, `-O` and `-OO` modes on pushes, pull requests and manual dispatch. The checkout and Python setup actions are pinned to the commits inspected on 2026-11-16. Permissions are limited to reading repository contents; the workflow installs no project dependencies and sends no research data elsewhere.

A successful default job means all 14 declared self-contained certificate replays and the file/index checks passed. The index contains 118 historical claim records: 51 analytic-proof, 37 mixed, four finite-certificate, 19 external-input-required and seven source-contract records. Several records share evidence and checkers; these are not counts of independent theorems. Analytic arguments and source assertions are not proved by the runner.

Four tasks require separate inputs: one graph seed, the 15 final Hadamard matrices, the selected source relationships, and the order-668 CSV. Default CI reports each as `MISSING_EXTERNAL_INPUT`, and `all_declared_replays_verified` stays false. Green CI does not mean these tasks were replayed, or that analytic proofs, novelty or global conjectures were machine-verified.

To require every declared replay, obtain the exact inputs under applicable permissions and follow the [external-input inventory](backlog-batch-004/EXTERNAL_INPUTS.md), then run:

```sh
python -B scripts/verify_all.py --external-seed /absolute/path/to/authorized-seed.g6 --matrix-root /absolute/path/to/authorized-matrix-inputs --require-external
```

The checker downloads nothing. A graph seed cannot discharge a matrix-input obligation, or conversely. Missing required input, a wrong input, a missing checker, an invalid certificate, a timeout, a nonzero child exit or a mismatched success contract produces a failing exit. Optional `--report NEW_FILE.json` saves the observed machine-readable result without overwriting an existing report. Normal, `-O` and `-OO` modes propagate to every child checker.

[RESULTS.md](RESULTS.md) explains each exact claim and its scope. [RESULTS.json](RESULTS.json) distinguishes analytic proofs, finite certificates, mixed arguments and external-input packages. [VERIFICATION_PLAN.json](VERIFICATION_PLAN.json) fixes checker membership, arguments and success contracts. [VERIFICATION_MANIFEST.json](VERIFICATION_MANIFEST.json) checks byte custody; editing both a file and its manifest is not independent proof of correctness.

Each mathematical consumer retains its own finite membership and invalid-input controls. The runner tests address execution and failure propagation. Neither set constitutes exhaustive software assurance, formal verification or independent expert review. Credit and source roles are in [REFERENCES.md](REFERENCES.md) and [ATTRIBUTION.txt](ATTRIBUTION.txt).

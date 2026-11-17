# Exact typed inputs: now included for reproducibility

The four input-dependent tasks keep their original strict input contracts. Their exact21 data files are now delivered in the repository's [versioned bundle](../verification-inputs/INPUTS.json), with [source references and credit](../verification-inputs/REFERENCES.md). This supersedes the earlier output-only delivery limitation, not the historical byte identities or mathematical statements.

From the repository root:

```sh
python -B scripts/prepare_inputs.py --output .verification-inputs --report input-report.json
python -B scripts/verify_all.py --matrix-root .verification-inputs/matrices --external-seed .verification-inputs/graph/seed.g6 --require-external --report verification-report.json
```

The output directory and reports must be new. All18 tasks must finish successfully; `--require-external` rejects a missing input. The materializer performs no download and never executes archive contents. See [full verification instructions](../VERIFICATION.md).

The15 final matrix objects retain their compressed/expanded hashes in [MATRIX_INPUTS.json](MATRIX_INPUTS.json). The10 selected source relationships retain all four exact capture/derivative hashes in [RELATION_INPUTS.json](RELATION_INPUTS.json); all12 payload records and23,828 signs remain required. C166 retains its exact1,115,894-byte CSV hash. The graph task retains its independent exact145-byte record hash excluding its saved newline. A valid alternative matrix or graph is not accepted as a replacement.

Directly invoking the mathematical runner without prepared inputs still produces an explicit missing-input state. Hosted CI now always prepares the bundle and requires all18, under normal,-O,-OO. Original-source and third-party-rights qualifications remain in the references; this delivery change is not a new license, account-authentication or novelty claim.

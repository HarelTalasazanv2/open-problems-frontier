# Reproduce all18 declared replay tasks

A clean checkout includes the exact21data files required by the four input-dependent tasks, in a versioned archive. The materializer checks the archive, complete member identities, sizes and SHA256 hashes before making a fresh data directory. Captured source and decoder text remain inert.

Run with Python3.12 and its standard library from the repository root:

```sh
python -B -m unittest discover -s scripts -p 'test_*.py' -v
python -B scripts/prepare_inputs.py --output .verification-inputs --report input-report.json
python -B scripts/verify_all.py --external-seed .verification-inputs/graph/seed.g6 --matrix-root .verification-inputs/matrices --require-external --report verification-report.json
```

The report files and output directory must be new; the tools refuse to overwrite them. A repeat can use new report names and reuse the already verified data directory. To test another optimization mode, use `python -B -O` or `python -B -OO` for both commands, selecting fresh report names. Child checkers inherit the selected mode.

GitHub Actions runs the runner/input contract tests, materializes the frozen inputs in a fresh checkout, and **requires all18 replays** in each of normal, `-O` and `-OO` modes. There is no missing-input success fallback in the workflow. A successful full run reports `DECLARED_REPLAYS_VERIFIED`,18 `VERIFIED_REPLAY` rows, zero failed/missing tasks and `all_declared_replays_verified=true`. Checkout and Python setup actions remain pinned; permissions are read-only. No source program from the archive is imported or executed, and no external input download or secret is needed.

Calling `verify_all.py` directly without its data arguments still explicitly reports missing inputs. `--require-external` makes that incomplete run fail. Keeping this direct-call behavior preserves the distinction between missing data and a mathematical counterexample.

The18 tasks consist of14 self-contained consumers and4 typed-input consumers. The input origin remains external to each individual historical package, but the required bytes are now included at the repository level. The [input inventory](verification-inputs/INPUTS.json) and [source references](verification-inputs/REFERENCES.md) identify every supplied object. No scientific statement, output certificate or mandatory task was changed to create this reproduction path.

[RESULTS.md](RESULTS.md) and [RESULTS.json](RESULTS.json) retain118 historical claim records. These comprise51 analytic-proof,37 mixed,4 finite-certificate,19 external-input-required and7 source-contract records; several share checkers. The19 record labels describe their historical evidence dependency, now satisfied for CI by the frozen bundle. This is not118 new or independent theorems.

The runner checks [complete record membership](PUBLISHED_RECORD_IDS.json), [task contracts](VERIFICATION_PLAN.json) and [file byte custody](VERIFICATION_MANIFEST.json). Green CI does not machine-prove analytic arguments, imported theorems, source authenticity, novelty or global conjectures. Concrete defects and their exact affected statements are assessed in [REVIEW_FINDINGS.md](REVIEW_FINDINGS.md). Credit and original source roles remain in [REFERENCES.md](REFERENCES.md) and [ATTRIBUTION.txt](ATTRIBUTION.txt).

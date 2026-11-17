# Exact external inputs

The public package contains project proofs, checkers, lossless output certificates and input identities. Raw third-party data and source captures are supplied separately. Default CI explicitly reports the matrix/source checks as `MISSING_EXTERNAL_INPUT`; it does not claim to have replayed them.

For the fifteen final witnesses, put the exact gzip files at the filenames in [MATRIX_INPUTS.json](MATRIX_INPUTS.json) in one folder. Each compressed and expanded hash must match. The checker accepts no replacement matrix merely because it is Hadamard at the same order.

For the ten source relationships, the same folder also needs the four exact files named in [RELATION_INPUTS.json](RELATION_INPUTS.json): the saved announcement HTML, decoder-reply HTML, payload-sign derivative and inert decoded-program derivative. They are parsed as data. The decoded program is never imported, evaluated or executed. The twelve headers and all 23,828 signs must be present, even though only ten selected matrices are reconstructed.

For C166, add the exact `H668.csv` to that folder: 1,115,894 bytes, SHA256 `5eaef5f4c814469a1f0815756876b83e8c4944ff7ccf4f023ee479de5e8f9a8b`. The checker tests the canonical sign encoding and every row/column pair.

From the repository root:

```sh
python3 -B scripts/verify_all.py --matrix-root '/path/to/exact matrix inputs'
```

The separate graph-seed tasks still require their own exact graph input. To require every declared replay, supply both independent inputs:

```sh
python3 -B scripts/verify_all.py --matrix-root '/path/to/exact matrix inputs' --external-seed '/path/to/exact seed.g6' --require-external
```

These are user-supplied data paths, not files claimed to be distributed in the repository. No network download, permission bypass or automatic acquisition is performed. Missing or wrong inputs remain a missing-input state or a failed check, respectively. References describe the source lineages and their unresolved authentication/redistribution limits.

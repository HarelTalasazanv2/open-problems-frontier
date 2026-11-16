# Open Problems Frontier: Cycle 197 audit

This package contains three precisely scoped results:

| ID | Outcome | Scope |
|---|---|---|
| C197-685 | PROVED | The 17-vertex graph exclusion stated in [PROOF.md](PROOF.md). |
| C197-CAPACITY | CERTIFIED_RANGE | All 50 supplied representatives x six vertices; only 685 satisfies the strict single-vertex obstruction. |
| C197-CENSUS-REVIEW | CERTIFIED_RANGE | All 32,768 six-vertex masks, 22,484 admissible masks and 84 complete permutation orbits. |

The remaining 49 classes/14,872 labeled neighborhoods remain unresolved. The prior 50-class list is an explicit input, not a claim that this package re-proves every earlier exclusion.

- [Proof and scope](PROOF.md)
- [Exact certificate](data/certificate.json) and [full model](data/model.json)
- [Finite audit](data/audit.json), [source orbits](data/source_orbits.json), [prior list](data/prior_residual.json), [updated list](data/residual.json)
- [Fresh read-only checker](verify_v2.py) and [observed verification](verification_result.json)
- [Original-source identities](source_identities.json)
- [References and credit](REFERENCES.md) and [attribution text](ATTRIBUTION.txt)

## Reproduce

From this directory, using Python 3.10 or newer and the standard library:

```sh
python3 -B verify_v2.py
python3 -B -OO verify_v2.py
```

Each command reads the seven data files and prints a result. Neither installs dependencies nor writes research artifacts. The checker reconstructs the relevant matrix, uses exact Fraction arithmetic, enumerates the complete six-vertex census and orbit memberships, and challenges 17 selected invalid inputs. A zero-margin case is retained as a boundary control. These controls are not exhaustive software assurance.

The checked runtime was Python 3.12.14. The review's first checker mistook an explicit census membership list for a count and rejected it. That failure and version were preserved locally; v2 corrects the schema interpretation and adds missing/duplicate list-member controls. Original Cycle 197 artifacts were not edited.

Verification here is a fresh implementation with shared inputs and exposed expected conclusions. GitHub source inspection supplied definitions and review guidance; it did not supply an external review or a Lean proof of C197. Physics empirical verification and all earlier unreviewed project claims are outside this package.


# Explicit corrections and failed instruments

## Historical C034 rotation comparison

The main Hessian derivation uses `C=i/d` and correctly obtains, at scalar stationarity,

`r^2 k'' = pq[(r+1)d - (r/a)i]/(2d^2)`.

The original Section7 recovery paragraph instead printed `H_old=(r+1)d-2(r/a)i` in that comparison. The extra factor2 is incorrect. Its asserted right side is too small by `pq*r*i/(2*a*d^2)>0` for the stated nontrivial stationary ratio. C018's original rotation formula has the correct single coefficient.

The main Theorems1/2 do not depend on the erroneous recovery paragraph: the earlier second-variation and quotient equations use the correct coefficient. The current reading edition explicitly corrects the comparison. The original project proof remains unchanged; its identity is recorded in [SOURCE_LINEAGE.json](SOURCE_LINEAGE.json). This is a failed ancillary identity, not a falsification of the primary Hessian/local-stability theorem. The current analytic audit rederives those primary steps separately.

## Current curvature instrument

The first new curvature checker reached serialization after its exact interval predicates, then failed at Python's 4,300-decimal-digit integer conversion limit. It produced no accepted certificate. Its source and failed execution are preserved locally outside the release.

Version2 serializes lossless signed hexadecimal numerators and positive hexadecimal denominators. Arithmetic and outward bounds are retained. Complete generation, JSON readback and recomputation under `-OO` passed, including an exact signed rational serialization canary. [Current checker](curvature_check_v2.py) and [current certificate](CURVATURE_AUDIT_V2.json). This repair concerns representation, not an improvement in the mathematical bounds.

## Historical C024 page pointer

The older C024 prior-art note pointed to physical pages 18–19. Its later C050 correction identifies Proposition 4.2 on physical 19 and Remark 4.3 on physical 20 of the pinned Chen–Weth v6 PDF. The current reading edition carries this qualification. The elementary Hardy/domain argument is unaffected; no error in the primary theorem is inferred.

## Optimization-safe derivative replay

The reviewed historical C061 producer used `assert` for 19 input/arithmetic guards. The current replay replaces these with explicit exceptions so the required guards remain active under `-O` and `-OO`. Its original reviewed source and the precise adaptation are identified in [CODE_LINEAGE.json](elliptic/CODE_LINEAGE.json). The 7,900 integration cells, interval arithmetic and complete tails are unchanged and were replayed. This is a verification-instrument qualification, not evidence that the historical derivative range was false.

A local review-registration helper also stopped on a cycle locator that was not a stable claim identifier. Its failed script and receipt are retained locally. Six already saved reviews were reconciled exactly, the nine exact stable identifiers were then used, and the complete 83-member roster was checked. No scientific certificate was changed by that documentation repair.

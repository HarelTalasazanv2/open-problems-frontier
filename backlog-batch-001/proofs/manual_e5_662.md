> Public reading edition for the audited mathematical claim. Historical phase counts below are not current global status. The original proof is retained unchanged in the project. Local navigation was adapted for this package; credit is in [REFERENCES.md](../REFERENCES.md). CNF/SAT encodings, slide-coverage counts, novelty and external/formal review are outside this audit.

# Case662: a combined capacity cut closes the individual-bound gap

**PROVED at the same restricted scope as PROOF.md:** the neighborhood class662cannot occur at a selected degree-six root of a17vertex simple graph with noK5, no independent four-set and maximum degree7, using the explicitly pinned C186degree refinement and C189saturation reduction.

The exact Alocal edges are02,03,05,14,23. The saturated crossdegrees are(2,4,3,3,4,4), and the complete permitted pair list is05,14,15,23,25,35,45. All other pair counts are zero by disjoint independent-triple witnesses. These data are reconstructed from the literal edge list and checked against the retained model. Because14is an Aedge, x14<=2by the clique/K5argument in PROOF.md.

Vertex0has only the permitted incident pair05, so x05=2. Its subtraction from the vertex5degree equation gives

`x15+x25+x35+x45=4-2=2`.

Nonnegativity implies x15+x45<=2. On the other hand, adding the vertex1and vertex4degree equations requires

`2*x14+x15+x45=4+4=8`.

The left side is at most2*2+2=6, a contradiction. Individual vertex capacities missed this interaction; their passing result remains correct as a historical restricted observation.

The saved certificate introduces s14=2-x14>=0. Twice its cap equation, plus degree5minus degrees0,1,4, and the required forbidden-type zero rows gives exactly

`x25+x35+2*s14=-2`.

All left coefficients are nonnegative and all variables are nonnegative. This is an exact contradiction; no optimization solver, numerical tolerance or strong-duality assumption is used. The actual saved row weights are checked against every source column and RHS. Negated, zero, truncated, insufficient-cap and altered-column controls are rejected; positive scaling remains accepted.

All720vertex permutations of the literal graph reproduce exactly the original180-member orbit. Removing precisely those180members from the first-stage57class/16,672labeled residual leaves **56classes/16,492labeled neighborhoods**. In total the full-slide application removes four named E5classes659,662,692,920, comprising360+180+360+45=945distinct labeled neighborhoods. Prior exclusions and all earlier phase artifacts remain unchanged.

This closes those four local cases and, with prior dated exclusions, the remaining E5route in the pinned C188domain. It does not classify the remaining56classes, decide the full17vertex graph target, prove the global Ramsey value, establish novelty or provide external/formal review. The next model must preserve singleton/pair distinctions when five-edge saturation is absent; it cannot silently reuse pair-only equations for a denser neighborhood.


[Batch verification](../verification_result.json) · [Extension verification](../extension_result.json) · [Exact exclusion chain](../chain_result.json).

# open-problems-frontier

**HTYT Enterprises LLC | Public research repository**

Start with the [results index](RESULTS.md) for exact statements, proof/certificate links and review limits. Run the [automated verification](VERIFICATION.md) to replay the self-contained packages. Analytic proofs and external-input dependencies are identified separately.

Open Problems Frontier is a research program for investigating open problems in mathematics and physics through precise statements, primary-source review, mathematical reasoning, computational certificates, and adversarial verification.

Research is directed and commissioned by **Harel Talasazan, HTYT Enterprises LLC**, with AI assistance documented in the relevant research records.

The objective is reliable information gained: a verified lemma, a rejected argument, a sharper bound, a decisive counterexample, a resolved source dependency, or a better-founded next experiment.

## Purpose

The project develops a catalog of research questions and conducts bounded investigations of specific obligations within them.

Each investigation should make clear:

- The exact question being examined.
- Its assumptions, definitions, domain, and normalization.
- What was already known and which sources establish it.
- What was attempted and actually verified.
- Which dependencies remain assumed or unreproduced.
- What the result permits us to conclude.
- The next action most likely to resolve a remaining uncertainty.

The catalog is selective and evolving. It is not a claim of comprehensive coverage of mathematical or physical open problems.

## Research scope

Research areas include:

- Number theory and arithmetic geometry.
- Algebraic geometry, Hodge theory, and K3 surfaces.
- Combinatorics, graph theory, and finite classification problems.
- Analysis, differential equations, and mathematical physics.
- Functional inequalities and quantum information mathematics.
- Cosmology and particle physics, where identifiable observations or datasets permit meaningful tests.

Individual investigations may concern a restricted theorem, a finite computation, a known result requiring local reproduction, an empirical hypothesis, or a missing source dependency.

A question unresolved within this project is not automatically an open problem in the mathematical or scientific literature.

## Research method

The working sequence is:

**Reconstruct → Select → Freeze → Attempt → Challenge → Adjudicate → Integrate → Report**

Before a deciding experiment or computation, define the claim, admissible inputs, dependencies, acceptance criteria, error model where applicable, and finite resource budget.

Challenge proposed results with relevant counterexamples, boundary cases, alternative derivations, and deliberately invalid inputs. For exhaustive computations, verify the expected case membership and completeness of coverage.

Preserve unsuccessful approaches and explain why they failed. Repeated work requires a substantive change in mechanism, evidence, scale, or certification strategy.

Operational completion, improvement of the research record, and resolution of a mathematical or empirical claim are recorded separately.

## Understanding result labels

Every label applies to a precisely stated claim and its documented scope.

| Label | Meaning |
| --- | --- |
| `PROVED` | A complete argument or valid certificate establishes the stated claim within its recorded scope. |
| `CONDITIONALLY_PROVED` | The conclusion follows under explicitly identified assumptions or theorem imports, with their verification limits recorded. |
| `CERTIFIED_RANGE` | A specified finite range, collection of inputs, or numerical enclosure has been rigorously checked. |
| `EMPIRICALLY_SUPPORTED` | Documented observations support the stated hypothesis within the tested conditions and uncertainty. |
| `FALSIFIED` | A valid counterexample or discriminating test refutes the exact stated claim. |
| `INCONCLUSIVE` | The attempted work does not decide the question. |
| `BLOCKED` | A necessary source, input, method, or other dependency prevents progress on the stated obligation. |
| `NOT_TESTED` | The relevant check or investigation has not been performed. |

A restricted proof does not establish its broader parent conjecture. A failed proof attempt does not establish that its conclusion is false. A finite search supports a universal claim only when a valid reduction connects the complete search to that claim.

## Evidence and reproducibility

Research records should preserve the information needed to inspect and reproduce their conclusions, including:

- Precise statements and mathematical conventions.
- Source identities, versions, dates, and inspection extents.
- Input provenance, parameters, and content hashes.
- Relevant code, dependencies, environment, and execution instructions.
- Exact arithmetic or justified numerical error bounds.
- Certificates, outputs, negative controls, and unresolved cases.
- Review history and the limits of each reproduction.

Rerunning supplied code, writing another implementation, deriving a result independently, obtaining external expert review, and completing formal verification are different forms of evidence. Records must identify which actually occurred.

Hashes and manifests support integrity checks within the project's custody model. They do not establish mathematical truth, source independence, or external authenticity.

For physics, model consistency, simulation, observational fit, and empirical support are assessed separately.

## Repository scope

This repository is the public GitHub home for Open Problems Frontier. Audited research records are added selectively when authorized for public release.

A project description or result summary does not imply that its complete evidence package has been uploaded. Evaluate an individual result against its accompanying proof, sources, inputs, certificates, and limitations.

Research records distinguish current working views from dated historical evidence. Material corrections should identify the affected claims and preserve the earlier record.

## Published research packages

- [Cycle 197: fixed-class proof and support-capacity audit](cycle-197/README.md).
- [Backlog batch 001: fourteen earlier scoped records](backlog-batch-001/README.md).
- [Backlog batch 002: eight scoped mathematical records](backlog-batch-002/README.md).
- [Backlog batch 003: nine additional audits and three output-only graph releases](backlog-batch-003/README.md).
- [Backlog batch 004: eighty-three individual audits, qualified corrections and expanded verification](backlog-batch-004/README.md).
- [Publication policy](PUBLICATION_POLICY.md), [references and credit](REFERENCES.md), and [rights notice](LICENSE).

The current release contains all 118 individually audited records in the authorized historical snapshot. Seven are source/interface records, and several mathematical records share a proof or checker; these are not counts of new discoveries. The 83-record backlog is covered by batch 004 at explicit claim ceilings, including the documented M07 correction. The three graph packages previously held are released as project-authored proofs, outputs and checking tools requiring an exact externally supplied seed. The curator's graph data and original CNF input are excluded; their redistribution terms remain unresolved. New matrix/source-input packages likewise publish project proofs, checking tools, output certificates and exact input identities while requiring separately supplied raw inputs. Each dated batch preserves its own historical counts and claim ceilings.

The historical exclusion chain released through Cycle 197 left 49 neighborhood classes / 14,872 labeled neighborhoods unresolved at that cycle. Later local graph work is outside that released chain. No full graph/Ramsey, Erdős covering, Erdős–Straus, P-versus-NP or other global open-problem resolution is asserted.

## Attribution and AI assistance

Research direction and commissioning are attributed to **Harel Talasazan, HTYT Enterprises LLC**.

AI assistance includes **Codex (OpenAI)** and **Claude (Anthropic)** in their documented roles. Contributions and reviews must be attributed to the work actually performed. AI assistance does not, by itself, constitute independent expert review.

Published theorems, methods, software, and other source materials retain their original academic and technical attribution. Applying or reproducing an existing result does not establish novelty.

## Access and disclosure

This repository contains research materials authorized for public release and review.

Public access does not, by itself, grant permission to republish, modify, redistribute, or sublicense copyrightable Company Materials outside an applicable authorization. External submissions, communications on behalf of the project, and additional releases require separate authorization. Applicable law, third-party rights, and the exclusions for facts, ideas, and discoveries stated below remain in effect.

## Rights

Copyright © 2026 HTYT Enterprises LLC. All rights reserved.

Original copyrightable Company Materials are proprietary to the extent that HTYT Enterprises LLC owns the applicable rights. This README grants no public license to reproduce, modify, distribute, publish, or sublicense those materials.

Third-party materials remain subject to their respective ownership, attribution requirements, and license terms. Applicable law and controlling separate agreements remain in effect.

No copyright ownership is asserted over mathematical facts, theorems, scientific facts, ideas, or discoveries as such.
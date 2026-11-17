# Audited historical reading edition

**Current audited claim:** CERTIFIED_RANGE: The cited manuscript defines the stated positive finite reset generator, weighted entropy/production, all-finite-tracial auxiliary class and common-mean pencils. Its displayed algebraic sanity checks hold.

**Claim ceiling:** Definitions and sanity checks only. The manuscript unrestricted-state equivalence needs a converse not supplied here; separate V3/V3x2 proofs support only their own bounds.

Current review: [individual audit](../ANALYTIC_AUDIT.json), [source lineage](../SOURCE_LINEAGE.json), [references and credit](../REFERENCES.md). The dated text below is retained as historical context. Its old read counts, source-status polls, runtime/control claims, operational instructions and next actions are not new executions or current instructions. Only the explicit current statement above is adopted. No novelty, blind or external expert review, formal verification or global resolution is asserted.

# M07: reset-model definitions and admission decision

Cycle164, UTC/local2026-11-10. **CERTIFIED_RANGE: a precise finite reset-model contract is now identified.** The definitions missing from the restricted136window are present in the submitted manuscript's proposition and reset section. The source's generator, entropy-production normalization and auxiliary class agree with the selected primary definition. This resolves definition debt; it does not verify the claimed alpha_SLlower bound, sharpness, a decimal optimum, a counterexample certificate or the global MLSI/CMLSI question.

## Sources and executed scope

The submitted TeX snapshot has266lines/20239bytes and SHA256 `77446b5626b9974f0f0cb33a61fe9107c0d5f5cb7b2971cf85aeb7b0628f6504`. Its correlated internal REPORT has333lines/25036bytes and SHA256 `ef82dcb59361b5811c95fbe1d9d566f400ab0f5ec2f5859c81842d49c957230e`. Paths and literal byte/codepoint ranges are in the Cycle164inspection register. The report's title does not make it external independent review: it explicitly records model exposure to the manuscript and expected results, and no human/formal review.

The initial frozen read covered REPORT1–225and manuscript1–197:422literal lines. It found the proposition but not its reset-specific Kdefinition. A prospective amendment added only the source-located manuscript198–266reset section and closing material,69lines, bringing current reads to491lines. This is a documented adaptation of the stopping/read budget, not a reconstruction of absent text. The complete manuscript was observed; REPORT226–333was not read this run. Its previously validated cumulative reading remains1–270, leaving271–333unread. The manuscript's prior1–197extent advances to1–266, with69new direct lines. No TeX, imported source program, numerical script or certificate was executed.

Eight fixed UTF8/hash/range controls passed before the deciding read. The extension required the old197line capture to be an exact byte prefix of the unchanged full source, with exactly69remaining lines. These checks concern extraction/custody, not mathematical truth.

The primary comparison used the public [Gao–Junge–LaRacuente–Li article](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/complete-positivity-order-and-relative-entropy-decay/7270B6BBA7891B612C00FAB066F1A380), Definition3.1, Eq3.3and the entropy-production display, plus the scope of Problem6.4. The observed web extraction ranges were830–851and1870–1876of2376lines. Raw HTML hash/byte offsets were not captured and remain UNKNOWN; the whole article was not read. Definition3.1uses2alpha and arbitrary finite auxiliary von Neumann algebras, agreeing with the local conventions. Problem6.4is posed for classical symmetric semigroups generally. This historical posed question and today's page access do not establish present openness or absence of later results. No current status or novelty survey was performed.

## Exact admitted model

Take a finite set with k>=2atoms, probabilities pi_i>0, sum_i pi_i=1, and p_min=min_i pi_i. Thus0<p_min<=1/2. On scalar functions, E_pi f=(sum_i pi_i f_i)1and

    L=c(I-E_pi),       c>0,       T_t=exp(-tL).

Here pi is invariant: E_pi preserves the pi mean, and T_t=exp(-ct)I+(1-exp(-ct))E_pi preserves it as well. The off-diagonal jump rates of the negative generator -L are c*pi_j, so detailed balance is pi_i*c*pi_j=pi_j*c*pi_i. Thus the specified positive generator, invariant probability and time scale match, without changing a sign convention.

The amplification algebra is ell-infinity(Omega) tensor Q, with Qa finite von Neumann algebra and taua faithful normal tracial state. Its trace is tau_pi(f)=sum_i pi_i tau(f_i). The source's CMLSIquantifier is over every such auxiliary Q. The reset pencil is explicitly formed for bounded positive invertible f_i; the source's later non-invertible extension is an additional mathematical claim, not verified here.

Let m=sum_i pi_i f_i and phi(s)=s log(s). The entropy and production at c1are

    H(f)=sum_i pi_i tau(phi(f_i))-tau(phi(m)),
    I(f)=sum_i pi_i tau[(f_i-m) log(f_i)].

The comparison convention is I(f)>=2alpha H(f). Positive generators, time convention, factor2and the weighted trace must be preserved together. A density is globally normalized by tau_pi(f)=1; each individual component need not have trace1. Homogeneity permits working with unnormalized positive inputs and restoring the global density normalization. The equilibrium case has zero entropy/production and must not be turned into a quotient with zero denominator.

The one-atom endpoint and c0are outside this contract: their fixed-point algebra/constant interpretation degenerates, and the displayed alpha_SLformula is not an admitted endpoint formula there. The source's reset proposition is applied at the nontrivial finite-state scope clarified by REPORT225.

## Definition-to-source map

| Field | Exact local source | Admission consequence |
|---|---|---|
| Semigroup/factor2/complete auxiliary class | manuscript35–43; REPORT30–53; primary Definition3.1 | Same convention; no factor2translation silently omitted |
| Reset generator and probabilities | manuscript84–92,209–220 | Special finite reset chain, not every classical generator |
| Weighted entropy/production | manuscript53–62,169–192,209–215 | Global density normalization and Umegaki trace entropy |
| Finite tracial algebra/Hilbert-space operators | manuscript94–108 | Qwith tracial tau; H=L2(Q,tau); left/right multiplication |
| psi_alpha and support-line domain | manuscript84–89 | Explicit scalar comparison function, not the two-point optimal constant |
| Reset-specific K and spectral measure | manuscript207–220 | Common-mean structured pencils, with a trace-induced vector state |
| Claimed lower/upper bound and extension | manuscript227–245; REPORT199–225 | Source assertion/proof available for a fresh audit; no bound adopted164 |
| Unrestricted arbitrary-state extension | manuscript92,238–245; REPORT21–26 | Only a sufficient stronger condition is exhibited; converse/realization bridge missing |

## Scalar function and structured operator class

For u>-1the source defines

    psi_alpha(u)=u log(1+u)
                 -2alpha[(1+u)log(1+u)-u],
    tilde_psi_alpha(kappa)=psi_alpha(kappa-1).

Its support-line constant is defined by existence of lambda with psi_alpha(u)>=lambda uon(-1,1/p-1], equivalently the displayed negative/positive-uquotient condition. For an actual reset chain the parameter is p=p_min, not an arbitrary selected atom weight. REPORT199–225asserts the closed formula

    A(p)=(1-p)log(1/p) / [2(log(1/p)-1+p)].

This formula, its numerical values and its use as a complete lower bound remain AS_REPORTED in this run. It is named alpha_SL; it is neither a certified sharp scalar constant nor a separation certificate. The source itself distinguishes the lower method from its scalar two-point upper test. A matrix quotient below a scalar upper bound would still not establish separation.

On H=L2(Q,tau), for theta in[0,1], define

    P_theta=(1-theta)L_m+theta R_m,
    Q_i,theta=(1-theta)L_fi+theta R_fi,
    K_i,theta=P_theta^-1/2 Q_i,theta P_theta^-1/2.

The source's spectral measure is in v=m^1/2in H. Under global density normalization, ||v||2^2=tau(m)=1. Equivalently the induced state on B(H)is omega_theta(T)=<v,Tv>; without normalization divide by tau(m). This is a vector state on the Hilbert-space operator algebra and generally is not tracial there. It is produced from a tracial underlying Qand a shared mean/pencil construction. It must not be confused with replacing the underlying CMLSItrace by an arbitrary state.

The source's exact reset-deficit representation is an integral in theta of sum_i pi_i omega_theta(tilde_psi_alpha(K_i,theta)), with the appropriate vector-mass factor if unnormalized. Its derivation depends on the entropy Hessian and pencil identity, integration and singular extension. Those analytic dependencies are not newly re-audited164merely because the formulas are now located.

## Restricted analytic sanity checks, PROVED internally

These checks are complete algebraic consequences of the identified positive-invertible model. They do not establish an entropy inequality or the alpha_SLbound.

First, the Umegaki relative entropy to the conditional expectation is H: sum_i pi_i tau(f_i log(m))=tau(m log(m))because m=sum_i pi_i f_i. The production for L=I-E_piis I. Subtracting log(m)inside each summand does not change I, since sum_i pi_i(f_i-m)=0. At two atoms, the two summands combine into pq tau[(A-B)(log(A)-log(B))], recovering the factor convention without a numerical example.

For L_c=cL, production becomes cIwhile Hdoes not change, so the admissible inequality constants and their optimum scale by c>0. Joint scaling f_i→r f_i, r>0, multiplies both H/Iby r: all extra log(r)terms cancel by the same mean identity. Scaling the trace multiplies both expressions equally. Ratios are compared only where H>0; an equilibrium ratio is not defined by these identities.

Second, the reset pencils obey exactly

    sum_i pi_i Q_i,theta=P_theta,
    sum_i pi_i K_i,theta=I,
    0<K_i,theta<=pi_i^-1 I<=p_min^-1 I.

Indeed, left/right multiplication are linear and positive on the tracial L2space. The mean identity proves the first equality. Each positive summand pi_i Q_i,thetais bounded above by their sum P_theta; congruence by P_theta^-1/2preserves that order and proves the second equality and spectral upper bound. Uniform invertibility makes every inverse well defined. These are necessary structural constraints; they do not prove that every family satisfying the constraints comes from such a shared left/right pencil.

## The unresolved converse and claim ceiling

The introduction calls the remaining reset question equivalent to an unrestricted operator/state inequality, while the reset remark establishes only that this inequality would suffice. The source provides no converse showing that every arbitrary admissible Kfamily/state can be realized by its common-mean left/right construction, or that a signed violation survives its theta integral. Therefore the claimed equivalence is unestablished by the supplied argument. This is a missing necessity/realization bridge, not a verified false theorem.

The internal REPORTalso asserts an arbitrary-state counterexample later in its discussion. No witness arithmetic, negative enclosure or certificate was audited164; no report226+was read this run. That assertion cannot become a classical CMLSIseparation. The bounded two-point/tracial retirements and published-version access holds remain unchanged.

**Admission decision:** MATCHED_CONTRACT_FOR_POSITIVE_INVERTIBLE_FINITE_RESET_MODEL. The C136definition debt is resolved at source/convention scope. The claimed reset lower-bound proof, non-invertible completion, sharpness, general-classical equality and global/current status remain separate unresolved obligations. The primary comparison checks normalization, not the internal manuscript's theorem validity or provenance as independent review.

## Next discriminating action

Prepare one fresh analytic audit of the reset deficit representation and the stated alpha_SLsupport-line lower bound for bounded uniformly invertible inputs in finite tracial auxiliaries. Keep p=p_minand the factor2/time scaling fixed. Re-derive the required Hessian/pencil integration and scalar nonnegativity; stop at the first failed lemma or a complete positive-invertible deficit proof. Do not promote a full CMLSIconstant before the bounded non-invertible extension is also justified. This uses the newly explicit model and is preferable to optimizing matrices or auditing an unrestricted witness that has no necessary-converse bridge to the catalog claim.

The proof audit is a proposal, not executed164. No new matrix search, external reviewer engagement, publication, status/novelty claim or performance gain is authorized by this source admission.

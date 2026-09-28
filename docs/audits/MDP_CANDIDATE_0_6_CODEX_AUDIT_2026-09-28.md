# Independent adversarial audit — MDP-Candidate 0.6

Date: 2026-09-28

**INFERENCE:** Candidate 0.6 should not be frozen. Its defects are remediable, but correcting them requires more than choosing a bootstrap method or increasing N. The central issues are an ambiguous manipulation, a mismatch between the question and the estimand, and an undefined population for inference.

**FACT / SOURCES:** I read the supplied handoff in full. I treated Candidate 0.5 as an unfrozen historical proposal and evaluated your newer Candidate 0.6. I checked the repository’s program audit and current README, verified the direct-configuration replication release, and searched literature independently through September 28, 2026. No experiment code was written, no behavioral calls were made, and no repository files were changed.

**1. Historical evidence does not validate this new instrument.**

**FACT / SOURCES:** The repository reports v0.7 root-only performance of 35/36 and derived-lure performance of 7/12, with a frozen `REDESIGN_FAILED_STOP` decision. It explicitly excludes v0.7 from confirmatory IAER inference. The program audit requires a materially new measurement idea before restarting. [Canonical program audit](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/blob/main/docs/program_audit_v0_2_to_v0_7.md).

The September replication release confirms a direct-configuration replication with H1 supported and H2 unsupported. It expressly distinguishes this from bit-for-bit runtime reproduction because the historical GGUF hash was not preserved. Thus, “same configuration” needs that qualification. [Replication release](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/iaer-v0.4.3-level-b-replication-20260927).

**INFERENCE:** These observations motivate a question; they do not supply a validated measurement instrument, a variance estimate for \(W\), or a transferable effect-size threshold. Neither the historical H1 effect nor v0.7’s lure error rate justifies N for this interaction.

**PROPOSAL:** Treat the follow-up as a new, configuration-specific metadata experiment. This prevents historical results from silently supplying its validity or power assumptions. It can still fail independently of the historical program. Its conclusions must concern its own frozen prompt distribution and model configuration.

**2. The boolean contrast isolates a text intervention, not a provenance mechanism.**

**FACT / SOURCES:** Within each U/L pair, Candidate 0.6 changes five assertions of linkage validity while preserving the candidate identifiers and substantive AUX content. Every AUX remains explicitly non-independent and zero-vote. Under the stipulated counting rule, neither linkage condition changes the correct answer.

Also, a 2-to-1 source majority is “normative” here **because the task stipulates equal root votes**. Independence alone would not generally establish that decision rule for real evidence.

**INFERENCE:** The strongest identifiable treatment is:

> Changing the displayed assertion that five candidate lineage links are invalid to an assertion that they are valid.

That is a legitimate behavioral intervention. It is not an isolated intervention on internal provenance reasoning.

Several explanations remain observationally compatible with any effect:

- **Credibility:** “valid” records appear more trustworthy.
- **Relevance:** a verified association makes their content more applicable.
- **Error handling:** “invalid” means discard the record.
- **Consistency checking:** an apparently incorrect reference contaminates the record’s perceived quality.
- **Symbolic binding:** an affirmed pointer strengthens association with an existing root.
- **Instruction/schema heuristics:** `true` fields receive attention or activation; `false` fields are suppressed.
- **Provenance interpretation:** the model responds to asserted derivational ancestry.

These are not all uncontrolled differences in the *causal intervention*: several are possible mediators of that intervention. But they prevent attributing its effect specifically to provenance-sensitive reasoning.

`candidate_root_id=R1` together with `root_link_valid=false` is logically coherent if R1 is a proposed association that was rejected. It is not self-explanatory. “False” might mean:

1. the candidate root does not exist;
2. it exists but is the wrong ancestor;
3. ancestry is unknown;
4. the record failed validation;
5. the association is merely inactive.

Those meanings are scientifically different. Calling all of them “unlinked” conceals the ambiguity.

There is another limit: a model can answer every item correctly by ignoring AUX records completely. Success therefore does not demonstrate that it parsed or understood their lineage.

**PROPOSAL:** Reject the current boolean as the sole operationalization of provenance linkage. Explicitly distinguish **absent lineage information**, **known absence of ancestry**, and **incorrect lineage information**. Select one before freeze.

This prevents an invalid-record treatment from being misdescribed as absence of a link. The residual problem is that every linguistic encoding changes semantics and can recruit heuristics. Permitted conclusions concern behavior under the selected metadata semantics; claims about internal provenance graphs, deduplication, or source counting remain prohibited.

**3. A cleaner encoding is possible, but no encoding makes semantics disappear.**

**FACT / SOURCES:** Keeping an identifier present removes one difference between the earlier sentinel design and Candidate 0.6. Equal identifier presence does not equate the meanings of “valid” and “invalid,” nor establish equal tokenizer behavior.

**INFERENCE:** The design faces a real tradeoff:

| Encoding | Advantage | Remaining problem |
|---|---|---|
| `NONE` versus a root ID | Natural missing-versus-present reference | Identifier presence and lexical association differ |
| Candidate ID plus validity boolean | Endpoint and structure match | Rejected/invalid association introduces quality cues |
| Lineage recorded versus unspecified | Avoids asserting an erroneous link | Tests disclosure versus missing information |
| Derivation relation versus topical association | Both associations are meaningful and valid | Tests relation type, not linked versus entirely unlinked |
| Counterbalanced arbitrary relation codes | Reduces fixed token–meaning association | Adds codebook interpretation and instruction dependence |

**PROPOSAL:** My preferred revision is a **typed-association contrast**:

- Both conditions identify the same real root.
- Both describe a valid association.
- One identifies the root as the AUX’s derivational source.
- The other identifies it only as a topical cross-reference, making no ancestry assertion.
- Both retain identical non-independence and zero-vote declarations.
- Neither uses “invalid,” “malformed,” or a nonexistent identifier.

The resulting question must become:

> Does explicitly designating an existing association as derivational, rather than merely topical, change directional AUX influence despite explicit zero-vote status?

Use two prospectively fixed realizations: transparent relation names and counterbalanced relation codes with a complete legend. Reverse the code-to-meaning mapping across balanced blocks. Do not select an encoding after behavioral results.

**Why:** Both associations are interpretable without making one record defective. Counterbalancing helps distinguish fixed token preferences from relation semantics.

**What it prevents:** A result driven solely by the presence of a real ID, or by a repeated “invalid” warning.

**What can still go wrong:** Derivation may imply authority, topical association may imply irrelevance, and codebooks may introduce additional difficulty. Agreement across realizations improves robustness; it does not establish mechanism.

**Permitted conclusion:** Sensitivity to the explicitly designated relation under these encodings. **Not permitted:** a pure effect of actual ancestry, a universal linked/unlinked effect, or proof of provenance reasoning.

If keeping the original scientific question unchanged is essential, use **recorded versus unspecified lineage** instead and acknowledge that missing information is part of the treatment. There is no honest wording fix that makes these different interventions equivalent.

**4. The factorial contrast is causally interpretable, but answers a narrower question than the one stated.**

**FACT / SOURCES:** Define the two simple linkage effects:

\[
\tau_{\mathrm{LOW}}
=E[Y(L_{\mathrm{LOW}})-Y(U_{\mathrm{LOW}})]
\]

\[
\tau_{\mathrm{HIGH}}
=E[Y(L_{\mathrm{HIGH}})-Y(U_{\mathrm{HIGH}})].
\]

Then:

\[
\Delta_{\mathrm{LINK}}=\tau_{\mathrm{LOW}}-\tau_{\mathrm{HIGH}}.
\]

This is an additive factorial interaction. It is not an omnibus test of whether linkage affects behavior.

For example:

| Condition | Probability of choosing LOW |
|---|---:|
| U_LOW | 0.20 |
| U_HIGH | 0.00 |
| L_LOW | 0.30 |
| L_HIGH | 0.10 |

Both linkage effects are \(+0.10\), yet \(\Delta_{\mathrm{LINK}}=0\).

**INFERENCE:** The interaction can identify **differential linkage effects by AUX direction**, assuming isolated calls, correctly implemented interventions, and a stable execution regime. It does not require the parallel-trends assumption associated with observational longitudinal difference-in-differences.

However:

- It cannot establish “no behavioral linkage effect” when zero.
- Opposing item effects can cancel.
- The HIGH-root condition targets one of two roots; LOW targets its only root.
- Balancing which HIGH root is selected removes arbitrary root-identity imbalance, not this structural asymmetry.
- Because HIGH is always correct, changes toward LOW increase error, whereas changes toward HIGH decrease error. Floor and ceiling effects can create asymmetric probability-scale effects.
- An interaction on the probability scale need not correspond to an interaction in any internal evidence-weighting process.

A positive \(\Delta_{\mathrm{LINK}}\) is not always “amplification.” If \(D_U=-0.4\) and \(D_L=-0.1\), the positive interaction reflects reduction of a reverse-direction effect.

**PROPOSAL:** Retain \(\Delta_{\mathrm{LINK}}\) only if the primary question explicitly becomes **directional modulation**. Report all four cell rates, both simple linkage effects, \(D_U\), \(D_L\), and the five-category \(W\) distribution.

Balance claim identity, root identifier, selected HIGH root, position template, and execution order prospectively. Restrict interpretation to the 1-versus-2 structure. Do not describe it as a root-count-invariant property.

This prevents a zero interaction from answering an omnibus question and prevents misleading sign interpretations. Cancellation and scale dependence remain possible. A broader “any influence” claim would require a separately specified joint analysis of the two simple effects, with corresponding multiplicity and power planning.

**5. C0 is necessary but insufficient for diagnosing failure.**

**FACT / SOURCES:** C0 establishes performance with three roots alone. Every main factorial condition adds five AUX records, additional fields, and additional text. Thus C0 differs from all four experimental cells in context load and structure.

**INFERENCE:** A neutral control is not mathematically necessary to identify the matched U/L contrasts. It is useful for a different question:

> Does adding five task-adjacent, zero-vote records impair root-count performance even without directional claim repetition?

Its role is diagnostic. It cannot isolate “pure length” if its content and support fields also differ.

**PROPOSAL:** Include one prespecified neutral-load condition as a secondary diagnostic. Its five AUX records should contain task-adjacent administrative information that makes no assertion about either claim, using the same record envelope and position template as the main conditions. Document any unavoidable differences, including `supports=NONE`.

This distinguishes broad eight-record interface failure from directional-content effects. Neutrality remains a semantic assumption, and a neutral control cannot rule out credibility or invalid-link interpretations. Do not subtract it from the primary interaction or present it as eliminating every context-load confound.

**FACT / SOURCES:** The proposed positive control changes real root votes from 1-versus-2 to 3-versus-2, reversing the correct claim.

**INFERENCE:** Aggregate positive-control accuracy alone is weak. A model could choose the former LOW claim in both C0 and the positive control and appear successful only in the latter.

**PROPOSAL:** Make **paired correctness and switching** the competence measure:

\[
J_i=1\{Y(C0)=0\ \text{and}\ Y(PC)=1\}.
\]

Report the full paired transition table, including wrong-to-wrong and reverse switches. Do not condition the denominator on C0 correctness.

Also include balanced, equal-record-count root-only reversals among qualification cases—for example, mirrored 2-versus-3 and 3-versus-2 problems. These prevent total record count from being sufficient to explain switching. The positive control demonstrates responsiveness to the stipulated root-count task; it does not demonstrate lineage comprehension or validate the AUX manipulation.

**6. Item-block inference is appropriate only after defining what items represent.**

**FACT / SOURCES:** With one binary choice per cell,

\[
W_i\in\{-2,-1,0,1,2\},\qquad
\widehat{\Delta}=\frac1N\sum_i W_i.
\]

Its variance is:

\[
\operatorname{Var}(W)
=\sum_{w=-2}^{2}w^2p_w-\left(\sum_{w=-2}^{2}wp_w\right)^2.
\]

The four outcomes within an item are dependent; their covariance is part of the design.

**INFERENCE:** Resampling calls independently would destroy the pairing and answer the wrong uncertainty question. But “resample items” is not sufficient by itself.

- If items are independently sampled from a frozen generator, inference can target that generator.
- If they are a handpicked finite benchmark and execution is deterministic, the observed benchmark mean is a census quantity. Bootstrapping does not manufacture a sampling population.
- If several items are cosmetic variants of one underlying scenario, the base scenario may be the resampling unit.
- Sharing a fixed template does not automatically invalidate independence conditional on that template. It does limit generalization beyond it.
- Runtime randomness and item variation are different sources of uncertainty.

**PROPOSAL:** Define a frozen stimulus-generating population, its strata and weights, and the independent base unit before choosing N. Sample independently within prespecified strata. Keep mirrored presentations and repeated realizations inside their base-item block.

This prevents pseudoreplication and unsupported generalization. A narrow generator can still give narrow scientific coverage. The resulting interval concerns that population and execution regime, not “LLMs generally.”

**7. Ordinary bootstrap inference should not be the sole primary safeguard.**

**FACT / SOURCES:** A nonparametric bootstrap samples only observed values. If every \(W_i=0\), every resampled mean is zero. BCa additionally requires an acceleration calculation that can be undefined for constant data; SciPy explicitly documents degenerate-distribution warnings and possible NaN endpoints. [SciPy bootstrap documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html).

Consider the hypothetical population:

\[
P(W=0)=0.99,\quad P(W=2)=0.01.
\]

Its true mean is \(0.02\). With \(N=64\), the probability of observing only zeros is approximately \(0.99^{64}=0.526\). A percentile interval of \([0,0]\) on those samples plainly lacks nominal coverage. This is an analytical example, not target-model data.

**INFERENCE:**

| Method | Assessment for this design |
|---|---|
| Percentile bootstrap | Simple and useful descriptively; unreliable near sparse-support boundaries |
| BCa | Can improve regular-case approximation; does not recover unobserved tail mass and can fail under degeneracy |
| Studentized/bootstrap-t | Requires reliable standard errors in resamples; zero or tiny resample variance causes instability |
| Linear probability regression | A saturated balanced factorial model reproduces the interaction; cluster-robust inference still needs enough independent blocks |
| Logistic regression/GEE | Estimates a different interaction unless marginal probabilities are standardized back to the stated estimand |
| Mixed models | Add distributional assumptions; separation and random-effect estimation can be problematic |
| Randomization inference | Exact only for a specified assignment mechanism and appropriate sharp null; not automatically an exact test of zero average interaction |
| Sign test | Tests sign balance among nonzero values, not the mean when magnitudes differ |
| Finite-support inference | Can exploit the five categories and accommodate zeros, provided nuisance parameters and stratification are handled correctly |

The sign-test distinction matters: a population with \(P(W=2)=1/3\) and \(P(W=-1)=2/3\) has mean zero but unequal sign probabilities.

**PROPOSAL:** Use a finite-sample-valid bounded-mean procedure as the primary safeguard. A simple conservative choice is the Hoeffding interval:

\[
C_N=
\left[
\bar W-\sqrt{\frac{8\log(2/\alpha)}N},
\bar W+\sqrt{\frac{8\log(2/\alpha)}N}
\right]\cap[-2,2].
\]

It requires independent bounded blocks; it does not require normality, positive sample variance, or identical distributions when targeting the average of their expectations. Unequal analysis weights require the corresponding weighted bound.

A potentially more efficient alternative is a confidence region for the five category probabilities, projected onto their mean. For fixed stratification, construct it within strata and combine using frozen weights and simultaneous coverage. That method must be fully specified and mathematically validated before replacing the conservative option.

This prevents degenerate resamples from producing false certainty. The cost is conservatism or additional analytical complexity. Neither method repairs dependent items or an unidentified construct.

**PROPOSAL — prospective failure rules:**

- Primary inference must remain defined when all \(W\) values are identical.
- Missing or malformed choices must not silently become \(Y=0\), nor be removed by complete-case selection.
- Unresolved incomplete blocks trigger the frozen integrity disposition, not outcome-dependent replacement.
- If bootstrap results are reported, use fixed block resampling, frozen strata/weights, a fixed seed, quantile convention, and—for example—50,000 resamples.
- Mark zero-width percentile intervals as empirical-bootstrap degeneracy, not proof of zero population uncertainty.
- Mark BCa unavailable for undefined acceleration, nonfinite correction, or invalid endpoints.
- Do not discard zero-standard-error bootstrap-t draws.
- Never switch to whichever method yields significance.

For this study, percentile bootstrap is sufficient as a **secondary descriptive sensitivity analysis**; BCa and bootstrap-t add little protection against the central sparse-support problem.

All-zero observations need not force inconclusiveness: a correctly constructed finite-support interval can bound rare unobserved events. The failure is false bootstrap certainty, not the existence of a degenerate sample.

**8. N can be justified without a behavioral pilot—but not uniquely without a scientific target.**

**FACT / SOURCES — mathematical derivation:** Since \(W\in[-2,2]\),

\[
\operatorname{Var}(W)\le4.
\]

For an approximate two-sided 5% test with 80% power at mean interaction \(\delta\),

\[
N\approx
\frac{(1.96+0.842)^2\sigma_W^2}{\delta^2}.
\]

Using \(\delta=0.25\) only as an illustration:

| Hypothetical distribution | Mean | Variance | Approximate N |
|---|---:|---:|---:|
| \(P(1)=0.25,\ P(0)=0.75\) | 0.25 | 0.1875 | 24 |
| \(P(2)=0.125,\ P(0)=0.875\) | 0.25 | 0.4375 | 55 |
| \(P(1)=0.625,\ P(-1)=0.375\) | 0.25 | 0.9375 | 118 |
| \(P(2)=0.5625,\ P(-2)=0.4375\) | 0.25 | 3.9375 | 495 |

These are normal-approximation planning illustrations, not exact power guarantees. Sparse cases particularly require exact evaluation of the intended rejection rule.

**INFERENCE:** N=64 can be adequate under some distributions and badly inadequate under others. Historical paired-RD sample sizes do not resolve this uncertainty.

Using the worst-case variance, the approximate 80%-power detectable interaction at N=64 is about **0.70**, not 0.25.

A distribution-free precision calculation is possible. The 95% Hoeffding half-width is:

\[
h_N=\sqrt{\frac{8\log40}{N}}.
\]

Therefore:

| Guaranteed half-width | Sufficient N, before balancing adjustments |
|---|---:|
| 0.25 | 473 |
| 0.125 | 1,889 |
| 0.10 | 2,952 |

At N=64, this conservative half-width is approximately **0.679**.

For the same interval, a sufficient condition for at least \(1-\beta\) power to exclude zero when \(|\Delta|\ge\delta\) is:

\[
N\ge
\frac{8\left[\sqrt{\log(2/\alpha)}
+\sqrt{\log(1/\beta)}\right]^2}{\delta^2}.
\]

For \(\alpha=.05,\ \beta=.20,\ \delta=.25\), **N=1,312** is a convenient sufficient balanced choice. It is conservative, not a claim that 1,312 is necessary or economically sensible.

**PROPOSAL:** Choose one planning objective before N:

1. a guaranteed precision;
2. power at a justified interaction magnitude;
3. a fixed resource budget with an honestly stated sensitivity limit.

For a less conservative finite-support analysis, evaluate the exact rejection rule over prespecified five-category distributions, including boundary, skewed, sparse-tail, and cancellation cases. Search beyond a few favorable scenarios; a finite grid alone is not a worst-case proof.

This prevents importing a favorable variance assumption. Unknown variance is **not** grounds for saying fixed N is impossible. What remains impossible is choosing a uniquely appropriate N without a population, a meaningful effect scale, and a resource/value decision.

If the scientifically useful precision is unaffordable, abandon the experiment rather than relabel an underpowered null as informative.

**9. The 0.25 threshold has no inherited scientific authority.**

**FACT / SOURCES:** A paired RD and a difference between two paired RDs are different quantities. Here the interaction ranges from −2 to 2. An interaction of 0.25 could arise from:

- one simple linkage effect of 0.25 and the other zero;
- effects of +0.125 and −0.125;
- much larger effects with partial cancellation.

It does not mean “25% of items changed because of linkage.”

**INFERENCE:** Nothing supplied establishes 0.25 as the smallest scientifically important interaction. A historical convention cannot do that work.

**PROPOSAL:** Remove 0.25 as a mandatory success criterion until its meaning is justified prospectively. It may remain an explicitly arbitrary descriptive reference, but should not automatically be called “large.”

If a SESOI \(\delta_*\) is adopted:

- evidence of nonzero modulation requires an interval excluding zero;
- evidence that the effect exceeds the SESOI requires the interval beyond \(+\delta_*\) or below \(-\delta_*\);
- evidence of practically negligible interaction requires an equivalence interval contained within \([-\delta_*,\delta_*]\);
- otherwise the result is unresolved at that scale.

A point estimate exceeding 0.25 with a CI barely excluding zero does not establish a population effect exceeding 0.25. Nor can a study have high power to prove an effect exceeds a threshold when the true effect sits exactly at that threshold.

This prevents mixing detection, magnitude, and practical relevance. Equivalence of the interaction still does not establish equivalence of both simple linkage effects.

**10. The gates need to separate competence, symmetry, and the phenomenon being studied.**

**FACT / SOURCES:** The handoff’s proposed per-cell rule of at least 12/16 correct is a minimum competence threshold. Two cells scoring 12/16 and 16/16 both pass despite a 25-point difference. It is not a symmetry test.

Likewise, 8/8 preflight successes do not establish high population competence. Under an IID binomial interpretation, the one-sided 95% lower confidence bound is only approximately 0.688.

**INFERENCE:** There are three different purposes:

- **Integrity gates:** Did the intended experiment execute?
- **Competence gates:** Can this configuration perform the stipulated task?
- **Symmetry assessments:** Does behavior remain sufficiently invariant under label/order transformations?

Passing one does not establish the others. Moreover, requiring the target AUX conditions to produce correct answers as a validity gate would gate away the phenomenon being investigated.

**PROPOSAL:**

| Check | Prospective treatment | Failure implication |
|---|---|---|
| Rendered roots, fields, pairing, keys, oracle agreement | Require exact agreement | Invalid implementation; stop |
| Model/runtime/tokenizer identity | Require frozen identity or declared new configuration | Invalid configuration comparison |
| Root-only competence | Prespecify acceptable error rate and sampling interpretation | Failed qualification; no clean AUX interpretation |
| Positive control | Require paired responsiveness, not isolated accuracy | Failed root-sensitivity qualification |
| Neutral-load competence | Diagnose whether the full record envelope is usable | Limits interpretation; if designated fundamental, inconclusive |
| Label/order symmetry | Use mirrored items and prespecified equivalence margins | Failure of invariant claim; not automatically failure of the balanced average |
| Target linkage effect | Analyze as the outcome | Never a validity gate |

For competence, a defensible **proposal**, not an established universal standard, is to require evidence that success exceeds 90% on a disjoint frozen qualification population. Choose the number of qualification cases from that criterion. For illustration, 32/32 IID successes give a one-sided 95% lower bound above 90%; joint cellwise requirements need simultaneous error control and more cases.

For symmetry, use the same base scenarios under label swaps and order reversals. Assess paired behavioral disagreement and interaction heterogeneity, not merely separate accuracy floors. Freeze an acceptable symmetry margin and adequate precision. Failure to reject a difference is not evidence of symmetry.

Keep the eight-case preflight, if desired, as a **smoke test** for catastrophic rule/interface failures. Require 8/8 once, after freeze; no behavioral tuning or rerunning to obtain a pass. It must not determine N or encoding.

**Why:** This prevents weak competence screens from being presented as symmetry evidence and prevents outcome selection.

**Remaining risk:** Qualification itself selects a configuration and task regime. Nominal primary intervals are not automatically 95%-coverage intervals conditional on passing correlated gates. Report all gates and outcomes transparently; do not retain only favorable items or hide failed frozen candidates.

**Permitted conclusions:** A valid, qualified experiment may support the frozen behavioral contrast. Failed fundamental gates mean `INVALID / INCONCLUSIVE` for that interpretation, not a negative scientific result. Representation heterogeneity can itself be a valid finding and should not be erased by calling every asymmetry “invalid.”

**11. Offline matching must examine actual rendered prompts and token sequences.**

**FACT / SOURCES:** No exact tokenizer audit, rendered stimulus set, or final prompt was supplied. Consequently, token equality and structural matching remain unverified.

**INFERENCE:** Equal character length is insufficient. Equal token count is also insufficient: token identities, positions, and associations can differ. Repeating the same root ID five times holds lexical frequency fixed across U/L but may still become behaviorally consequential when the relation is affirmed.

**PROPOSAL:** Before freeze, require a complete offline audit of:

- exact chat template, system/user boundaries, delimiters, whitespace, and final token IDs;
- tokenizer artifact/version and special-token handling;
- field names and field order;
- contextual tokenization of `true`, `false`, identifiers, relation codes, and claim labels;
- byte-level and token-level U/L differences against an explicit allowed-difference list;
- record counts, root counts, AUX counts, and zero-vote invariants;
- exact substantive U/L content matching;
- claim-token frequency, identifier frequency, and root-ID assignment;
- root/AUX positions and distances to the referenced root;
- selected HIGH-root balance crossed with claim identity and position;
- presentation order, template assignment, and absence of visible LOW/HIGH labels;
- prompt lengths, answer budget, and absence of truncation;
- fresh entity/content identities against historical stimuli;
- independently implemented expected-answer checks.

Freeze position schedules shared within item blocks and randomize execution order independently of condition. Use isolated contexts. A fixed seed does not substitute for documenting the complete runtime.

Require exact paired token-length equality where feasible, but do not add semantically odd padding merely to achieve it. If equality is impossible, document the difference and weaken the claim; do not call it “length matched.”

This prevents unrecognized implementation differences. It cannot make different tokens semantically equivalent or prove model comprehension. Validators establish what the prompt contains, not what the model understands.

**12. Prior art leaves a narrow possible contribution, not a broad novelty claim.**

**FACT / SOURCES:** The independent search covered repetition/paraphrase, conflicting sources, ancestry, provenance metadata, redundant retrieval, and correlated agent memory. I also followed related-work references beyond the handoff. The closest verified sources were:

| Source | Relevant overlap |
|---|---|
| [Naphade, *Rational Synthesizers or Heuristic Followers?*](https://aclanthology.org/2026.findings-acl.2003/) | GroupQA experiments report that paraphrased arguments can outweigh distinct independent support and identify presentation-order effects. |
| [Schuster et al., *Whose Facts Win?*](https://aclanthology.org/2026.acl-long.1357/) | Repetition can reverse preferences among conflicting source types. |
| [Bara, *Epistemic Sybil Resistance*](https://arxiv.org/html/2609.01873v1) | Separates report multiplicity, ancestry, and representation similarity. Crucially, its principal provenance-aware comparisons use explicit statistical aggregators over LLM-generated reports; they should not be misdescribed as this prompt-level boolean experiment. |
| [Wang et al., *GraphEcho*](https://arxiv.org/html/2609.17695v1) | Holds evidence wording and path templates fixed while varying origin assignments. Includes mirrored redundancy and controls using provenance identifiers, distinct-origin instructions, and path collapse. This is the closest conceptual overlap. |
| [Ross et al., *How retriever redundancy and diversity impact RAG effectiveness*](https://arxiv.org/abs/2608.13956) | Uses fictional QA to compare duplicates, paraphrases, and diverse documents while controlling answer availability. |
| [Qi et al., *When Not to Write Memory*](https://arxiv.org/abs/2607.02579) | Studies promotion of memories from correlated traces and dependency-aware support. |
| [Deng et al., *PAGE-RAG*](https://arxiv.org/abs/2608.29753) | Uses source-tracing metadata in graph-based evidence selection; distinguishes connectivity from support. |
| [Sabouhi, *Context Is Not Control*](https://symbolicsuite.com/context-is-not-control) | A working manuscript studies source-admissibility relations and behavior changes under source-boundary rendering. It is relevant adjacent work, not established evidence of this exact contrast. |

The search is not exhaustive, and abstract-level screening of adjacent papers cannot establish absence of an equivalent appendix experiment.

**INFERENCE — A. Clearly not novel:** Repetition effects; paraphrase effects; source-conflict sensitivity; distinctions between reports and independent observations; provenance identifiers; instructions to count distinct origins; and provenance-aware handling of redundant evidence.

**INFERENCE — B. Potentially distinctive:** A tightly controlled test of whether **explicitly designating ancestry changes directional choice behavior after non-independence and zero evidential contribution are already stipulated**, with relation semantics separated from invalid-record cues.

The distinctive feature would be the **incremental effect of redundant ancestry information**, not provenance reasoning generally.

**INFERENCE — C. Already done?** I did not identify an exact match for the complete zero-vote AUX contrast. GraphEcho substantially occupies the surrounding conceptual space. Absence of an exact hit does not establish priority, and a different field name or boolean is not, by itself, a scientific contribution.

**INFERENCE — D. Positive-result value:** A robust effect across counterbalanced realizations could show that explicit zero-weight instructions do not make ancestry metadata behaviorally inert. That is useful as a narrow interface result. A single `true/false` effect with ambiguous “invalid” semantics would add little beyond known prompt sensitivity.

**INFERENCE — E. Null-result value:** A sufficiently precise null could bound directional modulation under the frozen interface. It would not establish correct provenance use, absence of linkage effects in both directions, or robustness outside this generator. A wide interval or failed qualification would provide little information about the primary scientific question.

**PROPOSAL:** Make continuation conditional on a contribution statement that survives without the words “first,” “mechanism,” or “general provenance reasoning.” Require the revised design to resolve a specific remaining uncertainty rather than merely produce a new benchmark score.

This prevents cosmetic novelty. The remaining risk is that the effect is too interface-specific to justify the collection cost. Only a bounded behavioral result is permitted.

**Final disposition**

**FACT / SOURCES:** The design is unfrozen; N and the primary uncertainty method are undecided; exact stimulus/token matching is unverified. The literature already covers most of its broad motivation.

**INFERENCE:** I do not find a mathematical reason that forces abandonment: prospective fixed-N inference is possible without pilot data. Nor have I established exact prior-art duplication. But Candidate 0.6 currently cannot support its intended interpretation cleanly enough.

**PROPOSAL:** Continue only after these specific defects are resolved:

1. Replace invalid-versus-valid linkage with an explicitly defined, semantically coherent relation contrast—or accept the narrower invalidity-cue interpretation.
2. Align the primary question with directional interaction and preserve both simple effects.
3. Define the independent stimulus population and representation scope.
4. Select a scientifically justified precision/effect target and a finite-sample-valid primary analysis.
5. Replace purported symmetry gates with actual paired symmetry assessments.
6. Demonstrate that the bounded contribution warrants its prospective sample cost.

These revisions prevent ambiguous results from being promoted into provenance claims. They can still reveal that the required study is too expensive or too narrow to be worthwhile; that would justify abandonment before collection. The current design does not warrant proceeding to a freeze-ready protocol.

**REVISE**
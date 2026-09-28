# Adversarial audit of MDP-Candidate 0.6

**Date:** 2026-09-28
**Subject:** MDP-Candidate 0.6 (a prospective diagnostic follow-up to IAER v0.7)
**Input:** `IAER_MDP_HANDOFF_2026-09-28.md` + the proposed Candidate 0.6 revision
**Behavioral calls:** none. **Repository changes:** none.
**Verdict:** NO-GO

---

## 0. What I verified and what I didn't

**FACT / SOURCES**
- I could not read the repository's contents through the GitHub API (access isn't enabled for this session). I could only read the public README page. It confirms the program's status ("PAUSED — instrument redesign path exhausted under v0.7"), the disposition of every version from v0.4.3 to v0.7, and v0.4.3's H1 (Holm p = 9.5367e-7) and H2 (p = 0.50) results. Everything else I say about IAER history comes from the handoff and has **not** been checked against the repo.
- For prior art, I read an abstract or summary for each paper. For GraphEcho I also pulled verbatim quotes on its mitigation conditions M1 and M2. I did not read any paper in full.
- I ran a small offline simulation of the estimand. It uses no behavioral data and I'm not delivering it as code.

---

## 1. Construct validity: the central defect

**FACT (from the design)**
- In every experimental condition, every AUX record carries `independent=false` and `epistemic_vote=0`. The correct answer is HIGH in all four conditions.
- So `root_link_valid` has **no normative role**: the rule you give the model says the answer doesn't depend on it.

**INFERENCE**

1. **The boolean changes credibility, not provenance.** In U, the record says: "I am not independent, I derive from R1, and that derivation is false." Read naturally, that is an invalid, unverified or possibly fabricated record. In L, the record is a well-formed derivative of R1. The contrast is therefore "flagged-invalid record vs. well-formed record," which is a trust/quality cue. It is not "record with lineage vs. record without lineage."
2. **U records don't make sense on their own terms.** `independent=false` claims the record depends on something, but in U the only dependency named is declared invalid. The model can resolve the contradiction several ways:
   - treat the record as malformed and ignore it (U influence goes down);
   - treat it as an orphan claim of unknown origin, possibly independent (U influence goes up);
   - treat `false` as a general negation cue attached to the claim (U influence goes down).

   These predict **opposite signs** for D_U, so any sign of Delta_LINK has at least two credible explanations that aren't about provenance.
3. **There is no theory that predicts the sign.** A positive Delta_LINK could mean "valid links make the AUX look credible." A negative one could mean "valid links let the model collapse the AUX into its root." Both are equally easy to explain after the fact. An estimand whose sign can't be interpreted in advance can't serve as a confirmatory hypothesis.
4. **A null can't be interpreted either.** Nothing checks that the model read the field at all. That makes "insensitive to provenance" indistinguishable from "never parsed a boolean buried in eight records." A manipulation check that asks the model to report link status would be the same kind of explicit classification that v0.4.3 already showed does not establish use.
5. **Other channels the boolean opens:**
   - `true`/`false` carry strong prior associations with the truth of the claim itself.
   - `false` sits next to `independent=false`, so U records hold two `false` tokens and L records hold one. The count of negation cues per record differs.
   - Schema-completion heuristics: "all fields valid" reads as a finished record.

**Conclusion:** the experiment wouldn't measure provenance-sensitive reasoning. At best it measures how a metadata flag with credibility connotations modulates influence that the rule says should already be zero.

---

## 2. Other encodings

**PROPOSAL (evaluated, not recommended)**

| Encoding | Lexical difference | Semantic problem |
|---|---|---|
| `root_link_valid=true/false` (current) | 1 token | reads as credibility/validity; U is internally contradictory |
| `root_ref=R1` vs `root_ref=NONE` | ID present vs. absent | `independent=false` with no parent is incoherent; the ID adds salience |
| `root_ref=R1` vs `root_ref=R9` (an ID that doesn't exist) | 1 character | dangling reference, so a malformed-record cue |
| `derived_from=R1` (a ROOT) vs `derived_from=N1` (a non-evidence NOTE record present in **every** condition, C0 included) | 1 character plus the target's record type | cleanest option I found: both references resolve and there is no boolean. But the construct becomes "lineage into the evidence set vs. into a non-evidence record," and the NOTE records change C0 |
| Link to the same-claim root vs. link to an opposite-claim root | 1 character | the second creates a content–lineage contradiction, which is a contradiction-detection confound |

**INFERENCE:** every encoding with low lexical distance adds a semantic anomaly, and every semantically clean encoding adds structural or lexical asymmetry. The trade-off doesn't go away because it comes from the same source as §1: when both levels are normatively irrelevant, at least one level has to look odd.

---

## 3. Factorial logic

**INFERENCE**

1. **Floor effect kills the HIGH arm.** A competent model almost never chooses LOW when the AUX supports HIGH, since that direction agrees with the root majority. So Y(U_HIGH) ≈ Y(L_HIGH) ≈ 0, and Delta_LINK ≈ P(L_LOW error) − P(U_LOW error). The "2×2" collapses into a single paired contrast and the difference-in-differences adds nothing but noise.
2. **The range is asymmetric.** If U_LOW's error rate is e_U, then Delta_LINK is bounded roughly within [−e_U, 1−e_U]. If the model is fairly competent, an attenuating effect (negative sign) can barely be detected. The estimand is structurally biased toward being able to see only one sign.
3. **The two arms link to different structures.** In L_LOW, the five AUX records hang off the *only* root of their claim, so their lineage is the whole of LOW's provenance. In L_HIGH they hang off *one of two* roots, which is half of HIGH's provenance. "Link" therefore changes a different structural relation in each arm, and the interaction mixes the link effect with a (link × root cardinality) effect. Balancing which HIGH root is used doesn't fix this, because the asymmetry is 1-vs-2, not which root.
4. **Label, order and position:** the handoff's 4-cell balancing helps. But v0.7 R3 showed strong asymmetries (A_FIRST 5/6 vs. B_FIRST 2/6). Balancing removes these effects from the mean but not from the variance, and they can interact with direction.
5. **The link from v0.7 is backwards.** R3's derived records were explicitly tied to the INITIAL root, so R3 is closest to **L_LOW**, not to U. The motivating anomaly had no U counterpart. The new question isn't a diagnostic of what was observed. It is a new question the observation happened to suggest.

---

## 4. Controls

**INFERENCE / PROPOSAL**
- **C0 on its own can't separate repetition from context load.** C0 vs. U_LOW changes content direction, record count and length together. A neutral control (TARGET_NEUTRAL: C0 plus five `supports=NONE` AUX records, length-matched) answers one specific question: *does adding five zero-vote records degrade root counting regardless of content?* It is necessary for H-MULT, but **not** for Delta_LINK, whose contrasts all have five AUX records.
- **The TARGET_NEUTRAL control is itself confounded.** `supports=NONE` is a structural cue that repeats five times. It is not "neutral content," it is "content marked as irrelevant."
- **Positive control:** checking paired flips against C0 is better than an aggregate threshold. The same item must switch HIGH→LOW when the root count goes 1→3. That tests sensitivity at the item level, whereas "≥14/16 correct" can be met by a model biased toward whichever claim appears first. The limitation is that it only proves **counting of roots**. It doesn't prove the model reads AUX metadata, so it does nothing to validate the manipulation from §1.

---

## 5. Statistics

**FACT (simulation, 400 replicates per cell, percentile bootstrap B = 2000)**

| Scenario | N | Bootstrap CI excludes 0 | CI excl. 0 **and** \|Δ̂\| ≥ 0.25 |
|---|---|---|---|
| null, 94% zeros | 64 | 0.04 | 0.00 (62% of samples have <5 nonzero W) |
| Δ=0.25, discordance 50% | 64 / 128 | 0.82 / 0.98 | **0.52 / 0.53** |
| Δ=0.25, discordance 80% | 64 / 128 / 256 | 0.62 / 0.89 / 0.99 | **0.55 / 0.54 / 0.47** |
| Δ=0.15, discordance 30% | 128 | 0.88 | 0.03 |

The percentile bootstrap, the t interval and the sign test kept type I error ≤ 0.05 in the null scenarios I tried.

**INFERENCE**
1. **The combined rule is broken by construction.** If the true effect equals the threshold, the point estimate lands above it about half the time, whatever N is. Power stays near 50% even at infinite N. This defect alone is enough to reject the current rule.
2. **Item is the correct resampling unit.** At temperature 0, repeating calls on the same item adds no information, so the inference is about the item generator's population. Bootstrap over item blocks is correct for that target.
3. **Percentile vs. BCa vs. bootstrap-t:** with discrete W and many zeros, BCa's acceleration estimate is unstable (the jackknife gives many identical values), and bootstrap-t needs a standard error inside each resample that becomes 0 in degenerate resamples. A simple t interval on W had the same behavior as the percentile interval. **PROPOSAL:** primary analysis = t interval on the W_i (a mean of bounded variables, where the central limit theorem is adequate at N ≥ 128), with the percentile bootstrap and the exact sign test prespecified as sensitivity analyses. Reverse the burden: if the three disagree about excluding 0, the result is reported as INCONCLUSIVE, not "significant."
4. **GEE or mixed models** on the 4 calls × N items (logit, cluster = item) estimate a log-odds interaction, a different estimand that is unstable at the floor (quasi-separation when the HIGH arms are 0). Not recommended as primary.
5. **Exact randomization inference** would require the U/L assignment to be randomized within an item and exchangeable. It isn't, since U and L are fixed conditions each item always receives. A sign-flip test assumes a W distribution symmetric under the null, which is plausible but can't be guaranteed. Withdrawing the earlier "exact block permutation" wording was correct.
6. **Degeneracy rule (PROPOSAL):** if the number of nonzero W values is below a prespecified threshold (for example 10), report INCONCLUSIVE–DEGENERATE. Don't report a [0,0] interval as "no effect."

---

## 6. Sample size

**INFERENCE**
- With the HIGH arm at the floor, W ∈ {−1,0,1} and Var(W) = d − Δ², where d is the discordance rate. d is unknown but bounded by 1.
- Worst case (σ = 1), 80% power, α = 0.05, Δ = 0.25: N ≈ (2.80/0.25)² ≈ **126**. Without the floor (W up to ±2, σ ≤ 2), worst case N ≈ 502.
- N = 64 is enough only if d ≤ ~0.55, which can't be known without behavioral data.

**PROPOSAL (if the design continued):** set N by **worst-case variance** rather than an estimated one. Items are generated synthetically and the model runs locally, so N = 128 (W ∈ {−1,0,1}) or 256 (a margin for ±2) costs little. That removes the need for a pilot entirely. The alternative is a group-sequential design with prespecified alpha spending, which is legitimate but more complex than the problem warrants.

**What can't be justified prospectively:** a "sufficient" N for an effect below 0.25, and anything that depends on e_U (the §3 floor), since that sets which effects are even possible.

---

## 7. The 0.25 threshold

**INFERENCE**
- As an **SESOI** it has no anchor. The historical RD = 0.25 was a difference in proportions between two conditions. Delta_LINK is a difference of differences, bounded by e_U, and on a different scale.
- As a **decision threshold combined with a point estimate**, it is statistically defective (§5).
- **What it can defensibly be:** at most a prespecified *descriptive* label ("large effect") reported next to the interval, or an SESOI tested properly through an equivalence test (TOST) for the null-claim branch. That would require N ≈ 250+ for margins of ±0.15.

---

## 8. Validity gates

**PROPOSAL / INFERENCE**
- **Competence gates** (minimum thresholds): C0 ≥ 90% correct; positive control ≥ 87.5% **paired flips**. These establish that the model can do the task, not that it is symmetric.
- **Symmetry tests** are a different thing: the difference between LOW=A and LOW=B cells, and between A_FIRST and B_FIRST, in C0, with a tolerance (for example |diff| ≤ 0.15). Requiring "≥12/16 per cell" is a competence threshold dressed up as a symmetry test.
- **Structural and token gates are offline (pre-freeze):**
  - U/L prompts differ **only** at the authorized position (a character-level diff);
  - the exact token-count difference under Ministral's own tokenizer, reported per pair;
  - root positions balanced;
  - no stimulus collides with historical IAER items.
- **INVALID/INCONCLUSIVE (not a negative result):** failure of C0, of the positive control, of the symmetry tests, of structure/integrity, or a degenerate sample.
- **Negative result permitted only if:** all gates pass, there is enough nonzero W, and an equivalence test excludes the SESOI.
- **Unfixable gap:** no gate checks that the metadata was read (§1.4). This is exactly the gate that would separate "no effect" from "manipulation not perceived."

---

## 9. Tokenization and structure (offline, before freeze)

**PROPOSAL:** check with Ministral's exact tokenizer:
- `true`/`false` (single tokens? with or without a leading space?);
- the tokenization of `candidate_root_id` and `root_link_valid`;
- IDs `R1..R3`/`X1..X5` (single tokens, no splitting);
- `CLAIM_A`/`CLAIM_B` (identical token counts);
- field order that never varies;
- delimiters and whitespace byte-for-byte identical;
- the distance in tokens between each AUX and the root it references, balanced across U/L (it is identical by construction, but must be reported);
- the frequency of the referenced root ID in the prompt (in U and L it appears 5 extra times in both, which is good).

This is the part of the design that is remediable.

---

## 10. Prior art

**FACT / SOURCES**
- **GraphEcho** (arXiv 2609.17695): mitigation M1 "adds provenance identifiers"; M2 "also instructs the model to count distinct origins." On Qwen3-4B, the redundancy effect stayed ≈7.5 pp (M1 7.47, M2 7.22). Only structurally collapsing the equivalent paths (M3) removed it (0.05 pp).
- **Epistemic Sybil Resistance** (arXiv 2609.01873): separates report multiplicity from the multiplicity of evidence roots; >20,000 controlled calls. I only read a summary, so I haven't verified exactly what role the LLM plays versus the statistical aggregator.
- **Retriever redundancy/diversity** (arXiv 2608.13956): on fictional data, duplicate or paraphrased redundancy doesn't improve correctness; genre diversity does.
- **Established:** repetition reverses source preferences (Whose Facts Win?, ACL 2026); paraphrase is more persuasive than independent support (Naphade, Findings ACL 2026); models are distracted by irrelevant context even when told to ignore it (Shi et al., ICML 2023).

**INFERENCE**
- **A. Not novel:** repetition bias; the redundancy effect; same-root vs. independent-root multiplicity; and **whether visible provenance identifiers modulate the redundancy effect** (GraphEcho M1/M2 is the closest analog found, in a different format and on a different model).
- **B. What remains distinctive:** a flat-record format with zero-vote labels already present, plus a link-validity flag, on Ministral-3-8B Q4. That is a variation in format, model and flag, not a new question.
- **C. Has it already been done?** Not exactly, as far as my searches found, and absence from search results is not proof. Its conceptual core has been done.
- **D. Positive result:** "a boolean flag shifts one quantized model's behavior." Given §1, it wouldn't be attributable to provenance, so it would add little knowledge.
- **E. Null result:** it can't be separated from "the flag wasn't read," and it would be consistent with GraphEcho, so it would add almost nothing.

---

## Decisions (summary)

| Decision | Why | What it prevents | What can still go wrong | Conclusions permitted / not permitted |
|---|---|---|---|---|
| Don't freeze Candidate 0.6 | The U/L construct is credibility, not provenance; the sign can't be interpreted | A confirmatory result that can't be interpreted | — | Permitted: "the design was rejected before collection." Not permitted: anything about Ministral or provenance |
| Don't "patch" the encoding | Every option I evaluated trades one anomaly for another (§2) | Endless iteration on the same instrument, which the program audit already warns against | — | — |
| Any restart = a new question in which **lineage changes the normative answer**, so the model has to infer independence from lineage (e.g. an AUX with its own origin counts as a vote, one derived from R1 doesn't) | Only then does "using provenance" produce a measurable, directional prediction | Normatively null manipulations | Overlap with Bara/GraphEcho is even larger there; it must be judged as a new candidate, not a revision | — |

**Symmetry of the verdict:** I would have given **REVISE** if either (a) I had found an encoding where U and L are both semantically coherent and differ only in lineage, or (b) there were a prospective argument predicting the sign of Delta_LINK. I would have given **GO** if, on top of that, GraphEcho M1/M2 didn't exist or had tested something substantially different. Neither condition holds. The statistical and sample-size defects (§5–7) are fixable on their own and are not why I'm rejecting the design. I'm rejecting it because of §1 and §10.

This verdict isn't a scientific result about Ministral or about IAER. It says only that this instrument wouldn't produce interpretable information.

---

## Sources

- [IAER repository (README)](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling)
- [GraphEcho — arXiv 2609.17695](https://arxiv.org/html/2609.17695)
- [Epistemic Sybil Resistance — arXiv 2609.01873](https://arxiv.org/abs/2609.01873)
- [How retriever redundancy and diversity impact RAG effectiveness — arXiv 2608.13956](https://arxiv.org/abs/2608.13956)
- [Whose Facts Win? — arXiv 2601.03746](https://www.arxiv.org/abs/2601.03746)
- [Large Language Models Can Be Easily Distracted by Irrelevant Context — arXiv 2302.00093](https://arxiv.org/abs/2302.00093)
- [How Is LLM Reasoning Distracted by Irrelevant Context? — arXiv 2505.18761](https://arxiv.org/abs/2505.18761)

---

## Final decision

NO-GO
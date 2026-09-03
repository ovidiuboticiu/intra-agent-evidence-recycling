# Reviewer-Style Audit — IAER Methodological Note Draft v0.1

**Decision:** MAJOR REVISION, but **worth continuing**  
**Intended article type:** methodological note / negative-results case study  
**No new behavioral experiment required for the next draft**

## Overall assessment

The paper has a defensible contribution, but only if it is framed as a case study in **measurement transportability / instrument qualification before cross-family replication**. It should not be sold as discovery of dependent-evidence effects, repeated-evidence bias, or the general principle that construct validity matters in LLM evaluation. All of those have substantial prior art.

The strongest feature is the unusually complete sequence of preserved failed stages after a prior confirmatory target: preflight failure, exploratory interface diagnosis, preregistered ineligibility, calibration failure under two interfaces, measurement-decoupling redesign, and a preregistered STOP. This sequence gives the paper more value than any one failed model run.

## Major strengths

### 1. Clear scientific target precedes the failed replication program

The paper is not reverse-engineering a methodological lesson from arbitrary failed runs. v0.4.3 supplied a real, completed confirmatory target that later studies attempted to transport across families.

### 2. Strong separation of result classes

The project distinguishes:
- confirmatory effect;
- exploratory diagnostic;
- preflight failure;
- eligibility failure;
- calibration failure;
- instrument-redesign failure;
- invalid/inconclusive execution.

This taxonomy is practically useful and prevents failed instruments from being mislabeled as negative scientific results.

### 3. Fail-closed history is unusually transparent

The project retained aborted versions and did not rerun gates until they passed. This provides an auditable example of anti-model-shopping discipline.

### 4. v0.7 provides a useful decoupling test

Removing probability/reliability arithmetic directly addresses an auxiliary-capability confound exposed in v0.5/v0.6. The resulting 35/36 independent-root-control accuracy versus 7/12 in the derived-record lure is descriptively informative even though the frozen gates failed.

### 5. The paper has an honest negative endpoint

The final conclusion is not “we eventually replicated.” It is “the redesign path failed its own gate and the project paused.” That strengthens methodological credibility.

## Major weaknesses / reviewer risks

### 1. Direct phenomenon novelty is weak

By 2026, strong prior art already studies:
- repeated/paraphrased evidence versus independent support;
- redundancy and diversity in RAG;
- dependent/copy-derived evidence;
- belief revision and evidence aggregation.

Naphade (Findings of ACL 2026) is especially close because it reports that paraphrasing an argument can be more persuasive than distinct independent support and also finds order effects.

**Required revision:** state early and explicitly that the paper is not claiming novelty for the underlying repeated/dependent-evidence phenomenon.

### 2. General construct-validity novelty is also weak

Construct validity is already an explicit theme in LLM evaluation, including ICML 2025 and 2026 work on benchmark validity.

**Required revision:** do not present “benchmark validity matters” as the contribution. Present the contribution as a concrete *longitudinal empirical case* of what happens when a frozen effect is transported and the candidate repeatedly fails prerequisites.

### 3. The word “replication” can still mislead

A reviewer may object that no actual post-v0.4.3 confirmatory replication was performed.

**Required revision:** distinguish:
- *replication program/attempt* from
- *confirmatory replication test*.

The title should make clear that the paper is about a replication program stopping at qualification, not failed confirmatory replications.

### 4. v0.7 is underpowered for mechanism claims

Twelve items, three-item cross-cells, and label/order asymmetry make the R3 pattern suggestive only.

**Required revision:** use v0.7 primarily to show that removing one auxiliary demand did not yield a stable instrument. Keep the 35/36 vs 7/12 pattern descriptive and avoid causal language such as “derived records caused the failure.”

### 5. The proposed three-class taxonomy is sensible but not yet validated

The taxonomy is based on one research program. A reviewer may reject universal wording.

**Required revision:** call it a “practical reporting taxonomy” or “proposed operational distinction,” not a validated framework.

### 6. v0.6 preregistration deviation must remain visible

The partial Freeze-A publication weakens a claim of perfect preregistration discipline across the entire program.

**Required revision:** keep it in the main limitations section, not only supplementary material. Emphasize that v0.7 fixed the procedure by requiring the complete frozen ZIP release asset before authorization.

### 7. The paper needs a sharper unit of contribution

Draft v0.1 partly reads as project history. A publishable note needs one central argument.

Recommended central thesis:

> **An absent cross-family effect is not an interpretable non-replication unless the candidate model first demonstrates that the measurement instrument is usable for the construct-relevant comparison.**

The experiment history should support this thesis rather than dominate the paper.

## Required structural revisions

### Abstract

Shorten and organize as:
1. problem;
2. prior confirmatory target;
3. sequential qualification outcomes;
4. core methodological lesson.

Do not foreground IAER terminology before the general problem is understandable.

### Introduction

Open with the measurement problem, not project history.

Suggested opening question:

> If a behavioral effect disappears on another LLM, when is that evidence of non-replication—and when has the new model simply failed the instrument?

### Related work

Organize into only three clusters:
1. evidence repetition/dependence;
2. belief revision/evidence aggregation;
3. construct validity/evaluation transport.

### Results

Compress v0.5.0–v0.7 into one staged table plus short subsections.

### Discussion

Separate:
- what the program demonstrates;
- what it only suggests;
- what remains unknown.

### Conclusion

End on measurement interpretation, not IAER promotion.

## Recommended title revision

Preferred:

**When the Instrument Does Not Transfer: Qualification Failure in Cross-Family Replication of an LLM Behavioral Effect**

Alternative:

**Before Calling It a Non-Replication: Instrument Qualification Across LLM Families**

The second is stronger for a methodological note and avoids implying that the underlying IAER effect itself was repeatedly tested and failed.

## Publication readiness judgment

### Preprint

**YES after major revision.**

### Workshop / methodology / negative-results venue

**Plausible.** The transparency and sequential failed-gate history are a good fit.

### Findings-style short paper

**Possible but uncertain.** It would depend heavily on framing, reviewer interest in evaluation methodology, and the venue's tolerance for single-program case studies.

### Main-conference full paper

**Not recommended in the present evidence state.** A broader systematic set of transported instruments/models or a valid cross-family confirmatory replication would likely be needed.

## Decision for next action

**REVISE TO v0.2.**

Do not collect more IAER behavioral data. Strengthen the manuscript by narrowing the claim, reducing project chronology, and foregrounding the measurement-transport lesson.

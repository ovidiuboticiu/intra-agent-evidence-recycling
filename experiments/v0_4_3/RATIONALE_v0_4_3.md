# RATIONALE — v0.4.3 behavioral-confirmatory study

v0.4.3 is designed to answer the two behavioral questions that survived the earlier
pilot work, while avoiding an unstable provenance-semantic gate that is not required
to test those behavioral effects.

## Confirmatory targets
H1: repeated target-consistent memory records derived from one source increase
    retention relative to an equal-sized neutral-memory control.

H2: explicit lineage metadata on self-generated application traces reduces retention
    relative to otherwise untraced self-generated application traces.

## What v0.4.3 does NOT claim
v0.4.3 does not confirm that the model internally "knows provenance but fails to use it".
The provenance audit is descriptive only. Any mechanistic claim about provenance-use
requires a separate study specifically validated for that construct.

## Active-use manipulation
The repaired v0.4.2 application task is retained. The model applies an already
authorized configuration to five downstream operations. These calls do not ask the model
to re-evaluate which claim is true.

## Code compliance
All JSON-schema response formats use Python boolean `True` for `strict`.

## Fresh data
32 new fictional items are used. No v0.4.1 or v0.4.2 item is reused.

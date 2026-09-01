# v0.4.1 ABORT NOTE

Status: ABORTED — MANIPULATION VALIDITY FAILURE.

The v0.4.1 run produced 7 valid trajectories and then stopped at:
C16 / active_lineage / operation O2
expected CLAIM_B, received CLAIM_A.

This was not a transport failure, parse failure, or timeout. The v0.4.1
preregistration required all five active operations to retain INITIAL, so the
confirmatory dataset became invalid at that point and was not resumed.

The aborted v0.4.1 data are retained only as an audit record and are not merged
with v0.4.2.

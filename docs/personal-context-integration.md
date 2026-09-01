# Personal Context integration

Personal Context and DeTool govern different sides of one agent loop.

| Boundary | Question | Canonical output |
| --- | --- | --- |
| Personal Context | What is known, from which evidence, and under what disclosure policy? | Purpose-limited working projection |
| DeTool | What may be done, by which provider, under which authority, and how is success proved? | Verified usage proof |

## Outbound contract

An agent sends DeTool:

- the requested external state transition;
- the minimum input projection needed for that action;
- explicit authority or an approval challenge result;
- cost, latency, privacy, and verification constraints;
- an idempotency key.

The projection is temporary. DeTool must not receive a full personal-context
dump merely because the caller can access one.

## Return contract

DeTool returns a usage proof containing:

- the capability and provider route used;
- request, result, and optional before/after state digests;
- the verification method and evidence locator;
- a confirmation identifier when one exists;
- outcome, timing, and chargeability.

The proof is evidence of an attempted or completed action. It is not permission
to rewrite Personal Context. The caller may submit it as a candidate context
update, where ordinary provenance and write-governance rules still apply.

## Failure semantics

- `failed`: the requested transition did not occur and the failure is known.
- `indeterminate`: the caller cannot prove whether the transition occurred;
  retries require idempotency or explicit review.
- `challenged`: execution paused for additional authority or human approval.
- `verified`: the declared verifier confirmed the requested transition.

Network success, HTTP 200, or a queued response alone must not be promoted to
`verified`.


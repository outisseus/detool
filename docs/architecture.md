# Architecture

## Layers

### Registry

Stores versioned capability manifests. Discovery filters only over declared, inspectable fields; it does not infer permission from mere availability.

### Policy

Evaluates user authority, data classification, requested side effects, jurisdiction or organizational rules, and whether an interactive challenge is required.

### Router

Ranks allowed providers against explicit objectives such as reliability, latency, price ceiling, data locality, and verification strength. The selected route and rejected alternatives are logged.

### Adapter

Translates a canonical capability request into a provider-specific call. Secrets stay in the execution environment and are never embedded in manifests or usage proofs.

### Verifier

Checks the strongest available evidence: exact read-back, response schema, signed receipt, state transition, or a bounded health probe. “Request accepted” is not equivalent to “outcome verified.”

### Meter and reputation

Records normalized usage and dispute outcomes. Reputation is scoped to a capability version and verifier context; it is not a universal score.

### Optional settlement

Payment and open-network settlement remain adapters. They should not be introduced until identity, access, verification, and dispute semantics work locally.

## Non-goals for pre-alpha

- A token or speculative marketplace
- Automatic authority escalation
- A universal reputation score
- Treating a provider's success response as proof of the requested real-world outcome
- Storing provider credentials in the public registry


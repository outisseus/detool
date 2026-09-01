# Architecture

DeTool sits at the external-action boundary of an agent system. Its job is not
to teach a model how to call an API. Its job is to resolve a requested outcome
to a maintained provider, constrain the authority and data used, verify the
resulting state transition, and emit a normalized usage proof.

```text
desired transition + constraints
              │
              ▼
registry → policy → resolver → adapter → external provider
              │                         │
              └──────── verifier ◀──────┘
                            │
                            ▼
                usage proof + metering
```

## Layers

### 1. Capability registry

Stores versioned capability manifests around outcome semantics, not transport
packages. A capability states the action, expected state transition, required
authority, accepted data classes, service level, verification method, and the
available execution endpoints.

Discovery filters only over declared, inspectable fields; availability never
implies permission.

### 2. Policy

Evaluates user authority, data classification, requested side effects,
jurisdiction or organizational rules, and whether an interactive challenge is
required. Personal Context can supply a purpose-limited projection, but a
remembered preference or fact does not grant DeTool authority to act.

### 3. Resolver

Ranks allowed providers against explicit objectives such as reliability,
latency, price ceiling, data locality, and verification strength. The selected
route and rejected alternatives are recorded so the decision can be audited.

### 4. Adapter

Translates a canonical request into a provider-specific call. MCP, OpenAPI,
GraphQL, browser automation, local functions, another agent, and a human
operator are interchangeable transports behind the same capability contract.
Secrets stay in the execution environment and never enter public manifests or
usage proofs.

### 5. Verifier

Checks the strongest available evidence: exact read-back, signed receipt,
before/after state digest, bounded state probe, or explicit human review.
“Request accepted” is not equivalent to “outcome verified.”

### 6. Meter and scoped reputation

Records normalized usage, latency, cost, verification strength, failures, and
dispute outcomes. Reputation is scoped to a capability version, provider route,
policy context, and verifier. It is not a universal operator score.

### 7. Optional settlement

Payment, invoicing, tokens, and open-network settlement remain adapters. They
should not be introduced until identity, access, verification, and dispute
semantics work locally.

## What DeTool owns

- stable capability identity and versioned outcome semantics;
- a maintained provider graph and real reliability history;
- normalized verification and chargeability rules;
- routing, demand, dispute, and performance history.

These histories compound with use and are the durable layer.

## What DeTool abstracts

- MCP, HTTP, OpenAPI, GraphQL, browser, RPC, local, agent, or human transports;
- OAuth, API keys, wallets, sessions, and approval interfaces;
- model providers, databases, queues, and observability vendors;
- payment rails and token systems.

## Current pre-alpha compromises

- JSON contracts stand in for a running registry and resolver;
- service levels are declared rather than measured;
- examples are synthetic rather than maintained live providers;
- access decisions are reasoned manually rather than by a policy evaluator;
- billing and disputes are documented but not implemented.

## Non-goals for pre-alpha

- A token or speculative marketplace
- A catalogue of prompt wrappers
- Automatic authority escalation
- A universal reputation score
- Treating a provider success response as proof of a real-world outcome
- Storing provider credentials in the public registry


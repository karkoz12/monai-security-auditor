# Threat Model

This document describes the threat model for MONAI Security.

## Purpose

MONAI Security is a defensive, read-only auditing framework for MONAI-based medical AI projects. It inspects project metadata without executing untrusted code.

## Security Objectives

- Protect audit integrity.
- Preserve reproducibility.
- Avoid execution of untrusted artifacts.
- Detect technical security and integrity risks.
- Produce traceable audit evidence.

## Assets

Protected assets include:

- project source code,
- model artifacts,
- medical datasets,
- MONAI Bundle configuration,
- generated reports,
- dependency information.

## Trust Boundary

```{mermaid}
flowchart LR
User --> Auditor[MONAI Security]
Auditor -->|Read Only| Project
Auditor -->|Read Only| Dataset
Auditor -->|Read Only| Models
Auditor --> Reports
```

## Threat Actors

- Malicious model providers
- Compromised datasets
- Supply-chain attackers
- Insider threats
- Accidental users

## Attack Surfaces

### Model Files

Risks:
- unsafe pickle checkpoints,
- tampered models,
- unknown provenance.

Mitigations:
- metadata inspection,
- SHA-256 hashing,
- no model execution.

### Datasets

Risks:
- corrupted files,
- duplicate images,
- invalid metadata,
- NaN or infinite values.

Mitigations:
- integrity validation,
- metadata inspection,
- hash calculation.

### Source Code

Risks:
- hidden preprocessing,
- unsafe transforms.

Mitigations:
- static AST analysis,
- no dynamic imports,
- no code execution.

### Dependencies

Risks:
- outdated packages,
- unpinned versions,
- supply-chain weaknesses.

Mitigations:
- dependency inventory,
- pip freeze,
- requirements inspection.

## STRIDE Summary

| Threat | Mitigation |
|--------|------------|
| Spoofing | Hashes and provenance review |
| Tampering | Integrity checks |
| Repudiation | Persistent reports |
| Information Disclosure | Read-only analysis |
| Denial of Service | Fault-tolerant scanners |
| Elevation of Privilege | No execution of untrusted artifacts |

## Security Controls

Implemented controls:

- read-only operation,
- SHA-256 hashing,
- static analysis,
- structured reporting,
- graceful error handling.

## Out of Scope

The current version does not provide:

- malware analysis,
- penetration testing,
- runtime monitoring,
- digital signature verification,
- regulatory certification.

## Residual Risks

- zero-day vulnerabilities,
- compromised execution environments,
- obfuscated project logic,
- malicious content undetectable through metadata.

## Future Work

Potential extensions include:

- SBOM generation,
- CVE integration,
- provenance verification,
- digital signatures,
- configurable risk scoring.

## Summary

The MONAI Security threat model focuses on protecting audit integrity by using a read-only, static-analysis architecture while identifying common risks affecting MONAI-based medical AI pipelines.

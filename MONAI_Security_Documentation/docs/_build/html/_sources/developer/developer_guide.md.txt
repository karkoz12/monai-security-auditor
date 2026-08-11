# Developer Guide

This guide describes the internal architecture of MONAI Security and provides recommendations for extending the project with new scanners, reports, and security checks.

## Project Structure

```text
monai_security.py
docs/
requirements.txt
README.md
```

The core implementation is centered around the `MonaiSecurityAuditor` class, which coordinates the complete audit workflow.

## Audit Workflow

```{mermaid}
flowchart TD
    A[CLI] --> B[MonaiSecurityAuditor]
    B --> C[Dependency Scanner]
    B --> D[Model Scanner]
    B --> E[Dataset Scanner]
    B --> F[Transform Scanner]
    B --> G[Bundle Scanner]
    C --> H[Collected Findings]
    D --> H
    E --> H
    F --> H
    G --> H
    H --> I[Report Generation]
```

## Core Class

`MonaiSecurityAuditor` is responsible for:

- path discovery,
- scanner execution,
- issue collection,
- report generation,
- writing structured outputs.

The audit is started with:

```python
auditor.run_all()
```

## Data Classes

The implementation uses dataclasses for structured results.

Primary classes include:

- `AuditIssue`
- `DependencyRecord`
- `ModelFileRecord`
- `DatasetFileRecord`
- `TransformRecord`

These classes provide a common schema for reports.

## Scanner Design

Each scanner should:

1. inspect a single functional area,
2. avoid executing untrusted project code,
3. report findings using `add_issue()`,
4. generate structured records where appropriate,
5. continue execution after recoverable errors.

Current scanners include:

- Dependency Scanner
- Model File Scanner
- Dataset Metadata Scanner
- MONAI Transform Scanner
- MONAI Bundle Scanner

## Adding a New Scanner

A new scanner should be implemented as a method of `MonaiSecurityAuditor` and invoked from `run_all()`.

Typical implementation steps:

1. collect input paths,
2. inspect artifacts,
3. create `AuditIssue` objects,
4. store structured records,
5. optionally export scanner-specific JSON.

## Reporting

All reports are generated from a single audit payload.

Supported formats:

- JSON
- Markdown
- HTML
- PDF
- summary.txt

Adding a new format should not require modifying scanner implementations.

## Error Handling

Development follows a fault-tolerant approach.

Recommended behavior:

- catch recoverable exceptions,
- continue remaining scanners,
- record failures as audit findings,
- avoid terminating the entire audit.

## Coding Guidelines

Recommended practices:

- use type hints,
- keep scanners independent,
- prefer static analysis,
- avoid loading untrusted model files,
- document new scanners,
- write deterministic output.

## Testing

When adding functionality, verify:

- scanner execution,
- generated reports,
- JSON schema consistency,
- CLI behavior,
- handling of missing files,
- optional dependency handling.

## Future Extensions

Potential contributions include:

- DICOM privacy inspection,
- CVE database integration,
- Software Bill of Materials (SBOM),
- plugin architecture,
- digital signature verification,
- configurable severity scoring,
- parallel scanner execution,
- CI/CD integrations.

## Summary

The modular architecture of MONAI Security allows developers to extend functionality while preserving a consistent reporting model and a safe, read-only audit workflow.

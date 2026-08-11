
# Dependency Security Scanner

The **Dependency Security Scanner** analyzes the Python software environment used by a MONAI-based project. Its primary goal is to document project dependencies, identify reproducibility issues, and detect configuration patterns that may increase maintenance or integrity risks.

The scanner performs **read-only analysis** of dependency manifests and never modifies the audited project.

---

## Purpose

Modern medical AI projects depend on dozens of third-party libraries.

Incorrect, missing, or inconsistent dependency definitions can lead to:

- non-reproducible experiments,
- incompatible environments,
- deployment failures,
- difficult debugging,
- inconsistent research results.

The Dependency Security Scanner collects dependency information and reports observations that may affect project reproducibility.

---

## Scanner Architecture

```{mermaid}
flowchart TD
A[Audit Engine] --> B[Dependency Scanner]
B --> C[Locate Dependency Files]
C --> D[requirements.txt]
C --> E[pyproject.toml]
C --> F[environment.yml]
D --> G[Dependency Parser]
E --> G
F --> G
G --> H[Version Analysis]
H --> I[Finding Generator]
I --> J[Report Generator]
```

---

## Workflow

1. Receive project directory.
2. Search for supported dependency manifests.
3. Parse dependency definitions.
4. Extract package names.
5. Extract version constraints.
6. Detect missing manifests.
7. Detect unpinned packages.
8. Generate findings.
9. Return results to the Security Engine.

---

## Supported Dependency Files

| File | Purpose |
|------|----------|
| requirements.txt | pip dependencies |
| pyproject.toml | Python project metadata |
| environment.yml | Conda environment |

---

## Dependency Discovery

The scanner recursively searches the project for supported dependency manifests and records every detected file.

---

## Version Analysis

For each dependency the scanner records:

- Package name
- Version constraint
- Source manifest

Example:

| Package | Version |
|----------|----------|
| monai | ==1.4.0 |
| torch | ==2.5.1 |
| nibabel | >=5.0 |
| numpy | *(unpinned)* |

---

## Checks Performed

### Dependency Manifest Present

Finding:

```
Missing dependency manifest
```

Severity: **Medium**

### Unpinned Dependencies

Example:

```
numpy
```

instead of

```
numpy==2.1.3
```

Severity: **Low**

### Missing Required Dependencies

Example:

```
ModuleNotFoundError: reportlab
```

Severity: **High**

---

## CLI Example

```powershell
python monoai_audyt.py audit `
    .\project `
    --out .\audit_output
```

---

## Example JSON Finding

```json
{
  "scanner":"dependency",
  "finding_id":"DEP-001",
  "severity":"low",
  "title":"Unpinned dependency",
  "description":"Package 'numpy' has no fixed version.",
  "recommendation":"Specify an exact package version."
}
```

---

## Example HTML Report

```text
Dependency Security
-------------------
Status: Warning

Detected manifests:
✓ requirements.txt

Finding:
DEP-001 - Unpinned dependency

Recommendation:
Pin package versions.
```

---

## Risk Severity

| Severity | Meaning | Action |
|-----------|---------|--------|
| Critical | Scanner cannot continue | Resolve immediately |
| High | Missing required dependency | Install package |
| Medium | Missing manifest | Add dependency file |
| Low | Unpinned dependency | Pin versions |
| Informational | Observation | Documentation |

---

## Implementation Details

The scanner performs static inspection only. It opens dependency manifests, parses package entries, extracts version information and generates standardized findings. It never installs packages or modifies project files.

---

## Developer Notes

All findings should use a consistent schema containing:

- Finding ID
- Scanner name
- Severity
- Description
- Recommendation

---

## Performance Considerations

Dependency analysis is lightweight and typically completes in under a second for small projects.

---

## Error Handling

Parsing errors are reported as findings whenever possible instead of terminating the audit.

---

## Limitations

Current implementation:

- does not install packages,
- does not resolve dependency conflicts,
- does not verify package signatures,
- does not evaluate package quality.

---

## Future Work

Potential extensions include:

- SBOM generation
- CycloneDX export
- SPDX export
- Dependency graph visualization
- Optional CVE database integration
- Reproducibility scoring
- Signed dependency verification

---

## Summary

The Dependency Security Scanner documents the software environment of a MONAI project and highlights dependency-related issues that may reduce reproducibility while remaining a read-only component of the MONAI Security framework.

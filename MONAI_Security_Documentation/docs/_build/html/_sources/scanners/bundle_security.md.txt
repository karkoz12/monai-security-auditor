
# MONAI Bundle Security Scanner

The **Bundle Security Scanner** evaluates whether a project follows the MONAI Bundle structure and documents the presence of the files required for reproducible packaging, distribution, and deployment.

The scanner performs **read-only** analysis and never modifies bundle contents.

---

## Purpose

MONAI Bundles provide a standardized way to package medical AI projects. A complete bundle improves reproducibility, portability, and collaboration by combining models, configuration, metadata, and documentation in a consistent structure.

---

## Scanner Architecture

```{mermaid}
flowchart TD
A[Audit Engine] --> B[Bundle Security Scanner]
B --> C[Bundle Discovery]
C --> D[Directory Structure Validation]
D --> E[Configuration Inspection]
E --> F[Metadata Inspection]
F --> G[Bundle Rule Evaluation]
G --> H[Finding Generator]
H --> I[Report Generator]
```

---

## Workflow

1. Search for MONAI Bundle directories.
2. Validate expected folder structure.
3. Inspect configuration files.
4. Verify metadata availability.
5. Record model artifacts.
6. Evaluate bundle completeness.
7. Generate findings.
8. Export results.

---

## Expected Bundle Components

| Component | Purpose |
|-----------|---------|
| `configs/` | Workflow configuration |
| `models/` | Model artifacts |
| `docs/` | Documentation |
| `metadata.json` | Bundle metadata |
| `LICENSE` | Licensing information |
| `README.md` | Project description |

---

## Checks Performed

### Bundle Discovery

Detects whether the project follows a MONAI Bundle layout.

**Severity:** Informational

### Directory Structure

Verifies that expected directories are present.

**Severity:** Medium

### Configuration Files

Checks for required configuration files.

**Severity:** Medium

### Metadata Validation

Confirms that bundle metadata is available.

**Severity:** Medium

### Documentation Presence

Checks for README and supporting documentation.

**Severity:** Low

### Model Artifact Presence

Reports missing or incomplete model artifacts.

**Severity:** High

---

## CLI Example

```powershell
python monoai_audyt.py audit `
    .\project `
    --out .\audit_output
```

Bundle analysis is executed automatically during a complete audit.

---

## Example JSON Finding

```json
{
  "scanner": "bundle",
  "finding_id": "BND-001",
  "severity": "medium",
  "title": "Bundle metadata missing",
  "description": "metadata.json was not found.",
  "recommendation": "Provide bundle metadata for reproducibility."
}
```

---

## Example HTML Report

```text
Bundle Security
---------------

Bundle Status
-------------
Incomplete

Findings
--------
BND-001
Medium
Bundle metadata missing

Recommendation
--------------
Add metadata.json to the project bundle.
```

---

## Risk Severity

| Severity | Meaning | Recommended Action |
|-----------|---------|--------------------|
| Critical | Scanner cannot complete | Resolve immediately |
| High | Required bundle component missing | Complete bundle before release |
| Medium | Recommended structure incomplete | Review bundle layout |
| Low | Documentation improvement | Update documentation |
| Informational | Observation only | No action required |

---

## Implementation Details

The scanner performs static inspection of the project directory. It inventories bundle-related files and folders, compares them against expected MONAI Bundle conventions, and generates standardized findings. It does not modify files or validate model performance.

---

## Developer Notes

Bundle-specific checks should use the common finding schema with:

- Finding identifier
- Scanner name
- Severity
- Description
- Recommendation

Future checks should remain modular and independent from other scanners.

---

## Performance Considerations

Bundle inspection is lightweight because it relies primarily on filesystem traversal and metadata collection. Runtime scales with the number of files in the project.

---

## Error Handling

Unreadable directories, missing files, permission errors, and malformed configuration files are reported as findings whenever possible instead of terminating the audit.

---

## Limitations

The current implementation:

- does not certify compliance with external standards,
- does not validate model quality,
- does not execute workflows,
- does not verify digital signatures,
- does not publish or package bundles.

---

## Future Work

Potential enhancements include:

- automated MONAI Bundle validation,
- schema validation for metadata,
- dependency cross-checking,
- bundle completeness scoring,
- digital signature verification,
- export of bundle validation reports.

---

## Summary

The Bundle Security Scanner documents the completeness and organization of MONAI Bundles, helping developers identify missing components and improve the reproducibility and maintainability of medical AI projects within the MONAI Security framework.

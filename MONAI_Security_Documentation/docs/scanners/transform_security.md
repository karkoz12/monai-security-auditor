
# MONAI Transform Security Scanner

The **Transform Security Scanner** analyzes preprocessing and augmentation pipelines implemented with MONAI transforms. It documents the transformation workflow, identifies reproducibility concerns, and reports configuration patterns that may affect consistency between training and inference.

The scanner performs **read-only** analysis and never modifies project code or configuration.

---

## Purpose

Image preprocessing directly influences the quality and reproducibility of medical AI models. This scanner inventories MONAI transform pipelines and highlights observations that may impact experiment repeatability or deployment consistency.

---

## Scanner Architecture

```{mermaid}
flowchart TD
A[Audit Engine] --> B[Transform Security Scanner]
B --> C[Discover Configuration Files]
C --> D[Parse MONAI Transforms]
D --> E[Pipeline Analysis]
E --> F[Reproducibility Rules]
F --> G[Finding Generator]
G --> H[Report Generator]
```

---

## Workflow

1. Locate MONAI configuration files and Python pipelines.
2. Identify MONAI transform definitions.
3. Record transform sequence.
4. Detect random transforms.
5. Identify custom transforms.
6. Evaluate reproducibility-related settings.
7. Generate findings.
8. Export results to the reporting engine.

---

## Supported Analysis

| Component | Description |
|-----------|-------------|
| Compose pipelines | Transform sequence |
| Deterministic transforms | Documentation |
| Random transforms | Reproducibility review |
| Custom transforms | Identification |
| Configuration files | Static inspection |

---

## Checks Performed

### Transform Discovery

Detects MONAI transform pipelines used by the project.

**Severity:** Informational

### Random Transform Detection

Identifies transforms introducing stochastic behavior (for example, random flips, crops, or rotations).

**Severity:** Medium

### Custom Transform Detection

Reports user-defined transform classes that may require manual review.

**Severity:** Low

### Pipeline Documentation

Records the preprocessing sequence for reporting and reproducibility.

**Severity:** Informational

### Configuration Consistency

Reports malformed or incomplete transform configurations when detected.

**Severity:** Medium

---

## CLI Example

```powershell
python monoai_audyt.py audit `
    .\project `
    --out .\audit_output
```

Transform analysis is executed automatically during a complete audit.

---

## Example JSON Finding

```json
{
  "scanner": "transform",
  "finding_id": "TRN-001",
  "severity": "medium",
  "title": "Random transform detected",
  "description": "RandomFlipd is used within the preprocessing pipeline.",
  "recommendation": "Document seed management and reproducibility strategy."
}
```

---

## Example HTML Report

```text
Transform Security
------------------

Pipeline Summary

LoadImaged
EnsureChannelFirstd
Spacingd
Orientationd
ScaleIntensityRanged
RandomFlipd

Findings

TRN-001
Medium
Random transform detected

Recommendation

Document reproducibility settings.
```

---

## Risk Severity

| Severity | Meaning | Recommended Action |
|-----------|---------|--------------------|
| Critical | Scanner cannot complete | Resolve immediately |
| High | Configuration may invalidate workflow | Review before deployment |
| Medium | Reproducibility concern | Document and verify |
| Low | Informational improvement | Review if needed |
| Informational | Metadata only | No action required |

---

## Implementation Details

The scanner performs static analysis of MONAI transform definitions. It documents transform order, identifies stochastic operations, and generates standardized findings. It does not execute transforms or process medical images.

---

## Developer Notes

Each finding should follow the common finding schema:

- Finding identifier
- Scanner name
- Severity
- Description
- Recommendation

New transform categories should integrate through the shared scanner interface to ensure consistent reporting.

---

## Performance Considerations

Pipeline inspection is lightweight because only configuration files and Python source are analyzed. Runtime depends mainly on project size rather than dataset size.

---

## Error Handling

Unreadable configuration files, unsupported syntax, or parsing errors are reported as findings whenever possible instead of terminating the audit.

---

## Limitations

The current implementation:

- does not execute transform pipelines,
- does not validate clinical appropriateness,
- does not measure augmentation quality,
- does not benchmark preprocessing performance,
- cannot determine whether random seeds are applied correctly at runtime.

---

## Future Work

Potential enhancements include:

- transform dependency graphs,
- visualization of preprocessing pipelines,
- deterministic pipeline verification,
- configuration diff reports,
- reproducibility scoring,
- support for additional configuration formats.

---

## Summary

The Transform Security Scanner documents MONAI preprocessing pipelines, identifies reproducibility-related characteristics, and provides structured findings that help developers understand and review transformation workflows within the MONAI Security framework.

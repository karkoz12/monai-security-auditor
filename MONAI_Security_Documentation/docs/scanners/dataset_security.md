
# Dataset Security Scanner

The **Dataset Security Scanner** evaluates the integrity, consistency, and basic quality of medical imaging datasets used by MONAI projects. It performs a **read-only** inspection of dataset contents and metadata without modifying any files.

---

## Purpose

Reliable datasets are essential for reproducible medical AI. This scanner documents dataset characteristics and reports conditions that may negatively affect preprocessing, training, or inference workflows.

---

## Scanner Architecture

```{mermaid}
flowchart TD
A[Audit Engine] --> B[Dataset Security Scanner]
B --> C[Dataset Discovery]
C --> D[Format Detection]
D --> E[Metadata Inspection]
E --> F[Integrity Checks]
F --> G[Finding Generator]
G --> H[Report Generator]
```

---

## Workflow

1. Discover dataset files.
2. Detect supported formats.
3. Read image metadata.
4. Validate dimensions and data types.
5. Check for NaN/Inf values.
6. Detect constant images.
7. Verify image-mask consistency (when available).
8. Generate findings.
9. Export results.

---

## Supported Formats

| Format | Extension |
|---------|-----------|
| NIfTI | `.nii`, `.nii.gz` |
| DICOM | `.dcm` |
| MetaImage | `.mha`, `.mhd` |
| NRRD | `.nrrd` |

---

## Checks Performed

### Dataset Discovery
Records all supported medical image files.

**Severity:** Informational

### Metadata Inspection
Extracts dimensions, voxel spacing, datatype, and selected metadata.

**Severity:** Informational

### Shape Validation
Detects unexpected image dimensions.

**Severity:** High

### Image–Mask Consistency
Checks whether paired image and segmentation mask have compatible dimensions.

**Severity:** High

### NaN / Infinite Values
Detects invalid numeric values.

**Severity:** High

### Constant Images
Flags images containing a single constant intensity value.

**Severity:** Medium

### Unsupported File Format
Reports files that cannot be interpreted as supported medical image formats.

**Severity:** Medium

---

## CLI Example

```powershell
python monoai_audyt.py audit `
    .\project `
    --dataset .\dataset `
    --out .\audit_output
```

---

## Example JSON Finding

```json
{
  "scanner": "dataset",
  "finding_id": "DATA-001",
  "severity": "high",
  "title": "Image-mask shape mismatch",
  "description": "The segmentation mask dimensions differ from the corresponding image.",
  "recommendation": "Verify preprocessing and dataset alignment."
}
```

---

## Example HTML Report

```text
Dataset Security
----------------

Dataset:
BraTS2025

Files scanned:
250

Findings:
DATA-001
High
Image-mask shape mismatch

Recommendation:
Verify preprocessing and dataset alignment.
```

---

## Risk Severity

| Severity | Meaning | Recommended Action |
|-----------|---------|--------------------|
| Critical | Scanner cannot complete | Resolve immediately |
| High | Dataset integrity issue | Correct before training |
| Medium | Quality or compatibility concern | Review |
| Low | Minor improvement | Document |
| Informational | Metadata only | No action required |

---

## Implementation Details

The scanner performs static inspection of image files and metadata. It does not modify datasets, alter metadata, or execute preprocessing pipelines. Results are normalized into the common finding schema used by the reporting engine.

---

## Developer Notes

New file formats should be added through the common scanner interface. Each finding should include:

- finding identifier,
- scanner name,
- severity,
- description,
- recommendation.

---

## Performance Considerations

Runtime depends primarily on the number and size of dataset files. Metadata extraction is generally inexpensive, while integrity checks scale linearly with the dataset.

---

## Error Handling

Unreadable files, corrupted metadata, permission errors, and unsupported formats are reported as findings whenever possible instead of terminating the audit.

---

## Limitations

The current implementation:

- does not assess annotation quality,
- does not evaluate clinical correctness,
- does not detect labeling bias,
- does not repair corrupted datasets,
- does not validate training suitability beyond implemented integrity checks.

---

## Future Work

Potential enhancements include:

- duplicate image detection,
- annotation consistency analysis,
- dataset fingerprinting,
- DICOM de-identification checks,
- dataset lineage tracking,
- automatic quality scoring.

---

## Summary

The Dataset Security Scanner provides a structured assessment of medical imaging datasets by documenting metadata, validating integrity, and reporting findings that may affect reproducibility and downstream MONAI workflows.

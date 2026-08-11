
# Model Security Scanner

The **Model Security Scanner** inspects machine learning model artifacts used by MONAI projects. It documents model files, identifies potentially unsafe serialization formats, and records metadata that supports reproducibility and traceability.

The scanner performs **read-only analysis** and never modifies model files.

---

## Purpose

Model checkpoints are one of the most valuable assets in a medical AI project. This scanner inventories model artifacts and highlights findings that may affect portability, reproducibility, or operational safety.

---

## Scanner Architecture

```{mermaid}
flowchart TD
A[Audit Engine] --> B[Model Security Scanner]
B --> C[Discover Model Files]
C --> D[Format Detection]
D --> E[Metadata Extraction]
E --> F[SHA256 Calculation]
F --> G[Security Rules]
G --> H[Finding Generator]
H --> I[Report Generator]
```

---

## Workflow

1. Locate model files.
2. Identify supported formats.
3. Extract basic metadata.
4. Compute SHA256 hashes.
5. Detect pickle-based formats.
6. Generate findings.
7. Export results to the reporting engine.

---

## Supported Model Formats

| Extension | Status |
|-----------|--------|
| `.pt` | Supported |
| `.pth` | Supported |
| `.ckpt` | Supported |
| `.onnx` | Supported |
| `.torchscript` | Supported |
| `.ts` | Supported |
| `.safetensors` | Supported |

---

## Checks Performed

### Model Discovery

Detects model files within the audited project.

**Severity:** Informational

### File Hash

Calculates a SHA256 checksum to support artifact identification.

**Severity:** Informational

### Pickle-based Serialization

Flags checkpoint formats that commonly rely on Python pickle serialization.

**Severity:** High

### Unsupported Model Format

Reports model files with unknown or unsupported extensions.

**Severity:** Medium

### Missing Model

Reports when an expected model artifact cannot be located.

**Severity:** High

---

## CLI Example

```powershell
python monoai_audyt.py audit `
    .\project `
    --model .\models\best_model.pth `
    --out .\audit_output
```

---

## Example JSON Finding

```json
{
  "scanner": "model",
  "finding_id": "MODEL-001",
  "severity": "high",
  "title": "Pickle-based checkpoint detected",
  "description": "Model uses a serialization format based on Python pickle.",
  "recommendation": "Consider using safetensors where appropriate."
}
```

---

## Example HTML Report

```text
Model Security
--------------

Detected Models
---------------
best_model.pth

Findings
--------
MODEL-001
High
Pickle-based checkpoint detected

Recommendation
--------------
Consider using safetensors where appropriate.
```

---

## Risk Severity

| Severity | Meaning | Recommended Action |
|-----------|---------|--------------------|
| Critical | Scanner cannot continue | Resolve immediately |
| High | Potential security or integrity concern | Review before deployment |
| Medium | Compatibility or portability issue | Investigate |
| Low | Improvement recommended | Document |
| Informational | Metadata only | No action required |

---

## Implementation Details

The scanner performs static inspection only. It records:

- file name,
- extension,
- file size,
- SHA256 checksum,
- detected model format.

It does not execute, deserialize, or modify model artifacts.

---

## Developer Notes

New model formats should integrate through the common scanner interface and produce standardized findings with:

- finding identifier,
- scanner name,
- severity,
- description,
- recommendation.

---

## Performance Considerations

Hash calculation time depends on model size. Metadata extraction itself is lightweight and scales linearly with the number of model files.

---

## Error Handling

Unreadable files, permission errors, or unsupported formats are reported as findings whenever possible instead of terminating the audit.

---

## Limitations

The current implementation:

- does not evaluate model accuracy,
- does not validate clinical performance,
- does not execute model inference,
- does not detect malicious payloads,
- does not certify regulatory compliance.

---

## Future Work

Potential enhancements include:

- digital signature verification,
- model provenance tracking,
- SBOM linkage,
- model lineage visualization,
- reproducibility scoring,
- optional cryptographic signing support.

---

## Summary

The Model Security Scanner inventories machine learning model artifacts, records identifying metadata, and reports observations that improve traceability, reproducibility, and operational awareness within the MONAI Security framework.

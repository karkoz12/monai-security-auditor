# Radiologist Guide

This guide explains how radiologists can use MONAI Security to assess the technical integrity and reproducibility of MONAI-based AI projects before research or clinical evaluation.

## Purpose

MONAI Security does **not** evaluate diagnostic performance. Instead, it verifies the technical quality of an AI project by identifying:

- missing or corrupted datasets,
- potentially unsafe model formats,
- incomplete MONAI Bundles,
- reproducibility issues,
- preprocessing transforms,
- dependency information.

## Workflow

```{mermaid}
flowchart LR
A[Select Project] --> B[Run MONAI Security]
B --> C[Review Reports]
C --> D[Investigate Findings]
D --> E[Clinical Evaluation]
```

## Running the Audit

```bash
python monai_security.py security ./project --dataset ./dataset --model ./models --out ./audit
```

The audit is read-only and never modifies the project.

## Severity Levels

### ERROR
Issues requiring immediate investigation, such as corrupted files or missing mandatory components.

### WARNING
Potential risks including pickle-based model formats, duplicate images or incomplete bundle documentation.

### INFO
Additional metadata supporting reproducibility, including software versions, hashes and detected transforms.

## Model Review

Supported formats include:

- .pt
- .pth
- .ckpt
- .onnx
- .ts
- .torchscript
- .safetensors

Pickle-based formats are highlighted because loading untrusted checkpoints may execute Python code.

## Dataset Review

The dataset scanner evaluates:

- empty files,
- duplicate content,
- NaN and infinity values,
- affine consistency,
- constant images,
- image-mask compatibility,
- NIfTI metadata.

## Transform Review

The transform scanner statically analyzes MONAI preprocessing pipelines without executing project code. It reports transform names, source locations and configured keys.

## Reports

Generated outputs include:

- JSON
- Markdown
- HTML
- PDF
- summary.txt

## Best Practices

- Review all warnings before using a model.
- Archive reports with research documentation.
- Verify dataset provenance.
- Repeat audits after project updates.

## Limitations

MONAI Security does not assess clinical performance, replace validation studies, execute models or provide regulatory certification.

## Summary

MONAI Security helps radiologists verify the technical integrity of MONAI-based AI projects and supports reproducible, transparent medical AI workflows.

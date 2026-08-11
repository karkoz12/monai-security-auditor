# Reports

MONAI Security generates multiple report formats from a single audit execution. Each report targets a different audience while using the same underlying audit data.

## Reporting Workflow

```{mermaid}
flowchart LR
    A[Security Assessment] --> B[Audit Findings]
    B --> C[JSON]
    B --> D[Markdown]
    B --> E[HTML]
    B --> F[PDF]
    B --> G[Summary]
```

## Generated Files

After a successful assessment, the output directory contains:

```text
monai_security_report/
├── monai_security_report.json
├── monai_security_report.md
├── monai_security_report.html
├── monai_security_report.pdf
├── summary.txt
├── dependencies.json
├── model_files.json
├── dataset_metadata.json
├── monai_transforms.json
└── pip_freeze.txt
```

## JSON Report

The JSON report is the primary machine-readable output. It contains:

- project information,
- execution environment,
- audit findings,
- dependency inventory,
- model metadata,
- dataset metadata,
- MONAI transform analysis.

It is intended for automation, CI/CD pipelines and further processing.

## Markdown Report

The Markdown report summarizes the assessment in a human-readable format with grouped findings and tables. It is suitable for version control, documentation and publication supplements.

## HTML Report

The HTML report provides an interactive overview including:

- executive summary,
- findings table,
- dependency inventory,
- model inventory,
- dataset metadata,
- transform review.

It is intended for day-to-day review in a web browser.

## PDF Report

When ReportLab is installed, a PDF report is generated for distribution and archival. If ReportLab is unavailable, the remaining report formats are still produced.

## Summary Report

`summary.txt` provides a compact overview of:

- audited project,
- dataset,
- model,
- numbers of scanned objects,
- numbers of findings by severity.

## Scanner Outputs

Individual scanners also generate structured outputs:

| File | Produced by |
|------|-------------|
| `dependencies.json` | Dependency Scanner |
| `model_files.json` | Model File Scanner |
| `dataset_metadata.json` | Dataset Metadata Scanner |
| `monai_transforms.json` | MONAI Transform Scanner |
| `pip_freeze.txt` | Dependency Scanner |

## Report Contents

Every report is derived from the same audit payload and may include:

- project path,
- dataset path,
- model path,
- Python environment,
- operating system,
- findings,
- recommendations,
- integrity metadata,
- SHA-256 hashes.

## Error Handling

Report generation is fault tolerant.

- JSON, Markdown and HTML reports are always attempted.
- PDF generation is optional.
- Individual scanner failures are reported without aborting the complete assessment.

## Summary

The reporting subsystem separates machine-readable data from human-readable documentation while ensuring that every report is generated from the same verified audit results.

# First Assessment

This tutorial walks through the first security assessment performed with MONAI Security.

## Prerequisites

- Install project dependencies.
- Prepare a MONAI project.
- Optionally prepare dataset and model directories.

## Running the Audit

```bash
python monai_security.py security ./my_project --dataset ./data --model ./models --out ./audit_results
```

If dataset or model paths are omitted, MONAI Security attempts automatic discovery.

## Workflow

```{mermaid}
flowchart LR
A[Select Project]-->B[Run Audit]
B-->C[Execute Scanners]
C-->D[Generate Reports]
D-->E[Review Findings]
```

## Generated Reports

```text
audit_results/
├── monai_security_report.json
├── monai_security_report.md
├── monai_security_report.html
├── monai_security_report.pdf
├── summary.txt
├── dependencies.json
├── dataset_metadata.json
├── model_files.json
├── monai_transforms.json
└── pip_freeze.txt
```

## Severity Levels

### ERROR
Critical issues that should be resolved before using the project.

### WARNING
Potential risks requiring review.

### INFO
Additional information supporting reproducibility.

## Recommended Review Order

1. Read `summary.txt`.
2. Open the HTML report.
3. Review the Markdown report.
4. Inspect JSON outputs if detailed analysis is required.

## After the Assessment

- Investigate all ERROR findings.
- Review WARNING findings.
- Archive the generated reports.
- Repeat the audit after major project changes.

## Summary

The first assessment establishes a reproducible baseline for the technical integrity and security posture of a MONAI-based medical AI project.

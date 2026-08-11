# Administrator Guide

This guide describes how system administrators can deploy, execute, and maintain MONAI Security in research laboratories, hospitals, and development environments.

## Purpose

Administrators are responsible for ensuring that MONAI Security can be executed consistently, securely, and reproducibly across supported systems.

Typical responsibilities include:

- installing required dependencies,
- maintaining Python environments,
- configuring project access,
- storing audit reports,
- integrating audits into automated workflows.

## Deployment

MONAI Security is designed to run as a standalone command-line application.

Typical installation:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Verify the installation:

```bash
python monai_security.py --help
```

## Running Audits

Example:

```bash
python monai_security.py security ./project \
    --dataset ./dataset \
    --model ./models \
    --out ./audit
```

The application performs read-only inspection and writes all generated artifacts to the selected output directory.

## Output Management

A typical output directory contains:

```text
audit/
├── monai_security_report.json
├── monai_security_report.md
├── monai_security_report.html
├── monai_security_report.pdf
├── dependencies.json
├── dataset_metadata.json
├── model_files.json
├── monai_transforms.json
├── pip_freeze.txt
└── summary.txt
```

Administrators should archive these reports together with the audited project version.

## Environment Management

Recommended practices:

- use isolated Python virtual environments,
- pin package versions,
- maintain reproducible dependency files,
- keep MONAI and Python updated,
- archive `pip_freeze.txt` with reports.

## Permissions

The audit process requires read access to:

- project source code,
- datasets,
- model artifacts.

Write access is only required for the configured output directory.

## Automation

MONAI Security can be integrated into CI/CD workflows.

Typical pipeline:

```{mermaid}
flowchart LR
A[Source Code] --> B[CI Pipeline]
B --> C[Run MONAI Security]
C --> D[Generate Reports]
D --> E[Archive Results]
```

Administrators may execute the audit before releases, publications, or deployment to production systems.

## Log and Report Retention

Recommended retention includes:

- JSON reports,
- HTML reports,
- PDF reports,
- dependency inventories,
- dataset metadata,
- model inventories,
- software version records.

These artifacts support traceability and reproducibility.

## Security Considerations

MONAI Security:

- does not execute project code,
- does not load model checkpoints,
- does not modify datasets,
- does not install software automatically,
- performs static analysis whenever possible.

## Troubleshooting

Common issues include:

- missing optional libraries,
- unreadable files,
- missing datasets,
- invalid project paths,
- PDF generation unavailable because ReportLab is not installed.

Most errors are reported as findings while the remaining scanners continue to execute.

## Best Practices

- Audit every release candidate.
- Preserve reports with project archives.
- Review warnings before deployment.
- Repeat assessments after dependency updates.
- Verify dataset integrity regularly.

## Summary

MONAI Security provides administrators with a lightweight, read-only auditing framework for MONAI-based medical AI projects. Proper deployment and routine execution improve reproducibility, documentation quality, and operational security.

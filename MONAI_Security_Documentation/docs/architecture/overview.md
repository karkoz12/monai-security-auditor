# System Architecture

MONAI Security is a defensive auditing framework for MONAI-based medical AI projects. Its architecture is organized around a central auditor that coordinates independent scanners and produces structured security and integrity reports.

The implementation follows a sequential, read-only assessment model. It inspects the project environment, model artifacts, dataset files, MONAI transforms, and bundle structure without modifying the audited project.

## Architectural Overview

```{mermaid}
flowchart TD
    A[Command-Line Interface] --> B[MonaiSecurityAuditor]
    B --> C[Dependency Scanner]
    B --> D[Model File Scanner]
    B --> E[Dataset Metadata Scanner]
    B --> F[MONAI Transform Scanner]
    B --> G[MONAI Bundle Scanner]

    C --> H[Audit Issues]
    D --> H
    E --> H
    F --> H
    G --> H

    C --> I[Dependency Records]
    D --> J[Model File Records]
    E --> K[Dataset File Records]
    F --> L[Transform Records]

    H --> M[Report Generator]
    I --> M
    J --> M
    K --> M
    L --> M

    M --> N[JSON Report]
    M --> O[Markdown Report]
    M --> P[HTML Report]
    M --> Q[PDF Report]
    M --> R[Text Summary]
```

## Core Components

### Command-Line Interface

The command-line interface is implemented with `argparse`.

The main command is:

```text
python monai_security.py security <PROJECT> [OPTIONS]
```

Supported options include:

- `--dataset` — dataset root directory,
- `--model` — model file or model directory,
- `--out` — output directory.

The CLI creates an instance of `MonaiSecurityAuditor`, starts the complete assessment, and prints the paths of generated reports.

### Audit Orchestrator

The `MonaiSecurityAuditor` class is the central coordination component.

It is responsible for:

- resolving project, dataset, model, and output paths,
- detecting common dataset and model locations,
- executing all scanners,
- collecting findings and metadata records,
- generating reports.

The complete audit is initiated through:

```python
auditor.run_all()
```

The scanners are executed sequentially in the following order:

1. dependency scanner,
2. model file scanner,
3. dataset metadata scanner,
4. MONAI transform scanner,
5. MONAI Bundle scanner,
6. report generator.

## Data Model

The application uses dataclasses to represent findings and scanner output.

### AuditIssue

Represents a security, integrity, reproducibility, or configuration finding.

Fields:

- `level`,
- `scanner`,
- `category`,
- `path`,
- `message`,
- `recommendation`.

Supported levels currently include:

- `ERROR`,
- `WARNING`,
- `INFO`.

### DependencyRecord

Stores an installed package and its version.

Fields:

- package name,
- version,
- source.

### ModelFileRecord

Stores model artifact metadata.

Fields:

- path,
- file size,
- SHA-256 checksum,
- extension,
- risk notes.

### DatasetFileRecord

Stores dataset file metadata.

Fields include:

- path,
- file size,
- SHA-256 checksum,
- extension,
- image shape,
- data type,
- minimum and maximum intensity,
- unique values,
- affine determinant.

### TransformRecord

Stores information about detected MONAI transforms.

Fields:

- Python source file,
- source line,
- transform name,
- configured keys,
- review notes.

## Scanner Architecture

Each scanner is implemented as a method of `MonaiSecurityAuditor`. Scanners share the same issue collection mechanism through `add_issue()`.

This approach gives all scanners a consistent output schema and allows findings to be combined into a single report.

### Dependency Scanner

The dependency scanner:

- checks required Python packages,
- records installed versions,
- captures `pip freeze`,
- examines `requirements*.txt` and lock files,
- reports remote dependency references,
- reports potentially unpinned dependencies.

The scanner writes:

```text
dependencies.json
pip_freeze.txt
```

### Model File Scanner

The model scanner searches for supported artifacts:

```text
.pt
.pth
.ckpt
.onnx
.ts
.torchscript
.safetensors
```

For every model artifact, it records:

- size,
- extension,
- SHA-256 checksum,
- format-related risk notes.

Pickle-based PyTorch formats are reported for additional review because unsafe loading may execute embedded Python code.

The scanner writes:

```text
model_files.json
```

### Dataset Metadata Scanner

The dataset scanner recursively processes files under the selected dataset root.

It performs:

- SHA-256 hashing,
- empty-file detection,
- duplicate-content detection,
- NIfTI metadata inspection,
- NaN and infinity detection,
- constant-image detection,
- affine matrix validation,
- mask-value inspection,
- image-mask shape comparison.

NIfTI-specific inspection requires `nibabel`.

The scanner writes:

```text
dataset_metadata.json
```

### MONAI Transform Scanner

The transform scanner analyzes Python source files with the standard-library `ast` module.

It detects selected MONAI transforms and extracts:

- transform names,
- source locations,
- configured `keys`,
- transform-specific review notes.

The scanner does not execute project code. It performs static source analysis.

The scanner writes:

```text
monai_transforms.json
```

### MONAI Bundle Scanner

The bundle scanner searches for MONAI Bundle-like directory structures.

It checks for:

- configuration files,
- metadata files,
- documentation,
- model artifacts.

When expected elements are missing, the scanner produces recommendations for improving bundle completeness and traceability.

## Path Discovery

When paths are not provided explicitly, the auditor attempts automatic discovery.

### Dataset Discovery

The following directories are checked:

```text
data/
dataset/
datasets/
images/
```

### Model Discovery

The auditor first checks:

```text
models/
```

If that directory is unavailable, it searches the project recursively for supported model file formats.

## Integrity Mechanisms

### SHA-256 Hashing

Model and dataset files are hashed with SHA-256.

Files are processed in chunks to avoid loading large artifacts entirely into memory.

Checksums support:

- artifact identification,
- duplicate detection,
- integrity verification,
- reproducibility records,
- comparison across audit runs.

### Read-Only Operation

The scanner reads project files and creates reports only in the configured output directory.

It does not:

- execute model files,
- load PyTorch checkpoints,
- modify datasets,
- change project source code,
- install dependencies,
- exploit detected weaknesses.

## Reporting Architecture

All findings and records are combined into one payload containing:

- audited paths,
- Python and platform information,
- issues,
- dependency records,
- model records,
- dataset records,
- transform records.

The payload is passed to several report builders.

### JSON

The JSON report contains the complete structured audit result and is intended for:

- automation,
- integration,
- archival,
- downstream analysis.

### Markdown

The Markdown report provides a readable technical report with tables and grouped findings.

### HTML

The HTML report provides a browser-based dashboard with:

- executive summary,
- findings table,
- dependency inventory,
- model artifact inventory,
- dataset metadata,
- transform review.

### PDF

The PDF report is generated with ReportLab when available.

If ReportLab is missing, the application records a warning and continues generating the remaining formats.

### Text Summary

The text summary contains basic counts and audit scope information for quick review or command-line workflows.

## Error Handling

The architecture favors partial completion instead of terminating the entire assessment.

Examples include:

- missing optional libraries are reported as findings,
- unreadable files generate scanner issues,
- Python parsing errors are reported without stopping other files,
- PDF generation failure does not prevent JSON, Markdown, or HTML output,
- missing dataset or model paths are reported and the remaining scanners continue.

This behavior is important for large medical AI projects where one malformed artifact should not prevent the remaining assessment.

## Security Boundaries

MONAI Security is designed as a defensive inspection tool.

The current architecture intentionally avoids:

- loading untrusted pickle-based model files,
- executing analyzed project source code,
- dynamically importing project modules,
- modifying audited assets,
- performing exploitation or penetration testing.

Static analysis and metadata inspection reduce the risk created by untrusted medical AI artifacts.

## Extension Points

The current architecture can be extended by adding new scanner methods to `MonaiSecurityAuditor`.

A new scanner should:

1. inspect one clearly defined area,
2. create findings with `add_issue()`,
3. store structured records where appropriate,
4. avoid executing untrusted project content,
5. write scanner-specific JSON output if needed,
6. be added to `run_all()`.

Potential extensions include:

- DICOM metadata privacy inspection,
- software bill of materials generation,
- CVE database integration,
- model signature verification,
- configuration schema validation,
- provenance validation,
- risk scoring,
- CI/CD integration.

## Architectural Limitations

The current implementation has several limitations:

- scanners run sequentially,
- there is no plugin registry,
- severity scoring is qualitative,
- transform detection covers a predefined list,
- dataset deep inspection primarily targets NIfTI,
- bundle detection is heuristic,
- no external vulnerability database is queried,
- no cryptographic signature validation is implemented,
- configuration is primarily CLI-based.

These limitations are suitable targets for future versions.

## Summary

MONAI Security uses a modular defensive architecture centered on `MonaiSecurityAuditor`.

The architecture separates:

- command-line input,
- path discovery,
- scanner execution,
- structured findings,
- integrity metadata,
- multi-format reporting.

This design supports transparent, reproducible, and extensible security assessment of MONAI-based medical AI projects.

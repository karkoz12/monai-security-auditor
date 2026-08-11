# GUI Guide

This guide explains how to use the graphical user interface (GUI) of MONAI Security to perform security assessments of MONAI-based medical AI projects.

## Overview

The GUI provides a user-friendly interface for configuring projects, running security assessments, monitoring progress, and opening generated reports.

The graphical interface uses the same auditing engine as the command-line version.

## Main Window

The main window is divided into four areas:

1. Security Assessment Setup
2. Dashboard
3. Security Log
4. Report Viewer

```{mermaid}
flowchart LR
A[Project Configuration] --> B[Run Assessment]
B --> C[Dashboard]
B --> D[Security Log]
B --> E[Generated Reports]
```

## Security Assessment Setup

The left panel contains the project configuration.

### Project

Select the root directory of the MONAI project.

### Dataset

Optionally select the dataset directory.

### Model

Select either:

- a single model file, or
- a directory containing model artifacts.

Supported formats include:

- `.pt`
- `.pth`
- `.ckpt`
- `.onnx`
- `.ts`
- `.torchscript`
- `.safetensors`

### Output

Choose the directory where reports will be generated.

## Automatic Detection

The **Auto-detect dataset/model** button searches the selected project for common dataset and model locations.

Typical dataset folders:

- `data`
- `dataset`
- `datasets`
- `images`

Model files are detected recursively using supported file extensions.

## Running an Assessment

Click **Run MONAI Security Assessment**.

The GUI starts the same audit performed by the command-line interface.

During execution:

- the dashboard is reset,
- the security log is updated,
- generated reports are written to the selected output directory.

The **Stop** button terminates the running assessment.

## Dashboard

The dashboard summarizes the audit results.

### Model Safety Score

Displays the calculated safety score when available.

### Status

Displays the overall assessment status.

### Recommended Action

Provides a high-level recommendation based on the audit findings.

If no score is available, the GUI displays a summary based on detected issues.

## Security Log

The log window displays:

- executed command,
- scanner progress,
- warnings,
- errors,
- completion status.

The log is updated while the assessment is running.

## Report Viewer

After a successful assessment, the GUI provides shortcuts to:

- Open PDF
- Open HTML
- Radiologist View
- Developer View
- Open Output Folder

These buttons open the generated reports directly.

## Demo Projects

The GUI includes demonstration shortcuts.

### PASS Demo

Loads a project configured to complete the assessment without significant findings.

### ISSUE Demo

Loads a project containing intentionally introduced issues for demonstration and testing.

These examples are useful for training and validation.

## Typical Workflow

1. Select a project.
2. Use automatic detection if desired.
3. Verify dataset and model paths.
4. Choose an output directory.
5. Run the assessment.
6. Review the dashboard.
7. Open the generated reports.
8. Investigate reported findings.

## Troubleshooting

Common issues include:

- invalid project paths,
- missing datasets,
- unsupported model locations,
- unavailable optional libraries,
- missing report files after interrupted execution.

The security log provides detailed diagnostic information.

## Best Practices

- Audit projects before publication or deployment.
- Archive generated reports.
- Repeat assessments after project updates.
- Review warnings before clinical evaluation.
- Use the HTML report for interactive analysis.

## Summary

The GUI provides an intuitive interface for configuring and running MONAI Security assessments while exposing the same functionality as the command-line interface. It simplifies project selection, report access, and result interpretation for researchers, radiologists, administrators, and developers.

# Command-Line Interface (CLI)

## Command

```text
python monai_security.py security <PROJECT> [OPTIONS]
```

## Usage

```powershell
python monai_security.py security . --dataset data --out monai_security_report
```

```powershell
python monai_security.py security . --dataset data --model model.pt --out monai_security_report
```

```powershell
python monai_security.py security . --dataset data --model models --out monai_security_report
```

## Arguments

| Option | Description |
|---|---|
| PROJECT | Project root to audit |
| --dataset | Dataset directory (optional; auto-detected if omitted) |
| --model | Model file or directory (optional; auto-detected if omitted) |
| --out | Output directory (default: monai_security_report) |

## Executed Scanners

1. Dependency Scanner
2. Model File Scanner
3. Dataset Metadata Scanner
4. MONAI Transform Scanner
5. MONAI Bundle Scanner

## Reports

JSON, Markdown, HTML, PDF, summary.txt, dependencies.json, model_files.json, dataset_metadata.json, monai_transforms.json and pip_freeze.txt (if available).

## Notes

The audit is read-only and defensive.
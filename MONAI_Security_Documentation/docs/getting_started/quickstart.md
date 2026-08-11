# Quickstart

This guide runs a complete audit with the current MONAI Security prototype.

The command-line engine is provided by `monoai_audyt.py`. The required command is `audit`.

---

## Prepare the Files

Place the audit engine and optional GUI in one directory:

```text
monai_security/
├── monoai_audyt.py
├── monoai_gui.py
└── project_to_audit/
```

A typical MONAI project may look like:

```text
project_to_audit/
├── data/
│   ├── images/
│   └── labels/
├── models/
│   └── model.safetensors
├── configs/
├── train.py
├── inference.py
└── requirements.txt
```

The dataset and model locations are optional because the engine attempts automatic detection. Supplying them explicitly is recommended for a controlled and reproducible audit.

---

## Activate the Environment

```powershell
conda activate monai_security_env
```

Confirm that the engine is available:

```powershell
python .\monoai_audyt.py audit --help
```

---

## Run a Basic Audit

From the directory containing `monoai_audyt.py`, run:

```powershell
python .\monoai_audyt.py audit .\project_to_audit
```

The default output directory is:

```text
monoai_audit_report
```

---

## Run an Explicit Audit

For the most reproducible workflow, provide the project, dataset, model, and output paths:

```powershell
python .\monoai_audyt.py audit `
  .\project_to_audit `
  --dataset .\project_to_audit\data `
  --model .\project_to_audit\models `
  --out .\project_to_audit\audit_output
```

The `--model` option can point to either:

- one model file, or
- a directory containing model artifacts.

Recognized model formats include:

```text
.pt
.pth
.ckpt
.onnx
.ts
.torchscript
.safetensors
```

---

## Limit the Number of Files

The default maximum number of scanned files is 5000.

To change it:

```powershell
python .\monoai_audyt.py audit `
  .\project_to_audit `
  --dataset .\project_to_audit\data `
  --model .\project_to_audit\models `
  --out .\project_to_audit\audit_output `
  --max-files 10000
```

A limit prevents unexpectedly large projects or datasets from causing an unbounded scan.

---

## Use Strict Preflight Mode

Strict mode prevents the scanners from running when the preflight stage reports blocking errors:

```powershell
python .\monoai_audyt.py audit `
  .\project_to_audit `
  --dataset .\project_to_audit\data `
  --model .\project_to_audit\models `
  --out .\project_to_audit\audit_output `
  --strict
```

Without `--strict`, the engine records preflight problems and continues where possible.

---

## What the Audit Checks

The current engine performs the following high-level stages:

1. preflight validation,
2. dependency inspection,
3. model-file inspection,
4. dataset metadata inspection,
5. MONAI Bundle structure inspection,
6. risk-score calculation,
7. report generation.

Examples of recorded findings include:

- missing or inaccessible paths,
- missing Python dependencies,
- unrecognized model formats,
- pickle-based PyTorch checkpoints,
- model SHA256 hashes,
- invalid NIfTI files,
- NIfTI arrays containing `NaN` or infinite values,
- metadata-like files that may require privacy review,
- incomplete MONAI Bundle metadata, documentation, or model artifacts.

The scanner catches individual scanner failures and records them instead of terminating the entire audit wherever possible.

---

## Expected Console Output

After a successful run, the console displays a summary similar to:

```text
MonoAI robust audit finished.
Score: 86/100
Status: Ready for controlled validation
Recommended action: Proceed with controlled research validation. Keep audit reports with the experiment.

Reports:
json: ...
html: ...
summary: ...
issues_csv: ...
manifest: ...
```

The exact score and status depend on the detected findings.

---

## Generated Output

The output directory follows a structured layout:

```text
audit_output/
├── reports/
│   ├── security_report.html
│   ├── security_report.pdf
│   ├── radiologist_view.html
│   └── developer_view.html
├── json/
│   ├── security_report.json
│   ├── manifest.json
│   └── preflight.json
├── csv/
│   └── issues.csv
└── logs/
```

The exact set of generated files may depend on the installed dependencies and the current module version.

### Main reports

- `security_report.html` — primary browser-readable report,
- `security_report.pdf` — shareable PDF report,
- `radiologist_view.html` — simplified view for clinical reviewers,
- `developer_view.html` — more technical findings view,
- `security_report.json` — structured machine-readable audit data,
- `issues.csv` — tabular list of findings,
- `manifest.json` — audit environment and command metadata,
- `preflight.json` — path, dependency, and permission checks.

---

## Review the Risk Score

The current score begins at 100 and is reduced when findings are recorded.

The report assigns one of the following general statuses:

| Score | Status |
|---:|---|
| 85–100 | Ready for controlled validation |
| 70–84 | Use only for research validation |
| 50–69 | High caution |
| 0–49 | Not ready |

The score is a technical project-readiness indicator. It is not a clinical-performance score and does not certify the model for clinical deployment.

---

## Run the GUI

Start the graphical interface:

```powershell
python .\monoai_gui.py
```

Then:

1. Select the MONAI project folder.
2. Select the dataset folder or use automatic detection.
3. Select a model file or model directory.
4. Select the output folder.
5. Click **Run MonoAI Audit**.
6. Review the log and score.
7. Open the generated HTML, PDF, radiologist, or developer report.

The GUI runs the same command-line engine in a separate process.

---

## Example for the Current Windows Project

Using a project located under:

```text
C:\Users\kozakka\monai_test\audit_cyber_monoai
```

an example command is:

```powershell
python .\monoai_audyt.py audit `
  C:\Users\kozakka\monai_test\audit_cyber_monoai `
  --dataset C:\Users\kozakka\monai_test\audit_cyber_monoai\data `
  --model C:\Users\kozakka\monai_test\audit_cyber_monoai\models `
  --out C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_audit_report
```

Adjust the dataset and model paths to match the actual project structure.

---

## Open the Reports

After the audit, open the main HTML report:

```powershell
Start-Process .\project_to_audit\audit_output\reports\security_report.html
```

Open the output directory:

```powershell
explorer .\project_to_audit\audit_output
```

---

## Next Steps

After the first audit:

1. review all `ERROR` and `WARNING` findings,
2. verify model provenance and SHA256 hashes,
3. inspect dataset integrity findings,
4. add missing MONAI Bundle metadata and documentation,
5. pin project dependencies,
6. rerun the audit,
7. archive the report with the experiment or model release.

MONAI Security supports technical review and research reproducibility. It does not replace clinical validation, regulatory assessment, or formal penetration testing.

# Installation

This page describes how to install and prepare the current MONAI Security prototype based on:

- `monoai_audyt.py` — command-line audit engine,
- `monoai_gui.py` — optional graphical interface.

MONAI Security is currently distributed as a source-code prototype rather than as a published Python package. The files should therefore be placed together in the same project directory.

---

## System Requirements

The current prototype is intended for research and development environments.

Recommended configuration:

- Windows 10 or Windows 11,
- Python 3.10 or newer,
- a dedicated Python virtual environment,
- sufficient read access to the analyzed project, dataset, and model files,
- write access to the selected report directory.

The graphical interface uses Tkinter, which is included with standard Windows Python installations.

---

## Create a Virtual Environment

Using Conda:

```powershell
conda create -n monai_security_env python=3.11 -y
conda activate monai_security_env
```

Alternatively, using the standard Python virtual environment module:

```powershell
python -m venv monai_security_env
.\monai_security_env\Scripts\Activate.ps1
```

---

## Install Core Dependencies

Install the dependencies used by the current audit engine:

```powershell
python -m pip install --upgrade pip
python -m pip install numpy nibabel scipy pydicom reportlab monai torch
```

The current implementation checks for the following modules:

| Dependency | Purpose |
|---|---|
| `numpy` | Numerical and image-array analysis |
| `nibabel` | Loading and validating NIfTI files |
| `scipy` | Supporting scientific and imaging operations |
| `pydicom` | DICOM-related support |
| `reportlab` | PDF report generation |
| `monai` | MONAI environment and pipeline support |
| `torch` | PyTorch model and runtime support |

Some scanners can continue when an optional dependency is unavailable. Missing dependencies may nevertheless appear as warnings or errors in the preflight report.

---

## Recommended Project Layout

Place the command-line engine and GUI in the same directory:

```text
monai_security/
├── monoai_audyt.py
├── monoai_gui.py
├── example_project/
├── requirements.txt
└── README.md
```

The current GUI expects `monoai_audyt.py` to be located in the same folder as `monoai_gui.py`.

---

## Optional Requirements File

A minimal `requirements.txt` for the current prototype can contain:

```text
numpy
nibabel
scipy
pydicom
reportlab
monai
torch
```

Install it with:

```powershell
python -m pip install -r requirements.txt
```

For reproducible research, replace unpinned dependency names with versions validated in your environment.

Example:

```text
numpy==2.1.3
nibabel==5.3.2
scipy==1.14.1
pydicom==3.0.1
reportlab==4.2.5
monai==1.4.0
torch==2.5.1
```

The example versions are illustrative. Use versions tested with your project and hardware.

---

## Verify the Command-Line Installation

From the directory containing `monoai_audyt.py`, run:

```powershell
python .\monoai_audyt.py
```

The application should display the command help because no audit subcommand was provided.

You can also request audit help explicitly:

```powershell
python .\monoai_audyt.py audit --help
```

The help output should include:

- the project directory argument,
- `--dataset`,
- `--model`,
- `--out`,
- `--max-files`,
- `--strict`.

---

## Verify the GUI Installation

Run:

```powershell
python .\monoai_gui.py
```

The MONAI Security window should open and provide selectors for:

- project directory,
- dataset directory,
- model file or model directory,
- output directory.

The GUI also provides automatic dataset and model detection, an audit log, risk-score summary, and buttons for opening generated reports.

---

## Verify Installed Dependencies

Run:

```powershell
python -c "import numpy, nibabel, scipy, pydicom, reportlab, monai, torch; print('MONAI Security dependencies are available.')"
```

Expected output:

```text
MONAI Security dependencies are available.
```

If an import fails, install the missing package with:

```powershell
python -m pip install PACKAGE_NAME
```

---

## GPU Support

A GPU is not required for the current static audit workflow.

Most operations involve:

- file discovery,
- hashing,
- metadata inspection,
- NIfTI validation,
- source and project-structure analysis,
- report generation.

PyTorch and MONAI may be installed with CPU support unless the audited project or future runtime tests require CUDA.

---

## Permissions

MONAI Security performs read-oriented analysis of project assets, but it must be able to create the output directory and report files.

Before running an audit, confirm that:

- the project directory exists,
- the dataset directory is readable,
- the model file or directory is readable,
- the output directory is writable.

The preflight stage records these checks before executing the scanners.

---

## Troubleshooting

### `monoai_audyt.py` was not found

Make sure the GUI and engine are in the same directory:

```text
monoai_gui.py
monoai_audyt.py
```

### `ModuleNotFoundError`

Install the missing package:

```powershell
python -m pip install PACKAGE_NAME
```

Make sure the intended virtual environment is active.

### PowerShell blocks environment activation

Run PowerShell as the current user and, where permitted by local policy, use:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the environment again.

### PDF report is not generated

Install ReportLab:

```powershell
python -m pip install reportlab
```

### MONAI or PyTorch is unavailable

Install both packages:

```powershell
python -m pip install monai torch
```

The audit may still complete partially, but dependency-related warnings will be recorded.

---

## Development Status

MONAI Security is currently a research prototype. It is not yet installed through a command such as:

```powershell
pip install monai-security
```

Until packaging is added, run the engine and GUI directly from their Python source files.

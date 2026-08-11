"""
generate_monai_security_docs.py

Generate a complete Sphinx + MyST documentation portal for the MONAI Security module.

Usage:

    python generate_monai_security_docs.py

Then build the documentation:

    cd monai_security_docs/docs
    pip install -r requirements.txt
    python -m sphinx -b html . _build/html

Open:

    monai_security_docs/docs/_build/html/index.html
"""

from __future__ import annotations

from pathlib import Path
import shutil


PROJECT_DIR = Path("monai_security_docs")


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def main() -> None:
    root = PROJECT_DIR
    docs = root / "docs"

    if root.exists():
        shutil.rmtree(root)

    folders = [
        docs / "_static",
        docs / "_templates",
        docs / "getting_started",
        docs / "architecture",
        docs / "scanners",
        docs / "reports",
        docs / "clinical",
        docs / "developer",
        docs / "administrator",
        docs / "security",
        docs / "tutorials",
        docs / "examples",
        docs / "api",
        root / "examples",
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    write_file(root / "README.md", """
    # MONAI Security Documentation Portal

    This folder contains a Sphinx + MyST Markdown documentation portal for the
    **MONAI Security** module.

    ## Build HTML

    ```powershell
    cd monai_security_docs\\docs
    pip install -r requirements.txt
    python -m sphinx -b html . _build\\html
    ```

    Open:

    ```text
    monai_security_docs\\docs\\_build\\html\\index.html
    ```

    ## Build on Linux/macOS

    ```bash
    cd monai_security_docs/docs
    pip install -r requirements.txt
    python -m sphinx -b html . _build/html
    ```
    """)

    write_file(docs / "requirements.txt", """
    sphinx>=7.0
    myst-parser>=2.0
    furo>=2024.1.29
    sphinx-copybutton>=0.5
    sphinx-design>=0.6
    sphinxcontrib-mermaid>=0.9
    sphinx-autodoc-typehints>=2.0
    """)

    write_file(docs / "conf.py", """
    from pathlib import Path
    import sys

    ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(ROOT))

    project = "MONAI Security"
    author = "MONAI Security Contributors"
    release = "0.1.0"

    extensions = [
        "myst_parser",
        "sphinx_copybutton",
        "sphinx_design",
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.viewcode",
        "sphinxcontrib.mermaid",
        "sphinx_autodoc_typehints",
    ]

    source_suffix = {
        ".rst": "restructuredtext",
        ".md": "markdown",
    }

    myst_enable_extensions = [
        "colon_fence",
        "deflist",
        "fieldlist",
        "tasklist",
        "attrs_inline",
        "attrs_block",
    ]

    templates_path = ["_templates"]
    exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

    html_theme = "furo"
    html_title = "MONAI Security Documentation"
    html_static_path = ["_static"]

    html_theme_options = {
        "sidebar_hide_name": False,
        "navigation_with_keys": True,
        "light_css_variables": {
            "color-brand-primary": "#0066cc",
            "color-brand-content": "#0066cc",
        },
        "dark_css_variables": {
            "color-brand-primary": "#58a6ff",
            "color-brand-content": "#58a6ff",
        },
    }

    pygments_style = "sphinx"
    pygments_dark_style = "monokai"

    copybutton_prompt_text = r">>> |\\.\\.\\. |\\$ |PS "
    copybutton_prompt_is_regexp = True

    autodoc_member_order = "bysource"
    autodoc_typehints = "description"

    latex_engine = "xelatex"
    latex_documents = [
        ("index", "monai_security_documentation.tex", "MONAI Security Documentation", author, "manual"),
    ]
    """)

    write_file(docs / "Makefile", """
    SPHINXOPTS    ?=
    SPHINXBUILD   ?= sphinx-build
    SOURCEDIR     = .
    BUILDDIR      = _build

    .PHONY: help html clean latexpdf

    help:
    \t@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

    html:
    \t@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

    latexpdf:
    \t@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

    clean:
    \trm -rf "$(BUILDDIR)"
    """)

    write_file(docs / "make.bat", """
    @ECHO OFF
    set SPHINXBUILD=sphinx-build
    set SOURCEDIR=.
    set BUILDDIR=_build

    if "%1" == "" goto help

    %SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR%
    goto end

    :help
    %SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR%

    :end
    """)

    write_file(docs / "_static" / "custom.css", """
    .monai-security-hero {
      border-radius: 18px;
      padding: 2rem;
      background: linear-gradient(135deg, #0f172a, #1e40af);
      color: white;
      margin-bottom: 1.5rem;
    }

    .monai-security-badge {
      display: inline-block;
      padding: .25rem .6rem;
      border-radius: 999px;
      background: #dbeafe;
      color: #1e40af;
      font-weight: 700;
    }
    """)

    # Index
    write_file(docs / "index.md", """
    # MONAI Security Documentation

    :::{div} monai-security-hero
    # MONAI Security

    **Cybersecurity, integrity and readiness assessment for MONAI-based medical imaging AI pipelines.**

    MONAI Security is a defensive module for reviewing the security posture,
    integrity, reproducibility and clinical readiness of MONAI projects before
    research validation, publication, deployment preparation or institutional review.
    :::

    ```{mermaid}
    flowchart LR
        A[MONAI Project] --> B[Preflight]
        B --> C[Security Scanners]
        C --> D[Security Findings]
        D --> E[Reports]
        E --> F[Clinical View]
        E --> G[Developer View]
    ```

    ## What the module does

    MONAI Security audits the surrounding project infrastructure rather than the
    diagnostic accuracy of a neural network. It helps answer practical questions:

    - Is the model artifact identifiable and hashable?
    - Are the dataset files readable and internally consistent?
    - Are there corrupted NIfTI files, NaN values or suspicious masks?
    - Does the project contain MONAI transforms that affect reproducibility?
    - Is the MONAI Bundle-style structure complete enough for review?
    - Are reports available for clinical, technical and research documentation?

    ## What the module does not do

    MONAI Security does not approve a model for clinical use. It does not replace
    clinical validation, regulatory review, reader studies or diagnostic
    performance evaluation.

    ```{toctree}
    :maxdepth: 2
    :caption: Getting Started

    getting_started/overview
    getting_started/installation
    getting_started/quickstart
    getting_started/cli
    getting_started/gui
    ```

    ```{toctree}
    :maxdepth: 2
    :caption: Architecture

    architecture/overview
    architecture/workflow
    architecture/data_flow
    architecture/gui_architecture
    ```

    ```{toctree}
    :maxdepth: 2
    :caption: Security Scanners

    scanners/project_security
    scanners/dependency_security
    scanners/model_security
    scanners/dataset_security
    scanners/transform_security
    scanners/bundle_security
    scanners/integrity_verification
    ```

    ```{toctree}
    :maxdepth: 2
    :caption: Reports

    reports/overview
    reports/html_report
    reports/pdf_report
    reports/json_csv
    reports/summary
    ```

    ```{toctree}
    :maxdepth: 2
    :caption: Clinical and Security Guides

    clinical/radiologist_guide
    clinical/clinical_readiness
    security/threat_model
    security/supply_chain
    security/model_integrity
    security/dataset_integrity
    security/reproducibility
    ```

    ```{toctree}
    :maxdepth: 2
    :caption: Developer and Administrator Guides

    developer/developer_guide
    developer/extending_scanners
    administrator/administrator_guide
    tutorials/first_security_assessment
    tutorials/demo_project_assessment
    tutorials/batch_assessment
    examples/index
    api/index
    ```
    """)

    # Getting started
    write_file(docs / "getting_started" / "overview.md", """
    # Overview

    MONAI Security is a defensive cybersecurity audit module for MONAI-based
    medical imaging AI projects. It is designed for researchers, radiologists,
    machine learning engineers, MLOps teams and institutional security reviewers.

    The module focuses on the artifacts around a medical AI model:

    - source project structure
    - dataset files and metadata
    - model files
    - MONAI transforms
    - MONAI Bundle-style organization
    - dependency environment
    - generated reports and audit trail

    The goal is to identify weaknesses that can affect trust, reproducibility,
    data integrity and future clinical translation.

    ## Main value

    A typical medical AI project may contain a trained model, a dataset folder,
    a few scripts and configuration files. Even when the model performs well on a
    benchmark, the project may still be difficult to trust if the model file is
    not hashed, dataset provenance is unclear, MONAI Bundle metadata is missing
    or preprocessing is not reproducible.

    MONAI Security turns these concerns into a structured assessment.
    """)

    write_file(docs / "getting_started" / "installation.md", """
    # Installation

    ## Recommended Python environment

    ```powershell
    conda create -n monai_security_env python=3.11 -y
    conda activate monai_security_env
    ```

    ## Runtime dependencies

    ```powershell
    pip install monai torch nibabel numpy scipy pydicom reportlab
    ```

    `reportlab` is required for PDF generation. If it is missing, HTML, JSON,
    Markdown and CSV outputs can still be generated by the module variants that
    support graceful fallback.

    ## Documentation dependencies

    ```powershell
    cd monai_security_docs\\docs
    pip install -r requirements.txt
    ```

    ## Build the documentation portal

    ```powershell
    python -m sphinx -b html . _build\\html
    ```

    Open:

    ```text
    _build\\html\\index.html
    ```
    """)

    write_file(docs / "getting_started" / "quickstart.md", """
    # Quickstart

    ## Run a security assessment

    ```powershell
    python monai_security.py security .\\monai_test --dataset .\\monoai_demo_projects\\ --model .\\monoai_demo_projects\\ --out monai_security_report
    ```

    ## Expected outputs

    ```text
    monai_security_report/
    ├── monai_security_report.json
    ├── monai_security_report.md
    ├── monai_security_report.html
    ├── monai_security_report.pdf
    └── summary.txt
    ```

    ## Open the reports

    The HTML report is useful for interactive local review.

    The PDF report is useful for archiving, sharing with collaborators or
    including as supplementary documentation in a research project.
    """)

    write_file(docs / "getting_started" / "cli.md", """
    # Command Line Interface

    The main command is:

    ```powershell
    python monai_security.py security <project> --dataset <dataset> --model <model> --out <output>
    ```

    ## Example

    ```powershell
    python monai_security.py security .\\monai_test `
        --dataset .\\monoai_demo_projects\\ `
        --model .\\monoai_demo_projects\\ `
        --out monai_security_report
    ```

    ## Arguments

    `project`
    : Root folder of the MONAI project.

    `--dataset`
    : Dataset root folder. This may point to a clean dataset, demo project folder
      or a broader folder containing several medical imaging files.

    `--model`
    : Model file or folder. The scanner looks for `.pt`, `.pth`, `.ckpt`,
      `.onnx`, `.ts`, `.torchscript` and `.safetensors`.

    `--out`
    : Output folder for reports.
    """)

    write_file(docs / "getting_started" / "gui.md", """
    # GUI

    The GUI is a thin layer over the same security engine. It allows non-technical
    users to select folders, run the assessment and open reports.

    ## Typical workflow

    1. Select the MONAI project folder.
    2. Select the dataset folder.
    3. Select the model file or model folder.
    4. Select the output folder.
    5. Run the security assessment.
    6. Open HTML or PDF reports.

    ## Why GUI matters

    Radiologists and clinical researchers may not want to use command-line tools.
    A GUI lowers the barrier to first use while keeping the underlying assessment
    reproducible because it still calls the same Python engine.
    """)

    # Architecture
    write_file(docs / "architecture" / "overview.md", """
    # Architecture Overview

    MONAI Security is organized as a modular security assessment pipeline.

    ```{mermaid}
    flowchart TD
        Project[Project Folder] --> Engine[Security Engine]
        Engine --> Dep[Dependency Scanner]
        Engine --> Model[Model Security Scanner]
        Engine --> Dataset[Dataset Security Scanner]
        Engine --> Transform[MONAI Transform Scanner]
        Engine --> Bundle[MONAI Bundle Scanner]
        Dep --> Reports[Report Generator]
        Model --> Reports
        Dataset --> Reports
        Transform --> Reports
        Bundle --> Reports
        Reports --> HTML[HTML Report]
        Reports --> PDF[PDF Report]
        Reports --> JSON[JSON Report]
        Reports --> MD[Markdown Report]
    ```

    The engine coordinates scanner execution and report generation. Each scanner
    focuses on a specific part of the MONAI project and produces structured
    findings.
    """)

    write_file(docs / "architecture" / "workflow.md", """
    # Assessment Workflow

    A complete assessment follows these stages:

    1. Parse CLI or GUI inputs.
    2. Resolve project, dataset, model and output paths.
    3. Scan Python dependencies.
    4. Scan model files.
    5. Scan dataset metadata and NIfTI health.
    6. Scan MONAI transform usage.
    7. Scan MONAI Bundle-like structure.
    8. Generate JSON, Markdown, HTML, PDF and summary reports.

    The design is intentionally read-only. The module should not modify model
    files, datasets or source code during a security assessment.
    """)

    write_file(docs / "architecture" / "data_flow.md", """
    # Data Flow

    ```{mermaid}
    sequenceDiagram
        participant User
        participant GUI
        participant Engine
        participant Scanners
        participant Reports

        User->>GUI: Select project, dataset and model
        GUI->>Engine: Run security command
        Engine->>Scanners: Execute scanner methods
        Scanners-->>Engine: Return findings and metadata
        Engine->>Reports: Build JSON, HTML, PDF and summary
        Reports-->>User: Open reports
    ```

    All file content used for reports is derived from local project artifacts.
    The module does not require internet access for its core operation.
    """)

    write_file(docs / "architecture" / "gui_architecture.md", """
    # GUI Architecture

    The GUI is intentionally simple. It does not duplicate security logic. It
    launches the engine as a subprocess and streams the console output into a log
    window.

    ## Benefits

    - the CLI remains scriptable
    - the GUI remains thin and maintainable
    - both interfaces produce the same reports
    - failures in the engine do not freeze the GUI
    """)

    # Scanners
    scanner_pages = {
        "project_security": ("Project Security Scanner", "Reviews project layout, available folders, configuration files and general readiness."),
        "dependency_security": ("Dependency Security Scanner", "Reviews installed Python packages and dependency declarations for reproducibility and supply-chain risk."),
        "model_security": ("Model Security Scanner", "Hashes model files and flags risky formats such as pickle-based PyTorch checkpoints."),
        "dataset_security": ("Dataset Security Scanner", "Reviews dataset files, NIfTI metadata, NaN/Inf values, constant images, masks and image-label shape consistency."),
        "transform_security": ("MONAI Transform Security Scanner", "Parses Python files and detects MONAI transforms that affect reproducibility or geometry."),
        "bundle_security": ("MONAI Bundle Security Scanner", "Checks whether the project follows a MONAI Bundle-like structure with configs, docs, metadata and model artifacts."),
        "integrity_verification": ("Integrity Verification", "Uses SHA256 hashes to create an audit trail for model and dataset files."),
    }

    for filename, (title, summary) in scanner_pages.items():
        write_file(docs / "scanners" / f"{filename}.md", f"""
        # {title}

        {summary}

        ## Why it matters

        Security in medical AI is not limited to network attacks. A project can
        become risky if its model file is replaced, dataset files are corrupted,
        preprocessing is not reproducible or bundle metadata is missing.

        ## Typical findings

        - missing files
        - unreadable artifacts
        - incomplete metadata
        - risky model format
        - missing MONAI Bundle structure
        - reproducibility concerns

        ## Output

        Findings are written into JSON, Markdown, HTML and PDF reports. Each
        issue contains a severity level, scanner name, category, path and message.

        ## Recommended action

        Fix warnings and errors before using the project for research validation,
        publication or clinical translation planning.
        """)

    # Reports
    write_file(docs / "reports" / "overview.md", """
    # Reports Overview

    MONAI Security generates multiple report formats so that the same assessment
    can be used by different stakeholders.

    - JSON for automation and reproducibility
    - Markdown for version control and human review
    - HTML for local browser-based review
    - PDF for sharing and archival
    - summary text for quick terminal review
    """)

    write_file(docs / "reports" / "html_report.md", """
    # HTML Report

    The HTML report contains executive summary, issues, dependencies, model files,
    dataset metadata and MONAI transform review.

    It is intended for local interactive review in a browser.
    """)

    write_file(docs / "reports" / "pdf_report.md", """
    # PDF Report

    The PDF report is intended for:

    - documentation packages
    - internal review
    - research artifact storage
    - sharing with collaborators

    PDF generation requires `reportlab`.
    """)

    write_file(docs / "reports" / "json_csv.md", """
    # JSON and CSV Outputs

    JSON and CSV outputs are useful for reproducible research, benchmarking and
    automated processing.

    They can be used to compare projects, track improvements between versions or
    create tables for publications.
    """)

    write_file(docs / "reports" / "summary.md", """
    # Summary Report

    `summary.txt` provides a short overview with counts of dependencies, model
    files, dataset files, transforms and issues.
    """)

    # Clinical/security/developer/admin/tutorials/examples/API
    write_file(docs / "clinical" / "radiologist_guide.md", """
    # Radiologist Guide

    This guide explains the report from the perspective of radiologists and
    clinical researchers.

    The key question is not whether the model is diagnostically accurate, but
    whether the project is documented, traceable and safe enough for controlled
    research validation.

    ## What to check first

    - Are there critical or error-level findings?
    - Is the model file identified and hashed?
    - Is dataset metadata readable?
    - Is the MONAI Bundle structure complete?
    - Are recommendations clear?

    MONAI Security should be treated as an aid to review, not as a clinical
    approval tool.
    """)

    write_file(docs / "clinical" / "clinical_readiness.md", """
    # Clinical Readiness

    Clinical readiness is affected by documentation, provenance, reproducibility
    and security posture.

    A project with missing metadata, untrusted model files or corrupted dataset
    records should not be used for clinical decision support.
    """)

    security_pages = {
        "threat_model": "Threat Model",
        "supply_chain": "Software Supply Chain Security",
        "model_integrity": "Model Integrity",
        "dataset_integrity": "Dataset Integrity",
        "reproducibility": "Reproducibility",
    }

    for filename, title in security_pages.items():
        write_file(docs / "security" / f"{filename}.md", f"""
        # {title}

        MONAI Security addresses practical risks that can appear in medical AI
        projects before deployment.

        ## Examples

        - model file replacement
        - corrupted medical image files
        - missing dataset provenance
        - unpinned dependencies
        - incomplete MONAI Bundle metadata
        - non-deterministic preprocessing transforms

        ## Defensive approach

        The module is read-only and focuses on detection, documentation and
        reporting.
        """)

    write_file(docs / "developer" / "developer_guide.md", """
    # Developer Guide

    Developers can extend MONAI Security by adding scanners, report sections or
    new output formats.

    ## Scanner design principles

    - read-only
    - deterministic where possible
    - JSON-serializable outputs
    - clear severity levels
    - clinical and technical explanations
    """)

    write_file(docs / "developer" / "extending_scanners.md", """
    # Extending Scanners

    A scanner should inspect one specific area of the project and add structured
    findings.

    Example scanner responsibilities:

    - inspect files
    - collect metadata
    - add warnings or errors
    - write structured output to the final report
    """)

    write_file(docs / "administrator" / "administrator_guide.md", """
    # Administrator Guide

    Administrators should use MONAI Security to support internal review of
    research AI artifacts.

    ## Recommendations

    - keep reports with experiment artifacts
    - archive JSON reports
    - review dataset side files for patient identifiers
    - avoid loading untrusted checkpoints
    - keep environments reproducible
    """)

    write_file(docs / "tutorials" / "first_security_assessment.md", """
    # Tutorial: First Security Assessment

    ```powershell
    python monai_security.py security .\\monai_test --dataset .\\monoai_demo_projects\\ --model .\\monoai_demo_projects\\ --out monai_security_report
    ```

    Open:

    ```text
    monai_security_report\\monai_security_report.html
    ```
    """)

    write_file(docs / "tutorials" / "demo_project_assessment.md", """
    # Tutorial: Demo Project Assessment

    Demo projects are useful for learning how different findings appear in the
    reports. Run the assessment against clean and intentionally problematic
    examples, then compare the HTML and PDF reports.
    """)

    write_file(docs / "tutorials" / "batch_assessment.md", """
    # Tutorial: Batch Assessment

    ```powershell
    Get-ChildItem .\\projects -Directory | ForEach-Object {
        python monai_security.py security $_.FullName --out ("reports\\" + $_.Name)
    }
    ```
    """)

    write_file(docs / "examples" / "index.md", """
    # Examples

    Suggested examples:

    - brain MRI segmentation project
    - lung CT project
    - liver CT project
    - MONAI Bundle project
    - corrupted dataset project
    - missing metadata project
    - batch assessment workflow
    """)

    write_file(docs / "api" / "index.md", """
    # API Reference

    If `monai_security.py` is available in the documentation root, autodoc can be
    enabled for API extraction.

    ```{eval-rst}
    .. automodule:: monai_security
       :members:
       :undoc-members:
       :show-inheritance:
    ```
    """)

    write_file(root / "examples" / "run_first_assessment.py", """
    from pathlib import Path
    import subprocess
    import sys

    project = Path(".")
    subprocess.run([
        sys.executable,
        "monai_security.py",
        "security",
        str(project),
        "--out",
        "monai_security_report",
    ], check=False)
    """)

    print(f"Documentation portal generated: {root.resolve()}")
    print("Build command:")
    print("  cd monai_security_docs/docs")
    print("  pip install -r requirements.txt")
    print("  python -m sphinx -b html . _build/html")


if __name__ == "__main__":
    main()

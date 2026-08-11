"""
monoai_audit.py

Defensive cybersecurity and integrity module for MONAI-based medical AI projects.

Modules:
1. Dependency scanner
2. Model file scanner
3. Dataset metadata scanner
4. MONAI transform scanner
5. Markdown / JSON report generator

Usage examples:

    python monai_security.py security . --dataset data --out monai_security_report

    python monai_security.py security . --dataset data --model model.pt --out monai_security_report

    python monai_security.py security . --dataset data --model models --out monai_security_report

This module is defensive only. It does not exploit, modify, or attack systems.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import importlib.metadata
import json
import os
import platform
import re
import subprocess
import sys
from html import escape
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
except Exception:
    A4 = None
    colors = None
    getSampleStyleSheet = None
    ParagraphStyle = None
    cm = None
    SimpleDocTemplate = None
    Paragraph = None
    Spacer = None
    Table = None
    TableStyle = None
    PageBreak = None


try:
    import nibabel as nib
except Exception:
    nib = None

try:
    import torch
except Exception:
    torch = None


# =========================================================
# Data structures
# =========================================================

@dataclass
class AuditIssue:
    level: str
    scanner: str
    category: str
    path: str
    message: str
    recommendation: str = ""


@dataclass
class DependencyRecord:
    name: str
    version: str
    source: str = "python_environment"


@dataclass
class ModelFileRecord:
    path: str
    size_bytes: int
    sha256: str
    extension: str
    risk_notes: List[str] = field(default_factory=list)


@dataclass
class DatasetFileRecord:
    path: str
    size_bytes: int
    sha256: str
    extension: str
    shape: Optional[Tuple[int, ...]] = None
    dtype: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    unique_values: Optional[List[float]] = None
    affine_det: Optional[float] = None


@dataclass
class TransformRecord:
    file: str
    line: int
    transform_name: str
    keys: Optional[List[str]] = None
    risk_notes: List[str] = field(default_factory=list)


# =========================================================
# Utility helpers
# =========================================================

def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def safe_rel(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except Exception:
        return str(path)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def read_text_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def iter_project_files(root: Path, suffixes: Tuple[str, ...]) -> List[Path]:
    ignored_dirs = {
        ".git", ".venv", "venv", "__pycache__", ".pytest_cache",
        "node_modules", "audit_report", "monoai_audit_report", "monai_audit_report", "monai_security_report"
    }
    files = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in ignored_dirs for part in p.parts):
            continue
        if str(p).lower().endswith(suffixes):
            files.append(p)
    return files



def find_model_files(root: Path) -> List[Path]:
    """Find recognized model files under a file or directory."""
    model_exts = (".pt", ".pth", ".ckpt", ".onnx", ".ts", ".torchscript", ".safetensors")
    if not root.exists():
        return []
    if root.is_file():
        return [root] if str(root).lower().endswith(model_exts) else []
    candidates: List[Path] = []
    for suffix in ("*.pt", "*.pth", "*.ckpt", "*.onnx", "*.ts", "*.torchscript", "*.safetensors"):
        candidates.extend(root.rglob(suffix))
    return [p for p in candidates if "monoai_audit_report" not in p.parts and "monai_security_report" not in p.parts]


def guess_dataset_root(project_root: Path) -> Optional[Path]:
    """Guess common dataset folders inside a MONAI project."""
    for name in ("data", "dataset", "datasets", "images"):
        candidate = project_root / name
        if candidate.exists() and candidate.is_dir():
            return candidate
    return None


def guess_model_path(project_root: Path) -> Optional[Path]:
    """Guess common model locations inside a MONAI project."""
    model_dir = project_root / "models"
    if model_dir.exists() and model_dir.is_dir():
        return model_dir
    models = find_model_files(project_root)
    return models[0] if models else None


# =========================================================
# Main auditor
# =========================================================

class MonaiSecurityAuditor:
    def __init__(
        self,
        project_root: str | Path,
        dataset_root: Optional[str | Path] = None,
        model_path: Optional[str | Path] = None,
        output_dir: str | Path = "monai_security_report",
    ):
        self.project_root = Path(project_root).resolve()
        self.dataset_root = Path(dataset_root).resolve() if dataset_root else guess_dataset_root(self.project_root)
        self.model_path = Path(model_path).resolve() if model_path else guess_model_path(self.project_root)
        self.output_dir = Path(output_dir).resolve()

        self.issues: List[AuditIssue] = []
        self.dependencies: List[DependencyRecord] = []
        self.model_files: List[ModelFileRecord] = []
        self.dataset_files: List[DatasetFileRecord] = []
        self.transforms: List[TransformRecord] = []

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def add_issue(
        self,
        level: str,
        scanner: str,
        category: str,
        path: str | Path,
        message: str,
        recommendation: str = "",
    ) -> None:
        self.issues.append(
            AuditIssue(
                level=level,
                scanner=scanner,
                category=category,
                path=str(path),
                message=message,
                recommendation=recommendation,
            )
        )

    # =====================================================
    # 1. Dependency scanner
    # =====================================================

    def scan_dependencies(self) -> None:
        scanner = "dependency_scanner"

        required = [
            "monai",
            "torch",
            "numpy",
            "nibabel",
            "scipy",
            "pydicom",
            "matplotlib",
        ]

        for name in required:
            try:
                version = importlib.metadata.version(name)
                self.dependencies.append(DependencyRecord(name=name, version=version))
            except importlib.metadata.PackageNotFoundError:
                self.add_issue(
                    "WARNING",
                    scanner,
                    "missing_dependency",
                    name,
                    f"Dependency not found: {name}",
                    "Install it if this project requires that feature.",
                )

        # Capture full pip freeze if available
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "freeze"],
                capture_output=True,
                text=True,
                timeout=20,
            )
            if result.returncode == 0:
                freeze_path = self.output_dir / "pip_freeze.txt"
                freeze_path.write_text(result.stdout, encoding="utf-8")
        except Exception as e:
            self.add_issue(
                "INFO",
                scanner,
                "pip_freeze",
                self.project_root,
                f"Could not capture pip freeze: {e}",
            )

        # Flag risky or unstable dependency patterns from requirements files
        req_files = list(self.project_root.glob("requirements*.txt")) + list(self.project_root.glob("*.lock"))
        for req in req_files:
            content = read_text_safe(req)
            for line_no, line in enumerate(content.splitlines(), start=1):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue

                if "git+" in stripped or "http://" in stripped or "https://" in stripped:
                    self.add_issue(
                        "WARNING",
                        scanner,
                        "remote_dependency",
                        f"{req}:{line_no}",
                        f"Remote dependency reference found: {stripped}",
                        "Pin trusted versions and verify source integrity.",
                    )

                if "==" not in stripped and not stripped.startswith(("-r", "--")) and not any(x in stripped for x in [">=", "<=", "~="]):
                    self.add_issue(
                        "INFO",
                        scanner,
                        "unpinned_dependency",
                        f"{req}:{line_no}",
                        f"Dependency may be unpinned: {stripped}",
                        "Pin versions for reproducible medical AI pipelines.",
                    )

        self._write_dependency_report()

    def _write_dependency_report(self) -> None:
        write_json(
            self.output_dir / "dependencies.json",
            [asdict(x) for x in self.dependencies],
        )

    # =====================================================
    # 2. Model file scanner
    # =====================================================

    def scan_model_files(self) -> None:
        scanner = "model_file_scanner"

        if self.model_path is None:
            candidates = find_model_files(self.project_root)
        elif self.model_path.is_dir():
            candidates = find_model_files(self.model_path)
        else:
            candidates = [self.model_path]

        if not candidates:
            self.add_issue(
                "INFO",
                scanner,
                "no_model_files",
                self.model_path or self.project_root,
                "No model files found.",
            )
            return

        for path in candidates:
            if not path.exists():
                self.add_issue(
                    "ERROR",
                    scanner,
                    "missing_model_file",
                    path,
                    "Model file does not exist.",
                )
                continue

            try:
                digest = sha256_file(path)
                size = path.stat().st_size
                ext = "".join(path.suffixes).lower()
            except Exception as e:
                self.add_issue(
                    "ERROR",
                    scanner,
                    "model_hash",
                    path,
                    f"Could not hash model file: {e}",
                )
                continue

            notes = []

            if ext in (".pt", ".pth", ".ckpt"):
                notes.append("PyTorch pickle-based formats can execute code when loaded unsafely.")
                self.add_issue(
                    "WARNING",
                    scanner,
                    "pickle_model_format",
                    path,
                    "Model uses a pickle-based PyTorch format.",
                    "Prefer state_dict-only checkpoints, signed artifacts, or safetensors/ONNX where appropriate.",
                )

            if size > 2_000_000_000:
                notes.append("Very large model file.")
                self.add_issue(
                    "INFO",
                    scanner,
                    "large_model_file",
                    path,
                    f"Large model file: {size} bytes.",
                    "Confirm provenance and storage integrity.",
                )

            self.model_files.append(
                ModelFileRecord(
                    path=str(path),
                    size_bytes=size,
                    sha256=digest,
                    extension=ext,
                    risk_notes=notes,
                )
            )

        write_json(
            self.output_dir / "model_files.json",
            [asdict(x) for x in self.model_files],
        )

    # =====================================================
    # 3. Dataset metadata scanner
    # =====================================================

    def scan_dataset_metadata(self) -> None:
        scanner = "dataset_metadata_scanner"

        if self.dataset_root is None:
            self.add_issue(
                "INFO",
                scanner,
                "no_dataset_root",
                self.project_root,
                "No dataset root provided.",
                "Use --dataset <path> to audit NIfTI dataset metadata.",
            )
            return

        if not self.dataset_root.exists():
            self.add_issue(
                "ERROR",
                scanner,
                "missing_dataset_root",
                self.dataset_root,
                "Dataset root does not exist.",
            )
            return

        files = [p for p in self.dataset_root.rglob("*") if p.is_file()]
        if not files:
            self.add_issue(
                "WARNING",
                scanner,
                "empty_dataset",
                self.dataset_root,
                "Dataset folder contains no files.",
            )
            return

        seen_hashes: Dict[str, str] = {}

        for path in files:
            try:
                digest = sha256_file(path)
                size = path.stat().st_size
                ext = "".join(path.suffixes).lower()
            except Exception as e:
                self.add_issue(
                    "ERROR",
                    scanner,
                    "file_hash",
                    path,
                    f"Could not hash dataset file: {e}",
                )
                continue

            if size == 0:
                self.add_issue(
                    "ERROR",
                    scanner,
                    "empty_file",
                    path,
                    "Dataset file is empty.",
                )

            if digest in seen_hashes:
                self.add_issue(
                    "WARNING",
                    scanner,
                    "duplicate_dataset_file",
                    path,
                    f"Duplicate file content detected. Same as: {seen_hashes[digest]}",
                )
            else:
                seen_hashes[digest] = str(path)

            record = DatasetFileRecord(
                path=str(path),
                size_bytes=size,
                sha256=digest,
                extension=ext,
            )

            if str(path).lower().endswith((".nii", ".nii.gz")):
                self._inspect_nifti_metadata(path, record)

            self.dataset_files.append(record)

        self._audit_image_mask_shapes()
        write_json(
            self.output_dir / "dataset_metadata.json",
            [asdict(x) for x in self.dataset_files],
        )

    def _inspect_nifti_metadata(self, path: Path, record: DatasetFileRecord) -> None:
        scanner = "dataset_metadata_scanner"

        if nib is None:
            self.add_issue(
                "ERROR",
                scanner,
                "missing_nibabel",
                path,
                "Cannot inspect NIfTI because nibabel is not installed.",
            )
            return

        try:
            img = nib.load(str(path))
            data = img.get_fdata(dtype=np.float32)
        except Exception as e:
            self.add_issue(
                "ERROR",
                scanner,
                "nifti_load_error",
                path,
                f"Could not load NIfTI file: {e}",
            )
            return

        record.shape = tuple(int(x) for x in data.shape)
        record.dtype = str(data.dtype)
        record.min_value = float(np.nanmin(data))
        record.max_value = float(np.nanmax(data))

        if np.isnan(data).any():
            self.add_issue("ERROR", scanner, "nan_values", path, "NIfTI contains NaN values.")
        if np.isinf(data).any():
            self.add_issue("ERROR", scanner, "inf_values", path, "NIfTI contains Inf values.")
        if record.min_value == record.max_value:
            self.add_issue("WARNING", scanner, "constant_image", path, "Image has constant intensity.")

        try:
            record.affine_det = float(np.linalg.det(img.affine[:3, :3]))
            if abs(record.affine_det) < 1e-8:
                self.add_issue(
                    "WARNING",
                    scanner,
                    "degenerate_affine",
                    path,
                    "Affine matrix appears degenerate.",
                )
        except Exception:
            self.add_issue(
                "WARNING",
                scanner,
                "affine_inspection",
                path,
                "Could not inspect affine matrix.",
            )

        lower = path.name.lower()
        looks_like_mask = any(x in lower for x in ["mask", "label", "seg", "tumor"])
        if looks_like_mask:
            unique = np.unique(data)
            if len(unique) <= 64:
                record.unique_values = [float(x) for x in unique.tolist()]
            else:
                self.add_issue(
                    "WARNING",
                    scanner,
                    "mask_unique_values",
                    path,
                    f"Mask-like file has many unique values: {len(unique)}",
                    "Segmentation masks should usually contain discrete class IDs.",
                )

    def _audit_image_mask_shapes(self) -> None:
        scanner = "dataset_metadata_scanner"

        by_name = {Path(x.path).name: x for x in self.dataset_files if x.shape is not None}

        for rec in self.dataset_files:
            if rec.shape is None:
                continue

            path = Path(rec.path)
            lower = path.name.lower()

            if any(t in lower for t in ["mask", "label", "seg"]):
                continue

            candidates = []
            if path.name.endswith(".nii.gz"):
                stem = path.name[:-7]
                candidates.extend([
                    stem + "_mask.nii.gz",
                    stem + "_label.nii.gz",
                    stem + "_seg.nii.gz",
                    stem.replace("image", "label") + ".nii.gz",
                ])
            elif path.name.endswith(".nii"):
                stem = path.name[:-4]
                candidates.extend([
                    stem + "_mask.nii",
                    stem + "_label.nii",
                    stem + "_seg.nii",
                    stem.replace("image", "label") + ".nii",
                ])

            for candidate in candidates:
                if candidate in by_name:
                    mask_rec = by_name[candidate]
                    if tuple(rec.shape[:3]) != tuple(mask_rec.shape[:3]):
                        self.add_issue(
                            "ERROR",
                            scanner,
                            "image_mask_shape_mismatch",
                            path,
                            f"Image and mask shapes differ: image={rec.shape}, mask={mask_rec.shape}",
                        )
                    break

    # =====================================================
    # 4. MONAI transform scanner
    # =====================================================

    def scan_monai_transforms(self) -> None:
        scanner = "monai_transform_scanner"

        py_files = iter_project_files(self.project_root, (".py",))

        monai_transform_names = {
            "LoadImaged",
            "LoadImageD",
            "EnsureChannelFirstd",
            "ScaleIntensityd",
            "Spacingd",
            "Orientationd",
            "RandFlipd",
            "RandRotate90d",
            "RandAffined",
            "RandGaussianNoised",
            "RandAdjustContrastd",
            "NormalizeIntensityd",
            "CropForegroundd",
            "RandCropByPosNegLabeld",
            "ToTensord",
            "EnsureTyped",
            "EnsureType",
        }

        for py_file in py_files:
            text = read_text_safe(py_file)
            if "monai" not in text.lower() and "LoadImaged" not in text:
                continue

            try:
                tree = ast.parse(text)
            except Exception as e:
                self.add_issue(
                    "WARNING",
                    scanner,
                    "python_parse_error",
                    py_file,
                    f"Could not parse Python file: {e}",
                )
                continue

            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    name = self._call_name(node.func)
                    if name in monai_transform_names:
                        keys = self._extract_keys_kwarg(node)
                        notes = self._risk_notes_for_transform(name, node)

                        self.transforms.append(
                            TransformRecord(
                                file=str(py_file),
                                line=getattr(node, "lineno", 0),
                                transform_name=name,
                                keys=keys,
                                risk_notes=notes,
                            )
                        )

                        for note in notes:
                            self.add_issue(
                                "INFO",
                                scanner,
                                "transform_review",
                                f"{py_file}:{getattr(node, 'lineno', 0)}",
                                f"{name}: {note}",
                            )

        if not self.transforms:
            self.add_issue(
                "INFO",
                scanner,
                "no_transforms_found",
                self.project_root,
                "No MONAI dictionary transforms detected in project Python files.",
            )

        write_json(
            self.output_dir / "monai_transforms.json",
            [asdict(x) for x in self.transforms],
        )

    def _call_name(self, func: ast.AST) -> str:
        if isinstance(func, ast.Name):
            return func.id
        if isinstance(func, ast.Attribute):
            return func.attr
        return ""

    def _extract_keys_kwarg(self, node: ast.Call) -> Optional[List[str]]:
        for kw in node.keywords:
            if kw.arg == "keys":
                if isinstance(kw.value, ast.List):
                    keys = []
                    for elt in kw.value.elts:
                        if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                            keys.append(elt.value)
                    return keys
                if isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
                    return [kw.value.value]
        return None

    def _risk_notes_for_transform(self, name: str, node: ast.Call) -> List[str]:
        notes = []

        if name == "LoadImaged":
            notes.append("Verify file paths are controlled and not user-supplied without validation.")

        if name in {"RandAffined", "RandGaussianNoised", "RandAdjustContrastd"}:
            notes.append("Random transform affects reproducibility. Set deterministic seed for audits and regulated experiments.")

        if name == "Spacingd":
            notes.append("Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.")

        if name == "Orientationd":
            notes.append("Orientation changes coordinate convention. Confirm image and label transforms are synchronized.")

        if name == "NormalizeIntensityd":
            notes.append("Normalization may hide abnormal intensity ranges. Audit raw intensity statistics separately.")

        if name == "CropForegroundd":
            notes.append("Cropping can remove context. Confirm crop source key and margin settings.")

        return notes


    # =====================================================
    # 5. MONAI Bundle security scanner
    # =====================================================

    def scan_monai_bundle(self) -> None:
        scanner = "monai_bundle_security_scanner"

        candidates: List[Path] = []
        for p in self.project_root.rglob("*"):
            if not p.is_dir():
                continue
            if any(part in {"monoai_audit_report", "monai_audit_report", "monai_security_report"} for part in p.parts):
                continue

            has_configs = (p / "configs").exists() or any(x.suffix.lower() in {".json", ".yaml", ".yml"} for x in p.glob("*"))
            has_docs = (p / "docs").exists() or (p / "README.md").exists()
            has_models = (p / "models").exists() or bool(find_model_files(p))

            if has_configs and (has_docs or has_models):
                candidates.append(p)

        if not candidates:
            self.add_issue(
                "WARNING",
                scanner,
                "no_bundle_found",
                self.project_root,
                "No MONAI Bundle-like structure detected.",
                "Add bundle/configs, bundle/docs, metadata files, and model artifacts.",
            )
            return

        bundle = candidates[0]
        metadata_files = list(bundle.rglob("*metadata*.json")) + list(bundle.rglob("*metadata*.yaml")) + list(bundle.rglob("*metadata*.yml"))
        config_files = list(bundle.rglob("*.json")) + list(bundle.rglob("*.yaml")) + list(bundle.rglob("*.yml"))
        doc_files = list(bundle.rglob("README*")) + list(bundle.rglob("*.md"))
        model_files = find_model_files(bundle)

        if not metadata_files:
            self.add_issue(
                "WARNING",
                scanner,
                "bundle_metadata_missing",
                bundle,
                "MONAI Bundle-like folder found, but metadata is missing.",
                "Add metadata describing intended use, data provenance, limitations, and validation status.",
            )

        if not config_files:
            self.add_issue(
                "WARNING",
                scanner,
                "bundle_config_missing",
                bundle,
                "MONAI Bundle-like folder found, but config files are missing.",
                "Add inference/training configuration files.",
            )

        if not doc_files:
            self.add_issue(
                "WARNING",
                scanner,
                "bundle_docs_missing",
                bundle,
                "MONAI Bundle-like folder found, but documentation is missing.",
                "Add README.md or docs/ with usage, limitations, and validation notes.",
            )

        if not model_files:
            self.add_issue(
                "WARNING",
                scanner,
                "bundle_model_missing",
                bundle,
                "MONAI Bundle-like folder found, but no model artifact was found.",
                "Add model artifacts under bundle/models or provide --model.",
            )


    # =====================================================
    # 5. Report generator
    # =====================================================


    def _build_html_report(self, payload: Dict[str, Any]) -> str:
        counts: Dict[str, int] = {}
        for issue in self.issues:
            counts[issue.level] = counts.get(issue.level, 0) + 1

        issue_rows = []
        for issue in payload["issues"]:
            issue_rows.append(
                "<tr>"
                f"<td class='{escape(issue['level'])}'>{escape(issue['level'])}</td>"
                f"<td>{escape(issue['scanner'])}</td>"
                f"<td>{escape(issue['category'])}</td>"
                f"<td><code>{escape(str(issue['path']))}</code></td>"
                f"<td>{escape(issue['message'])}</td>"
                f"<td>{escape(issue.get('recommendation', ''))}</td>"
                "</tr>"
            )

        dep_rows = []
        for dep in payload["dependencies"]:
            dep_rows.append(
                f"<tr><td>{escape(dep['name'])}</td><td>{escape(dep['version'])}</td></tr>"
            )

        model_rows = []
        for rec in payload["model_files"]:
            notes = "; ".join(rec.get("risk_notes", []))
            model_rows.append(
                "<tr>"
                f"<td><code>{escape(rec['path'])}</code></td>"
                f"<td>{rec['size_bytes']}</td>"
                f"<td><code>{escape(rec['sha256'][:24])}...</code></td>"
                f"<td>{escape(notes)}</td>"
                "</tr>"
            )

        dataset_rows = []
        for rec in payload["dataset_files"][:200]:
            dataset_rows.append(
                "<tr>"
                f"<td><code>{escape(rec['path'])}</code></td>"
                f"<td>{escape(str(rec.get('shape')))}</td>"
                f"<td>{escape(str(rec.get('min_value')))}</td>"
                f"<td>{escape(str(rec.get('max_value')))}</td>"
                f"<td><code>{escape(rec['sha256'][:24])}...</code></td>"
                "</tr>"
            )

        transform_rows = []
        for tr in payload["transforms"]:
            notes = "; ".join(tr.get("risk_notes", []))
            transform_rows.append(
                "<tr>"
                f"<td><code>{escape(tr['file'])}</code></td>"
                f"<td>{tr['line']}</td>"
                f"<td>{escape(tr['transform_name'])}</td>"
                f"<td>{escape(str(tr.get('keys')))}</td>"
                f"<td>{escape(notes)}</td>"
                "</tr>"
            )

        return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>MONAI Cybersecurity Security Report</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 32px; background: #f8fafc; color: #111827; }}
.card {{ background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 18px; margin: 16px 0; box-shadow: 0 1px 3px rgba(0,0,0,.05); }}
h1, h2 {{ color: #0f172a; }}
table {{ border-collapse: collapse; width: 100%; margin-top: 12px; }}
th, td {{ border: 1px solid #e5e7eb; padding: 8px; font-size: 13px; text-align: left; vertical-align: top; }}
th {{ background: #111827; color: white; }}
code {{ background: #f1f5f9; padding: 2px 4px; border-radius: 4px; }}
.ERROR, .CRITICAL {{ color: #b91c1c; font-weight: bold; }}
.WARNING {{ color: #b45309; font-weight: bold; }}
.INFO {{ color: #0369a1; font-weight: bold; }}
.metric {{ display: inline-block; background: #e0f2fe; color: #075985; padding: 10px 14px; border-radius: 10px; margin: 4px; font-weight: bold; }}
</style>
</head>
<body>
<h1>MONAI Cybersecurity Security Report</h1>

<div class="card">
<h2>Executive Summary</h2>
<div class="metric">Dependencies: {len(payload["dependencies"])}</div>
<div class="metric">Model files: {len(payload["model_files"])}</div>
<div class="metric">Dataset files: {len(payload["dataset_files"])}</div>
<div class="metric">Transforms: {len(payload["transforms"])}</div>
<div class="metric">Issues: {len(payload["issues"])}</div>
<p><b>Project:</b> <code>{escape(payload["project_root"])}</code></p>
<p><b>Dataset:</b> <code>{escape(str(payload["dataset_root"]))}</code></p>
<p><b>Model:</b> <code>{escape(str(payload["model_path"]))}</code></p>
</div>

<div class="card">
<h2>Issues</h2>
<table>
<tr><th>Level</th><th>Scanner</th><th>Category</th><th>Path</th><th>Message</th><th>Recommendation</th></tr>
{''.join(issue_rows) if issue_rows else '<tr><td colspan="6">No issues found.</td></tr>'}
</table>
</div>

<div class="card">
<h2>Dependencies</h2>
<table><tr><th>Package</th><th>Version</th></tr>
{''.join(dep_rows) if dep_rows else '<tr><td colspan="2">No dependency records.</td></tr>'}
</table>
</div>

<div class="card">
<h2>Model Files</h2>
<table><tr><th>Path</th><th>Size</th><th>SHA256</th><th>Notes</th></tr>
{''.join(model_rows) if model_rows else '<tr><td colspan="4">No model files scanned.</td></tr>'}
</table>
</div>

<div class="card">
<h2>Dataset Metadata</h2>
<table><tr><th>Path</th><th>Shape</th><th>Min</th><th>Max</th><th>SHA256</th></tr>
{''.join(dataset_rows) if dataset_rows else '<tr><td colspan="5">No dataset files scanned.</td></tr>'}
</table>
</div>

<div class="card">
<h2>MONAI Transform Review</h2>
<table><tr><th>File</th><th>Line</th><th>Transform</th><th>Keys</th><th>Notes</th></tr>
{''.join(transform_rows) if transform_rows else '<tr><td colspan="5">No MONAI transforms detected.</td></tr>'}
</table>
</div>

</body>
</html>"""

    def _pdf_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawString(1.5 * cm, 1.0 * cm, "MONAI Cybersecurity Security Report")
        canvas.drawRightString(A4[0] - 1.5 * cm, 1.0 * cm, f"Page {doc.page}")
        canvas.restoreState()

    def _pdf_table(self, rows, widths=None):
        table = Table(rows, colWidths=widths, repeatRows=1 if len(rows) > 1 else 0)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#111827")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 7),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#d1d5db")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f9fafb")]),
        ]))
        return table

    def _short(self, value, max_len=80):
        text = str(value)
        return text if len(text) <= max_len else text[:max_len - 3] + "..."

    def _build_pdf_report(self, payload: Dict[str, Any], pdf_path: Path) -> bool:
        if SimpleDocTemplate is None:
            self.add_issue(
                "WARNING",
                "report_generator",
                "pdf_dependency_missing",
                pdf_path,
                "ReportLab is not installed. PDF report was not generated.",
                "Install with: pip install reportlab",
            )
            return False

        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        doc = SimpleDocTemplate(
            str(pdf_path),
            pagesize=A4,
            rightMargin=1.5 * cm,
            leftMargin=1.5 * cm,
            topMargin=1.5 * cm,
            bottomMargin=1.5 * cm,
        )

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name="SmallBody", parent=styles["BodyText"], fontSize=8, leading=10))

        story = []
        story.append(Paragraph("MONAI Cybersecurity Security Report", styles["Title"]))
        story.append(Spacer(1, 10))
        story.append(Paragraph("Executive Summary", styles["Heading2"]))

        summary_rows = [
            ["Metric", "Value"],
            ["Project root", self._short(payload["project_root"], 90)],
            ["Dataset root", self._short(payload["dataset_root"], 90)],
            ["Model path", self._short(payload["model_path"], 90)],
            ["Dependencies", len(payload["dependencies"])],
            ["Model files", len(payload["model_files"])],
            ["Dataset files", len(payload["dataset_files"])],
            ["MONAI transforms", len(payload["transforms"])],
            ["Issues", len(payload["issues"])],
        ]
        story.append(self._pdf_table(summary_rows, widths=[5 * cm, 11 * cm]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("Issues", styles["Heading2"]))
        issue_rows = [["Level", "Scanner", "Category", "Message"]]
        for issue in payload["issues"][:80]:
            issue_rows.append([
                issue["level"],
                self._short(issue["scanner"], 28),
                self._short(issue["category"], 28),
                self._short(issue["message"], 100),
            ])
        if len(issue_rows) == 1:
            issue_rows.append(["PASS", "-", "-", "No issues found."])
        story.append(self._pdf_table(issue_rows, widths=[2 * cm, 3.5 * cm, 3.5 * cm, 7 * cm]))

        story.append(PageBreak())

        story.append(Paragraph("Dependencies", styles["Heading2"]))
        dep_rows = [["Package", "Version"]]
        for dep in payload["dependencies"]:
            dep_rows.append([dep["name"], dep["version"]])
        if len(dep_rows) == 1:
            dep_rows.append(["No records", "-"])
        story.append(self._pdf_table(dep_rows, widths=[7 * cm, 7 * cm]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("Model Files", styles["Heading2"]))
        model_rows = [["Path", "Size", "SHA256", "Notes"]]
        for rec in payload["model_files"][:50]:
            model_rows.append([
                self._short(rec["path"], 50),
                str(rec["size_bytes"]),
                rec["sha256"][:16] + "...",
                self._short("; ".join(rec.get("risk_notes", [])), 60),
            ])
        if len(model_rows) == 1:
            model_rows.append(["No model files scanned", "-", "-", "-"])
        story.append(self._pdf_table(model_rows, widths=[5 * cm, 2 * cm, 3 * cm, 6 * cm]))

        story.append(PageBreak())

        story.append(Paragraph("Dataset Metadata", styles["Heading2"]))
        dataset_rows = [["Path", "Shape", "Min", "Max", "SHA256"]]
        for rec in payload["dataset_files"][:80]:
            dataset_rows.append([
                self._short(rec["path"], 45),
                self._short(rec.get("shape"), 24),
                self._short(rec.get("min_value"), 12),
                self._short(rec.get("max_value"), 12),
                rec["sha256"][:12] + "...",
            ])
        if len(dataset_rows) == 1:
            dataset_rows.append(["No dataset files scanned", "-", "-", "-", "-"])
        story.append(self._pdf_table(dataset_rows, widths=[5 * cm, 3 * cm, 2 * cm, 2 * cm, 4 * cm]))

        story.append(Spacer(1, 12))
        story.append(Paragraph("Defensive Notes", styles["Heading2"]))
        notes = [
            "Use checksum-verified datasets and model artifacts.",
            "Avoid loading untrusted pickle-based PyTorch checkpoints.",
            "Keep raw intensity and affine metadata in audit logs.",
            "Review MONAI preprocessing transforms before training or deployment.",
            "Keep JSON and CSV reports for reproducibility and publication support.",
        ]
        for note in notes:
            story.append(Paragraph("- " + note, styles["SmallBody"]))

        doc.build(story, onFirstPage=self._pdf_footer, onLaterPages=self._pdf_footer)
        return True


    def generate_reports(self) -> Dict[str, str]:
        payload = {
            "project_root": str(self.project_root),
            "dataset_root": str(self.dataset_root) if self.dataset_root else None,
            "model_path": str(self.model_path) if self.model_path else None,
            "environment": {
                "python": sys.version,
                "platform": platform.platform(),
            },
            "issues": [asdict(x) for x in self.issues],
            "dependencies": [asdict(x) for x in self.dependencies],
            "model_files": [asdict(x) for x in self.model_files],
            "dataset_files": [asdict(x) for x in self.dataset_files],
            "transforms": [asdict(x) for x in self.transforms],
        }

        json_path = self.output_dir / "monai_security_report.json"
        write_json(json_path, payload)

        md_path = self.output_dir / "monai_security_report.md"
        md_path.write_text(self._build_markdown_report(payload), encoding="utf-8")

        html_path = self.output_dir / "monai_security_report.html"
        html_path.write_text(self._build_html_report(payload), encoding="utf-8")

        pdf_path = self.output_dir / "monai_security_report.pdf"
        pdf_ok = self._build_pdf_report(payload, pdf_path)

        summary_path = self.output_dir / "summary.txt"
        summary_path.write_text(self._build_text_summary(), encoding="utf-8")

        reports = {
            "json": str(json_path),
            "markdown": str(md_path),
            "html": str(html_path),
            "summary": str(summary_path),
        }

        if pdf_ok:
            reports["pdf"] = str(pdf_path)
        else:
            reports["pdf"] = "PDF not generated. Install reportlab: pip install reportlab"

        return reports

    def _build_text_summary(self) -> str:
        counts: Dict[str, int] = {}
        for issue in self.issues:
            counts[issue.level] = counts.get(issue.level, 0) + 1

        lines = [
            "MONAI Cybersecurity Summary",
            "====================",
            "",
            f"Project root: {self.project_root}",
            f"Dataset root: {self.dataset_root}",
            f"Model path: {self.model_path}",
            "",
            f"Dependencies: {len(self.dependencies)}",
            f"Model files: {len(self.model_files)}",
            f"Dataset files: {len(self.dataset_files)}",
            f"MONAI transforms: {len(self.transforms)}",
            f"Issues: {len(self.issues)}",
            "",
        ]

        for level in sorted(counts):
            lines.append(f"{level}: {counts[level]}")

        return "\n".join(lines) + "\n"

    def _build_markdown_report(self, payload: Dict[str, Any]) -> str:
        issues_by_level: Dict[str, List[Dict[str, Any]]] = {}
        for issue in payload["issues"]:
            issues_by_level.setdefault(issue["level"], []).append(issue)

        lines = []
        lines.append("# MONAI Cybersecurity Report")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append(f"- Project root: `{payload['project_root']}`")
        lines.append(f"- Dataset root: `{payload['dataset_root']}`")
        lines.append(f"- Model path: `{payload['model_path']}`")
        lines.append("")
        lines.append("## Executive Summary")
        lines.append("")
        lines.append(f"- Dependencies scanned: **{len(payload['dependencies'])}**")
        lines.append(f"- Model files scanned: **{len(payload['model_files'])}**")
        lines.append(f"- Dataset files scanned: **{len(payload['dataset_files'])}**")
        lines.append(f"- MONAI transforms detected: **{len(payload['transforms'])}**")
        lines.append(f"- Issues found: **{len(payload['issues'])}**")
        lines.append("")

        lines.append("## Issues")
        lines.append("")
        if not payload["issues"]:
            lines.append("No issues found.")
            lines.append("")
        else:
            for level in ["CRITICAL", "ERROR", "WARNING", "INFO"]:
                group = issues_by_level.get(level, [])
                if not group:
                    continue
                lines.append(f"### {level}")
                lines.append("")
                for issue in group:
                    lines.append(f"- **{issue['scanner']} / {issue['category']}**")
                    lines.append(f"  - Path: `{issue['path']}`")
                    lines.append(f"  - Message: {issue['message']}")
                    if issue.get("recommendation"):
                        lines.append(f"  - Recommendation: {issue['recommendation']}")
                lines.append("")

        lines.append("## Dependencies")
        lines.append("")
        if payload["dependencies"]:
            lines.append("| Package | Version |")
            lines.append("|---|---|")
            for dep in payload["dependencies"]:
                lines.append(f"| `{dep['name']}` | `{dep['version']}` |")
        else:
            lines.append("No dependency records.")
        lines.append("")

        lines.append("## Model Files")
        lines.append("")
        if payload["model_files"]:
            lines.append("| Path | Size | SHA256 | Notes |")
            lines.append("|---|---:|---|---|")
            for rec in payload["model_files"]:
                notes = "; ".join(rec.get("risk_notes", []))
                lines.append(f"| `{rec['path']}` | {rec['size_bytes']} | `{rec['sha256'][:16]}...` | {notes} |")
        else:
            lines.append("No model files scanned.")
        lines.append("")

        lines.append("## Dataset Metadata")
        lines.append("")
        if payload["dataset_files"]:
            lines.append("| Path | Shape | Min | Max | SHA256 |")
            lines.append("|---|---|---:|---:|---|")
            for rec in payload["dataset_files"][:200]:
                lines.append(
                    f"| `{rec['path']}` | `{rec.get('shape')}` | "
                    f"{rec.get('min_value')} | {rec.get('max_value')} | `{rec['sha256'][:16]}...` |"
                )
            if len(payload["dataset_files"]) > 200:
                lines.append("")
                lines.append(f"Only first 200 dataset files shown. Full data is in JSON report.")
        else:
            lines.append("No dataset files scanned.")
        lines.append("")

        lines.append("## MONAI Transform Review")
        lines.append("")
        if payload["transforms"]:
            lines.append("| File | Line | Transform | Keys | Notes |")
            lines.append("|---|---:|---|---|---|")
            for tr in payload["transforms"]:
                notes = "; ".join(tr.get("risk_notes", []))
                lines.append(
                    f"| `{tr['file']}` | {tr['line']} | `{tr['transform_name']}` | "
                    f"`{tr.get('keys')}` | {notes} |"
                )
        else:
            lines.append("No MONAI transforms detected.")
        lines.append("")

        lines.append("## Defensive Notes")
        lines.append("")
        lines.append("- Use signed or checksum-verified datasets and model artifacts.")
        lines.append("- Avoid loading untrusted pickle-based PyTorch checkpoints.")
        lines.append("- Keep raw intensity and affine metadata in audit logs.")
        lines.append("- Run transform review before training and inference deployment.")
        lines.append("- Keep generated JSON reports under version control or artifact storage.")
        lines.append("")

        return "\n".join(lines)

    # =====================================================
    # Orchestration
    # =====================================================

    def run_all(self) -> Dict[str, str]:
        self.scan_dependencies()
        self.scan_model_files()
        self.scan_dataset_metadata()
        self.scan_monai_transforms()
        self.scan_monai_bundle()
        return self.generate_reports()



def main() -> None:
    parser = argparse.ArgumentParser(
        prog="monai_security",
        description="MONAI Security module for cybersecurity, integrity, and reproducibility assessment.",
    )

    subparsers = parser.add_subparsers(dest="command")

    security_parser = subparsers.add_parser(
        "security",
        help="Run MONAI security assessment.",
    )
    security_parser.add_argument("project", help="Project root folder.")
    security_parser.add_argument("--dataset", default=None, help="Dataset root folder.")
    security_parser.add_argument("--model", default=None, help="Model file or model folder.")
    security_parser.add_argument("--out", default="monai_security_report", help="Output report folder.")

    # Backward-compatible options:
    parser.add_argument("--project", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--dataset", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--model", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--out", default=None, help=argparse.SUPPRESS)

    args = parser.parse_args()

    if args.command == "security":
        project = args.project
        dataset = args.dataset
        model = args.model
        out = args.out
    else:
        project = args.project or "."
        dataset = args.dataset
        model = args.model
        out = args.out or "monai_security_report"

    auditor = MonaiSecurityAuditor(
        project_root=project,
        dataset_root=dataset,
        model_path=model,
        output_dir=out,
    )

    reports = auditor.run_all()

    print("MONAI security assessment finished.")
    for key, value in reports.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

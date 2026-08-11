
"""
monai_security_audit.py

Defensive security and integrity audit module for MONAI datasets.

Checks:
- dataset paths and file hashes
- empty / duplicate files
- NIfTI loading health
- NaN / Inf / constant intensity
- label-like files with too many unique values
- image-label shape consistency
- optional MONAI smoke test
- safe robustness artifact generation

This is defensive only.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

try:
    import nibabel as nib
except Exception:
    nib = None

try:
    import torch
except Exception:
    torch = None

try:
    from monai.transforms import Compose, LoadImaged, EnsureChannelFirstd, ScaleIntensityd
    from monai.data import Dataset, DataLoader
except Exception:
    Compose = None
    LoadImaged = None
    EnsureChannelFirstd = None
    ScaleIntensityd = None
    Dataset = None
    DataLoader = None


@dataclass
class SecurityIssue:
    level: str
    category: str
    path: str
    message: str


@dataclass
class FileRecord:
    path: str
    size_bytes: int
    sha256: str
    extension: str


@dataclass
class NiftiRecord:
    path: str
    shape: Tuple[int, ...]
    dtype: str
    min_value: float
    max_value: float
    unique_values: Optional[List[float]]
    affine_det: Optional[float]


class MonaiDatasetSecurityAuditor:
    def __init__(self, dataset_root, output_dir="monai_dataset_security_report", max_unique_label_values=32):
        self.dataset_root = Path(dataset_root).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.max_unique_label_values = max_unique_label_values
        self.issues: List[SecurityIssue] = []
        self.file_records: List[FileRecord] = []
        self.nifti_records: List[NiftiRecord] = []
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def add_issue(self, level, category, path, message):
        self.issues.append(SecurityIssue(level, category, str(path), message))

    def iter_files(self):
        if not self.dataset_root.exists():
            self.add_issue("CRITICAL", "dataset_root", self.dataset_root, "Dataset root does not exist.")
            return []
        if not self.dataset_root.is_dir():
            self.add_issue("CRITICAL", "dataset_root", self.dataset_root, "Dataset root is not a directory.")
            return []
        return [p for p in self.dataset_root.rglob("*") if p.is_file()]

    def is_safe_path(self, path):
        try:
            path.resolve().relative_to(self.dataset_root)
            return True
        except Exception:
            return False

    def sha256_file(self, path, chunk_size=1024 * 1024):
        h = hashlib.sha256()
        with Path(path).open("rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()

    def audit_files(self):
        seen_hashes: Dict[str, str] = {}
        for path in self.iter_files():
            if not self.is_safe_path(path):
                self.add_issue("CRITICAL", "path_traversal", path, "File resolves outside dataset root.")
                continue

            suffix = "".join(path.suffixes).lower()
            size = path.stat().st_size

            if size == 0:
                self.add_issue("ERROR", "empty_file", path, "File is empty.")

            try:
                digest = self.sha256_file(path)
            except Exception as e:
                self.add_issue("ERROR", "hashing", path, f"Could not hash file: {e}")
                continue

            self.file_records.append(FileRecord(str(path), size, digest, suffix))

            if digest in seen_hashes:
                self.add_issue("WARNING", "duplicate_file", path, f"Duplicate content. Same as: {seen_hashes[digest]}")
            else:
                seen_hashes[digest] = str(path)

    def audit_nifti_files(self):
        if nib is None:
            self.add_issue("ERROR", "dependency", "nibabel", "nibabel is not installed.")
            return

        files = [p for p in self.iter_files() if str(p).lower().endswith((".nii", ".nii.gz"))]
        if not files:
            self.add_issue("INFO", "nifti", self.dataset_root, "No NIfTI files found.")
            return

        for path in files:
            try:
                img = nib.load(str(path))
                data = img.get_fdata(dtype=np.float32)
            except Exception as e:
                self.add_issue("ERROR", "nifti_load", path, f"Could not load NIfTI: {e}")
                continue

            if data.ndim not in (3, 4):
                self.add_issue("WARNING", "shape", path, f"Unexpected dimensionality: {data.ndim}")

            if np.isnan(data).any():
                self.add_issue("ERROR", "nan", path, "Contains NaN values.")

            if np.isinf(data).any():
                self.add_issue("ERROR", "inf", path, "Contains infinite values.")

            min_value = float(np.nanmin(data))
            max_value = float(np.nanmax(data))

            if min_value == max_value:
                self.add_issue("WARNING", "intensity", path, "Constant intensity image.")

            affine_det = None
            try:
                affine_det = float(np.linalg.det(img.affine[:3, :3]))
                if abs(affine_det) < 1e-8:
                    self.add_issue("WARNING", "affine", path, "Degenerate affine matrix.")
            except Exception:
                self.add_issue("WARNING", "affine", path, "Could not inspect affine.")

            unique_values = None
            name = path.name.lower()
            looks_like_label = any(t in name for t in ("label", "seg", "mask", "tumor"))

            if looks_like_label:
                unique = np.unique(data)
                if len(unique) <= self.max_unique_label_values:
                    unique_values = [float(x) for x in unique.tolist()]
                else:
                    self.add_issue("WARNING", "label_values", path, f"Too many unique label values: {len(unique)}")

            self.nifti_records.append(
                NiftiRecord(
                    str(path),
                    tuple(int(x) for x in data.shape),
                    str(data.dtype),
                    min_value,
                    max_value,
                    unique_values,
                    affine_det,
                )
            )

    def audit_image_label_pairs(self):
        if not self.nifti_records:
            return

        records_by_name = {Path(r.path).name: r for r in self.nifti_records}

        for rec in self.nifti_records:
            path = Path(rec.path)
            lower = path.name.lower()

            if any(t in lower for t in ("label", "seg", "mask")):
                continue

            candidates = []
            if path.name.endswith(".nii.gz"):
                stem = path.name[:-7]
                candidates = [
                    stem + "_label.nii.gz",
                    stem + "_seg.nii.gz",
                    stem + "_mask.nii.gz",
                    stem.replace("image", "label") + ".nii.gz",
                ]
            elif path.name.endswith(".nii"):
                stem = path.name[:-4]
                candidates = [
                    stem + "_label.nii",
                    stem + "_seg.nii",
                    stem + "_mask.nii",
                    stem.replace("image", "label") + ".nii",
                ]

            for candidate in candidates:
                if candidate in records_by_name:
                    label_rec = records_by_name[candidate]
                    if tuple(rec.shape[:3]) != tuple(label_rec.shape[:3]):
                        self.add_issue(
                            "ERROR",
                            "image_label_shape",
                            path,
                            f"Shape mismatch: image={rec.shape}, label={label_rec.shape}",
                        )
                    break

    def monai_smoke_test(self, image_path):
        if Compose is None:
            self.add_issue("ERROR", "dependency", "MONAI", "MONAI is not available.")
            return False

        image_path = Path(image_path)
        if not image_path.exists():
            self.add_issue("ERROR", "smoke_test", image_path, "Image path does not exist.")
            return False

        try:
            data = [{"image": str(image_path)}]
            transforms = Compose([
                LoadImaged(keys=["image"]),
                EnsureChannelFirstd(keys=["image"]),
                ScaleIntensityd(keys=["image"]),
            ])
            ds = Dataset(data=data, transform=transforms)
            loader = DataLoader(ds, batch_size=1)
            for batch in loader:
                image = batch["image"]
                if torch is not None and torch.isnan(image).any():
                    self.add_issue("ERROR", "smoke_test", image_path, "Loaded tensor contains NaN.")
                    return False
                break
            self.add_issue("INFO", "smoke_test", image_path, "MONAI smoke test passed.")
            return True
        except Exception as e:
            self.add_issue("ERROR", "smoke_test", image_path, f"MONAI loading failed: {e}")
            return False

    def write_reports(self):
        paths = {}

        issues_path = self.output_dir / "issues.json"
        with issues_path.open("w", encoding="utf-8") as f:
            json.dump([asdict(x) for x in self.issues], f, indent=2, ensure_ascii=False)
        paths["issues_json"] = str(issues_path)

        files_path = self.output_dir / "files.csv"
        with files_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["path", "size_bytes", "sha256", "extension"])
            writer.writeheader()
            for rec in self.file_records:
                writer.writerow(asdict(rec))
        paths["files_csv"] = str(files_path)

        nifti_path = self.output_dir / "nifti_records.json"
        with nifti_path.open("w", encoding="utf-8") as f:
            json.dump([asdict(x) for x in self.nifti_records], f, indent=2, ensure_ascii=False)
        paths["nifti_json"] = str(nifti_path)

        summary_path = self.output_dir / "summary.txt"
        counts = {}
        for issue in self.issues:
            counts[issue.level] = counts.get(issue.level, 0) + 1

        with summary_path.open("w", encoding="utf-8") as f:
            f.write("MONAI Dataset Security Summary\\n")
            f.write("============================\\n\\n")
            f.write(f"Dataset root: {self.dataset_root}\\n")
            f.write(f"Files audited: {len(self.file_records)}\\n")
            f.write(f"NIfTI files audited: {len(self.nifti_records)}\\n")
            f.write(f"Issues total: {len(self.issues)}\\n\\n")
            for level, count in sorted(counts.items()):
                f.write(f"{level}: {count}\\n")
        paths["summary_txt"] = str(summary_path)

        return paths

    def run_full_audit(self):
        self.audit_files()
        self.audit_nifti_files()
        self.audit_image_label_pairs()
        return self.write_reports()



def main():
    parser = argparse.ArgumentParser(
        prog="monai_dataset_security",
        description="Defensive MONAI dataset security and integrity assessment.",
    )

    subparsers = parser.add_subparsers(dest="command")
    security_parser = subparsers.add_parser("security", help="Run dataset security assessment.")
    security_parser.add_argument("dataset", help="Dataset root folder.")
    security_parser.add_argument("--out", default="monai_dataset_security_report", help="Output report folder.")
    security_parser.add_argument("--smoke-test", default=None, help="Optional NIfTI path for MONAI loading smoke test.")

    # Backward-compatible options:
    parser.add_argument("--dataset", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--out", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--smoke-test", default=None, help=argparse.SUPPRESS)

    args = parser.parse_args()

    if args.command == "security":
        dataset = args.dataset
        out = args.out
        smoke_test = args.smoke_test
    else:
        if not args.dataset:
            parser.error("dataset is required. Use: python monai_dataset_security.py security <dataset> or --dataset <dataset>")
        dataset = args.dataset
        out = args.out or "monai_dataset_security_report"
        smoke_test = args.smoke_test

    auditor = MonaiDatasetSecurityAuditor(dataset, out)
    auditor.audit_files()
    auditor.audit_nifti_files()
    auditor.audit_image_label_pairs()

    if smoke_test:
        auditor.monai_smoke_test(smoke_test)

    reports = auditor.write_reports()
    print("MONAI dataset security assessment finished.")
    for k, v in reports.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()

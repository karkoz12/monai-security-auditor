# MonoAI AI Model Safety Check for Medical Imaging

## Radiologist View

**Model Safety Score:** 15/100

**Status:** Not ready

**Recommended action:** Do not use for clinical workflows. Complete remediation and rerun audit.

### Main issues

1. Model file does not exist.
2. Missing dataset provenance
3. Preprocessing pipeline needs reproducibility review
4. Preprocessing pipeline needs reproducibility review
5. Preprocessing pipeline needs reproducibility review

## Clinical Checklist

| Area | Item | Status | Recommendation |
|---|---|---|---|
| Model identity | Model artifact hash available | WARNING | Provide verified model artifacts and preserve SHA256 hashes. |
| Dataset provenance | Dataset folder available and scanned | WARNING | Provide dataset root and provenance documentation. |
| Dataset integrity | No critical dataset errors | FAIL | Fix corrupted files, NaN/Inf values, and image-mask mismatches. |
| MONAI Bundle | Bundle metadata and documentation available | PASS | Use MONAI Bundle-style metadata, configs, documentation, and model artifacts. |
| Pipeline reproducibility | MONAI transforms detected and reviewed | PASS | Document preprocessing, spacing, orientation, normalization, and random seeds. |
| Model loading safety | No pickle-based model risk flagged | PASS | Avoid untrusted PyTorch pickle checkpoints; prefer verified artifacts. |

## Scope

- Project root: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects`
- Dataset root: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\data`
- Model path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\models`

## Executive Summary

- Dependencies scanned: **7**
- Model files scanned: **0**
- Dataset files scanned: **0**
- MONAI transforms detected: **55**
- Issues found: **35**

## Issues

### ERROR

- **model_file_scanner / missing_model_file**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\models`
  - Message: Model file does not exist.
- **dataset_metadata_scanner / missing_dataset_root**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\data`
  - Message: Dataset root does not exist.

### INFO

- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\01_healthy_project\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\01_healthy_project\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\01_healthy_project\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\02_missing_model\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\02_missing_model\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\02_missing_model\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\03_missing_bundle\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\03_missing_bundle\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\03_missing_bundle\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\04_corrupted_dataset\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\04_corrupted_dataset\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\04_corrupted_dataset\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\05_wrong_labels\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\05_wrong_labels\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\05_wrong_labels\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\06_untrusted_pt_model\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\06_untrusted_pt_model\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\06_untrusted_pt_model\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\07_incomplete_metadata\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\07_incomplete_metadata\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\07_incomplete_metadata\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\08_research_prototype\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\08_research_prototype\train.py:9`
  - Message: RandAffined: Random transform affects reproducibility. Set deterministic seed for audits and regulated experiments.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\08_research_prototype\train.py:10`
  - Message: RandGaussianNoised: Random transform affects reproducibility. Set deterministic seed for audits and regulated experiments.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\09_clinical_candidate\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\09_clinical_candidate\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\09_clinical_candidate\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\10_bad_mask_values\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\10_bad_mask_values\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\10_bad_mask_values\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\11_nan_image\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\11_nan_image\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\11_nan_image\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.

## Dependencies

| Package | Version |
|---|---|
| `monai` | `1.5.2` |
| `torch` | `2.10.0` |
| `numpy` | `2.2.6` |
| `nibabel` | `5.4.2` |
| `scipy` | `1.15.3` |
| `pydicom` | `3.0.1` |
| `matplotlib` | `3.10.8` |

## Model Files

No model files scanned.

## Dataset Metadata

No dataset files scanned.

## MONAI Transform Review

| File | Line | Transform | Keys | Notes |
|---|---:|---|---|---|
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\01_healthy_project\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\01_healthy_project\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\01_healthy_project\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\01_healthy_project\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\01_healthy_project\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\02_missing_model\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\02_missing_model\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\02_missing_model\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\02_missing_model\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\02_missing_model\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\03_missing_bundle\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\03_missing_bundle\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\03_missing_bundle\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\03_missing_bundle\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\03_missing_bundle\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\04_corrupted_dataset\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\04_corrupted_dataset\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\04_corrupted_dataset\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\04_corrupted_dataset\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\04_corrupted_dataset\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\05_wrong_labels\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\05_wrong_labels\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\05_wrong_labels\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\05_wrong_labels\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\05_wrong_labels\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\06_untrusted_pt_model\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\06_untrusted_pt_model\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\06_untrusted_pt_model\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\06_untrusted_pt_model\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\06_untrusted_pt_model\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\07_incomplete_metadata\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\07_incomplete_metadata\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\07_incomplete_metadata\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\07_incomplete_metadata\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\07_incomplete_metadata\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\08_research_prototype\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\08_research_prototype\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\08_research_prototype\train.py` | 8 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\08_research_prototype\train.py` | 9 | `RandAffined` | `['image', 'label']` | Random transform affects reproducibility. Set deterministic seed for audits and regulated experiments. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\08_research_prototype\train.py` | 10 | `RandGaussianNoised` | `['image']` | Random transform affects reproducibility. Set deterministic seed for audits and regulated experiments. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\09_clinical_candidate\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\09_clinical_candidate\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\09_clinical_candidate\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\09_clinical_candidate\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\09_clinical_candidate\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\10_bad_mask_values\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\10_bad_mask_values\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\10_bad_mask_values\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\10_bad_mask_values\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\10_bad_mask_values\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\11_nan_image\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\11_nan_image\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\11_nan_image\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\11_nan_image\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monoai_demo_projects\11_nan_image\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |

## Defensive Notes

- Use signed or checksum-verified datasets and model artifacts.
- Avoid loading untrusted pickle-based PyTorch checkpoints.
- Keep raw intensity and affine metadata in audit logs.
- Run transform review before training and inference deployment.
- Keep generated JSON reports under version control or artifact storage.

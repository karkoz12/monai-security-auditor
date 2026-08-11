# MONAI Cybersecurity Report

## Scope

- Project root: `C:\Users\kozakka\monai_test\audit_cyber_monoai`
- Dataset root: `None`
- Model path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\models`

## Executive Summary

- Dependencies scanned: **7**
- Model files scanned: **1**
- Dataset files scanned: **0**
- MONAI transforms detected: **61**
- Issues found: **36**

## Issues

### INFO

- **dataset_metadata_scanner / no_dataset_root**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai`
  - Message: No dataset root provided.
  - Recommendation: Use --dataset <path> to audit NIfTI dataset metadata.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_dataset_security.py:267`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\01_healthy_project\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\01_healthy_project\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\01_healthy_project\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\02_missing_model\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\02_missing_model\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\02_missing_model\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\03_missing_bundle\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\03_missing_bundle\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\03_missing_bundle\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\04_corrupted_dataset\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\04_corrupted_dataset\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\04_corrupted_dataset\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\05_wrong_labels\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\05_wrong_labels\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\05_wrong_labels\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\06_untrusted_pt_model\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\06_untrusted_pt_model\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\06_untrusted_pt_model\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\07_incomplete_metadata\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\07_incomplete_metadata\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\07_incomplete_metadata\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\08_research_prototype\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\08_research_prototype\train.py:9`
  - Message: RandAffined: Random transform affects reproducibility. Set deterministic seed for audits and regulated experiments.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\08_research_prototype\train.py:10`
  - Message: RandGaussianNoised: Random transform affects reproducibility. Set deterministic seed for audits and regulated experiments.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\10_bad_mask_values\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\10_bad_mask_values\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\10_bad_mask_values\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\11_nan_image\train.py:6`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\11_nan_image\train.py:8`
  - Message: Orientationd: Orientation changes coordinate convention. Confirm image and label transforms are synchronized.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\11_nan_image\train.py:9`
  - Message: Spacingd: Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels.
- **monai_transform_scanner / transform_review**
  - Path: `C:\Users\kozakka\monai_test\audit_cyber_monoai\old_versions\monai_security_audit.py:267`
  - Message: LoadImaged: Verify file paths are controlled and not user-supplied without validation.

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

| Path | Size | SHA256 | Notes |
|---|---:|---|---|
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\models\brain_segmentation.safetensors` | 29 | `afc3f90840476f83...` |  |

## Dataset Metadata

No dataset files scanned.

## MONAI Transform Review

| File | Line | Transform | Keys | Notes |
|---|---:|---|---|---|
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_dataset_security.py` | 267 | `LoadImaged` | `['image']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_dataset_security.py` | 268 | `EnsureChannelFirstd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_dataset_security.py` | 269 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\01_healthy_project\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\01_healthy_project\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\01_healthy_project\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\01_healthy_project\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\01_healthy_project\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\02_missing_model\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\02_missing_model\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\02_missing_model\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\02_missing_model\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\02_missing_model\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\03_missing_bundle\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\03_missing_bundle\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\03_missing_bundle\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\03_missing_bundle\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\03_missing_bundle\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\04_corrupted_dataset\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\04_corrupted_dataset\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\04_corrupted_dataset\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\04_corrupted_dataset\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\04_corrupted_dataset\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\05_wrong_labels\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\05_wrong_labels\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\05_wrong_labels\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\05_wrong_labels\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\05_wrong_labels\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\06_untrusted_pt_model\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\06_untrusted_pt_model\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\06_untrusted_pt_model\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\06_untrusted_pt_model\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\06_untrusted_pt_model\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\07_incomplete_metadata\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\07_incomplete_metadata\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\07_incomplete_metadata\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\07_incomplete_metadata\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\07_incomplete_metadata\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\08_research_prototype\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\08_research_prototype\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\08_research_prototype\train.py` | 8 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\08_research_prototype\train.py` | 9 | `RandAffined` | `['image', 'label']` | Random transform affects reproducibility. Set deterministic seed for audits and regulated experiments. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\08_research_prototype\train.py` | 10 | `RandGaussianNoised` | `['image']` | Random transform affects reproducibility. Set deterministic seed for audits and regulated experiments. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\09_clinical_candidate\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\10_bad_mask_values\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\10_bad_mask_values\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\10_bad_mask_values\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\10_bad_mask_values\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\10_bad_mask_values\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\11_nan_image\train.py` | 6 | `LoadImaged` | `['image', 'label']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\11_nan_image\train.py` | 7 | `EnsureChannelFirstd` | `['image', 'label']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\11_nan_image\train.py` | 8 | `Orientationd` | `['image', 'label']` | Orientation changes coordinate convention. Confirm image and label transforms are synchronized. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\11_nan_image\train.py` | 9 | `Spacingd` | `['image', 'label']` | Spacing changes voxel geometry. Confirm spacing is logged and consistent with labels. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\monai_demo_projects\11_nan_image\train.py` | 10 | `ScaleIntensityd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\old_versions\monai_security_audit.py` | 267 | `LoadImaged` | `['image']` | Verify file paths are controlled and not user-supplied without validation. |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\old_versions\monai_security_audit.py` | 268 | `EnsureChannelFirstd` | `['image']` |  |
| `C:\Users\kozakka\monai_test\audit_cyber_monoai\old_versions\monai_security_audit.py` | 269 | `ScaleIntensityd` | `['image']` |  |

## Defensive Notes

- Use signed or checksum-verified datasets and model artifacts.
- Avoid loading untrusted pickle-based PyTorch checkpoints.
- Keep raw intensity and affine metadata in audit logs.
- Run transform review before training and inference deployment.
- Keep generated JSON reports under version control or artifact storage.
